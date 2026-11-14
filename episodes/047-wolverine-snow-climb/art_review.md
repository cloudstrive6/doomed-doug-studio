# 047-wolverine-snow-climb: art review (art director, 2026-11-14)

## Verdict: PASS (round 2)

Round 1: assets PASS, keyframes FAIL (6 composition fixes). Round 2: I made all fixes directly in
`build/gen_shotlist.py` (narration unchanged, checked against the round 1 shotlist: all 178 lines identical), regenerated
`shotlist.json` and re-rendered all 179 keyframes. `validate shotlist` is clean apart from the expected s001 thumbnail ref.

## 1. New assets (24): PASS

Previews: `assets/previews/047-wolverine-snow-climb-assets-a(-context).png`, `047-assets-b(-onsnow,-fitcheck).png`,
`047-assets-items8-9.png`, `047-assets-den-context.png`, `047-assets-climb-context.png`, `047-assets-crampons-climbing-closeup.png`.

| Asset | Notes |
|---|---|
| altitude_stake | Clear 4-band ramp (rock grey, snow white, ice blue, forest green). Reads as the HUD meter at 0.24. |
| reindeer | Detailed tier, pale rump, ruff and saddle shading. Recognisable at 0.6. |
| reindeer_costume / _flat | Costume reads on Doug and keeps the cap visible. The flat death is cartoon only, with loose antlers and no blood. |
| lynx | Spots, ear tufts and ruff. Reads next to wolf and bear at small scale. |
| fennoscandia_map | On palette and matches the library map style. |
| wolverine_bloated | Round "drum" belly, library wolverine palette. Not cute, not gory. |
| old_map_north | Strong period look (sea serpent, compass rose). The small wolverine inset reads. |
| twin_pines | Bent trunks make a clear "gap". They pair with pine crowns in context. |
| chest_freezer, frozen_food_lump, box_trap, log_cabin_open | Bold silhouettes with layered fills. All read on snow (onsnow preview). |
| wolverine_trotting | The workhorse (31 shots). Palette is exact (dark coat, tan flank band, pale claws). The belly fringe reads as shaggy fur at shot scale. The silhouette and red-glow version works. |
| wolverine_digging, wolverine_paw | The head-in-snow pose reads. The paw-vs-boot scale beat reads, and the claws are pale, not bloody. |
| paper_map, high_heel, snowshoe | Clear props. The heel-in-sand vs snowshoe split reads instantly. |
| wolverine_den_cutaway | Tunnels around boulders, with **no kits** (brief sec 7 respected). |
| doug_snowdrift | Snow mound with the red cap on top. Doug stays on-model by implication. Cartoon death. |
| mount_cleveland | Tall, icy face with strata bands. Works at scale 1.0 and in the tall pan. |
| wolverine_climbing, crampons | Climbing pose reads at 0.5-0.65. Crampons are only legible at Doug scale 0.3+, which is how they are used. |

Doug: no rig changes this episode. He is on-model in every shot, with the cap visible in all deaths, the ghost and the snowdrift.

## 2. Keyframes (178 shots + endslate)

Overall: the style is consistent. The zone ramp follows the stake: forest grey-blue, treeline blue with snowy firs,
snow slate, then summit dusk blue, and finally the dawn orange payoff. Every frame has the caption bar. The HUD
(counter + ALTITUDE) is consistent and its value ticks correctly 356 to 363. Death beats are cartoon only, and layouts
vary well. The longest same-composition run is s094-s097 (4 shots, a build-up on the cross-section), which is inside
the 2-6 rule.

### Round 1 fixes (composition, routed to director; applied by me in the generator)
1. **s006**: the wolverine was drawn on Doug's head (overlap), and FINLAND wordart crossed the map frame and land.
   I moved the wordart into the clear cream area at (1480, 420), put the wolverine on the ground at (1400, 990) and
   moved Doug to x 1760. **Fixed.**
2. **s011**: SWEDEN wordart sat on the land mass (art bible text rule). I moved it to the clear side at (1420, 380),
   above the banknote. **Fixed.**
3. **s008, s021**: the `narrator_hand_pencil` sleeve stopped mid-frame (around x 1170 and x 1440), so the arm floated.
   In s021 the ghost Doug also sat on the arm's path, in a busy pine row. I added a sleeve extension to the frame edge
   (`SLEEVE` helper), raised the EARLY SPRING label above the arm (1500, 380) and moved the ghost to clear snow at
   (1330, 860). **Fixed.** I added the rule to the art bible (Narrator hand).
4. **s095**: the red arrow at y 300 crossed the ALTITUDE meter in the reserved counter zone. I moved it to y 390.
   **Fixed.**
5. **s141**: SNOW COVER wordart touched the world-map frame's bottom edge. I raised the map to y 720 and set the
   wordart to (760, 1000) at size 80. **Fixed.**
6. **s162** (tall pan): STRAIGHT UP wordart sat on top of the climbing wolverine, and the wolverine was small for the
   hero beat. I moved the wordart to clear sky at (390, 820) at size 84, inside the safe area, and scaled the
   wolverine 0.5 to 0.65. **Fixed.**

### Checked and accepted (no change)
- s020, s041, s060, s118, s136, s153, s175-s177: death beats are cartoon (X eyes, cap, ghost, snowdrift, black cut).
  s175 shows as a black keyframe because the keyframe is the shot's final state after `black_cut(0.62)`. Rendered at
  t=0.6, it shows the flag, flying cap and speed lines correctly.
- s147, s148: the wordart uses the white/yellow override on the green summer meadow and sits in the sky (art bible
  green-ground rule).
- s012, s015, s152: the den rings show a hole and adult silhouettes only. No kits anywhere.
- s162: the HUD is in scene space, so it enters only during the second half of the pan_up. This is the same as
  previous tall-pan shots, and the shot lasts under 2.5 s.
- s001: thumbnail ref pending (designer), ignored as instructed.

No illustrator fixes required.
