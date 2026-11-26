"""Props for the toon engine: the megalodon rig and episode objects. Local units, facing right, drawn through a Pen."""
from __future__ import annotations

import math

from .toon import INK, OUT, Pen, catmull, ellipse_pts, mix, rgba, shade, star_pts, tint

SHARK_TOP = "#5f7f9c"
SHARK_BELLY = "#eef3f6"

# body profile for a 400-unit megalodon (nose +200, tail root -175)
_TOP = [(200, 8), (192, -14), (165, -40), (110, -62), (30, -68), (-50, -54), (-120, -30), (-172, -10)]
_BOT = [(-172, 9), (-120, 22), (-50, 44), (30, 58), (110, 54), (165, 38), (192, 24)]


def _bend(p, phase, amp, L=400.0):
    x, y = p
    k = max(0.0, (120 - x) / (L * 0.8))   # head stays still, tail swings
    return (x, y + amp * k * k * math.sin(phase - (120 - x) / 90.0) * 60)


def draw_megalodon(pen: Pen, t=0.0, swim=1.0, jaw=0.0, mood="calm", pup=0.0, col=SHARK_TOP, bite_flash=0.0):
    """t seconds (tail sway), swim 0..1 sway strength, jaw 0..1 open, pup 0..1 (bigger eye, rounder head),
    mood: calm, happy, hungry, curious, sleepy, guilty."""
    ph = t * (5.5 + 2 * swim)
    amp = 0.18 * swim + 0.05
    B = lambda pts: [_bend(p, ph, amp) for p in pts]
    dark = shade(col, 0.8)
    # far pectoral fin
    pen.poly(B([(70, 40), (40, 46), (6, 96), (30, 92)]), dark, ow=OUT * 0.9)
    # caudal fin (lunate, megalodon-like near-equal lobes)
    tail = [(-168, -6), (-215, -60), (-262, -100), (-240, -40), (-212, 0), (-238, 48), (-258, 92), (-210, 52), (-168, 8)]
    pen.blob(B(tail), col)
    # body
    body = catmull(_TOP, 8, closed=False) + catmull(_BOT, 8, closed=False)
    if pup > 0:
        body = [(x, y * (1 + 0.12 * pup * max(0, (x - 40) / 160))) for x, y in body]
    body_b = B(body)
    pen.poly(body_b, col)
    # belly (countershading) and a lighter sheen on the back
    belly = catmull([(197, 14), (165, 12), (110, 14), (30, 20), (-50, 16), (-120, 8), (-168, 4)], 8, closed=False)
    belly += [(-120, 20), (-50, 42), (30, 56), (110, 52), (165, 36), (192, 24)]
    pen.poly(B(belly), SHARK_BELLY, ow=0)
    pen.poly(B([(150, -40), (90, -56), (20, -60), (-60, -44), (-40, -36), (30, -48), (100, -46)]), tint(col, 0.18), ow=0)
    pen.poly(body_b, None)
    # dorsal fins
    pen.blob(B([(-20, -58), (-6, -110), (8, -146), (28, -118), (64, -66)]), col)
    pen.poly(B([(-118, -28), (-122, -48), (-104, -30)]), col, ow=OUT * 0.8)
    pen.poly(B([(-110, 22), (-128, 44), (-100, 26)]), col, ow=OUT * 0.8)
    # gills
    for i in range(5):
        gx = 92 - i * 11
        pen.curve(B([(gx, -24 + i), (gx - 6, 2), (gx, 28 - i)]), shade(col, 0.62), 3.2, n=6)
    # mouth and jaw
    hinge = (118, 34)
    if jaw > 0.02:
        a = math.radians(-36 * jaw)
        def rot(p):
            x, y = p[0] - hinge[0], p[1] - hinge[1]
            return (hinge[0] + x * math.cos(a) - y * math.sin(a), hinge[1] + x * math.sin(a) + y * math.cos(a))
        upper = [(hinge[0], hinge[1]), (150, 26), (182, 20), (196, 14)]
        lower = [rot(p) for p in [(196, 16), (180, 34), (150, 42), (hinge[0], hinge[1])]]
        mouth = B(upper + lower)
        pen.poly(mouth, "#4a1826", ow=OUT * 0.9)
        # teeth: triangles along both jaws
        for i in range(6):
            f = 0.12 + i * 0.14
            ux = hinge[0] + (194 - hinge[0]) * f
            uy = hinge[1] + (14 - hinge[1]) * f
            pen.poly(B([(ux - 5, uy - 1), (ux + 5, uy - 1), (ux, uy + 11)]), "#ffffff", ow=1.8)
            lx, ly = rot((ux, uy + 8 + 10 * f))
            pen.poly(B([(lx - 5, ly + 1), (lx + 5, ly + 1), (lx, ly - 10)]), "#ffffff", ow=1.8)
        pen.poly(B([(194, 18)] + [rot(p) for p in [(196, 16), (180, 36), (150, 46), (120, 40)]] + [(150, 40), (182, 26)]),
                 SHARK_BELLY, ow=OUT * 0.9)
    else:
        smile = mood in ("happy", "guilty")
        pts = [(190, 22), (160, 30), (128, 30)] if not smile else [(192, 20), (162, 34), (126, 26)]
        pen.curve(B(pts), INK, 4, n=6)
        if mood == "guilty":
            pen.poly(B([(170, 30), (176, 30), (173, 38)]), "#ffffff", ow=1.6)
    # snout pores (electric sense), always drawn
    for i, (px, py) in enumerate(((182, 2), (172, -6), (176, 8), (164, 2), (160, 12), (168, -14))):
        bx, by = _bend((px, py), ph, amp)
        pen.circle(bx, by, 2.6, shade(col, 0.55), ow=0)
    # eye
    er = 8 + 7 * pup
    ex, ey = 150, -16 + 2 * pup
    exb, eyb = _bend((ex, ey), ph, amp)
    if mood in ("happy",):
        pen.curve([(exb - er, eyb + 2), (exb, eyb - er * 0.7), (exb + er, eyb + 2)], INK, 4.5, n=6)
    elif mood == "sleepy":
        pen.curve([(exb - er, eyb), (exb, eyb + er * 0.4), (exb + er, eyb)], INK, 4.5, n=6)
    else:
        pen.circle(exb, eyb, er, "#14101a", ow=OUT * 0.6)
        pen.circle(exb + er * 0.3, eyb - er * 0.35, er * 0.33, "#ffffff", ow=0)
        if pup > 0.3:
            pen.circle(exb - er * 0.3, eyb + er * 0.35, er * 0.15, "#ffffff", ow=0)
        if mood == "hungry":
            pen.line([(exb - er * 1.3, eyb - er * 1.5), (exb + er * 1.1, eyb - er * 0.9)], INK, 5)
        if mood == "curious":
            pen.curve([(exb - er * 1.2, eyb - er * 1.4), (exb, eyb - er * 1.9), (exb + er * 1.2, eyb - er * 1.5)], INK, 4.5, n=6)
    # near pectoral fin
    pen.blob(B([(96, 40), (60, 50), (28, 112), (44, 116), (100, 56)]), col)
    pen.curve(B([(90, 46), (56, 58), (40, 104)]), shade(col, 0.7), 2.5, n=6)


