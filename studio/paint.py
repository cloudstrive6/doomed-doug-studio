"""MS Paint-style rendering engine.

Everything is drawn with Pillow's aliased (non-antialiased) primitives, so edges
come out jagged exactly like MS Paint. Shapes are described as JSON "elements"
(see docs/SCENE_SCHEMA.md) and every shape is reduced to polylines/polygons so
the same code handles scaling, flipping, rotation and hand-drawn "boil" jitter.
"""
from __future__ import annotations

import math
import random
from functools import lru_cache
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
FONT_DIR = ROOT / "assets" / "fonts"
LIBRARY_DIR = ROOT / "assets" / "library"

# ---------------------------------------------------------------- utilities


def hex_rgb(c):
    if c is None or c == "none":
        return None
    if isinstance(c, (list, tuple)):
        return tuple(c)
    c = str(c).lstrip("#")
    if len(c) == 3:
        c = "".join(ch * 2 for ch in c)
    return tuple(int(c[i : i + 2], 16) for i in (0, 2, 4))


@lru_cache(maxsize=64)
def font(size: int, name: str = "default", bold: bool = False):
    """Fonts ship in assets/fonts: 'default' = Arimo (Arial look-alike, like MS Paint text),
    'ComicNeue-Bold' / 'ComicNeue-Regular' for comic lettering."""
    candidates = []
    if name and name != "default":
        candidates += [FONT_DIR / name, FONT_DIR / f"{name}.ttf"]
    candidates += [FONT_DIR / "Arimo.ttf"] + sorted(FONT_DIR.glob("*.ttf"))
    candidates += [
        Path("C:/Windows/Fonts/arial.ttf"),
        Path("/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"),
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
    ]
    for p in candidates:
        if p.exists():
            f = ImageFont.truetype(str(p), int(size))
            try:
                f.set_variation_by_axes([700 if bold else 400])
            except Exception:
                pass
            return f
    return ImageFont.load_default()


class Transform:
    """scale -> rotate -> flip -> translate, applied to local points."""

    def __init__(self, x=0.0, y=0.0, scale=1.0, rotate=0.0, flip=False, parent=None):
        self.x, self.y, self.s, self.r, self.flip = x, y, scale, math.radians(rotate), flip
        self.parent = parent

    def apply(self, p):
        px, py = p[0] * self.s, p[1] * self.s
        if self.flip:
            px = -px
        if self.r:
            c, s = math.cos(self.r), math.sin(self.r)
            px, py = px * c - py * s, px * s + py * c
        out = (px + self.x, py + self.y)
        return self.parent.apply(out) if self.parent else out

    @property
    def total_scale(self):
        return self.s * (self.parent.total_scale if self.parent else 1.0)


def ellipse_points(cx, cy, rx, ry, n=None, a0=0.0, a1=360.0):
    n = n or max(16, int((rx + ry) / 3))
    pts = []
    for i in range(n + 1):
        a = math.radians(a0 + (a1 - a0) * i / n)
        pts.append((cx + rx * math.cos(a), cy + ry * math.sin(a)))
    return pts


def catmull_rom(points, steps=8):
    if len(points) < 3:
        return list(points)
    pts = [points[0]] + list(points) + [points[-1]]
    out = []
    for i in range(1, len(pts) - 2):
        p0, p1, p2, p3 = pts[i - 1], pts[i], pts[i + 1], pts[i + 2]
        for s in range(steps):
            t = s / steps
            t2, t3 = t * t, t * t * t
            out.append(tuple(
                0.5 * ((2 * p1[k]) + (-p0[k] + p2[k]) * t + (2 * p0[k] - 5 * p1[k] + 4 * p2[k] - p3[k]) * t2
                       + (-p0[k] + 3 * p1[k] - 3 * p2[k] + p3[k]) * t3)
                for k in (0, 1)))
    out.append(points[-1])
    return out


