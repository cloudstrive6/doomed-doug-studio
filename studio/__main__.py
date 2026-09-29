"""Studio CLI:  python -m studio <command> ...

Episode stages (episodes/<id>/status.json):
  idea -> scripted -> script_approved -> shotlisted -> art_approved -> packaged -> built -> qc_passed -> uploaded
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path

from .config import ROOT, episode_dir, load_config

STAGES = ["idea", "scripted", "script_approved", "shotlisted", "art_approved", "packaged", "built",
          "qc_passed", "uploaded"]


def set_stage(ep: Path, stage: str, note: str = ""):
    if stage not in STAGES:
        raise SystemExit(f"unknown stage {stage}; valid: {STAGES}")
    p = ep / "status.json"
    st = json.loads(p.read_text(encoding="utf-8")) if p.exists() else {"history": []}
    st["stage"] = stage
    st["history"].append({"stage": stage, "at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
                          "note": note})
    p.write_text(json.dumps(st, indent=2), encoding="utf-8")


def get_stage(ep: Path) -> str:
    p = ep / "status.json"
    return json.loads(p.read_text(encoding="utf-8"))["stage"] if p.exists() else "idea"


def cmd_new(a):
    eps = ROOT / "episodes"
    nums = [int(d.name[:3]) for d in eps.iterdir() if d.is_dir() and d.name[:3].isdigit()]
    n = max(nums, default=0) + 1
    ep = eps / f"{n:03d}-{a.slug}"
    ep.mkdir(parents=True)
    (ep / "brief.md").write_text(f"# Episode {n:03d}: {a.slug}\n\n(creative director fills this in)\n", encoding="utf-8")
    set_stage(ep, "idea", "created")
    print(ep)


def cmd_status(a):
    for d in sorted((ROOT / "episodes").iterdir()):
        if d.is_dir():
            meta = d / "metadata.json"
            m = json.loads(meta.read_text(encoding="utf-8")) if meta.exists() else {}
            print(f"{d.name:40} {get_stage(d):16} {m.get('publish_at', ''):22} {m.get('title', '')}")


def cmd_stage(a):
    set_stage(episode_dir(a.episode), a.stage, a.note or "")


def cmd_validate(a):
    from .validate import validate_metadata, validate_shotlist
    ep = episode_dir(a.episode)
    probs = validate_shotlist(ep) if a.what in ("shotlist", "all") else []
    if a.what in ("metadata", "all"):
        probs += validate_metadata(ep)
    print("\n".join(probs) if probs else "OK")
    sys.exit(1 if probs else 0)


def cmd_keyframes(a):
    from .assemble import keyframes
    ep = episode_dir(a.episode)
    paths = keyframes(ep, a.shots.split(",") if a.shots else None)
    print(f"{len(paths)} keyframes -> {ep / 'build' / 'keyframes'}; contact sheets -> {ep / 'build' / 'contact'}")


def render_scene_file(src: Path, out: Path):
    from .scene import render_still
    scene = json.loads(src.read_text(encoding="utf-8"))
    img = render_still(scene, 0, None, seed=src.stem, style=load_config()["style"])
    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out)
    return out


def cmd_thumbnail(a):
    ep = episode_dir(a.episode)
    out = render_scene_file(ep / "thumbnail.json", ep / "build" / "thumbnail.png")
    from PIL import Image
    im = Image.open(out)
    if im.size != (1280, 720):
        im.resize((1280, 720), Image.NEAREST).save(out)
    im.resize((320, 180), Image.LANCZOS).save(ep / "build" / "thumbnail_small.png")  # how it looks in the feed
    print(out)


def cmd_art(a):
    print(render_scene_file(Path(a.scene), Path(a.out)))


def cmd_asset_preview(a):
    from .scene import render_still
    names = a.names
    tiles = []
    for n in names:
        scene = {"size": [800, 600], "background": "#ffffff",
                 "elements": [{"type": "asset", "name": n, "x": 400, "y": 300, "scale": a.scale},
                              {"type": "text", "text": n, "x": 400, "y": 570, "size": 28}]}
        tiles.append(render_still(scene, 0, None, seed=n))
    from PIL import Image
    sheet = Image.new("RGB", (800 * min(3, len(tiles)), 600 * ((len(tiles) + 2) // 3)), "white")
    for i, t in enumerate(tiles):
        sheet.paste(t, ((i % 3) * 800, (i // 3) * 600))
    out = ROOT / "assets" / "previews" / (a.out or "preview.png")
    out.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(out)
    print(out)


def cmd_narrate(a):
    from .assemble import narration
    ep = episode_dir(a.episode)
    t = narration(ep)
    print(f"{len(t)} shots, {sum(x['duration'] for x in t) / 60:.1f} min -> {ep / 'build' / 'narration.wav'}")


def cmd_render(a):
    from .assemble import render_video
    ep = episode_dir(a.episode)
    out = render_video(ep, "final.mp4" if a.final else "draft.mp4", require_voice=a.final, limit_shots=a.limit)
    if a.final:
        set_stage(ep, "built", "final render")
    print(out)


def cmd_qc(a):
    """Automated technical QC of the final render. Writes build/qc.json, exits 1 on failure."""
    from .assemble import probe, sample_frames
    ep = episode_dir(a.episode)
    cfg = load_config()
    video = ep / "build" / "final.mp4"
    problems = []
    info = probe(video)
    dur = float(info["format"]["duration"])
    lo, hi = cfg["video"]["target_minutes"]
    if not (lo * 60 * 0.8 <= dur <= hi * 60 * 1.5):
        problems.append(f"duration {dur / 60:.1f} min outside target {lo}-{hi} min")
    kinds = {s["codec_type"] for s in info["streams"]}
    if kinds != {"video", "audio"}:
        problems.append(f"streams: {kinds}")
    timing = json.loads((ep / "build" / "timing.json").read_text(encoding="utf-8"))
    if not timing.get("real_voice"):
        problems.append("narration is silent placeholder (no TTS key)")
    # style bible: a visual change at least every 5 s; fail any static stretch > 6 s
    from .assemble import load_shotlist
    shots = {s["id"]: s for s in load_shotlist(ep)["shots"]}
    stale = []
    for tm in timing["shots"]:
        sh = shots.get(tm["id"], {})
        if (sh.get("camera") or {}).get("move", "").startswith("pan"):
            continue  # a pan keeps revealing new content
        marks = sorted({0.0, 1.0} | {float(e.get("appear", 0)) for e in sh.get("scene", {}).get("elements", [])})
        gap = max(b - a for a, b in zip(marks, marks[1:])) * tm["duration"]
        if gap > 6.0:
            stale.append(f"{tm['id']} ({gap:.1f}s)")
    if stale:
        problems.append(f"static stretches > 6 s (add a pop-in element or split the shot): {stale}")
    if timing.get("real_voice") and not 185 <= timing.get("wpm_speech", 0) <= 215:
        problems.append(f"narration pace {timing.get('wpm_speech')} wpm; adjust voice.speaking_rate for 190-205")
    for f in ("thumbnail.png", "captions.srt"):
        if not (ep / "build" / f).exists():
            problems.append(f"{f} missing")
    frames = sample_frames(video, ep / "build" / "samples", every_s=a.every)
    res = {"duration_s": dur, "problems": problems, "samples": [str(f) for f in frames]}
    (ep / "build" / "qc.json").write_text(json.dumps(res, indent=1), encoding="utf-8")
    print(json.dumps(res, indent=1))
    sys.exit(1 if problems else 0)


def cmd_upload(a):
    from . import notify
    from .youtube import upload_episode
    ep = episode_dir(a.episode)
    if not a.dry_run and get_stage(ep) != "qc_passed" and not a.force:
        raise SystemExit(f"episode stage is {get_stage(ep)}, expected qc_passed")
    meta = upload_episode(ep, dry_run=a.dry_run)
    if a.dry_run:
        return
    set_stage(ep, "uploaded", meta.get("youtube_id", ""))
    warn = "\n".join("⚠ " + w for w in meta.get("upload_warnings", []))
    notify.send(f"🎬 Doomed Doug: new episode scheduled\n{meta['title']}\nGoes public: {meta['publish_at']} (UTC)\n"
                f"Review now: https://studio.youtube.com/video/{meta['youtube_id']}/edit\n{warn}",
                ep / "build" / "thumbnail.png")
    print(json.dumps(meta, indent=1, ensure_ascii=False))


def cmd_notify(a):
    from . import notify
    notify.send(a.text, Path(a.photo) if a.photo else None)


def cmd_auth(a):
    from .youtube import auth
    auth()


def cmd_analytics(a):
    from .youtube import pull_analytics, pull_competitors
    print(pull_analytics(a.days))
    print(pull_competitors())


def cmd_branding(a):
    from .youtube import set_channel_branding
    ch = ROOT / "channel"
    desc = (ch / "description.md").read_text(encoding="utf-8").strip() if (ch / "description.md").exists() else None
    set_channel_branding(desc, a.keywords, ch / "banner.png" if (ch / "banner.png").exists() else None)


def cmd_voices(a):
    """Render the same line with several Chirp 3 HD voices so a human can pick."""
    from . import tts
    cfg = load_config()
    out = ROOT / "channel" / "voice_samples"
    line = a.text or ("This is Doug. Today, we're dropping him into the deepest part of the ocean. "
                      "He did not agree to this.")
    for name in a.names.split(","):
        pcm, real = tts.synthesize(line, {**cfg["voice"], "name": f"en-US-Chirp3-HD-{name}"}, out / "cache")
        tts.write_wav(out / f"{name}.wav", pcm)
        print(out / f"{name}.wav", "" if real else "(silent: no GOOGLE_TTS_API_KEY)")


def cmd_queue(a):
    """Prints queue status; with --github-output writes need=true/false for the workflow."""
    import os
    from .youtube import queue_status
    q = queue_status()
    print(json.dumps(q, indent=1))
    if a.github_output and os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as f:
            f.write(f"need={'true' if q['need_episode'] else 'false'}\n")


def cmd_actions_usage(a):
    from .actions_usage import check
    u = check(alert=a.alert)
    print(json.dumps(u, indent=1))


def main():
    p = argparse.ArgumentParser(prog="studio")
    s = p.add_subparsers(dest="cmd", required=True)
    x = s.add_parser("new"); x.add_argument("slug"); x.set_defaults(f=cmd_new)
    x = s.add_parser("status"); x.set_defaults(f=cmd_status)
    x = s.add_parser("stage"); x.add_argument("episode"); x.add_argument("stage"); x.add_argument("--note"); x.set_defaults(f=cmd_stage)
    x = s.add_parser("validate"); x.add_argument("episode"); x.add_argument("what", nargs="?", default="all",
                                                                           choices=["shotlist", "metadata", "all"]); x.set_defaults(f=cmd_validate)
    x = s.add_parser("keyframes"); x.add_argument("episode"); x.add_argument("--shots"); x.set_defaults(f=cmd_keyframes)
    x = s.add_parser("thumbnail"); x.add_argument("episode"); x.set_defaults(f=cmd_thumbnail)
    x = s.add_parser("art"); x.add_argument("scene"); x.add_argument("out"); x.set_defaults(f=cmd_art)
    x = s.add_parser("asset-preview"); x.add_argument("names", nargs="+"); x.add_argument("--scale", type=float, default=1.0)
    x.add_argument("--out"); x.set_defaults(f=cmd_asset_preview)
    x = s.add_parser("narrate"); x.add_argument("episode"); x.set_defaults(f=cmd_narrate)
    x = s.add_parser("render"); x.add_argument("episode"); x.add_argument("--final", action="store_true")
    x.add_argument("--limit", type=int); x.set_defaults(f=cmd_render)
    x = s.add_parser("qc"); x.add_argument("episode"); x.add_argument("--every", type=float, default=30.0); x.set_defaults(f=cmd_qc)
    x = s.add_parser("upload"); x.add_argument("episode"); x.add_argument("--dry-run", action="store_true")
    x.add_argument("--force", action="store_true"); x.set_defaults(f=cmd_upload)
    x = s.add_parser("notify"); x.add_argument("text"); x.add_argument("--photo"); x.set_defaults(f=cmd_notify)
    x = s.add_parser("auth"); x.set_defaults(f=cmd_auth)
    x = s.add_parser("analytics"); x.add_argument("--days", type=int, default=28); x.set_defaults(f=cmd_analytics)
    x = s.add_parser("branding"); x.add_argument("--keywords"); x.set_defaults(f=cmd_branding)
    x = s.add_parser("voices"); x.add_argument("--names", default="Charon,Fenrir,Orus,Puck,Iapetus,Algenib")
    x.add_argument("--text"); x.set_defaults(f=cmd_voices)
    x = s.add_parser("queue"); x.add_argument("--github-output", action="store_true"); x.set_defaults(f=cmd_queue)
    x = s.add_parser("actions-usage"); x.add_argument("--alert", action="store_true"); x.set_defaults(f=cmd_actions_usage)
    a = p.parse_args()
    a.f(a)


if __name__ == "__main__":
    main()
