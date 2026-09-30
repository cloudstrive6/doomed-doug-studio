"""Facebook + Instagram cross-posting (Meta Graph API), modelled on the InforMed publisher.

What goes out, only AFTER the video is public on YouTube (so the owner's review window covers Meta too):
  - each Short      -> Instagram Reel + Facebook Reel
  - each episode    -> native Facebook Page video (Instagram can't take 17-min videos)
Instagram fetches videos from a public URL: every episode's files are attached to a GitHub release (public repo).

Env: META_PAGE_ACCESS_TOKEN (never expires), META_PAGE_ID, META_IG_USER_ID; one-time: META_APP_ID,
META_APP_SECRET, META_USER_TOKEN for `python -m studio auth-meta`.
"""
from __future__ import annotations

import datetime as dt
import json
import os
import subprocess
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

from .config import ROOT, load_config, load_dotenv

V = os.environ.get("META_GRAPH_VERSION", "v23.0")
REPO = os.environ.get("GITHUB_REPOSITORY", "cloudstrive6/doomed-doug-studio")


def G(path: str) -> str:
    return f"https://graph.facebook.com/{V}/{path}"


def _req(url, data=None, method=None, headers=None, timeout=120):
    body = urllib.parse.urlencode(data).encode() if isinstance(data, dict) else data
    req = urllib.request.Request(url, data=body, method=method or ("POST" if body else "GET"), headers=headers or {})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read() or b"{}")
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"Meta API {e.code}: {e.read()[:500]!r}") from None


def _token():
    load_dotenv()
    return os.environ["META_PAGE_ACCESS_TOKEN"]


def post(path, params):
    return _req(G(path), {**params, "access_token": _token()})


# ------------------------------------------------------------------ one-time auth


def auth():
    """Short-lived user token -> never-expiring Page token + linked Instagram account. Saves to .env (and GitHub
    secrets with SAVE_SECRETS=1). Tokens are never printed."""
    load_dotenv()
    app_id, secret, short = (os.environ.get(k, "").strip() for k in ("META_APP_ID", "META_APP_SECRET", "META_USER_TOKEN"))
    if not (app_id and secret and short):
        raise SystemExit("Put META_APP_ID, META_APP_SECRET and META_USER_TOKEN in studio/.env first.")
    q = urllib.parse.urlencode({"grant_type": "fb_exchange_token", "client_id": app_id, "client_secret": secret,
                                "fb_exchange_token": short})
    long = _req(G(f"oauth/access_token?{q}"))["access_token"]
    pages = _req(G("me/accounts?fields=id,name,access_token,instagram_business_account{id,username}"
                   f"&access_token={long}")).get("data", [])
    for p in pages:
        print(f"  page: {p['name']} ({p['id']}) -> IG: {(p.get('instagram_business_account') or {}).get('username', 'none linked')}")
    page = next((p for p in pages if "doomed" in p["name"].lower()), None)
    if not page:
        raise SystemExit("No Page named like 'Doomed Doug' found for this login.")
    ig = page.get("instagram_business_account")
    dbg = _req(G(f"debug_token?input_token={page['access_token']}&access_token={app_id}|{secret}")).get("data", {})
    print("Page token expires:", "never" if not dbg.get("expires_at") else
          dt.datetime.fromtimestamp(dbg["expires_at"]).isoformat())
    vals = {"META_PAGE_ACCESS_TOKEN": page["access_token"], "META_PAGE_ID": page["id"]}
    if ig:
        vals["META_IG_USER_ID"] = ig["id"]
        print("Instagram linked:", "@" + ig.get("username", "?"))
    else:
        print("WARNING: no Instagram professional account linked to the Page (Page settings -> Linked accounts).")
    env = ROOT / ".env"
    lines = [l for l in env.read_text(encoding="utf-8").splitlines() if l.split("=", 1)[0] not in vals]
    lines += [f"{k}={v}" for k, v in vals.items()]
    env.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("Saved", ", ".join(vals), "to studio/.env")
    if os.environ.get("SAVE_SECRETS") == "1":
        for k, v in vals.items():
            subprocess.run(["gh", "secret", "set", k], input=v, text=True, check=True, cwd=ROOT)
        print("Saved them to GitHub secrets.")


# ------------------------------------------------------------------ media hosting (public URLs for Instagram)


