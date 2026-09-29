"""Doug: the channel's recurring stick man, as a posable rig.

Local coordinates: origin at the hips, y grows downward, figure faces right.
Doug is ~400 units tall at scale 1 (feet at y=+150, top of cap at y=-255).

Scene usage:
  {"type": "doug", "x": 960, "y": 700, "scale": 1, "pose": "arms_up",
   "expression": "scared", "gear": ["scuba"], "facing": "right"}
`pose` may be a list, e.g. ["swim1", "swim2"]; it cycles with the boil variant
(the GIF-like loop). Same for `expression`.
"""
from __future__ import annotations

import math

INK = "#000000"
CAP = "#e0201b"      # Doug's signature red cap
SKIN = "#ffffff"     # head fill (keeps backgrounds from showing through)

HEAD_R = 42
NECK = (0, -150)
HEAD_C = (0, -150 - HEAD_R - 2)
SHOULDER = (0, -120)
HIP = (0, 0)
UPPER_ARM, FOREARM = 62, 58
THIGH, SHIN = 78, 74
LINE = 7

# angles in degrees: 0 = straight down, 90 = pointing right (forward), -90 = back, 180 = up
POSES = {
    "stand":    dict(arm_f=(20, 10), arm_b=(-20, -10), leg_f=(12, 0), leg_b=(-12, 0), lean=0),
    "wave":     dict(arm_f=(115, 55), arm_b=(-20, -10), leg_f=(12, 0), leg_b=(-12, 0), lean=0),
    "point":    dict(arm_f=(95, 95), arm_b=(-20, -10), leg_f=(12, 0), leg_b=(-12, 0), lean=0),
    "arms_up":  dict(arm_f=(120, 40), arm_b=(-120, -40), leg_f=(18, 5), leg_b=(-18, -5), lean=0),
    "panic1":   dict(arm_f=(125, 50), arm_b=(-115, -30), leg_f=(30, -10), leg_b=(-15, 0), lean=0),
    "panic2":   dict(arm_f=(115, 30), arm_b=(-125, -50), leg_f=(15, 0), leg_b=(-30, 10), lean=0),
    "shrug":    dict(arm_f=(60, 150), arm_b=(-60, -150), leg_f=(12, 0), leg_b=(-12, 0), lean=0),
    "think":    dict(arm_f=(30, 140), arm_b=(-20, -10), leg_f=(12, 0), leg_b=(-12, 0), lean=0),
    "hands_hips": dict(arm_f=(60, -40), arm_b=(-60, 40), leg_f=(15, 0), leg_b=(-15, 0), lean=0),
    "walk1":    dict(arm_f=(35, 60), arm_b=(-35, -10), leg_f=(30, 0), leg_b=(-30, -20), lean=4),
    "walk2":    dict(arm_f=(-30, -5), arm_b=(30, 60), leg_f=(-25, -20), leg_b=(25, 0), lean=4),
    "run1":     dict(arm_f=(70, 150), arm_b=(-60, -20), leg_f=(70, 0), leg_b=(-50, -110), lean=15),
    "run2":     dict(arm_f=(-60, -20), arm_b=(70, 150), leg_f=(-50, -110), leg_b=(70, 0), lean=15),
    "swim1":    dict(arm_f=(160, 110), arm_b=(-150, -170), leg_f=(20, 40), leg_b=(-20, -40), lean=70),
    "swim2":    dict(arm_f=(110, 60), arm_b=(170, 150), leg_f=(-10, 20), leg_b=(10, -20), lean=70),
    "float":    dict(arm_f=(110, 130), arm_b=(-110, -130), leg_f=(25, 15), leg_b=(-25, -15), lean=0),
    "sit":      dict(arm_f=(30, 80), arm_b=(-10, 30), leg_f=(90, 0), leg_b=(80, 0), lean=0, drop=70),
    "fall":     dict(arm_f=(160, 120), arm_b=(-120, -160), leg_f=(150, 120), leg_b=(-150, -130), lean=0),
    "cower":    dict(arm_f=(140, 60), arm_b=(-140, -60), leg_f=(60, -30), leg_b=(-40, 30), lean=10, drop=40),
    "lie":      dict(arm_f=(10, 0), arm_b=(-10, 0), leg_f=(5, 0), leg_b=(-5, 0), lean=0),
    "dive":     dict(arm_f=(175, 180), arm_b=(-175, -180), leg_f=(3, 0), leg_b=(-3, 0), lean=0),
}

EXPRESSIONS = ["neutral", "happy", "scared", "shocked", "worried", "dead", "smug", "crying",
               "confused", "angry", "sleepy", "determined", "screaming", "nervous_smile"]


def _limb(start, a1, a2, l1, l2):
    def seg(p, a, l):
        r = math.radians(a)
        return (p[0] + l * math.sin(r), p[1] + l * math.cos(r))
    mid = seg(start, a1, l1)
    end = seg(mid, a2, l2)
    return [start, mid, end]


