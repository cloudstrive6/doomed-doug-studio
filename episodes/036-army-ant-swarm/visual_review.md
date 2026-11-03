# 036-army-ant-swarm: visual review

## Round 1: keyframes (2026-11-03)

Screened: `build/contact/sheet_01..19.png` (s001 to s218 + endslate) and full-size keyframes s008, s012, s028,
s100, s117, s197.

VERDICT: FAIL

Overall the episode is in good shape. Doug is on-model in every shot (red cap, white head, readable on all of the
pale, dark-green, night and orange Africa backgrounds). The death counter runs cleanly from 280 to 287 (s026, s066,
s107, s129, s149, s169, s191) and matches the series bible (035 ended at 280). Chapter labels and title cards are
spelled correctly and nothing is cropped. There is no gore: the deaths are a ghost Doug, X eyes, or a costume in
a box. s100 (stick-figure road workers lying in potholes with traffic going over them) is clearly cartoon, the
workers are smiling, and it is fine. Nothing looks like a kids' show. s001 is the thumbnail placeholder, which is
expected at this stage.

It fails on two runs of near-identical compositions and three drawings that read wrong. Each of these is a
small fix.

### Required fixes

1. **s062-s065: four near-identical shots** (director). All four use the same mid shot: grasshopper-Doug at
   x 1100 in the carpet, and only the expression, the pencil hand and the thumbs-up change. Make s063 ("and for a
   while it goes well") a wide shot: Doug at scale 0.4 with the carpet filling the whole frame and flowing around
   him, plus a clock or sun-arc to show time passing. Alternatively, make s064 a tight close-up (camera zoom about
   1.6 on Doug's face, with the pencil hand entering frame). Keep s062 and s065 as they are.
2. **s103-s107: five near-identical shots** (director). Two logs, Doug `on_back` at (1000, 670), and the same
   framing all five times. Only s104 has a 1.08 zoom. Change s104 ("Doug volunteered.") to a hard close-up
   (zoom about 1.8 on Doug's hopeful face and cap). Change s106 (the sun going up and down) to a wide shot with
   Doug at scale 0.5, with the ant column running across him and out both sides of the frame, so the time-lapse
   reads as a different picture. Leave s103, s105 and s107.
3. **s117 and s118: the ant mill stands up like a wheel** (director, with the illustrator if needed).
   `army_ant_mill` is a top-down ring placed in a side-view scene, so it shows as an upright hoop half sunk into
   the dirt. A viewer won't read it as a ring of ants on the ground. Either:
   (a) the illustrator draws `army_ant_mill_side`, a flat ellipse about 4:1 that sits on the ground line, and the
   director swaps it in at (1260, 820); or
   (b) the director restages s117 and s118 on the top-down dirt background used in s109-s116, with the
   naturalist as a small inset or standing at the frame edge.
4. **s197: palm trees in "Greater New York"** (director). `city_skyline_small` is the Darwin skyline and includes
   palms, which is wrong for New York. Use `city_skyline_night` with a day tint if that is possible, or ask the
   illustrator for a palm-free skyline. In the same shot, Doug (x 1790, scale 0.35) is standing on top of the last
   building. Move him clear of the skyline to x 1850 or so, or put him in front at ground level y about 1000 on the
   dirt band.
5. **s008: the swarm is a flat brown slab** (director). The polygon at (160..1790, 440..790) doesn't read as ants.
   It reads as a wall or a board, and the bus overlaps its bottom edge. Fill the same 15 m+ span with
   `army_ant_carpet` tiles, as in s006 and s007, and put the bus *beside* or *below* it with no overlap, so that
   "wider than a bus is long" works as a side-by-side comparison.

### Recommended (not blocking)

6. **s119 and s120 are the same picture** (director). In s120 ("almost one full lap"), make the red ellipse a
   ~90% arc that stops short of closing, or add a small gap marker, so the second shot adds information.
7. **s122-s125 and s127-s130: two runs of circle-centre compositions** (director). s125 ("Here is the disturbing
   part") is just the bare ring and Doug. Give it a slow zoom_in on the ring (1.3) so it feels like a beat rather
   than filler.
8. **Distance tracker format changes at s029** (director). It reads "ABOUT 200 M" in s001-s028 and then "200 M"
   from s029, so the label width jumps. Use one format all the way through.
9. **s053 and s054: "nestling birds" is drawn as a nest of eggs** (illustrator/director). Use chicks in the nest
   (or add a beak and head to two of the eggs) so the picture matches what is said.
10. **s169 and s170: ghost Doug is wearing the cap** while the cap is stuck on, or lying under, the bivouac (s170
    shows the cap on the ground). Drop the cap from the ghost in s169 and s170 if the rig allows it (art director),
    or accept it as the standard ghost.
11. **s184: the red X covers the "O" in "VOTE"**. Shrink the X slightly or move it, so the word reads fully
    before it is crossed out (director).

### Re-screen needed
s008, s062-s065, s103-s107, s117, s118, s197 (re-render keyframes with `--shots`). Post-render checks (samples,
thumbnails, Shorts) are still to come.

## Round 2: keyframes after the director's fixes (2026-11-03)

Screened: all of `build/contact/sheet_01..19.png` (s001 to s218 + endslate; the sheets are newer than the shotlist),
plus full-size keyframes s031, s179 and s184. Note that `studio keyframes` ignores `camera` on 1920x1080 canvases,
so the sheet tiles show the unzoomed picture. I simulated the camera moves of s063, s104, s125 and s180 with
`camera_rect` to check the zoomed frames.

VERDICT: FAIL (one required fix, s184)

### Round 1 items, re-checked
- **s008** fixed. Carpet tiles now span the width, the bus sits below with no overlap, and "15 M+" is over the swarm.
  The side-by-side comparison reads.
- **s053-s054** fixed. The nest now holds chicks with beaks.
- **s062-s065** fixed. s063 pushes in to 1.35 with a sun arc ("GOES WELL"), and s064 is now a wide shot with the
  pencil hand. The run is broken.
- **s103-s107** fixed. s104 has a 1.8 close-up on Doug's face plus "VOLUNTEERED" (the death counter drops out of
  frame for this one shot, which is fine), and s106 is a wide time-lapse with the column running out both sides.
- **s117-s118** fixed. They are restaged top-down on the dirt card, with Beebe at the frame edge and a tape measure
  in s118. The mill now reads as a ring on the ground.
- **s119-s120** fixed. s120 has an open ~90% red arc with a gap marker and "ALMOST 1 LAP".
- **s125** fixed. It zooms in to 1.35 on the ring, and neither the ring nor Doug is cropped at the end frame.
- **s169-s170** fixed. The ghost is capless and the cap lies on the ground in s170, so there is one cap per frame.
- **s197** fixed. The skyline is Empire State plus library buildings with no palms, and Doug stands clear at ground
  level.
- **Distance tracker** fixed. It uses one format ("DISTANCE TO QUEEN: 200 M") from s002 onwards.
- **s031, s173, s176-s178** have no issues. The Rettenmeyers, the paper stack and the calendar read as "decades of
  cataloguing". The egg piles, the 1-WEEK calendar, the AGAIN calendars and the marked queen (blue dot plus arrow)
  all match the narration.
- **Regression scan:** no regressions found. Doug is on-model throughout. The counter runs 280 to 287 on the death
  beats. There is no gore and no kids-show tone, and no text is cropped or overlapping.

### Required fix
1. **s184: the ballot reads as a vote cast** (director). The narration is "doesn't get a vote", but the picture
   shows a ballot card labelled VOTE with a red X neatly inside the mark area. In the UK, NZ and AU, that is exactly
   how a completed ballot looks, so it says the opposite of the line. Remove the small X inside the card. Then do
   one of these:
   (a) draw a red prohibition sign (circle plus slash, width ~14) centred on the card at about (1410, 650) with r
   ~200, so it covers the whole card; or
   (b) draw one large red X corner to corner across the entire card, overshooting its edges by ~30 px.
   Optionally add a red arrow from the queen to the card, ending short of it, so the "no" is clearly hers.

### Recommended (not blocking)
2. **s179: the "split in two" isn't drawn** (director). The beige dashed ^ in the dirt under the three queens doesn't
   read as anything. Replace it with a fork: one short arrow from centre-bottom that splits into two red arrows going
   left and right (or a vertical dashed divider at x 960 with the queens split across it), so "splits in two" is
   visible.
3. **s180: unclear which queen "makes it"** (director). At the 1.4 end zoom, two identical queens sit side by side
   and the red arrow starts in empty space to the right of them, so the eye can't tell who wins. Start the arrow at
   the rightmost queen's head and end it at the NEW NEST label (or a small nest drawing under it), and/or give the
   winning queen a red ring.
4. **s106: the sun phases are four loose coloured discs** (director). They read a little like balls. Connect them
   with a dashed red arc (as in s063), or give the yellow ones rays, so it reads as one sun moving over time.

### Next
Re-render s184 (and s179/s180 if changed) with `--shots`. After that, keyframes pass. Post-render checks (samples,
qc.json, three thumbnails, Shorts) are still to come.
