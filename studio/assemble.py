"""Episode builder: shotlist.json -> keyframes / narration / captions / final MP4."""
from __future__ import annotations

import json
import math
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw

from . import tts
from .config import ROOT, load_config

# Shared narration cache (keyed by text + voice settings), persisted between CI runs with actions/cache so a
# retried or re-rendered episode doesn't pay for Chirp 3 HD characters twice.
TTS_CACHE = ROOT / ".cache" / "tts"
from .scene import OUT_H, OUT_W, ShotRenderer, render_still, with_topbar


def _upscale_scene(scene: dict) -> dict:
    """A referenced 16:9 scene drawn smaller than 1080p (the 1280x720 thumbnail) is redrawn at 1920x1080 through a
    scaled group, so the opening shot has crisp 1080p lines and text instead of a blurry/jagged bitmap upscale."""
    w, h = scene.get("size", [OUT_W, OUT_H])
    if w >= OUT_W or abs(w / h - OUT_W / OUT_H) > 0.01:
        return scene
    k = OUT_W / w
    return {"background": scene.get("background", "#ffffff"),
            "elements": [{"type": "group", "x": 0, "y": 0, "scale": k, "elements": scene.get("elements", [])}]}


def load_shotlist(ep_dir: Path) -> dict:
    """Load shotlist.json, resolve `scene_ref` (e.g. the opening thumbnail grid) and the running caption bar."""
    sl = json.loads((ep_dir / "shotlist.json").read_text(encoding="utf-8"))
    current = None
    for shot in sl.get("shots", []):
        ref = shot.get("scene_ref")
        if ref and "scene" not in shot:
            f = ep_dir / f"{ref}.json"
            shot["scene"] = (json.loads(f.read_text(encoding="utf-8")) if f.exists() else
                             {"background": "#ffffff", "elements": [{"type": "text", "text": f"({ref} pending)",
                                                                     "x": 960, "y": 540, "size": 60}]})
            shot["scene"] = _upscale_scene(shot["scene"])
        if shot.get("chapter"):
            current = shot["chapter"]
        tb = shot.get("topbar", True)
        shot["_topbar"] = None if tb is False else (tb if isinstance(tb, str) else current)
    return sl


# ------------------------------------------------------------------ previews


def keyframes(ep_dir: Path, only: list[str] | None = None) -> list[Path]:
    """Render each shot's final state (all pop-ins visible) + contact sheets for review."""
    cfg = load_config()
    sl = load_shotlist(ep_dir)
    out = ep_dir / "build" / "keyframes"
    out.mkdir(parents=True, exist_ok=True)
    paths = []
    for shot in sl["shots"]:
        if only and shot["id"] not in only:
            continue
        img = render_still(shot["scene"], 0, None, seed=shot["id"], style=cfg["style"])
        if img.size != (OUT_W, OUT_H):
            from .scene import camera_rect, fit_frame
            w, h = img.size
            rect = camera_rect(shot.get("camera"), w, h, 1.0)
            img = fit_frame(img, rect)
        img = with_topbar(img, shot.get("_topbar"))
        p = out / f"{shot['id']}.png"
        img.save(p)
        paths.append(p)
    contact_sheets(ep_dir, sl, paths)
    return paths


