# 028-megalodon-every-era: visual review

## Round 1 (2026-10-27): pre-render keyframes + thumbnails

Scope: all 26 contact sheets (s001-s309 + endslate), `build/thumbnail.png`, `thumbnail_b.png`, `thumbnail_c.png`
and their 168x94 `_small` versions. I zoomed into the full-res keyframes for s010, s033, s035/s036, s095, s097,
s108 and s252.

Policy: PASS. There is no gore. Every death is a cartoon ghost float or a frozen block, and the shark's mouth is never
on Doug. Nothing reads as nursery tone. Ruby (s063-s078) is a neutral stick figure, which is fine. The HMS Challenger
flies a white ensign, not a US flag, so it is correct. The HUD (deaths 226 -> 234, meg survived 0 -> 4/11) stays
consistent the whole way through.

### KEYFRAMES: VERDICT: FAIL

Blocking fixes:

1. **s010 (director): Doug appears twice.** He waves from the time machine on the sand bank AND sits in the cage
   (second `doug` element at x1094 with scuba gear). Remove one. Keep the cage Doug, because the cage sequence
   follows, or drop the cage from this shot.
2. **Chapter-title cards collide with the cage (director).** The red title and the date/place sub-label are drawn
   over the cage top and its rope in s004, s031, s060, s111, s138, s166, s218, s244 and s272. Move the cage down or
   left by about 150 px, or move the title block to the right two-thirds, so the sub-label sits on clear water. This
   is the chapter opener every viewer sees, so it has to be clean.
3. **The mosasaur silhouette is unrecognisable (illustrator).** In `mosasaurus` with `silhouette: true` (s030,
   s034, s035) the fill bulges into a blunt, sperm-whale head. Put s035 next to s036 and it does not match the
   pointed-snout drawing. It also looks like the Livyatan silhouette in s113, so two different teases read as the
   same animal. Fix the silhouette fill so the outline follows the visible snout and jaw. Re-check all three shots.
4. **s054 (director): the action contradicts the narration.** "has to swim up to the surface for a breath", but the
   mosasaur is angled nose-DOWN, with its tail at the top beside the up arrow. Flip or rotate it so the snout points
   at the surface and the arrow leads from the snout.
5. **Runs of near-identical "cage left + board/shark right" compositions (director).** Break each run below 4 with a
   cutaway: Doug out of the cage, a close-up, a size comparison or a scene change.
   - s017-s020 (4 boards in a row)
   - s072-s075 (4 boards)
   - s146-s150 (5 boards)
   - s203-s208 (6 boards)
   - s278-s288 (**11 boards in a row**, the worst run in the episode, at the payoff chapter. It needs at least 3
     breaks, e.g. Doug at the dig site for s279-s280, a full-frame rock wall for s283, a beach/tool cutaway for
     s287)
   - s097-s100 and s106-s110 (the same cage-at-surface + star + shark frame 9 times across the Supernova chapter)
   - s180-s185 (6 frames of the same cage + big shark)
6. **s252 (director/illustrator): the stack is unreadable.** Six thin grey spikes on black do not read as Burj
   Khalifa. Add a "BURJ KHALIFA" label, draw at least the bottom tower with a base, and keep the top tower below the
   HUD band. Right now its tip runs into the sky strip.
7. **s207 and s208 (director): the patches are almost invisible.** The "dense patches" spray circles are pale teal
   on blue/cream and practically disappear. Use solid green plankton clumps, like the dots in s206, packed into 2-3
   blobs.
8. **s008 (director): the chalkboard covers the subject.** It hides the megalodon's head and "ONE VERDICT" sits on
   its belly. Move the board above-left of the shark and put the text in clear water.
9. **The bus asset (illustrator) is a yellow school bus.** It is used in s049 and s071 ("city buses") and s156
   (labelled "A CITY BUS"). The label contradicts the picture, and a school bus is kid-coded iconography for a
   not-for-kids channel. Draw a city transit bus (white/red or grey, flat front, route sign) and swap it in all three
   shots.

Should fix (polish, not blocking on their own):

10. **s024 (director):** the "2x DOUG" comparison has no Doug beside the pup. Add a small standing Doug, or a
    Doug-length bar, under the dashed line so the 2x reads.
11. **s033 (director):** the "LONG BEFORE" arrow's tail pokes out of the right side of the label as a stray red
    stroke. Start the arrow below the label.
