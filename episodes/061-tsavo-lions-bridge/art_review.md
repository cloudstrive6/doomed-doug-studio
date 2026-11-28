# 061-tsavo-lions-bridge: art review (art director, 2026-11-28)

## Round 1: new assets (29) + DAYS WITHOUT AN INCIDENT board: FAIL (assets) / PASS (board)

What I checked: `assets/previews/061-tsavo-lions-bridge-assets.png`. Every asset on white, on night navy `#0f1a36` and as
`silhouette` + grey rim on `#080c1c`, against the requested bbox (`build/check_assets.py`). Lion faces zoomed 3x. Test keyframes
in context: s002 s020 s027 s034 s040 s050 s091 s102 s108 s109 s116 s121 s146 s155 s160 s163.

**CD conditions: all met.** The lions are maneless and lean. The eye is a small amber dot under a heavy flat brow, with no
highlight and no emoting brow. The mouth is closed and there is no smile, so the drawings are not Lion King coded. No blood, wounds,
claws, bared teeth, rifles or trophy imagery anywhere. `donkey_carcass_outline` is gore-free. `lion_trap` reads as a crude
timber-and-iron box, not a torture device. The humans are plain generic stick men.

**Why it fails:** the shared lion head reads as a hamster, bear or capybara, not a lion. Two things cause it: an egg-shaped head
with the nose at a pointed tip, and two round "teddy" ears on top of the crown. In context this is clear in three places:
s027 (head silhouette = a black Mickey/bear blob), s091 (sitting lion reads as a bear from behind) and s160 (finale lion reads as
a marmot looking up). The lion is the star of 17+ minutes, so it has to read as a lion at a glance. Second problem: the trap
occupants are drawn over the front bars (s116, s121), so the lion and the soldiers appear to stand *in front of* the cage.

### Fixes (illustrator unless noted)

1. **All lion drawings** (`tsavo_lion`, `_walking`, `_charging`, `_sitting`, `_looking_up`, `_head`, `_mattress`): redraw the
   head as a lion profile. It is one shared head, so fix it once.
   - Make the muzzle a longer, boxier block, about 45% of the head length, with a flat, near-straight bridge from the brow to
     the nose. No pointed egg tip.
   - Put a broad dark nose pad on the front-top corner of the muzzle.
   - Give it a deeper, squared lower jaw and chin, with a flat closed mouth line running back to under the eye.
   - Make the ears about 60% of their current size, rounded-triangular, set back behind the eye on the rear of the skull, not
     side by side on the crown.
   - Keep the brow, the amber eye, the pale muzzle patch, the cheek fringe and the whiskers.
   - Keep nose tips within ±15 units of the noted key points. If any moves more than that, note the new value under the request
     in `asset_requests.md`.
   - Re-check `tsavo_lion_head` as a black silhouette: the outline alone (flat forehead, square muzzle, chin) must say "big cat".
2. **All lion drawings: stray spray texture outside the outline.** Pale fur-speckle dots fall outside the body below the belly
   (standing, walking, mattress), above the back (charging) and behind the back (sitting, looking_up). On the night navies they
   read as floating dust. Keep every spray inside the fill (smaller radius or moved inward).
3. `tsavo_lion_looking_up`: the rotated brow stroke cuts straight through the eye, which reads as a slashed or closed eye. Move it
   just above the eye toward the forehead, so the eye stays a clean amber dot.
4. `tsavo_lion_head`: the throat fringe under the chin is drawn as zig-zag glyphs that read like scribbled letters ("ƐV").
   Replace them with 3-4 short tapered strokes, like the cheek fringe.
5. `lion_trap` and `lion_trap_bent_bar`: add two front overlay assets, `lion_trap_front` and `lion_trap_bent_bar_front`. They
   contain only the front iron bars, the horizontal rail, the frame posts and the divider rails, with the same anchor and bbox and
   transparent between the bars. **Director:** in s111-s128 layer them as trap, then occupants (lion, soldiers, Doug, lamp), then
   front overlay, so everyone sits *behind* the bars.
