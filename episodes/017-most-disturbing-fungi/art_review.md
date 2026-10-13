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
