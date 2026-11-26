"""Backgrounds for the toon engine. Each set is drawn once in a 1920x1080 world at 2x (3840x2160), antialiased, and
cached as PNG; the camera crops it per frame. animate_layer / foreground_layer add the cheap moving parts
(water shimmer, light shafts, bubbles, underwater tint)."""
from __future__ import annotations

import math
import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

from .toon import INK, OUT, Pen, catmull, ellipse_pts, mix, rgba, rrect_pts, shade, star_pts, tint

ROOT = Path(__file__).resolve().parent.parent
W, H = 1920, 1080
CACHE = ROOT / ".cache" / "toon_sets"
BW, BH = 3840, 2160
K = 2  # world -> background pixels

# ------------------------------------------------------------------ helpers


def grad(img, y0, y1, c0, c1, x0=0, x1=None):
    """Vertical gradient between world y0 and y1 (world is 1080 tall)."""
    d = ImageDraw.Draw(img)
    k = img.height / 1080
    y0, y1 = y0 * k, y1 * k
    x1 = img.width if x1 is None else x1
    a, b = rgba(c0), rgba(c1)
    for y in range(int(y0), int(y1)):
        t = (y - y0) / max(1, (y1 - y0))
        d.line([(x0, y), (x1, y)], fill=tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(4)))


def _canvas():
    ss = 2
    img = Image.new("RGBA", (BW * ss, BH * ss), (255, 255, 255, 255))
    return img, Pen(img, 0, 0, K * ss), ss


def _done(img, ss):
    return img.reduce(ss).convert("RGB")


def window(p, x, y, w, h, view="day"):
    p.rrect(x - 14, y - 14, w + 28, h + 28, 10, "#f4efe6")
    sky = {"day": ("#8fd3ff", "#d8f1ff"), "night": ("#1c2550", "#3a3f7a"), "dusk": ("#ff9a6b", "#ffd49a")}[view]
    p.poly([(x, y), (x + w, y), (x + w, y + h), (x, y + h)], sky[0], ow=4)
    p.poly([(x, y + h * 0.55), (x + w, y + h * 0.55), (x + w, y + h), (x, y + h)], sky[1], ow=0)
    if view == "night":
        p.circle(x + w * 0.72, y + h * 0.3, 24, "#fff6c9", ow=0)
        for i in range(6):
            p.poly(star_pts(x + 30 + i * (w - 60) / 5, y + 30 + (i % 2) * 40, 7, 3), "#fff6c9", ow=0)
    else:
        p.ellipse(x + w * 0.3, y + h * 0.3, 50, 18, "#ffffff", ow=0)
    p.line([(x + w / 2, y), (x + w / 2, y + h)], "#f4efe6", 12, caps=False)
    p.line([(x, y + h / 2), (x + w, y + h / 2)], "#f4efe6", 12, caps=False)
    p.poly([(x, y), (x + w, y), (x + w, y + h), (x, y + h)], None, ow=5)


def plant(p, x, y, s=1.0):
    p.poly([(x - 40 * s, y - 70 * s), (x + 40 * s, y - 70 * s), (x + 30 * s, y), (x - 30 * s, y)], "#c8643c")
    for a in (-40, -15, 10, 35):
        tip = (x + math.sin(math.radians(a)) * 110 * s, y - 70 * s - math.cos(math.radians(a)) * 110 * s)
        p.blob([(x, y - 70 * s), (tip[0] - 18 * s, (tip[1] + y - 70 * s) / 2), tip, (tip[0] + 18 * s, (tip[1] + y - 70 * s) / 2)],
               "#3f9a5a")


def floor_boards(p, y0, col):
    p.poly([(0, y0), (1920, y0), (1920, 1080), (0, 1080)], col, ow=0)
    for i in range(1, 7):
        yy = y0 + (1080 - y0) * (i / 7) ** 1.4
        p.line([(0, yy), (1920, yy)], shade(col, 0.88), 3, caps=False)
    p.line([(0, y0), (1920, y0)], INK, 5, caps=False)


