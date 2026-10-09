# Art review: 013 closer-to-a-hippo, library assets (18)

Reviewer: art director. Previews: `assets/previews/013-closer-to-a-hippo-assets-a*.png`, `-b*.png`
(`-b-context.png` re-rendered after the fixes below).

**Verdict: PASS** (3 small REVISE items fixed by the art director in `/tmp/hipgen/gen.py`, re-generated and re-previewed).

## Hippo set (illustrator A, `/tmp/hippo_gen/gen.py`)
One animal across all poses: same palette, head, eye/ear/nostril layout. Detailed tier (outline, flat fills, darker
back, paler belly, spray) against crude Doug. Small eyes with heavy brows, no smile, no blush, short thick legs: reads
dangerous, not cuddly. Bold silhouettes hold at the 0.33 scale.

| # | Asset | Verdict | Notes |
|---|---|---|---|
| 1 | `hippo` | APPROVED | Barrel body, level back, lower canine at the lip corner. Points match the request. |
| 2 | `hippo_yawn` | APPROVED | Clear 150-degree gape, flat pink interior, no tongue/saliva/gums, tusks read. Canine tip 17 units off the request (noted by illustrator) is fine. |
| 3 | `hippo_waterline` | APPROVED | Ears/eye/nostrils read at 2.4x and at map scale; covers `hippo_rock`. |
| 4 | `hippo_rock` | APPROVED | Reads as a plain river rock; 300x64 accepted (fits inside waterline). |
| 5 | `hippo_grazing` | APPROVED | Mouth on the grass tuft at the requested point. |
| 6 | `hippo_red_sweat` | APPROVED | Orange `#e8662a`/`#f0902a` with white gloss reads as wet coating, not blood. Director: keep the "NOT BLOOD" label on screen in s094-s097 as planned. |
| 7 | `hippo_trot` | APPROVED | All four feet off the ground, clear gap for the s087 arrow, shadow on y=0. |
| 8 | `hippo_underwater` | APPROVED | Mid-tone body reads on murky `#5d6b45` and on black. |
| 9 | `hippo_sleeping` | APPROVED | Eyes shut, calm pose; works for the three-up diagram. |

## Batch B (`/tmp/hipgen/gen.py`)
| # | Asset | Verdict | Notes / fixes |
|---|---|---|---|
| 10 | `hippo_submerged` | REVISE -> FIXED | (a) The mouth line curved up into a corner with a pink dot, which read as a **smile** (kid-appeal rule). Fixed: the mouth line now runs flat and turns down (`(372,70)->(330,78)->(290,92)`), and the pink corner is a small 5x4 flesh spot with no outline. (b) The belly spray under the jaw spilled outside the outline as grey fuzz. Fixed: moved to (310,96), r 22. |
| 11 | `hippo_mouth_front` | REVISE -> FIXED | Spray spilled outside the outline (grey fuzz above the head and beside the cheeks on the orange background). Fixed: back spray now (0,-880) r 80, cheek sprays (+-425,-500) r 30. The silhouette reads as a gaping mouth. The red speckle in the silhouette tile is the engine's intended glow, not the asset. The chin centre stays light, so Doug's black ink reads. |
| 12 | `hippo_canine` | APPROVED | Wear facet at the tip, yellow root, at ruler scale. |
| 13 | `lettuce` | APPROVED | Reads at 0.32 on dark pink-red. |
| 14 | `tent` | REVISE -> FIXED | The light-green spray at the top right bled past the dome outline. Fixed: (80,-160) r 35. Mid-tone fills read on the night ground. |
| 15 | `sticking_plaster` | APPROVED | |
| 16 | `dung_cloud` | APPROVED | Flat, abstract scribble with no lumps. Gross but not gross-out. Use in one shot only. |
| 17 | `africa_map` | APPROVED | Matches the `world_map` style, with rivers, lakes, Madagascar and the Arabian edge. Director: check the icon positions on the s232 keyframe. |
| 18 | `astronaut` | APPROVED | Crude tier, no cap, auto_ink works on black and on white. |

## Routing
- No outstanding asset fixes for the illustrator.
- Director: follow the notes on #6 and #17 when you check the keyframes.
