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

---

# Keyframe review: 011 Every Animal Doug Could Beat in a Fight, Until He Dies

Reviewer: art director · 2026-10-09
Scope: all 285 keyframes (`build/contact/sheet_01..24.png`), full-res crops of s072, s123, s146, s189, s208, s209, s218, s264, s267, and a
check of the flagged shots against `shotlist.json`. s001 is "(thumbnail pending)", which is expected and not reviewed here.

## Verdict: FAIL (7 composition fixes plus 3 label-count trims, all small). Re-render only the listed shots. I will re-check those shots only.

### What already works (keep it)
- **Style:** one look across 285 shots. Crude Doug sits against the detailed-tier animals throughout. Each item has its own environment and they
  read as a set: goose pond (sky/grass), house-cat brick wall, kangaroo dune orange, wolf night navy, cassowary rainforest, chimp blue-grey
  forest, gorilla misty grey-green, croc river (mud band + sand), polar ice, and the elephant red-dusk savanna for the boss item. Cream diagram
  shots break up every item, so the layouts keep changing (insets, bar charts, maps, timelines, silhouettes, crowd rows, close-ups).
- **Doug:** on-model in every shot. The red cap stays visible on every death and on the ghost (s072, s099, s125, s153, s213, s243, s279). The
  capless s021-s024 exception is as approved, with the goose wearing the cap. Boxing gloves (s069-s073, s187-s188, s205) read as gloves, with the
  white cuff, and not as blood next to the body (s072 crop).
- **Counter:** it ticks only on the death shot: 94 at s072, 95 at s099, 96 at s125, 97 at s153, 98 at s213, 99 at s243, 100 at s279. It holds on the
  goose, cat and gorilla survivals. The counter zone is clear on every item title card and sun/moon placement.
- **Field guide:** WIN ticks for goose and cat, MAYBE for the gorilla, and NO stamps on the deaths. The s280-s283 hero and the s281 grid are consistent.
- **Reveals:** the cassowary (s103) and polar bear (s217) use silhouette plus red glow, with the colour reveal in the next shot.
- **Gore:** none. Every death is a dust cloud, a splash or X-eyes.
- **Earlier advisory notes:** D1 (s161), D3 (s201, now a dashed circle) and D4 (s267, "NOT FOOLED" now clears the crown by about 25 px) are fixed.
  D2 (s218) now has about 45 px between the "E" and the claw tips. That is acceptable. Shortening to "BIGGEST CARNIVORE" is optional.
- **Verdict cards** s004/s049/s155 ("DOUG WINS / DOUG LOSES / NO CONTEST") have no caption bar, on purpose (pre-item teaser on the next item's
  background). They are consistent with each other, so keep them.

## Required fixes: shotlist (director)
1. **s189 (car on the croc):** the `small_car` wheels sit on the croc's back, so it reads as a car parked on the crocodile, not as a length
   comparison. The car must not touch the croc. Option A (preferred): put both on the ground at true scale side by side. Keep the croc in the
   river, move the car to the near sand at its own baseline (for example x 1350, y about 1040, scale about 1.5, wheels on the sand) and move the
   6 M dashed line above the croc (y about 620). Option B: switch s189 to a cream diagram (croc on one baseline, car on a second baseline under
   it, both left-aligned, one dashed length line each). Either way, keep at least 60 px of clear space between the car and the croc.
2. **s123 (birdseed bag):** `rotate: 180` flips the bag body, but its printed label stays upright (engine text cannot rotate). It reads as an upright
   bag with a broken base, floating at head height beside Doug's hand. Drop the rotate. Either put the bag on the ground at Doug's feet, tipped
   over (rotate up to about 20 degrees) with 3-4 seed dots spilling from the mouth, or hold it upright at hand height (about x 700, y 760)
   with a few seeds falling out of the bottom. The "?" stays. (This limitation is now in the art bible, Text section.)
3. **s264 (BOYS on the sun):** the "BOYS" label at (400, 640) sits right on the sun disc, which covers x 280-520. Move it to about (640, 780), to the right of
   the loudspeaker and below the horizon, clear of the sun.
4. **s208 (label on Doug):** the "27 FATAL" box at (1550, 660) overlaps Doug's cap. Raise both labels by 50 px (87 ATTACKS at 470, 27 FATAL at 610)
   or move Doug to x 1780. Doug's cap must be fully clear of the box.
5. **s209 (Doug in the jaws):** Doug (x 300) stands on the croc's snout tip, so it reads as Doug in the jaws on a non-death beat. Move the croc to
   x 1080 and Doug to x 220, which leaves about 100 px of clear sand between the snout and Doug. The tail stays inside x 1856.
6. **s154 (lime on green):** the "EVERYTHING ELSE" wordart at y 600 sits on the dark-green rainforest hills. The art bible forbids lime wordart on green.
   Lift it to y about 470 (blue sky band) and move the ghost Doug to x about 1500 so the two don't touch.
7. **s146 (red dots):** the red `#e0201b` dots over the black chimp silhouettes, on the "killings" beat, can read as blood drops at phone size.
   Recolour them blue `#3a8fd6` (the poll/USA blue already in this episode) and keep the 10th chimp unmarked.

Label count (style bible 7.4: at most 2 labels or wordart at once):
8. **s025:** there are 3 stacked labels. Keep "POND" (move it onto the pond next to the goose) and merge the other two into one label, "DIGNITY + LAST WORD".
9. **s055:** "2x" wordart plus FEMALE and MALE makes 3. Delete the "2x" wordart and change the MALE label to "MALE 2x".
10. **s083:** ELK, BISON and MOOSE are 3 labels. Use one label, "ELK, MOOSE, BISON", centred above the moose (about 1100, 320).

## Required fixes: assets (illustrator)
None. All the library drawings render on-model at every scale used.

## Routing
- Director: fixes 1-10, then re-render with `python -m studio keyframes 011-every-animal-fight --shots s025,s055,s083,s123,s146,s154,s189,s208,s209,s264`.
- Illustrator: nothing.
- Art bible: I added the text-in-rotated-assets rule (Text section) from s123.