def subdivide(points, max_len=40.0):
    if len(points) < 2:
        return list(points)
    out = [points[0]]
    for a, b in zip(points, points[1:]):
        d = math.dist(a, b)
        n = max(1, int(d / max_len))
        for i in range(1, n + 1):
            out.append((a[0] + (b[0] - a[0]) * i / n, a[1] + (b[1] - a[1]) * i / n))
    return out


class Jitter:
    """Hand-drawn wobble. `static` wobble is fixed per element (freehand look);
    `boil` changes per variant so held drawings shimmer like a looping GIF."""

    def __init__(self, seed, boil_variant=0, boil=1.6, wobble=1.2):
        self.seed, self.variant, self.boil, self.wobble = seed, boil_variant, boil, wobble
        self.counter = 0

    def __call__(self, pts, scale=1.0):
        self.counter += 1
        rs = random.Random(f"{self.seed}:{self.counter}")
        rb = random.Random(f"{self.seed}:{self.counter}:v{self.variant}")
        amp_w = self.wobble * min(scale, 2.0)
        amp_b = self.boil * min(scale, 2.0) if self.variant else 0.0
        # low-frequency static wobble: a couple of sine waves along the path
        ph1, ph2 = rs.uniform(0, 6.28), rs.uniform(0, 6.28)
        out = []
        for i, (x, y) in enumerate(pts):
            dx = amp_w * math.sin(i * 0.35 + ph1)
            dy = amp_w * math.sin(i * 0.29 + ph2)
            if amp_b:
                dx += rb.uniform(-amp_b, amp_b)
                dy += rb.uniform(-amp_b, amp_b)
            out.append((x + dx, y + dy))
        return out


# ---------------------------------------------------------------- canvas


class Canvas:
    def __init__(self, w, h, background="#ffffff", seed="scene", variant=0, boil=1.6, wobble=1.2):
        self.w, self.h = int(w), int(h)
        self.img = Image.new("RGB", (self.w, self.h), hex_rgb(background) or (255, 255, 255))
        self.draw = ImageDraw.Draw(self.img)
        self.draw.fontmode = "1"  # aliased text, MS Paint style
        self.seed, self.variant, self.boil, self.wobble = seed, variant, boil, wobble

    # low-level ---------------------------------------------------------
    def stroke(self, pts, color="#000", width=4, closed=False):
        if len(pts) < 2 or color in (None, "none"):
            return
        pts = [(round(x), round(y)) for x, y in pts]
        if closed:
            pts = pts + [pts[0]]
        w = max(1, round(width))
        self.draw.line(pts, fill=hex_rgb(color), width=w, joint="curve")
        if w >= 4:  # round caps
            r = w / 2
            for x, y in (pts[0], pts[-1]):
                self.draw.ellipse((x - r + 0.5, y - r + 0.5, x + r - 0.5, y + r - 0.5), fill=hex_rgb(color))

    def poly(self, pts, fill=None, color="#000", width=4):
        if len(pts) < 3:
            return
        ipts = [(round(x), round(y)) for x, y in pts]
        if fill not in (None, "none"):
            self.draw.polygon(ipts, fill=hex_rgb(fill))
        if width and color not in (None, "none"):
            self.stroke(pts, color, width, closed=True)

    def bucket(self, x, y, color):
        x, y = int(x), int(y)
        if 0 <= x < self.w and 0 <= y < self.h:
            ImageDraw.floodfill(self.img, (x, y), hex_rgb(color), thresh=40)

    def spray(self, x, y, radius, color, density=0.35, seed=0):
        r = random.Random(f"spray:{seed}")
        n = int(density * radius * radius)
        c = hex_rgb(color)
        for _ in range(n):
            a, d = r.uniform(0, 6.283), radius * math.sqrt(r.random())
            px, py = int(x + d * math.cos(a)), int(y + d * math.sin(a))
            if 0 <= px < self.w and 0 <= py < self.h:
                self.img.putpixel((px, py), c)

    def text(self, s, x, y, size=48, color="#000", align="center", outline=None, outline_width=0,
             font_name="default", max_width=None, line_spacing=1.1, bold=False):
        f = font(int(size), font_name, bold)
        lines = wrap(s, f, max_width) if max_width else str(s).split("\n")
        heights = [f.getbbox(l or " ")[3] - f.getbbox(l or " ")[1] for l in lines]
        lh = int(size * line_spacing)
        total = lh * len(lines)
        cy = y - total / 2
        for line in lines:
            tw = self.draw.textlength(line, font=f)
            if align == "center":
                tx = x - tw / 2
            elif align == "right":
                tx = x - tw
            else:
                tx = x
            kw = {}
            if outline and outline_width:
                kw = dict(stroke_width=int(outline_width), stroke_fill=hex_rgb(outline))
            self.draw.text((round(tx), round(cy)), line, font=f, fill=hex_rgb(color), **kw)
            cy += lh


