"""What If pilot pipeline: script.md -> voiced lines -> auto-directed shots -> toon render -> mastered MP4.

  py -m studio.whatif voices <pilot_dir>        voice every line (Chirp 3 HD, cached), write lines.json
  py -m studio.whatif shots <pilot_dir>         build shots.json from script + staging + line timings
  py -m studio.whatif stills <pilot_dir>        one still per shot into build/stills (contact sheets)
  py -m studio.whatif render <pilot_dir> [--jobs N] [--limit N]
  py -m studio.whatif master <pilot_dir>        mix voice, music bed, effects; mux the final MP4

Pilot only (branch whatif-pilot). Nothing here uploads anything.
"""
from __future__ import annotations

import json
import math
import random
import re
import subprocess
import sys
import wave
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

from . import toon as T
from . import toon_props as P
from . import toon_sets as S
from . import toon_held as HP

ROOT = Path(__file__).resolve().parent.parent
W, H, FPS = 1920, 1080, 30
SR = 24000
NAVY, RED, YEL, CREAM = "#1e2a44", "#e0201b", "#f6b73c", "#fff8ea"

# ------------------------------------------------------------------ script parsing

EMO_MAP = {"delighted": "happy", "hyped": "excited", "flat": "deadpan", "fond": "soft", "panting": "tired",
           "panicked": "panic", "dizzy": "confused", "presenter voice": "excited", "dry": "deadpan", "writing": "deadpan",
           "quiet": "sad", "sleepy": "tired", "paddling hard": "excited", "cheering": "excited", "realising": "amazed",
           "tearful": "happy", "clinging to the kayak": "scared", "spotting doug": "excited", "whispering to phone": "whisper",
           "to phone": "excited", "counting on his fingers": "confused", "eager": "excited", "waving": "soft"}


def norm_emo(e):
    e = (e or "").strip().lower()
    e = EMO_MAP.get(e, e)
    return e if e in T.EMOTIONS else "neutral"


LINE_RE = re.compile(r"^([A-Z][A-Z0-9_]*)\s*(?:\[([^\]]+)\])?\s*:\s*(.+)$")


