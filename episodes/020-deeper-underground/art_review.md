# 020 Deeper Underground: art review (art director, 2026-10-16)

Scope: the new assets in `asset_requests.md` (33 library files: 6 gated devices, 8 stickers, 2 creatures, 16 places/props,
1 crude-tier human). Checked against the previews in `assets/previews/020-*.png`, plus zoomed check renders, the radii in
the JSON, and the shotlist placements.

## Verdict: FAIL (assets). All 6 gated devices are APPROVED. 4 non-gated assets need one more pass.
Shotlisting can continue. The four REVISE assets keep their anchors and sizes, so no shot has to move. Re-preview only those four
and send them back to me. I will re-check them without a full review.

## Gated devices
| # | Asset | Verdict | Notes |
|---|---|---|---|
| 1 | `earth_cross_section` | APPROVE | Radii verified in JSON: outer 400, crust 400→392 (8 units), transition band `#9c542f` 374.4/358.4 (0.936/0.896), outer core 218.4 (0.546), inner core 76 (0.19) with `#ffe24a` ring at 85, outline 6. The band is subtle, so the scene's dashed rings will read on it. Edges are clean at 2.6 and it reads as "Earth" at 0.2 on dark strata. No text. Reusable for any later into-the-planet episode. |
| 2 | `drill_pod` | APPROVE (AD fix) | Industrial, riveted and dry, not cute. **AD fix:** I removed the small `curve` (60,90)-(80,100)-(96,92) under the porthole. Next to the round porthole it read as a smirk, which turned the pod into a one-eyed face (kid-appeal risk, brief section 7). |
| 3 | `drill_pod_open` | APPROVE | The opening is empty, the floor is at y 130 and Doug at hip +35 / 0.6 stands on it (35 + 152 x 0.6 = 126). Doug's black ink reads on the mid-grey interior. The door porthole is kept. |
| 4 | `drill_pod_melted` | APPROVE | It reads as the same pod, melted: drooping porthole, sideways drill, bent exhaust, orange puddle. There is no face. |
| 5 | `depth_icon` | APPROVE | Bold. It reads as "go down into rock" at 32 px and matches the 015 shovel and 016 ice-cube family. |
| 6 | `again_stamp` | APPROVE | Rough red ink, a believable -8 degree tilt, and on-palette `#e0201b`. At 1.5 on the closing card it is crisp. At suitcase scales of 0.165-0.32 it reads as a red mark rather than a word, which is expected and fine because the narration names it. |

## Stickers
| # | Asset | Verdict | Notes |
|---|---|---|---|
| 7 | `sticker_movile_cave` | APPROVE | |
| 8 | `sticker_lechuguilla` | APPROVE (AD fix) | The text ran into the peel corner and the right edge. **AD fix:** text size 13.8 → 12.0, x 0 → -4. |
| 9 | `sticker_veryovkina` | APPROVE | |
| 10 | `sticker_mponeng` | APPROVE (AD fix) | The text touched both edges and the peel. **AD fix:** text size 19 → 16, x -4. |
| 11 | `sticker_the_moho` | APPROVE (AD fix) | The final "O" sat on the peel. **AD fix:** text size 18.9 → 16, x -4. |
| 12 | `sticker_hidden_ocean` | APPROVE (AD fix) | **AD fix:** text size 12.6 → 11.2, x -4. |
| 13 | `sticker_outer_core` | APPROVE (AD fix) | "CORE" crossed the peel. **AD fix:** text size 16 → 14, x -2, y 1 → -1. |
| 14 | `sticker_the_center` | APPROVE (AD fix) | "CENTER" crossed the peel. **AD fix:** text size 15 → 12, x -2, y 1 → -2. en-US spelling confirmed. |
Zoomed re-render checked: every name now clears the peel corner and the border. The badge family matches `sticker_naica`.

## Creatures and human
| # | Asset | Verdict | Notes |
|---|---|---|---|
| 15 | `cave_centipede` | APPROVE | It is eyeless and has forcipules, about 21 segments and long antennae. It is creepy but clean. Its solid-black silhouette reads as a centipede. |
| 16 | `devil_worm` | APPROVE | A scientific drawing with a gut line, blunt head and tapered tail. It is exactly 400 long. |
| 17 | `scientist_woman` | APPROVE | Crude tier: same rig, crescent, `auto_ink`, glasses, coat and hair. It is generic, not a likeness. |

