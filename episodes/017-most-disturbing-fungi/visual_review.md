# Visual review: 017-most-disturbing-fungi

## Round 1: keyframes (2026-10-13)

The verdict was FAIL with 23 fixes: text colliding with the counter, drawings or the frame edge; pictures that didn't match the narration (s061, s099, s192, s097); a red "menace" stipple that read as blood (s047, s061, s257); the porpoise drawn as a fish (s210/s211); a horse drawn on top of a cat (s249); huts behind the hospital grid (s167); and an unreadable footnote (s234). Round 2 below checks each one.

## Round 2: keyframes + thumbnail (2026-10-13)

Scope: all 266 re-rendered keyframes (contact sheets `build/contact/sheet_01–23.png`) plus full-res crops of every borderline shot. Also checked `build/thumbnail.png`, `build/thumbnail_small.png` and `thumbnail.json` (3x3 grid). I re-rendered nothing.

### Round 1 fixes: verification
| # | Shot | Status |
|---|---|---|
| 1 | s015 DOESN'T STOP vs counter | Fixed. About 50 px horizontal clearance. |
| 2 | s023 CAN'T INFECT PEOPLE | Fixed. About 60 px clear. |
| 3 | s024 DRESSED AS A CICADA | Fixed. |
| 4 | s141 MORE THAN A DOZEN | Fixed. About 90 px clear. |
| 5 | s198 ABOUT AS WELL | Fixed. |
| 6 | s157 INTO A COUNTY | Fixed. About 110 px clear. |
| 7 | s036 BEFORE SUNSET vs Doug | Fixed. About 75 px gap to the fly-eye bauble. |
| 8 | s030 GETS THE REST vs sun | Fixed. The sun now sits beside the text. |
| 9 | s088 MORE THAN HALF edge | Fixed. Now inside title-safe. |
| 10 | s061/s062 GUNPOWDER STORE label | Fixed. Moved left, fully readable. |
| 11 | s108 WHITE-NOSE SYNDROME vs bat | Fixed. |
| 12 | s125 ENDANGERED vs bat | Fixed. |
| 13 | s206 CRYPTOCOCCUS GATTII vs tree | Fixed. |
| 14 | s242 WHO label vs red cross | Fixed. The building moved down; the cross is clear. |
| 15 | s061 white spider | Fixed. The lit spider is the white, fungus-coated asset. |
| 16 | s099 card text | Fixed. Reads "GREATEST RECORDED LOSS OF BIODIVERSITY TO A DISEASE", sober. |
| 17 | s186/s192 researcher card | Fixed. s186 has the hedged card "ACCORDING TO LATER ACCOUNTS: 10 OF ~12 DIED". s192 shows spores going to the lungs, with LUNG INFECTIONS and WEAK IMMUNE SYSTEMS. |
| 18 | s097 crossed-out ratio | Fixed. 4 of 20 crossed out. |
| 19 | s047/s061/s257 red stipple | Fixed. Now a dark purple haze; nothing reads as blood. |
| 20 | s210/s211 porpoise, ferret | Fixed. A ferret was added and the porpoise has a dorsal fin, flukes and a blunt snout. See advisory A3. |
| 21 | s249 cat/horse tangle | Fixed. Cat and horse are now separate. |
| 22 | s167 huts under hospitals | Fixed. Plain ground. |
| 23 | s234 footnote | Fixed. Large "FOOTNOTE: NEW YEAST" with an arrow. |

### New scan: what's still good
- The death counter runs 139 to 147, +1 on each death shot (s029, s056, s079, s106, s131, s178, s229, s261). The two "Doug is fine" beats (s154, s204) don't change it.
- Doug is on-model in every costume, with the red cap readable everywhere. The cap-only gag at s262/s263 is intentional.
- The sober cards (s099, s152, s168, s186, s223, s243) have a plain background, white text, no Doug and no counter.
- No gore. Every death is cartoon (X-eyes, ghost, fuzz-covered Doug at s261). Nothing reads as kids' TV.
- No stale runs. s127–s130 is the deliberate alarm-clock rhythm gag.
- The cold open (s001) matches the thumbnail grid, so the opening image is consistent.

