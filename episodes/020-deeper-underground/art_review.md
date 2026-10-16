# 020 Deeper Underground: art review (art director, 2026-10-16)

Scope: the new assets in `asset_requests.md` (33 library files: 6 gated devices, 8 stickers, 2 creatures, 16 places/props,
1 crude-tier human). Checked against the previews in `assets/previews/020-*.png`, plus zoomed check renders, the radii in
the JSON, and the shotlist placements.

## Verdict: PASS (assets, re-check 2026-10-16). All 33 assets are APPROVED.
The first pass sent 4 non-gated assets back (fixes 1-4 below). The illustrator's revisions were re-checked on
`assets/previews/020-revise.png` and `020-revise-zoom.png` and in context (s027, s048, s062, s157, s164, s206). All four now pass.
See "Re-check" at the end.

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
| 18 | `mine_headframe` | APPROVE (re-check) | Fix 1 done. See Re-check. |
| 19 | `mine_cage` | APPROVE | Two decks, 7 miners in yellow hats, mesh sides. It reads at 0.2. |
| 20 | `mine_fan` | APPROVE | |
| 21 | `drilling_rig` | APPROVE | The crown block ties both legs together at the top, so it reads as one derrick. The pipe rack and cabin are good. |
| 22 | `borehole_cap` | APPROVE (re-check) | Fix 2 done. See Re-check. |
| 23 | `gypsum_chandelier` | APPROVE | Top anchor, 660 tall, the glints read on dark rock. |
| 24 | `gypsum_cluster` | APPROVE | |
| 25 | `juina_diamond` | APPROVE | Dull and scruffy as briefed, with the green speck at (+20,-10). |
| 26 | `rug` | APPROVE | |
| 27 | `houseplant` | APPROVE (re-check) | Fix 3 done. See Re-check. |
| 28 | `water_glass` | APPROVE | It is cloudy grey-brown, so it reads as "not tap water". |
| 29 | `water_glass_empty` | APPROVE | |
| 30 | `antibiotic_capsule` | APPROVE | |
| 31 | `compass` | APPROVE | |
| 32 | `stretcher` | APPROVE (re-check) | Fix 4 done. See Re-check. |
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
  blood spatter. Use `"glow": "#5e4670"` (dull purple) and keep `glow_r` 330. **Done by the AD** in `build/gen_shotlist.py`
  (line 520), shotlist regenerated, s027 keyframe checked: the purple haze reads as menace, not blood.
  (s078 `devil_worm` keeps its red glow: it sits on near-black `#1f1416`, not brown, and the red is the "devil" beat.)
- **s277 melted pod**: `doug_cap` is in frame and the counter ticks. Good.
- **Pod shots at 1.0 (s251-s254, s274-s276)**: the exhaust tip is at about y -330 x scale. At y 560 it clears the DOUG DEPTH meter zone
  (x 1300-1860, y 110-260). Keep it that way if the pod moves up or right.
- `again_stamp` and the stickers at suitcase scale 0.125-0.26 are marks, not legible words, and that is intended. Do not rely on them for any
  spoken beat before the closing card at 1.5.

## Art-director edits made in `assets/library/` (please keep them)
- `drill_pod.json`: removed the smirk-like `curve` under the porthole.
- `sticker_lechuguilla`, `sticker_mponeng`, `sticker_the_moho`, `sticker_hidden_ocean`, `sticker_outer_core`, `sticker_the_center`: the text is
  smaller or shifted so it clears the peel corner (values above). No other change.