## Places, machines, props
| # | Asset | Verdict | Notes |
|---|---|---|---|
| 18 | `mine_headframe` | **REVISE** | See fix 1. |
| 19 | `mine_cage` | APPROVE | Two decks, 7 miners in yellow hats, mesh sides. It reads at 0.2. |
| 20 | `mine_fan` | APPROVE | |
| 21 | `drilling_rig` | APPROVE | The crown block ties both legs together at the top, so it reads as one derrick. The pipe rack and cabin are good. |
| 22 | `borehole_cap` | **REVISE** | See fix 2. |
| 23 | `gypsum_chandelier` | APPROVE | Top anchor, 660 tall, the glints read on dark rock. |
| 24 | `gypsum_cluster` | APPROVE | |
| 25 | `juina_diamond` | APPROVE | Dull and scruffy as briefed, with the green speck at (+20,-10). |
| 26 | `rug` | APPROVE | |
| 27 | `houseplant` | **REVISE** | See fix 3. |
| 28 | `water_glass` | APPROVE | It is cloudy grey-brown, so it reads as "not tap water". |
| 29 | `water_glass_empty` | APPROVE | |
| 30 | `antibiotic_capsule` | APPROVE | |
| 31 | `compass` | APPROVE | |
| 32 | `stretcher` | **REVISE** | See fix 4. |
| 33 | `burj_khalifa` | APPROVE | Exactly 600 tall, the stack checked, steel-blue. |

## Required fixes (illustrator)
1. **`mine_headframe`**: it reads as two separate radio towers with a wide gap, not one headframe. The cables do not show at 0.55.
   - Join the two lattice legs at the top with a steel **sheave deck** (a horizontal girder, `#5a5f66`, outline 4) spanning the full width at
     about y -470. Both sheave wheels sit on that deck, so they read as one machine.
   - Add a light lattice cross-brace between the legs **above y -300 only**. Below y -300, keep x -25..+25 empty as requested,
     because the shaft is drawn there.
   - Make the hoist cables visible: width 4, black, from the wheel rims down to the shaft mouth at x ±32 (they are invisible now).
   - Bring the inner leg edges to about x ±30 at ground level so the empty column is about 50-60 wide, not about 70.
   - Keep the anchor (bottom-centre = shaft mouth) and the 360 x 520 size.
2. **`borehole_cap`**: at scale 0.6 it reads as a cooking pot. Without the knob it reads as a chocolate cake or a hat (I tried this and reverted it).
   The whole thing is one rust-brown colour, and the dark bolt dots on the top look like chocolate chips.
   - Make the cap **steel** `#6a6e75` (shade `#4f535a`) with rust *patches and streaks* `#b0521a` / `#c86a2a`, not solid brown.
   - Make the top a flat welded plate: a lighter grey ellipse with one irregular weld bead around its rim (a dark grey `#3f4349` zigzag, width 3).
     Remove the valve knob and the ring of dark dots on the lid.
   - Move the bolts to the flange only, as light-grey hex heads (`#a8acb2`, outline 2) so they read as metal.
   - Lower the cylinder to about 25 tall, so it is a squat stub rather than a pot or a hat. Keep the concrete slab, the rust streaks running onto it, the
     anchor and the 260 x 110 size.
3. **`houseplant`**: the flat top "leaf" at y -300 is a green trapezoid on a stem and reads as a tray or an umbrella.
   - Redraw it as a real broad leaf seen from the side: a lens shape with a pointed tip at one end, a midrib vein (`#2e8b3a`, width 3) and a
     darker underside crescent. Keep the **top edge flat at y -300** and at least 120 wide so the cap still sits on it.
   - Add a slight lean so it grows naturally off the main stem (stem joins the leaf's underside off-centre).
4. **`stretcher`**: it reads as an orange bread basket or a canoe. Make it read as a rescue litter.
   - Add a steel **top rail** around the rim (`#a8acb2`, width 6, black outline).
   - Add 2-3 black **cross straps** with small grey buckles across the bed.
   - Make the ends squarer and flatter (a basket litter is a long tray, not a boat): flatten the bow curve.
   - Keep it empty, neutral and plain, with the same anchor and the 420 x 140 size.

## Notes for the director (composition, no asset change)
- **s027 centipede silhouette**: the backdrop is brown cave rock (`#3b2a17` / `#a87a40`). Under the art bible, red speckle on brown reads as
  blood spatter. Use `"glow": "#5e4670"` (dull purple) and keep `glow_r` 330.
- **s277 melted pod**: `doug_cap` is in frame and the counter ticks. Good.
- **Pod shots at 1.0 (s251-s254, s274-s276)**: the exhaust tip is at about y -330 x scale. At y 560 it clears the DOUG DEPTH meter zone
  (x 1300-1860, y 110-260). Keep it that way if the pod moves up or right.
- `again_stamp` and the stickers at suitcase scale 0.125-0.26 are marks, not legible words, and that is intended. Do not rely on them for any
  spoken beat before the closing card at 1.5.

## Art-director edits made in `assets/library/` (please keep them)
- `drill_pod.json`: removed the smirk-like `curve` under the porthole.
- `sticker_lechuguilla`, `sticker_mponeng`, `sticker_the_moho`, `sticker_hidden_ocean`, `sticker_outer_core`, `sticker_the_center`: the text is
  smaller or shifted so it clears the peel corner (values above). No other change.
