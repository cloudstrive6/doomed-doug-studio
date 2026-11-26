"""CI driver for What If episodes (new Doomed Doug format, 2026-11-27). The agents write the creative files into
whatif/<slug>/; these commands do the mechanical work and the gates. Every step is safe to re-run.

  py -m studio.whatif_ci prep <wdir>      staging generator (if any), voices, shots, automatic re-framing, preflight
  py -m studio.whatif_ci render <wdir>    full 16:9 render (all cores), master, QC, review sheets every 3 s
  py -m studio.whatif_ci thumbs <wdir>    thumbnails A/B/C from thumbs.json and their feed-size sheet
  py -m studio.whatif_ci shorts <wdir>    the native 9:16 Shorts from shorts_plan.json, each preflighted and QC'd
  py -m studio.whatif_ci gate <wdir>      review score vs the last episode's (channel/whatif_scores.json), QC, preflight
  py -m studio.whatif_ci publish <wdir>   episodes/<NNN-slug>/ for `python -m studio upload` and `shorts upload`
  py -m studio.whatif_ci status           What If folders and their state

Files the agents write in whatif/<slug>/ (format in pipeline/prompts/produce_whatif.md):
  script.md, facts.md, script_review.md, build_staging.py (writes staging.json, cast_looks.json, voices.json),
  packaging.json, thumbs.json, shorts_plan.json, review.json and video_review.md (reviewer), fixes.md (fixer)
"""
from __future__ import annotations

import datetime as dt
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WHATIF = ROOT / "whatif"
LEDGER = ROOT / "channel" / "whatif_scores.json"
CRITERIA = ["hook", "clarity", "polish", "pacing", "story", "packaging"]
SHORT_CRITERIA = ["hook", "readability", "framing", "payoff", "title"]
PY = sys.executable


def _run(args, check=True, **kw):
    print("+", " ".join(str(a) for a in args), flush=True)
    r = subprocess.run([str(a) for a in args], cwd=ROOT, **kw)
    if check and r.returncode:
        raise SystemExit(f"failed ({r.returncode}): {' '.join(str(a) for a in args)}")
    return r


def _state(w: Path) -> dict:
    p = w / "state.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {"history": []}


def _set_state(w: Path, step: str, note: str = "", **extra):
    st = _state(w)
    st["step"] = step
    st.update(extra)
    st["history"].append({"step": step, "at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"), "note": note})
    (w / "state.json").write_text(json.dumps(st, indent=1), encoding="utf-8")


def _jobs():
    return str(max(2, min(12, os.cpu_count() or 4)))


# ------------------------------------------------------------------ prep

def prep(w: Path):
    if (w / "build_staging.py").exists():
        _run([PY, w / "build_staging.py"])
    for f in ("script.md", "staging.json", "cast_looks.json", "voices.json"):
        if not (w / f).exists():
            raise SystemExit(f"{w.name}: {f} missing")
    _run([PY, "-m", "studio.whatif", "parse", w])
    _run([PY, "-m", "studio.whatif", "voices", w])
    _run([PY, "-m", "studio.whatif", "shots", w])
    r = _run([PY, "-m", "studio.whatif_check", w], check=False)
    _set_state(w, "prepped" if r.returncode == 0 else "preflight_failed", "preflight " + ("clean" if r.returncode == 0 else "FAIL"))
    return r.returncode


# ------------------------------------------------------------------ render + QC

def _probe(v: Path):
    pr = json.loads(subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                                    "stream=codec_type,width,height,r_frame_rate:format=duration", "-of", "json", str(v)],
                                   capture_output=True, text=True).stdout)
    vs = next(s for s in pr["streams"] if s["codec_type"] == "video")
    num, den = vs["r_frame_rate"].split("/")
    return float(pr["format"]["duration"]), vs["width"], vs["height"], float(num) / float(den)


