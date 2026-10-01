# Visual review: 003-every-mass-extinction

## Round 2: pre-render keyframes + thumbnail (2026-10-01)

Scope: all 249 keyframes in `build/contact/sheet_01..21.png`, re-checked against the narration in `shotlist.json`. I opened
full-size keyframes for s047, s103, s198 and s224. I checked `build/thumbnail.png`, `build/thumbnail_small.png` (320x180), and a
168x94 downscale for the feed-size test.

VERDICT: PASS

All 13 blocking fixes from round 1 have landed. No new blocking problems. The remaining items below are polish and do not block
the render.

### Round 1 fixes: verification
| # | Shot(s) | Status |
|---|---|---|
| 1 | s047, s071, s110, s152, s198, s220 death pose | Fixed. New `on_back` pose: Doug lies flat with X eyes, cap still reads as a cap, ghost above. Reads as "dead Doug" at contact-sheet size. |
| 2 | s130, s131 towel | Fixed. The towel sits on top of the cap, matching s132. |
| 3 | s024 "FREEZE A PLANET" | Fixed. The wordart is upper right, clear of the "good moss" bubble. |
| 4 | s196, s197 "BLEND IN" / "VERY SERIOUSLY" | Fixed. Moved right of Doug; the cap is clear. |
| 5 | s116 "BRUTAL" | Fixed. Moved above the thermometer; the conodont tooth is fully visible. |
| 6 | s224, s201 asteroid | Fixed. s201 uses the real asteroid drawing. s224 keeps the silhouette but now sits on a lighter navy sky with a flame trail, so it reads as an incoming rock (the alternative route from round 1). The reveal follows in s225. |
| 7 | s058 red X | Fixed. An "O2" label sits above the crossed-out bubbles. |
| 8 | s233 thermometer | Fixed. It is in clear sky, off the sauropod, with a blue down arrow for "cooled". |
| 9 | s150 Lystrosaurus | Fixed. Doug stands apart and offers the leaf; the animal faces away. Reads as "ignored". |
| 10 | s145 bubble and scientist | Fixed. The tail points to the scientist, who stands on a sand strip. |
| 11 | s049-s054 variety | Fixed. s051 is a globe with the reef belt, s053 is an O2 graph and s055 is a timeline. The reef backdrop no longer runs more than 2 shots in a row. |
| 12 | s101-s104 variety | Fixed. s103 is a close-up of the burning coal seam and s104 pulls back to the surface with gas plumes. |
| 13 | s001 thumbnail placeholder | Fixed. s001 now shows the 3x3 grid thumbnail. |

### Checks passed
- Death counter is correct throughout: 18, then 19 (s025), 20 (s047), 21 (s071, and holds at s091), 22 (s110), 23 (s132),
  24 (s152, and holds at s177), 25 (s198), 26 (s220), 27 (s246, s249).
- Doug is on-model in every shot (red cap, white head). The red sunburn in s089-s091 and the ghost in s249 are intended.
- No gore, no realistic violence, and no kids-show tone. No spelling errors found.
- No run of 4 or more near-identical compositions remains.

### Thumbnail
PASS. It is an Archetype A 3x3 labelled grid on white, matching the style bible. The 9 labels are the chapter names and none repeats a
word from the title "How Doug Would Die in Every Mass Extinction". At 320x180 every label is readable and every tile subject is
clear (moss, ice cap, angry sun, volcanoes, hot tub, rotten egg, rift, India + volcano, asteroid). At 168x94 the tile pictures
still read, but the labels blur.
- Optional (graphic designer): raise `label_size` from 42 to about 50 (shorten tile `h` to make room) so the labels survive at
  168x94. Gondwana Ice is the weakest tile (a green blob with a white patch); a darker outline on the ice cap would help.

### Polish still open from round 1 (non-blocking, director unless noted)
These were not changed. They are fine to ship, but fix them if the director does another pass:
1. s047: one flipper still stands upright, detached from Doug. Lay it flat by his feet.
2. Text crossing outlines. Nudge each 40-80 px clear: s027 "SUPERCONTINENT" over the globe top, s084 "NOWHERE TO HIDE" across
   the sea/fresh-water divider, s091 "MADE IT" on the ozone line, s140 "GREEN SULFUR BACTERIA" over the circle edge,
   s154 "PANGAEA SPLITS" with the rift through it, s155 "PANGAEA" over the map edge, s193 "DISAPPEARED" over the coastline,
   s211 "SHOOK THE PLANET" over the shock rings.
3. s210: stray "- - - -" dashes under the timeline. Remove them.
4. s098: the map is still cropped at left and bottom with a blue band above, and Siberia shows only a faint speckle.
   Frame the map fully and add a solid lava patch.