12. **s035, s062, s113, s245 (art director):** the `spray` glow disc behind each reveal silhouette shows as a grey
    noise circle. In s035 it bleeds over the sand. Reduce the density or radius, or drop it.
13. **s097-s110 (art director): Supernova gear.** The straw hat sits on top of the red cap, and the scuba
    mask/sunglasses plus the cage top bar cover most of the white head, so Doug's on-model read (red cap, white head)
    is lost. Drop the straw hat or seat it so the cap brim shows, and raise Doug so his face clears the top bar.
    s108's pink/red-limbed Doug is acceptable as a radiation gag, but confirm it is intentional.
14. **s172 (illustrator):** the plankton under the red X is a tiny unreadable circle. Use the s206 green plankton
    dots, or a labelled "PLANKTON" foram, at 3x size.
15. **s028, s077, s234, s237 (director): text overlaps art.**
    - "PLENTY TO EAT" sits on the seagrass (s028).
    - "THE SMALL ONE" sits on the ichthyosaur's fins (s077).
    - "WHERE PUPS WERE BORN" runs into the tree canopy (s234).
    - "PUPS GREW UP HERE" covers the sun (s237).

    Nudge each label into clear space.
16. **s148 and s149 (director):** the denticle triangles spill past the right edge of the board. Clip them to the
    board.
17. **s200 and s201 (director):** the Beringia map has no "SIBERIA" or "ALASKA" labels, so the land bridge is hard to
    parse. The mammoth in s201 is a brown speck; scale it up about 2x.
18. **s303 (director):** the cause of death (snapped rope) is a tiny kink. Make the break obvious, with a frayed end
    and a falling arrow on the cage, so "Doug has died. Again." has a visible cause.
19. **endslate (director):** "DOUG'S NEXT DEATH" starts about 10 px from the left edge. Move it inside title-safe
    (x >= 96).
20. **s230 and s231 (editor):** the contact-sheet captions render "Gatún" and "Colón" with missing glyphs. The
    on-screen labels are fine. Confirm the burned-in subtitle font has ú and ó before the final render.

Advisory: in most cage shots Doug is at scale 0.33-0.5 behind bars, so only the red cap reads at small sizes. That is
acceptable at 1080p, but where the beat is about Doug (s005, s016, s076, s260), use a cage scale of 0.9 or bring Doug
out of the cage.

### THUMBNAIL A (`thumbnail.png`, "SPOILER: NO"): VERDICT: PASS

At 168x94, "SPOILER: NO" is readable, the megalodon head is the single clear focal point and the cage reads. It
answers the title's question honestly: megalodon fails 7 of 11 stops and is extinct. The art is menacing, with the
mouth closed. Non-blocking suggestions for the graphic designer:
- At feed size Doug is only a red cap speck behind the bars. Scale the cage about 1.3x, or lower the middle bar so
  his face shows.
- Only two fragments of the half-drawn red X show, and they read as stray red slashes. Either reveal more of one
  stroke so the X shape is legible, or drop it.

### THUMBNAIL B (`thumbnail_b.png`, "NEWBORN"): VERDICT: PASS

This is the strongest read at 168x94: one big shark, a screaming Doug on the cage (fully on-model), and one bold word.
It is not misleading, because the video opens on the 4 m newborn (s001-s024). The weakness is that it speaks to the
hook rather than the "every era" title. That makes it a fair A/B variant, but A complements the title better.

### THUMBNAIL C (`thumbnail_c.png`, 2x3 verdict grid): VERDICT: FAIL

Fixes for the graphic designer:
1. **No single focal point.** There are six equal tiles, and at 168x94 none of them dominates. Doug is a 6 px figure
   in one tile, so "Doug + threat obvious" fails. Make one tile hero-sized, e.g. the Orcas X tile at 2x with Doug in
   the cage, or put a large Doug/cage overlay across the grid.
2. **The X badges are much weaker than the check badges.** A thin red X on white nearly vanishes at feed size (it
   reads pink). Match the check style: a solid red disc with a thick white X, at the same size and stroke as the
   green check.
3. **Tile labels are in a different handwritten font** from the channel's bold sans with black outline (the art
   bible thumbnail type), and they are about 7 px tall at feed size. Use the channel font, bigger, or drop the
   labels. The pictures carry the meaning.