def parse_script(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    title = re.search(r"^# (.+)$", text, re.M).group(1).strip()
    out = {"title": title, "cast": {}, "sets": {}, "props": {}, "scenes": []}

    def table(section):
        m = re.search(rf"^## {section}\s*\n(.*?)(?=^## )", text, re.M | re.S)
        rows = []
        if not m:
            return rows
        for ln in m.group(1).splitlines():
            if ln.startswith("|") and not re.match(r"^\|\s*-", ln):
                cells = [c.strip() for c in ln.strip().strip("|").split("|")]
                rows.append(cells)
        return rows[1:]
    for r in table("CAST"):
        out["cast"][r[0]] = {"name": r[1], "role": r[2] if len(r) > 2 else "", "voice": r[3] if len(r) > 3 else ""}
    for r in table("SETS"):
        out["sets"][r[0]] = r[1] if len(r) > 1 else ""
    for r in table("PROPS"):
        out["props"][r[0]] = r[1] if len(r) > 1 else ""
    scene = None
    pending = {}
    for raw in text.splitlines():
        ln = raw.strip()
        m = re.match(r"^## SCENE (\d+)\s*\|\s*set:\s*([a-z0-9_]+)\s*\|\s*day:\s*([0-9-]+)", ln)
        if m:
            if scene is not None and scene["lines"] and pending:
                for k in ("card", "word"):
                    if k in pending:
                        scene["lines"][-1].setdefault(k, pending[k])
            pending = {}
            scene = {"n": m.group(1).zfill(2), "set": m.group(2), "day": None if m.group(3) == "-" else int(m.group(3)),
                     "directions": [], "lines": []}
            out["scenes"].append(scene)
            continue
        if scene is None or not ln:
            continue
        if ln.startswith("["):
            scene["directions"].append(ln.strip("[]"))
            pending.setdefault("dir", []).append(ln.strip("[]"))
            continue
        if ln.startswith("CARD:"):
            parts = [p.strip() for p in ln[5:].split("|")]
            card = {"head": parts[0], "fact": parts[1] if len(parts) > 1 else "", "source": ""}
            for p in parts[2:]:
                if p.upper().startswith("SOURCE:"):
                    card["source"] = p.split(":", 1)[1].strip()
            pending["card"] = card
            continue
        if ln.startswith("WORD:"):
            pending["word"] = ln[5:].strip()
            continue
        m = LINE_RE.match(ln)
        if m and m.group(1).lower() in out["cast"]:
            item = {"who": m.group(1).lower(), "emo": norm_emo(m.group(2)), "text": m.group(3).strip()}
            item.update({k: v for k, v in pending.items()})
            pending = {}
            scene["lines"].append(item)
    return out


# ------------------------------------------------------------------ voices

def load_voice_map(pdir: Path) -> dict:
    return json.loads((pdir / "voices.json").read_text(encoding="utf-8"))


def _pcm_to_np(pcm: bytes) -> np.ndarray:
    return np.frombuffer(pcm, dtype=np.int16).astype(np.float32) / 32768.0


def _trim(x: np.ndarray, thr=0.006) -> np.ndarray:
    idx = np.where(np.abs(x) > thr)[0]
    if len(idx) == 0:
        return x
    a = max(0, idx[0] - int(0.03 * SR))
    b = min(len(x), idx[-1] + int(0.08 * SR))
    return x[a:b]


def cmd_voices(pdir: Path):
    from . import tts
    from .config import load_config
    sc = parse_script(pdir / "script.md")
    vmap = load_voice_map(pdir)
    prons = load_config()["voice"].get("pronunciations", []) + vmap.get("_pronunciations", [])
    cache = ROOT / ".cache" / "tts"
    lines = []
    t = 0.6
    clips_dir = pdir / "build" / "clips"
    clips_dir.mkdir(parents=True, exist_ok=True)
    real = True
    for s in sc["scenes"]:
        if lines:
            t += 0.35  # scene change breath
        for i, ln in enumerate(s["lines"]):
            v = dict(vmap[ln["who"]])
            v["pronunciations"] = prons
            pcm, ok = tts.synthesize(ln["text"], v, cache)
            real = real and ok
            x = _trim(_pcm_to_np(pcm))
            name = f"{s['n']}_{i:02d}.npy"
            np.save(clips_dir / name, x)
            dur = len(x) / SR
            lines.append({"scene": s["n"], "i": i, "who": ln["who"], "emo": ln["emo"], "text": ln["text"],
                          "start": round(t, 3), "dur": round(dur, 3), "clip": name,
                          **{k: ln[k] for k in ("card", "word", "dir") if k in ln}})
            gap = 0.16 if ln["who"] != "narrator" else 0.22
            if i + 1 < len(s["lines"]) and s["lines"][i + 1]["who"] == ln["who"]:
                gap = 0.12
            t += dur + gap
    total = t + 0.8
    (pdir / "build" / "lines.json").write_text(json.dumps({"total": round(total, 3), "real_voice": real,
                                                           "lines": lines}, indent=1), encoding="utf-8")
    words = sum(len(l["text"].split()) for l in lines)
    print(f"{len(lines)} lines, {words} words, {total / 60:.2f} min, {words / (total / 60):.0f} wpm, real voice: {real}")


def envelope(x: np.ndarray) -> np.ndarray:
    hop = SR // FPS
    n = max(1, len(x) // hop)
    rms = np.sqrt(np.mean(x[: n * hop].reshape(n, hop) ** 2, axis=1) + 1e-9)
    ref = np.percentile(rms, 90) + 1e-6
    e = np.clip((rms - 0.12 * ref) / (0.8 * ref), 0, 1)
    out = e.copy()
    for k in range(1, len(e)):
        out[k] = max(e[k], out[k - 1] * 0.55)
    return out


# ------------------------------------------------------------------ shots (auto director)

def _scene_staging(staging: dict, n: str) -> dict:
    return staging.get("scenes", {}).get(n, {})


def cmd_shots(pdir: Path):
    sc = parse_script(pdir / "script.md")
    staging = json.loads((pdir / "staging.json").read_text(encoding="utf-8"))
    S.register_aliases(staging.get("aliases", {}))
    L = json.loads((pdir / "build" / "lines.json").read_text(encoding="utf-8"))
    lines = L["lines"]
    rnd = random.Random(7)
    shots = []
    seen_names = set()
    by_scene = {}
    for ln in lines:
        by_scene.setdefault(ln["scene"], []).append(ln)
    scene_order = [s["n"] for s in sc["scenes"]]
    prev_day = None
    for si, n in enumerate(scene_order):
        st = _scene_staging(staging, n)
        sdef = next(s for s in sc["scenes"] if s["n"] == n)
        sl = by_scene.get(n, [])
        if not sl:
            continue
        s_start = sl[0]["start"] - (0.35 if si else 0.6)
        s_end = (by_scene[scene_order[si + 1]][0]["start"] - 0.35) if si + 1 < len(scene_order) else L["total"]
        day = sdef["day"]
        actors = list(st.get("chars", {}).keys())
        # day transition card
        cursor = max(0.0, s_start)
        if day is not None and day != prev_day and si > 0 and st.get("day_wipe", True):
            shots.append({"t0": cursor, "t1": cursor + 0.0, "kind": "daywipe", "day": day, "scene": n})
        prev_day = day if day is not None else prev_day
        overrides = st.get("lines", {})
        for li, ln in enumerate(sl):
            t0 = ln["start"] if li else cursor
            t1 = sl[li + 1]["start"] if li + 1 < len(sl) else s_end
            ov = overrides.get(str(li), {})
            vis = [a for a in actors if a not in set(ov.get("hide") or [])]
            plan = ov.get("shots") or _auto_cover(ln, vis, st, t1 - t0, rnd, ov)
            if ov.get("shots") and ln.get("card") and "meg" in st and plan[0] in ("meg", "wide") and not ov.get("keep_shots"):
                plan = ["megclose"] + plan[1:]
            # split the line's time across its planned shots
            k = len(plan)
            bounds = [t0 + (t1 - t0) * j / k for j in range(k + 1)]
            for j, shot in enumerate(plan):
                sc_n = n
                if "|" in shot:
                    sc_n, shot = shot.split("|", 1)
                sset = staging["scenes"].get(sc_n, st).get("set", sdef["set"])
                spec = {"t0": round(bounds[j], 3), "t1": round(bounds[j + 1], 3), "scene": sc_n, "set": sset,
                        "day": day, "line": f"{n}_{li:02d}", "who": ln["who"], "emo": ln["emo"], "frame": shot}
                if sc_n != n:
                    spec["borrowed"] = True
                if j == 0:
                    if ln.get("card"):
                        spec["card"] = {**ln["card"], **({"art": ov["card_art"]} if ov.get("card_art") else {})}
                    if ln.get("word") and not ov.get("noword"):
                        spec["word"] = ln["word"]
                    if ov.get("word"):
                        spec["word"] = ov["word"]
                    if ln["who"] not in ("narrator",) and ln["who"] not in seen_names and ln["who"] in staging.get("name_cards", {}):
                        spec["namecard"] = ln["who"]
                        seen_names.add(ln["who"])
                    if ov.get("title"):
                        spec["title"] = ov["title"]
                spec["card_on"] = bool(ln.get("card"))
                if ov.get("noday"):
                    spec["day"] = None
                if ov.get("as_scene"):
                    spec["scene"] = ov["as_scene"]
                    spec["set"] = staging["scenes"][ov["as_scene"]].get("set")
                for key in ("pose", "move", "meg", "fx", "props_add", "hide", "holds"):
                    if key in ov:
                        spec[key] = ov[key]
                shots.append(spec)
    total = L["total"]
    if "END" in staging.get("scenes", {}):
        shots.append({"t0": round(total, 3), "t1": round(total + 12.0, 3), "scene": "END", "set": staging["scenes"]["END"]["set"],
                      "day": None, "line": "END", "who": "narrator", "emo": "neutral", "frame": "wide", "fx": ["endslate"]})
        total += 12.0
    (pdir / "build" / "shots.json").write_text(json.dumps({"total": total, "shots": shots}, indent=1), encoding="utf-8")
    cuts = sum(1 for s in shots if s.get("kind") != "daywipe")
    print(f"{len(shots)} shots, {cuts / (L['total'] / 60):.1f} cuts a minute over {L['total'] / 60:.2f} min")


def _auto_cover(ln, actors, st, dur, rnd, ov):
    """Coverage rules: speakers get a close-up, listeners a reaction, narrator alternates wide / subject.
    Long lines are split so no shot holds more than ~2.4 s (target 25 to 30 cuts a minute)."""
    who = ln["who"]
    focus = ov.get("focus")
    n = max(1, round(dur / 2.2))
    plan = []
    has_meg = "meg" in st
    for j in range(n):
        if who != "narrator" and who in actors:
            if j % 2 == 0:
                plan.append(f"close:{who}" if j == 0 or rnd.random() < 0.6 else f"medium:{who}")
            else:
                others = [a for a in actors if a != who] + (["megclose"] if has_meg else [])
                pick = rnd.choice(others) if others else None
                plan.append(("megclose" if pick == "megclose" else f"close:{pick}") if pick and rnd.random() < 0.55 else "wide")
        else:
            opts = ["wide"]
            if focus:
                opts = [focus] * 2 + opts
            if has_meg:
                opts += ["meg", "megclose"]
            for a in actors:
                opts.append(f"medium:{a}")
            pick = rnd.choice(opts)
            if plan and pick == plan[-1]:
                pick = "wide" if pick != "wide" else (opts[-1] if len(opts) > 1 else "wide")
            plan.append(pick)
    if ln.get("card") and plan and not focus:
        # science cards sit on the right: put the shark or a wide under them, never a speaker's close-up
        left = sorted(actors, key=lambda a: st["chars"][a]["x"])
        plan[0] = "megclose" if has_meg else (f"medium:{left[0]}" if left else "wide")
    return plan


# ------------------------------------------------------------------ rendering

class Ctx:
    def __init__(self, pdir: Path):
        self.pdir = pdir
        self.staging = json.loads((pdir / "staging.json").read_text(encoding="utf-8"))
        S.register_aliases(self.staging.get("aliases", {}))
        self.lines = {f"{l['scene']}_{l['i']:02d}": l for l in
                      json.loads((pdir / "build" / "lines.json").read_text(encoding="utf-8"))["lines"]}
        self.env = {}
        self.cast = json.loads((pdir / "cast_looks.json").read_text(encoding="utf-8"))
        self.looks = {k: T.Look(**{a: b for a, b in v.items() if not a.startswith("_")}) for k, v in self.cast.items()}
        self.looks.setdefault("doug", T.CAST_LOOKS["doug"])

    def talk(self, line_id, t_abs):
        l = self.lines.get(line_id)
        if l is None:
            return 0.0
        if not l:
            return 0.0
        if line_id not in self.env:
            self.env[line_id] = envelope(np.load(self.pdir / "build" / "clips" / l["clip"]))
        e = self.env[line_id]
        k = int((t_abs - l["start"]) * FPS)
        return float(e[k]) if 0 <= k < len(e) else 0.0


def _actor_world(st, who, spec, t_rel, dur):
    a = dict(st["chars"][who])
    mv = (spec.get("move") or {}).get(who)
    if mv:
        f = T.ease(min(1.0, t_rel / max(0.3, dur * 0.8)))
        a["x"] = a["x"] + (mv[0] - a["x"]) * f
        if len(mv) > 1:
            a["y"] = a.get("y", 0) + (mv[1] - a.get("y", 0)) * f
    return a


def _frame_target(frame, st, ground):
    """Return (cx, cy, zoom) world camera for a shot label."""
    chars = st.get("chars", {})
    if frame.startswith("close:") or frame.startswith("medium:"):
        who = frame.split(":", 1)[1]
        z = 2.6 if frame.startswith("close") else 1.7
        if who == "meg" and "meg" in st:
            return _frame_target("meg", st, ground)
        if who in chars:
            a = chars[who]
            s = a.get("scale", 1.0)
            gy = a.get("y", ground)
            head_y = gy - (330 if a.get("pose", "") not in ("sit", "sit_talk", "sleep") else 230) * s
            cy = head_y + (95 if z > 2 else 160) * s
            return a["x"] + 40 * a.get("facing", 1) * s, cy, z / max(0.6, s)
    if frame == "megclose" and "meg" in st:
        m = st["meg"]
        s = m.get("scale", 0.5)
        return m["x"] + m.get("facing", 1) * 110 * s, m["y"] - 20 * s, max(1.8, min(3.4, 900 / max(150, 330 * s)))
    if frame == "meg" and "meg" in st:
        m = st["meg"]
        span = 520 * m.get("scale", 0.5)
        z = max(1.15, min(2.6, 1100 / max(200, span)))
        return m["x"], m["y"] - 10, z
    if frame.startswith("pt:"):
        x, y, z = [float(v) for v in frame[3:].split(",")]
        return x, y, z
    xs = [a["x"] for a in chars.values()] + ([st["meg"]["x"]] if "meg" in st else [])
    cx = sum(xs) / len(xs) if xs else 960
    return cx, 540, st.get("wide_zoom", 1.06)


def _fit_heads(cx, cy, z, st, ground, frame):
    """No half heads: if a character's head is cut by the top edge of the frame, widen the shot to include it."""
    if frame.startswith(("close:", "medium:", "megclose")):
        return cx, cy, z
    for a in st.get("chars", {}).values():
        s = a.get("scale", 1.0)
        gy = a.get("y", ground)
        sitting = a.get("pose") in ("sit", "sit_talk", "sleep")
        top = gy - (410 if not sitting else 300) * s
        hw, hh = W / 2 / z, H / 2 / z
        if abs(a["x"] - cx) > hw + 60 * s:
            continue
        ftop, fbot = cy - hh, cy + hh
        if top < ftop < gy:
            new_top = max(0.0, top - 10)
            z = max(1.0, H / (fbot - new_top))
            cy = (fbot + new_top) / 2
    return cx, cy, z


def _clamp_cam(cx, cy, z):
    z = max(1.0, z)
    hw, hh = W / 2 / z, H / 2 / z
    return min(max(cx, hw), W - hw), min(max(cy, hh), H - hh), z


def render_frame(ctx: Ctx, spec: dict, t_abs: float, bgcache: dict) -> Image.Image:
    st = dict(ctx.staging["scenes"][spec["scene"]])
    for k in ("meg",):
        if spec.get("meg") and "meg" in st:
            st["meg"] = {**st["meg"], **spec["meg"]}
    set_id = spec.get("set") or st.get("set")
    ground = S.GROUND.get(set_id, 900)
    dur = spec["t1"] - spec["t0"]
    t_rel = t_abs - spec["t0"]
    f = t_rel / max(0.05, dur)
    cx, cy, z = _frame_target(spec["frame"], st, ground)
    if spec.get("card_on"):
        cx += 260 / z     # keep the subject left of the science card
    cx, cy, z = _fit_heads(cx, cy, z, st, ground, spec["frame"])
    push = 1.0 + 0.06 * T.ease(f, "inout") * (1 if hash(spec["line"] + spec["frame"]) % 2 else -0.6)
    drift = (math.sin(spec["t0"] * 3.1) * 26) * (f - 0.5)
    cx, cy, z = _clamp_cam(cx + drift / z, cy, z * push)
    shake = 0.0
    if spec["emo"] in ("shock", "shocked", "panic", "scared", "yelling", "loud") or "shake" in (spec.get("fx") or []):
        shake = 7.0 * max(0.0, 1 - t_rel / 0.6)
    # background
    if set_id not in bgcache:
        bgcache[set_id] = S.background(set_id)
    bg = bgcache[set_id]
    k = bg.width / W
    bw, bh = W / z * k, H / z * k
    x0 = (cx - W / 2 / z) * k + random.uniform(-shake, shake)
    y0 = (cy - H / 2 / z) * k + random.uniform(-shake, shake)
    x0 = min(max(0, x0), bg.width - bw)
    y0 = min(max(0, y0), bg.height - bh)
    frame = bg.resize((W, H), Image.BILINEAR, box=(x0, y0, x0 + bw, y0 + bh)).convert("RGBA")
    s2w = lambda wx, wy: ((wx - x0 / k) * z, (wy - y0 / k) * z)
    S.animate_layer(set_id, frame, t_abs, s2w, z)
    # props behind
    for pr in st.get("props", []) + (spec.get("props_add") or []):
        if pr.get("front"):
            continue
        _draw_prop(frame, pr, s2w, z, t_abs)
    # megalodon and characters, sorted by depth (y)
    drawables = []
    hide = set(spec.get("hide") or [])
    if spec["frame"] == "megclose":
        hide |= set(st.get("chars", {}))
    if "meg" in st and "meg" not in hide:
        mg = dict(st["meg"])
        mv = (spec.get("move") or {}).get("meg")
        if mv:
            fm = T.ease(min(1.0, t_rel / max(0.3, dur * 0.85)))
            mg["x"] = mg["x"] + (mv[0] - mg["x"]) * fm
            if len(mv) > 1:
                mg["y"] = mg["y"] + (mv[1] - mg["y"]) * fm
        drawables.append((mg.get("depth", mg["y"]), "meg", mg))
    for who in st.get("chars", {}):
        if who in hide:
            continue
        a = _actor_world(st, who, spec, t_rel, dur)
        drawables.append((a.get("depth", a.get("y", ground)), who, a))
    for _, who, a in sorted(drawables, key=lambda d: d[0]):
        if who == "meg":
            _draw_meg(frame, a, s2w, z, t_abs, spec)
        else:
            _draw_actor(ctx, frame, who, a, s2w, z, t_abs, spec, ground)
    for pr in st.get("props", []) + (spec.get("props_add") or []):
        if pr.get("front"):
            _draw_prop(frame, pr, s2w, z, t_abs)
    S.foreground_layer(set_id, frame, t_abs, s2w, z)
    _fx(frame, spec, st, t_rel, s2w, z)
    return frame


def _fx(frame, spec, st, t_rel, s2w, z):
    fx = spec.get("fx") or []
    if not fx:
        return
    d = ImageDraw.Draw(frame, "RGBA")
    if "speedlines" in fx or "shock" in fx:
        rnd = random.Random(int(t_rel * 12))
        for i in range(28):
            a = rnd.uniform(0, 2 * math.pi)
            r0, r1 = rnd.uniform(560, 700), 1300
            cx, cy = W / 2, H / 2
            d.line([(cx + r0 * math.cos(a), cy + r0 * math.sin(a) * 0.62), (cx + r1 * math.cos(a), cy + r1 * math.sin(a) * 0.62)],
                   fill=(255, 255, 255, 150), width=rnd.randint(3, 9))
    if "splash" in fx and "meg" in st:
        mx, my = s2w(st["meg"]["x"], st["meg"].get("water", st["meg"]["y"]))
        k = min(1, t_rel / 0.5)
        rnd = random.Random(5)
        for i in range(22):
            a = math.radians(rnd.uniform(200, 340))
            dist = (80 + rnd.uniform(0, 220)) * k * z * 0.6
            x = mx + math.cos(a) * dist
            y = my + math.sin(a) * dist + 300 * (k ** 2) * z * 0.25
            r = rnd.uniform(8, 20) * z * 0.6 * (1.2 - k * 0.5)
            d.ellipse([x - r, y - r, x + r, y + r], fill=(220, 245, 255, int(230 * (1 - k * 0.6))), outline=(28, 22, 34, 200), width=2)
    if "sweat" in fx:
        pass
    if "flash" in fx and t_rel < 0.2:
        frame.alpha_composite(Image.new("RGBA", frame.size, (255, 255, 255, int(200 * (1 - t_rel / 0.2)))))
    if "endslate" in fx:
        for (x, y, w, h) in ((1000, 150, 760, 428), (1180, 640, 400, 225)):
            d.rounded_rectangle([x - 8, y - 8, x + w + 8, y + h + 8], 24, fill=(255, 255, 255, 255))
            d.rounded_rectangle([x, y, x + w, y + h], 18, fill=(20, 32, 60, 255))
        f = T.font(54, "RussoOne-Regular")
        d.text((1380, 110), "WHAT IF YOU... WATCH THIS NEXT", font=T.font(40, "RussoOne-Regular"), fill=(246, 183, 60, 255), anchor="mm")
    if "flashback" in fx:
        over = Image.new("RGBA", frame.size, (255, 200, 120, 70))
        frame.alpha_composite(over)
        vig = Image.new("L", frame.size, 0)
        ImageDraw.Draw(vig).ellipse([-200, -160, W + 200, H + 160], fill=255)
        vig = vig.filter(ImageFilter.GaussianBlur(80))
        dark = Image.new("RGBA", frame.size, (40, 25, 10, 200))
        dark.putalpha(vig.point(lambda v: 200 - int(v * 200 / 255)))
        frame.alpha_composite(dark)
    if "dark" in fx:
        frame.alpha_composite(Image.new("RGBA", frame.size, (10, 15, 40, 110)))


def _draw_actor(ctx, frame, who, a, s2w, z, t_abs, spec, ground):
    look = ctx.looks.get(who)
    if look is None:
        return
    if a.get("extras_add"):
        import copy
        look = copy.copy(look)
        look.extras = set(look.extras) | set(a["extras_add"])
    speaking = spec["who"] == who
    emo = spec["emo"] if speaking else a.get("emo", "neutral")
    pose_over = (spec.get("pose") or {}).get(who)
    eyes, brows, mouth, cyc = T.EMOTIONS.get(emo or "neutral", T.EMOTIONS["neutral"])
    if pose_over:
        cyc = pose_over if isinstance(pose_over, list) else [pose_over]
    elif not speaking:
        cyc = a.get("idle", ["stand"])
        if spec["who"] != "narrator" and spec["emo"] in ("shock", "shocked", "panic", "scared") and who == "doug":
            cyc = ["panic1", "panic2"]
    elif a.get("pose") in ("sit", "sit_talk", "sleep"):
        cyc = ["sit_talk", "sit"]
    base = a.get("pose")
    if base and not speaking and not pose_over:
        cyc = [base] if isinstance(base, str) else base
    phase = (hash(who) % 100) / 37.0
    rate = 1.6 if speaking else 0.5
    if any(str(c).startswith(("walk", "run", "swim", "tread", "panic")) for c in cyc):
        rate = 4.0
    pose = T.pose_at(cyc, t_abs, rate=rate, phase=phase)
    if speaking or "walk" in str(cyc):
        pass
    talk = ctx.talk(spec["line"], t_abs) if speaking else 0.0
    blink = ((t_abs + phase * 1.7) % 3.7) < 0.12
    s = a.get("scale", 1.0) * z
    gy = a.get("y", ground)
    bob = math.sin(t_abs * 2.2 + phase) * 2.5
    px, py = s2w(a["x"], gy)
    hip = (px, py - 140 * s + bob * s)
    holds = (spec.get("holds") or {}).get(who, a.get("holds"))
    extra = [HP.HELD[h] for h in ([holds] if isinstance(holds, str) else (holds or [])) if h in HP.HELD]
    if a.get("eyes"):
        eyes = a["eyes"] if not speaking else eyes
    img, org = T.sprite(lambda p: T.draw_character(p, look, pose, eyes=eyes, brows=brows, mouth=mouth, talk=talk,
                                                   blink=blink, look_dir=1.0, extra_props=extra),
                        (-260, -520, 520, 230) if extra else T.CHAR_BBOX, s, flip=a.get("facing", 1) < 0)
    if img is None:
        return
    if a.get("water"):
        img = _waterline(img, org, a["water"], gy, s, z, s2w, hip)
    T.paste(frame, img, org, hip)


def _waterline(img, org, water_y, gy, s, z, s2w, hip):
    """Characters standing in water: hide below the water line."""
    _, wy = s2w(0, water_y)
    cut = int(wy - (hip[1] - org[1]))
    if 0 < cut < img.height:
        img = img.copy()
        img.paste((0, 0, 0, 0), (0, cut, img.width, img.height))
    return img


def _water_tint(img, org, water_y, s2w, at, col=(40, 150, 210)):
    """Below the water line the sprite is tinted and faded, so a fin can break the surface."""
    _, wy = s2w(0, water_y)
    cut = int(wy - (at[1] - org[1]))
    if cut >= img.height:
        return img
    cut = max(0, cut)
    img = img.copy()
    lower = img.crop((0, cut, img.width, img.height))
    a = lower.getchannel("A").point(lambda v: int(v * 0.7))
    tinted = Image.blend(lower.convert("RGB"), Image.new("RGB", lower.size, col), 0.45).convert("RGBA")
    tinted.putalpha(a)
    img.paste(tinted, (0, cut))
    return img


def _draw_meg(frame, m, s2w, z, t_abs, spec):
    s = m.get("scale", 0.5) * z
    px, py = s2w(m["x"], m["y"])
    jaw = m.get("jaw", 0.0)
    if m.get("chomp"):
        jaw = max(0.0, math.sin(t_abs * 9)) ** 2
    mood = m.get("mood", "calm")
    bobx = math.sin(t_abs * 1.3) * 6 * s
    boby = math.sin(t_abs * 1.9) * 5 * s
    img, org = T.sprite(lambda p: P.draw_megalodon(p, t=t_abs, swim=m.get("swim", 0.6), jaw=jaw, mood=mood,
                                                   pup=m.get("pup", 0.0), col=m.get("col", P.SHARK_TOP)),
                        P.MEG_BBOX, s, flip=m.get("facing", 1) < 0)
    if img is None:
        return
    if m.get("water"):
        img = _water_tint(img, org, m["water"], s2w, (px + bobx, py + boby))
    T.paste(frame, img, org, (px + bobx, py + boby), alpha=m.get("alpha", 1.0))


def _draw_prop(frame, pr, s2w, z, t_abs):
    pid = pr["id"]
    fn, bbox = P.PROP_DRAW.get(pid, (None, None))
    if fn is None:
        fn, bbox = S.EXTRA_PROPS.get(pid, (None, None))
    if fn is None:
        return
    s = pr.get("scale", 1.0) * z
    px, py = s2w(pr["x"], pr["y"])
    kw = {k: v for k, v in pr.items() if k not in ("id", "x", "y", "scale", "front", "facing", "rot", "depth")}
    if "t" in fn.__code__.co_varnames:
        kw["t"] = t_abs
    rot = pr.get("rot", 0)
    def draw(p):
        p.push(rot=rot)
        fn(p, **kw)
        p.pop()
    img, org = T.sprite(draw, _rot_bbox(bbox, rot), s, flip=pr.get("facing", 1) < 0)
    T.paste(frame, img, org, (px, py))


def _rot_bbox(b, rot):
    if not rot:
        return b
    r = max(abs(b[0]), abs(b[1]), abs(b[2]), abs(b[3]))
    return (-r, -r, r, r)


# ------------------------------------------------------------------ overlays

def _ov_sprite(key, fn, w, h, cache):
    if key not in cache:
        img = Image.new("RGBA", (w * T.SS, h * T.SS), (0, 0, 0, 0))
        pen = T.Pen(img, 0, 0, T.SS)
        fn(pen)
        cache[key] = img.reduce(T.SS)
    return cache[key]


def _paste_scaled(frame, img, cx, cy, scale, alpha=1.0, rot=0.0):
    if scale <= 0.01 or alpha <= 0.01:
        return
    im = img
    if abs(scale - 1) > 0.01:
        im = im.resize((max(1, int(im.width * scale)), max(1, int(im.height * scale))), Image.BILINEAR)
    if rot:
        im = im.rotate(rot, resample=Image.BICUBIC, expand=True)
    T.paste(frame, im, (im.width / 2, im.height / 2), (cx, cy), alpha)


def _wrap(text, fnt, maxw, d):
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        test = (cur + " " + w_).strip()
        if d.textlength(test, font=fnt) > maxw and cur:
            lines.append(cur)
            cur = w_
        else:
            cur = test
    if cur:
        lines.append(cur)
    return lines


def draw_overlays(frame, spec, t_abs, ctx, ovc, state):
    t_rel = t_abs - spec["t0"]
    # DAY badge
    day = spec.get("day")
    if day is not None:
        def badge(p):
            p.rrect(6, 6, 228, 92, 22, NAVY, ow=5, ink="#ffffff")
            p.text(120, 52, f"DAY {day}", 52, YEL, "RussoOne-Regular")
        img = _ov_sprite(f"day{day}", badge, 240, 104, ovc)
        since = t_abs - state.get("day_since", {}).get(day, t_abs)
        sc = T.ease(min(1, since / 0.35), "back") if since < 0.35 else 1.0
        _paste_scaled(frame, img, 48 + 120, 40 + 52, sc)
    # name card
    if spec.get("namecard"):
        nc = ctx.staging["name_cards"][spec["namecard"]]
        def card(p):
            p.poly([(0, 20), (640, 0), (620, 120), (10, 132)], "#ffffff", ow=6)
            p.poly([(0, 20), (640, 0), (636, 54), (4, 70)], RED, ow=0)
            p.poly([(0, 20), (640, 0), (620, 120), (10, 132)], None, ow=6)
            p.text(26, 40, nc["name"].upper(), 50 if len(nc["name"]) < 16 else 36, "#ffffff", "RussoOne-Regular", anchor="lm")
            p.text(28, 100, nc["tag"], 32, NAVY, "Quicksand-Bold", anchor="lm")
        img = _ov_sprite("nc_" + spec["namecard"], card, 660, 140, ovc)
        dur = min(3.2, spec["t1"] - spec["t0"] + 1.2)
        if t_rel < dur:
            slide = T.ease(min(1, t_rel / 0.3), "out")
            out_f = 1 - T.ease(max(0, (t_rel - dur + 0.3) / 0.3), "in")
            T.paste(frame, img, (0, 0), (-700 + 760 * slide, 780), alpha=out_f)
    # science card
    card = state.get("card")
    if card and card["t1"] > t_abs >= card["t0"]:
        c = card["card"]
        key = "card_" + c["head"] + c["fact"]
        def draw_card(p):
            p.rrect(8, 8, 744, 404, 30, "#ffffff", ow=7)
            p.rrect(8, 8, 744, 112, 30, NAVY, ow=7)
            p.poly([(15, 80), (745, 80), (745, 118), (15, 118)], NAVY, ow=0)
            p.rrect(8, 8, 744, 404, 30, None, ow=7)
            hd = c["head"].upper()
            hs = 56 if len(hd) < 18 else (46 if len(hd) < 24 else 38)
            p.text(380, 66, hd, hs, YEL, "RussoOne-Regular")
            d = ImageDraw.Draw(Image.new("RGB", (10, 10)))
            f = T.font(44, "Quicksand-Bold")
            lines = _wrap(c["fact"], f, 640, d)[:4]
            y = 140 + (4 - len(lines)) * 26
            if c.get("art"):
                lines, y = lines[:2], 128
            for ln in lines:
                p.text(380, y + 26, ln, 44, NAVY, "Quicksand-Bold")
                y += 54
            if c.get("art") == "size_compare":
                _size_compare(p)
            if c.get("source"):
                p.text(380, 378, "SOURCE: " + c["source"].upper(), 22, "#6b7280", "Quicksand-Bold")
        img = _ov_sprite(key, draw_card, 760, 420, ovc)
        tin = t_abs - card["t0"]
        tout = card["t1"] - t_abs
        sc = T.ease(min(1, tin / 0.3), "back") * (1 if tout > 0.2 else T.ease(tout / 0.2))
        _paste_scaled(frame, img, 1450, 470, 0.25 + 0.75 * sc, alpha=min(1, tin / 0.12))
    # kinetic word
    wd = state.get("word")
    if wd and wd["t1"] > t_abs >= wd["t0"]:
        text = wd["text"].upper()
        def draw_word(p):
            size = 170 if len(text) < 10 else (130 if len(text) < 16 else 100)
            p.text(700, 150, text, size, YEL, "Bangers-Regular", stroke=11, stroke_color=NAVY)
        img = _ov_sprite("w_" + text, draw_word, 1400, 300, ovc)
        tin = t_abs - wd["t0"]
        sc = T.ease(min(1, tin / 0.22), "back")
        wob = math.sin(tin * 18) * 2.5 * max(0, 1 - tin / 0.6)
        cyw = 860 if not state.get("card") or not (state["card"]["t1"] > t_abs >= state["card"]["t0"]) else 930
        cxw = 960 if cyw == 860 else 700
        _paste_scaled(frame, img, cxw, cyw, 0.35 + 0.65 * sc, rot=-4 + wob)
    # title drop
    tt = state.get("title")
    if tt and tt["t1"] > t_abs >= tt["t0"]:
        text = tt["text"]
        def draw_title(p):
            p.rrect(10, 10, 1500, 330, 40, NAVY, ow=9, ink="#ffffff")
            parts = text.split("|")
            p.text(760, 110, parts[0], 92 if len(parts[0]) < 18 else 72, "#ffffff", "RussoOne-Regular")
            if len(parts) > 1:
                p.text(760, 240, parts[1], 130 if len(parts[1]) < 18 else 112, YEL, "Bangers-Regular", stroke=8, stroke_color=RED)
        img = _ov_sprite("title_" + text, draw_title, 1520, 350, ovc)
        tin = t_abs - tt["t0"]
        tout = tt["t1"] - t_abs
        sc = T.ease(min(1, tin / 0.35), "back") * (1 if tout > 0.25 else T.ease(tout / 0.25))
        _paste_scaled(frame, img, 960, 500, 0.2 + 0.8 * sc, rot=-2 * (1 - sc))
    # day wipe
    dw = state.get("daywipe")
    if dw and dw["t0"] <= t_abs < dw["t0"] + 0.9:
        tin = t_abs - dw["t0"]
        cover = T.ease(min(1, tin / 0.25), "out") if tin < 0.6 else 1 - T.ease((tin - 0.6) / 0.3, "in")
        over = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        d = ImageDraw.Draw(over)
        x = -W + (W + 200) * cover if tin < 0.6 else W * (1 - cover) * 1.1 + 0
        if tin < 0.6:
            d.polygon([(x - 200, 0), (x + W, 0), (x + W, H), (x - 200 + 0, H)], fill=T.rgba(NAVY))
        else:
            d.polygon([(x, 0), (W + 200, 0), (W + 200, H), (x - 200, H)], fill=T.rgba(NAVY))
        frame.alpha_composite(over)
        if 0.18 < tin < 0.72:
            def dwc(p):
                p.text(500, 130, f"DAY {dw['day']}", 230, YEL, "Bangers-Regular", stroke=10, stroke_color="#0b1222")
            img = _ov_sprite(f"dw{dw['day']}", dwc, 1000, 260, ovc)
            sc = T.ease(min(1, (tin - 0.18) / 0.2), "back")
            _paste_scaled(frame, img, 960, 540, 0.5 + 0.5 * sc)


def _size_compare(p):
    """Silhouette strip for the science card: person, great white, megalodon (estimate range)."""
    base = 318
    p.line([(40, base), (720, base)], "#9aa3b2", 3, caps=False)
    p.push(70, base - 20, scale=0.17)
    T.draw_character(p, T.CAST_LOOKS["doug"], T.POSES["stand"])
    p.pop()
    p.push(200, base - 22, scale=0.16)
    P.draw_megalodon(p, col="#8fa3b8", swim=0)
    p.pop()
    p.push(520, base - 32, scale=0.42)
    P.draw_megalodon(p, col=P.SHARK_TOP, swim=0)
    p.pop()
    p.text(70, base + 18, "YOU", 16, "#1e2a44", "RussoOne-Regular")
    p.text(200, base + 18, "GREAT WHITE", 16, "#1e2a44", "RussoOne-Regular")
    p.text(520, base + 18, "MEGALODON", 16, "#1e2a44", "RussoOne-Regular")


def _timeline_state(shots):
    """Card / word / title windows across shots (a card stays up for its whole line, across cuts)."""
    cards, words, titles, wipes, day_since = [], [], [], [], {}
    line_end = {}
    for s in shots:
        if s.get("kind") == "daywipe":
            continue
        line_end[s["line"]] = s["t1"]
    for s in shots:
        if s.get("kind") == "daywipe":
            wipes.append({"t0": s["t0"], "day": s["day"]})
            day_since.setdefault(s["day"], s["t0"] + 0.6)
            continue
        if s.get("day") is not None:
            day_since.setdefault(s["day"], s["t0"])
        if s.get("card"):
            cards.append({"t0": s["t0"] + 0.1, "t1": max(line_end[s["line"]], s["t0"] + 3.0), "card": s["card"]})
        if s.get("word"):
            words.append({"t0": s["t0"] + 0.15, "t1": min(line_end[s["line"]], s["t0"] + 1.9), "text": s["word"]})
        if s.get("title"):
            titles.append({"t0": s["t0"] + 0.2, "t1": line_end[s["line"]] + 0.4, "text": s["title"]})
    return cards, words, titles, wipes, day_since


def _active(items, t):
    for it in items:
        if it["t0"] <= t < it.get("t1", it["t0"] + 0.9):
            return it
    return None


def render_range(pdir: Path, shots, i0, i1, out_path: Path, total):
    ctx = Ctx(pdir)
    bgcache, ovc = {}, {}
    cards, words, titles, wipes, day_since = _timeline_state(shots)
    seq = [s for s in shots if s.get("kind") != "daywipe"]
    f0 = int(round(seq[i0]["t0"] * FPS)) if i0 else 0
    f1 = int(round(seq[i1 - 1]["t1"] * FPS)) if i1 < len(seq) else int(math.ceil(total * FPS))
    proc = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                             "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-threads", "4", "-preset", "medium", "-crf", "17",
                             "-pix_fmt", "yuv420p", str(out_path)], stdin=subprocess.PIPE)
    j = i0
    for fr in range(f0, f1):
        t = fr / FPS
        while j < len(seq) - 1 and t >= seq[j]["t1"]:
            j += 1
        spec = seq[j]
        random.seed(fr)
        frame = render_frame(ctx, spec, t, bgcache)
        state = {"card": _active(cards, t), "word": _active(words, t), "title": _active(titles, t),
                 "daywipe": _active([{**w, "t1": w["t0"] + 0.9} for w in wipes], t), "day_since": day_since}
        draw_overlays(frame, spec, t, ctx, ovc, state)
        proc.stdin.write(frame.convert("RGB").tobytes())
    proc.stdin.close()
    proc.wait()