## Re-check of the 4 revised assets (2026-10-16)
| # | Asset | Verdict | Notes |
|---|---|---|---|
| 1 | `mine_headframe` | APPROVE | The sheave deck ties both legs into one machine with the wheels on top. It reads as a headframe, not two radio towers, at 0.55 and at the 168 px tile. The cross-brace stays above y -300. **Deviation accepted:** the ropes drop at x ±14 into the shaft mouth instead of ±32. They are visible now, and in s164 the cage hangs between them. |
| 2 | `borehole_cap` | APPROVE | It is grey steel with rust patches and streaks running onto the slab. It has a welded top plate and light hex bolts on the flange only, and the stub is squat. It no longer reads as a pot, cake or hat. 260x80 instead of 110 tall is fine (bottom-centre anchor, nothing sits on it). In s206 at 0.6 it is small but reads as a capped stub on concrete. |
| 3 | `houseplant` | APPROVE | The top leaf is a real side-view leaf with a midrib and an underside crescent. The stem joins it off-centre. In s157 the cap sits cleanly on the flat top. |
| 4 | `stretcher` | APPROVE | The steel rail, three straps with buckles and the squared tray ends make it read as a rescue litter, not a basket or canoe. It is neutral and empty on the sober s048 card. |

No AD edits were needed on this pass. Asset gate: PASS. Shots s027, s048, s062, s157, s164 and s206 were re-rendered.
`build/contact/sheet_01.png` now holds only those 6, so re-run the full `keyframes` pass before the keyframe review.

## Keyframes round 1 (art director, 2026-10-16)
Scope: all 308 keyframes in `build/contact/sheet_01-26.png`, with full-res checks of `build/keyframes/` for s006, s059, s083, s151,
s161, s202, s216, s229, s231, s243, s279, s300, s302 and s307. s001 (thumbnail pending) is excluded.
Coordinates below are at 1080p. "Counter zone" means the reserved block at x 1300-1860, y 110-260 (art bible, Recurring layouts: second meter under
the counter). Wordart and title glyph tops must stay at y ≥ 290 where they overlap x 1300-1860.

### Verdict: FAIL (composition only, 41 numbered fixes). No asset or engine change is needed.
What passes, so please don't change it:
- **Doug is on-model in every shot.** He has the red cap on every living, dead and ghost Doug (s032, s107, s158, s232, s255, s304-s307). Auto-white ink works on
  every dark ground (s006, s076-s078, s098-s102, s150-s151, s201-s203, s213, s234, s284-s293).
  The cap is in frame on all 9 deaths. The counter ticks 161 to 170 on s031, s058, s106, s157, s183, s231, s254, s277 and s303, and s307 reads 170.
- **The zone ramp matches the art bible strata ramp and darkens one step per item.** The items run Movile `#3b2a17`/`#a87a40` → Lechuguilla `#d4a04a` → Devil Worm `#c07a3a` → Veryovkina `#a65a32` →
  Oldest Water `#8e4a2c` → Loneliest Bacterium `#665244` → Mponeng `#4a505c` → Kola `#3f444d` → Moho `#4a3a34` with mantle red → Hidden Ocean
  `#2a2a2e` → core items on `#15181a` / navy. Shaft and crack interiors are always `#f1e4c6`. The section cards are white with no top bar (Dark. / Hot. /
  Nobody.). The item titles are red. The DOUG DEPTH meter is monotonic.
- **Reveals and safety pass.** s027 centipede (purple haze on brown) and s078 devil worm (red glow on near-black) are silhouettes, and the reveal
  comes on a later beat. Nothing is gory. Nothing looks cute or kid-coded (the pod has no face).
- The closing card s307 is good. The stickers read as the trip's badges, and "170" and the ghost read at phone size.

### Required fixes (director)
**A. Layout variety (more than 6 shots on one composition)**
1. **s012-s022 (11 shots in the same wide Movile lake).** Cut s018-s021 ("The air itself is wrong ... a third of the normal oxygen") to a
   cream `#f4f1dc` diagram card. Put a big glass jar or bell of cave air at centre and Doug gritted (scale 0.6) at left. Build it up one shot at a time:
   s018 "THE AIR" wordart, s019 "100x CO2", s020 the METHANE / HYDROGEN SULFIDE labels, s021 the oxygen gauge with "1/3 OXYGEN". Return to the lake on s022.
