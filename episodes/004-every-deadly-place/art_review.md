# Art review: 004 Every Deadly Place (new assets)

Reviewer: art director, 2026-10-01
Scope: all 39 new assets listed in `asset_requests.md`. Checked against `channel/art_bible.md` and style bible section 7.
Previews checked: `assets/previews/004-every-deadly-place-*.png` (overview, suitcase and stickers, worn, creatures,
places, props context sheets). I also re-rendered keyframes s002, s098, s169, s240 and s280 to check the assets in context.

## Verdict: PASS (APPROVED)

All 39 assets are approved. I fixed three small issues myself (listed below), so nothing goes back to the illustrator.
Two composition notes for the director don't block approval.

## Per-asset decisions

### Series lore (art-director owned)
| # | asset | decision | notes |
|---|---|---|---|
| 1 | travel_suitcase | APPROVE | Clearly distinct from `suitcase.json`: no tag, no sock, no straps. Face is plain, the 9 slots are clear and the bottom strip is free for the s282 arrow. The handle reads at 0.55. I adopt it as the `places` playlist standard prop. |
| 2 | sticker_death_valley | APPROVE | Legible at 0.5 and above. |
| 3 | sticker_snake_island | APPROVE | |
| 4 | sticker_morecambe_bay | APPROVE (fixed by AD) | The 13 px text was unreadable on the suitcase at 0.5 (s240). I widened the pennant to x -62..+66 and raised the text to 16 px. |
| 5 | sticker_antarctica | APPROVE (fixed by AD) | The 15 px one-line text was too small. I widened the oval to rx 64 x ry 32 and raised the text to 16 px. |
| 6 | sticker_everest | APPROVE | The peak icon touches the top of the text, but the text still reads. |
| 7 | sticker_naica | APPROVE | |
| 8 | sticker_dallol | APPROVE | |
| 9 | sticker_nyos | APPROVE | Plain dark-blue oval with no icon, as required for the sombre item. |
| 10 | sticker_nyiragongo | APPROVE | The NYIRA / GONGO split reads well. |

### Worn props and crude-tier humans
| # | asset | decision | notes |
|---|---|---|---|
| 11 | flip_flops | APPROVE | Sits under the stand-pose feet. |
| 12 | flip_flops_cracked | APPROVE | Faded, with readable cracks. |
| 13 | flamingo_costume | APPROVE | Head, face and red cap are fully visible, the flamingo head sits beside Doug's head, and the folded leg and zipper read (s098). |
| 14 | zapped_hair | APPROVE (placement checked) | Drawn for the sit-pose head at (0,-148). It lines up exactly in s240, with eyes, mouth and cap clear. Grey spikes are a deliberate choice: they read on both night sky and white backgrounds, where black spikes would vanish at night. For a standing Doug, offset y by -70 x scale. |
| 15 | cooling_suit | APPROVE (fixed by AD) | The torso was drawn over the sleeve ice-pack pouches and hid them. I spread the sleeves out to x about ±94 and re-centred the 4 pouches so they show (s169). Face and glasses stay visible. |
| 16 | sands_guide | APPROVE | Green cap (cannot be mistaken for Doug), wellies and staff. On-tier, and auto_ink works on dark backgrounds. |
| 17 | climber | APPROVE | Beanie, mask, hose and ice axe all read. The yellow O2 bottle is only a sliver beside the head but stays visible at 0.6. |

### Creatures
| # | asset | decision | notes |
|---|---|---|---|
| 18 | golden_lancehead | APPROVE | Clear raised head (good silhouette), eye stripe, vertical pupil and pale belly. No fangs. Reads at 0.22. |
| 19 | lesser_flamingo | APPROVE | Dark bill and crimson coverts. Works in flocks. |
| 20 | flamingo_chick | APPROVE | Grey down, straight dark bill. Documentary, not a mascot. |
| 21 | flamingo_nest | APPROVE | |
| 22 | jackal | APPROVE | The saddle reads. |
| 23 | stone_bird | APPROVE | Chalky, closed eye, not gory. |
| 24 | stone_bat | APPROVE | Same. |

