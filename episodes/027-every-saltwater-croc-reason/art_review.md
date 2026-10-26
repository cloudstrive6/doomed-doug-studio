# 027-every-saltwater-croc-reason: art review (assets)

Reviewer: art director, 2026-10-26
Scope: the 37 new library assets in `asset_requests.md` (previews `assets/previews/027-every-saltwater-croc-reason-assets.png`
and `-assets-small.png`). Each one was re-rendered at scale 1 on its target background with the requested bbox overlaid, and
nine test keyframes were rendered (s037, s040, s071, s114, s115, s181, s201, s213, s229) to check them in context.

## Verdict: FAIL (round 1). 32 APPROVE, 5 FIX (illustrator)

Hard rules all pass. **No gore**: no blood, wounds or limbs anywhere, and the only thing in a mouth is the hatchling or the grey
shape. **Jaws are closed** on every new croc (the tongue close-up is the one requested open-mouth exception and holds no food).
**No body-length leap**: `croc_lunge_rising` has only the head and about the front third above the splash, and the rest of the body
and tail are a dark submerged shape. Every croc uses the `saltwater_crocodile` palette. The alligator reads darker, with a blunter
snout, and the thin-snout croc reads clearly different. Hatchlings are slim and banded with small eyes, so they are not cute.
The sober cards are muted, with no people, logos or readable text.

The failures are three close-ups whose cut neck or jaw edge lands mid-frame (style bible rule from 026: no severed-looking ends),
plus two weak reads.

## Fixed by the art director (trivial, already in the JSON)
1. `alligator_head_water`: the smoothed outline made a black spike at the snout tip, out to about x +270, past the bbox and nothing
   like an alligator's U snout. I added bottom points so the tip is round, and the asset now sits inside x -230..230.
2. `mangrove_clump`: the five trunks stopped about 15 units under the canopy and looked like floating posts (visible at 0.9 on the
   Lunge tree). I extended the trunk tops 45 units up under the canopy.
3. `croc_jaw_closeup` / `croc_jaw_closeup_lit`: the 19 belly-crease strokes ran 10-20 units below the lower-jaw outline. They showed
   as whiskers on dark grounds. I clamped them inside the outline in both files, so the geometry still matches for the overlay.
4. `croc_tongue_closeup`: the 54 salt-gland pores were red-brown `#5a3028` on flesh pink, which reads as blood specks or scabs at
   phone size. I recoloured them to neutral grey `#4a4a44` with outline `#2a2a26`.
Check preview: `assets/previews/027-every-saltwater-croc-reason-artfix.png`.