4. **The brief asked for a 3x3 grid of the non-boss stops.** This is a 2x3 grid that omits the Ichthyosaur, Rival,
   Hothouse and Canal. That is acceptable for readability, but the Supernova tile shows no megalodon, and the Ice
   Age and Trench tiles show Doug and a tooth. Put the shark (or its silhouette) in every tile so the check/X clearly
   refers to the megalodon.

### Summary
- Keyframes: **FAIL.** There are 9 blocking fixes (s010 double Doug; title-card/cage collisions in 9 chapter
  openers; the mosasaur silhouette; the s054 direction; repetition runs, worst s278-s288; s252; s207/s208; s008; the
  school bus asset) and 11 polish items.
- Thumbnail A: **PASS** (optional tweaks).
- Thumbnail B: **PASS.**
- Thumbnail C: **FAIL** (no focal point, weak X badges, off-style labels).

## Round 2 (2026-10-27): re-check of keyframes + thumbnails

Scope: all 26 contact sheets (re-rendered 08:09, after commit 89306e5), `build/thumbnail.png`, `thumbnail_b.png` and
`thumbnail_c.png` (rendered 08:03, after the cb9f6e0 thumbnail JSON changes), and their 168x94 `_small` versions. I
zoomed into the full-res keyframes for s030, s035, s036, s113, s125, s232, s245, s252, s303 and s309.

Policy: still PASS. No gore, cartoon deaths only (ghost float, ice block, falling cage), nothing nursery-toned. The
HUD runs 226 -> 234 and 0/11 -> 4/11 consistently.

### Round-1 blocking fixes
| # | Item | Verdict | Notes |
|---|---|---|---|
| 1 | s010 double Doug | **PASS** | There is one Doug, in the cage. The booth on the bank is empty. |
| 2 | Chapter cards vs cage (s004, s031, s060, s085, s111, s138, s166, s194, s218, s244, s272) | **PASS** | All 11 openers are clean. The cage is at the left (s218/s272 at the right, s085/s194 on the surface or bank), and every title and sub-label sits on clear background. |
| 3 | Mosasaur silhouette | **PASS** | s030/s031/s034/s035 now show a long, tapered, toothed jaw, and the silhouette matches the s036 colour drawing. It is clearly different from the blunt Livyatan silhouette in s113/s117, and the two read as different animals side by side in s309. |
| 4 | s054 direction | **PASS** | The snout points up and the arrow leads from the snout to the surface. |
| 5 | Repetition runs | **PASS** | No run is longer than 3. s018 and s021/s022 break s017-s020. s073/s078 break s072-s075. s146/s149 break the Orcas boards. s206/s207 break the Ice Age run. The Supernova gets s099/s101/s102/s103/s108. The Hothouse gets s182/s184. s278-s288 now goes board, board, s280/s281 lab, board, s283 rock strata, board, board, s286 timeline walk, board, s288 Doug + rock. |
| 6 | s252 Burj stack | **PASS** | It has a base, an "x6" and a "BURJ KHALIFA" label, and the top tower clears the HUD band. |
| 7 | s207/s208 patches | **PASS** | Solid green clumps, readable at a glance. |
| 8 | s008 board covering the shark | **PASS** | The board is above-left and "ONE VERDICT" sits in clear water. |
| 9 | School bus asset | **PASS** | s049, s071 and s156 use a white/red `city_bus` with a "42 CITY" route sign. |

### Round-1 polish items
- 10 s024 (DOUG bars): PASS. 11 s033 arrow: PASS. 14 s172 plankton (shell under the X): PASS. 15 s028/s077/s234/s237
  labels: PASS. 16 s148/s149 denticles clipped: PASS. 17 s200/s201 (SIBERIA/ALASKA labels, mammoth 2x): PASS.
  13 Supernova gear: PASS. Doug stands on the cage with the cap brim and white head readable, and the straw hat
  is acceptable. s108 is confirmed as an intentional sunburn gag.
- 18 s303: PASS (marginal). The empty cage drops with a red down-arrow and the cap is left on the cage roof, so the
  cause reads. The frayed end is only a small fork just above the hook. A wider gap between the frayed rope end and the
  cage hook would make the snap obvious (director, optional).
- 19 endslate: PASS. "DOUG'S NEXT DEATH" now starts at about x 126, inside title-safe.
- 12 glow discs: PARTIAL, not blocking. s245 (and faintly s113) still show a dark speckled disc behind the silhouette.
  On these dark backgrounds it reads as murk, not as a grey noise circle, and nothing bleeds onto the sand any more.
  Optional: drop the spray (art director).
