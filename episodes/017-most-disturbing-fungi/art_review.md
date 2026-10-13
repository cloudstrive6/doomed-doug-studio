# 017 art review: new library assets (55)

Reviewer: art director · 2026-10-13
Inputs: `asset_requests.md`, `assets/previews/017-*.png`, re-renders with `asset-preview` (tree_branch, gunpowder_store,
spider_costume_fuzz, cicada_nymph, frog, frog_costume_flat), a fit test of `doug_fuzz_silhouette` against the rig
(`studio art`), and 22 test keyframes (s016-s261) to check the costumes, hats and rotate-180 groups in real shots.

## Verdict per asset

### Insects
| # | Asset | Verdict | Notes |
|---|---|---|---|
| 1 | `cicada` | APPROVE | Black body, red eye, orange-veined tent wings. Detailed tier. |
| 2 | `cicada_infected` | APPROVE | Chalky plug at the rear, wings intact. Reads as fungus, not as a wound. |
| 3 | `cicada_nymph` | APPROVE | Hunched digger angled up-right. Dirt speckle at the claws is fine. |
| 4 | `tree_branch` | APPROVE | Leaf clusters at both ends, twig stubs, within ±100 of the line. The sheet crop only hid the leaves. |
| 5 | `cicada_costume` | APPROVE | Pom-pom eyes sit beside the cap. The abdomen sticks out behind and the wing cape works. |
| 6 | `cicada_costume_half` | APPROVE | |
| 7 | `cicada_costume_rear` | APPROVE | The cork read lands in s026. |
| 8 | `cicada_costume_flat` | APPROVE | |
| 9 | `house_fly` | APPROVE | |
| 10 | `fly_death_pose` | APPROVE | Head-down, wings in a high V, stiff legs. |
| 11 | `fly_death_pose_banded` | APPROVE | Cream bands with soft puffs. Not a wound. Drawn alone. |
| 12 | `fly_costume` | APPROVE | |
| 13 | `fly_costume_wings_up` | APPROVE | The wings sit behind the arms with `arms_up`. |
| 14 | `fly_costume_banded` | APPROVE | |
| 15 | `fly_costume_flat` | APPROVE | |
| 16 | `alarm_clock` | APPROVE | 6:00, twin bells. |
| 17 | `ireland_map` | APPROVE | world_map style, faint NI border, no labels. |
| 18 | `gunpowder_store` | APPROVE | Slate roof, arched door, barred vent, ivy, and the GUNPOWDER STORE sign (the only text). Keep it upright (sign text). |
| 19 | `cave_spider` | APPROVE | Creepy, not cute. Banded legs, front pair longest. |
| 20 | `cave_spider_fuzz` | APPROVE | Stiff white fuzz sticks with a pale halo. No gore. |
| 21 | `spider_costume` | APPROVE | Bead eyes beside the cap. It works upright, flipped and at rotate 180 (s076). |
| 22 | `spider_costume_fuzz` | FIX (done by AD) | Five dark-brown `#5a3420` "felt" specks on the white fuzz read as dried blood or rot at small size. I recoloured them to grey `#a8a8a0`. |

### Whole species
| # | Asset | Verdict | Notes |
|---|---|---|---|
| 23 | `frog_costume` | APPROVE | It also works waist-deep (fit sheet). Frog eyes: see decision 5. |
| 24 | `frog_costume_flat` | APPROVE | |
| 25 | `lily_pad` | APPROVE | |
| 26 | `bat_hanging` | APPROVE | |
| 27 | `bat_white_nose` | APPROVE | Advisory, not blocking: the wing-edge puffs are evenly spaced and at 0.5 scale they read slightly like fairy lights. If the illustrator touches it again, vary the size and spacing and merge a few puffs into a fuzzy edge. |
| 28 | `bat_costume` | APPROVE | Ears beside the cap. It works at rotate 180 (s127). |
| 29 | `bat_costume_flat` | APPROVE | |
| 30 | `thermostat_dial` | APPROVE | No numbers, pointer at max. |
| 31 | `fuel_gauge` | APPROVE | |

