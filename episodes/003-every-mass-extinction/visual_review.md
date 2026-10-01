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
