"""2D toon engine for the What If format (pilot w01, 2026-11-26).

A new look for Doomed Doug, separate from the MS Paint engine (paint.py): clean antialiased outlines, flat colour
with one cel-shade tone, rigged characters with real bodies and clothes, layered backgrounds and a moving camera.
Everything is vector, drawn with Pillow at SS-times supersampling and reduced, so it renders on CPU only (GitHub
runners or the PC) with no new packages.

Coordinates: characters and props are drawn in their own local units (a character is ~430 units tall at scale 1,
origin at the hips, y down, facing right). Sets are drawn in a 1920x1080 "world"; the camera crops the world.
"""
from __future__ import annotations

import math
import random
from functools import lru_cache
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
FONTS = ROOT / "assets" / "fonts"
SS = 3                      # supersampling for sprites and overlays
INK = (28, 22, 34, 255)     # outline colour (warm near-black, never pure black)
OUT = 4.2                   # outline width in local units at scale 1


# ------------------------------------------------------------------ colour helpers

def rgba(c, a=255):
    if c is None:
        return None
    if isinstance(c, tuple):
        return c if len(c) == 4 else (*c, a)
    c = c.lstrip("#")
    if len(c) == 3:
        c = "".join(ch * 2 for ch in c)
    r, g, b = int(c[0:2], 16), int(c[2:4], 16), int(c[4:6], 16)
    if len(c) == 8:
        a = int(c[6:8], 16)
    return (r, g, b, a)


def shade(c, k=0.78):
    r, g, b, a = rgba(c)
    return (int(r * k), int(g * k), int(b * k), a)


def tint(c, k=0.25, to=(255, 255, 255)):
    r, g, b, a = rgba(c)
    return (int(r + (to[0] - r) * k), int(g + (to[1] - g) * k), int(b + (to[2] - b) * k), a)


def mix(c1, c2, t):
    a, b = rgba(c1), rgba(c2)
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(4))


@lru_cache(maxsize=128)
def font(size: int, name: str = "Quicksand-Bold"):
    for p in (FONTS / f"{name}.ttf", FONTS / name, FONTS / "Quicksand-Bold.ttf", FONTS / "Arimo.ttf"):
        if p.exists():
            return ImageFont.truetype(str(p), max(4, int(size)))
    return ImageFont.load_default()


def ease(t, kind="inout"):
    t = max(0.0, min(1.0, t))
    if kind == "in":
        return t * t
    if kind == "out":
        return 1 - (1 - t) * (1 - t)
    if kind == "back":  # overshoot pop
        c = 1.9
        return 1 + (c + 1) * (t - 1) ** 3 + c * (t - 1) ** 2
    if kind == "linear":
        return t
    return t * t * (3 - 2 * t)


# ------------------------------------------------------------------ the pen

class Pen:
    """Draws vector shapes through an affine transform stack. Every shape becomes a polygon or polyline."""

    def __init__(self, img: Image.Image, ox=0.0, oy=0.0, s=1.0, flip=False):
        self.img = img
        self.d = ImageDraw.Draw(img)
        sx = -s if flip else s
        self.m = [(sx, 0.0, ox, 0.0, s, oy)]

    # transform stack
    def push(self, x=0.0, y=0.0, rot=0.0, scale=1.0, sx=None, sy=None):
        a, b, c, d, e, f = self.m[-1]
        r = math.radians(rot)
        cs, sn = math.cos(r), math.sin(r)
        kx = scale if sx is None else sx * scale
        ky = scale if sy is None else sy * scale
        # local = T(x,y) * R * S
        la, lb, lc = cs * kx, -sn * ky, x
        ld, le, lf = sn * kx, cs * ky, y
        self.m.append((a * la + b * ld, a * lb + b * le, a * lc + b * lf + c,
                       d * la + e * ld, d * lb + e * le, d * lc + e * lf + f))

    def pop(self):
        self.m.pop()

    def tp(self, p):
        a, b, c, d, e, f = self.m[-1]
        return (a * p[0] + b * p[1] + c, d * p[0] + e * p[1] + f)

    @property
    def k(self):
        a, b, c, d, e, f = self.m[-1]
        return math.sqrt(abs(a * e - b * d))

    # primitives
    def poly(self, pts, fill=None, ow=OUT, ink=INK):
        q = [self.tp(p) for p in pts]
        if len(q) < 3:
            return
        if fill is not None:
            self.d.polygon(q, fill=rgba(fill))
        if ow and ink is not None:
            w = max(1, int(round(ow * self.k)))
            self.d.line(q + [q[0], q[1]], fill=rgba(ink), width=w, joint="curve")

    def line(self, pts, color=INK, w=OUT, caps=True):
        q = [self.tp(p) for p in pts]
        ww = max(1, int(round(w * self.k)))
        self.d.line(q, fill=rgba(color), width=ww, joint="curve")
        if caps:
            r = ww / 2
            for p in (q[0], q[-1]):
                self.d.ellipse([p[0] - r, p[1] - r, p[0] + r, p[1] + r], fill=rgba(color))

    def limb(self, pts, w, fill, ow=OUT, ink=INK):
        if ow:
            self.line(pts, ink, w + 2 * ow)
        self.line(pts, fill, w)

    def ellipse(self, cx, cy, rx, ry, fill=None, ow=OUT, rot=0.0, a0=0.0, a1=360.0, n=44, ink=INK, closed=True):
        pts = ellipse_pts(cx, cy, rx, ry, rot, a0, a1, n)
        if closed:
            if a1 - a0 < 360:
                pts = [(cx, cy)] + pts
            self.poly(pts, fill, ow, ink)
        else:
            self.line(pts, ink, ow)

    def circle(self, cx, cy, r, fill=None, ow=OUT, ink=INK):
        self.ellipse(cx, cy, r, r, fill, ow, ink=ink)

    def rrect(self, x, y, w, h, r, fill=None, ow=OUT, ink=INK):
        self.poly(rrect_pts(x, y, w, h, r), fill, ow, ink)

    def blob(self, ctrl, fill=None, ow=OUT, ink=INK, n=10):
        """Smooth closed shape through control points (Catmull-Rom)."""
        self.poly(catmull(ctrl, n, closed=True), fill, ow, ink)

    def curve(self, ctrl, color=INK, w=OUT, n=10):
        self.line(catmull(ctrl, n, closed=False), color, w)

    def text(self, x, y, s, size, color=INK, name="Quicksand-Bold", anchor="mm", stroke=0, stroke_color=INK):
        p = self.tp((x, y))
        f = font(int(size * self.k), name)
        self.d.text(p, s, font=f, fill=rgba(color), anchor=anchor,
                    stroke_width=int(stroke * self.k), stroke_fill=rgba(stroke_color))