### People
| # | Asset | Verdict | Notes |
|---|---|---|---|
| 32 | `dust_plume` | APPROVE | No stars, limbs or faces. |
| 33 | `hard_hat` | APPROVE | Perched on the cap with the dome and brim visible (s153, s156). |
| 34 | `rye_stalk` | APPROVE | |
| 35 | `rye_ergot` | APPROVE | Purple-black spur, clearly visible. |
| 36 | `grain_sack` | APPROVE | |
| 37 | `medieval_cottage` | APPROVE | |
| 38 | `stone_hospital_medieval` | APPROVE | Blue tau cross, bell gable. |
| 39 | `medicine_bottle_plain` | APPROVE | Blank label. |
| 40 | `wawel_cathedral` | APPROVE | Tallest tower on the left and the right third kept low. Gold dome, warm windows. |
| 41 | `stone_tomb` | APPROVE | |
| 42 | `stone_tomb_open` | APPROVE | Dark gap and soft haze. Nothing inside. |
| 43 | `newspaper_curse` | APPROVE | Generic masthead. |
| 44 | `peanuts_and_corn` | APPROVE | |
| 45 | `petri_dish_mould` | APPROVE | |
| 46 | `vial` | APPROVE | |
| 47 | `paper_crown` | APPROVE | Perched on the cap (s201, s205). |
| 48 | `bc_map` | APPROVE | |
| 49 | `porpoise` | APPROVE | Blunt, no beak. |
| 50 | `llama` | APPROVE | Calm half-lidded eye, not cute. |
| 51 | `hospital_building` | APPROVE | Exterior only, nothing visible through the windows. |
| 52 | `petri_dish_auris` | APPROVE | Creamy colonies on pink chromogenic agar read well. |
| 53 | `spore_puff_walk` | APPROVE | No face, dry. |
| 54 | `spore_puff_sit` | APPROVE | |
| 55 | `doug_fuzz_silhouette` | APPROVE (one-time variant approval) | Overlaid on the rig, it matches Doug's stand silhouette, hip anchor, feet and exact cap. It has a black outline, so it reads on cream and dark grounds. See decision 3. |

## Decisions on the notes in asset_requests.md

1. **Background colours: approved with one change.**
   - Every proposed colour stands except the boss.
   - C. auris "sterile" `#f3f1d6` is almost identical to the opener cream `#f4f1dc`, and close to the ergot parchment and the Valley Fever hills. The final item would look like the first.
   - Use cold clinical mint `#e4eeec` with floor `#b9c7c4` for every C. auris scene shot (s231-s263). That includes the s258-s263 thermostat room, which currently uses `#f3e8c0` / `#c9a87a`.
   - The s243 sober card keeps dark text on a pale card. Use `#e4eeec` or white.
   - The whole set is now in the art bible as the "Fungus / mould environments" table.
   - Chytrid must stay on its swamp palette in every shot. s106 (the death, test render) switched to a blue sky and turquoise water `#9fdcd6`. Put it back on overcast `#b9c4a8` over olive water `#5d6b45`.
2. **Upside-down Doug via `group` + `rotate: 180`: confirmed.**
   - s076 and s127 test renders read as "hanging from the ceiling". The cap hanging below the head is funny, not broken.
   - Rules (now in the bible): only with `spider_costume` / `bat_costume`, Doug and the costume at local (0,0) with the same scale, never for a death beat.
   - Keep the group's hip y so that the costume legs and feet touch the ceiling line. s127 is right. In s076, check that the legs end on the ceiling and not in mid-air.
3. **`doug_fuzz_silhouette`: approved once as a reusable `parasites` death ("fuzz-over").**
   - Like the 012 amber variant, the overgrown body is the death image. So it has no X eyes and no ghost, the counter ticks to 147 and the cap is in frame.
   - Only for overgrowth deaths, logged in `decisions.md`, at most once per episode. Added to the bible.