## Per asset
| # | Asset | Verdict | Note |
|---|---|---|---|
| 1 | mangrove_clump | APPROVE | after fix 2. Reads as mangrove (prop roots), not palm or pine |
| 2 | croc_jaw_closeup | **FIX** | after fix 3. Cut neck edge sits mid-frame (fix A) |
| 3 | croc_jaw_closeup_lit | **FIX** | same as #2 (fix A). Glow dots good, densest on the jaws |
| 4 | saltwater_crocodile_lit | APPROVE | geometry matches the base, dots over the whole body |
| 5 | alligator | APPROVE | darker, blunt snout, upper teeth only |
| 6 | alligator_head_water | APPROVE | after fix 1. Reads on `#0c0f12` |
| 7 | croc_tongue_closeup | **FIX** | after fix 4. Flat cut edge at the hinge end, mid-frame in s071 (fix A) |
| 8 | croc_swimming | APPROVE | reads on `#3a9ad9`, wake, jaws closed |
| 9 | croc_nest_mound | APPROVE | a pile of vegetation, not a rock |
| 10 | croc_nest_cutaway | APPROVE | 24 eggs, same footprint |
| 11 | croc_egg | APPROVE | |
| 12 | egg_carton | APPROVE | |
| 13 | croc_mother_hatchling | **FIX** | jaws closed, hatchling fine. The neck ends in a flat ribbed slab mid-frame in s114/s115 and reads as a cut-off head (fix A) |
| 14 | croc_hatchling | APPROVE | not cute |
| 15 | croc_sleeping | APPROVE | eye closed (lid curve), legs splayed |
| 16 | croc_in_sling | APPROVE | jaws taped, hook at (0,0) |
| 17 | cape_york_map | APPROVE | tip and both coasts within about 10 units of the requested lon/lat points |
| 18 | car_trailer | APPROVE | |
| 19 | bathtub_croc | **FIX** | head is a box with a vertical back edge sitting on the rim (fix B) |
| 20 | croc_bounding | APPROVE | all four feet off the ground, small |
| 21 | croc_coiled_underwater | APPROVE | |
| 22 | croc_lunge_rising | APPROVE | front third only, jaws closed, splash crown is pale blue (not the white iceberg zigzag) |
| 23 | croc_holding_shape | **FIX** | the grey shape sits on top of the snout like a pebble, not clamped in the jaws (fix C) |
| 24 | croc_top_c | APPROVE | legs folded, reads on `#2a3040` |
| 25 | thin_snout_croc | APPROVE | no gharial knob |
| 26 | spinning_top | APPROVE | |
| 27 | croc_eyeshine | APPROVE | reads on `#0b0d10` |
| 28 | croc_trap_floating | APPROVE | see-through bars, so the cap will show |
| 29 | city_skyline_small | APPROVE | low, within y -240 |
| 30 | city_skyline_night | APPROVE | |
| 31 | myanmar_coast_map | APPROVE | Ramree outlined with mangrove hatch, Cheduba disc, no labels |
| 32 | record_book | APPROVE | blank gold plate, no title |
| 33 | record_book_open | APPROVE | right margin around (+230,0) is clear |
| 34 | old_book | APPROVE | |
| 35 | indonesia_map | APPROVE | |
| 36 | indonesia_map_ntt | APPROVE | Flores, Sumba and west Timor only (Timor-Leste left grey), aligned to the base |
| 37 | nt_map_sepia | APPROVE | Tiwi Islands and Groote present, no labels |

## Required fixes (route to the illustrator)
**A. Cut edges must leave the frame (#2, #3, #7, #13).** Extend the neck (or the throat, for the tongue) as a continuous body with the
same fills, scute row and belly band. Leave the far end open, with no closing outline, and push it past the frame at every placement
in the shotlist:
   - `croc_jaw_closeup` + `_lit` (s037-s053 at x 1180, scale 1.0, and x 1280-1300, scale 0.8): extend to local x **-1650**. The neck may
     widen slightly and run straight left. The `_lit` dots stay on the head only (sensor beat), and both files keep identical geometry.
   - `croc_mother_hatchling` (flipped; s114 x 1150 scale 0.9, s115 x 1000 scale 1.4): extend the neck and shoulder to local x **-900**, sloping
     down to the waterline.
   - `croc_tongue_closeup` (s071 x 960, scale 1.1): extend the jaw rims and pale throat to local x **-900**.
   Update the bboxes in `asset_requests.md`. The alternative is for the director to move each placement so the cut edge sits at or past
   the frame edge, but extending the asset fixes every future reuse, so do it in the asset.
**B. `bathtub_croc`:** replace the vertical back-of-head edge with a sloping neck that runs down from behind the eye into the water
   line, so the head grows out of a submerged body instead of sitting on the rim as a box. Keep the rim at (-180,-80) clear for
   `doug_cap`, and keep the head top at y ≥ -210.
**C. `croc_holding_shape`:** clamp the grey oblong **across the closed jaw line**. Show part of it above the upper jaw and part below it,
   poking out on both sides of the snout, with the upper jaw's outline and teeth drawn over the shape. Then it reads as gripped, not
   balanced on top. Use the same sloped neck as fix B instead of the boxy vertical back edge, and drop the hard-edged dark rectangle
   under the head (blend it into the submerged body shape). Keep the plain `#8a8f96` shape: no limbs, no features.

Minor, optional: the `mangrove_clump` canopy has no black outline along its underside. That is fine at horizon scale, so add one only if
the illustrator is already in the file.

After the fixes, re-render `python -m studio asset-preview <names>` and the keyframes s037, s040, s045, s071, s114, s115, s181, s213 and
s229 for round 2.