def contact_sheets(ep_dir: Path, sl: dict, paths: list[Path], per_sheet: int = 12):
    out = ep_dir / "build" / "contact"
    out.mkdir(parents=True, exist_ok=True)
    for f in out.glob("*.png"):
        f.unlink()
    by_id = {s["id"]: s for s in sl["shots"]}
    tw, th, cols = 640, 360, 3
    for n in range(math.ceil(len(paths) / per_sheet)):
        chunk = paths[n * per_sheet:(n + 1) * per_sheet]
        rows = math.ceil(len(chunk) / cols)
        sheet = Image.new("RGB", (cols * tw, rows * (th + 70)), "white")
        d = ImageDraw.Draw(sheet)
        for i, p in enumerate(chunk):
            x, y = (i % cols) * tw, (i // cols) * (th + 70)
            sheet.paste(Image.open(p).resize((tw, th)), (x, y))
            sid = p.stem
            txt = f"{sid}: {by_id.get(sid, {}).get('narration', '')}"
            d.text((x + 6, y + th + 4), txt[:95], fill="black")
            d.text((x + 6, y + th + 22), txt[95:190], fill="black")
            d.rectangle((x, y, x + tw - 1, y + th - 1), outline="black")
        sheet.save(out / f"sheet_{n + 1:02d}.png")


# ------------------------------------------------------------------ audio


def narration(ep_dir: Path, require_voice: bool = False) -> list[dict]:
    """Synthesize every shot's line. Returns timing list and writes narration.wav + captions.srt."""
    cfg = load_config()
    sl = load_shotlist(ep_dir)
    voice = {**cfg["voice"], **sl.get("voice", {})}
    build = ep_dir / "build"
    build.mkdir(parents=True, exist_ok=True)
    gap = cfg["video"]["gap_between_shots"]
    pcm_all, timing, t, real_all = [], [], 0.0, True
    for shot in sl["shots"]:
        text = shot.get("narration", "").strip()
        if text:
            pcm, real = tts.synthesize(text, voice, TTS_CACHE)
            real_all &= real
        else:
            pcm = b""
        hold = float(shot.get("hold", 0.0))
        pause = float(shot.get("pause_after", gap))
        dur = max(tts.pcm_seconds(pcm) + pause + hold, float(shot.get("min_duration", 0.8)))
        pad = dur - tts.pcm_seconds(pcm)
        pcm_all.append(pcm + tts._silence(pad))
        timing.append({"id": shot["id"], "start": round(t, 3), "duration": round(dur, 3),
                       "speech": round(tts.pcm_seconds(pcm), 3), "text": text})
        t += dur
    if require_voice and not real_all:
        raise RuntimeError("GOOGLE_TTS_API_KEY missing: refusing to build a silent final video")
    pcm = b"".join(pcm_all)
    sting = cfg["video"].get("sting")
    if sting:  # short music sting on every item change (kicker -> next item name)
        starts = [tm["start"] for sh, tm in zip(sl["shots"], timing) if sh.get("chapter")][1:]
        pcm = mix_at(pcm, load_pcm(Path(__file__).resolve().parent.parent / sting),
                     [max(0.0, s_ - 0.25) for s_ in starts], cfg["video"].get("sting_volume", 0.5))
    tts.write_wav(build / "narration.wav", pcm)
    if cfg["video"].get("loudness_lufs") is not None:
        tts.normalize_wav(build / "narration.wav", cfg["video"]["loudness_lufs"], cfg["video"].get("true_peak_db", -1.5))
    words = sum(len(tm["text"].split()) for tm in timing)
    speech = sum(tm["speech"] for tm in timing) or 1
    (build / "timing.json").write_text(json.dumps({"total": round(t, 3), "real_voice": real_all,
                                                   "words": words, "wpm_speech": round(words / speech * 60, 1),
                                                   "wpm_overall": round(words / max(t, 1) * 60, 1),
                                                   "shots": timing}, indent=1), encoding="utf-8")
    write_srt(build / "captions.srt", timing)
    write_chapters(build / "chapters.txt", sl["shots"], timing)
    return timing


def load_pcm(path: Path) -> bytes:
    """Decode any audio file to 24 kHz mono 16-bit PCM with ffmpeg."""
    r = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", str(path), "-f", "s16le", "-ac", "1", "-ar",
                        str(tts.SAMPLE_RATE), "-"], capture_output=True, check=True)
    return r.stdout


def mix_at(base: bytes, clip: bytes, times: list[float], gain: float) -> bytes:
    import array
    b = array.array("h", base)
    c = array.array("h", clip)
    for t0 in times:
        off = int(t0 * tts.SAMPLE_RATE)
        for i in range(min(len(c), len(b) - off)):
            v = b[off + i] + int(c[i] * gain)
            b[off + i] = 32767 if v > 32767 else (-32768 if v < -32768 else v)
    return b.tobytes()


def write_chapters(path: Path, shots: list[dict], timing: list[dict]):
    """YouTube chapters from shots' "chapter" fields: first at 0:00, each >= 10 s, at least 3."""
    marks = [(tm["start"], sh["chapter"]) for sh, tm in zip(shots, timing) if sh.get("chapter")]
    if not marks:
        path.write_text("", encoding="utf-8")
        return
    if marks[0][0] < 10:
        marks[0] = (0.0, marks[0][1])  # first chapter must start at 0:00
    else:
        marks.insert(0, (0.0, "Intro"))
    kept = []
    for t, name in marks:
        if kept and t - kept[-1][0] < 10:
            continue
        kept.append((t, name))
    if len(kept) < 3:
        path.write_text("", encoding="utf-8")
        return
    fmt = lambda t: f"{int(t // 3600)}:{int(t % 3600 // 60):02d}:{int(t % 60):02d}" if t >= 3600 else f"{int(t // 60)}:{int(t % 60):02d}"
    path.write_text("\n".join(f"{fmt(t)} {n}" for t, n in kept), encoding="utf-8")