4. **`hard_hat` / `paper_crown` placement: approved.**
   - List each after Doug at the same x/y/scale/flip. The rim sits at y -294 and the cap shows below.
   - Upright poses only. That covers every planned use: stand, thumbs_up, hands_hips, point, shrug.
5. **Frog eye: approved as drawn.**
   - The costume's hood eyes match the library `frog` exactly: gold iris, horizontal black pupil, green lid.
   - The front eye sits above the brim, with a clear gap, never on it (checked at 0.75 in s103).
   - The flat suit's half-lidded drooping eyes are the right "empty" read. No big shiny eyes anywhere.
6. **WordArt on green/olive: approved.** Use `top #ffffff`, `bottom #ffe24a`, `outline #1a1a1a` on every green or olive ground, light or dark. Added to the bible.
7. **No `cap_off`; deaths 140-147 as listed:** approved. The flat costume plus `doug_cap` plus ghost with X eyes matches the 008 eaten-whole rule.

## Notes for the director (seen in test keyframes; these will be failed at the keyframe gate if unchanged)
1. s044, s055: the wordart ("PALE BANDS", "PERMANENTLY") uses the default lime on the `#2f5a3a` green wall. Add the white/yellow override.
2. s103: the "DOUG IS A FROG" wordart at y 200 runs into the DOUG DEATHS counter box. Move it to y ≥ 290 or shorten/shift it left of x 1280.
3. s058: the title "THE CAVE SPIDER FUNGUS" crosses the fuzzy spider. Move the spider off the title line, or the title down.
4. s106: chytrid palette (decision 1).
5. s231-s263: C. auris backdrop to `#e4eeec` / `#b9c7c4` (decision 1).

## Fixes for the illustrator
None blocking. Optional: `bat_white_nose` puff spacing (asset 27).

**PASS.** 54 assets approved as drawn. `spider_costume_fuzz` was fixed by the art director and re-previewed. Director notes 1-5 apply at the keyframe gate.

## Keyframes

Reviewer: art director · 2026-10-13
Inputs: all 266 keyframes (`build/keyframes/s001-s266.png`), re-rendered from the committed shotlist because `build/contact/` only held a
one-shot sheet (s001) from a partial `--shots` run. 23 contact sheets (`build/contact/sheet_01-23.png`), full-res checks of every text/counter
near miss, and an estimate of each label/wordart box against the counter zone (x 1300-1860, y 110-230) and the safe area (x 64-1856).

### What holds
- **Doug is on-model in all 266 shots.** He has the cap in every frame, including all ghosts, and expressions come only from the fixed set.
  - The costumes (cicada, fly, spider, bat, frog) sit correctly, with pom-pom/bead eyes and ears beside the cap.
  - Upside-down Doug works in s076-s078 and s127-s130. The legs end on the ceiling line.
  - The hard hat (s153-s157) and paper crown (s201-s205) are perched on the cap.
- **Deaths 140-147 tick on the right beats:**
  - 140 at s029.
  - 141 at s056.
  - 142 at s079.
  - 143 at s106.
  - 144 at s131.
  - 145 at s178.
  - 146 at s229.
  - 147 at s261.
  - Flat costume + cap + ghost with X eyes for the costume deaths. Body + ghost for s178/s229. `doug_fuzz_silhouette` once at s261, with no ghost, as approved in decision 3.
  - Nothing is gory. The spore plug, banded fly, fuzzed spider and white-nose bat all read as fungus, not wounds.
- **Zone colours are consistent per item and match the art bible's fungus/mould table:**
  - Massospora: cream / sage grass.
  - Fly fungus: green wall + window.
  - Cave spider: cave greens.
  - Chytrid: overcast swamp (s106 fixed).
  - White-nose: slate cave.
  - Valley Fever: sand.
  - Ergot: parchment.
  - Tomb: charcoal.
  - Cryptococcus: forest.
  - C. auris: clinical mint `#e4eeec`/`#b9c7c4` throughout s231-s263, including the thermostat room.
  - Maps and sober cards (s099, s152, s168, s223, s243) are an intentional break.