def wrap(s, f, max_width):
    out = []
    for para in str(s).split("\n"):
        words, cur = para.split(), ""
        for w in words:
            t = (cur + " " + w).strip()
            if f.getlength(t) <= max_width or not cur:
                cur = t
            else:
                out.append(cur)
                cur = w
        out.append(cur)
    return out


# ---------------------------------------------------------------- elements


def load_asset(name):
    p = LIBRARY_DIR / f"{name}.json"
    if not p.exists():
        raise FileNotFoundError(f"asset '{name}' not found in {LIBRARY_DIR}")
    import json
    return json.loads(p.read_text(encoding="utf-8"))


def draw_elements(cv: Canvas, elements, tf: Transform | None = None, seed="root", visible_time=None):
    tf = tf or Transform()
    for i, el in enumerate(elements):
        if visible_time is not None and el.get("appear", 0) > visible_time:
            continue
        draw_element(cv, el, tf, f"{seed}/{i}")


def dashed(pts, on, off):
    """Split a polyline into dash segments."""
    out, cur, draw, left = [], [pts[0]], True, on
    for a, b in zip(pts, pts[1:]):
        d = math.dist(a, b)
        pos = 0.0
        while d - pos > left:
            pos += left
            p = (a[0] + (b[0] - a[0]) * pos / d, a[1] + (b[1] - a[1]) * pos / d)
            if draw:
                cur.append(p)
                out.append(cur)
            cur = [p]
            draw, left = not draw, (off if draw else on)
        left -= d - pos
        if draw:
            cur.append(b)
        else:
            cur = [b]
    if draw and len(cur) > 1:
        out.append(cur)
    return out


def rounded_rect(x, y, w, h, r):
    r = min(r, w / 2, h / 2)
    pts = []
    for cx, cy, a0 in ((x + w - r, y + r, -90), (x + w - r, y + h - r, 0), (x + r, y + h - r, 90), (x + r, y + r, 180)):
        pts += ellipse_points(cx, cy, r, r, n=6, a0=a0, a1=a0 + 90)
    return pts


def _silhouette(el, cv):
    """While drawing a silhouetted asset, everything becomes flat black (text/spray are skipped)."""
    if not getattr(cv, "silhouette", False):
        return el
    if el.get("type") in ("text", "label", "spray", "wordart"):
        return None
    el = dict(el)
    el["color"] = "#000000"
    if el.get("fill") not in (None, "none"):
        el["fill"] = "#000000"
    return el