2. **s025-s033 (9 shots in the same lake).** Move s025-s026 to a cream card. Show a grid of about 12 small cave animals (reuse the s016 spider and the
   centipede at small scale), and on s026 ring most of them in red for "37 ONLY HERE". Keep s027-s033 in the lake, because the reveal, the sandwich and the death need it.
3. **s128-s135 (8 shots in the same Kidd Creek tunnel).** Move s128-s129 to a cream card. Show two `water_glass` assets, labelled "SEAWATER" and
   "KIDD CREEK", with 1 salt pile vs 8 for "8x SALTIER". On s129, show bacteria eating from the second glass for "CHEMICAL FOOD" / "SULFATE". Return to the tunnel on s130.
4. **s262-s270 (9 globe shots, and s262-s265 are framed the same).** Play s262-s264 on the s259/s260 "inside the outer core" orange
   `#ff5a1f` layout. Add the swirl arrows on s262, "HEAT" rising arrows on s263 and a curved "SPIN" arrow on s264. Return to the globe on s265.

**B. Counter zone and caption bar collisions**
5. **s045**: the caver (1300, 344) and the scientist (1480, 344) put their heads in the counter zone. Move both to x 1000 / 1150.
6. **s071**: the "ROUNDWORM" wordart (960, 260) touches the depth meter. Move it to (760, 330).
7. **s089**: the top Burj Khalifa (1650, 434) runs into the counter zone. Move the 3-Burj stack to x 1450 and drop it about 140 px so the top
   spire stays below y 290 (or scale it 0.42). Keep the stack's base on the floor.
8. **s119**: the label "BARBARA SHERWOOD LOLLAR" (1200, 300) butts against the depth meter. Move it to (1100, 340) and GEOCHEMIST to (1200, 420).
9. **s141**: the petri dish (r 400 at 960, 540) touches the counter box. Shrink it to r 340 at (900, 600).
10. **s153**: the label "JOURNEY TO THE CENTER OF THE EARTH" (1100, 300) touches the meter. Move it to y 340, or wrap it to two lines.
11. **s190**: the second `drilling_rig` (1500, 280) sits under the depth meter. Move it to x 1150 and route the oil-well line from there.
12. **s003, s212, s237, s239, s241, s286, s294**: the wordart is at y 330-340, and the glyph tops land at about y 280 inside the counter zone. Set y 380 on each.
13. **s243**: the world map's top-right corner covers the depth meter. Use scale 0.75 at (900, 560) so the frame ends at x ≤ 1280 or starts at
    y ≥ 260. The "?" (1640, 860) then sits clear of the map edge.
14. **s244**: the map runs under the counter and the depth meter, and "MELTING" sits on green land (banned). Use `north_america_map`
    at scale 0.95, centred (820, 600). Put "MELTING" on the sea to the right, for example (1500, 760), or use the green-ground override.
15. **s248**: the top-right lattice circle (1360, 300) touches the meter. Shift the whole lattice down 60 px and left 60 px.
16. **s267**: the top solar-particle arrow starts at about y 255 under the meter. Shift the three yellow arrows down 60 px.
17. **s282**: the "?" (1500, 300) hits the depth meter. Move it to (1500, 380).
18. **s207, s208**: the `narrator_hand` (960, 300, flipped) enters through the caption bar "THE KOLA SUPERDEEP BOREHOLE". Bring it in from the
    right frame edge below y 120 (for example x 1250, y 380), so the arm never crosses the top bar. Hang the string from it to the same cap positions.
19. **s231**: the open pod (960, 376, scale 0.9) pushes its chimney up under the caption bar "THE MOHO". Set y 470, or scale it 0.8 (tall props must stay below the top bar).