def ellipse_pts(cx, cy, rx, ry, rot=0.0, a0=0.0, a1=360.0, n=44):
    r = math.radians(rot)
    cs, sn = math.cos(r), math.sin(r)
    out = []
    steps = max(6, int(n * (a1 - a0) / 360))
    for i in range(steps + (0 if a1 - a0 >= 360 else 1)):
        t = math.radians(a0 + (a1 - a0) * i / steps)
        x, y = rx * math.cos(t), ry * math.sin(t)
        out.append((cx + x * cs - y * sn, cy + x * sn + y * cs))
    return out


def rrect_pts(x, y, w, h, r, n=6):
    r = min(r, w / 2, h / 2)
    pts = []
    for cx, cy, a in ((x + w - r, y + r, -90), (x + w - r, y + h - r, 0), (x + r, y + h - r, 90), (x + r, y + r, 180)):
        for i in range(n + 1):
            t = math.radians(a + 90 * i / n)
            pts.append((cx + r * math.cos(t), cy + r * math.sin(t)))
    return pts


def catmull(ctrl, n=10, closed=True):
    pts = list(ctrl)
    if len(pts) < 3:
        return pts
    out = []
    m = len(pts)
    rng = range(m) if closed else range(m - 1)
    for i in rng:
        p0 = pts[(i - 1) % m] if closed or i > 0 else pts[0]
        p1 = pts[i]
        p2 = pts[(i + 1) % m]
        p3 = pts[(i + 2) % m] if closed or i + 2 < m else pts[-1]
        for j in range(n):
            t = j / n
            t2, t3 = t * t, t * t * t
            out.append(tuple(0.5 * ((2 * p1[k]) + (-p0[k] + p2[k]) * t + (2 * p0[k] - 5 * p1[k] + 4 * p2[k] - p3[k]) * t2
                                    + (-p0[k] + 3 * p1[k] - 3 * p2[k] + p3[k]) * t3) for k in (0, 1)))
    if not closed:
        out.append(pts[-1])
    return out


def seg(p, ang, length):
    """Angle convention: 0 = straight down, 90 = forward (+x), 180 = up, -90 = back."""
    r = math.radians(ang)
    return (p[0] + length * math.sin(r), p[1] + length * math.cos(r))


# ------------------------------------------------------------------ sprites

def sprite(draw_fn, bbox, scale, flip=False, ss=SS):
    """Render draw_fn(pen) for local bbox (x0,y0,x1,y1) at `scale` px per unit. Returns (RGBA image, offset of local
    origin inside the image) at output resolution."""
    x0, y0, x1, y1 = bbox
    pad = 6
    w = int((x1 - x0) * scale) + pad * 2
    h = int((y1 - y0) * scale) + pad * 2
    if w <= 0 or h <= 0:
        return None, (0, 0)
    img = Image.new("RGBA", (w * ss, h * ss), (0, 0, 0, 0))
    ox = (-x0 * scale + pad) if not flip else (x1 * scale + pad)
    oy = -y0 * scale + pad
    pen = Pen(img, ox * ss, oy * ss, scale * ss, flip=flip)
    draw_fn(pen)
    return img.reduce(ss), (ox, oy)


def paste(frame: Image.Image, img: Image.Image, origin, at, alpha=1.0):
    if img is None:
        return
    x = int(round(at[0] - origin[0]))
    y = int(round(at[1] - origin[1]))
    if alpha < 0.999:
        img = img.copy()
        a = img.getchannel("A").point(lambda v: int(v * alpha))
        img.putalpha(a)
    sx0, sy0 = max(0, -x), max(0, -y)
    sx1 = min(img.width, frame.width - x)
    sy1 = min(img.height, frame.height - y)
    if sx1 <= sx0 or sy1 <= sy0:
        return
    frame.alpha_composite(img.crop((sx0, sy0, sx1, sy1)), (max(0, x), max(0, y)))


# ------------------------------------------------------------------ characters