5. s228, s229: the four coloured bars have no labels. Add the extinction names.
6. s122 (illustrator, optional): the "chalky algae" are still plain circles with X's. A coccolith drawing would read better.

### Routing
- Director: optional polish items 1-5. Re-render only the touched shots.
- Graphic designer: optional thumbnail label size.
- Illustrator: optional s122.
- Next gate: art_approved. Post-render review (samples, qc.json, shorts) is due after `render --final`.

## Round 3: post-render (final.mp4, thumbnail, Shorts) (2026-10-01)

VERDICT: FAIL (the main video and thumbnail pass; the Shorts fail)

### Main video: PASS
- qc.json shows 0 problems, and the duration is 997.1 s. I checked all 33 samples, plus extra frames from 0-30 s and 930-997 s.
- No black or glitched frames, and no frozen shots. Doug is on-model throughout. The death counter reads 18 at the open and 27 at the end.
- f_033 (about 975 s) is a near-white frame. This is the intended impact flash at the start of s246 (white with yellow spray, about 2 s before
  the strata appear), so it is not a blank-frame fault.
- Sparse moments, non-blocking: f_009 (dead reefs, only a fish and Doug) and f_022 (Pangaea, a bare timeline line) are mid-reveal
  states. s247 shows a near-empty grey frame with a tiny Doug for about 2.5 s before the feathered dinosaur appears at 0.48. That last one is optional polish.
- Round 2 polish items are still open and still non-blocking.

### Thumbnail: PASS
- The 1280x720 3x3 grid is clean. All 9 labels are legible and none repeats a word from the title. Doug is in the Hot Tub tile.
- At 320x180 every label and tile reads. The bigger labels (round 2 note) survive at feed size, and the Gondwana ice cap now has a dark outline and reads as ice.
  It fits the title "How Doug Would Die in Every Mass Extinction" and is not misleading.

### Shorts: FAIL
Titles, subtitles, the @DoomedDoug handle and the end cards (the arrow points down to the link) are all fine in short01-03 and the previews.
The problem is the Shorts zoom-crop. Only x 260..1660 of the 1920 frame survives (studio/shorts.py, ZOOM 1.25). Several shots in the Short
ranges put content outside that band, so it is cut off at the sides.

Required fixes (director: composition; editor: re-render). The x values below are scene coordinates in shotlist.json.
1. s101, s102, s103 (short03): the right-hand label "COAL" shows as "COA". Move it from x 1700 to x 1560.
2. s103 (short03): the right-hand label "MAGMA" shows as "MAGI". Move it from x 1700 to x 1560. Also move Doug from x 1680 to x 1580 (his head is at the edge).
3. s233 (short01): the thermometer at x 1780, which carries the "cooled" beat, is lost in the Short. Move it to x 1540.
4. Doug is half cut at the right edge. Move him from x 1700/1750 to x 1600:
   - short01: s228, s229, s231, s232
   - short02: s112, s114, s115, s116, s117, s118 (s116: also move exclamation_mark from 1700 to 1600)
   - short03: s099
   In the 16:9 video the new positions still sit on the right third, so the composition is unchanged.
5. Then re-render the touched main-video shots plus `render --final`, and run `shorts render`. Re-check the Short frames.
   (Alternative if the main render must stay frozen: the editor adds a per-short x-shift/zoom override in shorts.py. Moving the elements is simpler.)

Non-blocking:
- short02_preview.png caption is caught mid-word ("exact temperature t"). Grab the preview at a caption boundary if that is easy.
- The s226/s227 and s098 world maps are deliberately oversized and cropped. Siberia and Mexico stay in frame, so this is OK.
- Decorative ferns at x 220/1750 in s233-s234 get cut. That is fine.

### Routing
- Director: fixes 1-4. Editor: fix 5 (re-render final + shorts). After that, I re-run the post-render check on the Shorts only.

## Round 4: Shorts re-check after the x fixes, plus a main-video spot check (2026-10-01)

VERDICT: FAIL (2 small fixes, both in the Shorts crop. The main video and thumbnail still pass.)

### Round 3 fixes: all verified in the fresh render
- short03, s100-s103: "COAL" (now x 1560) and "MAGMA" read in full. Doug (x 1580/1600) is whole in s099-s103.
- short01, s233: the thermometer (now x 1540) is fully in frame and carries the "cooled" beat. Doug is whole in s228, s229, s231 and s232.
- short02, s112-s118: Doug is whole, and the "40°C" and "LAND: 50-60°C" labels are fully in frame. The s116 exclamation mark is in frame.
- Titles, subtitles, the @DoomedDoug handle and the end cards (the arrow points down to the link) are fine in all three Shorts. Durations are 45.3 s, 24.1 s and 32.8 s.

