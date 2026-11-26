"""Native 9:16 Shorts for What If episodes, rendered with the same toon engine, cast, sets and voices.

shorts_plan.json in the episode's pilot folder:
{"shorts": [{"id": "short01", "scenes": ["01", "03"], "hook": "optional narrator line before",
             "outro": "The full thirty days is linked below.", "title": "...", "description": "..."}]}

  py -m studio.whatif_shorts build <pilot_dir> [short_id ...]   writes <pilot_dir>/shorts/<id>/ and renders it
  py -m studio.whatif_shorts publish <pilot_dir> <episode_dir>  copies the MP4s to <episode_dir>/build/shorts/ and
                                                                writes shorts.json entries for `studio shorts upload`
Each Short is a complete moment that ends on its payoff (Doug's Shorts rule since 2026-11-03), 35 to 60 s.
"""
from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
from pathlib import Path


def _scene_blocks(text: str) -> tuple[str, dict]:
    head, rest = text.split("## SCENE ", 1)
    blocks = {}
    for b in ("## SCENE " + rest).split("\n## SCENE ")[0:]:
        b = b if b.startswith("## SCENE ") else "## SCENE " + b
        n = re.match(r"## SCENE (\d+)", b).group(1).zfill(2)
        blocks[n] = b.rstrip() + "\n"
    return head, blocks


def build(pdir: Path, only: list[str] | None = None):
    plan = json.loads((pdir / "shorts_plan.json").read_text(encoding="utf-8"))
    text = (pdir / "script.md").read_text(encoding="utf-8")
    head, blocks = _scene_blocks(text)
    staging = json.loads((pdir / "staging.json").read_text(encoding="utf-8"))
    for sh in plan["shorts"]:
        if only and sh["id"] not in only:
            continue
        d = pdir / "shorts" / sh["id"]
        d.mkdir(parents=True, exist_ok=True)
        first, last = sh["scenes"][0], sh["scenes"][-1]
        set_of = lambda n: re.search(r"set:\s*([a-z0-9_]+)", blocks[n]).group(1)
        parts = [head.rstrip() + "\n\n"]
        if sh.get("hook"):
            parts.append(f"## SCENE 00 | set: {set_of(first)} | day: -\nNARRATOR: {sh['hook']}\n\n")
        parts += [blocks[n] + "\n" for n in sh["scenes"]]
        parts.append(f"## SCENE 99 | set: {set_of(last)} | day: -\nNARRATOR: {sh['outro']}\n")
        (d / "script.md").write_text("".join(parts), encoding="utf-8")
        st = json.loads(json.dumps(staging))
        st["scenes"].pop("END", None)
        for n in list(st["scenes"]):
            st["scenes"][n]["day_wipe"] = False
        base_first = {k: v for k, v in staging["scenes"][first].items() if k != "lines"}
        base_last = {k: v for k, v in staging["scenes"][last].items() if k != "lines"}
        st["scenes"]["00"] = dict(base_first, lines={"0": {"shots": ["megclose", "wide"] if "meg" in base_first else ["wide"]}})
        st["scenes"]["99"] = dict(base_last, lines={"0": {"word": "FULL VIDEO BELOW", "shots": ["wide"]}})
        st["short"] = {"title": sh["title"]}
        (d / "staging.json").write_text(json.dumps(st, indent=1), encoding="utf-8")
        for f in ("voices.json", "cast_looks.json"):
            shutil.copy2(pdir / f, d / f)
        (d / "build").mkdir(exist_ok=True)
        shutil.rmtree(d / "build" / "parts", ignore_errors=True)   # never reuse parts from an older render
        py = sys.executable
        for args in (["voices"], ["shots", "--vertical"], ["stills", "--vertical"], ["render", "--jobs", "8", "--vertical"], ["master"]):
            cmd = [py, "-m", "studio.whatif", args[0], str(d)] + args[1:]
            r = subprocess.run(cmd, capture_output=True, text=True)
            print(sh["id"], args[0], (r.stdout.strip().splitlines() or [""])[-1])
            if r.returncode:
                raise SystemExit(f"{sh['id']} {args[0]} failed: {r.stderr[-800:]}")
        pr = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration:stream=width,height", "-of", "json",
                             str(d / "build" / "final.mp4")], capture_output=True, text=True)
        info = json.loads(pr.stdout)
        print(sh["id"], "final:", info["streams"][0]["width"], "x", info["streams"][0]["height"],
              round(float(info["format"]["duration"]), 1), "s")


def publish(pdir: Path, ep: Path):
    plan = json.loads((pdir / "shorts_plan.json").read_text(encoding="utf-8"))
    out = ep / "build" / "shorts"
    out.mkdir(parents=True, exist_ok=True)
    sj = ep / "shorts.json"
    data = json.loads(sj.read_text(encoding="utf-8")) if sj.exists() else {"shorts": []}
    have = {s["id"] for s in data["shorts"]}
    for sh in plan["shorts"]:
        f = pdir / "shorts" / sh["id"] / "build" / "final.mp4"
        if not f.exists():
            continue
        shutil.copy2(f, out / f"{sh['id']}.mp4")
        dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(f)],
                                   capture_output=True, text=True).stdout.strip())
        entry = {"id": sh["id"], "format": "what-if-v1 native 9:16", "scenes": sh["scenes"], "title": sh["title"],
                 "outro": sh["outro"], "description": sh["description"], "duration_s": round(dur, 1)}
        if sh.get("schedule_at"):
            entry["schedule_at"] = sh["schedule_at"]
        if sh["id"] in have:
            for s in data["shorts"]:
                if s["id"] == sh["id"] and not s.get("youtube_id"):
                    s.update(entry)
        else:
            data["shorts"].append(entry)
    sj.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    print("shorts.json:", [s["id"] for s in data["shorts"]])


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "build":
        build(Path(sys.argv[2]).resolve(), sys.argv[3:] or None)
    elif cmd == "publish":
        publish(Path(sys.argv[2]).resolve(), Path(sys.argv[3]).resolve())