- **Earlier director notes 1-5 are all resolved:**
  - s044/s055 use the white/yellow override.
  - s103 clears the counter.
  - s058 has the spider off the title line.
  - s106 is on the swamp palette.
  - C. auris is on mint.
- **Layout variety is good.** The episode cycles through scenes, maps, bar/line charts, counting grids, sober cards, lab benches and title
  cards. No run of 5 near-identical compositions.
  - s127-s130 ("Then again. Then again.") is a deliberate build-up beat: each shot adds an element (alarm wiggle, then "!", then "!!"). Allowed.

### Fixed by the art director in `shotlist.json` (position/scale only, plus one wordart shortened; validated and re-rendered)
1. Wordart that crossed into the DOUG DEATHS box:
   - s015 "DOESN'T STOP": x 1100 to 960.
   - s023 "CAN'T INFECT PEOPLE": x 960 to 800.
   - s024 "DRESSED AS A CICADA": x 960 to 780.
   - s141 "MORE THAN A DOZEN": x 960 to 820.
   - s157 "INTO A COUNTY": x 1000 to 900.
   - s198 "ABOUT AS WELL": x 1340 to 960.
2. s019: the lime "WING FLICK" sat on the green hill line (lime on green). Moved y 640 to 595, onto cream.
3. s030: "GETS THE REST" ran through the yellow sun. Moved x 760 to 640.
4. s036: "BEFORE SUNSET" ran into Doug's head. Moved x 1300 to 1180.
5. s061, s062: the spider silhouette/fuzz covered the "GUNPOWDER STORE" label ("GUNPOWD..."). Moved the label x 960 to 520.
6. s088: "MORE THAN HALF" ran to the frame edge (outside the safe area). Moved x 1540 to 1420.
7. s108: the item title crossed the hanging white-nose bat. Title y 440 to 500, and the bat moved to (1200, 170), clear of the counter zone.
8. s147: "TEN TIMES" butted against the 1994 bar. Moved to (1520, 560), beside the bar under the counter.
9. s169: "THE POISON WAS THE BREAD" was 5 words (rule 7.4 allows 1-4). Changed to "POISON WAS THE BREAD" (still echoes the line) and moved x to 860.
10. s167: twelve hospitals were stamped over the two background cottages, and Doug overlapped the last hospital. Removed the cottages, shifted the hospitals 60 px left and moved Doug to x 1810.
11. s246: Doug (scale 0.5) stood on the face of the brick wall and read as painted on it. Moved him to the wall's left end at the s256/s257 wall-scene placement (120, 899.2, 0.4).
12. s249: the cat and horse were stacked on top of each other, and the horse was smaller than the cat. Cat is now (1440, 0.4) and horse (1660, 0.42).
13. s263: "it is also food" was identical to s262 apart from a 9 px dot. Added an approved `spore_puff_sit` (1380, 620, 0.4) beside the cap on the sill.