def qc(w: Path, vertical=False) -> dict:
    """Technical QC of build/final.mp4 against the playbook targets. Writes build/qc.json, returns it."""
    v = w / "build" / "final.mp4"
    dur, width, height, fps = _probe(v)
    err = lambda args: subprocess.run(args, capture_output=True, text=True).stderr
    lo = err(["ffmpeg", "-hide_banner", "-nostats", "-i", str(v), "-af", "ebur128=peak=true", "-f", "null", "-"])
    lufs = float(re.findall(r"I:\s+(-?[\d.]+) LUFS", lo)[-1])
    tp = float(re.findall(r"Peak:\s+(-?[\d.]+) dBFS", lo)[-1])
    fz = re.findall(r"freeze_duration: ([\d.]+)", err(["ffmpeg", "-hide_banner", "-nostats", "-i", str(v), "-vf",
                                                      "freezedetect=n=0.001:d=2", "-map", "0:v", "-f", "null", "-"]))
    bl = re.findall(r"black_duration:([\d.]+)", err(["ffmpeg", "-hide_banner", "-nostats", "-i", str(v), "-vf",
                                                    "blackdetect=d=0.5:pix_th=0.08", "-an", "-f", "null", "-"]))
    script = (w / "script.md").read_text(encoding="utf-8")
    lines = json.loads((w / "build" / "lines.json").read_text(encoding="utf-8"))["lines"]
    problems, notes = [], {}
    def need(ok, name, val):
        notes[name] = f"{val} {'PASS' if ok else 'FAIL'}"
        if not ok:
            problems.append(f"{name}: {val}")
    if vertical:
        need(15 <= dur <= 60, "length (15 to 60 s)", f"{dur:.1f} s")
        need((width, height) == (1080, 1920), "picture 1080x1920", f"{width}x{height}")
    else:
        need(8 * 60 <= dur <= 14.5 * 60, "length (8 to 14.5 min)", f"{dur / 60:.2f} min")
        need(height >= 1080 and width >= 1920, "picture 1920x1080", f"{width}x{height}")
    need(abs(lufs + 14) <= 1.0, "loudness (-14 LUFS +-1)", f"{lufs} LUFS")
    need(tp <= -1.0, "true peak (<= -1 dBTP)", f"{tp} dBTP")
    need(not fz, "no freeze over 2 s", f"{len(fz)} freezes")
    need(not bl, "no black over 0.5 s", f"{len(bl)} black")
    dashes = script.count("\u2014") + script.count("\u2013")
    need(dashes == 0, "no em or en dashes in script", dashes)
    if not vertical:
        voices = len({l["who"] for l in lines})
        need(voices >= 3, "3 or more voices", voices)
        pk = w / "packaging.json"
        drop = json.loads(pk.read_text(encoding="utf-8")).get("title_drop", "").lower() if pk.exists() else ""
        t_drop = next((l["start"] for l in lines if drop and drop in l["text"].lower()), None)
        need(t_drop is not None and 25 <= t_drop <= 95, "title drop spoken at 25 to 95 s",
             f"{t_drop:.1f} s" if t_drop is not None else f"phrase '{drop}' not found")
    out = {"duration_s": round(dur, 2), "lufs": lufs, "true_peak": tp, "checks": notes, "problems": problems}
    (w / "build" / "qc.json").write_text(json.dumps(out, indent=1), encoding="utf-8")
    return out


def sheets(w: Path, every=3):
    """Contact sheets of the final video every 3 s (the reviewer's input), 4x4 frames per sheet, timestamps burned in."""
    out = w / "build" / "review"
    shutil.rmtree(out, ignore_errors=True)
    out.mkdir(parents=True)
    dur, width, height, _ = _probe(w / "build" / "final.mp4")
    tw, th = (480, 270) if width > height else (240, 426)
    _run(["ffmpeg", "-v", "error", "-i", w / "build" / "final.mp4", "-vf",
          f"fps=1/{every},scale={tw}:{th},drawtext=fontfile=assets/fonts/RussoOne-Regular.ttf:text='%{{pts\\:hms}}':x=6:y=h-30:fontsize=20:fontcolor=white:box=1:boxcolor=black@0.6,"
          f"tile=4x4", "-vsync", "vfr", out / "sheet_%02d.jpg"])
    n = len(list(out.glob("sheet_*.jpg")))
    print(f"{n} review sheets ({every} s apart) in {out}")