### Places and props
| # | asset | decision | notes |
|---|---|---|---|
| 25 | ammonia_bottle | APPROVE | No brand. |
| 26 | research_hut | APPROVE | |
| 27 | sunscreen | APPROVE | |
| 28 | satellite | APPROVE | No logos. |
| 29 | helicopter | APPROVE | |
| 30 | gypsum_crystal | APPROVE | Reads well on the dark-brown cave and rotated (s169). |
| 31 | humidity_meter | APPROVE | |
| 32 | kitchen_timer | APPROVE | |
| 33 | magnifying_glass | APPROVE | The handle anchor lands in Doug's hand. |
| 34 | lemon | APPROVE | |
| 35 | soda_bottle | APPROVE | No label. |
| 36 | degassing_raft | APPROVE | Plain and factual, which suits the Nyos item. |
| 37 | storm_cloud | APPROVE | No bolts, with the inner glow. |
| 38 | fishing_rod | APPROVE | In context (s240) the rod clears Doug's face. |
| 39 | water_bottle | APPROVE | |

## Notes for the director (non-blocking, composition)
1. **Suitcase at scale 0.5 or less (e.g. s240):** the stickers read as colour patches, not words. That is fine for
   background lore. Where the script needs a sticker name read (pop-ins and s280-s282), keep the suitcase at 0.8 or more.
   s280 at 0.95 reads cleanly.
2. **s002 and other carry shots:** Doug's legs draw over the suitcase face, so it reads as "parked beside him" rather
   than "carried". Either draw the suitcase after Doug, or shift it about 40 px back so the handle meets the hand and the
   legs don't cross the case.

---

# Keyframe review: 004 Every Deadly Place

Reviewer: art director · 2026-10-01
Scope: all 282 keyframes (`build/contact/sheet_01..24.png`) and the thumbnail (`build/thumbnail.png`, `build/thumbnail_small.png`, also s001).
Cropped and zoomed: s011, s063, s103, s104, s171-s174, s183, s224, s225, s151, s162, s274. Test renders of my proposed fixes for
s063, s103, s147, s172 and s183 were made with `python -m studio art` (not committed). All four work as specified below.

## Verdict: FAIL (keyframes) · PASS (thumbnail)

Most of the episode is on-style and consistent. The two tiers hold (crude Doug against detailed snakes, flamingos, crystals,
volcano and storm clouds). Every segment frame has the caption bar. Each place keeps its own colour scheme from start to end
(Death Valley peach/sand, Snake Island sky/forest, Morecambe grey-blue/wet sand, Natron tan/brick, Antarctic navy/ice
`#dff4ff`, Everest cobalt, Naica dark brown (blue when flooded), Dallol cream/neon, Nyos night green, Maracaibo storm navy,
Nyiragongo black/lava `#ff5a1f`). The counter runs 27 to 36 with 9 deaths, and Natron and Maracaibo are survivals, as
scripted. Every ghost keeps the red cap. Nothing is gory: s094/s268 animals are chalky or tiny silhouettes, and s212 (Nyos)
shows no bodies, which is right. Annotation variety is good, and the split-screen s270-s272 and the suitcase sticker
payoff s280-s282 are strong.
It fails on three off-model or invisible Doug problems, one tier break, one counter-zone violation and a few small layout errors.

## Blocking fixes (director)

1. **s063, s064: Doug is buried to the neck and drawn as a head on two legs, with no torso or arms (off-model).**
   It also contradicts the science (s068: "sinks to about the waist"). Doug's `y` is his **hip**, so the sand `rect` must
   start at the hip. In both shots:
   - Change the sand `rect` from `y 600, h 480` to **`y 692, h 388`**.
   - Change the first point of the two black leg lines from `[870,600]` / `[930,600]` to **`[885,692]` / `[915,692]`**.
   Tested. Waist-deep, with the torso, arms and cap above the sand and the cross-section legs below.
2. **s103, s104: Doug's legs vanish on the snow.** Auto-ink samples the dark sky and draws white legs on `#dff4ff`.
   Lower Doug so his whole body is on the snow. Auto-ink then turns black.
   - s103: Doug **y 870**, suitcase **y 934**.
   - s104: Doug **y 880**, suitcase **y 950**.
   Tested (s103).
3. **s171, s172, s173: Doug's legs vanish on the crystal** (white ink on cream). Move the `doug` element so it comes
   **before** the `gypsum_crystal` element, and set Doug to **y 692**. He then sits on the beam with his shins hidden behind
   it, and his torso reads white against the dark wall. Keep the phone and timer after the crystal. Tested (s172).
