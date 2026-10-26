# Visual review: 027-every-saltwater-croc-reason

## Round 2: pre-render keyframes (2026-10-26)

Scope: all 28 rebuilt contact sheets (s001 to s330 plus the endslate, 331 keyframes). I zoomed into the full keyframes for s030, s105, s107, s195 and s201. The thumbnail (s001) is still pending, so it was not reviewed.

**VERDICT: FAIL** (2 small fixes left; everything else passes)

### Round-1 fixes: status
| # | Shot(s) | Status |
|---|---|---|
| 1 | s107 flood layering | **Partly fixed.** Doug is now visible and alive. But he stands on top of the water: his whole legs show and the ripple ring sits under his feet. See fix 2. |
| 2 | s195-s212 kitchen-counter scale | Fixed. The counter is about half Doug's height, and the branch sits about 60-70 px above the waterline. In s201 only the croc's head and neck clear the water (about 180 px of about 600), well under half its body. |
| 3 | s235 death beat | Fixed. Splash, roll arcs, cap on the bank and ghost Doug all read. |
| 4 | s292 static disc | Fixed. The standard splash is at the end of the jetty and the cap is on the boards. |
| 5 | s227 all-but-one | Fixed. There are 4 ticks and 1 red X, and the label reads "ALL BUT ONE". |
| 6 | s054/s055/s105 floating head | Fixed. s054 and s055 now have a waterline. In s105 the neck runs off the right edge, so it reads as an animal coming in from off-screen, not a severed head. |
| 7 | s054 stray dash | Fixed. It is now 3 speed lines behind the fish. |
| 8 | s030 "up to his knees" | **Not fixed.** See fix 1. |
| 9 | Variety runs | Fixed. s015 is a stopwatch close-up and s017 a heart/ECG close-up. s134-s136 are maps, s137 is a bar chart and s139 is the Doug-vs-Cassius gag. s161, s166, s167 and s170 break up the Cape York map run. s221 is a side-view spin and s222 a hand holding the tail. s282 is a full-frame coin and s283 a fishing boat. s245 is text on black. No run of 4 or more identical compositions is left. |
| 10 | s041/s042 ALLIGATOR label | Fixed. |
| 11 | s154 FAR AWAY collision | Fixed. The text is now left of the sling. |

No regressions: Doug is on-model and readable everywhere, and the counter climbs correctly from 218 to 226, one step per on-screen death. There is no gore, and the Ramree chapter (s240-s261) keeps its sober, Doug-free register. Text is spelled correctly and nothing is cropped.

### Required fixes
1. **s030 (director): Doug still stands on the water.** The narration says he "wades in up to his knees". The masking rect (`x 820, y 790, w 280, h 70`) and the ripple ellipses (y 791/793) sit at or below his feet, so they hide nothing. Lower the `doug` element from y 760 to about y 800, keeping the mask rect and ripples where they are, so his shins disappear under the rect and the ripple ring sits at knee height. Move the `fishing_rod` down by the same 40 px (y 724 to y 764).
2. **s107 (director): same problem.** The leg-mask rect (`x 175, y 758, w 90, h 40`) and the ripples (y 758/760) are under his feet. Lower the `doug` element from y 719 to about y 745, keeping the mask and ripples where they are, so the waterline crosses at his knees. The flood rectangle is fine as is: the mound half-submerged is a clear "flood destroys nests" picture.

Re-render only s030 and s107 for round 3.

### Minor (optional, no re-review needed)
- s022-s024: the 28°C and 35°C thermometers show the same mercury level. Raising the 35°C fill would match "summer temperature".
- s195: the kitchen-counter prop overlaps the end of the log. Sliding it right (off the log, standing on its own on the waterline) would read cleaner.
- s300 and s304: the red population line runs through the "ABOUT 3,000" label box. Nudge the label 30-40 px left or down.
- s297: the empty chart axes on the right look unfinished for one shot. Acceptable as a set-up for s298.
- Carried over from round 1: s008, s097, s098, s123 and s143 have captions over the mangrove canopy (still legible), and the s142 object under the 1914 calendar is still hard to identify.
