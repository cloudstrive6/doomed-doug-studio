# Art review: 006 Disturbing Deep Sea Discoveries

Reviewer: art-director · Date: 2026-10-04

**Assets verdict: PASS** (31/31 APPROVE, one small fix made by me)
**Keyframes verdict: PASS with notes** (3 fixes made by me; composition notes for the director below are non-blocking)

## How I checked
Each asset was rendered large on cream `#f4ecd8`, on its target zone colour (navy / twilight / abyss / hadal), as a
black silhouette with red glow, and at about 1/6 size for small-size legibility. Then I ran the full `keyframes` render
(278 shots, 24 contact sheets) and checked the problem shots at full resolution.

## Assets (31)

| # | Asset | Verdict | Notes |
|---|---|---|---|
| 1 | pacific_map | APPROVE | Same style as `world_map`, the Pacific is in one piece, Hawaii, Aleutian and Mariana dots read. Pins in s094/s106/s142/s226/s250 land in the right places. |
| 2 | microbe | APPROVE | No face, lime reads on dark rock and on cream. |
| 3 | tubeworm_cluster | APPROVE | Cream tubes and red plumes carry it on hadal black. Clean SIL. |
| 4 | clam | APPROVE | Pale shell, dark gap with a sliver of red flesh. Reads at contact-sheet size. |
| 5 | clam_with_cap | APPROVE | Dome has its 5 px outline. On hadal it reads as a red bulge plus the brim in the seam; with the s274 setup and the s276 arrow and heart it lands. |
| 6 | fingertip | APPROVE | Flat nail platform at y=-560. Figures and the car stand on it correctly (s149, s259). |
| 7 | seabed_mining_vehicle | APPROVE | Industrial yellow, no logos, strong SIL (s174). |
| 8 | kavachi_volcano | APPROVE | Open crater, no lava, lit and shaded flanks. |
| 9 | hammerhead_shark | APPROVE | Cephalofoil reads as a hammerhead even in silhouette (s014). No grin. |
| 10 | sixgill_stingray | APPROVE | Plain disc but correct (translucent snout). Reads small on the crater floor. |
| 11 | puffer_sand_circle | APPROVE | Strongest asset in the batch: a perfect geometric circle at every size. The `ink` grey variant works (s043). |
| 12 | lopsided_sand_circle | APPROVE | The square side is obvious, which is the joke. |
| 13 | pufferfish | APPROVE | Neutral, deadpan, clean SIL (s032). |
| 14 | alien_head | APPROVE | Light-bulb cranium is unmistakable in silhouette. |
| 15 | ctd_instrument | APPROVE | Light metal reads on dark blue. Cable attaches at the lifting eye. |
| 16 | lost_city_chimney | APPROVE | Ghostly pale spire glows on twilight navy and holds up at 0.15-0.8 scale. |
| 17 | apartment_block | APPROVE | 20 rows of windows, 1:1 with the chimney (s080). |
| 18 | blue_whale | APPROVE | Calm, not cute. Mottling and throat grooves read at 1.4. |
| 19 | iceberg | APPROVE | Flat top at -260 and the broken slab work (s105/s115). |
| 20 | brine_pool | APPROVE | Mirror surface plus mussel ring reads on navy. |
| 21 | double_decker_bus | APPROVE | Correct scale gag in s127. |
| 22 | champagne_glass | APPROVE | Reads on navy thanks to the white glints. The dropped glass in s161 works. |
| 23 | scaly_foot_snail | APPROVE | Silver highlights carry the iron shell on navy. Chain-mail scales are the hero detail at 1.5 (s165/s167). |
| 24 | black_smoker | APPROVE | Grey-shaded plume shows on navy. Mineral crust gives the column some value. |
| 25 | saucepan_armor | APPROVE | Checked at full res in s180/s181: the pan, handle and tape X read, and face and cap stay clear. Loose `rotate: 90` copy is small but fine. |
| 26 | asphalt_mound | APPROVE | Glints and ropy flows make the near-black mound read on abyss. It is the lowest-contrast asset here, so do not use it below scale 0.4 without a rim light. |
| 27 | golden_orb | APPROVE | Glossy gold dome, torn hole on the right, reads tiny (s212 monitor). |
| 28 | sea_sponge | APPROVE | Vase silhouette reads (s213). |
| 29 | giant_anemone | APPROVE | Long thin tentacles, pale column, golden basal disc. Good SIL. |
| 30 | manganese_nodule | APPROVE (fixed) | **Fixed by me:** the edge bumps and the belly-shadow polygon spilled past the black outline (sloppy edge at the 2.0 close-up). I pulled the bumps inward (positions x0.85, radii x0.92), and the shadow (x0.86) and rim light (x0.95) with them. The field at 0.55 and the close-up at 2.0 both read cleanly now. |
| 31 | research_ship | APPROVE | Lit yellow windows, red mast light, reads on a night sky (s272). |

Two-tier rule: all 31 are detailed tier (interior shading, layered fills, spray) and contrast correctly with crude Doug. Nothing is gory, and no animal has a cute face or a smile.