6. `donkey_carcass_outline`: gore-free, but it reads as a seal or rabbit loaf (head and ears melt into one blob). Keep the pale
   flat fill, the 4 px `#6b6358` outline, no eye and nothing red. Add these so it reads as a donkey:
   - a distinct long head with a squared muzzle
   - two long ears laid back as separate shapes
   - a short upright mane line along the neck
   - folded thin legs with small hoof ends showing
   - a thin tail with a small tuft
   The wire point at the hind leg must stay where the shotlist expects it.
7. `tree_with_beds` and `water_tank_beds`: the beds read as planks or benches (s102). On each bed, add a white pillow at one
   end, a grey blanket with a visible fold or hump, and short visible legs on the wooden frame. Keep the bed sizes and the tank's
   clear centre (x -60..60, y -520). The olive canopy on `tree_with_beds` is fine.
8. `narrator_hand_side`: it reads as a white fish or bird face with an eye (the dark filled triangle at the pinch). Remove the
   dark triangle. Draw a curled forefinger with the thumb tip meeting it at the pinch point (0,0), plus knuckle lines on top.
   Match the white-glove style of `narrator_hand` (white fill, thick black `keep_ink` outline, grey cuff). Keep the pale sticker
   dot.

### Per asset

| Asset | Verdict |
|---|---|
| tsavo_lion | FIX 1, 2. Body, tail tuft, tawny/pale palette and silhouette (legs, tail, ears separated) are good. |
| tsavo_lion_walking | FIX 1, 2. Stride and silhouette good. |
| tsavo_lion_charging | FIX 1, 2. Mouth closed, no claws, long low bound. Good. |
| tsavo_lion_sitting | FIX 1, 2. The head top 4 units over the bbox is accepted. |
| tsavo_lion_looking_up | FIX 1, 2, 3. The posture reads as patient waiting, not roaring. Good. |
| tsavo_lion_head | FIX 1, 4. The neck runs off the left edge with no end outline, as requested. **Director:** the `rim` draws a line around the cut end, so keep x -260 hidden behind the tent edge or off-frame. In s027 the neck rectangle currently sits in front of the tent wall: make it emerge from the dark doorway. |
| tsavo_lion_mattress | FIX 1, 2. The ticking mattress is plain, empty, absurd and not violent. Approved. |
| lion_paw_reach | APPROVE. Claws retracted, no end outline on the arm, reads as a big paw. |
| canvas_tent_open | APPROVE. Clean dark doorway. |
| canvas_tent_flat | APPROVE. Heap and snapped pole read. Overflow noted (pole -136, heap +170). |
| hurricane_lantern | APPROVE. The globe stays light on near-black. |
| thorn_fence | APPROVE. Mid-tone, no green, pale thorns read on navy, tiles. |
| thorn_fence_gap | APPROVE. |
| thin_thorn_tree | APPROVE. Fork, tin branch and climber points as noted. It reads on `#080c1c` (s160). |
| tree_with_beds | FIX 7. |
| water_tank_beds | FIX 7. Riveted tank and stand are good. |
| steam_locomotive_1898 | APPROVE. The charcoal boiler with brass bands reads on night skies. No text. |
| rail_truck_open | APPROVE. |
| tsavo_bridge | APPROVE. |
| tsavo_bridge_unfinished | APPROVE. |
| lion_trap | APPROVE the drawing (not a torture device). FIX 5 (front overlay) is needed before keyframes. |
| lion_trap_bent_bar | APPROVE the drawing. FIX 5. |
| machan_platform | APPROVE. Properly flimsy and crooked. |
| donkey_carcass_outline | FIX 6 (readability only; gore check passes). |
| stick_man_sitting | APPROVE. Crude tier, `auto_ink` works on navy, no cap. |
| patterson_hat | APPROVE. Sits correctly on `stick_man_plain` (head centre -368 x scale). **Director:** use -368, not -376. |
| narrator_hand_side | FIX 8. |
| lion_sketch_paper | APPROVE. The fluffy-maned "everyone's lion" is a deliberate contrast. Flat mouth, no smile, pencil grey. |
| lion_skull_broken | APPROVE. Clean diagram bone, broken lower canine with a dark (not red) spot, no gums or flesh. |