MEG_BBOX = (-275, -160, 215, 125)


# ------------------------------------------------------------------ simple props (local units ~ 1 unit = 1 px at scale 1)

def fish(pen, col="#7fc8e8", size=1.0, t=0.0):
    pen.push(0, 0, scale=size)
    sway = math.sin(t * 9) * 6
    pen.poly([(-30, 0), (-52, -16 + sway), (-50, 16 + sway)], shade(col, 0.85), ow=3)
    pen.ellipse(0, 0, 34, 16, col, ow=3)
    pen.circle(18, -4, 3.5, INK, ow=0)
    pen.curve([(-4, -12), (2, 0), (-4, 12)], shade(col, 0.7), 2.5, n=4)
    pen.pop()


def bucket(pen, col="#c84c3c", full="fish"):
    pen.poly([(-60, -70), (60, -70), (48, 40), (-48, 40)], col)
    pen.poly([(-60, -70), (60, -70), (58, -54), (-58, -54)], shade(col, 0.8), ow=3)
    pen.curve([(-58, -66), (0, -128), (58, -66)], INK, 4)
    if full == "fish":
        for i, (fx, fy, r) in enumerate(((-30, -78, -20), (8, -86, 15), (34, -74, 35))):
            pen.push(fx, fy, rot=r)
            fish(pen, "#9fb7c8", 0.7)
            pen.pop()


def bathtub(pen, water=True, foam=True):
    pen.rrect(-260, -110, 520, 150, 40, "#f4f6fa")
    pen.poly([(-230, 40), (-200, 40), (-205, 80), (-235, 80)], "#d9b45a", ow=3)
    pen.poly([(200, 40), (230, 40), (235, 80), (205, 80)], "#d9b45a", ow=3)
    if water:
        pen.poly([(-235, -88), (235, -88), (235, -70), (-235, -70)], "#7ad0f0", ow=0)
    pen.rrect(-260, -110, 520, 150, 40, None)
    pen.line([(-240, -100), (240, -100)], shade("#f4f6fa", 0.85), 6, caps=False)
    pen.line([(-210, -30), (210, -30)], (255, 255, 255, 140), 8)


def kiddie_pool(pen, col="#4aa3e0"):
    pen.ellipse(0, 0, 300, 70, col)
    pen.ellipse(0, -10, 270, 52, "#8fe0ff", ow=3)
    for i in range(7):
        a = 200 + i * 22
        x = 285 * math.cos(math.radians(a))
        pen.circle(x, 10 + 40 * math.sin(math.radians(a)), 12, "#ffffff", ow=2.5)