def render(w: Path):
    for p in ("parts",):
        shutil.rmtree(w / "build" / p, ignore_errors=True)   # never reuse parts from an older plan
    _run([PY, "-m", "studio.whatif", "render", w, "--jobs", _jobs()])
    _run([PY, "-m", "studio.whatif", "master", w])
    q = qc(w)
    sheets(w)
    print(json.dumps(q["checks"], indent=1))
    _set_state(w, "rendered" if not q["problems"] else "qc_failed", "; ".join(q["problems"]) or "QC clean")
    return 0 if not q["problems"] else 1


# ------------------------------------------------------------------ thumbnails, Shorts

def thumbs(w: Path):
    if not (w / "thumbs.json").exists():
        raise SystemExit(f"{w.name}: thumbs.json missing")
    _run([PY, "-m", "studio.whatif_thumb", w])
    for n in "ABC":
        if not (w / "thumbs" / f"thumb_{n}.png").exists():
            raise SystemExit(f"thumbnail {n} missing")


def shorts(w: Path, only=None):
    if not (w / "shorts_plan.json").exists():
        print("no shorts_plan.json: no Shorts")
        return 0
    _run([PY, "-m", "studio.whatif_shorts", "build", w] + (only or []))
    plan = json.loads((w / "shorts_plan.json").read_text(encoding="utf-8"))
    bad = []
    for sh in plan["shorts"]:
        if only and sh["id"] not in only:
            continue
        d = w / "shorts" / sh["id"]
        r = _run([PY, "-m", "studio.whatif_check", d, "--vertical"], check=False)
        q = qc(d, vertical=True)
        sheets(d, every=2)
        if r.returncode or q["problems"]:
            bad.append(sh["id"])
    _set_state(w, _state(w).get("step", "rendered"), f"shorts built; problems in {bad}" if bad else "shorts built clean",
               shorts_bad=bad)
    return 1 if bad else 0


# ------------------------------------------------------------------ gate

def _ledger():
    if LEDGER.exists():
        return json.loads(LEDGER.read_text(encoding="utf-8"))
    return {"floor": 3.5, "episodes": []}


def target_score() -> float:
    led = _ledger()
    done = [e for e in led["episodes"] if e.get("status") in ("passed", "uploaded")]
    return max(led.get("floor", 3.5), done[-1]["score"] if done else 0)


def _avg(scores: dict, keys) -> float:
    vals = [float(scores[k]) for k in keys if k in scores]
    if len(vals) != len(keys):
        raise SystemExit(f"review.json must score every criterion {keys}; got {sorted(scores)}")
    return round(sum(vals) / len(vals), 2)


