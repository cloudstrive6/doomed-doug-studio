"""Held props (drawn at a character's front hand) and world props for What If w01. Importing this registers the world
props in toon_props.PROP_DRAW."""
from __future__ import annotations

import math
import random

from .toon import INK, shade, tint
from .toon_props import MEG_BBOX, PROP_DRAW, bucket, draw_megalodon, fish


# ------------------------------------------------------------------ held props (character local units, h = hand point)

def _torch(p, h):
    x, y = h
    p.poly([(x + 6, y - 30), (x + 300, y - 140), (x + 300, y + 60), (x + 6, y - 6)], (255, 245, 170, 80), ow=0)
    p.rrect(x - 10, y - 28, 30, 18, 5, "#f5c842", ow=3)


def _phone_ring(p, h):
    x, y = h
    p.line([(x, y), (x + 40, y - 120)], "#2a2a33", 7)
    p.circle(x + 46, y - 150, 34, None, ow=9, ink="#ffffff")
    p.circle(x + 46, y - 150, 34, None, ow=3)
    p.rrect(x + 32, y - 172, 28, 46, 5, "#1e1d26", ow=2.5)
    p.circle(x + 52, y - 164, 4, "#e0201b", ow=0)


def _clipboard(p, h):
    x, y = h
    p.rrect(x - 26, y - 70, 54, 72, 4, "#a8744a", ow=3)
    p.rrect(x - 20, y - 62, 42, 58, 2, "#ffffff", ow=0)
    for i in range(4):
        p.line([(x - 14, y - 52 + i * 12), (x + 14, y - 52 + i * 12)], "#9aa3b2", 2, caps=False)


def _fish_rod(p, h):
    x, y = h
    tip = (x + 170, y - 190)
    p.line([(x - 20, y + 20), tip], "#3a2a1a", 6)
    p.line([tip, (tip[0] + 10, tip[1] + 150)], "#ffffff", 2, caps=False)
    p.push(tip[0] + 10, tip[1] + 170, rot=90)
    fish(p, "#c8d6e0", 0.8)
    p.pop()


def _bucket(p, h):
    x, y = h
    p.push(x, y + 70, scale=0.55)
    bucket(p, "#f4f6fa", full="water")
    p.pop()


def _tin(p, h):
    x, y = h
    p.rrect(x - 16, y - 34, 32, 34, 4, "#c8c8d0", ow=3)
    p.ellipse(x, y - 34, 16, 5, "#8a3b2a", ow=2.5)


def _contract(p, h):
    x, y = h
    p.poly([(x - 30, y - 80), (x + 30, y - 84), (x + 34, y - 4), (x - 26, y)], "#ffffff", ow=3)
    p.text(x + 2, y - 66, "DEAL", 13, INK, "RussoOne-Regular")
    p.curve([(x - 16, y - 24), (x, y - 34), (x + 16, y - 20)], "#f28c28", 4, n=4)


def _melon_stick(p, h):
    x, y = h
    tip = (x + 300, y - 120)
    p.line([(x - 10, y + 6), tip], "#2a2a33", 7)
    p.ellipse(tip[0] + 30, tip[1], 44, 34, "#3f9a4a")
    for i in range(-2, 3):
        p.curve([(tip[0] + 30 + i * 14, tip[1] - 30), (tip[0] + 32 + i * 16, tip[1]), (tip[0] + 30 + i * 14, tip[1] + 30)],
                "#2a6a32", 3, n=4)


def _handle(p, h):
    x, y = h
    p.line([(x - 10, y + 6), (x + 60, y - 24)], "#2a2a33", 7)


def _envelope(p, h):
    x, y = h
    for i in range(3):
        p.rrect(x - 30 + i * 6, y - 74 + i * 4, 60, 26, 3, "#7cc47a", ow=2.5)
    p.rrect(x - 40, y - 52, 80, 52, 4, "#f2e3c6", ow=3)


def _net(p, h):
    x, y = h
    top = (x + 140, y - 330)
    p.line([(x - 40, y + 60), top], "#8a6a44", 8)
    p.ellipse(top[0] + 10, top[1] - 50, 70, 55, None, ow=6)
    for i in range(-2, 3):
        p.line([(top[0] + 10 + i * 24, top[1] - 100), (top[0] + 10 + i * 24, top[1])], (255, 255, 255, 180), 2, caps=False)


def _fish(p, h):
    x, y = h
    p.push(x + 10, y - 8, rot=-30)
    fish(p, "#c8d6e0", 0.7)
    p.pop()