def wall(p, y1, col, stripe=None):
    p.poly([(0, 0), (1920, 0), (1920, y1), (0, y1)], col, ow=0)
    if stripe:
        for x in range(0, 1920, 120):
            p.poly([(x, 0), (x + 60, 0), (x + 60, y1), (x, y1)], stripe, ow=0)
    p.poly([(0, y1 - 26), (1920, y1 - 26), (1920, y1), (0, y1)], shade(col, 0.85), ow=3)


def house(p, x, y, w, h, col, roof="#b5473a", door="#7a4a2e"):
    p.poly([(x, y), (x + w, y), (x + w, y + h), (x, y + h)], col)
    p.poly([(x - 30, y), (x + w / 2, y - h * 0.55), (x + w + 30, y)], roof)
    p.rrect(x + w * 0.42, y + h * 0.45, w * 0.18, h * 0.55, 8, door)
    for wx in (x + w * 0.12, x + w * 0.7):
        p.rrect(wx, y + h * 0.25, w * 0.18, h * 0.22, 6, "#bfe8ff")


def tree(p, x, y, s=1.0, col="#4fae5c"):
    p.limb([(x, y), (x, y - 160 * s)], 30 * s, "#8a5a3a")
    p.blob([(x - 110 * s, y - 170 * s), (x - 90 * s, y - 280 * s), (x, y - 330 * s), (x + 100 * s, y - 280 * s),
            (x + 115 * s, y - 170 * s), (x, y - 130 * s)], col)


def cloud(p, x, y, s=1.0):
    p.blob([(x - 90 * s, y), (x - 60 * s, y - 40 * s), (x, y - 60 * s), (x + 60 * s, y - 45 * s), (x + 95 * s, y),
            (x, y + 18 * s)], "#ffffff", ow=OUT * 0.8)


def palm(p, x, y, s=1.0):
    pts = [(x, y), (x + 20 * s, y - 150 * s), (x + 50 * s, y - 300 * s)]
    p.curve(pts, "#8a5a3a", 34 * s)
    top = (x + 50 * s, y - 300 * s)
    for a in (-150, -110, -60, -20, 20):
        tip = (top[0] + math.cos(math.radians(a)) * 170 * s, top[1] + math.sin(math.radians(a)) * 90 * s + 60 * s)
        p.blob([top, ((top[0] + tip[0]) / 2, (top[1] + tip[1]) / 2 - 30 * s), tip, ((top[0] + tip[0]) / 2, (top[1] + tip[1]) / 2 + 10 * s)],
               "#3f9a5a")


def kelp(p, x, y, h, s=1.0, col="#2f8a5e"):
    pts = [(x + math.sin(i * 0.9) * 22 * s, y - i * h / 6) for i in range(7)]
    p.curve(pts, col, 16 * s)
    for i in range(1, 6):
        px, py = pts[i]
        p.ellipse(px + 18 * s * (1 if i % 2 else -1), py, 22 * s, 9 * s, tint(col, 0.15), ow=3, rot=30 if i % 2 else -30)


def rock(p, x, y, s=1.0, col="#7d7f8f"):
    p.blob([(x - 90 * s, y), (x - 70 * s, y - 60 * s), (x, y - 85 * s), (x + 80 * s, y - 50 * s), (x + 95 * s, y)], col)


# ------------------------------------------------------------------ set builders


