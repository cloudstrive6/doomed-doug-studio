"""Shot -> frames. Handles boil variants (GIF-like loop), element pop-ins and camera moves."""
from __future__ import annotations

from PIL import Image

from .paint import Canvas, draw_elements, font

OUT_W, OUT_H = 1920, 1080
_BAR_CACHE: dict = {}


def topbar_image(text: str):
    """Persistent top-centre caption bar with the current item name in ALL CAPS (style bible 4.2)."""
    if text in _BAR_CACHE:
        return _BAR_CACHE[text]
    from PIL import ImageDraw
    f = font(46, "ComicNeue-Bold")
    label = text.upper()
    probe = ImageDraw.Draw(Image.new("RGB", (1, 1)))
    tw = int(probe.textlength(label, font=f))
    w, h = min(tw + 70, OUT_W - 80), 68
    bar = Image.new("RGBA", (w, h), (255, 255, 255, 255))
    d = ImageDraw.Draw(bar)
    d.fontmode = "1"
    d.rectangle((0, 0, w - 1, h - 1), outline=(0, 0, 0, 255), width=3)
    d.text((w / 2, h / 2 + 2), label, font=f, fill=(0, 0, 0, 255), anchor="mm")
    _BAR_CACHE[text] = bar
    return bar


def fit_frame(img, rect):
    """Crop the camera rect and scale it to 1920x1080. Nearest-neighbour keeps flat MS Paint fills crisp for 1:1
    and small push-ins; big upscales (e.g. the 1280x720 thumbnail used as the opening shot) use Lanczos, because
    nearest at 1.5x gives uneven, jagged pixel doubling on every line and letter."""
    crop = img.crop(tuple(round(v) for v in rect))
    up = OUT_W / max(1, crop.width)
    return crop.resize((OUT_W, OUT_H), Image.LANCZOS if up >= 1.25 else Image.NEAREST)


