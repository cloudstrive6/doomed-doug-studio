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
  stays in frame. **When you move Doug, move every worn prop with him** (`flip_flops`, `zapped_hair`, costumes):
  same x/y/scale, every time (004 s104: Doug was lowered, the flip-flops stayed behind on his shins).
- **Planted props (flags, poles, signs) touch the ground**: end the pole on the surface line, never in the air
  beside a slope (004 s146: the summit flag floated about 80 px above the slope).
- **Death pose (from 003)**: `pose: "on_back"`, `expression: "dead"`, never `rotate`. Body flat, head near-upright
  facing the sky, red cap on (or `gear: ["cap_off"]` for the cap knocked off beside his head). `lie` + `rotate: -90`
  is retired for new shots: it turns the cap into a red half-head and the body into a fan of whiskers. Only
  001/002 still use it, and their renders are kept pixel-identical.
- **Doug's `y` is his hip, not his feet** (from 004). Feet are at y + 152 x scale, neck at y - 150 x scale (the
  `sit` pose drops the hip by 70 x scale). Aim flip-flop arrows at the feet, not at y + 200.
- **Capless upright Doug (from 008)**: `gear: ["cap_off"]` on any non-`on_back` pose simply omits the cap (nothing
  drawn on the ground); head and face unchanged. The cap is his signature, so this is **only for approved one-off
  exceptions logged in the episode's `decisions.md`** (008 close: tiny capless Doug waving while an orca wears the cap).
- **Thumbs up (from 005)**: use `pose: "thumbs_up"` (standing) or `"sit_thumbs_up"` (seated, same hip drop as `sit`).
  The hand point is local (+112, -156) x scale, with the thumb tip about 42 x scale above it, so aim arrows there. Never paste a
  separate hand prop next to Doug, because it reads as off-model. A seated Doug must sit *on* something: put the
  surface at y + 70 x scale.
- **Buried / sinking Doug (quicksand, mud, water; from 004 s063)**: draw Doug, then the ground `rect` starting
  **exactly at his hip y**, then (optionally) cross-section leg lines from the hip down. Torso, arms, head and cap
  stay above the surface. Never put the surface above the hip: a head on two legs with no torso is off-model.
- **Auto-ink is decided at one point** (80 x scale above the hip). If Doug straddles a dark sky and a light ground
  (snow, salt, crystal), his legs go white-on-white and vanish (004 s103, s171-s173, s183). Keep the whole body on
  one side of the horizon (lower him so his neck is below the ground line), or sit him *behind* a light prop (draw
  Doug before the prop, hips at its top edge) so only the torso shows against the dark.
- **Dark backdrop prop behind Doug on light ground** (bridge, building, cliff): the auto-ink point can land on the
  prop and turn Doug white, so his legs vanish on the snow or ice (007 s036-s051). Set `"ink": "#000000"` on the `doug`.
- **No floating Doug**: if the shot has a ground, dam, bank or sea surface, his feet go on it (hip = surface -
  152 x scale; swimmers sit at the water line). Doug only floats in empty diagram or space backgrounds, or as a ghost.
- **Cover rects** that hide an earlier Doug must stop above the ground line, or they cut a notch into the horizon (007 s238).
- **Props on humans** (medals, badges) hang on the chest (below neck y), never over the face (007 s120).
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
One exception: a sombre item about a real mass-casualty event (004 Lake Nyos) may use a white `#ffffff` title
with black outline. No other colours (no yellow, no green) for item title cards.
Wordart and title text must not cross a map frame line, land masses, crystals or lightning bolts; find clear sky/sea.
On full-width maps there is no clear band below the frame: shrink the map (about 0.8-0.9) and raise it, then put the
wordart in the freed strip, or use a short word in the side margin (007: 9 map shots failed this). Tall props (trees,
towers, fishing rods) must stay below the chapter top bar.

## Recurring layouts
- **Depth meter**: tall canvas + `pan_down`, zone bands, white `label` depth markers at left.
- **Death counter**: `label` "DOUG DEATHS: N" top-right, appears on each death shot. Its zone (about
  x 1300-1860, y 110-230 at 1080p) is reserved: no sun, moon, creature, tree crown, arrow or other label may touch it. On death
  shots, move the sun/moon down to about (1720, 330) or drop it. This applies to **every** shot that shows the
  counter, including survival beats and title cards that carry the counter over (004 s222 moon at 1650,200).
- **Ground texture lines** (lava crust, cracks) must not pass behind Doug's shoulders or hips: they read as extra
  arms or a skewer (004 s273-s277).
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
