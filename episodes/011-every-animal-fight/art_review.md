# Art review: 011 Every Animal Doug Could Beat in a Fight, Until He Dies

**Scope:** the 41 new assets in `asset_requests.md` (previews `assets/previews/011-every-animal-fight-assets-A.png`,
`-assets-BC.png`, `-props.png`, `-props-backdrops.png`). I re-rendered each one at scale 1 on a large canvas so the grid
cells could not crop it (the moose antlers, the standing polar bear, the front elephant and the pine tree are clipped in
the grid sheets, but not in the actual drawings). I measured every bounding box against its requested box, checked the
four SIL assets as black silhouettes with a red glow on navy, and rendered 70 context keyframes across all ten items.

**Verdict: PASS.** All 41 are approved. I fixed two small things myself (below), so nothing goes back to the illustrator.

## Fixes made by the art director (already in the library)
1. `african_bush_elephant_front`: the brows were two black width-5 lines slanting down toward the trunk, which made an
   angry V-frown. The brief asks for "still and attentive (it's listening)". I replaced them with flat, slightly arched
   dark-grey (`#3a3a3a`) width-4 brow ridges. It still looks heavy-browed and not cute, but it no longer looks angry.
2. `african_bush_elephant` (side view): its brow had the same downward slant, so I gave it the matching arched ridge.
   The side and front views now cut together.
3. `croc_eyes_water`: the two under-water `spray` shadows (r 60-70 at y +14) spread speckle haloes above the waterline
   around the brow bumps, and they read as dirt on the sky or bank. I moved them to y +44 with r 40, so they now sit fully
   under the water strip.
4. `croc_log` and `croc_log_eye`: one body spray (r 70 at y -40) leaked a speckle smear below the belly line. I changed it
   to r 52 at y -56 and made the **identical** edit in both files, so the overlay in s211 still matches pixel for pixel
   (wobble 0 and boil 0 are kept).

## Flagged items
- **Front elephant frowning brows:** fixed (fix 1).
- **`red_kangaroo_kick` size:** measured at 548x590 against the requested 560x520. The extra 70 px of height is just the
  ears on the leaned-back head. The keypoints are where they should be: the tail tip is at about (-205, 0) and the hind
  feet at about (+290, -190..-255). In s057, s063-s066 and s071 it sits clear of the counter, the caption bar and the
  wordart. **APPROVE as drawn.**
- **`silverback_gorilla` / `silverback_chest_beat` size:** measured at 495x652 and 489x650 against 440x640. The arms and
  hands make it about 12% wider. The two still share a footprint, so they swap cleanly, and the eye sits at (+60, -560) as
  requested (the s179 gaze line lands on it). This is fine in every gorilla keyframe. The only contact is in s161, where
  the "UP TO 227 KG" label touches the flank (director note D1). **APPROVE as drawn.**

