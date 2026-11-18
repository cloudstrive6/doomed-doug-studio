# 051 art review

## Round 1 (art director, 2026-11-18)

Checked: `assets/previews/051-great-white-flees-orcas-assets.png`, plus test renders of each flagged asset at its shotlist scale on
its real ground (dusk `#14365e`, kelp `#4f8a7f`, cream `#f4f1dc`, sky `#cfe9ff`), and 15 in-context keyframes
(s002, s007, s016, s022, s030, s036, s044, s045, s048, s052, s053, s067, s084, s112-s114).

### SHARKS GONE meter (relabel of the 022 `wait_stopwatch`): APPROVED
It's the art bible "second meter under the counter" layout (size-28 `label` at (1590, 238), icon at 0.16, icon right edge ~30 px left
of the label box). "SHARKS GONE: ABOUT 5 MIN" is the widest value and ends at about x 1805, inside the safe area. The red
`#ffd2cc` / `#e0201b` state at The Empty Bay follows the 009/049 precedent. Nothing needs drawing.

### New assets (21): FAIL (5 asset fixes for the illustrator, 3 composition fixes for the director)

These 15 pass as drawn: `orca_fin_bent`, `southeast_farallon_island`, `elephant_seal_pup`, `tour_boat`, `central_california_map`,
`fire_alarm_pull`, `great_white_beached`, `shark_liver_icon`, `great_white_cutaway`, `oil_drop`, `fuel_gauge_full`, `costume_xray`,
`speed_camera`, `autumn_leaf_icon`, `snowflake_icon`. They're on palette and detailed-tier. There's no gore: the beached shark is a
clean outline with X eyes, and the liver is a flat icon. The pups are animals, not plush toys.

The illustrator's flags, resolved:
- **`orca_fin_bent` size: OK as drawn.** It's 280 x 256, as requested, and the bend reads clearly from 0.18 up (s007 is good). At
  0.10-0.12 it shrinks to a ~28 px black hook and the grey highlight disappears. That's a placement problem, so it's director fix 7.
- **`fuel_gauge_full` needle: OK as drawn.** It points at the last tick above F, mirroring the library low needle, and sits clear of
  the F letter. A needle flat on the F end-stop would run through the letter. Side by side with `fuel_gauge` at 0.9, it reads as full.
- **`shark_costume_sevengill`, `kelp_stalk`, `elephant_seal_bull`: fixes required (below).**

#### Illustrator
1. **`kelp_stalk` reads as a palm tree.** In s053 and s067, four of them stand on the green water: a straight trunk, a round
   "coconut" float, and fronds that fan both ways and droop back down. Make it read as kelp in current:
   - Shrink the float bulb to an elongated, olive bulb about 40 x 60 that is the same colour as the stipe. It must not be a round,
     lighter ball.
   - Have all fronds leave the bulb on **one side only (+x)**. Make them long, flat, ribbon-like straps (about 6-8 of them, each
     250-400 local long) streaming sideways and slightly up, as if pulled by the swell. None should curl back down below the bulb.
   - Give the stipe a longer, gentle S-bend so it isn't a ruler-straight trunk.
   - Keep the brown body and dark outline, the anchor, and the 720 height.
2. **`shark_costume_sevengill`: you can't count the seven gills.** At 0.6 (s067) and 0.45 (s068-s069), three lines sit on the white
   belly panel and read as the original printed gills. The other four bunch into a blur on the 15 px felt strip at the right edge.
   - Make the panel narrower on its right side (pull its right edge in to about local x +10), so there's a clear grey felt band
     from x +10 to +115.
   - Draw all seven marker lines on that felt band, not on the panel. Make them black, width 5-6 at scale 1, about 70-90 local long,
     still wobbly and uneven, but with a gap of at least 12 local units between lines.
   - Remove any of the original three gills that survive under them.
   - Check at 0.45: you must be able to count seven separate lines.
3. **`elephant_seal_bull`: a stray whisker line.** It's a single long thin line from the proboscis tip toward the chest, and it pokes
   out of the s112 silhouette as a hair-thin spike. Replace it with 3 short whisker ticks (about 25 local long) that start inside the
   outline.
   - Recommended, not blocking: drop the outline seam where the proboscis joins the face and blend its fill into the head. At the
     moment it reads slightly like a floppy ear. Add a short closed mouth line under its tip.
   - The chest shield's scallop texture is fine. It doesn't read as scars.
4. **`elephant_seal_bull_flat`: the chest shield reads as a sore.** In s114 and in the test render, it has become a floating
   pink-brown oval with speckles in the middle of the grey body, so it looks like a rash or a wound patch.
   - Move it to the front underside behind the head, running down to the ground line like in the upright bull.
   - Use the same muted pinkish-grey with the scallop texture, and no speckle cloud.
5. **`sevengill_shark` and `bronze_whaler`: the mouth lines curve up into a faint smile** (in the test render at 1.0, the sevengill's
   is the more visible one). The sevengill is the hero at 0.65-1.0, and the brief rules out smiles. Make both mouths straight or
   slightly down-turned. Nothing else changes.

