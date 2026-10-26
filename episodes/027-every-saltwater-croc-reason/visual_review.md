# Visual review: 027-every-saltwater-croc-reason

## Round 3: pre-render keyframes (2026-10-26)

Scope: the shots changed in the round-2 fix commit (s022, s023, s024, s030, s107, s123, s282, s300, s304), viewed full size in `build/keyframes/` with zoomed crops of s030 and s107. I also skimmed the rebuilt contact sheets (sheets 01-04, 09, 11, 24 and 26 in detail) for regressions. No other shot changed in the shotlist, and the only new asset is `coin_generic`. The thumbnail (s001) is still pending, so it was not reviewed.

**VERDICT: PASS**

### Round-2 fixes: status
| # | Shot(s) | Status |
|---|---|---|
| 1 | s030 "up to his knees" | Fixed. Doug was lowered to y 800 and the mask grew to h 100. The waterline and ripple ring now cross his lower legs, so only his hips and upper legs show above the water. He clearly reads as wading. The rod lowered with him and his hand still meets the grip. |
| 2 | s107 flood | Fixed. Doug was lowered to y 775 and the mask grew to h 90. He stands in the floodwater with the ripple ring around him, panicking, and the half-submerged mound still reads as "floods destroy nests". |
| m | s022-s024 thermometers | Fixed. The 35°C mercury is now visibly higher than the 28°C one in all three shots. In s022 it appears at 0.5 together with its thermometer. |
| m | s300 / s304 label collision | Fixed. "ABOUT 3,000" moved to x 1310, y 810 and the red line no longer crosses it in either shot. |
| m | s123 | "FOLLOWED." moved left (x 880) and no longer crowds the death counter. Having no chapter tab is intentional (`topbar: false`, a chapter-end card like s035). |
| m | s282 coin | The new `coin_generic` (a silver coin with a star, no US-quarter design) is clear and centred, and the flip arcs read as a coin toss. "100 ATTACKS", "60 FATAL" and "WORSE THAN 50/50" are legible and match the narration. |

### Regressions
None found. Doug is on-model (red cap, white head) and readable in every changed shot. Text is spelled correctly and nothing is cropped. The counter still holds at 218 through s030, 220 at s107, 221 at s123 and 225 at s300/s304, which matches round 2. There is no gore and nothing kid-coded.

### Minor (optional, no re-review needed)
- s030: one stick leg pokes a few pixels through the inner ripple ring. You can only see it when zoomed in, so it is not an issue at playback size.
- s300 vs s304: "1971" is a white boxed label in s300 but plain brown text in s304. The jump between the two consecutive chart shots is small but visible. Pick one style (director).
- Carried over: s195 kitchen-counter prop overlapping the log, s297 empty axes, mangrove-canopy captions (s008, s097, s098, s123, s143), and the s142 object under the 1914 calendar. All are acceptable.

Next: the thumbnail and the post-render checks (samples, qc.json, thumbnails, Shorts) still need review once they are built.