def phone(pen, screen="#7ad0f0", w=46, h=86):
    pen.rrect(-w / 2, -h / 2, w, h, 9, "#1e1d26")
    pen.rrect(-w / 2 + 5, -h / 2 + 8, w - 10, h - 18, 4, screen, ow=0)


def tooth(pen, col="#ece3cf", size=1.0):
    pen.push(0, 0, scale=size)
    pen.blob([(-60, 40), (-48, -20), (-16, -82), (0, -96), (16, -82), (48, -20), (60, 40), (30, 30), (0, 46), (-30, 30)], col)
    pen.poly([(-62, 40), (62, 40), (52, 80), (-52, 80)], "#5d4b3a", ow=OUT)
    for i in range(6):
        pen.line([(-40 + i * 4, 10 - i * 18), (-36 + i * 4, 6 - i * 18)], shade(col, 0.75), 2)
    pen.pop()


def boat(pen, col="#ffffff", trim="#d33b3b", name=""):
    pen.blob([(-260, -20), (260, -30), (220, 60), (-230, 60)], col)
    pen.poly([(-255, -6), (255, -16), (248, 4), (-250, 12)], trim, ow=3)
    pen.rrect(-150, -130, 180, 110, 16, "#f2f2f2")
    for i in range(3):
        pen.rrect(-135 + i * 55, -112, 40, 34, 6, "#8fd3ff", ow=3)
    pen.line([(60, -30), (60, -190)], INK, 6)
    if name:
        pen.text(120, 30, name, 26, "#1e3a5a", "RussoOne-Regular")


def whale(pen, col="#4f5f7a"):
    pen.blob([(320, 0), (280, -70), (120, -110), (-120, -90), (-300, -30), (-380, -10), (-300, 20), (-100, 60),
              (120, 80), (280, 50)], col)
    pen.blob([(310, 10), (260, 50), (100, 72), (-80, 52), (60, 40), (220, 30)], tint(col, 0.45), ow=0)
    pen.blob([(-370, -10), (-450, -90), (-420, -10), (-460, 60)], col)
    pen.circle(230, 0, 8, INK, ow=0)
    pen.curve([(320, 6), (260, 26), (200, 24)], INK, 4)


def truck(pen, col="#e8e8ea", tank=True):
    pen.rrect(-300, -150, 380, 170, 18, "#dfe6ee")
    if tank:
        pen.rrect(-290, -140, 360, 150, 16, "#7ad0f0", ow=3)
        pen.text(-110, -60, "LIVE SEAFOOD?", 30, "#1e3a5a", "RussoOne-Regular")
    pen.rrect(90, -110, 150, 130, 20, col)
    pen.rrect(150, -96, 70, 50, 8, "#8fd3ff", ow=3)
    for wx in (-200, 150):
        pen.circle(wx, 28, 38, "#2a2a33")
        pen.circle(wx, 28, 15, "#9a9aa6", ow=3)


def tank(pen, w=700, h=380, water="#5cc4ec"):
    pen.rrect(-w / 2 - 14, -h - 14, w + 28, h + 28, 10, "#3c4a5a")
    pen.poly([(-w / 2, -h), (w / 2, -h), (w / 2, 0), (-w / 2, 0)], water, ow=0)
    pen.poly([(-w / 2 + 20, -h + 10), (-w / 2 + 70, -h + 10), (-w / 2 + 30, -20), (-w / 2 + 10, -20)], (255, 255, 255, 70), ow=0)


def tape_measure(pen, length_px=600, label=""):
    pen.rrect(0, -18, length_px, 36, 6, "#f5c842")
    for i in range(0, int(length_px), 20):
        pen.line([(i, -18), (i, -18 + (16 if i % 100 == 0 else 8))], INK, 2, caps=False)
    if label:
        pen.text(length_px / 2, 0, label, 24, INK, "RussoOne-Regular")


def sign(pen, text, w=360, h=140, col="#ffe27a", post=True, size=40):
    if post:
        pen.limb([(0, h / 2), (0, h / 2 + 160)], 16, "#8a6a44")
    pen.rrect(-w / 2, -h / 2, w, h, 12, col)
    pen.text(0, 0, text, size, INK, "RussoOne-Regular")


PROP_DRAW = {
    "fish": (fish, (-60, -30, 45, 30)),
    "bucket": (bucket, (-70, -140, 70, 50)),
    "bathtub": (bathtub, (-270, -120, 270, 90)),
    "kiddie_pool": (kiddie_pool, (-320, -90, 320, 90)),
    "phone": (phone, (-30, -50, 30, 50)),
    "tooth": (tooth, (-70, -105, 70, 90)),
    "boat": (boat, (-270, -200, 270, 70)),
    "whale": (whale, (-470, -120, 330, 90)),
    "truck": (truck, (-310, -160, 250, 70)),
}
