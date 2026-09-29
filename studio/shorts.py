"""YouTube Shorts cut from an episode: 1080x1920 @ fps, stacked layout (hook title / whole 16:9 drawing /
big burned-in subtitles), ending on a card that sends viewers to the long video via the "Related video" link.

episodes/<id>/shorts.json (written by the director, titled by the youtube-titler):
{"shorts": [{"id": "short01", "from": "s031", "to": "s042", "title": "...", "hook": "...",
             "outro": "The full dive is linked above.", "description": "..."}]}
Uploaded state is written back into the same entries (youtube_id, publish_at, related_set).
"""
from __future__ import annotations

import datetime as dt
import json
import math
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw

from . import tts
from .assemble import TTS_CACHE, load_shotlist
from .config import ROOT, load_config
from .paint import font, wrap
from .scene import ShotRenderer, render_still

SW, SH = 1080, 1920
ZOOM = 1.25                         # drawing shown 1350x760, centre-cropped to 1080 wide (~10% trimmed per side)
BAND_H = round(608 * ZOOM)          # 760
SCENE_Y = 560                       # top of the drawing band
SUB_Y = SCENE_Y + BAND_H + 150      # centre of the subtitle block


def load(ep: Path) -> dict:
    p = ep / "shorts.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {"shorts": []}


def save(ep: Path, data: dict):
    (ep / "shorts.json").write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


def _shot_slice(sl: dict, a: str, b: str) -> list[dict]:
    ids = [s["id"] for s in sl["shots"]]
    i, j = ids.index(a), ids.index(b)
    return sl["shots"][i:j + 1]


def validate(ep: Path) -> list[str]:
    cfg = load_config().get("shorts", {})
    data, sl = load(ep), load_shotlist(ep)
    ids = {s["id"] for s in sl["shots"]}
    probs = []
    if len(data["shorts"]) < cfg.get("per_episode", 2):
        probs.append(f"shorts.json has {len(data['shorts'])} shorts; need {cfg.get('per_episode', 2)}")
    for s in data["shorts"]:
        for k in ("id", "from", "to", "title"):
            if not s.get(k):
                probs.append(f"{s.get('id', '?')}: missing {k}")
        if s.get("from") not in ids or s.get("to") not in ids:
            probs.append(f"{s.get('id')}: shot range {s.get('from')}..{s.get('to')} not in shotlist")
            continue
        words = sum(len(x.get("narration", "").split()) for x in _shot_slice(sl, s["from"], s["to"]))
        words += len(s.get("outro", "").split()) + len(s.get("hook", "").split())
        secs = words / 3.2
        if not 20 <= secs <= 58:
            probs.append(f"{s['id']}: ~{secs:.0f}s of narration; keep Shorts 25-55 s")
        if len(s["title"]) > 60:
            probs.append(f"{s['id']}: title over 60 chars")
    return probs


# ------------------------------------------------------------------ layout


def _chunks(text: str, speech: float, start: float, n: int = 4):
    words = text.split()
    groups = [" ".join(words[i:i + n]) for i in range(0, len(words), n)] or [""]
    total = sum(len(g) for g in groups) or 1
    t, out = start, []
    for g in groups:
        d = speech * len(g) / total
        out.append((t, t + d, g))
        t += d
    return out


