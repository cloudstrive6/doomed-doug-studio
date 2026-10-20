"""Marathon compilations: several finished episodes joined into one long video (watch-time engine for the
Partner Program's 4,000 hours and for session time, which the recommendation system rewards).

    python -m studio compile <slug> [--render-only] [--dry-run]

Spec: `compilations/<slug>/spec.json`
  {"title": "...", "episodes": ["002-every-parasite", ...], "intro": "spoken cold open (<= 45 words)",
   "card": "BIG TITLE ON THE INTRO", "description": "first lines of the description", "tags": [...]}
Builds `compilations/<slug>/build/final.mp4` (+ thumbnail.png) and uploads it privately scheduled into the
`compilations` playlist at the next free compilation slot (config `compilations.publish_*`). Lives outside
`episodes/` so it never takes a daily episode slot. Each episode's own end slate (the "next one is right here"
card) is trimmed off; older episodes are lifted to the channel loudness (-14 LUFS) so levels match.
"""
from __future__ import annotations

import datetime as dt
import json
import re
import subprocess
from pathlib import Path

from .config import ROOT, load_config

COMP = ROOT / "compilations"


def _run(cmd: list[str]):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        raise RuntimeError(f"{cmd[0]} failed: {r.stderr[-600:]}")
    return r.stdout


def _duration(f: Path) -> float:
    return float(_run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(f)]).strip())


def _loudness(f: Path) -> float:
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(f), "-vn", "-af", "ebur128", "-f", "null", "-"],
                       capture_output=True, text=True)
    m = re.findall(r"I:\s+(-?[\d.]+) LUFS", r.stderr)
    return float(m[-1]) if m else -14.0


def _fetch(ep: Path, out: Path) -> Path:
    if not out.exists():
        tmp = out.parent / f"dl-{ep.name[:3]}"
        tmp.mkdir(parents=True, exist_ok=True)
        _run(["gh", "release", "download", f"ep-{ep.name[:3]}", "-p", "final.mp4", "-D", str(tmp), "--clobber"])
        (tmp / "final.mp4").replace(out)
        tmp.rmdir()
    return out


def _prepare(ep: Path, build: Path) -> tuple[Path, float]:
    """Episode video with its end slate trimmed and its audio at -14 LUFS; same codecs as our renders, so the
    parts can be joined without re-encoding the video."""
    meta = json.loads((ep / "metadata.json").read_text(encoding="utf-8"))
    raw = _fetch(ep, build / f"{ep.name[:3]}_raw.mp4")
    keep = _duration(raw) - float(meta.get("end_slate_s", 0))
    gain = -14.0 - _loudness(raw)
    out = build / f"{ep.name[:3]}.mp4"
    if not out.exists():
        limit = 10 ** (-2.0 / 20)
        _run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(raw), "-t", f"{keep:.3f}", "-map", "0:v", "-map", "0:a",
              "-c:v", "copy", "-af", f"volume={gain:.2f}dB,alimiter=limit={limit:.4f}:level=false" if gain > 0.5
              else "anull", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-movflags", "+faststart", str(out)])
    return out, _duration(out)


def _intro(slug: str, spec: dict, build: Path) -> Path:
    """Short narrated cold open rendered by the engine (no end slate): what this marathon is, in Doug terms."""
    from .assemble import render_video
    d = build / "intro"
    d.mkdir(parents=True, exist_ok=True)
    card = spec.get("card") or spec["title"].upper()
    words = card.split()
    half = (len(words) + 1) // 2
    shot = {"id": "s001", "topbar": False, "narration": spec["intro"], "hold": 0.6, "scene": {
        "background": "#8fd3ff", "elements": [
            {"type": "rect", "x": 0, "y": 900, "w": 1920, "h": 180, "fill": "#7ac943", "width": 0},
            {"type": "wordart", "text": " ".join(words[:half]), "x": 960, "y": 200, "size": 110},
            {"type": "wordart", "text": " ".join(words[half:]), "x": 960, "y": 350, "size": 110, "appear": 0.15},
            {"type": "doug", "x": 760, "y": 880, "scale": 0.9, "pose": ["wave", "point"], "expression": "hopeful"},
            {"type": "label", "text": f"{len(spec['episodes'])} EPISODES, BACK TO BACK", "x": 1300, "y": 640,
             "size": 48, "appear": 0.35},
            {"type": "label", "text": "CHAPTERS IN THE DESCRIPTION", "x": 1300, "y": 740, "size": 40, "appear": 0.6}]}}
    (d / "shotlist.json").write_text(json.dumps({"episode": f"compilation-{slug}", "end_slate": False,
                                                 "shots": [shot]}, indent=1), encoding="utf-8")
    return render_video(d, require_voice=True)