- 20 accented glyphs: still OPEN, for the editor. The contact strip shows "Gat?n"/"Col?n" in s230/s231, while the
  on-screen labels "GATÚN FORMATION" and "NEAR COLÓN" render correctly. Check this against the burned-in subtitle font
  at the final render, before post-render review.

There are no new defects. I checked text against the HUD (s086, s125, s232), cropping, stray strokes and on-model
Doug on all 310 tiles.

### KEYFRAMES: VERDICT: PASS
All 9 blocking fixes are verified. The open items (s303 snap emphasis, the s245 glow, the subtitle glyphs) are
non-blocking and routed above.

### THUMBNAIL A (`thumbnail.png`, "SPOILER: NO"): VERDICT: PASS
Both round-1 suggestions are done. The stray half-X is gone, and Doug is bigger with his face clear of the bars,
so the 168x94 version reads as megalodon eye + scared Doug in a cage + "SPOILER: NO". It has one focal point,
complements the title and is honest (megalodon fails 7 of 11 stops).

### THUMBNAIL B (`thumbnail_b.png`, "NEWBORN"): VERDICT: PASS
Unchanged from round 1. It has the strongest single-subject read, and Doug is on the cage roof, fully on-model. It
is still a hook-led A/B variant rather than an "every era" read.

### THUMBNAIL C (`thumbnail_c.png`, verdict grid): VERDICT: PASS
All four round-1 fails are fixed.
1. There is now a hero tile (Orcas, about two-thirds of the frame) with a big, scared Doug in the cage, the
   megalodon and two orcas. At 168x94 this is the clear focal point.
2. The X and check badges are matched solid discs with thick white marks, and they read red/green at feed size.
3. Labels use the channel's bold sans with a black outline.
4. Every tile shows the megalodon, so each badge clearly refers to it.

Nit (optional, graphic designer): "NURSERY"/"ICE AGE" are about 8 px tall at feed size. The badges and pictures
carry the meaning, so this is fine.

### Summary (round 2)
- Keyframes: **PASS** (non-blocking: s303 snap emphasis for the director, the s245 glow for the art director, and the
  ú/ó subtitle glyphs for the editor).
- Thumbnail A: **PASS**. Thumbnail B: **PASS**. Thumbnail C: **PASS**.

## Round 3 (2026-10-27): Thumbnail B re-check after the scale fix (decisions.md items 17-21)
Scope: `build/thumbnail_b.png` and `build/thumbnail_b_small.png` (168x94) only. A and C are not re-checked.

### THUMBNAIL B (`thumbnail_b.png`, "NEWBORN"): VERDICT: PASS
1. **Scale (item 20.1): fixed.** Measured on the 1280x720 render: the pup runs from tail tip x 234 to nose x 881 (about
   647 px) and Doug runs from cap top y 23 to feet y 312 (about 289 px). That is **about 2.2x Doug's height**, inside the
   requested 2.0-2.3x and consistent with s024 "2x DOUG" and the script's "about twice as long as he is". The whole tail is
   in frame. The pup (about 647 px) is still clearly longer than the cage (about 232 px wide, 320 px tall).
2. **Feet on the roof (item 20.2): fixed.** The feet end at about y 312 on the roof bar (top about y 315), so he reads as
   standing on the cage. Arms up, shock face and sweat drop are kept. Doug is on-model (red cap, white head).
3. **Kept (item 20.3):** "NEWBORN" in the one bold font with a black outline, same colours, closed mouth, no blood.
4. **Feed size (168x94):** "NEWBORN" is the most legible element. Pup + cage + Doug on the roof read as one scene, and
   the red cap marks Doug at once. There is one focal line (text to pup to Doug). Nothing is cropped, and nothing overlaps
   the text.
- Nit (optional, graphic designer): at 168x94 Doug's face is only a few pixels and the panic comes mostly from the pose.
  That is acceptable for an A/B variant.

### Creative director proxy (scale point only)
Confirmed: the pup is about 2.2x Doug's standing height, the whole animal is visible and the image is honest to the video's
own claim. The blocking item 20.1 is cleared. B can join the test set with A (primary) and C. Final CD sign-off on the image
otherwise stands as in item 20.
