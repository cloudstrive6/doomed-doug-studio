# Doomed Doug: art bible

Owned by the art director. Style: **MS Paint, crude on purpose, readable instantly.** Aliased edges, flat
colours, bucket fills, spray-can glow, slight hand wobble, 3-drawing "boil" loop at 8 fps.

## Palette
| Use | Hex |
|---|---|
| Ink (outlines) | `#000000` (auto `#ffffff` for Doug on dark backgrounds) |
| Doug's cap | `#e0201b` |
| Sky | `#8fd3ff` |
| Sun / glow / lures | `#ffe24a`, `#fff36b`, spray `#fff7a0` |
| Sand / wood | `#e8c07a` / `#a0522d` |
| Danger red / blood-free "ouch" | `#7a0d0d` (mouths), never pools of blood |
| Labels | white box `#ffffff`, black text |

### Ocean depth ramp (use these exact colours so every ocean video matches)
| Zone | Depth | Colour |
|---|---|---|
| Surface / sunlight | 0–200 m | `#3a9ad9` |
| Twilight | 200–1,000 m | `#1b4f86` |
| Midnight | 1,000–4,000 m | `#0b2447` |
| Abyss | 4,000–6,000 m | `#050a1f` |
| Hadal / trenches | 6,000 m+ | `#020308` |

Other environments: lava `#ff5a1f`/`#ffb000`, rock `#6b5b4b`, jungle `#2e8b3a`/`#1d5e27`, ice `#dff4ff`,
desert `#f2c77a`, gut/flesh interiors (parasites) `#e79aa0` (cartoon pink, never realistic).

## Two-tier rendering (style bible 4.3)
- **Doug and humans: crude** MS Paint stick men: uniform thin lines (Doug's rig: 5 at scale 1 ≈ 4–5 px), big round
  head with grey shading crescent, oval eyes, meme faces.
  Human-tier library assets (e.g. `scientist`, `diver`) set `"auto_ink": true` so their black outlines flip to
  white on dark backgrounds, exactly like Doug; face and costume details inside white shapes carry
  `"keep_ink": true` so they stay black.
- **Costumes/props worn over Doug** (e.g. `squid_costume`) are props, not design changes: they sit on top of the rig
  at the same x/y/scale, and must leave Doug's head, face and red cap fully visible. Use upright poses only.
- **Creatures and places: the detailed tier**: cleaner cartoon illustrations with layered fills, interior shading
  (`spray`, darker back / lighter belly), texture strokes at 2–3, outlines 3–5. The contrast is part of the joke.

## Screen furniture
Caption bar (automatic) · `wordart` keyword labels (yellow→green gradient, 1–4 words, max 2 on screen) · red curved
arrows · red ? and ! · warning triangle · red X · thermometer · dotted distance lines · silhouette + red glow for
reveals · real photos only public-domain/licensed with a 4 px black frame.

## Text
Font: Arimo (bundled, Arial look-alike = classic MS Paint text). `label` boxes for depths, names and numbers.
Max ~8 words on screen per shot. Title cards: big bold red `#e0201b` with black outline (like the banner).

## Recurring layouts
- **Depth meter**: tall canvas + `pan_down`, zone bands, white `label` depth markers at left.
- **Death counter**: `label` "DOUG DEATHS: N" top-right, appears on each death shot. Its zone (about
  x 1300-1860, y 110-230 at 1080p) is reserved: no sun, moon, creature or other label may touch it. On death
  shots, move the sun/moon down to about (1720, 330) or drop it.
- **WordArt placement**: the yellow-to-green `wordart` must never sit on green ground, grass, leaves or any
  green field (lime-on-lime disappears at phone size). Put it on sky/cream/pink/dark areas; if the only free
  space is ground, move the label up instead.
- **Stop title card**: zone/creature name as a big `label` + Doug reacting.
- **Scale comparison**: Doug next to the creature, both at true relative size, a `label` with the size.

## Never
Realistic gore, blood pools, exposed organs, dismemberment; realistic (non-MS-Paint) art; changing Doug's design;
cutesy nursery look (pastel baby style, "kids" framing).