## DAYS WITHOUT AN INCIDENT board: PASS (approved)

Checked at full res on s002, s020, s040, s108, s109, s146, s155 and s163.
- Chalkboard `#2f3a33`, 5 px `#a0522d` frame and white `#f4f4ee` bold size-28 text. It is on-palette and fits the HUD board family
  (HEAD COUNT 054, DISTANCE TO FISH 060). It reads on sunset, pale day (s020), the night navies and the death black (s109).
- The longest value fits with margin inside the frame. The board (x 1345-1835, y 212-266) is inside the reserved counter zone
  (x 1300-1860, y 110-275) and inside the safe area (x ≤ 1856).
- Values follow the spec: 0 → 1 (s019) → 0 (s039) → 1 (s057) → 0 (s072, s092, s109) → 1 (s128) → 2 (s146). The board is absent on
  s001, the sober cards s015/s089, and from s163 on.
- The s109 wipe smear is visible but subtle. That is fine.
- The in-scene s108 board ("DAYS WITHOUT / AN INCIDENT / 0") is legible at 1080p.
- s163 gag (board, wipe, black, flat plank, THUD, lion eyes) reads well.

Add to the art bible as a reusable HUD board once the episode ships.

**Next:** illustrator applies fixes 1-8 and re-previews the lions, donkey, beds, hand and trap overlays. Director applies the
layering in fix 5, the s027 neck placement and the hat -368 offset. Then I re-check the changed assets in context (s027, s091,
s116, s121, s160 at minimum).

## Round 2: re-check of fixes 1-8 (art director, 2026-11-28): PASS (assets) / director items OPEN

What I checked: the 15 changed or new assets through `build/check_assets.py` (white, `#0f1a36` and silhouette + grey rim on
`#080c1c`, against the requested bbox), plus zooms at 2.4-4x on the lion head, standing lion, looking_up, both bed sets,
the hand and the donkey. I also re-rendered s027, s091, s102, s116 and s160 in context. Note: `assets/previews/061-tsavo-lions-bridge-fixes.png`
crops most tiles (looking_up shows no head, the beds and trap tops are cut off), so it can't be used for approval. I judged from the re-renders.

| Fix | Result |
|---|---|
| 1 Lion head | **PASS.** Long boxy muzzle, flat bridge, broad dark nose pad, squared jaw, closed flat mouth, small ears set back. All 7 lion drawings now read as a lean maneless lion. The head silhouette says "big cat". In context, s091 (sitting) now reads as a lioness, not a bear, and s160 (looking_up) reads as a lion staring up the tree. The CD conditions still hold: amber dot eye, flat brow, no smile, no teeth or claws. Every key-point move is within 15 units and is logged in `asset_requests.md`. The director should re-check the eye and nose anchors in sitting/looking_up/head shots. |
| 2 Stray spray | **PASS.** No speckle outside the outlines on any lion, on navy or as silhouette. |
| 3 looking_up brow | **PASS.** The brow sits on the forehead and the eye is a clean amber dot. |
| 4 Throat fringe | **PASS.** 4 tapered strokes, no letter-like glyphs. |
| 5 Trap overlays | **PASS (asset).** `lion_trap_front` and `lion_trap_bent_bar_front` contain bars, rails, posts, the door and the bent bar. Same anchor and bbox, transparent between the bars. |
| 6 Donkey | **PASS.** Long squared head, two laid-back ears, upright mane, folded thin legs with hooves, tufted tail. Still pale, gore-free, no eye, nothing red. Reads as a donkey. |
| 7 Beds | **PASS.** White pillow, grey humped blanket and short legs on both `tree_with_beds` and `water_tank_beds`. In s102 they read as beds. |
| 8 narrator_hand_side | **PASS.** Dark triangle gone. Reads as a white-glove pinch (curled forefinger, thumb at 0,0, knuckle lines, sticker dot), and it matches `narrator_hand`. |