def _part_ok(path: Path) -> bool:
    if not path.exists() or path.stat().st_size < 1000:
        return False
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)],
                       capture_output=True, text=True)
    return r.returncode == 0 and r.stdout.strip() not in ("", "N/A")


def _render_job(args):
    """Render one part; keep a finished part, retry a failed one once (render loops need an attempt cap)."""
    pdir, i0, i1, out, total = args
    sh = json.loads((Path(pdir) / "build" / "shots.json").read_text(encoding="utf-8"))["shots"]
    for attempt in range(2):
        if _part_ok(Path(out)):
            return out
        render_range(Path(pdir), sh, i0, i1, Path(out), total)
    if not _part_ok(Path(out)):
        raise RuntimeError(f"part {out} failed twice")
    return out


def cmd_render(pdir: Path, jobs=10, limit=None):
    from concurrent.futures import ProcessPoolExecutor
    data = json.loads((pdir / "build" / "shots.json").read_text(encoding="utf-8"))
    seq = [s for s in data["shots"] if s.get("kind") != "daywipe"]
    total = data["total"]
    n = len(seq) if not limit else min(limit, len(seq))
    if limit:
        total = seq[n - 1]["t1"]
    parts_dir = pdir / "build" / "parts"
    parts_dir.mkdir(parents=True, exist_ok=True)
    chunk = max(1, math.ceil(n / (jobs * 3)))
    tasks = []
    for k, i0 in enumerate(range(0, n, chunk)):
        i1 = min(n, i0 + chunk)
        tasks.append((str(pdir), i0, i1 if i1 < n or limit else len(seq), str(parts_dir / f"p{k:03d}.mp4"), total))
    with ProcessPoolExecutor(max_workers=jobs) as ex:
        for i, out in enumerate(ex.map(_render_job, tasks)):
            print(f"part {i + 1}/{len(tasks)} done", flush=True)
    lst = parts_dir / "list.txt"
    lst.write_text("".join(f"file '{Path(t[3]).name}'\n" for t in tasks), encoding="utf-8")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy",
                    str(pdir / "build" / "picture.mp4")], check=True)
    print("picture.mp4 written")


