"""Bridge from the old episode art library (assets/library/*.json, about 2,000 hand-built vector animals, plants and
objects drawn by the paint engine) to the toon engine: any library asset can be placed in a What If scene or
thumbnail as a prop with id "lib:<name>" (for example {"id": "lib:beluga", "x": 900, "y": 700, "scale": 1.2}).

The paint engine draws aliased shapes on an opaque canvas, so the asset is drawn on a key colour at 3x, keyed out,
and reduced (smooth edges), with the hand-drawn wobble switched off to match the clean toon line.
  py -m studio.toon_lib find mosquito          list library assets whose name, description or tags match
"""
from __future__ import annotations

import json
import sys
from functools import lru_cache

import numpy as np
from PIL import Image

from . import paint

KEY = (255, 0, 255)
SS = 3


def _bbox(elements):
    xs, ys = [], []
    def walk(els):
        for el in els:
            for p in el.get("points", []) or []:
                xs.append(p[0])
                ys.append(p[1])
            if "x" in el and "y" in el:
                rx, ry = el.get("rx", el.get("r", 0)), el.get("ry", el.get("r", 0))
                xs.extend([el["x"] - rx, el["x"] + rx])
                ys.extend([el["y"] - ry, el["y"] + ry])
            if el.get("elements"):
                walk(el["elements"])
    walk(elements)
    if not xs:
        return -100, -100, 100, 100
    return min(xs) - 8, min(ys) - 8, max(xs) + 8, max(ys) + 8


@lru_cache(maxsize=256)
def _master(name):
    """The asset at 1 unit = 1 px, RGBA, plus the anchor offset inside the image."""
    asset = paint.load_asset(name)
    x0, y0, x1, y1 = _bbox(asset["elements"])
    w, h = int((x1 - x0) * SS) + 2, int((y1 - y0) * SS) + 2
    cv = paint.Canvas(w, h, background="#ff00ff", seed=name, boil=0.0, wobble=0.0)
    tf = paint.Transform(x=-x0 * SS, y=-y0 * SS, scale=SS)
    paint.draw_elements(cv, asset["elements"], tf, seed=name)
    a = np.asarray(cv.img.convert("RGB"))
    keyed = (a[..., 0] > 245) & (a[..., 1] < 10) & (a[..., 2] > 245)   # paint draws aliased, so the key is exact
    rgba = np.dstack([a, np.where(keyed, 0, 255).astype(np.uint8)])
    rgba[keyed, :3] = 0          # no magenta fringe when the edges are averaged
    img = Image.fromarray(rgba, "RGBA").reduce(SS)
    return img, (-x0, -y0)


@lru_cache(maxsize=512)
def sprite(name, scale, flip=False):
    """(RGBA image, origin) at `scale` px per asset unit, like toon.sprite."""
    img, (ox, oy) = _master(name)
    w, h = max(1, int(img.width * scale)), max(1, int(img.height * scale))
    out = img.resize((w, h), Image.LANCZOS)
    if flip:
        out = out.transpose(Image.FLIP_LEFT_RIGHT)
        ox = img.width - ox
    return out, (ox * scale, oy * scale)


def find(words):
    hits = []
    for p in sorted(paint.LIBRARY_DIR.glob("*.json")):
        try:
            a = json.loads(p.read_text(encoding="utf-8"))
        except ValueError:
            continue
        text = " ".join([p.stem, a.get("description", ""), " ".join(a.get("tags", []))]).lower()
        if all(w.lower() in text for w in words):
            hits.append((p.stem, a.get("description", "")[:110]))
    return hits


if __name__ == "__main__":
    if sys.argv[1] == "find":
        for n, d in find(sys.argv[2:]):
            print(f"{n:32} {d}")