def gate(w: Path) -> int:
    """Passes only when QC is clean, preflight has no FAIL, the review scored every criterion, the average is at
    least the previous episode's score, and the reviewer listed no open must-fix. Records the result in the ledger."""
    reasons = []
    q = json.loads((w / "build" / "qc.json").read_text(encoding="utf-8")) if (w / "build" / "qc.json").exists() else None
    if not q or q["problems"]:
        reasons.append("QC: " + ("missing" if not q else "; ".join(q["problems"])))
    pf = w / "build" / "preflight.json"
    if not pf.exists() or json.loads(pf.read_text(encoding="utf-8"))["fails"]:
        reasons.append("preflight has FAIL items")
    rv = w / "review.json"
    if not rv.exists():
        raise SystemExit(f"{w.name}: review.json missing (the reviewer has not run)")
    review = json.loads(rv.read_text(encoding="utf-8"))
    score = _avg(review["scores"], CRITERIA)
    target = target_score()
    if score < target:
        reasons.append(f"review {score} is below the last episode's {target}")
    open_fixes = [m for m in review.get("must_fix", []) if not m.get("done")]
    if open_fixes:
        reasons.append(f"{len(open_fixes)} must-fix item(s) open")
    short_scores = {}
    for sid, sc in (review.get("shorts") or {}).items():
        short_scores[sid] = _avg(sc["scores"], SHORT_CRITERIA)
    passed = not reasons
    led = _ledger()
    led["episodes"] = [e for e in led["episodes"] if not (e["id"] == w.name and e.get("status") != "uploaded")]
    led["episodes"].append({"id": w.name, "score": score, "scores": review["scores"], "target": target,
                            "round": review.get("round", 1), "shorts": short_scores,
                            "date": dt.date.today().isoformat(), "status": "passed" if passed else "held",
                            "reasons": reasons})
    LEDGER.write_text(json.dumps(led, indent=1), encoding="utf-8")
    _set_state(w, "gate_passed" if passed else "gate_held", "; ".join(reasons) or f"review {score} >= {target}", score=score)
    print(f"{w.name}: review {score} (target {target}) -> {'PASS' if passed else 'HOLD: ' + '; '.join(reasons)}")
    return 0 if passed else 1


# ------------------------------------------------------------------ publish into episodes/

def _ts(t, srt=False):
    h, rem = divmod(t, 3600)
    m, s = divmod(rem, 60)
    if srt:
        return f"{int(h):02d}:{int(m):02d}:{int(s):02d},{int((s % 1) * 1000):03d}"
    return f"{int(m)}:{int(s):02d}" if h < 1 else f"{int(h)}:{int(m):02d}:{int(s):02d}"