# Poses: arm/leg = (upper angle, bend of the lower part relative to the upper). lean tilts the torso (deg forward),
# drop lowers the hips (sitting, crouching). Angles follow seg(): 0 down, 90 forward, 180 up.
POSES = {
    "stand":      dict(af=(12, 8), ab=(-12, -8), lf=(6, 0), lb=(-6, 0)),
    "talk1":      dict(af=(40, 70), ab=(-12, -8), lf=(6, 0), lb=(-6, 0)),
    "talk2":      dict(af=(55, 50), ab=(-14, -10), lf=(6, 0), lb=(-6, 0)),
    "explain1":   dict(af=(70, 40), ab=(-40, -60), lf=(6, 0), lb=(-6, 0)),
    "explain2":   dict(af=(85, 20), ab=(-55, -50), lf=(6, 0), lb=(-6, 0)),
    "wave1":      dict(af=(130, 25), ab=(-12, -8), lf=(6, 0), lb=(-6, 0)),
    "wave2":      dict(af=(125, -20), ab=(-12, -8), lf=(6, 0), lb=(-6, 0)),
    "point":      dict(af=(92, 0), ab=(-12, -8), lf=(8, 0), lb=(-8, 0)),
    "point_up":   dict(af=(140, 15), ab=(-12, -8), lf=(6, 0), lb=(-6, 0)),
    "arms_up":    dict(af=(135, 15), ab=(-140, -10), lf=(12, 0), lb=(-12, 0)),
    "cheer1":     dict(af=(132, 18), ab=(-145, -10), lf=(14, 0), lb=(-14, 0), hop=10),
    "cheer2":     dict(af=(118, 40), ab=(-125, -30), lf=(8, 0), lb=(-8, 0)),
    "shrug":      dict(af=(55, 110), ab=(-55, -110), lf=(6, 0), lb=(-6, 0)),
    "think":      dict(af=(35, 120), ab=(-20, -60), lf=(6, 0), lb=(-6, 0)),
    "hips":       dict(af=(45, -95), ab=(-45, 95), lf=(10, 0), lb=(-10, 0)),
    "worry":      dict(af=(30, 110), ab=(-25, -120), lf=(4, 0), lb=(-4, 0), head_tilt=-4),
    "panic1":     dict(af=(130, 30), ab=(-150, -10), lf=(28, -20), lb=(-14, 0), hop=6),
    "panic2":     dict(af=(118, -5), ab=(-160, -25), lf=(14, 0), lb=(-28, 20)),
    "hold":       dict(af=(70, 30), ab=(65, 35), lf=(6, 0), lb=(-6, 0)),
    "hold_up":    dict(af=(130, 20), ab=(125, 25), lf=(8, 0), lb=(-8, 0)),
    "phone":      dict(af=(40, 118), ab=(-12, -8), lf=(6, 0), lb=(-6, 0), head_tilt=6),
    "phone_look": dict(af=(60, 75), ab=(40, 80), lf=(6, 0), lb=(-6, 0), head_tilt=10),
    "facepalm":   dict(af=(45, 118), ab=(-12, -8), lf=(6, 0), lb=(-6, 0), head_tilt=12),
    "thumbs":     dict(af=(70, 85), ab=(-12, -8), lf=(6, 0), lb=(-6, 0), thumb=True),
    "reach":      dict(af=(100, 5), ab=(80, 10), lf=(20, 0), lb=(-25, 0), lean=12),
    "cower":      dict(af=(120, 70), ab=(-110, -60), lf=(40, -50), lb=(-20, 30), lean=10, drop=25),
    "walk1":      dict(af=(-25, 10), ab=(25, 20), lf=(25, 0), lb=(-25, 15), bob=1),
    "walk2":      dict(af=(0, 10), ab=(0, 10), lf=(5, 25), lb=(-5, 0), bob=0),
    "walk3":      dict(af=(25, 20), ab=(-25, 10), lf=(-25, 15), lb=(25, 0), bob=1),
    "walk4":      dict(af=(0, 10), ab=(0, 10), lf=(-5, 0), lb=(5, 25), bob=0),
    "run1":       dict(af=(-50, 80), ab=(70, 90), lf=(55, 10), lb=(-45, 90), lean=14, hop=8),
    "run2":       dict(af=(70, 90), ab=(-50, 80), lf=(-45, 90), lb=(55, 10), lean=14),
    "sit":        dict(af=(25, 40), ab=(15, 45), lf=(88, -88), lb=(80, -82), drop=105),
    "sit_talk":   dict(af=(50, 60), ab=(15, 45), lf=(88, -88), lb=(80, -82), drop=105),
    "crouch":     dict(af=(95, 15), ab=(60, 20), lf=(100, -125), lb=(55, -110), lean=18, drop=70),
    "kneel":      dict(af=(70, 30), ab=(40, 30), lf=(90, -90), lb=(-10, -80), drop=60, lean=6),
    "swim1":      dict(af=(165, 10), ab=(130, 10), lf=(15, 25), lb=(-15, -10), lean=72),
    "swim2":      dict(af=(120, 10), ab=(170, 10), lf=(-10, 10), lb=(15, 25), lean=72),
    "tread1":     dict(af=(80, 30), ab=(-80, -30), lf=(20, 30), lb=(-15, 20)),
    "tread2":     dict(af=(100, 10), ab=(-100, -10), lf=(5, 20), lb=(-25, 30)),
    "lean_rail":  dict(af=(60, 40), ab=(50, 45), lf=(8, 0), lb=(-14, 0), lean=10),
    "salute":     dict(af=(125, 95), ab=(-8, -6), lf=(4, 0), lb=(-4, 0)),
    "arms_cross": dict(af=(30, 115), ab=(40, 100), lf=(8, 0), lb=(-8, 0)),
    "smug":       dict(af=(45, -95), ab=(-45, 95), lf=(14, 0), lb=(-4, 0), head_tilt=-6),
    "sleep":      dict(af=(20, 40), ab=(10, 40), lf=(88, -88), lb=(80, -82), drop=105, head_tilt=18),
}