**Asset verdict: APPROVED.** All 29 episode assets plus the 2 new overlays are approved for keyframes.

### Still open (director): `shotlist.json` has not changed since round 1

1. **Trap layering (fix 5), s111-s128:** no shot uses the overlays yet (0 references). In s116 the soldiers still sit over the
   front bars. After each `lion_trap` / `lion_trap_bent_bar`, add the occupants (lion, soldiers, Doug, lamp), then
   `lion_trap_front` / `lion_trap_bent_bar_front` at the same x, y, scale and flip.
2. **s027 lion head:** the black `tsavo_lion_head` silhouette is still a huge slab beside the tent wall, not coming out of the
   doorway. It also has no rim, so on `#3a3050` it reads as a black box, not a lion. Fixes:
   - Place the head so the muzzle comes out of the dark doorway with the cut neck end (x -260) hidden inside it.
   - Scale it down so it is no wider than the tent.
   - Add `rim: {color: "#8a8a8a", px: 3}` so the muzzle and ear outline reads.
   - Remove the red spray glow behind it: on the purple night it reads as a blood mist, which is gore-adjacent. If you want a
     danger cue, use a pale amber eye glint or a plain dark vignette.
3. **Patterson hat offset:** still -376 (s005: man y 810, hat y 689.7, scale 0.32, so 120.3/0.32 = 376). Use head-centre
   **-368 x scale** in all 22 hat shots: s005 s006 s100 s106 s110 s111 s130-s135 s139-s143 s151-s153 s157 s158.

**Next:** the director applies items 1-3. I then check the final keyframes in context (s027, s111-s128, plus every hat shot)
before `art_approved`.

## Round 3: keyframe review (art director, 2026-11-28): FAIL (director fixes only, no asset changes)

What I checked: all 15 contact sheets (s001-s174 + endslate) for style, plus full-res crops of s027, s064, s100, s111, s116, s120,
s127, s131 and s153, and `shotlist.json` for the overlay order and the hat offsets.

### Round 2 open items

| Item | Result |
|---|---|
| 1 Trap layering, s111-s128 | **PASS.** All 14 trap shots draw `lion_trap` / `_bent_bar`, then the occupants, then `_front` at the same x, y and scale. In s116 the soldiers sit behind the front bars, and the lamp, lion and Doug-with-lunchbox (s126-s128) are inside too. |
| 2 s027 lion head | **PASS.** The head is now scaled to the doorway, the muzzle comes out of the dark opening, the neck end is hidden in the black, the grey rim reads, and the red spray is gone (only an amber eye dot). Reads as "lion at the door", not a slab. |
| 3 Patterson hat | **PASS.** Every standing/arms-up shot is at -368 x scale (s005 s006 s100 s106 s110 s111 s130 s151-s153 s157 s158). The sitting shots (s131-s135, s139-s143) use -218 x scale on `stick_man_sitting`, and the s131 zoom shows the hat sitting correctly on the head. |
| s120 / s127 red glow | **FAIL.** See fix 1. |

### Style across the sheets: mostly PASS

Doug is on-model in every shot (cap, auto-white ink on the navies, black on cream). The HUD counter and DAYS board are consistent
and inside the safe area. The zone ramp holds: sunset open, cream diagram cards, purple "Tent" night, navy thorn/trap/platform
nights, near-black last lion and the death blacks. Lion silhouettes keep the approved head. Nothing gory: the donkey is pale and
eyeless, the skull is clean bone, and the deaths are a cap, a lunchbox, a plank and eyes.

