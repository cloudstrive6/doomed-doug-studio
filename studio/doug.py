"""Doug: the channel's recurring stick man, as a posable rig.

Proportions follow the style bible's meme stick man: big round head (~1/3 of his height) with a grey shading
crescent, vertical oval eyes with dot pupils, thin uniform body lines, and our signature red cap.

Local coordinates: origin at the hips, y grows downward, figure faces right.
At scale 1 Doug is ~450 units tall (feet at y=+150, cap top at y≈-300).

Scene usage:
  {"type": "doug", "x": 960, "y": 700, "scale": 1, "pose": "arms_up",
   "expression": "shock", "gear": ["scuba"], "facing": "right", "ghost": false}
`pose` / `expression` may be lists; they cycle with the boil variant (GIF-like loop).
Lying down / death beats: `pose: "on_back"` with no `rotate` (optional gear `cap_off`); see docs/SCENE_SCHEMA.md.
"""
from __future__ import annotations

import math

INK = "#000000"
CAP = "#e0201b"      # Doug's signature red cap
SKIN = "#ffffff"
SHADE = "#d6d6d6"
TONGUE = "#ff8fa3"
BURN = "#ff8a7a"       # `sunburn` gear: head fill
BURN_SHADE = "#e0665a" # `sunburn` gear: the shading crescent, same shape, burnt tone
BURN_ARM = "#e0201b"   # `sunburn` gear: "his arms turn bright red"

HEAD_R = 72
NECK = (0, -150)
HEAD_C = (0, -150 - HEAD_R + 4)
SHOULDER = (0, -122)
HIP = (0, 0)
UPPER_ARM, FOREARM = 62, 58
THIGH, SHIN = 78, 74
LINE = 5

# angles in degrees: 0 = straight down, 90 = pointing right (forward), -90 = back, 180 = up
POSES = {
    "stand":    dict(arm_f=(20, 10), arm_b=(-20, -10), leg_f=(12, 0), leg_b=(-12, 0), lean=0),
    "wave":     dict(arm_f=(95, 55), arm_b=(-20, -10), leg_f=(12, 0), leg_b=(-12, 0), lean=0),
    "point":    dict(arm_f=(95, 0), arm_b=(-20, -10), leg_f=(12, 0), leg_b=(-12, 0), lean=0),
    "arms_up":  dict(arm_f=(105, 30), arm_b=(-105, -30), leg_f=(18, 5), leg_b=(-18, -5), lean=0),
    "panic1":   dict(arm_f=(110, 35), arm_b=(-100, -20), leg_f=(30, -10), leg_b=(-15, 0), lean=0),
    "panic2":   dict(arm_f=(100, 20), arm_b=(-110, -35), leg_f=(15, 0), leg_b=(-30, 10), lean=0),
    "shrug":    dict(arm_f=(60, 90), arm_b=(-60, -90), leg_f=(12, 0), leg_b=(-12, 0), lean=0),
    "think":    dict(arm_f=(30, 140), arm_b=(-20, -10), leg_f=(12, 0), leg_b=(-12, 0), lean=0),
    "hands_hips": dict(arm_f=(60, -40), arm_b=(-60, 40), leg_f=(15, 0), leg_b=(-15, 0), lean=0),
    "walk1":    dict(arm_f=(35, 60), arm_b=(-35, -10), leg_f=(30, 0), leg_b=(-30, -20), lean=4),
    "walk2":    dict(arm_f=(-30, -5), arm_b=(30, 60), leg_f=(-25, -20), leg_b=(25, 0), lean=4),
    "run1":     dict(arm_f=(70, 80), arm_b=(-60, -20), leg_f=(70, 0), leg_b=(-50, -110), lean=15),
    "run2":     dict(arm_f=(-60, -20), arm_b=(70, 80), leg_f=(-50, -110), leg_b=(70, 0), lean=15),
    "swim1":    dict(arm_f=(160, -50), arm_b=(-150, -20), leg_f=(20, 40), leg_b=(-20, -40), lean=70),
    "swim2":    dict(arm_f=(110, -50), arm_b=(170, -20), leg_f=(-10, 20), leg_b=(10, -20), lean=70),
    "float":    dict(arm_f=(110, 20), arm_b=(-110, -20), leg_f=(25, 15), leg_b=(-25, -15), lean=0),
    "sit":      dict(arm_f=(30, 50), arm_b=(-10, 30), leg_f=(90, 0), leg_b=(80, 0), lean=0, drop=70),
    # thumbs up: front forearm raised, small fist + thumb drawn at the hand (see _thumb). Standing and seated.
    "thumbs_up":     dict(arm_f=(95, 25), arm_b=(-20, -10), leg_f=(12, 0), leg_b=(-12, 0), lean=0, thumb=True),
    "sit_thumbs_up": dict(arm_f=(95, 25), arm_b=(-10, 30), leg_f=(90, 0), leg_b=(80, 0), lean=0, drop=70, thumb=True),
    "fall":     dict(arm_f=(130, -10), arm_b=(-130, 10), leg_f=(150, -30), leg_b=(-150, 20), lean=0),
    "cower":    dict(arm_f=(120, 45), arm_b=(-120, -45), leg_f=(60, -30), leg_b=(-40, 30), lean=10, drop=40),
    "lie":      dict(arm_f=(10, 0), arm_b=(-10, 0), leg_f=(5, 0), leg_b=(-5, 0), lean=0),
    "dive":     dict(arm_f=(175, 5), arm_b=(-175, -5), leg_f=(3, 0), leg_b=(-3, 0), lean=0),
    # Flat on his back, drawn natively horizontal: use WITHOUT `rotate`. See ON_BACK below and docs/SCENE_SCHEMA.md.
    "on_back":  dict(flat=True),
}

