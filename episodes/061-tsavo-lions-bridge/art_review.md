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