PUBLIC_TAG = "public-media"


def release_assets(ep: Path) -> dict:
    """Store the episode's videos in a DRAFT GitHub release ep-<NNN> (not publicly downloadable). Each file is
    copied to the public release only when it is cross-posted, i.e. after it is live on YouTube."""
    tag = "ep-" + ep.name[:3]
    files = [p for p in [ep / "build" / "final.mp4", *sorted((ep / "build" / "shorts").glob("short*.mp4"))] if p.exists()]
    exists = subprocess.run(["gh", "release", "view", tag, "--repo", REPO], capture_output=True).returncode == 0
    if not exists:
        subprocess.run(["gh", "release", "create", tag, "--repo", REPO, "--draft", "--title", f"Episode {ep.name}",
                        "--notes", "Private media store for cross-posting.",
                        *map(str, files)], check=True)
    elif files:
        subprocess.run(["gh", "release", "upload", tag, "--repo", REPO, "--clobber", *map(str, files)], check=True)
    return {p.name: f"(draft) {tag}/{p.name}" for p in files}


def local_file(ep: Path, name: str) -> Path:
    """The episode's video locally; on a CI runner, fetched from the draft release."""
    f = (ep / "build" / name) if name == "final.mp4" else (ep / "build" / "shorts" / name)
    if not f.exists():
        f.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(["gh", "release", "download", "ep-" + ep.name[:3], "--repo", REPO, "--pattern", name,
                        "--dir", str(f.parent), "--clobber"], check=True)
    return f


def public_url(ep: Path, name: str) -> str:
    """Publish one file to the public release (only called once the video is live on YouTube)."""
    f = local_file(ep, name)
    pub = f.parent / f"{ep.name[:3]}-{name}"
    if not pub.exists():
        pub.write_bytes(f.read_bytes())
    if subprocess.run(["gh", "release", "view", PUBLIC_TAG, "--repo", REPO], capture_output=True).returncode != 0:
        subprocess.run(["gh", "release", "create", PUBLIC_TAG, "--repo", REPO, "--title", "Published media",
                        "--notes", "Videos already public on YouTube, hosted for Instagram/Facebook to fetch."], check=True)
    subprocess.run(["gh", "release", "upload", PUBLIC_TAG, "--repo", REPO, "--clobber", str(pub)], check=True)
    return f"https://github.com/{REPO}/releases/download/{PUBLIC_TAG}/{pub.name}"


# ------------------------------------------------------------------ publishing


def _wait_ig(container: str, minutes=20):
    until = time.time() + minutes * 60
    while time.time() < until:
        j = _req(G(f"{container}?fields=status_code,status&access_token={_token()}"))
        if j.get("status_code") == "FINISHED":
            return
        if j.get("status_code") in ("ERROR", "EXPIRED"):
            raise RuntimeError(f"IG container {container} {j.get('status_code')}: {j.get('status')}")
        time.sleep(10)
    raise RuntimeError(f"IG container {container} not ready after {minutes} min")


def instagram_reel(video_url: str, caption: str) -> dict:
    ig = os.environ["META_IG_USER_ID"]
    c = post(f"{ig}/media", {"media_type": "REELS", "video_url": video_url, "caption": caption, "share_to_feed": "true"})
    _wait_ig(c["id"])
    pid = post(f"{ig}/media_publish", {"creation_id": c["id"]})["id"]
    link = _req(G(f"{pid}?fields=permalink&access_token={_token()}")).get("permalink")
    return {"id": pid, "url": link}


def facebook_reel(file: Path, description: str) -> dict:
    page = os.environ["META_PAGE_ID"]
    start = post(f"{page}/video_reels", {"upload_phase": "start"})
    data = file.read_bytes()
    url = start.get("upload_url") or f"https://rupload.facebook.com/video-upload/{V}/{start['video_id']}"
    _req(url, data=data, method="POST", headers={"Authorization": f"OAuth {_token()}", "offset": "0",
                                                 "file_size": str(len(data))}, timeout=1800)
    post(f"{page}/video_reels", {"upload_phase": "finish", "video_id": start["video_id"], "video_state": "PUBLISHED",
                                 "description": description})
    return {"id": start["video_id"], "url": f"https://www.facebook.com/reel/{start['video_id']}"}