## Keyframes

Overall the style is consistent. Doug is on-model in every shot (red cap always visible, including ghost Doug and the
dead/flat poses), and the zone ramp is consistent (sunlit `#3a9ad9`, then twilight `#1b4f86`, navy `#0b2447`, abyss
`#050a1f`, hadal `#020308`). The caption bars match the item names, the death counter runs 46 to 56 in order, and gore
never goes beyond cartoon level.

### Fixed by me (in `shotlist.json`, re-rendered and verified)
1. **s251:** the tubeworm silhouettes had `glow_r: 0`, so they were black on hadal black and invisible. Style bible §7.7 calls for a red glow. Set `glow_r: 260`, `glow: #d6332a`. They read now.
2. **s149:** the "EVERY FINGERNAIL" WordArt overlapped Doug's cap and the scientist's head. Moved it to y=150, clear of both heads and below the caption bar.
3. **s191:** the depth meter was drawn under the ground cutaway (its lower half and the "~3,000 M" label were hidden). Reordered so the meter draws after the ground.

### Notes for the director (composition, non-blocking, worth a pass before the final render)
1. **s015-s019:** the same crater cross-section with sharks five times in a row. Break it up: for example, s017 a close-up on the plume and thermometer, s018 a close-up on the scientist and microbes.
2. **s128-s135:** the brine pool at the same scale with Doug top-right for about 8 shots. Add one or two close-ups (a crab crossing the rim in s133, a big preserved fish in s134/s135).
3. **s089:** the POSEIDON label sits next to the 4th chimney while Doug climbs the 3rd, and the climbed chimney is not the tallest. In s079 Poseidon is the tallest, centre chimney. Keep Poseidon the same chimney (tallest) and put the label on it.
4. **s061, s068, s247:** these shots drop the depth meter while their neighbours have it. Add it back, or accept the omission as a deliberate beat.
5. **s103-s116:** surface iceberg scenes still show "~900 M" on the meter. Consider "0 M" or hiding the meter for the surface beats.
6. **s207-s222:** the orb-on-rock framing repeats (s209, s210, s211, s215, s219-s222). The gag beats s219-s221 justify continuity, but s215 could be a tighter close-up.

## Files touched
- `assets/library/manganese_nodule.json` (inner shading and bumps pulled inside the outline)
- `episodes/006-disturbing-deep-sea-discoveries/shotlist.json` (s149, s191, s251)

## Final keyframe review (after the director's 23 shot changes)

All 278 keyframes re-rendered and all 24 contact sheets checked. The director's changes (s015, s017-s019, s061, s068,
s089-s092, s103-s105, s113-s116, s128, s133-s135, s215, s247) resolve notes 1-6 above:
- **s017/s018** break up the crater run (plume plus thermometer close-up, then the scientist and microbes on a ledge). s015, s016 and s019 still share the crater composition, but they are no longer consecutive.
- **s089-s092:** Poseidon is the tallest centre chimney in s079, s089 and s090, it carries the label, and it is the one that breaks in s091/s092. Continuity holds.
- **s061, s068, s247** have the depth meter again. **s103-s116** surface beats read "0 M".
- **s133/s134** are tight crab-on-the-rim close-ups and **s135** is a cutaway of the pool's contents. The brine run now has three layouts.
- **s215** is a tight orb close-up and is clearly different from s209-s211.

### Fixed by me in this pass (in `shotlist.json`, re-rendered and verified)
1. **s113-s116:** the sky was `#c9d6df` (an off-palette grey) while the iceberg shots s103-s105 use the bible sky `#8fd3ff`. All four now use `#8fd3ff`.
2. **s113:** the bobber sat on the ice edge. The line now drops into the water at (1075, 772).
3. **s114:** Doug stood up (`hands_hips`) but the rod was still anchored at his old seated hand, so it floated free. Changed him to `point` and re-anchored the rod at his hand. The line ends in the water.
4. **s115:** there were two caps (one on the iceberg, one on falling Doug). Removed the loose `doug_cap`. The left-behind cap appears in s116, after he is gone.
5. **s116:** the "THE MONSTER" WordArt crossed the bubble trail. Moved the bubbles and ghost Doug to x≈1720 and the WordArt to x=1280. Text, arrow and bubbles are now all clear of each other.
6. **s240:** auto-ink sampled the black divider line and drew Doug in white on cream (head outline and body nearly invisible). His spine also merged with the divider, so he looked impaled. Set `ink: #000000` and moved him to x=1060, off the line.
7. **s215:** the "LEAST DRAMATIC" WordArt nearly touched the "~3,250 M" meter label. Moved it to x=830.

### Checks
- Doug is on-model in every shot. The red cap is visible everywhere, including the ghost, flat and floating poses. Nothing is gory.
- The zone ramp is consistent from sunlit to hadal. The meter and the counter (46 to 56) run in order. Captions and labels sit inside the safe area.
- s068: the first "DOWN" label sits high in the keyframe, but it belongs to the camera pan down the shaft (labels at y=1100/1700/2300). Accepted.

**Verdict: PASS**