def _basket(p, h):
    x, y = h
    p.poly([(x - 30, y - 20), (x + 110, y - 20), (x + 96, y + 36), (x - 16, y + 36)], "#e8e8ea", ow=3)
    rr = random.Random(3)
    for i in range(16):
        tx, ty = x - 14 + rr.uniform(0, 110), y - 26 + rr.uniform(-8, 10)
        p.poly([(tx - 6, ty + 4), (tx + 6, ty + 4), (tx, ty - 10)], "#ffffff", ow=1.6)


def _paddle(p, h):
    x, y = h
    p.line([(x - 90, y + 50), (x + 90, y - 50)], "#3a3a44", 7)
    p.ellipse(x + 110, y - 62, 30, 13, "#f28c28", rot=-30)
    p.ellipse(x - 110, y + 62, 30, 13, "#f28c28", rot=-30)


def _crayon(p, h):
    x, y = h
    p.line([(x, y), (x + 20, y - 40)], "#f28c28", 9)


HELD = {"torch": _torch, "phone_ring": _phone_ring, "clipboard": _clipboard, "fish_rod": _fish_rod, "bucket": _bucket,
        "tin": _tin, "contract": _contract, "melon_stick": _melon_stick, "handle": _handle, "envelope": _envelope,
        "net": _net, "fish": _fish, "basket": _basket, "paddle": _paddle, "crayon": _crayon}


# ------------------------------------------------------------------ world props

def kayak(pen, col="#f28c28"):
    pen.blob([(-330, -10), (-200, -34), (200, -34), (340, -12), (250, 30), (-240, 30)], col)
    pen.blob([(-300, -14), (-200, -30), (200, -30), (310, -14), (200, -6), (-200, -6)], shade(col, 0.8), ow=0)
    pen.blob([(-330, -10), (-200, -34), (200, -34), (340, -12), (250, 30), (-240, 30)], None)


def ute(pen, col="#f4f6fa"):
    pen.rrect(-320, -150, 300, 150, 18, col)
    pen.rrect(-300, -130, 120, 70, 8, "#8fd3ff", ow=3)
    pen.poly([(-20, -70), (330, -70), (330, 0), (-20, 0)], col)
    pen.poly([(-320, -40), (330, -40), (330, -22), (-320, -22)], "#2f6fd0", ow=2.5)
    pen.text(-170, -90, "FISHERIES", 26, "#1e3a5a", "RussoOne-Regular")
    for wx in (-230, 220):
        pen.circle(wx, 10, 44, "#2a2a33")
        pen.circle(wx, 10, 18, "#9a9aa6", ow=3)


def fish_truck(pen):
    pen.rrect(-330, -210, 420, 200, 18, "#dfe6ee")
    pen.rrect(-318, -198, 396, 176, 14, "#4fa7e0", ow=3)
    for i in range(5):
        pen.line([(-300 + i * 80, -160), (-260 + i * 80, -160)], (255, 255, 255, 170), 5)
    pen.text(-120, -100, "FISH TRANSPORT", 30, "#ffffff", "RussoOne-Regular", stroke=2)
    pen.rrect(100, -150, 170, 150, 20, "#f4f6fa")
    pen.rrect(170, -134, 80, 56, 8, "#8fd3ff", ow=3)
    for wx in (-230, 180):
        pen.circle(wx, 10, 42, "#2a2a33")
        pen.circle(wx, 10, 17, "#9a9aa6", ow=3)


def deckchair(pen, col="#3fa0d8"):
    pen.line([(-120, 0), (60, -150)], "#8a6a44", 9)
    pen.line([(120, 0), (-40, -100)], "#8a6a44", 9)
    pen.poly([(-110, -60), (100, -60), (80, -36), (-120, -36)], col, ow=3)
    pen.poly([(40, -150), (90, -150), (110, -60), (60, -60)], col, ow=3)


def sand_pile(pen):
    pen.blob([(-200, 20), (-120, -40), (0, -70), (130, -40), (210, 20)], "#ecd08a")
    pen.line([(60, -70), (120, -150)], "#3a7ad0", 7)
    pen.poly([(30, -60), (90, -60), (80, -20), (40, -20)], "#3a7ad0", ow=3)


def fridge(pen, open_=True):
    pen.rrect(-150, -560, 300, 560, 18, "#eef2f6")
    if open_:
        pen.rrect(-136, -540, 272, 520, 10, "#dde8f2", ow=3)
        for i in range(3):
            pen.line([(-136, -400 + i * 130), (136, -400 + i * 130)], "#b8c6d4", 5, caps=False)
        pen.poly([(150, -560), (330, -520), (330, -40), (150, 0)], "#e6ecf2")
    pen.circle(0, -500, 18, "#fff6c9", ow=0)


