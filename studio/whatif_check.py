"""Pre-review checks for What If episodes and Shorts: the reviewer's known must-fixes, caught by code before
anyone watches the render (Bryce 2026-11-27: every video must beat the last review score, so a fault the reviewer
found once must never reach the reviewer again).

  py -m studio.whatif_check <episode_dir> [--vertical]      needs build/lines.json and build/shots.json

Writes build/preflight.json and prints one line per problem. Exit code 1 when any FAIL is found.

FAIL checks (each one cost score in a past review):
  card_over_actor     a science card is up while a visible character's head sits under it (any shot of the line)
  closeup_hidden      a close-up or medium shot on a character who is hidden on that line or not in the scene
  head_cut_top        a character's head is cut by the top edge in a wide or group shot
  meg_missing         a shark shot in a scene that has no shark
  unknown_set         a set id that is not registered
  speaker_offscreen   a character line where the speaker is not on screen at any point of the line (and no
                      shot of the line is a shark close-up or borrowed from another scene)
WARN checks (the fixer looks, the reviewer decides):
  said_not_shown      a line names a prop the engine can draw, but no such prop is on screen in that scene
  long_hold           one shot holds more than 4.5 s
  card_too_short      a card is on screen for under 2.5 s (too short to read)
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from . import toon_held as HP
from . import toon_props as P
from . import toon_sets as S
from . import whatif as WF

HEAD_TOP, HEAD_BOT, HEAD_HALF_W = 410, 255, 80      # world units above the ground line, times the actor scale
SIT_TOP = 300
SAMPLES = (0.0, 0.5, 1.0)

# words that name each drawable prop (prop id -> spoken words); ids not listed use their own name
PROP_WORDS = {
    "fish_rod": ["fishing rod", "rod"], "phone_ring": ["ring light"], "phone": ["phone"], "torch": ["torch", "flashlight"],
    "melon": ["watermelon", "melon"], "melon_stick": ["watermelon", "melon"], "tin": ["sardine", "sardines", "tin"],
    "contract": ["contract"], "clipboard": ["clipboard", "form"], "net": ["net"], "bucket": ["bucket"],
    "kayak": ["kayak"], "ute": ["ute"], "fish_truck": ["truck"], "truck": ["truck"], "deckchair": ["deckchair"],
    "fridge": ["fridge"], "receipts": ["receipt", "receipts"], "coast_map": ["map"], "great_white": ["great white"],
    "fish_school": ["school of fish"], "rental_boat": ["boat"], "boat": ["boat"], "whale": ["whale"],
    "fossil_tooth": ["fossil", "tooth"], "tooth": ["tooth"], "bathtub": ["bath", "bathtub"], "basket": ["basket"],
    "paddle": ["paddle"], "envelope": ["envelope", "letter"], "crayon": ["crayon"], "lamp_post": ["lamp post"],
}
IGNORE_IN_NARRATION = {"tooth", "boat", "form", "map", "letter"}   # too common in plain narration to demand on screen


def _actors_in_shot(st, spec, frame_label):
    hide = set(spec.get("hide") or [])
    if frame_label == "megclose" or (frame_label == "meg" and WF.vertical()):
        hide |= set(st.get("chars", {}))
    return [w for w in st.get("chars", {}) if w not in hide]


def _head_box(a, ground, f, spec, who):
    """Screen-independent world box of a character's head at fraction f of the shot (moves interpolated)."""
    x, y = a["x"], a.get("y", ground)
    mv = (spec.get("move") or {}).get(who)
    if mv:
        k = WF.T.ease(min(1.0, f / 0.8))
        x = x + (mv[0] - x) * k
        if len(mv) > 1:
            y = a.get("y", 0) + (mv[1] - a.get("y", 0)) * k
    s = a.get("scale", 1.0)
    sitting = a.get("pose") in ("sit", "sit_talk", "sleep")
    pose = (spec.get("pose") or {}).get(who)
    if pose in ("sit", "sit_talk", "sleep"):
        sitting = True
    top = y - (SIT_TOP if sitting else HEAD_TOP) * s
    bot = y - (HEAD_BOT - (110 if sitting else 0)) * s
    return x - HEAD_HALF_W * s, top, x + HEAD_HALF_W * s, bot


def _to_screen(box, cx, cy, z):
    W, H = WF.W, WF.H
    x0, y0 = cx - W / 2 / z, cy - H / 2 / z
    return ((box[0] - x0) * z, (box[1] - y0) * z, (box[2] - x0) * z, (box[3] - y0) * z)


def _overlap(a, b):
    w = min(a[2], b[2]) - max(a[0], b[0])
    h = min(a[3], b[3]) - max(a[1], b[1])
    if w <= 0 or h <= 0:
        return 0.0
    return w * h / max(1.0, (a[2] - a[0]) * (a[3] - a[1]))