**C. Text colliding with art**
20. **s008**: the "1986" wordart (600, 300) sits on the green Eurasia land mass. Move it to open sea, for example (330, 160), or use the green-ground override.
21. **s051**: "4 MILLION YEARS" (1100, 990) sits on the dish rim, lime on pale green. Move it to (1100, 1010) below the dish, or to the cream at
    (520, 860).
22. **s083**: "SURVIVED" (600, 380) runs into the hand and into the "..." label (860, 420). Move the wordart to (520, 520) and the "..." to
    (1000, 240), clear of the hand.
23. **s161**: the "!" (1700, 620) sits on the final E of "DEEPEST MINE". Move it to (1780, 620), or move the wordart to x 1250.
24. **s173**: the red arrow from HOT TUB 40°C to ROCK 60°C passes through the "HOT TUB 40°C" text. Start it at the label's right edge
    (about 1540, 586).
25. **s184**: "PIPE FULL OF ICE" (960, 470) is cut by the pipe (rect x 1100). Move the wordart to (620, 420), clear of the pipe.
26. **s202**: the left half of "6,371 KM" (1400, 420) sits on the Earth's crust. Move it to (1560, 380), clear of the globe (y 380 keeps it under the counter zone).
    In **s203**, move "0.2%" (1450, 420) to (1560, 460) and "12 KM" to (1560, 340), so neither crosses the rim.
27. **s211**: the red arrow cuts through "20 YEARS" (1400, 600). Drop the label to (1400, 680) and aim the arrow at the cap from above-right.
28. **s222**: "GUADALUPE ISLAND, MEXICO" (1300, 330) sits on the ship's bridge. Move it onto the sea at (1500, 760).
    In **s223**, nudge "PROJECT MOHOLE" right 60 px so it clears the stern.