def cmd_stills(pdir: Path, every=1):
    data = json.loads((pdir / "build" / "shots.json").read_text(encoding="utf-8"))
    seq = [s for s in data["shots"] if s.get("kind") != "daywipe"]
    ctx = Ctx(pdir)
    bgc, ovc = {}, {}
    cards, words, titles, wipes, day_since = _timeline_state(data["shots"])
    out = pdir / "build" / "stills"
    out.mkdir(parents=True, exist_ok=True)
    thumbs = []
    for i, s in enumerate(seq[::every]):
        t = s["t0"] + (s["t1"] - s["t0"]) * 0.6
        fr = render_frame(ctx, s, t, bgc)
        state = {"card": _active(cards, t), "word": _active(words, t), "title": _active(titles, t), "daywipe": None,
                 "day_since": day_since}
        draw_overlays(fr, s, t, ctx, ovc, state)
        im = fr.convert("RGB").resize((480, 270))
        ImageDraw.Draw(im).text((6, 4), f"{s['line']} {s['frame']}", fill=(255, 0, 0))
        thumbs.append(im)
    for k in range(0, len(thumbs), 20):
        sheet = Image.new("RGB", (480 * 4, 270 * 5), (0, 0, 0))
        for j, im in enumerate(thumbs[k:k + 20]):
            sheet.paste(im, ((j % 4) * 480, (j // 4) * 270))
        sheet.save(out / f"sheet_{k // 20:02d}.jpg", quality=85)
    print(f"{len(thumbs)} stills in {(len(thumbs) + 19) // 20} sheets")


# ------------------------------------------------------------------ audio master

def _synth_music(total, sr=SR):
    """Original light underscore made in code: plucked chords and a soft bass at 96 bpm, I-vi-IV-V in C."""
    t = np.arange(int(total * sr)) / sr
    out = np.zeros_like(t)
    bpm = 96
    beat = 60 / bpm
    prog = [(60, 64, 67), (57, 60, 64), (53, 57, 60), (55, 59, 62)]
    def note(m, start, length, amp, decay):
        i0 = int(start * sr)
        n = int(length * sr)
        if i0 >= len(out):
            return
        n = min(n, len(out) - i0)
        tt = np.arange(n) / sr
        f = 440 * 2 ** ((m - 69) / 12)
        wave_ = (np.sin(2 * np.pi * f * tt) + 0.3 * np.sin(4 * np.pi * f * tt) + 0.1 * np.sin(6 * np.pi * f * tt))
        out[i0:i0 + n] += amp * wave_ * np.exp(-tt * decay)
    bar = 0
    pos = 0.0
    pat = [0, 2, 1, 2, 0, 2, 1, 2]
    while pos < total:
        ch = prog[bar % 4]
        note(ch[0] - 24, pos, beat * 4, 0.22, 0.9)
        for k, idx in enumerate(pat):
            note(ch[idx] + 12, pos + k * beat / 2, beat, 0.07, 5.5)
        pos += beat * 4
        bar += 1
    # gentle fade in/out
    fade = np.minimum(1, np.minimum(t / 2.0, (total - t) / 3.0))
    return out * np.clip(fade, 0, 1)


def _sfx_whoosh(sr=SR, dur=0.55):
    n = int(dur * sr)
    noise = np.random.RandomState(3).randn(n)
    env = np.sin(np.linspace(0, np.pi, n)) ** 2
    # crude band sweep with a moving one-pole filter
    out = np.zeros(n)
    y = 0.0
    for i in range(n):
        a = 0.02 + 0.5 * (i / n)
        y = y + a * (noise[i] - y)
        out[i] = y
    return 0.6 * out * env / (np.abs(out).max() + 1e-6)


def _sfx_pop(sr=SR):
    n = int(0.12 * sr)
    tt = np.arange(n) / sr
    f = 900 * np.exp(-tt * 18) + 300
    return 0.5 * np.sin(2 * np.pi * np.cumsum(f) / sr) * np.exp(-tt * 30)


def _sfx_ding(sr=SR):
    n = int(0.5 * sr)
    tt = np.arange(n) / sr
    return 0.28 * (np.sin(2 * np.pi * 1320 * tt) + 0.5 * np.sin(2 * np.pi * 1980 * tt)) * np.exp(-tt * 7)


def cmd_master(pdir: Path, music_db=-25.0):
    L = json.loads((pdir / "build" / "lines.json").read_text(encoding="utf-8"))
    shots = json.loads((pdir / "build" / "shots.json").read_text(encoding="utf-8"))["shots"]
    total = json.loads((pdir / "build" / "shots.json").read_text(encoding="utf-8"))["total"]
    n = int(total * SR) + SR
    voice = np.zeros(n, dtype=np.float32)
    for l in L["lines"]:
        x = np.load(pdir / "build" / "clips" / l["clip"])
        i0 = int(l["start"] * SR)
        voice[i0:i0 + len(x)] += x[: max(0, n - i0)]
    sfx = np.zeros(n, dtype=np.float32)
    def add(sig, t, g=1.0):
        i0 = int(t * SR)
        if i0 < n:
            sfx[i0:i0 + len(sig)] += g * sig[: n - i0]
    cards, words, titles, wipes, _ = _timeline_state(shots)
    for w in wipes:
        add(_sfx_whoosh(), w["t0"], 0.9)
    for wd in words:
        add(_sfx_pop(), wd["t0"], 0.8)
    for c in cards:
        add(_sfx_ding(), c["t0"], 0.7)
    for tt in titles:
        add(_sfx_whoosh(), tt["t0"] - 0.1, 1.0)
    music = _synth_music(n / SR).astype(np.float32)
    # duck the music under speech
    env = np.convolve(np.abs(voice), np.ones(int(0.25 * SR)) / int(0.25 * SR), mode="same")
    duck = 1.0 - 0.55 * np.clip(env / (np.percentile(env, 95) + 1e-6), 0, 1)
    vr = np.sqrt(np.mean(voice[voice != 0] ** 2)) if np.any(voice) else 0.1
    mr = np.sqrt(np.mean(music ** 2)) + 1e-9
    music *= (vr * 10 ** (music_db / 20)) / mr
    mix = voice + music * duck + sfx * vr / 0.25 * 0.35
    wav = pdir / "build" / "mix.wav"
    pcm = np.clip(mix, -1, 1)
    with wave.open(str(wav), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes((pcm * 32767).astype(np.int16).tobytes())
    from .tts import normalize_wav
    normalize_wav(wav, -17.0, -3.5)  # mono copied to both stereo channels reads +3 dB
    final = pdir / "build" / "final.mp4"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(pdir / "build" / "picture.mp4"), "-i", str(wav),
                    "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "256k", "-ar", "48000",
                    "-ac", "2", "-af", "pan=stereo|c0=c0|c1=c0", "-shortest", str(final)], check=True)
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(final), "-af", "ebur128=peak=true", "-f", "null", "-"],
                       capture_output=True, text=True)
    i = re.findall(r"I:\s+(-?[\d.]+) LUFS", r.stderr)
    tp = re.findall(r"Peak:\s+(-?[\d.]+) dBFS", r.stderr)
    print(f"final.mp4: integrated {i[-1] if i else '?'} LUFS, true peak {tp[-1] if tp else '?'} dBFS")


def main(argv):
    cmd, pdir = argv[0], Path(argv[1]).resolve()
    if cmd == "voices":
        cmd_voices(pdir)
    elif cmd == "shots":
        cmd_shots(pdir)
    elif cmd == "stills":
        cmd_stills(pdir, int(argv[2]) if len(argv) > 2 else 1)
    elif cmd == "render":
        jobs = int(argv[argv.index("--jobs") + 1]) if "--jobs" in argv else 12
        limit = int(argv[argv.index("--limit") + 1]) if "--limit" in argv else None
        cmd_render(pdir, jobs, limit)
    elif cmd == "master":
        cmd_master(pdir)
    elif cmd == "parse":
        sc = parse_script(pdir / "script.md")
        print(json.dumps({k: (v if k != "scenes" else len(v)) for k, v in sc.items()}, indent=1)[:3000])
        print(sum(len(s["lines"]) for s in sc["scenes"]), "lines")


if __name__ == "__main__":
    main(sys.argv[1:])
