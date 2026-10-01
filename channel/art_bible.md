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
  at the same x/y/scale, and must leave Doug's head, face and red cap fully visible. Use upright poses, except
  for a death beat: Doug uses `pose: "on_back"` (no `rotate`) and the prop keeps `rotate: -90` at Doug's x/y
  (003: `snorkel_gear`, `ammonite_costume_flat`; shift a torso costume +30 x scale in x so it clears the cap brim).
  Anything the prop carries on Doug's back (shells, tanks) then points *down*, so keep Doug high enough that it
  stays in frame.
- **Death pose (from 003)**: `pose: "on_back"`, `expression: "dead"`, never `rotate`. Body flat, head near-upright
  facing the sky, red cap on (or `gear: ["cap_off"]` for the cap knocked off beside his head). `lie` + `rotate: -90`
  is retired for new shots: it turns the cap into a red half-head and the body into a fan of whiskers. Only
  001/002 still use it, and their renders are kept pixel-identical.
- **Creatures and places: the detailed tier**: cleaner cartoon illustrations with layered fills, interior shading
  (`spray`, darker back / lighter belly), texture strokes at 2–3, outlines 3–5. The contrast is part of the joke.

## Screen furniture
Caption bar (automatic) · `wordart` keyword labels (yellow→green gradient, 1–4 words, max 2 on screen) · red curved
arrows · red ? and ! · warning triangle · red X · thermometer · dotted distance lines · silhouette + red glow for
reveals · real photos only public-domain/licensed with a 4 px black frame.

**Silhouette glow sizing.** The engine sprays the glow as a disc at the asset's *anchor* with radius
`glow_r x scale`, drawn behind the black shape. So:
- `glow_r` must be larger than the drawing's half-width (rule of thumb: about 0.7 x the asset's local width, e.g.
  asteroid 400 wide → 280, dunkleosteus 600 → 420), or the glow hides entirely behind the silhouette.
- Bottom-anchored assets (feet on the ground) put the glow centre at the feet: half of it lands on the ground.
  Prefer a centre-anchored asset, or skip `glow` and add a `spray` at the body centre yourself.
- Leaving out `glow` does **not** turn the glow off: every `silhouette: true` gets a default red glow
  (`glow_r` 260) at the anchor. To use your own body-centre `spray` instead, set `"glow_r": 0` on the silhouette.
- Spray is speckle, so a later ground `poly` does not cover it (the bucket fill skips the speckles). To keep a
  glow off the ground, put a flat ground-colour `rect` after the spray, starting at the ground line, then re-add
  the ground texture spray (see 003 s146).
- A small `scale` needs a bigger `glow_r`: the visible ring is `glow_r x scale` minus the drawing's half-width.
- Never put the colour reveal in the same shot on top of a glowing silhouette: the leftover red spray peeks out
  under the creature and reads as a blood puddle. Silhouette in one shot, colour in the next (1-3 beats later).

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
- **Time machine** (`time_machine`, from 003, time-travel episodes only): teal booth (`#2a9d8f`, dark `#1b6f66`),
  cream `TIME` sign, door open to the right (to x +330), mid-grey interior (`#8d9096`, kept mid so Doug's black lines
  read). Anchor bottom-centre on the ground; flat roof top at y=-640 (props on the roof go at ground - 640 x scale).
  Doug inside: draw Doug after the booth at the booth's x, feet at ground-8, Doug scale = 0.75 x booth scale.
  Keep wordart and labels off the open door (x +180..+330 x scale).

## Doug gear (art director only)
`scuba`, `mask`, `tank`, `helmet`, `sweat`, `sunburn` (003): head fill `#ff8a7a`, crescent `#e0665a` (same shape),
arm lines `#e0201b`, three tiny white peel flakes on the front of the face. Cap, eyes, head shape and legs unchanged.

## Never
Realistic gore, blood pools, exposed organs, dismemberment; realistic (non-MS-Paint) art; changing Doug's design;
cutesy nursery look (pastel baby style, "kids" framing).