def _rot(p, deg, origin=(0, 0)):
    r = math.radians(deg)
    x, y = p[0] - origin[0], p[1] - origin[1]
    return (origin[0] + x * math.cos(r) - y * math.sin(r), origin[1] + x * math.sin(r) + y * math.cos(r))


def _pick(v, variant):
    if isinstance(v, list):
        return v[variant % len(v)] if v else None
    return v


def doug_elements(el: dict, variant: int = 0):
    pose_name = _pick(el.get("pose", "stand"), variant)
    expr = _pick(el.get("expression", "neutral"), variant)
    pose = dict(POSES.get(pose_name, POSES["stand"]))
    gear = el.get("gear", []) or []
    lean = pose.get("lean", 0)
    drop = pose.get("drop", 0)

    def L(p):  # apply lean around the hips, then drop (for sitting)
        q = _rot(p, lean)
        return (q[0], q[1] + drop)

    hip = L(HIP)
    shoulder = L(SHOULDER)
    neck = L(NECK)
    head = L(HEAD_C)

    ink = el.get("ink", INK)
    body = []
    # legs first (behind), then torso, then arms, then head
    for key in ("leg_b", "leg_f"):
        a1, a2 = pose[key]
        pts = _limb(HIP, a1 - lean, a1 + a2 - lean, THIGH, SHIN)
        pts = [(p[0], p[1] + drop) for p in pts]
        body.append({"type": "line", "points": pts, "width": LINE, "color": ink})
    body.append({"type": "line", "points": [hip, neck], "width": LINE, "color": ink})
    arm_origin = shoulder
    for key in ("arm_b", "arm_f"):
        a1, a2 = pose[key]
        pts = _limb((0, 0), a1 - lean, a1 + a2 - lean, UPPER_ARM, FOREARM)
        pts = [(p[0] + arm_origin[0], p[1] + arm_origin[1]) for p in pts]
        body.append({"type": "line", "points": pts, "width": LINE, "color": ink})

    if "tank" in gear or "scuba" in gear:
        bx, by = L((-38, -110))
        body.insert(0, {"type": "rect", "x": bx - 22, "y": by - 10, "w": 30, "h": 95,
                        "fill": "#f2c21b", "width": 5})

    hx, hy = head
    body.append({"type": "circle", "x": hx, "y": hy, "r": HEAD_R, "fill": SKIN, "width": LINE, "color": ink})
    body += _face(hx, hy, expr, lean)
    body += _cap(hx, hy, lean)
    if "scuba" in gear or "mask" in gear:
        body.append({"type": "ellipse", "x": hx + 16, "y": hy - 6, "rx": 26, "ry": 18,
                     "fill": None, "width": 6, "color": "#3a6ea5"})
        body.append({"type": "line", "points": [(hx - 28, hy - 8), (hx - 10, hy - 8)], "width": 6,
                     "color": "#3a6ea5"})
    if "helmet" in gear:
        body.append({"type": "circle", "x": hx, "y": hy, "r": HEAD_R + 22, "fill": None,
                     "width": 5, "color": "#7fb2d9"})
    if "sweat" in gear or expr in ("nervous_smile", "worried"):
        body.append({"type": "poly", "points": [(hx - 44, hy - 30), (hx - 52, hy - 12), (hx - 44, hy - 6),
                                                (hx - 37, hy - 12)], "fill": "#6ec6ff", "width": 3})
    return body


def _cap(hx, hy, lean):
    dome = [(hx - HEAD_R + 2, hy - 14), (hx - HEAD_R + 8, hy - 34), (hx - 18, hy - HEAD_R - 6),
            (hx + 12, hy - HEAD_R - 6), (hx + HEAD_R - 6, hy - 32), (hx + HEAD_R - 2, hy - 14)]
    brim = [(hx + HEAD_R - 10, hy - 20), (hx + HEAD_R + 38, hy - 14), (hx + HEAD_R + 34, hy - 2),
            (hx + HEAD_R - 12, hy - 4)]
    return [{"type": "poly", "points": dome, "fill": CAP, "width": 5, "smooth": True},
            {"type": "poly", "points": brim, "fill": CAP, "width": 5}]