# Emotion tags from the script -> (eyes, brows, mouth, default pose cycle)
EMOTIONS = {
    "neutral":    ("open", "flat", "smile", ["talk1", "talk2"]),
    "calm":       ("open", "flat", "smile", ["talk1", "talk2"]),
    "happy":      ("happy", "up", "grin", ["talk1", "cheer2"]),
    "excited":    ("wide", "up", "grin", ["cheer1", "cheer2"]),
    "proud":      ("happy", "up", "grin", ["hips", "talk1"]),
    "amazed":     ("wide", "up", "o", ["arms_up", "cheer2"]),
    "shock":      ("wide", "up", "o", ["panic1", "panic2"]),
    "shocked":    ("wide", "up", "o", ["panic1", "panic2"]),
    "scared":     ("wide", "worry", "wobble", ["cower", "worry"]),
    "panic":      ("wide", "worry", "o", ["panic1", "panic2"]),
    "worried":    ("open", "worry", "wobble", ["worry", "talk1"]),
    "nervous":    ("open", "worry", "wobble", ["worry", "shrug"]),
    "sad":        ("open", "worry", "frown", ["stand", "talk1"]),
    "angry":      ("angry", "angry", "grit", ["point", "hips"]),
    "annoyed":    ("half", "angry", "flat", ["arms_cross", "hips"]),
    "smug":       ("half", "smug", "smirk", ["smug", "hips"]),
    "mocking":    ("half", "smug", "smirk", ["point", "smug"]),
    "sarcastic":  ("half", "smug", "smirk", ["shrug", "arms_cross"]),
    "confused":   ("open", "confused", "flat", ["shrug", "think"]),
    "thinking":   ("open", "confused", "flat", ["think", "think"]),
    "serious":    ("open", "angry", "flat", ["explain1", "explain2"]),
    "stern":      ("half", "angry", "flat", ["arms_cross", "point"]),
    "firm":       ("open", "angry", "flat", ["explain1", "point"]),
    "determined": ("open", "angry", "grin", ["hips", "point"]),
    "explaining": ("open", "flat", "smile", ["explain1", "explain2"]),
    "nerdy":      ("wide", "up", "grin", ["explain1", "explain2"]),
    "curious":    ("wide", "up", "smile", ["think", "talk1"]),
    "whisper":    ("open", "worry", "smile", ["talk1", "talk1"]),
    "tired":      ("half", "flat", "flat", ["stand", "talk1"]),
    "relieved":   ("happy", "up", "grin", ["stand", "talk1"]),
    "soft":       ("happy", "up", "smile", ["talk1", "stand"]),
    "embarrassed": ("happy", "worry", "wobble", ["shrug", "worry"]),
    "deadpan":    ("half", "flat", "flat", ["stand", "stand"]),
    "yelling":    ("angry", "angry", "o", ["point", "explain2"]),
    "loud":       ("wide", "up", "o", ["arms_up", "point"]),
}


class Look:
    """A character design. All colours are hex strings."""

    def __init__(self, skin="#f2c9a0", hair=("short", "#3b2a20"), top=("tee", "#f2b431"), bottom="#3e5a8a",
                 shoes="#f4f1ea", extras=(), head_r=64, height=1.0, build=1.0, eyes="#1c1622"):
        self.skin, self.hair, self.top, self.bottom, self.shoes = skin, hair, top, bottom, shoes
        self.extras = set(extras)
        self.head_r, self.height, self.build, self.eye_col = head_r, height, build, eyes


def _lerp_pose(a, b, t):
    out = {}
    for k in set(a) | set(b):
        va, vb = a.get(k, 0), b.get(k, 0)
        if isinstance(va, tuple) or isinstance(vb, tuple):
            va = va or (0, 0)
            vb = vb or (0, 0)
            out[k] = tuple(va[i] + (vb[i] - va[i]) * t for i in range(2))
        elif isinstance(va, bool) or isinstance(vb, bool):
            out[k] = vb if t > 0.5 else va
        else:
            out[k] = va + (vb - va) * t
    return out


def pose_at(cycle, t, rate=1.4, phase=0.0):
    """Smoothly cycle through a list of pose names at `rate` changes per second."""
    names = cycle if isinstance(cycle, (list, tuple)) else [cycle]
    if len(names) == 1:
        return dict(POSES.get(names[0], POSES["stand"]))
    x = t * rate + phase
    i = int(math.floor(x)) % len(names)
    j = (i + 1) % len(names)
    f = ease(x - math.floor(x))
    return _lerp_pose(POSES.get(names[i], POSES["stand"]), POSES.get(names[j], POSES["stand"]), f)


CHAR_BBOX = (-190, -360, 190, 190)