# `on_back` skeleton. Same joint positions that `lie` + rotate -90 produces, so worn props drawn for that combo
# (snorkel_gear, ammonite_costume_flat ... used with rotate -90 at Doug's x/y) still line up:
# hips (0,0), shoulders (-122,0), neck (-150,0), head centre (-218,0), feet out to the right (x ~ +150).
# The head is NOT rotated with the body: it stays near-upright (tilted HEAD_TILT, face to the sky) so the red cap
# keeps reading as a cap. Lowest points (head bottom, flat leg, flat arm) sit on y ~ +70: put that on the ground.
ON_BACK = {
    "leg_b": [(0, 0), (76, 40), (152, 70)],          # far leg: flat on the ground
    "leg_f": [(0, 0), (54, -50), (118, 0)],          # near leg: knee up, flopped
    "arm_b": [(-122, 0), (-66, 42), (-6, 70)],       # far arm: flat on the ground along his side
    "arm_f": [(-122, 0), (-86, -46), (-30, -18)],    # near arm: limp across the belly
}
HEAD_TILT = -15   # degrees; negative turns the face up toward the sky
ON_BACK_GROUND = 70  # local y of the ground contact line for `on_back`

# Style-bible expression set + aliases (older names map onto it)
EXPRESSIONS = ["shock", "gritted", "flat", "hopeful", "smirk", "dead", "neutral", "sad", "angry",
               "confused", "sleepy"]
ALIASES = {"happy": "hopeful", "scared": "gritted", "screaming": "shock", "shocked": "shock",
           "nervous_smile": "gritted", "worried": "sad", "crying": "sad", "smug": "smirk",
           "determined": "angry", "unimpressed": "flat"}
EXPRESSIONS += list(ALIASES)


def _limb(start, a1, a2, l1, l2):
    def seg(p, a, l):
        r = math.radians(a)
        return (p[0] + l * math.sin(r), p[1] + l * math.cos(r))
    mid = seg(start, a1, l1)
    return [start, mid, seg(mid, a2, l2)]


def _rot(p, deg, origin=(0, 0)):
    r = math.radians(deg)
    x, y = p[0] - origin[0], p[1] - origin[1]
    return (origin[0] + x * math.cos(r) - y * math.sin(r), origin[1] + x * math.sin(r) + y * math.cos(r))


def _pick(v, variant):
    if isinstance(v, list):
        return v[variant % len(v)] if v else None
    return v


def _turn(els, deg, origin):
    """Rotate already-built elements (points / x,y) around origin. Ellipse radii stay axis-aligned (small parts)."""
    out = []
    for e in els:
        e = dict(e)
        if "points" in e:
            e["points"] = [_rot(p, deg, origin) for p in e["points"]]
        elif "x" in e and "y" in e and e.get("type") != "rect":
            e["x"], e["y"] = _rot((e["x"], e["y"]), deg, origin)
        out.append(e)
    return out