def receipts(pen):
    pts = [(-200 + i * 40, -10 - 30 * math.sin(i * 1.3)) for i in range(11)]
    pen.curve(pts, INK, 30)
    pen.curve(pts, "#ffffff", 24)
    for x, y in pts[1:-1:2]:
        pen.line([(x - 8, y), (x + 8, y)], "#9aa3b2", 2, caps=False)


def coast_map(pen):
    pen.rrect(-200, -140, 400, 280, 4, "#f4ecd6")
    pen.blob([(-200, -140), (-40, -140), (-10, -40), (-60, 60), (20, 140), (-200, 140)], "#cfe6a8", ow=3)
    pen.ellipse(-20, 20, 46, 34, None, ow=6, ink="#e0201b")
    pen.text(80, -100, "COAST", 26, INK, "RussoOne-Regular")


def great_white(pen, t=0.0):
    draw_megalodon(pen, t=t, swim=0.8, jaw=0.0, mood="hungry", pup=0.0, col="#7d8893")


def fish_school(pen, t=0.0):
    for i in range(9):
        x = -300 + i * 70 + math.sin(t * 3 + i) * 16
        y = math.sin(i * 1.7) * 60
        pen.push(x, y)
        fish(pen, "#c8d6e0", 0.6, t + i)
        pen.pop()


def lamp_post(pen):
    pen.limb([(0, 0), (0, -420)], 14, "#2a2a33")
    pen.circle(0, -430, 26, "#ffe9a0")


def rental_boat(pen):
    pen.blob([(-220, -20), (220, -30), (180, 40), (-190, 40)], "#d8dce2")
    pen.poly([(-215, -6), (215, -16), (208, 0), (-210, 8)], "#9aa3b2", ow=2.5)
    pen.rrect(-60, -12, 120, 34, 6, "#ffffff", ow=2.5)
    pen.text(0, 5, "RENTAL", 22, "#e0201b", "RussoOne-Regular")
    pen.rrect(150, -70, 40, 60, 6, "#2a2a33")


def sign_lagoon(pen):
    pen.limb([(-120, 0), (-120, -170)], 16, "#8a6a44")
    pen.limb([(120, 0), (120, -170)], 16, "#8a6a44")
    pen.rrect(-200, -300, 400, 150, 12, "#6b4a32")
    pen.text(0, -255, "GULL LAGOON", 40, "#ffe9a0", "RussoOne-Regular")
    pen.text(0, -195, "MARINE RESERVE", 30, "#ffffff", "RussoOne-Regular")


def counter(pen):
    pen.rrect(-420, -190, 840, 190, 10, "#a8744a")
    pen.rrect(-400, -175, 800, 90, 6, "#bfe8ff", ow=3)
    for i in range(5):
        pen.push(-320 + i * 150, -128)
        fish(pen, "#e0a040" if i % 2 else "#9fb7c8", 0.6)
        pen.pop()


def fossil_tooth(pen):
    from .toon_props import tooth
    tooth(pen, "#6b6f78", 0.5)


def buyer(pen):
    """Shadowy buyer silhouette for the flash forward."""
    pen.circle(0, -330, 64, "#22222c")
    pen.blob([(-80, -250), (80, -250), (100, 0), (-100, 0)], "#22222c")
    pen.ellipse(0, -390, 110, 18, "#22222c")
    pen.blob([(-60, -400), (-50, -470), (50, -470), (60, -400)], "#22222c")


PROP_DRAW.update({
    "kayak": (kayak, (-340, -40, 345, 35)),
    "ute": (ute, (-330, -160, 340, 60)),
    "fish_truck": (fish_truck, (-340, -220, 280, 60)),
    "deckchair": (deckchair, (-130, -160, 130, 10)),
    "sand_pile": (sand_pile, (-210, -160, 215, 25)),
    "fridge": (fridge, (-160, -570, 340, 10)),
    "receipts": (receipts, (-225, -60, 225, 40)),
    "coast_map": (coast_map, (-205, -145, 205, 145)),
    "great_white": (great_white, MEG_BBOX),
    "fish_school": (fish_school, (-360, -110, 330, 110)),
    "lamp_post": (lamp_post, (-30, -460, 30, 10)),
    "rental_boat": (rental_boat, (-225, -80, 225, 45)),
    "sign_lagoon": (sign_lagoon, (-205, -305, 205, 10)),
    "counter": (counter, (-425, -195, 425, 5)),
    "fossil_tooth": (fossil_tooth, (-40, -55, 40, 45)),
    "buyer": (buyer, (-115, -480, 115, 5)),
})