def draw_character(pen: Pen, look: Look, pose: dict, eyes="open", brows="flat", mouth="smile", talk=0.0,
                   blink=False, look_dir=1.0, extra_props=()):
    """Draw a character at the pen's origin (hips). talk 0..1 opens the mouth (lip flap)."""
    b = look.build
    hh = look.height
    head_r = look.head_r
    drop = pose.get("drop", 0) + (-pose.get("hop", 0))
    lean = pose.get("lean", 0)
    hip = (0, drop)
    torso_len = 118 * hh
    sh = seg(hip, 180 + lean, torso_len)          # shoulder point
    neck = seg(hip, 180 + lean, torso_len + 14)
    head_c = seg(neck, 180 + lean * 0.5 + pose.get("head_tilt", 0), head_r - 6)
    ua, la = 58 * hh, 54 * hh
    ul, ll = 66 * hh, 62 * hh
    arm_w, leg_w = 19 * b, 23 * b

    skin = look.skin
    top_style, top_col = look.top
    sleeve = top_col if top_style in ("tee", "hoodie", "jacket", "coat", "uniform", "vest_tee", "polo") else skin
    long_sleeve = top_style in ("hoodie", "jacket", "coat", "uniform")
    pants = look.bottom
    shoes = look.shoes

    tw_top, tw_bot = 44 * b, 40 * b

    def arm(side):
        a1, a2 = pose["af"] if side == "f" else pose["ab"]
        off = 0.5 * tw_top if side == "f" else -0.5 * tw_top
        s0 = (sh[0] + off, sh[1] + 10)
        elbow = seg(s0, a1, ua)
        hand = seg(elbow, a1 + a2, la)
        dark = side == "b"
        sc = shade(sleeve, 0.82) if dark else sleeve
        kc = shade(skin, 0.86) if dark else skin
        if long_sleeve:
            pen.limb([s0, elbow, hand], arm_w, sc)
        else:
            pen.limb([elbow, hand], arm_w * 0.86, kc)
            pen.limb([s0, elbow], arm_w * 1.08, sc)
            pen.line([s0, seg(s0, a1, ua * 0.92)], sc, arm_w * 1.08 - 2)
        pen.circle(hand[0], hand[1], 11.5 * b, kc, ow=OUT * 0.9)
        if side == "f" and pose.get("thumb"):
            tip = (hand[0] + 3, hand[1] - 22)
            pen.limb([hand, tip], 8, kc, ow=OUT * 0.8)
        return hand

    def leg(side):
        a1, a2 = pose["lf"] if side == "f" else pose["lb"]
        off = (10, 0) if side == "f" else (-10, 0)
        h0 = (hip[0] + off[0], hip[1] - 4)
        knee = seg(h0, a1, ul)
        foot = seg(knee, a1 + a2, ll)
        dark = side == "b"
        pc = shade(pants, 0.8) if dark else pants
        if top_style == "dress":
            pc = shade(skin, 0.86) if dark else skin
        pen.limb([h0, knee, foot], leg_w, pc)
        shc = shade(shoes, 0.8) if dark else shoes
        pen.ellipse(foot[0] + 11, foot[1] + 4, 20 * b, 11, shc, ow=OUT * 0.9)
        return foot

    # back limbs
    arm("b")
    leg("b")
    leg("f")
    # torso
    ang = math.radians(lean)
    ux, uy = math.sin(ang), -math.cos(ang)       # up vector of the torso
    px, py = -uy, ux                              # perpendicular (to the right)
    def tpt(along, across):
        return (hip[0] + ux * along + px * across, hip[1] + uy * along + py * across)
    hem = -10 if top_style not in ("coat", "dress") else -42
    body = [tpt(hem, -tw_bot), tpt(hem - 4, 0), tpt(hem, tw_bot), tpt(torso_len * 0.6, tw_top + 4),
            tpt(torso_len + 4, tw_top - 6), tpt(torso_len + 12, 0), tpt(torso_len + 4, -tw_top + 6),
            tpt(torso_len * 0.6, -tw_top - 4)]
    if top_style != "dress":
        pen.blob([tpt(4, -tw_bot + 2), tpt(4, tw_bot - 2), tpt(-14, tw_bot - 4), tpt(-14, -tw_bot + 4)], pants)
    pen.blob(body, top_col)
    # cel shade: back third of the torso
    pen.blob([tpt(hem + 2, -tw_bot + 3), tpt(hem + 2, -tw_bot * 0.25), tpt(torso_len * 0.6, -tw_top * 0.25),
              tpt(torso_len, -tw_top * 0.3), tpt(torso_len, -tw_top + 8), tpt(torso_len * 0.6, -tw_top - 1)],
             shade(top_col, 0.86), ow=0)
    _top_details(pen, look, tpt, torso_len, tw_top, tw_bot)
    # head
    _draw_head(pen, look, head_c, head_r, eyes, brows, mouth, talk, blink, look_dir, pose.get("head_tilt", 0) + lean * 0.3)
    # front arm last
    hand = arm("f")
    for fn in extra_props:
        fn(pen, hand)
    return {"hand": hand, "head": head_c}


def _top_details(pen, look, tpt, L, tw_top, tw_bot):
    style, col = look.top
    ex = look.extras
    if style == "hoodie":
        pen.curve([tpt(L - 6, -tw_top + 10), tpt(L - 22, 0), tpt(L - 6, tw_top - 10)], shade(col, 0.7), 4)
        pen.line([tpt(L - 22, -6), tpt(L - 52, -8)], shade(col, 0.6), 3)
        pen.line([tpt(L - 22, 6), tpt(L - 52, 8)], shade(col, 0.6), 3)
    if style in ("jacket", "coat", "uniform"):
        pen.line([tpt(L + 6, 0), tpt(-8, 0)], shade(col, 0.6), 3)
        pen.poly([tpt(L + 6, -18), tpt(L - 30, 0), tpt(L + 6, 18)], tint(col, 0.35), ow=3)
    if style == "polo":
        pen.poly([tpt(L + 6, -16), tpt(L - 12, 0), tpt(L + 6, 16)], tint(col, 0.5), ow=3)
    if "lab_coat" in ex:
        pen.blob([tpt(-44, -tw_bot - 6), tpt(L + 6, -tw_top), tpt(L + 10, -12), tpt(-44, -14)], "#f6f7fb")
        pen.blob([tpt(-44, tw_bot + 6), tpt(L + 6, tw_top), tpt(L + 10, 12), tpt(-44, 14)], "#ffffff")
    if "vest" in ex:
        pen.blob([tpt(-6, -tw_bot), tpt(L, -tw_top + 4), tpt(L - 6, -10), tpt(-6, -10)], "#e8762b")
        pen.blob([tpt(-6, tw_bot), tpt(L, tw_top - 4), tpt(L - 6, 10), tpt(-6, 10)], "#f08a3c")
        pen.line([tpt(30, -tw_bot + 2), tpt(30, tw_bot - 2)], "#f4f1d0", 5, caps=False)
    if "badge" in ex:
        p = tpt(L - 34, 22)
        pen.poly(star_pts(p[0], p[1], 12, 6, 5), "#f5c842", ow=2.5)
    if "lanyard" in ex:
        pen.line([tpt(L + 4, -14), tpt(L - 50, 0), tpt(L + 4, 14)], "#d33b3b", 3)
        p = tpt(L - 56, 0)
        pen.rrect(p[0] - 11, p[1] - 4, 22, 28, 3, "#ffffff", ow=2.5)
    if "apron" in ex:
        pen.blob([tpt(-30, -tw_bot * 0.55), tpt(L * 0.55, -tw_top * 0.5), tpt(L * 0.55, tw_top * 0.5), tpt(-30, tw_bot * 0.55)], "#c9a46a")
        pen.line([tpt(L * 0.55, -tw_top * 0.5), tpt(L + 8, -10)], "#8a6a44", 3)
        pen.line([tpt(L * 0.55, tw_top * 0.5), tpt(L + 8, 10)], "#8a6a44", 3)
    if "foil" in ex:
        pen.blob([tpt(-40, -tw_bot - 14), tpt(L + 6, -tw_top - 12), tpt(L + 12, tw_top + 10), tpt(-40, tw_bot + 14)], "#d8dde6")
        for i in range(4):
            pen.line([tpt(i * 30, -tw_bot), tpt(i * 30 + 20, tw_bot)], (255, 255, 255, 200), 4)
    if "stripes" in ex:
        for i in range(4):
            pen.line([tpt(i * 28 + 6, -tw_bot + 4), tpt(i * 28 + 6, tw_bot - 4)], tint(col, 0.5), 5, caps=False)
    if "logo" in ex:
        p = tpt(L * 0.55, 8)
        pen.circle(p[0], p[1], 11, "#ffffff", ow=2.5)