def draw_element(cv: Canvas, el, tf: Transform, seed):
    el = _silhouette(el, cv)
    if el is None:
        return
    t = el.get("type")
    jit = Jitter(seed, cv.variant, cv.boil * el.get("boil", 1.0), cv.wobble * el.get("wobble", 1.0))
    sc = tf.total_scale
    width = el.get("width", 4) * sc
    color = el.get("color", "#000000")

    def P(pts):
        return [tf.apply(p) for p in pts]

    if t in ("line", "curve"):
        pts = el["points"]
        if t == "curve" or el.get("smooth"):
            pts = catmull_rom(pts)
        pts = jit(subdivide(P(pts), 30), sc)
        if el.get("dash"):
            on, off = el["dash"]
            for seg in dashed(pts, on * sc, off * sc):
                cv.stroke(seg, color, width)
        else:
            cv.stroke(pts, color, width)
    elif t == "arrow":
        (x1, y1), (x2, y2) = el["from"], el["to"]
        bend = el.get("bend", 0)  # perpendicular offset of the midpoint -> curved arrow
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        L = math.dist((x1, y1), (x2, y2)) or 1
        nx, ny = -(y2 - y1) / L, (x2 - x1) / L
        path = catmull_rom([(x1, y1), (mx + nx * bend, my + ny * bend), (x2, y2)]) if bend else [(x1, y1), (x2, y2)]
        shaft = jit(subdivide(P(path), 30), sc)
        cv.stroke(shaft, color, width)
        px, py = path[-2] if len(path) > 1 else (x1, y1)
        ang = math.atan2(y2 - py, x2 - px)
        hl = el.get("head", 34)
        head = [(x2, y2), (x2 + hl * math.cos(ang + 2.6), y2 + hl * math.sin(ang + 2.6)),
                (x2 + hl * math.cos(ang - 2.6), y2 + hl * math.sin(ang - 2.6))]
        cv.poly(jit(P(head), sc), color, color, max(1, width / 2))
    elif t in ("poly", "polygon"):
        pts = el["points"]
        if el.get("smooth"):
            pts = catmull_rom(pts + [pts[0]])
        pts = jit(subdivide(P(pts), 30), sc)
        cv.poly(pts, el.get("fill"), el.get("color", "#000000"), width if el.get("outline", True) else 0)
    elif t in ("ellipse", "circle"):
        cx, cy = el.get("x", 0), el.get("y", 0)
        rx = el.get("rx", el.get("r", 50))
        ry = el.get("ry", el.get("r", rx))
        n = max(16, int((rx + ry) * sc / 3))
        pts = jit(P(ellipse_points(cx, cy, rx, ry, n=n, a0=el.get("start", 0), a1=el.get("end", 360))), sc)
        if el.get("start") is not None or el.get("end") is not None:
            cv.stroke(pts, color, width)
        else:
            cv.poly(pts, el.get("fill"), color, width if el.get("outline", True) else 0)
    elif t == "rect":
        x, y, w, h = el["x"], el["y"], el["w"], el["h"]
        pts = jit(subdivide(P([(x, y), (x + w, y), (x + w, y + h), (x, y + h)]), 30), sc)
        cv.poly(pts, el.get("fill"), color, width if el.get("outline", True) else 0)
    elif t == "fill":
        x, y = tf.apply((el["x"], el["y"]))
        cv.bucket(x, y, el["color"])
    elif t == "spray":
        x, y = tf.apply((el["x"], el["y"]))
        cv.spray(x, y, el.get("r", 40) * sc, color, el.get("density", 0.35), seed)
    elif t == "text":
        x, y = tf.apply((el["x"], el["y"]))
        cv.text(el["text"], x, y, el.get("size", 56) * sc, color, el.get("align", "center"),
                el.get("outline"), el.get("outline_width", 0) * sc, el.get("font", "default"),
                el.get("max_width", None) and el["max_width"] * sc, bold=el.get("bold", False))
    elif t == "label":  # text with a white box behind it
        x, y = tf.apply((el["x"], el["y"]))
        size = el.get("size", 48) * sc
        f = font(int(size), el.get("font", "default"), el.get("bold", False))
        tw = cv.draw.textlength(el["text"], font=f)
        pad = size * 0.3
        box = [(x - tw / 2 - pad, y - size * 0.75), (x + tw / 2 + pad, y - size * 0.75),
               (x + tw / 2 + pad, y + size * 0.75), (x - tw / 2 - pad, y + size * 0.75)]
        cv.poly(jit(subdivide(box, 30), sc), el.get("fill", "#ffffff"), color, 3 * sc)
        cv.text(el["text"], x, y, size, el.get("text_color", color), bold=el.get("bold", False),
                font_name=el.get("font", "default"))
    elif t == "group":
        sub = Transform(el.get("x", 0), el.get("y", 0), el.get("scale", 1), el.get("rotate", 0),
                        el.get("flip", False), tf)
        draw_elements(cv, el["elements"], sub, seed)
    elif t == "asset":
        a = load_asset(el["name"])
        ax, ay = a.get("anchor", [0, 0])
        inner = Transform(-ax, -ay, 1.0, 0, False)
        outer = Transform(el.get("x", 0), el.get("y", 0), el.get("scale", 1), el.get("rotate", 0),
                          el.get("flip", False), tf)
        inner.parent = outer
        ink = el.get("ink")
        if ink is None and a.get("auto_ink"):  # crude-tier humans: same white-ink rule as Doug on dark backgrounds
            px, py = outer.apply((0, -80))
            px, py = min(max(int(px), 0), cv.w - 1), min(max(int(py), 0), cv.h - 1)
            r, g, b = cv.img.getpixel((px, py))[:3]
            if 0.299 * r + 0.587 * g + 0.114 * b < 70:
                ink = "#ffffff"
        if ink:
            def _ink(els):
                out = []
                for e in els:
                    e = dict(e)
                    if e.get("type") == "group":
                        e["elements"] = _ink(e.get("elements", []))
                    elif not e.get("keep_ink") and \
                            e.get("type") not in ("spray", "fill", "text", "wordart", "label", "speech") and \
                            e.get("color", "#000000").lower() == "#000000":
                        e["color"] = ink
                    out.append(e)
                return out
            a = {**a, "elements": _ink(a["elements"])}
        if el.get("silhouette"):
            # unknown/terrifying reveal: black shape with a red glow (style bible 4.2)
            gx, gy = outer.apply((0, 0))
            gr = el.get("glow_r", 260) * outer.total_scale
            for k, (rf, dens) in enumerate(((1.0, 0.16), (0.8, 0.32), (0.6, 0.6))):  # soft radial falloff
                cv.spray(gx, gy, gr * rf, el.get("glow", "#ff2a1a"), dens, f"{seed}:{k}")
            cv.silhouette = True
            try:
                draw_elements(cv, a["elements"], inner, seed + ":" + el["name"])
            finally:
                cv.silhouette = False
        else:
            draw_elements(cv, a["elements"], inner, seed + ":" + el["name"])
    elif t == "tile":  # thumbnail/intro grid tile: rounded black frame, content, comic label underneath
        x, y, w, h = el["x"], el["y"], el["w"], el["h"]
        frame = P(rounded_rect(x, y, w, h, el.get("radius", 26)))
        cv.poly(frame, el.get("fill", "#ffffff"), "#000000", 0)
        inner = el.get("elements") or ([{"type": "asset", "name": el["asset"], "x": x + w / 2, "y": y + h / 2,
                                          "scale": el.get("asset_scale", 0.5), "flip": el.get("flip", False)}]
                                       if el.get("asset") else [])
        before = cv.img.copy()
        draw_elements(cv, inner, tf, seed + ":tile")
        from PIL import Image as _I, ImageDraw as _D
        mask = _I.new("L", cv.img.size, 0)
        _D.Draw(mask).polygon([(round(a), round(b)) for a, b in frame], fill=255)
        cv.img.paste(_I.composite(cv.img, before, mask))  # clip tile contents to the frame
        cv.draw = _D.Draw(cv.img)
        cv.draw.fontmode = "1"
        cv.stroke(frame, "#000000", el.get("frame_width", 7) * sc, closed=True)
        if el.get("label"):
            lx, ly = tf.apply((x + w / 2, y + h + el.get("label_size", 44) * 0.75))
            cv.text(el["label"], lx, ly, el.get("label_size", 44) * sc, "#000000", font_name="ComicNeue-Bold")
    elif t == "wordart":  # keyword label: yellow->green gradient fill, thin dark outline (style bible 4.2)
        x, y = tf.apply((el["x"], el["y"]))
        size = el.get("size", 72) * sc
        f = font(int(size), el.get("font", "default"), True)
        from PIL import Image as _I, ImageDraw as _D
        tw = int(cv.draw.textlength(el["text"], font=f)) + 20
        th = int(size * 1.4)
        mask = _I.new("L", (tw, th), 0)
        md = _D.Draw(mask)
        md.fontmode = "1"
        md.text((10, int(size * 0.1)), el["text"], font=f, fill=255)
        top, bot = hex_rgb(el.get("top", "#fff200")), hex_rgb(el.get("bottom", "#39d353"))
        grad = _I.new("RGB", (tw, th))
        gd = _D.Draw(grad)
        for yy in range(th):
            u = yy / max(1, th - 1)
            gd.line([(0, yy), (tw, yy)], fill=tuple(int(top[k] + (bot[k] - top[k]) * u) for k in range(3)))
        ox, oy = int(x - tw / 2), int(y - th / 2)
        # outline: draw text stroke first, then gradient through the mask
        cv.draw.text((ox + 10, oy + int(size * 0.1)), el["text"], font=f, fill=hex_rgb(el.get("outline", "#1a1a1a")),
                     stroke_width=max(2, int(size / 18)), stroke_fill=hex_rgb(el.get("outline", "#1a1a1a")))
        cv.img.paste(grad, (ox, oy), mask)
    elif t == "image":  # real photo inset (public domain / licensed only; see assets/photos/SOURCES.md)
        from PIL import Image as _I
        p = ROOT / "assets" / "photos" / el["file"]
        im = _I.open(p).convert("RGB")
        w = int(el.get("w", 600) * sc)
        h = int(im.height * w / im.width)
        im = im.resize((w, h), _I.LANCZOS)
        x, y = tf.apply((el["x"], el["y"]))
        x0, y0 = int(x - w / 2), int(y - h / 2)
        cv.img.paste(im, (x0, y0))
        bw = int(el.get("frame_width", 4) * sc)
        cv.draw.rectangle((x0 - bw, y0 - bw, x0 + w + bw - 1, y0 + h + bw - 1), outline=(0, 0, 0), width=bw)
    elif t == "doug":
        from .doug import doug_elements
        if "ink" not in el:  # auto-contrast: white lines on dark backgrounds
            px, py = tf.apply((el.get("x", 0), el.get("y", 0) - 80 * el.get("scale", 1)))
            px, py = min(max(int(px), 0), cv.w - 1), min(max(int(py), 0), cv.h - 1)
            r, g, b = cv.img.getpixel((px, py))[:3]
            if 0.299 * r + 0.587 * g + 0.114 * b < 70:
                el = {**el, "ink": "#ffffff"}
        els = doug_elements(el, cv.variant)
        sub = Transform(el.get("x", 0), el.get("y", 0), el.get("scale", 1), el.get("rotate", 0),
                        el.get("facing", "right") == "left", tf)
        draw_elements(cv, els, sub, seed + ":doug")
    elif t == "bands":  # stacked horizontal colour bands (sky, ocean layers...)
        for b in el["bands"]:
            x0, _ = tf.apply((0, b["y0"]))
            _, y1 = tf.apply((0, b["y1"]))
            _, y0 = tf.apply((0, b["y0"]))
            cv.draw.rectangle((0, round(y0), cv.w, round(y1)), fill=hex_rgb(b["color"]))
    elif t == "speech":
        x, y = el["x"], el["y"]
        w, h = el.get("w", 420), el.get("h", 150)
        body = ellipse_points(x, y, w / 2, h / 2)
        tx, ty = el.get("tail", [x - w * 0.25, y + h * 0.9])
        tail = [(x - w * 0.12, y + h * 0.35), (tx, ty), (x + w * 0.02, y + h * 0.42)]
        cv.poly(jit(P(body), sc), "#ffffff", "#000000", 4 * sc)
        cv.poly(jit(P(tail), sc), "#ffffff", "#000000", 4 * sc)
        cv.poly(jit(P([(x - w * 0.1, y + h * 0.3), (x, y + h * 0.3), (x, y + h * 0.45)]), sc),
                "#ffffff", "#ffffff", 0)
        cx, cy = tf.apply((x, y))
        cv.text(el["text"], cx, cy, el.get("size", 40) * sc, "#000000", max_width=w * 0.8 * sc)
    else:
        raise ValueError(f"unknown element type: {t!r}")