## Per-asset verdicts
| # | Asset | Verdict | Notes |
|---|---|---|---|
| 1 | `cassowary` | APPROVE | It has the casque, blue neck, red wattles and shaggy near-black plumage. It reads on the rainforest, and it reads at 0.3 in s114. The silhouette is clean (casque, beak, wattles). |
| 2 | `red_kangaroo` | APPROVE | The tail is planted at (-267, 0). It looks muscular and hard-eyed, not cuddly. |
| 3 | `red_kangaroo_kick` | APPROVE | See the flagged items. It is the same head and colours as #2, so the two cut together. |
| 4 | `silverback_gorilla` | APPROVE | The stare is steady. The saddle reads. See the flagged items. |
| 5 | `silverback_chest_beat` | APPROVE | The cupped hands are on the chest. The open mouth is dark red with fangs, and there is no blood. |
| 6 | `silverback_walking` | APPROVE | The saddle sits right under the s164 arrow target. It knuckle-walks. |
| 7 | `african_bush_elephant` | APPROVE (AD fix 2) | It has Africa-shaped ears, a hollow back and tusks. |
| 8 | `african_bush_elephant_front` | APPROVE (AD fix 1) | Its 909x765 silhouette is huge. It clears the "AFRICAN BUSH ELEPHANT" label in s249. |
| 9 | `chimpanzee` | APPROVE | The face is flat and alert. The silhouette is clean for the "8 vs 1" and "9 in 10" diagrams. |
| 10 | `chimpanzee_sitting` | APPROVE | It sits correctly on the `fallen_log` top (s126, s151). |
| 11 | `canada_goose` | APPROVE | The chinstrap and scalloped feathers read. |
| 12 | `canada_goose_hiss` | APPROVE | The neck is low and the beak open. It is threatening, not cute. |
| 13 | `canada_goose_attack` | APPROVE | The wrist knob is obvious, and the s014 arrow lands on it. |
| 14 | `canada_goose_cap` | APPROVE | The cap is the exact `#e0201b` dome and brim, sitting crooked. It reads as Doug's cap even at small scale (s021-s024). |
| 15 | `cat_angry` | APPROVE | The ears are flat, the tail is an S-curve and the colours match `cat`. |
| 16 | `cat_yawn` | APPROVE | The footprint is identical to `cat`, and the squeezed eyes make it a yawn rather than a snarl. |
| 17 | `grey_wolf_sitting` | APPROVE | The coat and amber eyes match `grey_wolf`. It reads when mirrored (s097). |
| 18 | `moose` | APPROVE | It has palmate antlers, a dewlap and a hump. The antlers sit inside the 568 height. |
| 19 | `croc_eyes_water` | APPROVE (AD fix 3) | The yellow slit eyes read on the `#7a5a3a` river. |
| 20 | `croc_jaws_open` | APPROVE | The inner mouth is pale with no blood, and the teeth interlock. |
| 21 | `croc_log` | APPROVE (AD fix 4) | It reads as a log first, which is the gag. |
| 22 | `croc_log_eye` | APPROVE (AD fix 4) | The geometry still matches `croc_log`. The s211 to s212 reveal works. |
| 23 | `polar_bear_standing` | APPROVE | The outline is thick on white ice. It is a predator, not cuddly. The silhouette is strong in s217. |
| 24 | `grizzly_bear` | APPROVE | It has the hump and pale claws. |
| 25 | `dust_cloud` | APPROVE | There are no body parts and no blood. Doug's cap stays visible at the edge, as the death-beat rule requires. |
| 26 | `snow_dust_cloud` | APPROVE | It reads on both white ice and pale sky. |
| 27 | `pine_tree` | APPROVE | Its edge highlight reads on the `#2c3e66` dusk. |
| 28 | `fallen_log` | APPROVE | The top is at about y -130 as requested. |
| 29 | `birdseed_bag` | APPROVE | The label is legible at 0.55. |
| 30 | `sandwich` | APPROVE | |
| 31 | `cassowary_foot` | APPROVE | The claw tip is at (+238, -130), where the s107 arrow lands. |
| 32 | `ballpoint_pen` | APPROVE | |
| 33 | `bowling_ball` | APPROVE | |
| 34 | `house_brick` | APPROVE | |
| 35 | `cement_bag` | APPROVE | |
| 36 | `walnut` | APPROVE | |
| 37 | `silver_fish` | APPROVE | It reads in Doug's hand (s239). |
| 38 | `loudspeaker` | APPROVE | |
| 39 | `savanna_bush` | APPROVE | It is olive-brown, not green, and sits well on the red dust. |
| 40 | `acacia_tree` | APPROVE | It is a near-silhouette on the sunset, as requested. |
| 41 | `crumpled_paper` | APPROVE | The pencil and red-cap hint reads as "the death drawn already". |

## Capless Doug, s021-s024 (director note 1)
**APPROVED as a one-off** and logged in `decisions.md`. Doug sits dazed with `gear: ["cap_off"]`, and the goose clearly
wears the cap in every one of those shots, so the signature red stays on screen and the joke depends on it. The cap is
back on at s025. This is a survival, not a death beat. s072/s073/s243/s244 use `cap_off` on `on_back`, which is the
standard knocked-off-cap death pose and needs no exception.

## Chest-beat pose (director note 2)
**Not added.** `["hands_hips", "think"]` reads fine in s177-s178 with the "me too" bubble and the "tap tap" box. A
dedicated pose would only appear twice in this episode. I may revisit it if a later episode needs one.

## Advisory composition notes for the director (from the context keyframes, not part of this asset gate)
D1. s161: the "UP TO 227 KG" label touches the gorilla's flank. Move it about 30 px right or up.
D2. s218: the "LARGEST LAND CARNIVORE" wordart runs into the polar bear's raised forearm. Shorten it ("BIGGEST CARNIVORE")
    or move the bear right or the text left.
D3. s201: the brain spot is a filled pink disc on top of the croc's skull, and it can read as a wound or bump. Make it a
    dashed outline circle (or a pale fill under 50% with a black outline), linked to the walnut.
D4. s267: the "NOT FOOLED" wordart nearly touches the front elephant's crown. Lift it about 20 px.