def star_pts(cx, cy, r1, r2, n=5, rot=-90):
    pts = []
    for i in range(n * 2):
        r = r1 if i % 2 == 0 else r2
        a = math.radians(rot + i * 180 / n)
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return pts


def _draw_head(pen, look, c, r, eyes, brows, mouth, talk, blink, look_dir, tilt):
    hx, hy = c
    hair_style, hair_col = look.hair
    ex = look.extras
    pen.push(hx, hy, rot=tilt)
    # back hair
    if hair_style in ("long", "ponytail", "bob", "bun"):
        if hair_style == "long":
            pen.blob([(-r * 0.95, -r * 0.3), (-r * 1.05, r * 0.9), (-r * 0.2, r * 1.15), (r * 0.5, r * 0.6),
                      (0, -r * 1.0)], shade(hair_col, 0.85))
        if hair_style == "bob":
            pen.blob([(-r * 1.08, -r * 0.2), (-r * 1.0, r * 0.75), (-r * 0.1, r * 0.85), (r * 0.6, r * 0.5),
                      (0, -r * 1.05)], shade(hair_col, 0.85))
        if hair_style == "ponytail":
            pen.blob([(-r * 0.85, -r * 0.35), (-r * 1.55, r * 0.1), (-r * 1.35, r * 0.95), (-r * 0.9, r * 0.35)],
                     hair_col)
        if hair_style == "bun":
            pen.circle(-r * 0.55, -r * 0.95, r * 0.42, hair_col)
    # ear (back side of the head, 3/4 view)
    pen.ellipse(-r * 0.86, r * 0.06, r * 0.2, r * 0.25, shade(look.skin, 0.9), ow=OUT * 0.9)
    # head
    pen.circle(0, 0, r, look.skin)
    pen.ellipse(-r * 0.36, r * 0.12, r * 0.62, r * 0.82, shade(look.skin, 0.93), ow=0, a0=90, a1=270)
    pen.circle(0, 0, r, None)
    pen.ellipse(-r * 0.5, r * 0.08, r * 0.13, r * 0.18, shade(look.skin, 0.88), ow=OUT * 0.8)
    pen.curve([(-r * 0.5, r * 0.0), (-r * 0.56, r * 0.1), (-r * 0.48, r * 0.16)], shade(look.skin, 0.7), 3)
    # cheeks
    pen.ellipse(r * 0.62, r * 0.36, r * 0.15, r * 0.09, mix(look.skin, "#ff7a7a", 0.35), ow=0)
    # face
    _face(pen, look, r, eyes, brows, mouth, talk, blink, look_dir)
    # front hair / hats
    _hair_front(pen, look, r, hair_style, hair_col)
    if "cap_red" in ex:
        _cap(pen, r, "#e0201b")
    if "ranger_hat" in ex:
        pen.ellipse(0, -r * 0.62, r * 1.45, r * 0.26, "#a6834e")
        pen.blob([(-r * 0.7, -r * 0.62), (-r * 0.5, -r * 1.3), (0, -r * 1.42), (r * 0.5, -r * 1.3), (r * 0.7, -r * 0.62)],
                 "#c49a5c")
        pen.line([(-r * 0.68, -r * 0.72), (r * 0.68, -r * 0.72)], "#5b3f22", 7, caps=False)
    if "officer_cap" in ex:
        pen.blob([(-r * 0.85, -r * 0.55), (-r * 0.95, -r * 1.05), (0, -r * 1.22), (r * 0.95, -r * 1.05), (r * 0.85, -r * 0.55)],
                 "#2b3b5c")
        pen.ellipse(r * 0.55, -r * 0.52, r * 0.55, r * 0.12, "#1b2438")
        pen.poly(star_pts(r * 0.2, -r * 0.82, 10, 5), "#f5c842", ow=2)
    if "headband" in ex:
        pen.line([(-r * 0.98, -r * 0.42), (r * 0.98, -r * 0.42)], "#ff4f8b", 12, caps=False)
    if "glasses" in ex:
        for gx in (r * 0.28, r * 0.72):
            pen.circle(gx, -r * 0.08, r * 0.2, (255, 255, 255, 60), ow=4)
        pen.line([(r * 0.48, -r * 0.1), (r * 0.52, -r * 0.1)], INK, 4)
        pen.line([(r * 0.08, -r * 0.1), (-r * 0.2, -r * 0.16)], INK, 4)
    if "sunglasses" in ex:
        pen.rrect(r * 0.06, -r * 0.26, r * 0.42, r * 0.28, 6, "#1d1a26", ow=3)
        pen.rrect(r * 0.54, -r * 0.26, r * 0.42, r * 0.28, 6, "#1d1a26", ow=3)
        pen.line([(r * 0.46, -r * 0.16), (r * 0.56, -r * 0.16)], INK, 4)
        pen.line([(r * 0.3, -r * 0.2), (r * 0.36, -r * 0.24)], (255, 255, 255, 200), 4)
    if "headlamp" in ex:
        pen.line([(-r * 0.98, -r * 0.5), (r * 0.98, -r * 0.5)], "#2a2a33", 9, caps=False)
        pen.rrect(r * 0.62, -r * 0.68, r * 0.34, r * 0.3, 5, "#f5c842", ow=3)
        pen.poly([(r * 0.95, -r * 0.6), (r * 5.5, -r * 1.6), (r * 5.5, r * 0.6), (r * 0.95, -r * 0.42)], (255, 245, 170, 70), ow=0)
    if "headset" in ex:
        pen.ellipse(-r * 0.12, r * 0.08, r * 0.22, r * 0.26, "#2a2a33")
        pen.curve([(-r * 0.12, r * 0.08), (r * 0.25, r * 0.55), (r * 0.62, r * 0.52)], "#2a2a33", 5)
    pen.pop()


