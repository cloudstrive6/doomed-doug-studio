"""Thumbnails for the What If pilot, drawn with the toon engine (1280x720). Three concepts for the packaging gate:
  A  smug Doug waist-deep in his pool, a huge megalodon rising behind him
  B  growth split: DAY 1 pup in the pool | DAY 12 the shark too big for the pool, water spilling
  C  Doug in the pool with the pup while the influencer neighbour films in shock
  py -m studio.whatif_thumb <pilot_dir> [labelA] [labelB] [labelC]
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

from . import toon as T
from . import toon_held as HP
from . import toon_props as P
from . import toon_sets as S

TW, TH = 1280, 720
NAVY, RED, YEL = "#1e2a44", "#e0201b", "#f6b73c"


def _bg(set_id, cx, cy, z):
    bg = S.background(set_id)
    k = bg.width / 1920
    bw, bh = 1920 / z * k, 1080 / z * k
    x0 = min(max(0, (cx - 960 / z) * k), bg.width - bw)
    y0 = min(max(0, (cy - 540 / z) * k), bg.height - bh)
    return bg.resize((TW, TH), Image.LANCZOS, box=(x0, y0, x0 + bw, y0 + bh)).convert("RGBA")


def _label(img, text, x, y, size=150, rot=-5, col=YEL, stroke=NAVY):
    lay = Image.new("RGBA", (TW * 2, 400), (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    f = T.font(size, "Bangers-Regular")
    d.text((40, 200), text, font=f, fill=T.rgba(col), anchor="lm", stroke_width=max(6, size // 14), stroke_fill=T.rgba(stroke))
    lay = lay.crop(lay.getbbox()).rotate(rot, resample=Image.BICUBIC, expand=True)
    sh = Image.new("RGBA", lay.size, (0, 0, 0, 0))
    sh.putalpha(lay.getchannel("A").point(lambda v: int(v * 0.45)))
    sh = sh.filter(ImageFilter.GaussianBlur(6))
    img.alpha_composite(sh, (int(x) + 8, int(y) + 10))
    img.alpha_composite(lay, (int(x), int(y)))


def _arrow(img, p0, p1, col=RED, w=26):
    lay = Image.new("RGBA", (TW * 2, TH * 2), (0, 0, 0, 0))
    p = T.Pen(lay, 0, 0, 2)
    p.line([p0, p1], T.INK, w + 10)
    p.line([p0, p1], col, w)
    a = math.atan2(p1[1] - p0[1], p1[0] - p0[0])
    hd = [(p1[0] + math.cos(a) * 30, p1[1] + math.sin(a) * 30),
          (p1[0] + math.cos(a + 2.4) * 70, p1[1] + math.sin(a + 2.4) * 70),
          (p1[0] + math.cos(a - 2.4) * 70, p1[1] + math.sin(a - 2.4) * 70)]
    p.poly(hd, col, ow=6)
    img.alpha_composite(lay.reduce(2))


def _char(img, look, pose, scale, at, flip=False, holds=None, **face):
    extra = [HP.HELD[holds]] if holds else []
    spr, org = T.sprite(lambda p: T.draw_character(p, look, T.POSES[pose], extra_props=extra, **face),
                        (-260, -520, 520, 230), scale, flip)
    T.paste(img, spr, org, at)


def _meg(img, scale, at, flip=False, rot=0, **kw):
    spr, org = T.sprite(lambda p: P.draw_megalodon(p, **kw), P.MEG_BBOX, scale, flip)
    if rot:
        spr = spr.rotate(rot, resample=Image.BICUBIC, expand=True)
        org = (spr.width / 2, spr.height / 2)
    T.paste(img, spr, org, at)


def _water(img, y, alpha=255, h=None):
    h = TH - y if h is None else h
    w = Image.new("RGBA", (TW, h), (79, 192, 236, alpha))
    d = ImageDraw.Draw(w)
    for i in range(14):
        x = (i * 97) % TW
        yy = 30 + (i * 53) % max(40, h - 40)
        d.line([(x, yy), (x + 60, yy)], fill=(255, 255, 255, 170), width=7)
    d.line([(0, 0), (TW, 0)], fill=T.INK, width=6)
    img.alpha_composite(w, (0, y))


def concept_a(looks, label="MY PET"):
    img = _bg("backyard", 960, 560, 1.25)
    _meg(img, 1.95, (860, 330), flip=True, rot=-20, t=0.4, swim=0.2, jaw=1.0, mood="hungry")
    _water(img, 560)
    _char(img, looks["doug"], "thumbs", 1.75, (290, 690), eyes="half", brows="smug", mouth="smirk")
    _water(img, 640, alpha=255)
    _label(img, label, 600, 520, 170, rot=-5)
    return img


def concept_b(looks, label="DAY 12"):
    def half(meg_kw, doug_pose, face, cx_meg, cx_doug):
        im = _bg("backyard", 900, 700, 1.5)
        im.alpha_composite(Image.new("RGBA", (TW, TH - 470), (79, 192, 236, 255)), (0, 470))
        _meg(im, meg_kw.pop("scale"), (cx_meg, meg_kw.pop("y")), **meg_kw)
        _char(im, looks["doug"], doug_pose, 0.85, (cx_doug, 330), flip=True, **face)
        return im.crop((TW // 4, 0, TW // 4 + TW // 2, TH))
    img = Image.new("RGBA", (TW, TH))
    img.paste(half(dict(scale=0.75, y=560, mood="happy", pup=1.0, t=0.2), "cheer1",
                   dict(eyes="happy", brows="up", mouth="grin"), 620, 800), (0, 0))
    img.paste(half(dict(scale=2.1, y=560, flip=True, jaw=0.6, mood="curious", pup=0.6, t=0.6), "panic1",
                   dict(eyes="wide", brows="worry", mouth="o"), 610, 860), (TW // 2, 0))
    d = ImageDraw.Draw(img, "RGBA")
    d.line([(TW // 2, 0), (TW // 2, TH)], fill=T.rgba("#ffffff"), width=14)
    d.line([(TW // 2, 0), (TW // 2, TH)], fill=T.INK, width=5)
    _label(img, "DAY 1", 40, 24, 130, rot=-4)
    _label(img, label, 700, 24, 130, rot=4, col="#ffffff", stroke=RED)
    return img


def concept_c(looks, label="IT'S A BABY"):
    img = _bg("backyard", 1000, 600, 1.3)
    _water(img, 520)
    _meg(img, 1.35, (520, 620), mood="happy", pup=1.0, t=0.1, swim=0.1)
    _char(img, looks["doug"], "hold", 1.05, (300, 640), eyes="happy", brows="up", mouth="grin")
    _water(img, 610, alpha=255)
    _char(img, looks["tanner"], "panic1", 1.0, (1090, 400), flip=True, holds="phone_ring", eyes="wide", brows="up", mouth="o")
    _label(img, label, 420, 24, 140, rot=-4)
    return img


def _prop(img, pid, scale, at, flip=False, rot=0, **kw):
    if pid.startswith("lib:"):
        from . import toon_lib
        spr, org = toon_lib.sprite(pid[4:], scale, flip)
        if rot:
            spr = spr.rotate(rot, resample=Image.BICUBIC, expand=True)
            org = (spr.width / 2, spr.height / 2)
        T.paste(img, spr, org, at)
        return
    fn, bbox = P.PROP_DRAW.get(pid, (None, None))
    if fn is None:
        fn, bbox = S.EXTRA_PROPS.get(pid, (None, None))
    if fn is None:
        raise SystemExit(f"thumbs.json: unknown prop '{pid}'")
    spr, org = T.sprite(lambda p: fn(p, **kw), bbox, scale, flip)
    if rot:
        spr = spr.rotate(rot, resample=Image.BICUBIC, expand=True)
        org = (spr.width / 2, spr.height / 2)
    T.paste(img, spr, org, at)


def _layers(img, layers, looks):
    for L in layers:
        k = dict(L)
        t = k.pop("type")
        if t == "char":
            who = k.pop("who")
            _char(img, looks[who], k.pop("pose", "stand"), k.pop("scale", 1.0), tuple(k.pop("at")), k.pop("flip", False),
                  k.pop("holds", None), **k)
        elif t == "meg":
            _meg(img, k.pop("scale", 1.0), tuple(k.pop("at")), k.pop("flip", False), k.pop("rot", 0), **k)
        elif t == "prop":
            _prop(img, k.pop("id"), k.pop("scale", 1.0), tuple(k.pop("at")), k.pop("flip", False), k.pop("rot", 0), **k)
        elif t == "water":
            _water(img, k["y"], k.get("alpha", 255), k.get("h"))
        elif t == "tint":
            img.alpha_composite(Image.new("RGBA", img.size, tuple(k["rgba"])))
        elif t == "label":
            _label(img, k["text"], k["x"], k["y"], k.get("size", 150), k.get("rot", -5), k.get("col", YEL), k.get("stroke", NAVY))
        elif t == "arrow":
            _arrow(img, tuple(k["p0"]), tuple(k["p1"]), k.get("col", RED))
        else:
            raise SystemExit(f"thumbs.json: unknown layer type '{t}'")


def from_spec(spec, looks):
    """One thumbnail from a JSON spec. Either a single scene:
      {"set": "backyard", "cam": [cx, cy, zoom], "layers": [...]}
    or a before/after split: {"split": [<half spec>, <half spec>], "layers": [labels drawn over the whole image]}.
    Layer types: char (who, pose, scale, at [x, y], flip, holds, eyes, brows, mouth), meg (scale, at, flip, rot, jaw,
    mood, pup, t, swim), prop (id, scale, at, flip, rot), water (y, alpha, h), tint (rgba), label (text, x, y, size,
    rot, col, stroke), arrow (p0, p1, col). Coordinates are on the 1280x720 canvas."""
    if "split" in spec:
        img = Image.new("RGBA", (TW, TH))
        for i, half in enumerate(spec["split"][:2]):
            im = _bg(half["set"], *half.get("cam", [960, 540, 1.3]))
            _layers(im, half.get("layers", []), looks)
            img.paste(im.crop((TW // 4, 0, TW // 4 + TW // 2, TH)), (i * TW // 2, 0))
        d = ImageDraw.Draw(img, "RGBA")
        d.line([(TW // 2, 0), (TW // 2, TH)], fill=T.rgba("#ffffff"), width=14)
        d.line([(TW // 2, 0), (TW // 2, TH)], fill=T.INK, width=5)
    else:
        img = _bg(spec["set"], *spec.get("cam", [960, 540, 1.25]))
    _layers(img, spec.get("layers", []), looks)
    return img


def main(pdir: Path, labels):
    raw = json.loads((pdir / "cast_looks.json").read_text(encoding="utf-8"))
    looks = {k: T.Look(**{a: b for a, b in v.items() if not a.startswith("_")}) for k, v in raw.items()}
    looks.setdefault("doug", T.CAST_LOOKS["doug"])
    out = pdir / "thumbs"
    out.mkdir(exist_ok=True)
    stg = pdir / "staging.json"
    if stg.exists():
        S.register_aliases(json.loads(stg.read_text(encoding="utf-8")).get("aliases", {}))
    if (pdir / "thumbs.json").exists():   # CI episodes: three variants described as data
        specs = json.loads((pdir / "thumbs.json").read_text(encoding="utf-8"))
        fns = {n: (lambda s=specs[n]: from_spec(s, looks)) for n in "ABC"}
    else:                                 # pilot w01 concepts
        la = labels + [None] * 3
        fns = {"A": lambda: concept_a(looks, la[0] or "MY PET"), "B": lambda: concept_b(looks, la[1] or "DAY 12"),
               "C": lambda: concept_c(looks, la[2] or "IT'S A BABY")}
    for name, fn in fns.items():
        im = fn().convert("RGB")
        im.save(out / f"thumb_{name}.png")
        im.resize((320, 180), Image.LANCZOS).save(out / f"thumb_{name}_small.png")
    sheet = Image.new("RGB", (1280, 720 + 180), (20, 20, 24))
    for i, n in enumerate("ABC"):
        sheet.paste(Image.open(out / f"thumb_{n}.png").resize((640, 360)), ((i % 2) * 640, (i // 2) * 360))
        sheet.paste(Image.open(out / f"thumb_{n}_small.png"), (i * 330, 720))
    sheet.save(out / "sheet.jpg", quality=88)
    print("thumbs written to", out)


if __name__ == "__main__":
    main(Path(sys.argv[1]).resolve(), sys.argv[2:])