def _ts(s):
    h, m = int(s // 3600), int(s % 3600 // 60)
    return f"{h:02d}:{m:02d}:{s % 60:06.3f}".replace(".", ",")


def write_srt(path: Path, timing: list[dict], max_chars: int = 84):
    cues = []
    for sh in timing:
        words = sh["text"].split()
        if not words:
            continue
        chunks, cur = [], ""
        for w in words:
            if len(cur) + len(w) + 1 > max_chars and cur:
                chunks.append(cur)
                cur = w
            else:
                cur = (cur + " " + w).strip()
        chunks.append(cur)
        total_chars = sum(len(c) for c in chunks)
        t = sh["start"]
        for c in chunks:
            d = sh["speech"] * len(c) / total_chars if sh["speech"] else sh["duration"] / len(chunks)
            cues.append((t, t + d, c))
            t += d
    lines = []
    for i, (a, b, c) in enumerate(cues, 1):
        lines += [str(i), f"{_ts(a)} --> {_ts(b)}", c, ""]
    path.write_text("\n".join(lines), encoding="utf-8")


# ------------------------------------------------------------------ video


def render_video(ep_dir: Path, out_name: str = "final.mp4", require_voice: bool = False,
                 limit_shots: int | None = None) -> Path:
    cfg = load_config()
    sl = load_shotlist(ep_dir)
    build = ep_dir / "build"
    timing = narration(ep_dir, require_voice=require_voice)
    fps = cfg["video"]["fps"]
    shots = sl["shots"][:limit_shots] if limit_shots else sl["shots"]
    total = sum(t["duration"] for t in timing[:len(shots)])
    out = build / out_name
    cmd = ["ffmpeg", "-y", "-loglevel", "warning",
           "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{OUT_W}x{OUT_H}", "-r", str(fps), "-i", "-",
           "-i", str(build / "narration.wav")]
    music = cfg["video"].get("music")
    if music:
        cmd += ["-stream_loop", "-1", "-i", str(Path(__file__).resolve().parent.parent / music),
                "-filter_complex",
                f"[2:a]volume={cfg['video'].get('music_volume', 0.06)}[m];"
                f"[1:a][m]amix=inputs=2:duration=first:dropout_transition=0:normalize=0[a]",
                "-map", "0:v", "-map", "[a]"]
    else:
        cmd += ["-map", "0:v", "-map", "1:a"]
    cmd += ["-t", f"{total:.3f}", "-c:v", "libx264", "-preset", "veryfast", "-tune", "animation",
            "-crf", "20", "-pix_fmt", "yuv420p", "-profile:v", "high", "-r", str(fps),
            "-g", str(fps // 2), "-bf", "2",  # YouTube upload spec: closed GOP of half the frame rate, 2 B-frames
            "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-movflags", "+faststart",
            str(out)]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    try:
        for shot, tm in zip(shots, timing):
            # cumulative rounding: frame boundaries come from absolute times, so the total frame count equals
            # round(total * fps) exactly and video never runs past the audio (-t) cut
            f0 = round(tm["start"] * fps)
            f1 = round((tm["start"] + tm["duration"]) * fps)
            if f1 <= f0:
                continue
            r = ShotRenderer(shot, tm["duration"], fps=fps, style=cfg["style"], topbar=shot.get("_topbar"),
                             n_frames=f1 - f0)
            last_id, last_bytes = None, None
            for frame in r.frames():
                if id(frame) != last_id:
                    last_id, last_bytes = id(frame), frame.convert("RGB").tobytes()
                try:
                    proc.stdin.write(last_bytes)
                except BrokenPipeError:
                    raise RuntimeError("ffmpeg stopped reading frames early; see its error output above")
    finally:
        proc.stdin.close()
        proc.wait()
    if proc.returncode:
        raise RuntimeError("ffmpeg failed")
    return out


def sample_frames(video: Path, out_dir: Path, every_s: float = 30.0) -> list[Path]:
    """Grab frames from the finished video for the visual screener."""
    out_dir.mkdir(parents=True, exist_ok=True)
    for f in out_dir.glob("*.png"):
        f.unlink()
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(video), "-vf",
                    f"fps=1/{every_s},scale=640:-1", str(out_dir / "f_%03d.png")], check=True)
    return sorted(out_dir.glob("*.png"))


def probe(video: Path) -> dict:
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                        "format=duration:stream=codec_type,width,height,r_frame_rate,sample_rate",
                        "-of", "json", str(video)], capture_output=True, text=True, check=True)
    return json.loads(r.stdout)