def _cap(pen, r, col):
    pen.blob([(-r * 0.98, -r * 0.3), (-r * 0.9, -r * 0.82), (-r * 0.35, -r * 1.1), (r * 0.35, -r * 1.08),
              (r * 0.88, -r * 0.78), (r * 1.0, -r * 0.32)], col)
    pen.blob([(-r * 0.92, -r * 0.42), (-r * 0.82, -r * 0.85), (-r * 0.35, -r * 1.06), (-r * 0.25, -r * 0.6),
              (-r * 0.6, -r * 0.36)], shade(col, 0.82), ow=0)
    pen.blob([(r * 0.62, -r * 0.42), (r * 1.62, -r * 0.4), (r * 1.68, -r * 0.24), (r * 0.7, -r * 0.2)], shade(col, 0.9))
    pen.circle(-r * 0.08, -r * 1.08, r * 0.09, shade(col, 0.8), ow=2.5)
    pen.line([(-r * 0.08, -r * 1.02), (r * 0.12, -r * 0.34)], shade(col, 0.72), 3, caps=False)


def _hair_front(pen, look, r, style, col):
    if style in ("none", "bald"):
        return
    if style == "short":
        pen.blob([(-r * 0.98, -r * 0.1), (-r * 0.95, -r * 0.75), (-r * 0.2, -r * 1.12), (r * 0.6, -r * 0.98),
                  (r * 0.98, -r * 0.45), (r * 0.6, -r * 0.62), (r * 0.15, -r * 0.55), (-r * 0.45, -r * 0.5),
                  (-r * 0.7, -r * 0.15)], col)
    elif style == "spiky":
        pts = [(-r * 0.98, -r * 0.05), (-r * 1.1, -r * 0.7), (-r * 0.75, -r * 0.8), (-r * 0.7, -r * 1.3),
               (-r * 0.25, -r * 1.0), (0, -r * 1.45), (r * 0.25, -r * 1.02), (r * 0.65, -r * 1.3), (r * 0.7, -r * 0.85),
               (r * 1.12, -r * 0.8), (r * 0.95, -r * 0.4), (r * 0.5, -r * 0.6), (-r * 0.3, -r * 0.55), (-r * 0.7, -r * 0.1)]
        pen.poly(pts, col)
    elif style in ("long", "bob", "ponytail", "bun"):
        pen.blob([(-r * 1.0, r * 0.1), (-r * 0.98, -r * 0.7), (-r * 0.3, -r * 1.1), (r * 0.55, -r * 1.0),
                  (r * 1.02, -r * 0.45), (r * 0.7, -r * 0.55), (r * 0.25, -r * 0.7), (-r * 0.35, -r * 0.5),
                  (-r * 0.7, 0)], col)
    elif style == "curly":
        for i in range(9):
            a = math.radians(200 + i * 18)
            pen.circle(r * 0.92 * math.cos(a), r * 0.92 * math.sin(a) - r * 0.08, r * 0.3, col, ow=OUT * 0.8)
    elif style == "buzz":
        pen.ellipse(0, -r * 0.05, r * 1.0, r * 1.0, col, ow=0, a0=190, a1=350)
        pen.circle(0, 0, r, None)
    elif style == "quiff":
        pen.blob([(-r * 0.98, -r * 0.1), (-r * 0.9, -r * 0.8), (-r * 0.1, -r * 1.15), (r * 0.7, -r * 1.35),
                  (r * 1.15, -r * 1.05), (r * 0.9, -r * 0.55), (r * 0.3, -r * 0.62), (-r * 0.55, -r * 0.45),
                  (-r * 0.72, -r * 0.12)], col)