def _face(hx, hy, expr, lean):
    ex1, ex2, ey = hx + 4, hx + 24, hy - 2  # Doug looks right (toward the viewer's right)
    e = []

    def dot(x, y, r=5):
        e.append({"type": "circle", "x": x, "y": y, "r": r, "fill": INK, "width": 1, "boil": 0.3})

    def mouth(points, fill=None, width=4):
        if fill:
            e.append({"type": "poly", "points": points, "fill": fill, "width": width, "boil": 0.5})
        else:
            e.append({"type": "curve", "points": points, "width": width, "boil": 0.5})

    my = hy + 18
    if expr == "dead":
        for x in (ex1, ex2):
            e.append({"type": "line", "points": [(x - 6, ey - 6), (x + 6, ey + 6)], "width": 4})
            e.append({"type": "line", "points": [(x + 6, ey - 6), (x - 6, ey + 6)], "width": 4})
        mouth([(hx + 2, my + 4), (hx + 14, my), (hx + 26, my + 4)])
    elif expr in ("scared", "screaming", "shocked"):
        for x in (ex1, ex2):
            e.append({"type": "circle", "x": x, "y": ey - 2, "r": 8, "fill": "#ffffff", "width": 3})
            dot(x + 1, ey - 2, 3)
        if expr == "screaming":
            mouth([(hx + 2, my - 6), (hx + 26, my - 6), (hx + 22, my + 16), (hx + 6, my + 16)], "#5a0000", 4)
        elif expr == "shocked":
            e.append({"type": "ellipse", "x": hx + 14, "y": my + 2, "rx": 7, "ry": 10, "fill": INK, "width": 3})
        else:
            mouth([(hx + 2, my + 4), (hx + 8, my - 2), (hx + 14, my + 4), (hx + 20, my - 2), (hx + 26, my + 4)])
    elif expr == "happy":
        dot(ex1, ey); dot(ex2, ey)
        mouth([(hx + 0, my - 4), (hx + 14, my + 8), (hx + 28, my - 4)])
    elif expr == "smug":
        e.append({"type": "line", "points": [(ex1 - 6, ey), (ex1 + 6, ey)], "width": 4})
        e.append({"type": "line", "points": [(ex2 - 6, ey), (ex2 + 6, ey)], "width": 4})
        mouth([(hx + 4, my + 2), (hx + 18, my + 2), (hx + 28, my - 6)])
    elif expr == "crying":
        dot(ex1, ey); dot(ex2, ey)
        mouth([(hx + 2, my + 8), (hx + 14, my - 2), (hx + 26, my + 8)])
        e.append({"type": "line", "points": [(ex2, ey + 8), (ex2 + 2, ey + 30)], "width": 4, "color": "#3aa0ff"})
    elif expr == "worried":
        dot(ex1, ey); dot(ex2, ey)
        e.append({"type": "line", "points": [(ex1 - 8, ey - 16), (ex1 + 6, ey - 12)], "width": 3})
        e.append({"type": "line", "points": [(ex2 - 6, ey - 12), (ex2 + 8, ey - 16)], "width": 3})
        mouth([(hx + 2, my + 6), (hx + 14, my), (hx + 26, my + 6)])
    elif expr == "angry":
        dot(ex1, ey + 2); dot(ex2, ey + 2)
        e.append({"type": "line", "points": [(ex1 - 8, ey - 14), (ex1 + 6, ey - 8)], "width": 4})
        e.append({"type": "line", "points": [(ex2 - 6, ey - 8), (ex2 + 8, ey - 14)], "width": 4})
        mouth([(hx + 4, my + 4), (hx + 24, my + 4)])
    elif expr == "confused":
        dot(ex1, ey); dot(ex2, ey - 4, 6)
        mouth([(hx + 2, my + 2), (hx + 12, my - 2), (hx + 20, my + 4), (hx + 28, my)])
        e.append({"type": "text", "text": "?", "x": hx + 58, "y": hy - 62, "size": 48})
    elif expr == "sleepy":
        e.append({"type": "line", "points": [(ex1 - 6, ey), (ex1 + 6, ey)], "width": 4})
        e.append({"type": "line", "points": [(ex2 - 6, ey), (ex2 + 6, ey)], "width": 4})
        mouth([(hx + 8, my), (hx + 20, my)])
    elif expr == "determined":
        dot(ex1, ey); dot(ex2, ey)
        e.append({"type": "line", "points": [(ex1 - 8, ey - 14), (ex1 + 6, ey - 9)], "width": 4})
        e.append({"type": "line", "points": [(ex2 - 6, ey - 9), (ex2 + 8, ey - 14)], "width": 4})
        mouth([(hx + 2, my + 2), (hx + 14, my + 6), (hx + 26, my)])
    elif expr == "nervous_smile":
        dot(ex1, ey); dot(ex2, ey)
        mouth([(hx + 0, my - 2), (hx + 28, my - 2), (hx + 24, my + 8), (hx + 4, my + 8)], "#ffffff", 3)
        e.append({"type": "line", "points": [(hx + 7, my - 2), (hx + 7, my + 8)], "width": 2})
        e.append({"type": "line", "points": [(hx + 14, my - 2), (hx + 14, my + 8)], "width": 2})
        e.append({"type": "line", "points": [(hx + 21, my - 2), (hx + 21, my + 8)], "width": 2})
    else:  # neutral
        dot(ex1, ey); dot(ex2, ey)
        mouth([(hx + 6, my + 2), (hx + 22, my + 2)])
    return e