def _chapters(parts: list[tuple[Path, float, dict]], intro_s: float) -> str:
    """One chapter per episode item, offset into the marathon (each episode's own chapter list from its
    description); the episode title goes into its first chapter so viewers can jump between episodes."""
    lines, t = [f"0:00 Intro"], intro_s
    stamp = lambda s: f"{int(s // 3600)}:{int(s % 3600 // 60):02d}:{int(s % 60):02d}" if s >= 3600 \
        else f"{int(s // 60)}:{int(s % 60):02d}"  # noqa: E731
    for _, dur, meta in parts:
        own = re.findall(r"^(\d{1,2}:\d{2}(?::\d{2})?)\s+(.+)$", meta.get("description", ""), re.M)
        if not own:
            lines.append(f"{stamp(t)} {meta['title']}")
        for k, (ts, name) in enumerate(own):
            secs = sum(int(x) * 60 ** i for i, x in enumerate(reversed(ts.split(":"))))
            label = meta["title"] if k == 0 else name   # the episode's own "Intro" becomes its title
            if secs < dur:
                lines.append(f"{stamp(t + secs)} {label}")
        t += dur
    return "\n".join(lines)


def _thumb_scene(spec: dict) -> dict:
    """Feed-legible marathon thumbnail: a big worried Doug, four large creatures from the episodes closing in from the
    corners, and the length in huge type ("1 HOUR"). Spec keys: `thumb_assets` (4 asset names), `thumb_text`."""
    from .shorts import _asset_box
    els = [{"type": "wordart", "text": spec.get("thumb_text", "1 HOUR"), "x": 960, "y": 160, "size": 210},
           {"type": "doug", "x": 960, "y": 1010, "scale": 1.35, "pose": "panic1", "expression": "screaming",
            "gear": ["sweat"]}]
    for name, (cx, cy) in zip(spec["thumb_assets"], [(330, 420), (1590, 420), (330, 850), (1590, 850)]):
        b = _asset_box(name, 1.0)
        if not b:
            continue
        k = min(540 / max(b[2] - b[0], 1), 380 / max(b[3] - b[1], 1), 3.0)
        els.append({"type": "asset", "name": name, "x": round(cx - (b[0] + b[2]) / 2 * k),
                    "y": round(cy - (b[1] + b[3]) / 2 * k), "scale": round(k, 3), "flip": cx > 960})
    return {"background": "#ffd400", "elements": els}