### Fixes (all to the **director**)

1. **s120, s127: remove the red `#e0201b` spray behind the trapped lion.** Inside the cage it fills the boards between the bars as
   red speckle, right beside the soldiers (and Doug in s127). It reads as blood spatter in a box, which is the same blood-mist
   problem we removed from s027. Replace it with the purple `#5e4670` glow (art bible "red glow" rule) or drop it. Add
   `rim: {color: "#8a8a8a", px: 3}` to the `tsavo_lion` silhouette so it separates from the dark boards, as in s027. For the
   "throwing itself against the bars" beat in s120, put 2-3 white motion strokes by the lion's shoulder. The `shake` camera is fine.
   The red glow on the open-ground silhouettes (s002, s022, s028, s054, s139, s140, s152) is standing/walking animals on open
   ground. That is the normal reveal glow, so keep it.
2. **s112-s128: the same wide trap shot repeats too often.** s112-s117 is 6 identical framings in a row, s119-s122 is 4, and
   s124-s128 is 5 (s114's 1.1 zoom doesn't change the read). This breaks the "not the same composition 5 times in a row" rule
   for the most tense stretch of the video. Re-frame these as close inserts by scaling/offsetting the trap and its overlay together
   (same values for both). No new drawings are needed.
   - **s114:** close on the iron divider (trap ~2.5x, the divider rail near frame centre) with the `3 IN (7.5 CM)` marker between
     two rails. Doug is optional.
   - **s116:** close on the men's room: the two soldiers and the lamp fill the frame behind the front bars. Crop out the lion room.
   - **s117:** close on the door end (the left posts and the door), with the warning triangle and Doug peeking in from the left.
   - **s121:** close on the two frightened soldiers, with the edge of the lion silhouette visible through the divider. Keep
     `TOO FRIGHTENED`.
   - **s124:** close on the door's bent bar (`lion_trap_bent_bar` + `_front` ~2.5x). Keep the `ONE BAR` arrow.
   - **s127:** close two-shot: Doug (gritted, lunchbox) and the soldier in the foreground, the lion silhouette through the divider.
   After this the longest run of the wide framing is 2 (s112-s113, s119-s120, s125-s126). At close scale, keep the top rail
   and bars out of the HUD zone (x 1300-1860, y 110-275) and below the chapter tab. Put the counter board back on top if you can't.
3. **s064, s065: replace `lion_head_icon`.** The library icon is the old round egg head with small round ears and cheek puff. At
   pride-row size it reads as hamsters, which is exactly the problem round 2 fixed on the episode lions. Use a row of small
   `tsavo_lion_sitting` (~0.14 scale, feet on one baseline at y ~600, 110-120 px apart) under SMALL PRIDE / BIG PRIDE / TSAVO PRIDE.
   They read as a pride and match the episode lion.
4. **s111: off-palette and floating.** The flat `#2a4a6a` full-frame with no ground leaves the trap and Patterson hanging in space,
   and that blue appears nowhere else in the episode. Use the Walkout night (navy `#0f1a36` sky, `#1e1b16` ground, ground line)
   with the trap and Patterson on the ground line. If it is meant as an idea card, use the cream `#f4f1dc` diagram card and dark ink.
5. **s143 (nit): s142 and s143 have the same frame** (platform, two sitters, dark ground). The only change is that the eyes are
   removed. For "He shot it later that night", add the yellow `BANG` sound text (s123 style, no rifle drawn, per the CD
   conditions) and have the lion eyes gone. Or cut to a tighter platform framing so the beat changes visibly.

**Not an issue:** s001 is the thumbnail placeholder (graphic designer). The s129 counter text is cut by the hand on purpose. s100
and s106 repeat the bridge on purpose, 6 shots apart.

