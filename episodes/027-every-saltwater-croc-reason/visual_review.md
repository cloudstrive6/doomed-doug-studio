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

## Round 4: Thumbnails (2026-10-26)

Scope: `build/thumbnail.png` (A), `build/thumbnail_b.png` (B) and `build/thumbnail_c.png` (C), each viewed at 1280x720, at 168x94 (`*_small.png`) and in zoomed crops. They were checked against the title "Every Reason the Saltwater Crocodile Is the Scariest Reptile", the `thumbnail_brief` banned-word list in `metadata.json`, the brief's thumbnail and risk sections, and the no-leap rule in `decisions.md`.

**VERDICT: FAIL** (variant C only). A and B pass and can ship as the A/B pair. C has to be fixed or dropped from Test & Compare.

| Variant | Result | Summary |
|---|---|---|
| A (hero, "IT WAS THERE") | **PASS** | Clear focal point and readable at feed size. Doug is on-model. Jaws are closed and empty. No title words. |
| B (cross-section, "11.5 HOURS") | **PASS** | The strongest of the three at 168x94. The croc reads instantly, its snout is under the canoe, and the claim is sourced. |
| C (4-tile grid) | **FAIL** | The Skin tile can't be read at feed size (speckle that looks like a rash). The Dive tile is weak and repeats the Size silhouette. |

### A: PASS
- Feed size: "IT WAS THERE" is fully legible. The yellow eye, the tooth line and the ripple ring make the threat obvious. Doug's red cap and white head stand out against the green water. Doug and the threat read in under a second.
- Text: no word from the title or alt-title list. Nothing is cropped, and the text doesn't overlap any drawing.
- Doug is on-model (red cap, white head, scared face, sweat drop) and small, used as a scale figure.
- Policy: the jaws are closed with nothing in them. No blood. Not kid-coded. Not a leap: the croc's body stays under the water, and the head and neck rise from a ripple ring, which fits the `decisions.md` limit of "rising out of the water, body mostly submerged, jaws closed".
- Minor (graphic designer, optional): the snout tip is cropped off the top right edge. The snout is the croc's most recognisable feature, and the near-vertical head and neck lean slightly toward "sea serpent or dinosaur" at 168 px. If you redo A, lower the head angle by about 15-20 degrees so the snout tip and nostril sit inside the frame.

### B: PASS
- Feed size: "11.5 HOURS" is fully legible. The whole croc body, with its scutes, eye and curled tail, reads instantly as a crocodile. The canoe on the waterline with Doug in it and the bubbles from the snout just under the hull sell "it's right under you" at a glance.
- Text: "11.5 HOURS" uses no title or alt-title word, and it is sourced (Queensland Museum, `facts.md` line 38). It isn't misleading.
- Doug is on-model and readable. No blood, the mouth is closed, and nothing is kid-coded.
- Minor (illustrator, optional): the two legs are drawn as flat boot or flipper shapes, and the hind foot hangs into the mud band. This only shows at full size.

### C: FAIL
1. **Skin tile (graphic designer + illustrator):** the snout is covered in about 200 small yellow dots. At 168x94 they read as glitter, noise or a rash, not as pressure sensors, and the dense spotting comes close to trypophobia. Fix: crop tighter on the snout tip and show about 10-15 larger, evenly spaced sensor domes, or replace the tile with a different item (for example The Comeback).
2. **Dive tile (graphic designer):** the croc is a thin strip along the bottom of a plain green panel. At feed size it reads as "croc lying on mud", not as "stays under for hours", and its side-on silhouette repeats the Size tile. Fix: put Doug's canoe on the surface line at the left with his red cap visible (as in B), and let the croc fill more of the tile's height. Keep the jaws closed.
- Optional, not blocking (graphic designer): 4 of 11 chapters undersells "Every". The owner's 2026-10-20 C-grid rule (4-6 big tiles, `.claude/agents/graphic-designer.md`) allows 4, so this isn't a fail. A fifth or sixth tile such as The Comeback is worth trying if it stays readable at 168 px. Keep The Lunge and The Roll out (leap reading).
- No routing conflict: the creative director's 2026-10-26 thumbnail gate in `decisions.md` keeps C as the third Test & Compare arm. My fixes 1-2 agree with the CD's two required changes. The CD's figure of about 25-40 larger domes for Skin is fine too, as long as they read as separate points at 168x94.

Fine as drawn in C: the labels (Skin, Size, Home, Dive) are legible at feed size and avoid every banned word. Doug is on-model in the Size tile. The Home tile's bathtub croc with the floating cap is a cartoon death with no gore, and it matches the "He goes to run a bath" shot, so it isn't misleading.

### Checks passed on all three variants
No gore, no blood, no teeth on Doug, no hatchlings, no leaping croc, no kid-show tone, no title words in the thumbnail text, no MS Paint artifacts, and no text cropped at the edges.