def _thumbnail(eps: list[Path], spec: dict, build: Path) -> Path:
    if spec.get("thumb_assets"):
        from .config import load_config
        from .scene import render_still
        out = build / "thumbnail.png"
        render_still(_thumb_scene(spec), 0, None, seed="thumb", style=load_config()["style"]).convert("RGB")             .resize((1280, 720)).save(out)
        return out
    """2x2 grid of the episodes' own thumbnails with a red 'FULL MARATHON' band (house style: bold, MS Paint)."""
    from PIL import Image, ImageDraw

    from .paint import font
    tiles = []
    for ep in eps[:4]:
        f = ep / "build" / "thumbnail.png"
        if not f.exists():
            _run(["python", "-m", "studio", "thumbnail", ep.name])
        tiles.append(Image.open(f).convert("RGB").resize((640, 360)))
    while len(tiles) < 4:
        tiles.append(tiles[-1])
    img = Image.new("RGB", (1280, 720), "black")
    for i, t in enumerate(tiles):
        img.paste(t, ((i % 2) * 640, (i // 2) * 360))
    d = ImageDraw.Draw(img)
    d.rectangle((0, 300, 1280, 420), fill=(224, 32, 27))
    f = font(84, "default", True)
    d.text((640, 360), spec.get("thumb_text", "FULL MARATHON"), font=f, fill="white", anchor="mm",
           stroke_width=6, stroke_fill="black")
    out = build / "thumbnail.png"
    img.save(out)
    return out


def next_slot(taken: list[str]) -> dt.datetime:
    from zoneinfo import ZoneInfo
    cfg = load_config()
    c = cfg.get("compilations", {})
    tz = ZoneInfo(cfg["schedule"]["timezone"])
    days = {"Mon": 0, "Tue": 1, "Wed": 2, "Thu": 3, "Fri": 4, "Sat": 5, "Sun": 6}
    want = {days[x] for x in c.get("publish_days", ["Sat"])}
    hh, mm = map(int, c.get("publish_time", "14:00").split(":"))
    earliest = dt.datetime.now(tz) + dt.timedelta(days=cfg["schedule"]["review_window_days"])
    d = earliest.date()
    for _ in range(60):
        cand = dt.datetime(d.year, d.month, d.day, hh, mm, tzinfo=tz)
        if cand.weekday() in want and cand >= earliest and \
                cand.astimezone(dt.timezone.utc).isoformat().replace("+00:00", "Z") not in taken:
            return cand
        d += dt.timedelta(days=1)
    raise RuntimeError("no compilation slot")


def build(slug: str) -> Path:
    base = COMP / slug
    spec = json.loads((base / "spec.json").read_text(encoding="utf-8"))
    b = base / "build"
    b.mkdir(parents=True, exist_ok=True)
    eps = [ROOT / "episodes" / e for e in spec["episodes"]]
    for ep in eps:
        if not json.loads((ep / "metadata.json").read_text(encoding="utf-8")).get("youtube_id"):
            raise SystemExit(f"{ep.name} isn't uploaded yet; compilations only use published episodes")
    parts = []
    for ep in eps:
        f, dur = _prepare(ep, b)
        parts.append((f, dur, json.loads((ep / "metadata.json").read_text(encoding="utf-8"))))
    intro = _intro(slug, spec, b)
    intro_s = _duration(intro)
    lst = b / "concat.txt"
    lst.write_text("\n".join(f"file '{p.resolve().as_posix()}'" for p in [intro] + [x[0] for x in parts]),
                   encoding="utf-8")
    final = b / "final.mp4"
    _run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy",
          "-movflags", "+faststart", str(final)])
    (b / "chapters.txt").write_text(_chapters(parts, intro_s), encoding="utf-8")
    _thumbnail(eps, spec, b)
    print(f"{final} ({_duration(final) / 60:.1f} min)")
    return final


def upload(slug: str, dry_run: bool = False) -> dict:
    from googleapiclient.http import MediaFileUpload

    from .youtube import add_to_playlist, local, yt
    cfg = load_config()
    base = COMP / slug
    spec = json.loads((base / "spec.json").read_text(encoding="utf-8"))
    mp = base / "metadata.json"
    meta = json.loads(mp.read_text(encoding="utf-8")) if mp.exists() else {}
    if meta.get("youtube_id"):
        return meta
    b = base / "build"
    taken = [json.loads(f.read_text(encoding="utf-8")).get("publish_at") for f in COMP.glob("*/metadata.json")]
    slot = dt.datetime.fromisoformat(spec["publish_at"].replace("Z", "+00:00")) if spec.get("publish_at")         else next_slot([t for t in taken if t])   # spec publish_at (UTC) overrides the weekly slot
    publish_at = slot.astimezone(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    links = "\n".join(f"{m['title']}: https://youtu.be/{m['youtube_id']}" for m in
                      (json.loads((ROOT / "episodes" / e / "metadata.json").read_text(encoding="utf-8"))
                       for e in spec["episodes"]))
    desc = (f"{spec.get('description', '').strip()}\n\nChapters:\n{(b / 'chapters.txt').read_text(encoding='utf-8')}"
            f"\n\nThe episodes on their own:\n{links}\n\nThe narration is an AI text-to-speech voice. Scripts are "
            f"researched and written with AI assistance and fact-checked. All drawings are original.\n\n#DoomedDoug")
    body = {"snippet": {"title": spec["title"][:100], "description": desc[:5000],
                        "tags": (spec.get("tags") or cfg["channel"]["default_tags"])[:30],
                        "categoryId": cfg["channel"]["category_id"], "defaultLanguage": "en",
                        "defaultAudioLanguage": "en"},
            "status": {"privacyStatus": "private", "publishAt": publish_at,
                       "selfDeclaredMadeForKids": bool(cfg["channel"]["made_for_kids"]), "embeddable": True,
                       "license": "youtube", "containsSyntheticMedia": False},
            "paidProductPlacementDetails": {"hasPaidProductPlacement": False}}
    if dry_run:
        print(json.dumps(body, indent=1)[:3000])
        return meta
    api = yt()
    req = api.videos().insert(part="snippet,status,paidProductPlacementDetails", body=body,
                              media_body=MediaFileUpload(str(b / "final.mp4"), chunksize=32 * 1024 * 1024,
                                                         resumable=True))
    resp = None
    while resp is None:
        _, resp = req.next_chunk()
    vid = resp["id"]
    meta.update(title=spec["title"], youtube_id=vid, publish_at=publish_at, url=f"https://youtu.be/{vid}",
                episodes=spec["episodes"], uploaded_at=dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"))
    mp.write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")
    try:
        api.thumbnails().set(videoId=vid, media_body=MediaFileUpload(str(b / "thumbnail.png"))).execute()
    except Exception as e:
        meta["thumbnail_warning"] = str(e)[:200]
    try:
        add_to_playlist(api, vid, "compilations")
    except Exception as e:
        meta["playlist_warning"] = str(e)[:200]
    mp.write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"{slug}: https://youtu.be/{vid} goes public {local(publish_at)}")
    return meta
