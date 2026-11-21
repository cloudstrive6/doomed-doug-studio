# 054-cape-buffalo-black-death: visual review

## Round 2: keyframes + thumbnails (2026-11-21, visual screener)

Scope: I rechecked the round 1 blocking fixes at 1920x1080 in `build/keyframes/` (s010, s019-s023, s029, s040-s047,
s063-s070, s078, s085, s134, s135, s141, s148, s154). I also checked the changed shots s091, s093, s098, s104,
s138, s173 and s200, plus their neighbours s084 and s086. All three thumbnails were checked at full size and at
feed size (`build/thumbnail*_small.png`, 168x94).

VERDICT: FAIL

Seven of the nine round 1 blockers are fixed. Two are still open: s010 and part of s085. Thumbnail C needs one
clean-up. All three are quick fixes, and nothing else blocks.

### Round 1 blockers: status

| # | Shot | Status |
|---|---|---|
| 1 | s010 | **Still open.** `RANKING` is fixed: it now sits under the clipboard, clear of everything. `BLACK DEATH` was not moved up, though. It sits at y about 320-390, and "BL" still overlaps the book's top-right corner and its page edge (x about 680-760). |
| 2 | s134/s135 | Fixed. Doug's white head with X eyes and the red cap sits at the costume's neck end, the cow face is gone, and the ghost Doug in s135 reads clearly. |
| 3 | s078 | Fixed. `ONE ARM'S LENGTH` is drawn above the reeds and reads cleanly. |
| 4 | s141 | Fixed. The hidden lion is gone. Two lions are on the caught buffalo, with a clear gap to the herd, and the red arrow runs from the herd toward the lions. |
| 5 | s148 | Fixed. Doug stands in open ground to the right of the herd, and no horn crosses him. |
| 6 | s154 | Fixed. Doug's whole head and face clear the door line, giving a thumbs-up. |
| 7 | s029 | Fixed. The arrow starts beside Doug's hand and the arrowhead lands on the fused boss of the third head. |
| 8 | s085 | **Partly fixed.** The X was replaced by strike-through lines, as asked. Two problems remain (see fix 2). |
| 9 | Variety | Fixed. s020 is a close-up of Doug's deadpan face with `DID NOT AGREE`. s042 and s044 are tight shots on the branch. s066 is a close-up of the oxpecker on Doug's cap, and s068 is a tighter framing with the field guide. No run of 4 or more near-identical frames is left in s019-s022, s041-s046 or s064-s069. |

### Blocking fixes

1. **s010 (director): `BLACK DEATH` still overlaps the book.** Move the caption block up to centre y about 190,
   so it sits fully above the book's top edge (y 270). Or keep the current y and shift its left edge to x 800 or
   more (right of the book's page edge at x 765). Either way, no letter may touch the book.
2. **s085 (director + illustrator): the struck-out words are hard to read, and the GRUDGE bubble tail is broken.**
   - The bubble text is now a thin regular weight. The red line (about 8 px) runs through the middle of the
     letters and erases the crossbars of A, H and E. At phone size it reads as "AMBU-H PLAN" and a red bar. Set
     both words in the bold bubble font used elsewhere, and thin the strike line to about 4 px. Or show the words
     clean in s084/s085 and add the strike only on the last beat.
   - The GRUDGE bubble tail starts inside the bull's cheek (x about 1040, y 700). It runs as a thin open sliver
     *inside* the bubble and ends in a stray black dot (about x 1245, y 727). Redraw it as a normal closed tail
     from the bubble's lower-left edge to just in front of the muzzle, and delete the dot.
3. **Thumbnail C (graphic designer): stray swirl lines.** The tan curved strokes across the top (meant as dust)
   read as cracks or bare branches. At feed size they show as scribbles behind `1,000+`, and they pull the eye off
   the herd. Delete them, or replace them with the soft pale billows used for the s183/s186 dust cloud, kept
   behind the horns and away from the number.

### Changed shots: pass

- s091: the cap, the `NO` field guide and the glowing silhouettes all read, and the HUD shows 398. Nit: the red
  glow is now a coarse speckle, and at full size it is close to looking like spatter on the black shapes. The art
  director should confirm that it matches s113 and the art bible's glow (a soft halo, not red dots on the bodies).
- s093 and s098: the stare lines are now red, start at the standing cow's eye, and are clearly visible. This
  resolves the round 1 nit.
- s104, s138 and s173: clean. In s173 the lion is cropped at the left edge, but its face is in frame, so it reads
  as a lion.
- s200: clean. The arrow from the herd lands on Doug's cap, which matches "the small man wearing its badge". Nit:
  the herd's top-right horns run behind the HUD plaques. This is still legible.

### Thumbnails at feed size

- **A, `BLACK DEATH`** (title: "Why the 800 kg Cape Buffalo That Kills Lions Only Eats Grass"): PASS. There is one
  focal point, the bull's face and boss, and the text is readable at 168 px. Doug in the reeds is small but
  readable by his red cap, and he is looking the wrong way as the concept says.
- **B, `HE'S RETIRED`** (title: "How an 800 kg Cape Buffalo Kills Without Ever Eating Meat"): PASS. The bull's head
  and boss are the focal point and Doug with his camera is clear. The crouch legs the designer flagged read as a
  squat at full size and are invisible at feed size. Nit, optional: the vertical shin crosses the mud rim, and
  ending the feet on the ground just right of the mud would look tidier.
- **C, `1,000+`** (title: "Why the Cape Buffalo Gets Deadlier the Bigger the Herd"): FAIL on fix 3 only. The herd
  wall, the number and Doug (with his intern badge) all read at feed size. The fleeing lion is small but works as a
  secondary read.

None of the three is misleading, and each one matches its paired title.

### Nits still open from round 1 (non-blocking)

s001 (caption at the left edge), s013 (`RETIRED` touches the frame), s087 (page margin), s183 and s186 (captions
over the dust), s056-s058 (Doug against the fence post), s175 and s176 (horn tip touching Doug's face), s197
(lion against the herd). Also new: in s084 the red `?` covers "STORIES" on the book ("S??ES"). That is OK as a
gag, but moving the `?` beside the book would keep the title readable.

### Checked and fine

The HUD steps correctly through every death beat (396 to 402). Doug is on-model in every shot I rechecked. There
is no gore and nothing reads as a kids' show.
