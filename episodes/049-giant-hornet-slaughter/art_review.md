# 049 art review (art director, 2026-11-16)

## Verdict: FAIL (assets PASS, keyframes FAIL on composition)

The new library drawings are good and approved. The keyframes are on-style, the zone ramp is coherent (it is now in the art bible
as the "insect-raid afternoon to pre-dawn" ramp), and nothing is gory. Doug is on-model and the cap shows in every shot. The TARGET HUD
icon reads at 40 px. The fixes below are layout-rule breaks (narrator hand, counter zone, map frames, Doug's legs on night ground),
two runs of near-identical hive compositions, and costume continuity. They are all director fixes in `build/gen_shotlist.py`. Re-render
only the listed shots, then send them back to me.

## Assets (all new files in commit 79642ab): PASS
Previews: `assets/previews/049-giant-hornet-slaughter-assets.png`, `049-giant-hornet-slaughter-places.png`, `049-b1.png`.
- Two-tier rendering is correct. Creatures, props and places are the detailed tier (layered fills, spray shading, outlines 3-5).
  `hiker`, `hornet_crew_member` and `gloved_hand` are crude tier. The costumes keep Doug's face and cap clear in every pose (checked in
  s021, s088, s109, s132, s134).
- No gore: `meat_ball_bundle` and `brood_bundle` are plain bundles, `honeybee_dead` bees are whole with X eyes and no fluid, and
  `hornet_larva_cell` has no face. Nothing is cute (no pupils or smiles on bees, hornets or larvae).
- `the_target` reads as an archery target at scale 0.2 and looks nothing like 041's price tag or 043's fingerpost.
- Silhouettes are bold (`bee_heat_ball` s091, `hornet_stinger` s114, `nest_tree` s173).
- **Fixed by me:** `bee_costume_flat` and `hornet_costume_flat` now have a grey zipper seam and pull tab at the collar. The dark collar
  hole on the right end could read as a headless animal at phone size. The zipper makes it read as an empty suit (s068, s111, s112,
  s131 pick this up on re-render; nothing else changes). The illustrator can refresh the preview sheet whenever convenient.
- Note for later: `honeybee_dead` is slimmer than the "round and chunky" spec. The X eyes still read at 0.26-0.32 (s002, s052), so it passes.

## Keyframes: FAIL. Required fixes (director)
1. **Narrator hand enters through the top edge (s065, s066).** `narrator_hand` at (1000, 500) and (1010, 620), flipped, scale 0.9-1.0: the
   arm comes down from the top-left corner. Art bible rule: it enters from a **side** edge below y 120. Bring it in from the left edge
   (arm horizontal or angled up from below about y 400), and keep it clear of the "BEE COSTUME" / "EVEN UP" wordart.
2. **Counter zone (x 1300-1860, y up to 260 with the TARGET meter; wordart/labels must stay at y ≥ 290 where they overlap x 1300+):**
   - s116 label "BEEKEEPER'S SUIT" at (1210, 270), size 36, runs to about x 1400 at y 247-293. Move it to about (1210, 340) or put it under the
     fabric strip.
   - s074 wordart "FAT" at (1250, 270) ends against the target icon. Move it to about (1150, 330), or set both words to y ≥ 330.
   - s195 wordart "HALF" at (1300, 330), size 110: glyph tops sit at about y 285. Drop it to y 360.
3. **Text crosses a map frame (s154, s158).** s154: the "ONE CONTINENT." header sits on the `north_america_map` top frame and coastline.
   Shrink or lower the map (scale 0.6, centre y 720) and keep the header in clear navy above it. s158: "FIRST TIME" crosses the
   map's bottom frame line. Shrink and raise the map, as in the art bible's map rule, or move the word to the right margin.
4. **Same composition too many times in a row.** Hive-centre, Doug-left, hornet-at-entrance:
   - s025-s033 is 9 near-identical frames (s027-s033 alone is 7, past the 2-6 beat group). Break it with two different layouts. **s029**
     ("rubbing a gland at the very tip of its abdomen"): a cream `#f4f1dc` diagram close-up, using `hornet_stinger` (or the `asian_giant_hornet` at 1.0)
     with a red circle on the abdomen tip, the "GLAND" label and a soft orange scent spray. **s030/s031** ("invitation", "other hornets pick up
     the scent"): a wide map-like shot, with `hollow_tree` far left, the hive far right and the orange scent ribbon drifting between them while
     hornets follow it.
   - s058-s063 is 6 in a row on the same amber hive layout. Change **s061** ("the adult bees are just in the way") to a close-up
     (`asian_giant_hornet_front` at about 0.8 brushing a single `honeybee` aside with a red arrow) and **s062** ("survivors get ignored") to a
     ground-level shot (a few live bees at the front, the hornet walking past them into the hive in the background).
5. **Costume continuity, items 1-4 (brief section 4: bee costume through The Occupation; the cap always on top).** Doug drops the costume on
   every cream diagram card and then puts it back on in the next shot. That also undercuts s021's "which is exactly why Doug is dressed as a
   bee". Add `bee_costume` at Doug's x/y/scale (use `bee_costume_crouch` for crouch) in s007, s012, s013, s019, s020, s034-s037, s050,
   s053-s056, s081-s083, s085-s087, s094, s105-s107. Keep Doug plain only where intended: s003 (the boss tease) and s064 (the 010
   flashback).
6. **Doug's legs disappear on the pre-dawn ground (s003, s191, s192).** Doug stands in front of the pale cut wood of `nest_tree_open`, so
   his ink stays black and his legs (on `#141e1a`) barely read. Add a torch-light pool, an ellipse `#3a4a40` of about 260x60 under his feet
   (the crew worked with lights before dawn), or move his feet onto the stump base. Re-check that the hand still lands on the right half's
   cut edge.
7. **Zone colour (s152, s153).** These two shots are captioned THE TOLL but already use the Hitchhiker navy `#1b2f5a`. Keep them on the sober
   `#15181a` until the "ONE CONTINENT." card (s154). The art bible says every shot of an item stays on its item colour.

## Recommended (not blocking)
8. s199 (closing image): the radio tag on the cap is about 10 px at `doug_cap_radio_tag` scale 0.6, which is the kicker's whole joke. Raise
   it to 0.9-1.0 (cap centre about (960, 630)), or add a small label "RADIO TAG" left of the hollow.
9. s142: four tile captions (GIANT HORNET / HORNET / WASP / BEE) exceed the 2-label cap. I accept them as a legend row on a sober card. If
   you touch the shot anyway, drop "HORNET" and "BEE" (the drawings read on their own).
10. s091: the heat-ball silhouette's red glow is almost invisible on `#5a4b3d` brown. Use the bible's dull purple glow `#5e4670`
    with `glow_r` about 0.7 x 560 x scale, or move the tease to the dusk purple `#8a6a8a`.
11. Wordart bottoms in s101, s162 and s197 land at about y 1030. They are inside the safe area, but only just. Raise them by 20 px when
    re-rendering nearby shots.

## Not mine
- s001 shows "(thumbnail pending)". The graphic designer owns the thumbnail and opening image (brief section 1: huge hornet over an X-eyed
  bee pile, tiny Doug in the bee costume, no gore).

## Re-render list
s003, s007, s012, s013, s019, s020, s029, s030, s031, s034-s037, s050, s053-s056, s061, s062, s065, s066, s068, s074, s081-s083,
s085-s087, s094, s105-s107, s111, s112, s116, s131, s152, s153, s154, s158, s191, s192, s195 (plus s091 and s199 if you take the
recommendations).