### Fixes required

1. **s176** (director, composition): the "HALF" label box overlaps the brim of Doug's cap. The loaf also looks whole, so the label isn't clearly attached to anything. Move the label so it sits centred above the loaf, at least 20 px clear of the cap. Better still, show a visibly half-eaten loaf (illustrator: a bite-cut variant of the loaf asset, if one exists).
2. **Thumbnail, "White Nose" tile (row 2, centre)** (graphic designer): the bat's head, which carries the white-nose fuzz and is the whole point of the tile, is cut off by the tile's bottom border. At 320x180 the bat reads as a brown seed pod or cocoon. Scale the bat down to about 75% and move it up so the head, ears and white muzzle sit fully inside the tile with about 15 px margin. If possible, use a wings-spread or face-forward bat pose so it reads as a bat at feed size. Leave the other 8 tiles alone: they read well at small size and the labels are legible.

### Advisory (not blocking)
- A1. s042: the grass-blade tip pokes into the bottom of the "PARASITE DAYS" label. Nudge the label up about 20 px.
- A2. s067: the "DIM, DAMP" label hangs under a measurement-style dashed line beneath the spider, which looks like a size callout. Drop the dashed line, or move the label away from the spider.
- A3. s210/s211: the porpoise has a whale-style blowhole spout, which makes it look like a small whale. Removing the spout would make it read as a porpoise.
- A4. s183: the narration caption on the contact sheet renders "Kraków" as "Krak□w" (missing glyph in the caption font). The in-frame label is correct. Check that the subtitle/Shorts caption font has the ó glyph before the final render.
- A5. Carried over from round 1: s007's red arrow arriving from the Atlantic still implies something coming from overseas. s002 still has no person for "STARTED ON PEOPLE".

VERDICT: FAIL

## Round 3: narrow re-check (2026-10-13)

Scope: `build/keyframes/s176.png`, `s210.png`, `s211.png` and `s242.png`, plus `build/thumbnail.png` and `build/thumbnail_small.png` (with full-res and 4x crops of the White Nose tile). I re-rendered nothing.

### Round 2 fixes: verification
| # | Item | Status |
|---|---|---|
| 1 | s176 HALF label vs cap | Fixed. The label now sits above the loaf, about 45 px right of the cap brim tip, with no overlap. The loaf has a visible bite cut and crumbs below it, so "ate half of it" reads at a glance. |
| 2 | Thumbnail White Nose tile | Fixed. The bat (scale 0.36, hanging from a dark ceiling bar) fits fully inside the tile: ears and head are about 25 px above the bottom border at full res. At 320x180 it reads as a bat hanging upside down (folded wings, pointed ears), with the white fuzz dots visible. That's the classic hibernating pose, which suits white-nose syndrome. The other 8 tiles are unchanged and still read well. |

### Spot checks
- s210/s211: ferret, porpoise (dorsal fin, flukes), llama and horse are all clear. Each animal has its own question mark. On s211, ANIMALS FIRST and THEN PEOPLE are legible and clear of the drawings. The arrow points to Doug and the counter stays at 145. Advisory A3 (the porpoise's blowhole spout) still stands but doesn't block.
- s242: the CDC and WHO labels stack cleanly, with about 40 px clear of the red-cross sign. The counter is at 146, Doug is on-model, and the picture matches the narration.

### Advisory (not blocking)
- A6. s176: the bitten loaf floats at Doug's head height with no hand or surface under it. It reads fine in this style. If the director wants it tidier, drop it onto a crate or put it in Doug's hand.
- A7. Thumbnail White Nose tile: the white fuzz sits on the wing edges and throat more than on the muzzle itself. Putting a small white tuft right on the face would sell "white nose" better. Optional.
- Earlier advisories A1–A5 are carried forward unchanged.

VERDICT: PASS