29. **s229**: "DRILL POD" (1450, 420) covers the pod's porthole. Move it to (1580, 380).
30. **s251, s274**: "A SNORKEL" and "COMPASS" (1500, 420) sit on the open pod door. The art bible says to keep wordart off an open door. Move both to (1600, 380),
    right of the door (the door ends at about x 1250 at scale 1.0, so check the wordart's left edge clears it).
31. **s279**: the ghost Doug (400, 400) sits on the N of "NOBODY HAS SEEN" (760, 330). Move the ghost to (300, 640).
32. **s287**: the label "WHEN DOES IRON MELT?" (1400, 900) touches Doug's "?" at 1750. Move the label to (1300, 960).
33. **s299**: "ARGUED ABOUT" (960, 900) runs across both scientists' legs. Move it to (960, 330) above the ball.
34. **s302**: the down "UP" arrow starts inside Doug, skewering his legs and the suitcase. Start it below his feet (from y 900). Move the lower-right
    arrow so it doesn't cross the flag, or move the flag to x 1300.

**D. Readability and safe area**
35. **s216-s221, s226, s227**: Doug at (1800, 1006.8, scale 0.35) has his feet at y 1060, outside the safe area (y ≤ 1040). Set Doug at (1720, 980).
    **s271** (1800, 979.2, 0.4) → (1720, 960).
36. **s059**: Doug at scale 0.18 is about 25 px tall and reads as a speck. Use scale 0.35, or replace him with a red ring on the maze dead end.
    **s144**: same issue (scale 0.18 among the bacteria). Use scale 0.3 so "the same guy" gag reads.
37. **s236, s242, s246**: the tiny Doug (1250, 197, scale 0.25) stands on the globe rim right next to the counter. Move him to the rim at about x 700-800 at
    scale 0.3, or drop him (he adds nothing at that size). **s255**: the same applies to the ghost (1500, 460). Move it to (700, 300).
38. **s104**: the `phone` + `red_x` at scale 0.4 reads as an unidentifiable icon. Use scale 0.8.
    **s134**: the `doormat` at 0.5 reads as a brown tray. Use scale 0.9 at (1150, 878) so "waiting for a visitor" reads.
39. **s193**: the hand-drawn circle with rays reads as a sun or a spark, not a plankton fossil. Draw it as a small chambered spiral (a foram: 3-4
    touching circles in a spiral plus one spiral line, `#e8e2c8`, outline 4), about 70 px, in a white magnifier ring. Do not use `ammonite` (it's the wrong
    animal).
40. **s061, s136, s185, s186**: the map insets show their rectangular frame and a dark `#3a9ad9` band (the s185/s186 world map sits at y 1360). This
    doesn't match s007, s034, s086 and s110, where the map fills the panel. For s185/s186, use the world map at y about 1100 and x shifted so Kola is near (840, 640).
    For s061/s136, use `south_africa_map` at scale about 1.15 so its frame edges fall outside the 0-1180 panel.
41. **s304-s306** are the boss item's kicker, so they need the "THE INNER CORE" caption bar (style bible §7 rule 3). Remove `"topbar": false`. Only the
    closing card s307-s308 stays bare.

### Optional (not blocking)
- s281: Inge Lehmann (1936) uses the same `scientist_woman` as Barbara Sherwood Lollar (s113-s131). If the asset supports a hair colour, grey hair would
  separate them.
- s101/s102: the flood is a plain blue rectangle. A wavy top edge plus a `spray` of `#2a6fb0` would read more like water than a box.

Routing: all 41 fixes go to the **director** (`build/gen_shotlist.py` → regenerate → `keyframes --shots ...`). There are no illustrator fixes this round.
Re-review only the changed shots plus their neighbours on the next pass.

## Keyframes round 2 (art director, 2026-10-16)
Scope: all 308 keyframes in the fresh full render `build/contact/sheet_01-26.png` (s001 is now the chosen thumbnail A), with full-res checks
of `build/keyframes/` for s001, s089, s129, s154, s184, s186, s219, s221, s243 and s268. Coordinates are at 1920x1080.

### Verdict: FAIL (composition only, 2 numbered fixes). No asset or engine change is needed.
39 of the 41 round-1 fixes are applied cleanly. Two leftover counter-zone collisions (s221, s268) are the same class as round-1 fixes 13-16.
Both are coordinate edits on one shot each.

What passes, so please don't change it:
- **Round-1 fixes verified.** Fixes 1-4 work: the cream jar card (s018-s021), the animal grid (s025-s026), the two-glass card (s128-s129)
  and the orange liquid-metal run (s262-s264) all break up the long runs. No composition now repeats for more than 6 shots.
  The fixes for s045, s071, s089, s119, s141, s153, s161, s173, s184, s190, s202/s203, s207/s208, s211, s222/s223, s229, s231, s251/s274,
  s279, s282, s287, s299 and s302 are all correct. Doug's feet are inside the safe area on s216-s227 and s271. s059 and s144 now read as Doug.
  The s193 foram, the s104 phone and the s134 doormat all read. s304-s306 have the caption bar back.
- **Accepted deviations (director):**
  - s185/s186: the Kola world map is re-framed rather than shifted to the exact coordinates. It fills the panel, and Kola is clearly ringed.
    "1970" uses the cream green-ground override, which is allowed.
  - s061/s136: `south_africa_map` fills the panel with no frame band.
  - s244: the map is in a blue sea panel, and "MELTING" sits on the sea. Its corner clears the meter.
  - s236/s242/s246: the tiny Doug moved to the left rim. s255: the ghost is on the left rim.
  - s220: the 4 Everests stay on the ruler line in the middle, and "4 EVERESTS" is at top left.
  - s281: Lehmann keeps the brown-haired `scientist_woman`. The name label and the 1936 date separate her from Sherwood Lollar, and this fix was optional.
  - s128/s129: both glasses use the same water tint. The labels, the 1 vs 8 salt piles and the bacteria carry the comparison.
  - s243: the map frame starts at y 260, flush under the meter. That meets the letter of fix 13, and nothing overlaps.
- **Style and continuity hold.** Doug is on-model with the red cap in every shot, including all 9 deaths, the ghosts and the closing card.
  The counter runs 161 to 170 on the same beats as round 1. The zone ramp, the cream shaft and crack interiors, and the red item titles are unchanged.
  Nothing is gory or kid-coded.
- **s001 / thumbnail A:** on-palette strata wedge, with Doug on-model on the surface. The 8 labels are legible, and every element is inside the frame. PASS.

### Required fixes (director)
1. **s221**: the ocean band (rect y 200, h 160) runs under the counter. The depth icon (1366, 238) and the "DOUG DEPTH" box sit on the
   blue band. Start the ocean at y 290: set the rect to `y 290, h 70` and move the "OCEAN" label to y 325. Leave the crust, mantle, red Moho line
   and "6 KM" as they are. The diagram's top edge then matches s217-s220 (y ≈ 270-300).
2. **s268**: the top solar-wind curve ends at (1270, 230) and runs straight through the depth icon at (1366, 238). Change its points to
   `[[1640, 380], [1520, 380], [1440, 340], [1290, 300]]`. For symmetry, end the bottom curve at (1290, 910) instead of (1270, 980). The other
   two curves stay as they are.

### Optional (not blocking)
- s154: Doug (1250, 260, scale 0.25) stands in empty space next to the counter. Moving him onto the globe rim at about (700, 300) would match
  how s236/s242/s246 were fixed.
- s089: the "S" of "2.5 BURJ KHALIFAS" ends about 25 px from the half-Burj stub. Nudging the wordart 40 px left would give it air.
- s184: "WORKPLACE / OVEN" sit right under the depth meter (label top at y ≈ 278) and read as part of the HUD. Moving both labels to x 1250
  or y 340+ would separate them.

Routing: both fixes go to the **director** (`build/gen_shotlist.py` → regenerate → `keyframes --shots s221,s268`). There are no illustrator
fixes. Re-review is limited to s221 and s268. Once both are clean, the keyframe gate is PASS with no further full pass needed.

## Keyframes round 3 (art director, 2026-10-16)
Scope: full-res `build/keyframes/` for s089, s154, s184, s221, s268 and s303 (all re-rendered 17:52). This review also covers the
visual-screener's only blocking item (s303). Coordinates are at 1920x1080.

### Verdict: PASS. The keyframe gate is closed.
1. **s221 (round-2 fix 1)**: the ocean band now starts at y 290 and "OCEAN" sits inside it. The depth icon and the "DOUG DEPTH" box are on
   clean background, and the diagram top lines up with s217-s220. Fixed.
2. **s268 (round-2 fix 2)**: the top and bottom solar-wind curves now end at x 1290 (y 300 / 910) and are symmetric. Neither touches the
   HUD. Fixed. Accepted deviation: the outermost light-blue magnetosphere loop still passes behind the depth icon at about (1366, 238).
   The icon is drawn on top and stays fully legible, the loop clears the counter box, and the line is a thin background element. This is not blocking.
3. **s303 (screener's blocking item)**: with the cream cover and the cap-on-flag gag gone, there is now exactly one red cap, still on dead
   Doug's head as he lies on his side. That makes it continuous with the other 8 deaths. Doug is on-model with X eyes and a flat mouth, nothing is gory,
   and the "DOUG WAS HERE" flag and the stickered suitcase read cleanly. The caption bar "THE INNER CORE" is present, and the counter reads 170 with depth 6,371 km.
   The pale inner-core cream matches the zone ramp. PASS.
4. **Round-2 optionals taken**: s154 Doug now stands on the globe rim at about (700, 260), clear of the counter. s089 "2.5 BURJ KHALIFAS"
   has air before the Burj stack. In s184, "WORKPLACE / OVEN" moved down to y ≈ 315, below the depth box, so they no longer read as HUD.
   All three are PASS.

Routing: none. Stage → `art_approved` (art + visual screeners passed).