def _face(pen, look, r, eyes, brows, mouth, talk, blink, look_dir):
    ey = -r * 0.08
    ex1, ex2 = r * 0.3, r * 0.72
    erx, ery = r * 0.15, r * 0.2
    if eyes == "wide":
        erx, ery = r * 0.18, r * 0.24
    pup_dx = r * 0.035 * look_dir
    for i, exx in enumerate((ex1, ex2)):
        sx = 0.9 if i == 0 else 1.0
        if blink or eyes == "closed":
            pen.curve([(exx - erx * sx, ey), (exx, ey + ery * 0.3), (exx + erx * sx, ey)], INK, 4.5)
            continue
        if eyes == "happy":
            pen.curve([(exx - erx * sx, ey + ery * 0.2), (exx, ey - ery * 0.6), (exx + erx * sx, ey + ery * 0.2)], INK, 5)
            continue
        pen.ellipse(exx, ey, erx * sx, ery, "#ffffff", ow=OUT * 0.85)
        pr = erx * (0.55 if eyes != "wide" else 0.42)
        pen.ellipse(exx + pup_dx + erx * 0.12, ey + ery * 0.1, pr * sx, pr * 1.25, look.eye_col, ow=0)
        pen.circle(exx + pup_dx + erx * 0.25, ey - ery * 0.25, pr * 0.32, "#ffffff", ow=0)
        if eyes == "half":
            pen.poly([(exx - erx * sx - 2, ey - ery - 4), (exx + erx * sx + 2, ey - ery - 4),
                      (exx + erx * sx + 2, ey - ery * 0.05), (exx - erx * sx - 2, ey - ery * 0.05)], look.skin, ow=0)
            pen.line([(exx - erx * sx, ey - ery * 0.05), (exx + erx * sx, ey - ery * 0.05)], INK, 4.5)
        if eyes == "angry":
            pass
    by = ey - ery - r * 0.12
    bw = r * 0.17
    for i, exx in enumerate((ex1, ex2)):
        inner = exx + (bw if i == 0 else -bw)
        outer = exx - (bw if i == 0 else -bw)
        if brows == "flat":
            pts = [(outer, by), (inner, by)]
        elif brows == "up":
            pts = [(outer, by + 2), (exx, by - 8), (inner, by - 2)]
        elif brows == "angry":
            pts = [(outer, by - 6), (inner, by + 9)]
        elif brows == "worry":
            pts = [(outer, by + 4), (inner, by - 9)]
        elif brows == "smug":
            pts = [(outer, by - (8 if i == 1 else 0)), (inner, by - (2 if i == 1 else -4))]
        elif brows == "confused":
            pts = [(outer, by + (8 if i == 0 else -6)), (inner, by + (4 if i == 0 else -10))]
        else:
            pts = [(outer, by), (inner, by)]
        pen.line(pts, INK, 5.5)
    # mouth
    mx, my = r * 0.52, r * 0.42
    mw = r * 0.26
    if talk > 0.12 and mouth not in ("o",):
        h = r * (0.08 + 0.2 * talk)
        pen.blob([(mx - mw, my - 2), (mx + mw, my - 2), (mx + mw * 0.5, my + h), (mx - mw * 0.5, my + h)], "#5a1f2c", ow=OUT * 0.85)
        pen.ellipse(mx, my + h * 0.7, mw * 0.45, h * 0.3, "#e0687a", ow=0)
        return
    if mouth == "smile":
        pen.curve([(mx - mw, my - 4), (mx, my + 8), (mx + mw, my - 6)], INK, 5)
    elif mouth == "grin":
        pen.blob([(mx - mw * 1.1, my - 8), (mx + mw * 1.1, my - 10), (mx + mw * 0.6, my + 16), (mx - mw * 0.6, my + 14)],
                 "#5a1f2c", ow=OUT * 0.85)
        pen.poly([(mx - mw * 0.9, my - 7), (mx + mw * 0.9, my - 9), (mx + mw * 0.8, my - 1), (mx - mw * 0.8, my + 1)],
                 "#ffffff", ow=0)
    elif mouth == "o":
        h = r * (0.16 + 0.1 * talk)
        pen.ellipse(mx, my + 4, mw * 0.5, h, "#5a1f2c", ow=OUT * 0.85)
    elif mouth == "frown":
        pen.curve([(mx - mw, my + 8), (mx, my - 2), (mx + mw, my + 8)], INK, 5)
    elif mouth == "flat":
        pen.line([(mx - mw * 0.8, my + 2), (mx + mw * 0.8, my + 2)], INK, 5)
    elif mouth == "smirk":
        pen.curve([(mx - mw * 0.8, my + 4), (mx + mw * 0.3, my + 4), (mx + mw, my - 8)], INK, 5)
    elif mouth == "wobble":
        pen.curve([(mx - mw, my + 4), (mx - mw * 0.5, my), (mx, my + 4), (mx + mw * 0.5, my), (mx + mw, my + 4)], INK, 4.5)
    elif mouth == "grit":
        pen.rrect(mx - mw, my - 6, mw * 2, 18, 5, "#ffffff", ow=OUT * 0.85)
        pen.line([(mx - mw, my + 3), (mx + mw, my + 3)], INK, 2.5)


# ------------------------------------------------------------------ cast

CAST_LOOKS: dict[str, Look] = {
    # Doug: the one fixed design. Red cap is his signature; yellow tee and blue jeans.
    "doug": Look(skin="#f5d2b0", hair=("short", "#5a3a22"), top=("tee", "#f6b73c"), bottom="#3f5d93",
                 shoes="#f2f2ee", extras=("cap_red",), head_r=66),
}


def character_sprite(look: Look, pose: dict, scale: float, flip=False, **face):
    return sprite(lambda p: draw_character(p, look, pose, **face), CHAR_BBOX, scale, flip)