### Main video: PASS (spot check)
- qc.json shows 0 problems, and the duration is 997.1 s. In the 33 samples, the moved elements (COAL/MAGMA, thermometer, Doug at x 1600) look natural in 16:9.
  No new crops or overlaps, and no black or frozen frames. f_033 is still the intended s246 impact flash.

### Editor's question, s229 calendar: yes, it is a real problem
In short01 at about 10 s, on the line "...on a single day.", the calendar (x 1650, scale 0.7, about 1505-1795 in scene coordinates) is cut
roughly in half at the right edge. The "Y" of the "1 DAY" label touches the frame edge. This is the visual payoff of the Short's thesis
(blast day vs. thousands of years), and a half-cut drawing on that beat looks like a framing mistake. The "SINGLE DAY" wordart softens it but does not cover it.

### Required fixes (director: composition; editor: re-render)
1. s229 (short01): move the `calendar` asset and the "1 DAY" label from (1650, 450) to (1360, 870). That puts them bottom-right, right of the "SINGLE DAY" wordart
   and left of Doug at x 1600, inside 260-1660. Keep appear 0.73. Check that "SINGLE DAY" (x 850, size 100) does not touch the calendar. If it does, move the wordart to x 760.
2. s120 (short02): the control panel runs to x 1740, and the red-X "off" button (x 1640, r 50) has its X clipped at the right edge on "no button to turn it down".
   Shift the whole panel group 90-120 px left:
   - rect x 1300 to x 1220, w 440 to w 400
   - dial circle, needle line and "MAX" label x 1420 to x 1330 (shift the needle points by -90)
   - button circle and `red_x` x 1640 to x 1520
3. Editor: re-render s120 and s229, then run `render --final` and `shorts render`. I will re-check short01 at about 10 s and short02 at about 19 s only.

### Non-blocking
- s098 (short03 hook): Doug at x 260 is fully visible but sits flush on the left crop edge. x 330 would give some breathing room. Optional.
- short01_preview: the "A FEW HOURS" label is flush against the right edge but fully readable. Optional nudge left by 40 px.
- short02_preview caption is still caught mid-word ("exact temperature t"). Optional.
- s111 hook (short02): the rubber ring at x 1560 touches the right crop edge. Optional.
- Round 2 polish items are unchanged and still non-blocking.

### Routing
- Director: fixes 1-2. Editor: fix 3. Visual screener: a targeted Shorts re-check (round 5).

## Round 5: targeted Shorts re-check after the s229/s120 fixes, plus a main-video spot check (2026-10-01)

Render checked: final.mp4 and build/shorts/* from 11:27-11:28. Frames were pulled with ffmpeg: short01 at 9.6-10.6 s in 0.1 s steps, short02 at 17.5-20.5 s, and short03 at 2/12/22/31.5 s.

### Round 4 fixes: both verified
1. s229 (short01, about 10.0-10.5 s, "on a single day."): the calendar and the "1 DAY" label now sit at (1360, 870), fully inside the crop, with clear space
   on both sides. "SINGLE DAY" (x 850) does not touch the calendar, and Doug (x 1600) is whole beside it. In final.mp4 (about 908.6 s) the same layout reads well
   in 16:9: the calendar sits bottom-right under the bars, with no overlaps. Note: the calendar is on screen for only about 0.5 s (s229 is 1.79 s long, appear 0.73).
   That is short but readable, and it lands exactly on "single day". Not blocking.
2. s120 (short02, about 19-20 s, "no button to turn it off"): the panel (x 1220-1620) is fully in frame. The dial, the "MAX" label, the green button and the red X are all whole,
   with a margin on the right edge.

### Other checks
- short01 is 45.3 s, short02 is 24.1 s and short03 is 32.8 s. In all three, the titles are readable, the subtitles are legible, the @DoomedDoug handle is present and the
  end cards' arrows point down to the link.
- short03: the "COAL"/"MAGMA" labels are whole, Doug is whole in the hook (Siberia map) and in s100-s103, and the end card is fine.
- Main video: qc.json shows 0 problems, and the duration is 997.1 s. All 33 samples match round 4: no black or glitched frames, and no new crops.
  f_033 is still the intended s246 impact flash.
- thumbnail_small.png is unchanged from the approved design. The 3x3 grid still reads at feed size.

### Non-blocking (carried over, optional)
- s098: Doug is flush with the left crop edge. short01_preview: "A FEW HOURS" is flush right. short02_preview: the caption is caught mid-word. s111: the rubber ring touches the right edge.

VERDICT: PASS