def _band_colors(frame: Image.Image) -> tuple:
    """Colours for the areas above/below the drawing: per-channel MEDIAN of a 40 px strip at the drawing's top and
    bottom edge. A single-pixel sample flickered whenever a thin line or a spray dot (marine snow) crossed it
    during a pan; a median over a strip ignores those."""
    def med(box):
        px = list(frame.crop(box).convert("RGB").resize((96, 8), Image.NEAREST).getdata())
        return tuple(sorted(c[i] for c in px)[len(px) // 2] for i in range(3))
    w, h = frame.size
    return med((0, 0, w, 40)), med((0, h - 40, w, h))


def _compose(scene_frame: Image.Image, title: str, subtitle: str, item: str | None, bands: tuple | None = None) -> Image.Image:
    top, bottom = bands or _band_colors(scene_frame)
    canvas = Image.new("RGB", (SW, SH), top)
    ImageDraw.Draw(canvas).rectangle((0, SCENE_Y + BAND_H // 2, SW, SH), fill=bottom)  # seamless bands
    big = scene_frame.resize((round(SW * ZOOM), BAND_H), Image.LANCZOS)
    x0 = (big.width - SW) // 2
    canvas.paste(big.crop((x0, 0, x0 + SW, BAND_H)), (0, SCENE_Y))
    d = ImageDraw.Draw(canvas)
    d.fontmode = "1"
    # hook title (red, black outline), top band
    f = font(76, "default", True)
    lines = wrap(title, f, SW - 120)
    y = 330 - (len(lines) - 1) * 44
    for ln in lines:
        d.text((SW / 2, y), ln, font=f, fill=(224, 32, 27), anchor="mm", stroke_width=6, stroke_fill=(0, 0, 0))
        y += 88
    if item:
        fi = font(40, "ComicNeue-Bold")
        tw = d.textlength(item.upper(), font=fi)
        d.rectangle((SW / 2 - tw / 2 - 26, SCENE_Y - 70, SW / 2 + tw / 2 + 26, SCENE_Y - 14), fill="white",
                    outline="black", width=3)
        d.text((SW / 2, SCENE_Y - 42), item.upper(), font=fi, fill="black", anchor="mm")
    if subtitle:
        fs = font(84, "default", True)
        y = SUB_Y
        for ln in wrap(subtitle, fs, SW - 140)[:2]:
            d.text((SW / 2, y), ln, font=fs, fill="white", anchor="mm", stroke_width=7, stroke_fill=(0, 0, 0))
            y += 100
    # small channel tag
    ft = font(34, "ComicNeue-Bold")
    d.text((SW / 2, SH - 150), "@DoomedDoug", font=ft, fill="white", anchor="mm", stroke_width=3, stroke_fill="black")
    return canvas


def _end_card(text: str) -> dict:
    """End card: two-line WordArt + red arrow pointing DOWN to where Shorts show the Related-video link.
    Everything stays inside x 260..1660, the part of the 1920 frame that survives the Shorts zoom-crop."""
    words = text.split()
    half = (len(words) + 1) // 2
    l1, l2 = " ".join(words[:half]), " ".join(words[half:])
    return {"background": "#8fd3ff", "elements": [
        {"type": "wordart", "text": l1, "x": 960, "y": 210, "size": 108},
        {"type": "wordart", "text": l2, "x": 960, "y": 360, "size": 108},
        {"type": "doug", "x": 640, "y": 880, "scale": 0.95, "pose": ["point", "wave"], "expression": "hopeful"},
        {"type": "arrow", "from": [1180, 560], "to": [1180, 980], "color": "#e0201b", "width": 22, "head": 80}]}


# ------------------------------------------------------------------ render


def render(ep: Path, only: list[str] | None = None) -> list[Path]:
    cfg = load_config()
    fps = cfg["video"]["fps"]
    voice = cfg["voice"]
    gap = cfg["video"]["gap_between_shots"]
    data, sl = load(ep), load_shotlist(ep)
    out_dir = ep / "build" / "shorts"
    out_dir.mkdir(parents=True, exist_ok=True)
    made = []
    for s in data["shorts"]:
        if only and s["id"] not in only:
            continue
        segs = []  # (shot, pcm, duration, text)
        if s.get("hook"):
            first = _shot_slice(sl, s["from"], s["to"])[0]
            segs.append(({**first, "id": first["id"] + "_hook"}, s["hook"]))
        for shot in _shot_slice(sl, s["from"], s["to"]):
            segs.append((shot, shot.get("narration", "")))
        end_text = s.get("end_card", "FULL VIDEO: TAP THE LINK BELOW")
        segs.append(({"id": s["id"] + "_end", "scene": _end_card(end_text), "boil": True},
                     s.get("outro", "The full video is linked below.")))
        pcm_all, plan, t = [], [], 0.0
        for shot, text in segs:
            pcm = tts.synthesize(text, voice, TTS_CACHE)[0] if text.strip() else b""
            speech = tts.pcm_seconds(pcm)
            dur = max(speech + gap + float(shot.get("hold", 0)), 0.8)
            pcm_all.append(pcm + tts._silence(dur - speech))
            plan.append((shot, t, dur, speech, text))
            t += dur
        wav = out_dir / f"{s['id']}.wav"
        tts.write_wav(wav, b"".join(pcm_all))
        out = out_dir / f"{s['id']}.mp4"
        cmd = ["ffmpeg", "-y", "-loglevel", "warning", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{SW}x{SH}",
               "-r", str(fps), "-i", "-", "-i", str(wav), "-map", "0:v", "-map", "1:a", "-t", f"{t:.3f}",
               "-c:v", "libx264", "-preset", "veryfast", "-tune", "animation", "-crf", "20", "-pix_fmt", "yuv420p",
               "-profile:v", "high", "-r", str(fps), "-g", str(fps // 2), "-bf", "2",
               "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-movflags", "+faststart", str(out)]
        proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
        item = None
        try:
            for shot, start, dur, speech, text in plan:
                item = shot.get("chapter") or item
                subs = _chunks(text, speech, start)
                f0, f1 = round(start * fps), round((start + dur) * fps)
                r = ShotRenderer(shot, dur, fps=fps, style=cfg["style"], topbar=None, n_frames=f1 - f0)
                last_key, last_bytes, last_frame, target, band = None, None, None, None, None
                alpha = 1 - math.exp(-1 / (fps * 0.25))  # ~0.25 s smoothing of band colours during pans
                for k, frame in enumerate(r.frames()):
                    now = start + k / fps
                    sub = next((g for a, b, g in subs if a <= now < b), "")
                    if id(frame) != last_frame:
                        last_frame, target = id(frame), _band_colors(frame)
                    if band is None:  # snap on a cut, ease within a shot
                        band = [list(map(float, target[0])), list(map(float, target[1]))]
                    else:
                        for j in (0, 1):
                            band[j] = [b + (t - b) * alpha for b, t in zip(band[j], target[j])]
                    bands = tuple(tuple(int(round(v)) for v in band[j]) for j in (0, 1))
                    key = (id(frame), sub, bands)
                    if key != last_key:
                        last_key = key
                        last_bytes = _compose(frame, s["title"], sub,
                                              None if shot["id"].endswith("_end") else item, bands).tobytes()
                    proc.stdin.write(last_bytes)
        finally:
            proc.stdin.close()
            proc.wait()
        if proc.returncode:
            raise RuntimeError(f"ffmpeg failed for {s['id']}")
        s["duration_s"] = round(t, 1)
        made.append(out)
        # preview still for the visual screener
        mid = plan[len(plan) // 2]
        _compose(render_still(mid[0]["scene"], 0, None, seed=mid[0]["id"], style=cfg["style"]).resize((1920, 1080)),
                 s["title"], mid[4][:40], mid[0].get("chapter")).resize((540, 960)).save(out_dir / f"{s['id']}_preview.png")
    save(ep, data)
    return made


# ------------------------------------------------------------------ schedule + upload


def next_slot(taken: list[str], not_before: dt.datetime) -> dt.datetime:
    from zoneinfo import ZoneInfo
    cfg = load_config()
    tz = ZoneInfo(cfg["schedule"]["timezone"])
    from .youtube import in_launch_phase
    times = cfg["shorts"]["publish_times"] if in_launch_phase() else         cfg["shorts"].get("weekly_publish_times", cfg["shorts"]["publish_times"])
    earliest = max(dt.datetime.now(tz) + dt.timedelta(days=cfg["schedule"]["review_window_days"]),
                   not_before.astimezone(tz) + dt.timedelta(hours=2))
    used = {dt.datetime.fromisoformat(x.replace("Z", "+00:00")) for x in taken}
    d = earliest.date()
    for _ in range(800):
        for hm in times:
            hh, mm = map(int, hm.split(":"))
            c = dt.datetime(d.year, d.month, d.day, hh, mm, tzinfo=tz)
            if c >= earliest and c.astimezone(dt.timezone.utc) not in used:
                return c
        d += dt.timedelta(days=1)
    raise RuntimeError("no Shorts slot")


def taken_slots() -> list[str]:
    out = []
    for f in (ROOT / "episodes").glob("*/shorts.json"):
        out += [s["publish_at"] for s in json.loads(f.read_text(encoding="utf-8"))["shorts"] if s.get("publish_at")]
    return out


def upload(ep: Path) -> list[dict]:
    from googleapiclient.http import MediaFileUpload
    from .youtube import _parse_utc, add_to_playlist, local, yt
    cfg = load_config()
    meta = json.loads((ep / "metadata.json").read_text(encoding="utf-8"))
    if not meta.get("youtube_id"):
        raise SystemExit("upload the long video first (Shorts link to it)")
    long_at = _parse_utc(meta["publish_at"])
    data = load(ep)
    api = yt()
    done = []
    for s in data["shorts"]:
        f = ep / "build" / "shorts" / f"{s['id']}.mp4"
        if s.get("youtube_id") or not f.exists():
            continue
        if s.get("schedule_at"):  # one-off override in the owner's time zone (NZ), "YYYY-MM-DD HH:MM"
            from zoneinfo import ZoneInfo
            nz = ZoneInfo(cfg["schedule"].get("display_timezone", "Pacific/Auckland"))
            slot = dt.datetime.strptime(s["schedule_at"], "%Y-%m-%d %H:%M").replace(tzinfo=nz)
        else:
            slot = next_slot(taken_slots(), long_at)
        publish_at = slot.astimezone(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
        desc = (s.get("description") or s["title"]) + (
            f"\n\nFull video: {meta['title']}\nhttps://youtu.be/{meta['youtube_id']}\n\n#DoomedDoug #shorts")
        body = {"snippet": {"title": s["title"][:100], "description": desc[:5000],
                            "tags": (meta.get("tags") or [])[:10], "categoryId": cfg["channel"]["category_id"],
                            "defaultLanguage": "en", "defaultAudioLanguage": "en"},
                "status": {"privacyStatus": "private", "publishAt": publish_at, "selfDeclaredMadeForKids": False,
                           "embeddable": True, "license": "youtube", "containsSyntheticMedia": False}}
        req = api.videos().insert(part="snippet,status", body=body,
                                  media_body=MediaFileUpload(str(f), chunksize=16 * 1024 * 1024, resumable=True))
        resp = None
        while resp is None:
            _, resp = req.next_chunk()
        s.update(youtube_id=resp["id"], publish_at=publish_at, related_video=meta["youtube_id"], related_set=False,
                 uploaded_at=dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"))
        try:
            add_to_playlist(api, resp["id"], cfg["shorts"].get("playlist", "Doomed Doug Shorts"))
        except Exception as e:
            s["playlist_warning"] = str(e)[:200]
        save(ep, data)
        done.append(s)
        print(f"{s['id']}: https://youtu.be/{resp['id']} goes public {local(publish_at)}")
    return done


def pending_related() -> list[dict]:
    """Shorts whose 'Related video' link still has to be set in YouTube Studio (not available in the API)."""
    out = []
    for f in sorted((ROOT / "episodes").glob("*/shorts.json")):
        ep = f.parent
        meta = json.loads((ep / "metadata.json").read_text(encoding="utf-8"))
        for s in json.loads(f.read_text(encoding="utf-8"))["shorts"]:
            if s.get("youtube_id") and not s.get("related_set"):
                out.append({"episode": ep.name, "short": s["id"], "short_title": s["title"],
                            "studio_url": f"https://studio.youtube.com/video/{s['youtube_id']}/edit",
                            "related_title": meta["title"], "related_id": meta["youtube_id"],
                            "short_publish_at": s["publish_at"], "long_publish_at": meta["publish_at"]})
    return out


def mark_related(short_youtube_id: str):
    for f in (ROOT / "episodes").glob("*/shorts.json"):
        data = json.loads(f.read_text(encoding="utf-8"))
        for s in data["shorts"]:
            if s.get("youtube_id") == short_youtube_id:
                s["related_set"] = True
                f.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
                return True
    return False