def _cap_on_ground(x, ground_y):
    """The red cap knocked off, resting on the ground beside his head (on_back + gear `cap_off`)."""
    els = _turn(_cap(0, 0), 12, (0, 0))
    low = max(py for e in els for _, py in e["points"])
    for e in els:
        e["points"] = [(px + x, py + ground_y - low) for px, py in e["points"]]
    return els


def doug_elements(el: dict, variant: int = 0):
    pose_name = _pick(el.get("pose", "stand"), variant)
    expr = _pick(el.get("expression", "neutral"), variant)
    expr = ALIASES.get(expr, expr)
    pose = dict(POSES.get(pose_name, POSES["stand"]))
    gear = el.get("gear", []) or []
    ghost = el.get("ghost", False)
    ink = el.get("ink", "#8a8a8a" if ghost else INK)
    burnt = "sunburn" in gear and not ghost
    skin = "#eef3f7" if ghost else (BURN if burnt else SKIN)
    shade = BURN_SHADE if burnt else SHADE
    lean = pose.get("lean", 0)
    drop = pose.get("drop", 0)

    def L(p):
        q = _rot(p, lean)
        return (q[0], q[1] + drop)

    flat = pose.get("flat", False)
    hip, shoulder, neck, head = L(HIP), L(SHOULDER), L(NECK), L(HEAD_C)
    body = []
    if flat:
        hip, shoulder, neck, head = HIP, (-122, 0), (-150, 0), (-218, 0)
        for key in ("leg_b", "leg_f"):
            body.append({"type": "line", "points": ON_BACK[key], "width": LINE, "color": ink})
        body.append({"type": "line", "points": [hip, neck], "width": LINE, "color": ink})
        for key in ("arm_b", "arm_f"):
            body.append({"type": "line", "points": ON_BACK[key], "width": LINE, "color": BURN_ARM if burnt else ink})
    elif ghost:  # wavy ghost tail instead of legs
        body.append({"type": "curve", "points": [hip, (hip[0] - 25, hip[1] + 40), (hip[0] + 10, hip[1] + 80),
                                                  (hip[0] - 20, hip[1] + 120)], "width": LINE, "color": ink})
    else:
        for key in ("leg_b", "leg_f"):
            a1, a2 = pose[key]
            pts = _limb(HIP, a1 - lean, a1 + a2 - lean, THIGH, SHIN)
            body.append({"type": "line", "points": [(p[0], p[1] + drop) for p in pts], "width": LINE, "color": ink})
    if not flat:
        body.append({"type": "line", "points": [hip, neck], "width": LINE, "color": ink})
        for key in ("arm_b", "arm_f"):
            a1, a2 = pose[key]
            pts = _limb((0, 0), a1 - lean, a1 + a2 - lean, UPPER_ARM, FOREARM)
            body.append({"type": "line", "points": [(p[0] + shoulder[0], p[1] + shoulder[1]) for p in pts],
                         "width": LINE, "color": BURN_ARM if burnt else ink})
            if key == "arm_f" and pose.get("thumb"):
                hx_, hy_ = pts[-1][0] + shoulder[0], pts[-1][1] + shoulder[1]
                body += _thumb(hx_, hy_, ink, skin)

    if "tank" in gear or "scuba" in gear:
        if flat:  # tank under his back
            body.insert(0, {"type": "rect", "x": -120, "y": 4, "w": 90, "h": 26, "fill": "#f2c21b", "width": 4})
        else:
            bx, by = L((-30, -110))
            body.insert(0, {"type": "rect", "x": bx - 26, "y": by - 10, "w": 26, "h": 90, "fill": "#f2c21b", "width": 4})

    hx, hy = head
    n_body = len(body)
    body.append({"type": "circle", "x": hx, "y": hy, "r": HEAD_R, "fill": skin, "width": 0, "outline": False})
    # grey shading crescent on the back of the head
    outer = [(hx + HEAD_R * math.cos(math.radians(a)), hy + HEAD_R * math.sin(math.radians(a))) for a in range(100, 261, 10)]
    inner = [(hx + 14 + (HEAD_R - 6) * math.cos(math.radians(a)), hy + (HEAD_R - 6) * math.sin(math.radians(a)))
             for a in range(250, 109, -10)]
    body.append({"type": "poly", "points": outer + inner, "fill": shade, "outline": False, "boil": 0.5})
    body.append({"type": "circle", "x": hx, "y": hy, "r": HEAD_R, "fill": None, "width": LINE, "color": ink})
    body += _face(hx, hy, expr)
    if burnt:  # 3 tiny white peel flakes on the front of the face (nose area), nothing else changes
        for fx, fy, k in ((60, 20, 1.0), (65, 6, 0.8), (55, 31, 0.7)):
            body.append({"type": "poly", "points": [(hx + fx - 6 * k, hy + fy - 2 * k), (hx + fx + 1 * k, hy + fy - 6 * k),
                                                    (hx + fx + 6 * k, hy + fy + 1 * k), (hx + fx - 1 * k, hy + fy + 5 * k)],
                         "fill": "#ffffff", "width": 2, "color": ink, "boil": 0.3})
    cap_off = flat and "cap_off" in gear
    if not cap_off:
        body += _cap(hx, hy)
    if "scuba" in gear or "mask" in gear:
        body.append({"type": "ellipse", "x": hx + 26, "y": hy - 8, "rx": 38, "ry": 26, "fill": None, "width": 6,
                     "color": "#3a6ea5"})
        body.append({"type": "line", "points": [(hx - 60, hy - 14), (hx - 12, hy - 10)], "width": 6, "color": "#3a6ea5"})
    if "helmet" in gear:
        body.append({"type": "circle", "x": hx, "y": hy, "r": HEAD_R + 24, "fill": None, "width": 5, "color": "#7fb2d9"})
    if "sweat" in gear or el.get("expression") in ("nervous_smile", "worried"):
        body.append({"type": "poly", "points": [(hx - 64, hy - 40), (hx - 74, hy - 16), (hx - 64, hy - 8),
                                                (hx - 55, hy - 16)], "fill": "#6ec6ff", "width": 3})
    if flat:  # tilt the whole head (face, cap, gear) so he looks up at the sky; the cap stays a cap
        body = body[:n_body] + _turn(body[n_body:], HEAD_TILT, (hx, hy))
        if cap_off:
            body += _cap_on_ground(hx - HEAD_R - 80, ON_BACK_GROUND)
    return body