def card_rect():
    """Screen rectangle the science card covers (matches draw_overlays)."""
    if WF.vertical():
        w, h = 760 * 1.25, 420 * 1.25
        return (WF.W / 2 - w / 2, 1290 - h / 2, WF.W / 2 + w / 2, 1290 + h / 2)
    return (1450 - 380, 470 - 210, 1450 + 380, 470 + 210)


def _scene_st(staging, spec):
    st = dict(staging["scenes"].get(spec["scene"], {}))
    if spec.get("meg") and "meg" in st:
        st["meg"] = {**st["meg"], **spec["meg"]}
    return st


def card_hits(staging, spec, cards) -> list[str]:
    """Characters whose heads sit under a science card at any sampled moment of this shot."""
    up = [c for c in cards if c["t0"] < spec["t1"] and c["t1"] > spec["t0"]]
    if not up:
        return []
    st = _scene_st(staging, spec)
    set_id = spec.get("set") or st.get("set")
    crect = card_rect()
    hits = []
    for f in SAMPLES:
        t_here = spec["t0"] + (spec["t1"] - spec["t0"]) * f
        if not any(c["t0"] <= t_here + 0.05 and c["t1"] >= t_here - 0.05 for c in up):
            continue
        cx, cy, z, ground = WF.camera(st, spec, set_id, f)
        for who in _actors_in_shot(st, spec, spec["frame"]):
            box = _to_screen(_head_box(st["chars"][who], ground, f, spec, who), cx, cy, z)
            if _overlap(box, crect) > 0.25 and who not in hits:
                hits.append(who)
    return hits


def fix_card_shots(staging, shots) -> list[str]:
    """Re-frame any shot that would put a science card over a character's head: first clean option of a shark
    close-up, then a medium or close-up on the leftmost visible character. Shots marked keep are left alone."""
    S.register_aliases(staging.get("aliases", {}))
    cards = WF._timeline_state(shots)[0]
    log = []
    for spec in shots:
        if spec.get("kind") == "daywipe" or spec.get("line") == "END" or spec.get("keep"):
            continue
        hits = card_hits(staging, spec, cards)
        if not hits:
            continue
        st = _scene_st(staging, spec)
        vis = sorted(_actors_in_shot(st, spec, "wide"), key=lambda a: st["chars"][a]["x"])
        cands = (["megclose"] if "meg" in st else []) + [f"medium:{a}" for a in vis] + [f"close:{a}" for a in vis]
        for c in cands:
            if c == spec["frame"]:
                continue
            if not card_hits(staging, dict(spec, frame=c), cards):
                log.append(f"{spec['line']} t={spec['t0']}: {spec['frame']} -> {c} (card over {', '.join(hits)})")
                spec["frame"] = c
                spec["auto_fixed"] = "card"
                break
    return log