def b_room(wall_col="#cfe3f2", floor_col="#c99a6b", view="day", kind="bedroom", stripe=None):
    img, p, ss = _canvas()
    wall(p, 760, wall_col, stripe)
    floor_boards(p, 760, floor_col)
    if kind == "bedroom":
        window(p, 1240, 190, 380, 300, view)
        p.rrect(140, 560, 560, 230, 30, "#7c8fd6")       # bed
        p.rrect(130, 470, 70, 330, 16, "#8a5a3a")
        p.rrect(150, 540, 170, 80, 30, "#ffffff")
        p.rrect(300, 620, 400, 170, 20, "#5f74c4")
        p.rrect(320, 220, 200, 260, 6, "#ffe27a")         # poster: a shark poster (own drawing)
        p.text(420, 260, "SHARKS", 40, INK, "RussoOne-Regular")
        p.ellipse(420, 360, 70, 30, "#5f7f9c", ow=4)
        p.poly([(350, 360), (325, 335), (325, 385)], "#5f7f9c", ow=4)
        p.rrect(1500, 600, 300, 160, 10, "#a8744a")       # desk
        p.rrect(1560, 520, 120, 80, 8, "#2a2a33")
        plant(p, 1800, 760, 0.9)
    elif kind == "living":
        window(p, 260, 180, 420, 320, view)
        p.rrect(900, 520, 720, 260, 50, "#d0604a")        # sofa
        p.rrect(900, 440, 720, 150, 50, "#b9503c")
        p.rrect(860, 520, 100, 240, 40, "#b9503c")
        p.rrect(1560, 520, 100, 240, 40, "#b9503c")
        p.rrect(160, 560, 330, 200, 12, "#6b4a32")        # tv stand
        p.rrect(190, 360, 270, 180, 10, "#1e1d26")
        plant(p, 1780, 760, 1.0)
        p.circle(1400, 160, 50, "#fff3c4", ow=4)
    elif kind == "bathroom":
        for x in range(0, 1920, 80):
            for y in range(0, 760, 80):
                p.poly([(x, y), (x + 80, y), (x + 80, y + 80), (x, y + 80)], "#d9f0f4" if (x // 80 + y // 80) % 2 else "#c4e6ec", ow=1.5, ink="#a9cfd8")
        p.poly([(0, 760), (1920, 760), (1920, 1080), (0, 1080)], "#9fb7c4", ow=0)
        p.line([(0, 760), (1920, 760)], INK, 5, caps=False)
        p.rrect(1450, 220, 260, 320, 30, "#e8f6fa")       # mirror
        p.rrect(1430, 560, 300, 200, 12, "#ffffff")       # sink
        window(p, 260, 160, 260, 220, view)
    elif kind == "kitchen":
        p.rrect(0, 520, 1920, 240, 0, "#e0d4c0")
        p.rrect(100, 420, 1720, 110, 6, "#f4efe6")
        p.rrect(1300, 160, 420, 260, 10, "#ffffff")
        window(p, 400, 140, 420, 250, view)
    return _done(img, ss)


def b_yard(pool=True, view="day", fence="#f4efe6"):
    img, p, ss = _canvas()
    sky = {"day": ("#7ccaf5", "#d6f0ff"), "dusk": ("#ff9361", "#ffd99c"), "night": ("#141a3c", "#2c3470")}[view]
    grad(img, 0, 700, sky[0], sky[1])
    p = Pen(img, 0, 0, K * 2)
    for cx, cy in ((300, 140), (1300, 110), (1700, 200)):
        cloud(p, cx, cy, 1.0)
    house(p, 1180, 300, 640, 380, "#f2e3c6")
    for x in range(-20, 1920, 70):
        p.rrect(x, 520, 54, 210, 10, fence, ow=3.5)
    p.line([(0, 600), (1920, 600)], shade(fence, 0.85), 18, caps=False)
    p.poly([(0, 700), (1920, 700), (1920, 1080), (0, 1080)], "#6cc46a", ow=0)
    p.line([(0, 700), (1920, 700)], INK, 5, caps=False)
    if pool:
        p.rrect(420, 820, 1080, 230, 40, "#e8e8ea", ow=5)
        p.rrect(450, 840, 1020, 190, 30, "#4fc0ec", ow=4)
        for i in range(6):
            p.line([(520 + i * 160, 900 + (i % 2) * 40), (590 + i * 160, 900 + (i % 2) * 40)], (255, 255, 255, 170), 6)
    tree(p, 180, 720, 1.2)
    return _done(img, ss)


def b_street(view="day"):
    img, p, ss = _canvas()
    sky = {"day": ("#7ccaf5", "#d6f0ff"), "dusk": ("#ff9361", "#ffd99c"), "night": ("#141a3c", "#2c3470")}[view]
    grad(img, 0, 760, sky[0], sky[1])
    p = Pen(img, 0, 0, K * 2)
    cloud(p, 400, 130)
    cloud(p, 1500, 170, 0.8)
    for i, (x, col, roof) in enumerate(((60, "#f2e3c6", "#b5473a"), (560, "#cfe6f2", "#4a6fa5"), (1080, "#f6d6d6", "#7a4a8a"),
                                        (1560, "#e6f2cf", "#b5473a"))):
        house(p, x, 330, 380, 330, col, roof)
    p.poly([(0, 660), (1920, 660), (1920, 760), (0, 760)], "#c9c9cf", ow=4)
    p.poly([(0, 760), (1920, 760), (1920, 1080), (0, 1080)], "#55565f", ow=0)
    for x in range(40, 1920, 260):
        p.rrect(x, 900, 140, 18, 6, "#f4f1d0", ow=0)
    p.line([(0, 760), (1920, 760)], INK, 5, caps=False)
    for x in (480, 1500):
        tree(p, x, 680, 0.9)
    return _done(img, ss)


def b_beach(view="day"):
    img, p, ss = _canvas()
    sky = {"day": ("#6cc6f7", "#e2f6ff"), "dusk": ("#ff8a5c", "#ffd89a"), "night": ("#141a3c", "#2c3470"),
           "dawn": ("#f7a3b8", "#ffe2a6")}[view]
    grad(img, 0, 500, sky[0], sky[1])
    grad(img, 500, 1080, "#2aa0d8" if view != "dawn" else "#5a8fc0", "#5fd0f0" if view != "dawn" else "#f2b9a0")
    p = Pen(img, 0, 0, K * 2)
    if view == "dawn":
        p.ellipse(1500, 500, 70, 40, "#ffe9a0", ow=0, a0=180, a1=360)
    else:
        p.circle(1600, 160, 70, "#fff2a8", ow=0)
    cloud(p, 300, 150)
    cloud(p, 900, 100, 0.7)
    p.line([(0, 500), (1920, 500)], shade("#2aa0d8", 0.8), 4, caps=False)
    p.blob([(-40, 760), (500, 690), (1100, 720), (1960, 680), (1960, 1100), (-40, 1100)], "#f3dc9a")
    p.blob([(-40, 760), (500, 690), (1100, 720), (1960, 680), (1960, 712), (1100, 752), (500, 722), (-40, 792)], "#ffffff", ow=0)
    palm(p, 1700, 760, 1.1)
    rock(p, 200, 780, 0.8)
    p.ellipse(860, 900, 120, 26, "#e9c77f", ow=0)
    return _done(img, ss)


def b_harbor(view="day"):
    img, p, ss = _canvas()
    sky = {"day": ("#7ccaf5", "#d6f0ff"), "dusk": ("#ff9361", "#ffd99c"), "night": ("#141a3c", "#2c3470")}[view]
    grad(img, 0, 640, sky[0], sky[1])
    grad(img, 640, 1080, "#2f8fc4", "#1d6a9a")
    p = Pen(img, 0, 0, K * 2)
    cloud(p, 500, 140)
    from .toon_held import boathouse
    for x, col, roof in ((180, "#c9d8e6", "#4a6fa5"), (560, "#f2e3c6", "#b5473a"), (1420, "#e6f2cf", "#3f7a5a"),
                         (1760, "#f6d6d6", "#7a4a8a")):
        p.push(x, 640, scale=0.9)
        boathouse(p, col, roof)
        p.pop()
    p.poly([(0, 640), (1920, 640), (1920, 760), (0, 760)], "#b88a5a", ow=4)
    for x in range(0, 1920, 90):
        p.line([(x, 640), (x, 760)], shade("#b88a5a", 0.8), 3, caps=False)
    for x in (200, 700, 1300, 1800):
        p.limb([(x, 640), (x, 1080)], 34, "#8a6a44")
    p.poly([(0, 760), (1920, 760), (1920, 1080), (0, 1080)], "#2f8fc4", ow=0)
    return _done(img, ss)


def b_ocean_surface(view="day", reef=False):
    img, p, ss = _canvas()
    sky = {"day": ("#6cc6f7", "#e2f6ff"), "dusk": ("#ff8a5c", "#ffd89a"), "night": ("#141a3c", "#2c3470"), "storm": ("#4a5468", "#8a93a6")}[view]
    grad(img, 0, 550, sky[0], sky[1])
    grad(img, 550, 1080, "#1f86c0", "#0f5a8a")
    p = Pen(img, 0, 0, K * 2)
    if view != "storm":
        cloud(p, 400, 150)
        cloud(p, 1400, 120, 0.8)
    else:
        for x in range(0, 1920, 300):
            cloud(p, x + 100, 120, 1.4)
    p.line([(0, 550), (1920, 550)], shade("#1f86c0", 0.85), 4, caps=False)
    if view == "night":
        p.circle(1500, 160, 50, "#fff6c9", ow=0)
        rr = random.Random(4)
        for i in range(40):
            p.circle(rr.uniform(0, 1920), rr.uniform(0, 500), rr.uniform(1.5, 3.5), "#fff6c9", ow=0)
        img2 = Image.new("RGBA", img.size, (4, 10, 30, 120))
        img.alpha_composite(img2)
        p = Pen(img, 0, 0, K * 2)
    if reef:
        p.blob([(-40, 640), (300, 600), (700, 630), (900, 610), (900, 650), (700, 670), (300, 650), (-40, 690)], "#5a6070")
        p.blob([(1250, 610), (1600, 590), (1960, 620), (1960, 670), (1600, 640), (1250, 650)], "#5a6070")
        for x in range(0, 900, 60):
            p.ellipse(x, 615 + (x % 120) / 6, 40, 10, "#ffffff", ow=0)
        for x in range(1260, 1960, 60):
            p.ellipse(x, 600 + (x % 120) / 6, 40, 10, "#ffffff", ow=0)
    return _done(img, ss)


def b_shop():
    img, p, ss = _canvas()
    wall(p, 760, "#cfe0d6", None)
    floor_boards(p, 760, "#9c8466")
    for i in range(7):
        x = 90 + i * 60
        p.line([(x, 120), (x + 40, 620)], "#5a3a22", 6)
        p.circle(x + 30, 500, 14, "#2a2a33", ow=3)
    p.rrect(700, 120, 560, 360, 6, "#f4ecd6")
    p.blob([(700, 120), (860, 120), (900, 220), (840, 330), (920, 480), (700, 480)], "#cfe6a8", ow=3)
    p.ellipse(880, 300, 50, 36, None, ow=6, ink="#e0201b")
    p.text(1100, 170, "TIDE TIMES", 34, INK, "RussoOne-Regular")
    for i in range(4):
        p.line([(1000, 230 + i * 50), (1220, 230 + i * 50)], "#9aa3b2", 4, caps=False)
    p.rrect(1400, 160, 380, 120, 10, "#e0201b")
    p.text(1590, 220, "BAIT & TACKLE", 42, "#ffffff", "RussoOne-Regular")
    for i in range(3):
        p.rrect(1420 + i * 120, 560, 100, 120, 10, "#f4f6fa")
    return _done(img, ss)


def b_lagoon(view="day"):
    img, p, ss = _canvas()
    grad(img, 0, 430, "#6cc6f7", "#e2f6ff")
    grad(img, 430, 1080, "#5cd6c0", "#2fb0a6")
    p = Pen(img, 0, 0, K * 2)
    cloud(p, 300, 120)
    cloud(p, 1200, 90, 0.8)
    p.blob([(-40, 440), (500, 415), (1100, 430), (1380, 420), (1380, 452), (1100, 462), (500, 450), (-40, 470)], "#c9b27a")
    p.blob([(1560, 420), (1960, 410), (1960, 450), (1560, 452)], "#c9b27a")
    for x in range(0, 1380, 50):
        p.ellipse(x, 418 + (x % 100) / 10, 30, 7, "#ffffff", ow=0)
    for x in range(1570, 1960, 50):
        p.ellipse(x, 412, 30, 7, "#ffffff", ow=0)
    for x, y, r in ((700, 700, 120), (1300, 900, 160), (400, 980, 140), (1650, 760, 110)):
        p.ellipse(x, y, r, r * 0.22, (210, 245, 225, 255), ow=0)
    p.poly([(0, 560), (330, 560), (560, 1080), (0, 1080)], "#c8c4bc", ow=5)
    for i in range(6):
        y = 600 + i * 80
        p.line([(0, y), (330 + (y - 560) * 0.44, y)], "#b0aca4", 3, caps=False)
    p.push(160, 560, scale=0.8)
    from .toon_held import sign_lagoon
    sign_lagoon(p)
    p.pop()
    return _done(img, ss)


def b_studio():
    img, p, ss = _canvas()
    grad(img, 0, 1080, "#22356a", "#16244a")
    p = Pen(img, 0, 0, K * 2)
    p.poly([(-40, 700), (1960, 380), (1960, 560), (-40, 880)], "#e0201b", ow=0)
    p.poly([(-40, 880), (1960, 560), (1960, 600), (-40, 920)], "#f6b73c", ow=0)
    for i in range(10):
        p.circle(150 + i * 190, 120 + (i % 3) * 30, 6, (255, 255, 255, 90), ow=0)
    return _done(img, ss)


def b_underwater(depth="shallow"):
    img, p, ss = _canvas()
    c0, c1 = {"shallow": ("#5fd0f0", "#1d7fb4"), "mid": ("#2a7db8", "#0f3f6e"), "deep": ("#0d2a4e", "#040a1a")}[depth]
    grad(img, 0, 1080, c0, c1)
    p = Pen(img, 0, 0, K * 2)
    if depth != "deep":
        p.blob([(-40, 900), (400, 860), (900, 900), (1400, 850), (1960, 890), (1960, 1100), (-40, 1100)], "#e8d39a" if depth == "shallow" else "#8a7f6a")
        rock(p, 260, 930, 1.3, "#6c7a8a")
        rock(p, 1600, 910, 1.0, "#6c7a8a")
        for x in (120, 380, 1480, 1760):
            kelp(p, x, 960, 520, 1.0)
    else:
        p.blob([(-40, 980), (700, 950), (1300, 990), (1960, 960), (1960, 1100), (-40, 1100)], "#1a2233")
    return _done(img, ss)


def b_lab(view="day"):
    img, p, ss = _canvas()
    wall(p, 740, "#e6eef4")
    p.poly([(0, 740), (1920, 740), (1920, 1080), (0, 1080)], "#b9c4cf", ow=0)
    p.line([(0, 740), (1920, 740)], INK, 5, caps=False)
    p.rrect(120, 160, 760, 520, 14, "#3c4a5a")
    p.poly([(140, 180), (860, 180), (860, 660), (140, 660)], "#5cc4ec", ow=0)
    for i in range(6):
        p.circle(200 + i * 110, 600 - (i % 3) * 120, 10, (255, 255, 255, 140), ow=2)
    p.rrect(1100, 520, 700, 220, 10, "#ffffff")
    p.rrect(1160, 300, 240, 170, 10, "#1e1d26")
    p.rrect(1460, 260, 280, 200, 8, "#ffffff")
    p.text(1600, 300, "SPECIES", 26, INK, "RussoOne-Regular")
    p.ellipse(1600, 380, 80, 32, "#5f7f9c", ow=4)
    return _done(img, ss)


def b_office(view="day"):
    img, p, ss = _canvas()
    wall(p, 760, "#e9e2d4", "#e2d9c8")
    floor_boards(p, 760, "#8f7a64")
    window(p, 1300, 170, 420, 320, view)
    p.rrect(380, 560, 900, 200, 12, "#7a5a3c")
    p.rrect(300, 160, 220, 300, 8, "#2b3b5c")
    p.text(410, 220, "FISHERIES", 30, "#ffffff", "RussoOne-Regular")
    p.circle(410, 340, 60, "#f5c842", ow=4)
    p.rrect(1500, 560, 180, 200, 8, "#9aa8b8")
    return _done(img, ss)


def b_news(view="day"):
    img, p, ss = _canvas()
    grad(img, 0, 1080, "#16244a", "#0b1430")
    p = Pen(img, 0, 0, K * 2)
    for i in range(12):
        p.line([(i * 180, 0), (i * 180 - 300, 1080)], (255, 255, 255, 18), 40, caps=False)
    p.rrect(240, 140, 1440, 520, 20, "#22356a", ow=6)
    p.rrect(270, 170, 1380, 460, 12, "#5cc4ec", ow=4)
    p.poly([(0, 760), (1920, 760), (1920, 1080), (0, 1080)], "#0e1a3a", ow=0)
    p.rrect(560, 700, 800, 240, 20, "#e0201b")
    p.text(960, 800, "DAILY TIDE NEWS", 54, "#ffffff", "RussoOne-Regular")
    return _done(img, ss)


def b_plain(col="#9fd8f5"):
    img, p, ss = _canvas()
    grad(img, 0, 1080, tint(col, 0.2), col)
    return _done(img, ss)


# set id -> (builder, kwargs, ground y in world, animation kind)
SETS = {
    "bedroom": (b_room, dict(kind="bedroom"), 900, None),
    "bedroom_night": (b_room, dict(kind="bedroom", view="night", wall_col="#7c86b8"), 900, None),
    "living_room": (b_room, dict(kind="living", wall_col="#f2e3c6"), 900, None),
    "bathroom": (b_room, dict(kind="bathroom"), 920, None),
    "kitchen": (b_room, dict(kind="kitchen", wall_col="#fbe8c4"), 900, None),
    "backyard": (b_yard, dict(), 790, "pool"),
    "backyard_dusk": (b_yard, dict(view="dusk"), 790, "pool"),
    "backyard_night": (b_yard, dict(view="night"), 790, "night"),
    "street": (b_street, dict(), 960, None),
    "beach": (b_beach, dict(), 900, "sea"),
    "beach_dusk": (b_beach, dict(view="dusk"), 900, "sea"),
    "harbor": (b_harbor, dict(), 640, "harbor"),
    "ocean_surface": (b_ocean_surface, dict(), 700, "sea_big"),
    "ocean_storm": (b_ocean_surface, dict(view="storm"), 700, "sea_big"),
    "underwater": (b_underwater, dict(depth="shallow"), 950, "under"),
    "underwater_mid": (b_underwater, dict(depth="mid"), 950, "under"),
    "deep_sea": (b_underwater, dict(depth="deep"), 980, "deep"),
    "lab": (b_lab, dict(), 920, None),
    "office": (b_office, dict(), 920, None),
    "news": (b_news, dict(), 900, None),
    "plain": (b_plain, dict(), 900, None),
    "backyard_storm": (b_yard, dict(view="night"), 790, "storm"),
    "harbor_dusk": (b_harbor, dict(view="dusk"), 705, "harbor"),
    "reef_night": (b_ocean_surface, dict(view="night", reef=True), 700, "sea_night"),
    "sea_night": (b_ocean_surface, dict(view="night"), 700, "sea_night"),
    "beach_dawn": (b_beach, dict(view="dawn"), 900, "sea"),
    "bait_shop": (b_shop, dict(), 920, None),
    "lagoon": (b_lagoon, dict(), 700, "lagoon"),
    "studio": (b_studio, dict(), 900, None),
}
ALIASES: dict[str, str] = {}
GROUND = {}


def _resolve(set_id):
    return ALIASES.get(set_id, set_id)


def register_aliases(mapping: dict):
    ALIASES.update(mapping)
    for k, v in mapping.items():
        GROUND[k] = SETS[v][2]


for _k, _v in SETS.items():
    GROUND[_k] = _v[2]


def background(set_id) -> Image.Image:
    sid = _resolve(set_id)
    CACHE.mkdir(parents=True, exist_ok=True)
    f = CACHE / f"{sid}.png"
    if f.exists():
        return Image.open(f).convert("RGB")
    fn, kw, _, _ = SETS[sid]
    img = fn(**kw)
    img.save(f)
    return img


# ------------------------------------------------------------------ moving layers (screen space)

def animate_layer(set_id, frame, t, s2w, z):
    kind = SETS[_resolve(set_id)][3]
    if not kind:
        return
    d = ImageDraw.Draw(frame, "RGBA")
    if kind == "storm":
        rnd = random.Random(int(t * 30))
        for i in range(70):
            x = rnd.uniform(0, W)
            y = rnd.uniform(0, H)
            d.line([(x, y), (x - 12, y + 46)], fill=(200, 215, 255, 110), width=2)
        if (t % 4.3) < 0.12 or 1.0 < (t % 4.3) < 1.07:
            frame.alpha_composite(Image.new("RGBA", frame.size, (230, 235, 255, 120)))
    if kind == "lagoon":
        for i in range(18):
            wx = (i * 211 + t * 25) % 2000 - 40
            wy = 480 + (i * 61) % 560
            if wx < 400 and wy > 560:
                continue
            x, y = s2w(wx, wy)
            d.line([(x, y), (x + 36 * z, y)], fill=(255, 255, 255, 110), width=max(2, int(3 * z)))
    if kind in ("sea", "sea_big", "harbor", "sea_night"):
        y_top = {"sea": 500, "sea_big": 550, "harbor": 760, "sea_night": 560}[kind]
        for i in range(26):
            wx = (i * 173 + t * (40 + (i % 5) * 12)) % 2100 - 90
            wy = y_top + 20 + (i * 37) % (1080 - y_top)
            if kind == "sea" and wy > 690:
                continue
            x, y = s2w(wx, wy)
            ln = 40 * z
            d.line([(x, y), (x + ln, y)], fill=(255, 255, 255, 120 if kind != "sea_night" else 50), width=max(2, int(4 * z)))
    if kind in ("pool", "night"):
        for i in range(8):
            wx = 480 + ((i * 131 + t * 30) % 960)
            wy = 860 + (i * 23) % 150
            x, y = s2w(wx, wy)
            d.line([(x, y), (x + 50 * z, y)], fill=(255, 255, 255, 150), width=max(2, int(5 * z)))
    if kind in ("under", "deep"):
        rnd = random.Random(11)
        for i in range(34):
            bx = rnd.uniform(0, 1920)
            spd = rnd.uniform(40, 110)
            by = 1080 - ((t * spd + rnd.uniform(0, 1080)) % 1180)
            r = rnd.uniform(4, 11)
            x, y = s2w(bx + math.sin(t * 2 + i) * 10, by)
            rr = r * z
            a = 140 if kind == "under" else 70
            d.ellipse([x - rr, y - rr, x + rr, y + rr], outline=(255, 255, 255, a), width=max(1, int(2.2 * z)))


def foreground_layer(set_id, frame, t, s2w, z):
    kind = SETS[_resolve(set_id)][3]
    if kind in ("night", "storm"):
        frame.alpha_composite(Image.new("RGBA", frame.size, (12, 18, 50, 95)))
    if kind == "under":
        over = Image.new("RGBA", frame.size, (40, 150, 210, 36))
        d = ImageDraw.Draw(over)
        for i in range(5):
            x = (i * 430 + math.sin(t * 0.6 + i) * 80) % 2200 - 140
            d.polygon([(x, 0), (x + 120, 0), (x + 380, 1080), (x + 200, 1080)], fill=(255, 255, 255, 22))
        frame.alpha_composite(over)
    elif kind == "deep":
        frame.alpha_composite(Image.new("RGBA", frame.size, (5, 15, 40, 60)))


EXTRA_PROPS: dict = {}