### For the director (advisory, not blocking)
1. s206: the title "CRYPTOCOCCUS GATTII" crosses the left and right tree crowns. Readable thanks to the outline, but cleaner if the outer trees move to x ≤ 120 / ≥ 1800 or the title moves to y 360 (on dark green, below the crowns' widest point).
2. s242: the "WHO, 2022: CRITICAL PRIORITY" label sits on the hospital's roof sign. Drop the hospital 40 px or move the label to y 300.
3. s049, s050: Doug's fly wing touches the left frame edge (x ≈ 30). Move Doug to x ≥ 180.
4. These shots end 0-60 px inside the reserved counter zone (x ≥ 1300) but visibly clear of the box. Nudge left 60 px on the next pass if convenient:
   - Wordart: s018, s043, s051, s154, s156, s179, s194, s204.
   - Labels: s032, s063, s166, s195, s241, s242.
5. s127-s130: optional slow 5% push-in on s130 to sell the third repeat.

### Fixes for the illustrator
None.

**PASS.** 266 keyframes are on-model, on-palette and legible, with no gore. The 13 shot fixes above were applied by the art director and re-rendered.
Director advisories 1-5 are polish only.

### Round 2 (after visual_review round 1 fixes)

Reviewer: art director · 2026-10-13
Inputs: the fresh 17:27-17:28 UTC render (`build/keyframes/`, `build/contact/sheet_01-23.png`), the diff of commit 5b7ca42 (28 shots
changed), side-by-side checks of each changed shot against its neighbours, and full-res crops of s210 (new `ferret`, redrawn `porpoise`) and s257.

**Visual review items, all resolved:**
- **s047, s061, s257 (gore read, item 19).** The red stipple is gone.
  - s047: the banded fly silhouette now has a dull purple `#5e4670` glow.
  - s257: the blob on the brick wall has the same purple glow and no longer reads as spatter.
  - s061: now shows the white `cave_spider_fuzz` lit by the head-torch beam. This also fixes item 15.
  - The rule is now in the art bible (silhouette glow: purple on brick, red/brown or near-body grounds).
- **s097:** 4 of 20 frogs are crossed out (about 18%), which matches 90/501.
- **s099:** the sober card reads "GREATEST RECORDED LOSS / OF BIODIVERSITY / TO A DISEASE" with a lone frog silhouette. It is no longer a repeat of s097.
- **s125:** "ENDANGERED" sits clear below the hanging bat.
- **s186 / s192:**
  - s186 is the hedged sober card: "ACCORDING TO LATER ACCOUNTS: / 10 OF ~12 / DIED". No Doug, no counter, no joke.
  - s192 is now a lungs-and-spores body diagram with "LUNG INFECTIONS" and a "WEAK IMMUNE SYSTEMS" label. Doug looks gritted, not joking. The tone is right for the beat after the tomb deaths.
- **s206:** the outer firs moved to the frame edges and the title band is clean.
- **s210 / s211:** the redrawn `porpoise` (melon head, no beak, dorsal fin, flukes) reads as a porpoise, and the new `ferret` (bandit mask, cream body, dark legs) reads at 0.4. Both are detailed tier, on-palette, not cute and not gory, and both are **approved** as library assets. The lineup now matches the narration order: dog, cat, ferret, porpoise, llama, horse.
- **s234:** "FOOTNOTE: / NEW YEAST" is 40 px bold, readable at feed size, with the red arrow on it.
- **s242:** the labels sit above the roof and the red-cross sign is visible.
- **Counter clearance:**
  - My round-1 advisory list is done. s018, s032, s043, s051, s063, s154, s156, s166, s179, s194, s195, s204 and s241 all end at x ≤ 1290.
  - s242's WHO label ends at about 1288.
  - s049/s050: Doug's fly wing is now about 100 px from the frame edge (inside safe).

**Consistency check:**
- No other shots changed.
- The counter sequence (139→147 on s029/s056/s079/s106/s131/s178/s229/s261) and the zone colours are unchanged from round 1.
- The new s186 card follows the established sober-card style (s099/s152/s168/s223).
- s185→s186→s187 and s191→s192→s193 each change layout. There are no new runs of similar compositions.

**Advisory (polish, not blocking; director):**
1. s210/s211: the ferret's nose is about 20 px from the porpoise's flukes. Nudge the porpoise x +30 (or the ferret -20) for a cleaner gap.
2. s241→s242: the hospital shrinks from scale 1.0 to 0.85 at the same x between consecutive shots, which pops slightly on the cut. Either set s242's camera to a gentle `zoom_out` so the change reads as intended, or accept it.

**Fixes for the illustrator:** none.

**PASS.** All 13 targeted shots and the counter-clearance moves are on-model, on-palette and legible, with no gore read. `ferret` and the redrawn `porpoise` are approved.
