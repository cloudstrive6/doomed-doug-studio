# 027-every-saltwater-croc-reason: art review (round 2: assets + keyframes)

Reviewer: art director, 2026-10-26
Scope: the 5 round-2 asset fixes (`assets/previews/027-every-saltwater-croc-reason-assets-r2.png`, `-assets-r2-full.png`) and all
28 contact sheets (`build/contact/sheet_01..28.png`, s001-s330 + endslate).

## Verdict: FAIL (round 2). Assets all APPROVED. Composition fixes go to the director (no illustrator work needed)

The hard rules pass on all 331 frames. **No gore**: no blood or wounds, and every death cuts to a splash plus cap or a ghost. Teeth never
touch Doug. Jaws are closed on every croc with food (s114/s115 hatchling, s213-s231 grey shape). The only body-length motion is
`croc_lunge_rising` (s201), and it shows the front third only. Doug is on-model everywhere: red cap, round head with crescent, auto-white
on the night, sober and Roll grounds (s050-s052, s330). Zone colours follow the time-of-day ramp, and each chapter keeps its own colour.
The ramp is now in the art bible. The failures are one asset placed with a severed-looking edge, text over the treeline, and five runs of
the same composition.

## Round-2 assets
| Asset | Verdict | Note |
|---|---|---|
| croc_jaw_closeup | APPROVE | The neck runs off the left edge at every placement (s037-s040, s045, s046, s048). No cut edge shows |
| croc_jaw_closeup_lit | APPROVE | Same geometry. Dots are densest on the jaws (s040, s053) |
| croc_tongue_closeup | APPROVE | The throat runs off the left edge in s071. The grey pores read as pores, not specks |
| croc_mother_hatchling | APPROVE | The neck and shoulder run off the right edge in s114 and s115. The hatchling is small and not cute |
| bathtub_croc | APPROVE | Fix B works. The sloped neck grows out of the water, the cap reads on the rim (s183-s185, s329) |
| croc_holding_shape | APPROVE | Fix C works. The grey oblong crosses the jaw line, with the upper jaw drawn over it. It reads as gripped at s213 scale |

## Required fixes (director)
1. **Severed-looking open-jaw head (`croc_jaws_open`, a library asset from 011).** Its flat vertical back edge sits mid-frame and reads as a
   cut-off head, the same rule as round-1 fix A. Push the edge past the frame:
   - **s054, s055** (sage studio, no water, the worst cases): `"flip": true`, x 1150 → **1650** (scale 1.0). The snout then sits at about x 1330,
     facing Doug. Move `small_fish` to about x 1180 and its motion line to its left (s054).
   - **s066, s067, s068, s070** (sea): `"flip": true`, x 1150 → **1650**. **s065**: flip, x 1250 → **1710** (scale 0.7). Re-aim the s068 arrow and "?"
     and the s070 SALT GLANDS arrow at the new mouth.
   - **s105** (already flipped, on the mud next to the nest): x 1500 → **1690**.
2. **Text over the mangrove treeline (40 shots).** Wordart, titles and labels cross the canopy of the horizon clumps (canopy y 327-454). Move each
   text's centre to **y ≤ 255** (size ≤ 110, clear of the counter box), or delete the clump directly behind it:
   s007, s008, s035, s036, s082, s094, s095, s096, s097, s098, s099, s103 (FEMALE), s105, s107, s112 (top chirp), s114, s116, s120, s121, s122,
   s123, s124, s125, s126, s143, s144, s145, s146, s149, s186, s187, s194, s213, s214, s232, s236 (TO ESCAPE), s238, s262, s263, s267.
   Chapter titles (THE DIVE/SKIN/EGG/SIZE/LUNGE/ROLL) at size 140 may sit at y 245. They span about x 660-1260, so they are clear of the counter.
   This rule is now in the art bible (Text: "Treelines count as land").
3. **Same composition too many times in a row. Break every run to 4 shots or fewer** (keep the narration and the item colour):
   - **s129-s137 (9 framed-card shots: Lolong, then Cassius).** Recompose at least two. Suggested: s132 (DIED 2013) as a plain calendar card like s141.
     s134-s136 as a big Australia map with Doug beside it (card dropped). s137 (WELL BEYOND) as a two-bar age comparison, wild croc vs Cassius.
   - **s143-s152 (10 identical riverbank shots).** Recompose at least three. Suggested: s146 a close crop on the hind legs where the tape ends,
     s148 a `croc_sleeping` close-up with the Zs, and s151/s152 a side-on diagram of tape vs croc on cream (as at s190).
   - **s160-s165 (6 Cape York map shots).** Recompose s161: `croc_in_sling` under the helicopter over sea, or a 1.6x zoom on the release point. **s168-s172 (5)**:
     recompose s170, the sleeping croc close-up at the release point, on sea `#3a9ad9`.
   - **s279-s283 (5 identical Indonesia maps).** Recompose s282 as a coin-flip card (big `coin` plus the `60 FATAL` / `100 ATTACKS` labels, no map), or s283
     as the fishing boat alone on dark water (no people).
   - **s296-s301 (6 sepia map + graph shots).** Recompose s298 and s299 as the graph at full width without the map, so the drop to 1971 reads larger.
4. **s107: the flood swallows a living Doug.** The `rect` (y 740-890) is drawn over Doug, and only his cap tip shows, which reads as a death
   before his death in s119. Draw Doug after the rect, wading with feet at about y 780 and the shock face, and extend the rect to y 1080 so the
   flood doesn't leave a mud stripe under it.
5. **s086: Doug runs on the sea.** His feet are at y 694, above the water, and the sand top at x 380 is about y 755. Set y to about **752**.

## Optional (not blocking)
- s037-s040, s053: Doug's black legs and body cross the dark olive neck of the jaw close-up. They read only because the head is white. Dropping Doug
  below the jaw, as in s045-s048, would read cleaner.
- s084, s286, s287: the red X covers only the middle letters ("SALT ATER", "TH EAT", "MIS AKE"). Scale `red_x` up, or use a strike line across the
  whole word.
- s001 is the thumbnail placeholder (graphic designer).

## The concern: few Doug shots in the sober Legend/Menu sections. Verdict: acceptable, keep it
- The numbers: The Legend runs s240-s261 (22 shots, about 74 s) with no Doug. Then a Doug bridge runs s262-s270 (rock, record book, flashlight, about 25 s).
  Then The Menu runs s271-s288 (18 shots, about 50 s) with no Doug. Doug is still in 82% of shots overall.
- Why it's right: The Legend covers real wartime deaths, and The Menu covers real attack victims (mostly fishermen). A stick-man gag next to them would turn real
  dead people into a punchline, which is a tone and advertiser-friendliness risk. That risk is worse for a not-made-for-kids channel that relies on
  "cartoon deaths only". The 004 Lake Nyos precedent (white title, no gag) is the house rule, and this applies it.
- Why it holds attention: neither stretch runs over about 75 s. Doug comes back between them and again at s289. The sober frames change every shot
  (book, map, documents, text lists, world map, croc row, field guide), so on the contact sheet they read as a deliberate change of mode, not dead air.
  The one exception is the Indonesia map run (fix 3, s279-s283), which has to be broken up.
- Conditions for the editor: keep sober holds tight (no hold over about 4 s on a text-only card such as s254 or s257), and keep the music sting out as the brief says.

After the fixes, re-render keyframes for every shot listed above (`python -m studio keyframes 027-every-saltwater-croc-reason --shots ...`) and send them back
for round 3. Only the changed shots need review.