**Next:** the director applies fixes 1-4 (5 optional) and re-runs `python -m studio keyframes 061-tsavo-lions-bridge --shots
s064,s065,s111,s114,s116,s117,s120,s121,s124,s127,s143`. I then re-check those shots only. When those pass, this is a PASS for art,
and the visual-screener runs before `art_approved`.

## Round 4: keyframe re-review (art director, 2026-11-28): FAIL (one small director fix)

What I checked: the round 3 shots at full res (s064, s065, s111, s114, s116, s117, s120, s121, s124, s127, s143), sheets 10-11 for the
whole trap run in sequence (s111-s132), the new asset previews (`061-tsavo-lions-bridge-fixes3.png`, `-fixes3-ground.png`,
`-rifle-lap.png`), and the lion layers in `shotlist.json` for s120-s127. I judged the rifles on style only. Whether rifles go in at all
is the creative director's call, because the CD condition at the top of `asset_requests.md` says "No rifles anywhere".

### New assets: PASS
- **`stick_man_arms_up`:** the arms now start at the neck below the head and clear it. No more antennae. The head centre is unchanged, so the hat offset still fits.
- **`tsavo_lion_sitting`:** reads as a cat now: ears, pale muzzle, long front legs and a tail tuft at the paws. It matches the episode lion and reads at 0.14 in the pride rows. Nit: the front legs are very straight, like planks. That is fine for this episode.
- **`tsavo_lion_lying`:** peaceful, with a closed-eye curve and no wounds. It is the detailed tier and on palette. Not gory.
- **`rifle_held`:** plain period rifle in flat wood and steel, with no flash or smoke. It is the same detail tier as the lamp and the lunchbox. On the laps the muzzles point up and away from the lion room.

### Round 3 fixes
| Fix | Result |
|---|---|
| 1 s120/s127 red spray | **PASS.** The red is gone, the glow is off and the grey rim is on. s120 has white motion strokes and no blood read. |
| 2 Trap framing variety | **PASS.** s114 is close on the divider, s116 the men's room, s117 the door end, s121 the frightened soldiers, s124 the bent bar and s127 the two-shot. The wide framing now never runs more than 2 shots. The HUD and chapter tab stay legible over the close shots. |
| 3 s064/s065 pride rows | **PASS.** The rows of small `tsavo_lion_sitting` sit on one baseline and read as a pride. No more hamsters. |
| 4 s111 | **PASS.** Walkout navy, dark ground and ground line. Patterson and the trap stand on the ground. |
| 5 s143 | **PASS.** The yellow BANG is s123 style, no rifle is drawn, and the lying lion is under the platform. The shot is now clearly different from s142. |

### Fix (director)
1. **s120, s127: the lion switches between a black silhouette and the tan lion inside the trap.** It is tan in s121, s122, s123 and
   s125, but a black silhouette in s120 and s127. The trap interior is lamp-lit boards, so the tan lion is the consistent read.
   In the s127 close crop, the silhouette's edge at the left frame edge is just a black blob with an ear, not a lion. Fix: on the
   `tsavo_lion` layer in s120 and s127, remove `silhouette: true`, `glow_r` and `rim`, which makes it identical to s121.
   Keep the `appear` timing. In s120, move the motion strokes about 60 px up and left so they sit on the shoulder and leave the head clear.

### Nits (fix if cheap, not blocking)
- **s117, s124:** a sliver of soldier head and rifle is cut by the right frame edge (x ~1840-1920). Either nudge the trap so the
  soldier is fully out of frame, or drop that soldier's layers (man and rifle) from these two shots.

**Next:** the director applies fix 1 and re-runs `python -m studio keyframes 061-tsavo-lions-bridge --shots s120,s127`. If s120
and s127 show the tan lion, this is an art PASS and no further review round is needed. The visual-screener then runs before
`art_approved`.