def with_topbar(img, text):
    if not text:
        return img
    bar = topbar_image(text)
    out = img.copy()
    out.paste(bar, ((OUT_W - bar.width) // 2, 16), bar)
    return out


def render_still(scene: dict, variant: int = 0, t: float | None = None, seed: str = "shot",
                 style: dict | None = None) -> Image.Image:
    style = style or {}
    w, h = scene.get("size", [OUT_W, OUT_H])
    cv = Canvas(w, h, scene.get("background", "#ffffff"), seed=seed, variant=variant,
                boil=style.get("boil_px", 1.6), wobble=style.get("wobble_px", 1.2))
    draw_elements(cv, scene.get("elements", []), seed=seed, visible_time=t)
    return _clean_edges(cv.img, EDGE_PX)


# Ring depth rebuilt by _clean_edges (boil/wobble can pull full-bleed backgrounds ~3 px in from the border).
EDGE_PX = 5


def _clean_edges(img, ring=4):
    """Overwrite the outermost `ring` pixels with the row/column just inside them: background outlines, light rays
    and boil-shifted shapes (which pull in by up to 2 px) otherwise leave a white line at the canvas border that
    blinks at cuts on dark scenes."""
    w, h = img.size
    if w < 4 * ring or h < 4 * ring:
        return img
    for i in range(ring):
        img.paste(img.crop((0, ring, w, ring + 1)), (0, i))
        img.paste(img.crop((0, h - ring - 1, w, h - ring)), (0, h - 1 - i))
    for i in range(ring):
        img.paste(img.crop((ring, 0, ring + 1, h)), (i, 0))
        img.paste(img.crop((w - ring - 1, 0, w - ring, h)), (w - 1 - i, 0))
    return img


def _lerp(a, b, u):
    return a + (b - a) * u


def _ease(u, kind):
    if kind == "linear":
        return u
    if kind == "in":
        return u * u
    if kind == "out":
        return 1 - (1 - u) * (1 - u)
    return u * u * (3 - 2 * u)  # smoothstep


def camera_rect(cam: dict | None, canvas_w: int, canvas_h: int, u: float):
    """Return crop rect (x0, y0, x1, y1) at progress u in [0,1].
    cam: {"from": [cx, cy, zoom], "to": [cx, cy, zoom], "ease": "smooth"}; zoom 1 = 1920 wide view.
    Shorthands: {"move": "zoom_in"} / "zoom_out" / "pan_down" / "shake"."""
    if not cam:
        cam = {}
    move = cam.get("move")
    cx0, cy0 = canvas_w / 2, canvas_h / 2
    base_zoom = OUT_W / canvas_w if canvas_w / canvas_h >= OUT_W / OUT_H else OUT_H / canvas_h
    if move == "zoom_in":
        a, b = [cx0, cy0, 1.0], [cam.get("x", cx0), cam.get("y", cy0), cam.get("zoom", 1.15)]
    elif move == "zoom_out":
        a, b = [cam.get("x", cx0), cam.get("y", cy0), cam.get("zoom", 1.15)], [cx0, cy0, 1.0]
    elif move == "pan_down":
        a, b = [cx0, OUT_H / 2, 1.0], [cx0, canvas_h - OUT_H / 2, 1.0]
    elif move == "pan_up":
        a, b = [cx0, canvas_h - OUT_H / 2, 1.0], [cx0, OUT_H / 2, 1.0]
    elif move == "pan_right":
        a, b = [OUT_W / 2, cy0, 1.0], [canvas_w - OUT_W / 2, cy0, 1.0]
    else:
        a = cam.get("from", [cx0, cy0, 1.0])
        b = cam.get("to", a)
    e = _ease(u, cam.get("ease", "smooth"))
    cx, cy, z = (_lerp(a[i], b[i], e) for i in range(3))
    if move == "shake":
        import math
        cx += 12 * math.sin(u * 90)
        cy += 8 * math.cos(u * 77)
    vw = OUT_W / z
    vh = OUT_H / z
    if (move in (None, "static") and not cam.get("from") and (canvas_w, canvas_h) != (OUT_W, OUT_H)):
        # fit whole canvas
        vw, vh = canvas_w, canvas_w * OUT_H / OUT_W
    x0 = min(max(cx - vw / 2, 0), max(canvas_w - vw, 0))
    y0 = min(max(cy - vh / 2, 0), max(canvas_h - vh, 0))
    return (x0, y0, x0 + vw, y0 + vh)


class ShotRenderer:
    """Yields output frames (PIL images, 1920x1080) for one shot, caching drawings."""

    def __init__(self, shot: dict, duration: float, fps: int = 24, style: dict | None = None,
                 topbar: str | None = None, n_frames: int | None = None):
        self.shot, self.duration, self.fps, self.topbar = shot, duration, fps, topbar
        self.n_frames = n_frames
        self.style = style or {}
        self.scene = shot["scene"]
        self.n_variants = 1 if shot.get("boil") is False else int(self.style.get("boil_variants", 3))
        self.boil_fps = float(self.style.get("boil_fps", 8))
        appear = sorted({float(e.get("appear", 0)) for e in self.scene.get("elements", [])})
        self.appear_steps = appear or [0.0]
        self.cache = {}

    def _drawing(self, variant, step_t):
        key = (variant, step_t)
        if key not in self.cache:
            self.cache[key] = render_still(self.scene, variant, step_t, seed=self.shot.get("id", "shot"),
                                           style=self.style)
        return self.cache[key]

    def frames(self):
        n = self.n_frames if self.n_frames is not None else max(1, round(self.duration * self.fps))
        w, h = self.scene.get("size", [OUT_W, OUT_H])
        cam = self.shot.get("camera")
        static_cam = (not cam or cam.get("move") in (None, "static")) and not (cam or {}).get("from")
        last_key, last_frame = None, None
        for i in range(n):
            u = i / max(1, n - 1)
            t_frac = i / n
            step = max([s for s in self.appear_steps if s <= t_frac + 1e-9], default=0.0)
            variant = int(i / self.fps * self.boil_fps) % self.n_variants
            img = self._drawing(variant, step)
            rect = camera_rect(cam, w, h, 0 if static_cam else u)
            key = (variant, step, tuple(round(v) for v in rect))
            if key != last_key:
                if rect == (0, 0, OUT_W, OUT_H) and img.size == (OUT_W, OUT_H):
                    frame = img
                else:
                    frame = fit_frame(img, rect)
                frame = with_topbar(frame, self.topbar)
                last_key, last_frame = key, frame
            yield last_frame