#### Director
6. **The pups float above the Farallon terrace.** In s016 the pups are at y 285, but the island's ledge is at local -148
   (430 - 148 x 0.7 = y 326). So they hover about 40 px up, and the left one overlaps the lighthouse.
   - Put pup anchors on y = waterline - 148 x island scale.
   - Keep them inside the ledge: island x + 40 x scale to island x + 380 x scale.
   - Apply this to every pup-on-island shot (s016, s094-s095, s097, s122, s130-s133). Use fewer or smaller pups if they don't fit.
7. **`orca_fin_bent` map icons are too small to read as bent.** Raise it to at least 0.16 in s084 (now 0.10), s166 and s173 (0.12).
   s007 at 0.18 is the target.
8. **The s067 arrow points at Doug's cap, not the gills.** The "7" arrow lands at the cap brim (about 960, 450). Re-aim its tip
   at the new gill band, about (935, 560) at 0.6. Do this after fix 2 lands.

Re-check: after fixes 1-5, re-run `python -m studio asset-preview` for those 6 assets and re-render keyframes s016, s053, s067,
s084, s112-s114. Rounds 2+ only cover these items.

## Round 2 (art director, 2026-11-18): FAIL (1 asset fix, 2 composition fixes, all small)

Checked: `assets/previews/051-great-white-flees-orcas-assets-r2.png` (6 redrawn assets), the 18 contact sheets, and full-res keyframes
s016, s053-s057, s062-s069, s071, s084, s094-s097, s112-s114, s122, s130-s133, s137, s142, s166, s173.

### Round 1 items
1. `kelp_stalk`: **PASS.** It's no longer a palm. The S-bend stipe, the stipe-coloured elongated bulb and the 7 ribbon fronds
   streaming +x (none drooping back down) read as kelp in a current, on every Cousins shot. The wider frond spread caused a placement
   regression in nearby shots (fix B below).
2. `shark_costume_sevengill`: **PASS.** The panel ends at local x 0 and the felt band carries 7 separate marker lines. I counted all
   seven at 0.6 (s067) and at 0.45 (s068). The widened right side keeps Doug's legs inside the suit's footprint and his head sits
   cleanly on top, so it stays on-model. The asset's `description` is stale (fix A).
3. `elephant_seal_bull`: **PASS.** The s112 silhouette is clean with no spike. The proboscis seam is gone and the mouth line is in.
4. `elephant_seal_bull_flat`: **PASS.** The shield now sits at the front underside, reaches the ground line, matches the upright bull,
   and has no speckle. It reads as a chest, not a sore.
5. `sevengill_shark`, `bronze_whaler`: **PASS.** Both mouths are straight or slightly down-turned, with no smile.
6. Pups on the terrace: **PASS.** In s016 and s094 they sit on the ledge line (y 326), stay inside it, and are clear of the
   lighthouse. Correction to round 1: s095, s097, s122 and s130-s133 have no pups on the island, so nothing was needed there.
7. `orca_fin_bent` at 0.16: **PASS.** The bend reads clearly in s084 and s166. s173 is on a smaller map but still reads.
8. s067 arrow: **re-aimed correctly, but the arrowhead now covers the thing it points at.** The tip at (935, 560) puts the ~45 px red
   head over gill lines 4-6, so the "7" can't be counted in the very shot that counts them (fix C).

### Required fixes
#### Illustrator
A. **`shark_costume_sevengill` description is stale.** It still says "gill lines x 14..79, running over the belly panel edge" and
   "bbox about x -196..+124". Update it to match the drawing: belly panel x -46..0, 7 gill lines on the felt band x +8..+113,
   y -82..+12, bbox x -196..+156. Other shotlists place it from this text. This is metadata only; the drawing doesn't change.

#### Director
B. **The widened kelp fronds swallow Doug and the orca on the left kelp pair.** The fronds of the kelp stalks at x 150/380 (scale 0.8)
   now fill roughly x 90-700, y 414-560.
   - s055, s056: the diver's head sits inside the frond tuft.
   - s057: Doug's head and cap sit inside it, with a sevengill crossing him.
   - s062: the orca silhouette's bent fin, the subject of the shot, lies on top of the fronds.

   Move these subjects below the tuft, onto the clear water between the fronds and the floor:
   - s055-s057: Doug/diver (330, 600) to (330, 790).
   - s056-s057: the sevengill at (520, 560) to (560, 780), if it's meant to stay beside him.
   - s062: `orca_bent_fin` (330, 520) to (360, 720).

   Check that the bent fin's tip ends up on open water, not over a stipe.
C. **s067 arrowhead covers the gills.** Stop the arrow at the suit's right edge so the head sits outside the lines. Set `to` to about
   (985, 545) and leave `from` (1250, 400) as is. All 7 lines must stay visible once the arrow appears.

### Non-blocking notes
- s166: the red migration arrow starts at (515, 905), below the map frame's bottom edge (y ~893), so its tail pokes out of the map.
  Starting it inside the frame, about (520, 875), would be tidier.
- s068: in the `float` pose, Doug's right arm pokes out past the costume's top-right corner as a thin stick. Using `stand` or a
  hidden-arm pose under the costume would be cleaner.

Re-check: re-render s055-s057, s062 and s067. Round 3 covers only fixes A-C.