def _thumb(x, y, ink, skin):
    """Crude MS Paint thumbs-up at the hand point (x, y): a small round fist with a stubby thumb pointing up."""
    return [{"type": "circle", "x": x, "y": y - 4, "r": 15, "fill": skin, "width": 4, "color": ink, "boil": 0.3},
            {"type": "line", "points": [(x - 3, y - 16), (x - 3, y - 42)], "width": 10, "color": ink, "boil": 0.3}]


def _cap(hx, hy):
    r = HEAD_R
    dome = [(hx - r + 2, hy - r * 0.30), (hx - r * 0.85, hy - r * 0.78), (hx - r * 0.35, hy - r * 1.10),
            (hx + r * 0.30, hy - r * 1.10), (hx + r * 0.82, hy - r * 0.78), (hx + r - 2, hy - r * 0.30)]
    brim = [(hx + r * 0.80, hy - r * 0.42), (hx + r * 1.75, hy - r * 0.30), (hx + r * 1.70, hy - r * 0.10),
            (hx + r * 0.78, hy - r * 0.12)]
    return [{"type": "poly", "points": dome, "fill": CAP, "width": LINE, "smooth": True},
            {"type": "poly", "points": brim, "fill": CAP, "width": LINE}]


def _face(hx, hy, expr):
    """Face looks toward the viewer's right. Eyes are vertical ovals with dot pupils."""
    e = []
    ex1, ex2, ey = hx + 6, hx + 38, hy - 2
    my = hy + 34

    def eye(x, pupil_dx=3, pupil_dy=0, ry=15, rx=10):
        e.append({"type": "ellipse", "x": x, "y": ey, "rx": rx, "ry": ry, "fill": "#ffffff", "width": 3, "boil": 0.3})
        e.append({"type": "circle", "x": x + pupil_dx, "y": ey + pupil_dy, "r": 5, "fill": "#000000", "width": 1,
                  "boil": 0.2})

    def brow(x, tilt):  # tilt > 0: angry (inner end down), < 0: worried
        e.append({"type": "line", "points": [(x - 12, ey - 24 - tilt), (x + 12, ey - 24 + tilt)], "width": 4})

    if expr == "dead":
        for x in (ex1, ex2):
            e.append({"type": "line", "points": [(x - 10, ey - 10), (x + 10, ey + 10)], "width": 5})
            e.append({"type": "line", "points": [(x + 10, ey - 10), (x - 10, ey + 10)], "width": 5})
        e.append({"type": "curve", "points": [(hx + 2, my + 6), (hx + 22, my), (hx + 42, my + 6)], "width": 4})
    elif expr == "shock":  # wide open mouth with pink tongue (the most common face)
        eye(ex1, ry=17, rx=11); eye(ex2, ry=17, rx=11)
        brow(ex1, -4); brow(ex2, -4)
        e.append({"type": "ellipse", "x": hx + 24, "y": my + 4, "rx": 18, "ry": 22, "fill": "#2a0000", "width": 4})
        e.append({"type": "ellipse", "x": hx + 24, "y": my + 16, "rx": 12, "ry": 8, "fill": TONGUE, "outline": False})
    elif expr == "gritted":  # teeth grid (fear)
        eye(ex1, ry=16); eye(ex2, ry=16)
        brow(ex1, -5); brow(ex2, -5)
        x0, x1, y0, y1 = hx - 2, hx + 50, my - 8, my + 12
        e.append({"type": "rect", "x": x0, "y": y0, "w": x1 - x0, "h": y1 - y0, "fill": "#ffffff", "width": 4, "boil": 0.4})
        e.append({"type": "line", "points": [(x0, (y0 + y1) / 2), (x1, (y0 + y1) / 2)], "width": 2, "boil": 0.3})
        for i in range(1, 5):
            x = x0 + (x1 - x0) * i / 5
            e.append({"type": "line", "points": [(x, y0), (x, y1)], "width": 2, "boil": 0.3})
    elif expr == "flat":  # unimpressed
        for x in (ex1, ex2):
            e.append({"type": "ellipse", "x": x, "y": ey + 4, "rx": 10, "ry": 9, "fill": "#ffffff", "width": 3})
            e.append({"type": "line", "points": [(x - 11, ey), (x + 11, ey)], "width": 4})
            e.append({"type": "circle", "x": x + 3, "y": ey + 6, "r": 4, "fill": "#000000", "width": 1})
        e.append({"type": "line", "points": [(hx + 6, my + 2), (hx + 42, my + 2)], "width": 4})
    elif expr == "smirk":  # squint + smirk
        for x in (ex1, ex2):
            e.append({"type": "curve", "points": [(x - 10, ey + 2), (x, ey - 4), (x + 10, ey + 2)], "width": 4})
        e.append({"type": "curve", "points": [(hx + 4, my + 4), (hx + 26, my + 6), (hx + 44, my - 6)], "width": 4})
    elif expr == "hopeful":
        eye(ex1, pupil_dy=-3); eye(ex2, pupil_dy=-3)
        e.append({"type": "curve", "points": [(hx + 2, my - 6), (hx + 24, my + 10), (hx + 46, my - 6)], "width": 4})
    elif expr == "sad":
        eye(ex1, pupil_dy=3); eye(ex2, pupil_dy=3)
        brow(ex1, -6); brow(ex2, -6)
        e.append({"type": "curve", "points": [(hx + 4, my + 10), (hx + 24, my - 2), (hx + 44, my + 10)], "width": 4})
        e.append({"type": "line", "points": [(ex2, ey + 18), (ex2 + 2, ey + 44)], "width": 4, "color": "#3aa0ff"})
    elif expr == "angry":
        eye(ex1, ry=12); eye(ex2, ry=12)
        brow(ex1, 7); brow(ex2, -7)
        e.append({"type": "line", "points": [(hx + 6, my + 6), (hx + 40, my + 6)], "width": 4})
    elif expr == "confused":
        eye(ex1); eye(ex2, ry=11)
        brow(ex2, 6)
        e.append({"type": "curve", "points": [(hx + 4, my + 4), (hx + 18, my - 2), (hx + 30, my + 6), (hx + 44, my)],
                  "width": 4})
        e.append({"type": "text", "text": "?", "x": hx + 96, "y": hy - 96, "size": 64, "color": "#e0201b", "bold": True})
    elif expr == "sleepy":
        for x in (ex1, ex2):
            e.append({"type": "line", "points": [(x - 10, ey + 2), (x + 10, ey + 2)], "width": 4})
        e.append({"type": "line", "points": [(hx + 14, my + 2), (hx + 34, my + 2)], "width": 4})
    else:  # neutral
        eye(ex1); eye(ex2)
        e.append({"type": "line", "points": [(hx + 12, my + 2), (hx + 36, my + 2)], "width": 4})
    return e