def check(pdir: Path) -> dict:
    staging = json.loads((pdir / "staging.json").read_text(encoding="utf-8"))
    S.register_aliases(staging.get("aliases", {}))
    shots = json.loads((pdir / "build" / "shots.json").read_text(encoding="utf-8"))["shots"]
    lines = {f"{l['scene']}_{l['i']:02d}": l for l in
             json.loads((pdir / "build" / "lines.json").read_text(encoding="utf-8"))["lines"]}
    cards, _, _, _, _ = WF._timeline_state(shots)
    crect = card_rect()
    fails, warns = [], []
    seen = set()

    def add(lst, kind, spec, msg):
        key = (kind, spec.get("line"), msg)
        if key in seen:
            return
        seen.add(key)
        lst.append({"check": kind, "line": spec.get("line"), "t": round(spec.get("t0", 0), 2), "frame": spec.get("frame"),
                    "msg": msg})

    speaker_seen = {}
    for spec in shots:
        if spec.get("kind") == "daywipe" or spec.get("line") == "END":
            continue
        st = _scene_st(staging, spec)
        set_id = spec.get("set") or st.get("set")
        try:
            S._resolve(set_id)
            if S._resolve(set_id) not in S.SETS:
                raise KeyError(set_id)
        except Exception:
            add(fails, "unknown_set", spec, f"set '{set_id}' is not registered in toon_sets.SETS or the aliases")
            continue
        fr = spec["frame"]
        if fr in ("meg", "megclose") and "meg" not in st:
            add(fails, "meg_missing", spec, f"shark shot '{fr}' in scene {spec['scene']} which has no shark")
        if fr.startswith(("close:", "medium:")):
            who = fr.split(":", 1)[1]
            if who != "meg" and (who not in st.get("chars", {}) or who in set(spec.get("hide") or [])):
                add(fails, "closeup_hidden", spec, f"{fr} but {who} is hidden or not in scene {spec['scene']}")
        if spec["t1"] - spec["t0"] > 4.5:
            add(warns, "long_hold", spec, f"one shot holds {spec['t1'] - spec['t0']:.1f} s")
        card_up = [c for c in cards if c["t0"] < spec["t1"] and c["t1"] > spec["t0"]]
        actors = _actors_in_shot(st, spec, fr)
        lab = fr
        if WF.vertical() and fr == "wide" and st.get("chars"):
            lab = "medium"
        for f in SAMPLES:
            cx, cy, z, ground = WF.camera(st, spec, set_id, f)
            t_here = spec["t0"] + (spec["t1"] - spec["t0"]) * f
            for who in actors:
                box = _to_screen(_head_box(st["chars"][who], ground, f, spec, who), cx, cy, z)
                on_screen = box[2] > 0 and box[0] < WF.W and box[3] > 0 and box[1] < WF.H
                if who == spec["who"] and on_screen:
                    speaker_seen[spec["line"]] = True
                if not on_screen:
                    continue
                cut = max(0.0, -box[1]) / max(1.0, box[3] - box[1])   # share of the head above the frame
                if cut > 0.03 and box[3] > 0 and not lab.startswith(("close:", "medium")) and fr != "megclose":
                    add(fails if cut > 0.25 else warns, "head_cut_top", spec,
                        f"{who}'s head is {cut:.0%} cut by the top edge ({fr})")
        for who in card_hits(staging, spec, cards):
            add(fails, "card_over_actor", spec, f"science card covers {who}'s head ({fr})")
        ln = lines.get(spec["line"])
        if ln and spec["who"] not in ("narrator",) and (fr == "megclose" or spec.get("borrowed") or fr.startswith("pt:")):
            speaker_seen[spec["line"]] = True
    for lid, ln in lines.items():
        if ln["who"] == "narrator" or speaker_seen.get(lid):
            continue
        st = staging["scenes"].get(ln["scene"], {})
        if ln["who"] in st.get("chars", {}):
            spec = next((s for s in shots if s.get("line") == lid), {"line": lid, "t0": ln["start"], "frame": "?"})
            add(fails, "speaker_offscreen", spec, f"{ln['who']} speaks but is never on screen during the line")
    for c in cards:
        if c["t1"] - c["t0"] < 2.5:
            add(warns, "card_too_short", {"line": "?", "t0": c["t0"], "frame": "card"},
                f"card '{c['card'].get('head', '')}' is up {c['t1'] - c['t0']:.1f} s")
    # said but not shown
    drawable = set(P.PROP_DRAW) | set(HP.HELD) | set(getattr(S, "EXTRA_PROPS", {}))
    for lid, ln in lines.items():
        st = staging["scenes"].get(ln["scene"], {})
        present = {p.get("id") for p in st.get("props", [])}
        present |= {a.get("holds") for a in st.get("chars", {}).values() if a.get("holds")}
        for spec in (s for s in shots if s.get("line") == lid):
            present |= {p.get("id") for p in (spec.get("props_add") or [])}
            present |= set((spec.get("holds") or {}).values())
        present |= set(st.get("shows", []))
        text = " " + re.sub(r"[^a-z ]", " ", ln["text"].lower()) + " "
        for pid in drawable:
            words = PROP_WORDS.get(pid, [pid.replace("_", " ")])
            hit = next((w for w in words if f" {w} " in text or f" {w}s " in text), None)
            if not hit or (ln["who"] == "narrator" and hit in IGNORE_IN_NARRATION):
                continue
            same = {q for q, ws in PROP_WORDS.items() if hit in ws} | {pid}
            if not (same & present):
                spec = next((s for s in shots if s.get("line") == lid), {"line": lid, "t0": ln["start"], "frame": "?"})
                add(warns, "said_not_shown", spec, f"line says '{hit}' but no {'/'.join(sorted(same))} is on screen "
                                                   f"(add the prop, or list it under the scene's \"shows\" if the set draws it)")
    out = {"fails": fails, "warns": warns, "ok": not fails,
           "counts": {"fails": len(fails), "warns": len(warns), "shots": len(shots)}}
    (pdir / "build" / "preflight.json").write_text(json.dumps(out, indent=1), encoding="utf-8")
    return out


def main(argv):
    pdir = Path(argv[0]).resolve()
    if "--vertical" in argv:
        WF.set_canvas(1080, 1920)
        WF.VERTICAL_SHOTS = True
    out = check(pdir)
    for f in out["fails"]:
        print(f"FAIL {f['check']:<18} {f['line']:<8} t={f['t']:>7} {f['msg']}")
    for w in out["warns"]:
        print(f"WARN {w['check']:<18} {w['line']:<8} t={w['t']:>7} {w['msg']}")
    print(f"preflight: {out['counts']['fails']} fail, {out['counts']['warns']} warn over {out['counts']['shots']} shots")
    return 0 if out["ok"] else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