def publish(w: Path) -> Path:
    """Copy a gated What If episode into episodes/<NNN-slug>/ (stage qc_passed) with exact captions from the voiced
    line timings, chapters, metadata, thumbnails A/B/C and the Shorts, ready for `studio upload` and `shorts upload`."""
    st = _state(w)
    if st.get("step") not in ("gate_passed", "published"):
        raise SystemExit(f"{w.name}: step is {st.get('step')}, expected gate_passed")
    eps = ROOT / "episodes"
    if st.get("episode"):
        ep = eps / st["episode"]
    else:
        nums = [int(d.name[:3]) for d in eps.iterdir() if d.is_dir() and d.name[:3].isdigit()]
        ep = eps / f"{max(nums, default=0) + 1:03d}-whatif-{w.name}"
    (ep / "build").mkdir(parents=True, exist_ok=True)
    L = json.loads((w / "build" / "lines.json").read_text(encoding="utf-8"))
    cues = []
    for l in L["lines"]:
        words = l["text"].split()
        parts = [l["text"]] if len(words) <= 16 else [" ".join(words[:len(words) // 2]), " ".join(words[len(words) // 2:])]
        for i, ptxt in enumerate(parts):
            cues.append((l["start"] + l["dur"] * i / len(parts), l["start"] + l["dur"] * (i + 1) / len(parts), ptxt))
    (ep / "build" / "captions.srt").write_text(
        "\n".join(f"{i + 1}\n{_ts(a, True)} --> {_ts(b, True)}\n{t}\n" for i, (a, b, t) in enumerate(cues)), encoding="utf-8")
    pk = json.loads((w / "packaging.json").read_text(encoding="utf-8"))
    first = {}
    for l in L["lines"]:
        first.setdefault(l["scene"], l["start"])
    chs = pk.get("chapters") or []
    ch = [f"0:00 {chs[0][1]}"] + [f"{_ts(max(0, first[n] - 0.3))} {name}" for n, name in chs[1:] if n in first] if chs else []
    (ep / "build" / "chapters.txt").write_text("\n".join(ch), encoding="utf-8")
    review = json.loads((w / "review.json").read_text(encoding="utf-8"))
    meta = {
        "title": pk["title"], "alt_titles": pk.get("alt_titles", []),
        "format": f"what-if-v1 (toon engine, CI, whatif/{w.name})",
        "description": pk["description"].replace("{{CHAPTERS}}", "\n".join(ch)),
        "tags": pk.get("tags", []), "playlist": pk.get("playlist", "ocean"), "paid_promotion": False,
        "review": {"independent_video_review": f"{st.get('score')} of 5 (round {review.get('round', 1)})",
                   "file": f"whatif/{w.name}/video_review.md"},
        "thumbnail_tests": {"A": "build/thumbnail.png", "B": "build/thumbnail_B.png", "C": "build/thumbnail_C.png",
                            "note": "Bryce 2026-11-27: all three in YouTube Test & Compare"},
    }
    mp = ep / "metadata.json"
    old = json.loads(mp.read_text(encoding="utf-8")) if mp.exists() else {}
    if old.get("youtube_id"):
        print(f"{ep.name} is already uploaded; metadata kept")
    else:
        mp.write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")
    for src, dst in (("build/final.mp4", "build/final.mp4"), ("thumbs/thumb_A.png", "build/thumbnail.png"),
                     ("thumbs/thumb_B.png", "build/thumbnail_B.png"), ("thumbs/thumb_C.png", "build/thumbnail_C.png"),
                     ("script.md", "script.md"), ("facts.md", "facts.md"), ("script_review.md", "script_review.md"),
                     ("video_review.md", "video_review.md")):
        if (w / src).exists():
            shutil.copy2(w / src, ep / dst)
    if (w / "shorts_plan.json").exists():
        from .whatif_shorts import publish as shorts_publish
        shorts_publish(w, ep)
        held = set(_state(w).get("shorts_bad") or [])
        held |= {sid for sid, sc in (review.get("shorts") or {}).items() if _avg(sc["scores"], SHORT_CRITERIA) < 3.5}
        if held:   # a Short that failed its checks or scored under 3.5 is not uploaded
            sj = ep / "shorts.json"
            data = json.loads(sj.read_text(encoding="utf-8"))
            data["shorts"] = [s for s in data["shorts"] if s["id"] not in held or s.get("youtube_id")]
            sj.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
            print("Shorts held back:", sorted(held))
    from .__main__ import get_stage, set_stage
    if get_stage(ep) not in ("qc_passed", "uploaded"):
        set_stage(ep, "qc_passed", f"What If CI gate: review {st.get('score')}")
    ideas = ROOT / "data" / "whatif_ideas.md"
    if ideas.exists():
        t = ideas.read_text(encoding="utf-8")
        ideas.write_text(t.replace(f"in-production ({w.name})", f"done ({ep.name[:3]})"), encoding="utf-8")
    _set_state(w, "published", ep.name, episode=ep.name)
    print("episode folder ready:", ep)
    return ep


def status():
    led = _ledger()
    print(f"target score for the next episode: {target_score()}")
    for d in sorted(WHATIF.iterdir()) if WHATIF.exists() else []:
        if d.is_dir():
            st = _state(d)
            print(f"{d.name:40} {st.get('step', 'new'):18} {st.get('score', '')}")
    for e in led["episodes"][-5:]:
        print(f"  ledger: {e['id']} {e['score']} ({e['status']}, {e['date']})")


def main(argv):
    cmd = argv[0]
    if cmd == "status":
        return status()
    w = Path(argv[1])
    w = (w if w.is_absolute() else ROOT / w).resolve()
    fn = {"prep": prep, "render": render, "thumbs": thumbs, "gate": gate, "publish": publish,
          "qc": lambda w: print(json.dumps(qc(w), indent=1)), "sheets": sheets}.get(cmd)
    if cmd == "shorts":
        return shorts(w, argv[2:] or None)
    if fn is None:
        raise SystemExit(__doc__)
    r = fn(w)
    return r if isinstance(r, int) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]) or 0)
