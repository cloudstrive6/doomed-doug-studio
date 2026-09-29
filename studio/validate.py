"""Mechanical checks the agents must pass before handing work on. Returns a list of problems."""
from __future__ import annotations

import json
import re
from pathlib import Path

from .doug import EXPRESSIONS, POSES
from .paint import LIBRARY_DIR

KNOWN = {"line", "curve", "arrow", "poly", "polygon", "ellipse", "circle", "rect", "fill", "spray", "text",
         "label", "group", "asset", "doug", "bands", "speech"}


def _walk(elements, where, problems):
    for i, el in enumerate(elements or []):
        w = f"{where}[{i}]"
        t = el.get("type")
        if t not in KNOWN:
            problems.append(f"{w}: unknown element type {t!r}")
            continue
        if t == "asset" and not (LIBRARY_DIR / f"{el.get('name')}.json").exists():
            problems.append(f"{w}: asset '{el.get('name')}' missing from assets/library (illustrator must draw it)")
        if t == "doug":
            for p in (el.get("pose") if isinstance(el.get("pose"), list) else [el.get("pose", "stand")]):
                if p not in POSES:
                    problems.append(f"{w}: unknown Doug pose {p!r} (valid: {', '.join(POSES)})")
            for x in (el.get("expression") if isinstance(el.get("expression"), list) else [el.get("expression", "neutral")]):
                if x not in EXPRESSIONS:
                    problems.append(f"{w}: unknown expression {x!r} (valid: {', '.join(EXPRESSIONS)})")
        if t == "group":
            _walk(el.get("elements"), w + ".elements", problems)
        if "appear" in el and not (0 <= float(el["appear"]) < 1):
            problems.append(f"{w}: appear must be a fraction in [0, 1)")


def validate_shotlist(ep_dir: Path) -> list[str]:
    problems = []
    p = ep_dir / "shotlist.json"
    if not p.exists():
        return ["shotlist.json missing"]
    try:
        sl = json.loads(p.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return [f"shotlist.json is not valid JSON: {e}"]
    ids = set()
    words = 0
    doug_shots = 0
    for n, shot in enumerate(sl.get("shots", [])):
        sid = shot.get("id", f"#{n}")
        if sid in ids:
            problems.append(f"{sid}: duplicate id")
        ids.add(sid)
        if "scene" not in shot:
            problems.append(f"{sid}: no scene")
            continue
        _walk(shot["scene"].get("elements"), f"{sid}.elements", problems)
        words += len(shot.get("narration", "").split())
        if len(shot.get("narration", "").split()) > 45:
            problems.append(f"{sid}: narration over 45 words; split into more shots (keep visuals changing)")
        if any(e.get("type") == "doug" for e in shot["scene"].get("elements", [])):
            doug_shots += 1
    if not sl.get("shots"):
        problems.append("no shots")
    else:
        share = doug_shots / len(sl["shots"])
        if share < 0.5:
            problems.append(f"Doug appears in only {share:.0%} of shots; he should be in at least half")
    minutes = words / 160
    if minutes < 12:
        problems.append(f"script is ~{minutes:.1f} min at 160 wpm; target 15-20")
    script = ep_dir / "script.md"
    if script.exists():
        sw = len(re.sub(r"\[[^\]]*\]|#.*", "", script.read_text(encoding="utf-8")).split())
        if words < sw * 0.9:
            problems.append(f"shotlist narration ({words} words) drops >10% of the approved script ({sw} words)")
    return problems


def validate_metadata(ep_dir: Path) -> list[str]:
    p = ep_dir / "metadata.json"
    if not p.exists():
        return ["metadata.json missing"]
    m = json.loads(p.read_text(encoding="utf-8"))
    problems = []
    t = m.get("title", "")
    if not t:
        problems.append("title missing")
    if len(t) > 70:
        problems.append(f"title is {len(t)} chars (keep <= 70 so it isn't truncated)")
    if len(m.get("description", "")) < 200:
        problems.append("description under 200 chars")
    if not (ep_dir / "thumbnail.json").exists():
        problems.append("thumbnail.json missing")
    if sum(len(x) for x in m.get("tags", [])) > 480:
        problems.append("tags exceed 500 characters total")
    return problems