def facebook_video(video_url: str, title: str, description: str) -> dict:
    page = os.environ["META_PAGE_ID"]
    j = _req(f"https://graph-video.facebook.com/{V}/{page}/videos",
             {"file_url": video_url, "title": title, "description": description, "access_token": _token()}, timeout=600)
    return {"id": j["id"], "url": f"https://www.facebook.com/{page}/videos/{j['id']}"}


def _is_live(ts: str | None) -> bool:
    if not ts:
        return False
    return dt.datetime.fromisoformat(ts.replace("Z", "+00:00")) <= dt.datetime.now(dt.timezone.utc)


def _hashtags():
    return load_config().get("social", {}).get("hashtags", "#DoomedDoug #deepsea #ocean #science #animals")


def publish_due(dry_run: bool = False) -> list[str]:
    """Cross-post everything whose YouTube publish time has passed and hasn't gone to Meta yet."""
    load_dotenv()
    cfg = load_config().get("social", {})
    if not os.environ.get("META_PAGE_ACCESS_TOKEN"):
        print("Meta not configured (META_PAGE_ACCESS_TOKEN missing); nothing to do.")
        return []
    from . import notify
    done = []
    for ep in sorted((ROOT / "episodes").iterdir()):
        mp = ep / "metadata.json"
        if not mp.exists():
            continue
        meta = json.loads(mp.read_text(encoding="utf-8"))
        social = meta.setdefault("social", {})
        yt_url = f"https://youtu.be/{meta.get('youtube_id')}"
        # --- long episode -> Facebook Page video
        if cfg.get("facebook_long", True) and meta.get("youtube_id") and _is_live(meta.get("publish_at")) \
                and not social.get("facebook_video"):
            premise = meta["description"].split("\n\n")[0]
            desc = f"{premise}\n\nAlso on YouTube: {yt_url}\n\n{_hashtags()}"
            if dry_run:
                print("[dry] FB video:", meta["title"])
            else:
                try:
                    social["facebook_video"] = facebook_video(public_url(ep, "final.mp4"), meta["title"], desc)
                    done.append(f"FB video: {meta['title']} {social['facebook_video']['url']}")
                except Exception as e:
                    social["facebook_video_error"] = str(e)[:300]
                    notify.send(f"⚠️ Facebook video failed for {meta['title']}: {str(e)[:300]}")
                mp.write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")
        # --- Shorts -> Instagram Reel + Facebook Reel
        sp = ep / "shorts.json"
        if not sp.exists():
            continue
        shorts = json.loads(sp.read_text(encoding="utf-8"))
        for s in shorts["shorts"]:
            if not (s.get("youtube_id") and _is_live(s.get("publish_at"))):
                continue
            sm = s.setdefault("social", {})
            caption = f"{s['title']}\n\n{s.get('description', '')}\n\nFull episode on YouTube: Doomed Doug\n\n{_hashtags()}"
            if cfg.get("instagram_reels", True) and os.environ.get("META_IG_USER_ID") and not sm.get("instagram"):
                if dry_run:
                    print("[dry] IG reel:", s["title"])
                else:
                    try:
                        sm["instagram"] = instagram_reel(public_url(ep, f"{s['id']}.mp4"), caption)
                        done.append(f"IG reel: {s['title']} {sm['instagram'].get('url')}")
                    except Exception as e:
                        sm["instagram_error"] = str(e)[:300]
                        notify.send(f"⚠️ Instagram Reel failed for {s['title']}: {str(e)[:300]}")
            if cfg.get("facebook_reels", True) and not sm.get("facebook"):
                if dry_run:
                    print("[dry] FB reel:", s["title"])
                else:
                    try:
                        fb_caption = f"{s['title']}\n\nFull episode: {yt_url}\n\n{_hashtags()}"
                        sm["facebook"] = facebook_reel(local_file(ep, f"{s['id']}.mp4"), fb_caption)
                        done.append(f"FB reel: {s['title']} {sm['facebook']['url']}")
                    except Exception as e:
                        sm["facebook_error"] = str(e)[:300]
                        notify.send(f"⚠️ Facebook Reel failed for {s['title']}: {str(e)[:300]}")
            sp.write_text(json.dumps(shorts, indent=2, ensure_ascii=False), encoding="utf-8")
    if done:
        notify.send("📣 Posted to Facebook/Instagram:\n" + "\n".join(done))
    return done