4. **s183: Doug's sitting legs vanish on the salt flat** (same cause). Set Doug to **y 770**. Tested.
5. **s141, s142, s145-s150: the summit close-up is a flat one-colour triangle.** This breaks the detailed tier
   (style bible 7.1) and doesn't match the shaded `mount_everest` in s129-s140. In all 8 shots, insert these elements
   directly after the mountain `poly` (before the snowcap poly), then re-stroke the outline:
   ```json
   {"type":"poly","points":[[960,530],[1560,1120],[1180,1120],[1030,760],[1010,640]],"fill":"#5e5048","width":0,"outline":false},
   {"type":"spray","x":760,"y":900,"r":220,"color":"#a89a8a","density":0.05},
   {"type":"line","points":[[700,880],[760,860],[820,890]],"width":3,"color":"#6b5b4b"},
   {"type":"line","points":[[560,1010],[640,990],[700,1020]],"width":3,"color":"#6b5b4b"},
   {"type":"line","points":[[1150,900],[1230,880],[1290,910]],"width":3,"color":"#3e342c"},
   {"type":"poly","points":[[360,1120],[960,530],[1560,1120]],"fill":null,"width":6}
   ```
   Tested (s147). All 8 shots use the same triangle `[[360,1120],[960,530],[1560,1120]]`, so this block drops in unchanged.
6. **s222: the moon (circle at 1650,200) sits inside the reserved death-counter zone** and touches "DOUG DEATHS: 35".
   Move it to **(1720, 330)** or drop it.
7. **s273-s277: the lava crust line `[[300,760],[500,800],[700,770]]` runs right behind Doug** (x 600). It reads as
   arms 300 px long, or a skewer through his chest. In all 5 shots, move it to **`[[1150,960],[1350,1000],[1550,970]]`**
   (open lava, right of the rock shelf).
8. **s224: the "MOST LIGHTNING" wordart crosses the map's black frame line and lies on the green Arctic land.** Move it
   off the map, either into the light-blue margin (smaller map, scale 0.85, wordart above it) or onto open ocean. It must
   not touch the frame or land.
9. **s011, s101: the flip-flop arrows point at empty ground about 100-230 px below Doug's feet** (Doug's `y` is the hip,
   and his feet are at y + 152 x scale).
   - s011: first arrow `to` **[740, 830]**.
   - s101: arrow `to` **[790, 890]**.
10. **s223: the "LAKE MARACAIBO" title card is yellow.** Item title cards are red `#e0201b` with a black outline (art bible,
    Text). Change the text colour to **`#e0201b`**. Also nudge it to **y 760** so it clears the left bolt. (The white
    "LAKE NYOS" in s204 is accepted as the sombre-item exception, now written into the art bible.)

## Non-blocking (fix if touching the shot anyway)
11. **s151, s154, s162:** the title or wordart sits on the cream crystals (lime or red on cream). It is still legible, but
    move it into dark cave space. For s162, "REAL KILLER" could go to about x 1450, y 560.
12. **s225:** "ISN'T CLOSE" overlaps two yellow bolts. Move it to the lake band, about **x 1500, y 1000**.
13. **s213 -> s214:** these are back-to-back crater cross-sections, and s214 is s208 without arrows. Consider a different
    layout for s214, e.g. a rising CO2 gauge or a calendar with a growing bubble count.
14. **s231, s232:** the "SEA" is a tall blue slab that reads as a wall. A horizontal sea band on the right would read better.
15. **s105, s106:** Doug at scale 0.2 on the dome. His legs fade against the snow, but at that size it still reads as Doug.
16. **Carry shots (s051, s078, s103, s104, s151, s177, s203, s223, s245):** the suitcase is still drawn over Doug's legs
    (carried over from the asset review, note 2). Optional.

## Thumbnail: PASS
Archetype A: 9 tiles in a 3x3 grid, white background, black rounded frames, and one consistent comic font for the labels.
The labels exactly match the chapter names, and none of them repeats a title word ("Dying", "Deadly", "Place", "Earth").
At 168x94 (`thumbnail_small.png`), the angry sun, snakes, flamingo-Doug, hut, peak, crystals, storm and volcano all read.
Dallol reads as "weird neon place", which is enough. Leaving Lake Nyos off the thumbnail is the right call for a
mass-casualty item. Doug appears in only one tile. Minor and optional: "Everest Death Zone" is auto-fitted a little
smaller than the other labels.

No asset fixes for the illustrator.

## Changed files
- `channel/art_bible.md`:
  - Doug's `y` is his hip.
  - Recipe for a buried/sinking Doug (surface at hip y).
  - Auto-ink samples one point, so keep Doug on one side of a dark/light horizon or sit him behind a light prop.
  - Sombre-item white title exception, and no yellow/green title cards.
  - Wordart must not cross map frames, land, crystals or bolts.
  - The counter zone applies to every counter shot.
  - Ground texture lines must not pass behind Doug.
