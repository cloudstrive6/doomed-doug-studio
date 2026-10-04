# Visual review: 006-disturbing-deep-sea-discoveries

## Round 1: pre-render keyframes (2026-10-04)

Scope: all 24 contact sheets (s001 to s278), plus full-size keyframes for s018, s025, s038, s041, s063, s065, s092,
s097, s112, s113, s117, s136, s163, s180, s213, s240 and s256. s001 is the thumbnail placeholder; I ignored it as instructed.

### What passes
- **Doug:** on-model everywhere I checked (red cap, white head, snorkel and fins gear consistent). Ghost Doug and the
  dead/flat poses keep the cap, so he always reads.
- **Death counter:** 46, then 47 (s024), 48 (s069), 49 (s091), 50 (s115), 51 (s138), 52 (s161), 53 (s182), 54 (s205),
  55 (s244), 56 (s271). In order, with no skips.
- **Policy:** every death is cartoon only. X-eyes, ghost floats up, cap left behind, RIP headstone. No blood, organs or
  dismemberment. s092, s161, s205 and s271 show a lying body with all limbs attached. Nothing reads as a kids' show:
  animals have no cute faces, the humour is dry, and the speech bubbles are deadpan.
- **Text:** the caption bars, WordArt and labels are spelled right, and nothing is cropped at the frame edge. The depth
  meter is back on s061 and s068, and the surface iceberg beats now read 0 M.
- **Drawings:** recognisable on the whole (hammerhead, pufferfish, squid silhouette, scaly-foot snail, black smoker,
  submersible, inverted Empire State Building and inverted Everest as depth comparisons). Earlier art-review fixes (s149,
  s191, s251, s089) are confirmed in the renders.

### Required fixes (blocking)
1. **s038 (illustrator):** the crossed-out black silhouette (the "alien mystery") is an unreadable bell/blob shape.
   Nobody will see "alien" or "UFO" in it in 1 second. Replace it with a clear flying-saucer silhouette (dome plus disc
   rim plus a short beam) or a grey alien head with big almond eyes, then keep the red X.
2. **s213 (illustrator, then director):** the three "egg case / sponge" guess silhouettes are pure black (#000) on
   abyss navy (#050a1f), so they are nearly invisible and none of them can be identified.
   - Fill them mid-grey (about #5a6070) with a thin light outline, or give them the red guess-glow used in s014 and s032.
   - Make one shape a clear skate egg case (a rectangle with curled corner horns) and one a clear vase sponge.
   - Drop the third shape or make it obvious.
3. **s240 (director / art director):** Doug's body is drawn in white on the cream (#f4ecd8) lab background, so only
   his head and cap show. He looks like a floating head. The element sets `"ink": "#000000"`, but the render ignores
   it. Get the black ink to apply (or render Doug with the dark-background-off line colour, as he appears in
   s149/s214/s259). Also offset him a few px so the divider line does not run straight through his spine, unless the
   "on the fence" gag is wanted, in which case keep it with black ink.
4. **s112 (director):** Doug stands on top of the "~900 M" depth label. His legs disappear behind it and the label box
   cuts him off at the knees. Move Doug to x≈1650, y≈850 (right of the chart, under the red "?"), or anywhere clear of
   the meter column (x < 360).
5. **s018 (director):** the scientist's speech-bubble tail is a long double needle that enters the bubble and runs
   across "LIVE HERE", with a stray tick mark inside the bubble. Shorten the tail so it stops at the bubble edge, and
   anchor it toward the scientist's mask (≈1530, 330) without crossing the text. The same needle-tail habit is milder
   in s113 (crosses the fishing rod) and s180 (points into empty space up-left of Doug, not at his mouth). Re-aim
   both at Doug's head.
6. **s119–s125 (director): variety.** That is seven near-identical frames in a row: the same brine pool, same scale,
   bottom centre, dark navy, with only labels changing. s128–s132 repeats it five more times, with the pool sliding left
   and right. Break the run with at least two compositions:
   - s121 Cordes close-up: a waist-up scientist with the 2014 label and no pool.
   - s124 a macro cross-section: the pool as a heavy layer under seawater, salt particles sinking.
   - s129 a close-up of the warning sign and the gas plume over the pool surface.

### Recommended fixes (non-blocking, do them if time allows)
7. **s064, s065 (director):** Doug, the thermometer and the goldfish float inside the solid rock walls of the
   blue-hole cross-section. Doug reads as buried in rock. Put Doug on the surface (as in s063) or inside the shaft.
   For "LIKE THE CARIBBEAN", the generic goldfish says nothing. Swap it for a small Caribbean map inset with an arrow
   to the hole, or a "CARIBBEAN SEA" sign, and keep the thermometer.
8. **s117 (director):** the chapter WordArt "THE JACUZZI OF DESPAIR" starts flush against the depth meter (the T
   touches it at x≈255). Shrink it to about 90 px, or recentre it at x≈1060, so there is at least 40 px clear of the
   meter. s140 ("THE CHAMPAGNE VENT") is also tight against the meter and crossed by bubble columns. Nudge it right
   or drop the leftmost column behind it.
9. **s256 (director):** the "9,533 M" label sits on top of the left tubeworm cluster (only the red tips poke out), and
   a loose red marker triangle floats beside it. Move the label up to y≈880, left of the Everest tip, so it clears
   the worms, and delete the orphan triangle (or attach it to the tip).
10. **s163, s072, s076, s077, s078, s085, s088, s217 (director):** WordArt crosses drawings. Examples: "SNAIL" runs
    through the black-smoker plume in s163, "LOST CITY"/"PALE TOWERS"/"FIRST LIFE?" through chimney tops, "ANEMONE" and
    the 2 m dashed line through the tentacles in s217. All of it stays legible thanks to the outline, but shift the
    text into open water (usually 60–120 px up or sideways) so the key drawing is clean.
11. **s219–s222 (director):** four near-identical orb-on-rock frames (Doug left, orb centre). The gag continuity
    justifies some of it, but make s221 ("Doug is fine.") a tight two-shot of Doug and the orb, or a push-in camera,
    to break the run.
12. **s273–s278 (director):** six consecutive TV-monitor frames. The progression (cap drifts in, clam closes, heart)
    works as the payoff, but push in on s275 and s276: crop to the clam filling about 60% of the monitor so the
    "clam closes on it" beat reads at phone size.
13. **s125 (director):** the lone red X at the right has no referent. Either attach it to a "MIXING" label or a
    swirl icon ("without mixing"), or remove it. The same applies to the "?"-behind-X in s218 and s222: label it
    (for example, "EGG? SPONGE?") or drop it.

### Routing summary
- **Illustrator:** 1, 2
- **Director:** 2 (layout), 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13
- **Art director:** 3 (Doug ink colour on light backgrounds)
- **Graphic designer:** none this round (thumbnail pending)

VERDICT: FAIL. Fix shots s038, s213, s240, s112, s018 and the s119–s125 / s128–s132 variety run, then re-render those
keyframes for round 2.

## Round 2: keyframe re-check (2026-10-04)

Scope: every Round 1 item, checked against the current `build/keyframes` (all rendered 21:37, after the last shotlist
save, so they match commit 93b413c). I viewed these full size: s018, s038, s072, s085, s088, s112, s113, s117, s129,
s131, s140, s180, s213, s240, s256 and s275. I checked s117–s140, s063–s065, s163, s215–s226 and s270–s278 on
montages, plus every other shot changed in 93b413c (s022, s039, s137, s158, s212, s216, s238, s242, s269). Read-only:
I edited nothing and re-rendered nothing.

### Round 1 items
1. **s038: FIXED.** A grey alien head with almond eyes under a red X reads as "alien" at a glance.
2. **s213: FIXED.** The skate egg case (brown pouch with curled horns) and the vase sponge are in colour with a soft
   glow, labelled "EGG CASE?" and "SPONGE?". Both are clearly visible on the abyss navy. The third shape is gone.
3. **s240: FIXED.** Doug now draws in black ink on the cream background, so his whole body reads. He stands right of
   the divider, which no longer runs through him. (s240 itself is unchanged in the shotlist, so the fix came from the
   engine side; s214 and s238 also render correctly.)
4. **s112: FIXED.** Doug sits at the right, under the red "?", clear of the depth meter.
5. **s018 / s113 / s180: FIXED.** The tails are short and stop at the bubble edge. They aim at the scientist's mask
   (s018) and at Doug's head (s113, s180). They no longer cross text or the fishing rod, and the stray tick is gone.
6. **s119–s132 variety: FIXED.** The run is now broken by s121 (a waist-up Cordes with the 2014 calendar), s124 (the
   SEA vs POOL salt jars), s125 (the seawater-over-brine cross-section), s126/s127 (pit sections with the bus), s129
   (a push-in on the warning sign and gas plume) and s131 (a push-in on warmth with the crab). No run of 4 or more
   near-identical frames is left.
7. **s064 / s065: FIXED.** Doug is inside the shaft, and s065 has a Caribbean map inset with an arrow plus the
   thermometer.
8. **s117: FIXED.** The WordArt is recentred and clear of the meter. **s140: NOT FIXED.** The middle and right bubble
   columns still run through "CHAMPAGNE" and "VENT". It is still legible (non-blocking, carried over as R2-3).
9. **s256: FIXED.** "9,533 M" sits left of the tip, clear of the worms. The red triangle is now a flag on a stub under
   the inverted summit, so it reads as attached.
10. **WordArt over drawings: FIXED.** It moved into open water or onto the seabed band in s072, s076, s077, s078,
    s085, s088, s163 and s217.
11. **s221: FIXED.** It is now a tight two-shot of Doug and the orb, which breaks the s219–s222 run.
12. **s275 / s276: FIXED.** They push in so the clam fills the monitor, and the red cap is visibly caught in the shell.
13. **s125 / s218 / s222: FIXED.** The X now sits on a swirl icon labelled "MIXING". s218 has a struck-through
    "EGG? SPONGE?", and s222 has "2 YEARS" over a struck-through "MYSTERY".

Policy and Doug: no new gore or kid-appeal issues. The death counter is unchanged and in order (56 at s271–s278).
Doug is on-model in every changed shot.

### New findings
**Blocking**
- **R2-1. s088 (director):** Doug is placed exactly on the leftmost Lost City chimney (x≈410, y≈450–620). His white
  stick body and arms vanish into the white carbonate, so only his head, cap and fins show. He reads as a head
  impaled on the spire, the same "floating head" problem that made s240 blocking in Round 1. Move Doug into open
  water clear of every chimney, for example x≈1180, y≈520 (between the centre and fourth chimneys, as in s072), or
  x≈500 if he must stay left. Keep the scientist where he is, but nudge him about 40 px left so he no longer touches
  the right-hand chimney.

**Recommended (non-blocking)**
- **R2-2. s112 (director / art director):** the two "upsweep" traces are pale yellow (about #fff080) on the white
  chart panel, so they are barely visible at phone size. Recolour them to a dark ink (black, or orange #e07a00) at
  their current width.
- **R2-3. s140 (director):** this is Round 1 item 8, carried over. Shift the middle and right bubble columns about
  120 px so they clear the WordArt, or start them below y≈340.
- **R2-4. s085 (director):** the "120,000 YEARS" label sits on the tip of the fourth chimney. Raise it to y≈150, or
  move it right of the clock, so the tip shows.

### Routing summary
- **Director:** R2-1 (blocking), R2-2, R2-3, R2-4
- **Art director:** R2-2 (trace colour, if it is a style default)
- **Illustrator / graphic designer:** none

VERDICT: FAIL. Fix shot s088 (R2-1: move Doug off the chimney), then re-render the s088 keyframe. Every Round 1
blocking item (s018, s038, s112, s213, s240, s119–s132) is resolved. Once s088 is fixed, this round passes without
needing another full sheet review.

Round 2 note (showrunner): s088 fixed by art director before the screener render (Doug now x=515, readable); screener R2-1 resolved. Both gates effectively PASS.

## Thumbnail

I checked `build/thumbnail.png` (1280x720) and `build/thumbnail_small.png` (320x180) against the `thumbnail_brief`
and title in `metadata.json` ("The Most Disturbing Discoveries at Every Depth of the Ocean").

**Readability at feed size (320x180):** all nine labels are legible and spelled correctly: Sharkcano, Crop Circle,
Blue Hole, Lost City, Brine Lake, Iron Snail, Tar Volcano, Golden Orb, 9,533 m. None is cropped or overlaps a
drawing. The turquoise-to-black progression reads at once as "going deeper", which fits the title's depth frame. No
label uses a title or alternate-title word. The strongest tiles at small size are Sharkcano, Crop Circle, Lost City,
Brine Lake, Golden Orb and the 9,533 m boss tile.

**Accuracy / not misleading:** every tile maps to a segment in the shotlist (blue hole, scaly-foot "iron snail",
asphalt "tar volcano", golden orb, pufferfish crop circle, brine pool, Lost City, hadal tubeworms). There are no real
photos, no Titan or tragedy imagery and no shark attacks.

**Doug:** he is on-model (red cap, white head, stick body) in the Brine Lake tile and clearly readable at full size. At
320 px he shrinks to a red-and-white dot, but the brief asks for exactly that ("tiny"), so this is accepted.

**Policy:** no gore and no realistic violence. Doug smiling in a lethal brine "hot tub" lands as deadpan adult humour,
not nursery tone. The palette and framing are not kid-coded.

**Recommended (non-blocking)**
- **T-1. 9,533 m tile (graphic designer):** the dense red speckle around the tubeworms reads at 320 px as a red mist
  or spray on black, a faint blood-spatter impression next to the red plumes. Thin it out, or recolour it to dim
  grey/teal marine snow, so the red plumes stay the only red.
- **T-2. Tar Volcano tile (graphic designer):** the dark grey dome on navy has low contrast at feed size and reads as
  a dark hump. Lighten the dome's rim highlight, or add a small black plume or bubbles above the summit.
- **T-3. Blue Hole tile (graphic designer):** two sand blocks with a "?" are the weakest drawing. It is acceptable,
  but a darker, deeper gradient in the shaft would make "hole" read faster.

VERDICT: PASS. The thumbnail is readable at feed size, error-free, matches the brief and title, and carries no gore
or kid-appeal risk. T-1 to T-3 are optional polish.

## Post-render review, round 1 (final.mp4, thumbnail, Shorts)

What I checked: all 35 `build/samples/*.png` frames, plus `build/qc.json` (no problems, 1037.8 s). I also pulled
extra frames from `build/final.mp4` around s014, s068, s098, s102 and s144, and checked `build/thumbnail.png` /
`thumbnail_small.png` against `metadata.json`. For the Shorts I looked at `build/shorts/short0{1,2,3}_preview.png`,
a frame every 2 s from each `short0N.mp4` (1080x1920), and full-resolution crops of the edges. The Shorts show the
16:9 drawing zoomed 1.25x and centre-cropped (`studio/shorts.py`), so only about x 192-1728 of the 1920 frame
survives. The safe zone is x 260-1660.

### Main video: OK
- I found no black, blank-by-error or frozen sample frames and no glitches. Titles and labels are spelled correctly
  and readable. The depth meter climbs steadily (~20 M to 9,533 M). The DOUG DEATHS counter reaches 56 in the
  outro, and the Shorts run 48, 50, 51 in order.
- Doug is on-model everywhere (red cap, white head). His deaths are cartoon deaths: only the cap comes back, X-eyes
  ghost, the cap preserved in the brine. There is no gore. The tone is deadpan adult, not kids-show.
- s014: the red-glow sharks are the style bible's silhouette reveal (paint.py, style bible 4.2), and they resolve
  into grey sharks within about 1 s. Accepted.

### Thumbnail: PASS (unchanged since its approval)
The 3x3 depth-ordered grid reads at 320x180 and fits the title. Optional notes T-1 to T-3 from the thumbnail round
still apply.

### Blocking fixes
1. **s065 (director), Short01**: the "LIKE THE CARIBBEAN" label at x 1530 reads "LIKE THE CARIBBEAI", and the
   Caribbean inset map panel is cut off at the right edge. This shows on the Short01 preview frame itself. Move the
   label to about x 1350 and shift the inset panel left so its right edge is at or below x 1640. Shrink the inset if
   it collides with the hole.
2. **s069, s070 (Short01), s115, s116 (Short02), s138, s139 (Short03) (director)**: the "DOUG DEATHS: 48/50/51"
   plate at x 1530 loses its right border, and the last digit touches the frame edge. The episode-005 round-3 rule
   is that the counter must sit fully inside the frame with a margin. Move the plate to x 1380 in all six shots.
3. **s116 (director), Short02**: Doug's ghost at x 1720 shows as a cut-off sliver at the right edge, which looks
   like a glitch. Move him to x 1540 or less, clear of the counter plate.
4. **s102 (director), main video and Short02 (about 6-8 s)**: for the first 2.3 s of this 4.8 s shot nothing is on
   screen except the dark-blue background and the depth meter. The giant squid and scientist appear at 0.471 and
   Doug at 0.706. In the Short this is a dead frame right after the hook. Set the scientist's `appear` to 0 so the
   frame is never empty, and keep the squid silhouette reveal at 0.471. Optionally bring Doug in at 0.3.

### Non-blocking (recommended)
5. **s066 (director), Short01**: the "OPEN OCEAN" label (x 1600) and the open-ocean blue column sit right at the
   edge, and the column is half cut. The narration is about the hole connecting to the open ocean. Move the label to
   about x 1450 and the column to about x 1500-1600.
6. **s099 (director), Short02 hook**: the "LOUDER" label (x 1600) and Doug (x 1680) touch the right edge. Move them
   to about x 1480 and x 1560. s108 (Doug x 1700) and s129 (Doug + snorkel x 1680) are whole but tight; x 1580 is
   safer.
7. **Short03, warmth shot (the crab entering at right, about 19 s) (director)**: the crab is cut off at the right
   edge. Move it to about x 1550.
8. **s068 (director)**: during the "down, and down, and down" pan, the depth meter is drawn in world space, so it
   scrolls off the bottom of the frame (sample f_009). Pin it in screen space, or leave it out of this shot.
9. **Map shots (s006, the Bloop maps, the 2003 asphalt map, the Golden Orb map, the 9,533 m trench map)
   (director)**: the depth meter is drawn over the left edge of the world map and covers part of it. Shift the map
   right, or shrink it to clear x 280.
10. **9,533 m plate (director)**: it reads "9,533 M" in the ROV shot at about 1005 s (sample f_034) but "~9,533 M" in the previous shots.
    Pick one.
11. **Engine (editor)**: in the Shorts the depth meter (x 190) sits on the crop edge, so its label loses its first
    character ("0 M" for "~900 M") during zooms. Also, `shorts.py` line 222 builds the preview subtitle with
    `[:40]`, which cuts words mid-way ("the water's t"). This only affects the preview, not the video.

After the fixes, re-render s065, s069, s070, s102, s115, s116, s138 and s139 into final.mp4 (s102 is the only
main-video change), re-render all three Shorts, and re-screen the Shorts.

VERDICT: FAIL

## Post-render review, round 2 (re-rendered final.mp4 and Shorts)

What I checked: `build/qc.json` (no problems, 1037.8 s). I pulled frames from the new `build/final.mp4` at s065,
s066, s069, s070, s102 (4 points across the shot), s115, s116, s138 and s139. For the Shorts I made a contact sheet
with a frame every 2 s from each re-rendered `short0{1,2,3}.mp4` (55.2 s, 57.1 s, 48.8 s), plus full-resolution
1080x1920 frames at every fixed shot.

### Round-1 blocking fixes: all verified
1. **s065 / Short01:** the "LIKE THE CARIBBEAN" label is complete, and the inset map sits fully inside the 9:16
   crop with a margin (main video right edge about x 1640). Fixed.
2. **Counter plates s069, s070 (48), s115, s116 (50), s138, s139 (51):** in all three Shorts the plate has all four
   borders and every digit, with clear space to the edge. In the main video the plate also reads cleanly. Fixed.
3. **s116 / Short02:** Doug's ghost is whole, at about x 945 of 1080, and clear of the counter plate. "THE MONSTER"
   is inside the frame. Fixed.
4. **s102:** the scientist is on screen from frame 0, Doug enters early, and the squid silhouette reveal still
   lands. There is no empty frame in the main video or in Short02 (about 6-8 s). Fixed.

### Round-1 recommendations: verified
- s066: the "OPEN OCEAN" label and the ocean column are now inside the Short01 crop.
- s099: "LOUDER" and Doug are whole in the Short02 hook. s108 and s129 are whole.
- Short03 warmth shot: the crab is whole and inside the frame.
- Items 8-11 (s068 meter scroll, meter over map edges, "~9,533 M" consistency, preview subtitle `[:40]`) are
  unchanged and stay non-blocking.

### Regressions
None found. Titles, subtitles, the @DoomedDoug watermark and the end cards (the arrow points down) are legible in
all three Shorts. Doug stays on-model, the deaths are cartoon only, and there is no gore. The counter runs
48 → 50 → 51 in order.

VERDICT: PASS

## Post-render review, round 2 (final.mp4 22:24, Shorts 22:27-22:28)

What I checked: the `shotlist.json` diff against round 1. Frames pulled from `build/final.mp4` at the
`build/timing.json` times for s065 (244.8), s066 (247.3), s068 (255.0), s069 (257.5), s070 (262.5), s099 (371.8),
s102 (376.6 / 377.3 / 378.5 / 380.8), s108 (398.5), s115 (422.3), s116 (424.0), s129 (469.5), s138 (502.5) and
s139 (eight frames from 503.5 to 506.0). One frame per second from each `short0N.mp4` (1080x1920), plus full-resolution
crops, and a denser pass on Short01 at 31.5-33.0 s. All 35 regenerated `build/samples/*.png` frames, and `build/qc.json`
(no problems, 1037.8 s, duration unchanged).

### Blocking fixes from round 1
1. **s065 Caribbean label/inset: FIXED.** In final.mp4 and in Short01 (about 32.0-32.5 s), "LIKE THE CARIBBEAN" reads
   in full and the inset panel and its thermometer sit fully inside the Short crop with margin.
2. **Counter plates s069, s070, s115, s116, s138, s139: FIXED in all three Shorts.** The "DOUG DEATHS: 48/50/51"
   plates are whole, with both borders and a margin, in Short01 (45-50 s), Short02 (51-53 s) and Short03 (40-44 s).
   **Regression in the main video, s139:** see new fix R1 below.
3. **s116 ghost sliver: FIXED.** At x 1540, Doug's X-eyes ghost and bubbles show whole in final.mp4 (424.0) and in
   Short02 (53 s). They are clear of the counter plate.
4. **s102 empty opening: FIXED.** The scientist is on screen from frame 1 (376.6 in the main video, 7 s in Short02),
   Doug enters at about 378.0, and the squid silhouette reveal is unchanged. The Short no longer has a dead frame
   after the hook. The first 1.4 s is still sparse (one small scientist at the lower left), but it is not empty.
   Accepted.

### New blocking issue (regression)
R1. **s139 (director), main video 505.0-506.0 s:** the counter plate's move to x 1380 combines with this shot's
   `zoom_in` (1.08 about 1000,760) and pushes the world-space plate up and left under the screen-space topic plate.
   For the last ~1 s of the shot, "THE JACUZZI OF DESPAIR" covers the top-left of "DOUG DEATHS: 51", and the "DOUG"
   letters are clipped. This did not happen at x 1530. Short03 is not affected, because the topic plate sits
   elsewhere there. Fix: in s139 only, move the "DOUG DEATHS: 51" plate down to y 230 and keep x 1380. With the zoom
   its top lands at about y 155, well clear of the topic plate (bottom at about y 82), and it stays inside the Short
   crop. The alternative is to drop the zoom on s139. Re-render s139 into final.mp4, then re-render Short03.

### Non-blocking items 5-11
5. s066 OPEN OCEAN: **addressed.** The label and blue column are whole in Short01 (36-37 s).
6. s099 / s108 / s129: **addressed.** The LOUDER label, Doug, and Doug with snorkel are all whole in the Shorts. New
   cosmetic note: at x 1480 the LOUDER plate now sits across the chart's right border line. Optionally use x 1560 and
   y 470 (beside the curve's end, outside the chart).
7. Short03 warmth crab (s131 at about 20 s): **not addressed.** The crab is still cut off at the right edge of the
   Short.
8. s068 depth meter scrolling off-frame: **not addressed** (255.0 s).
9. Map shots, meter over the left edge of the map: **not addressed.**
10. "~9,533 M" vs "9,533 M": **not addressed** (sample f_034 still reads "9,533 M").
11. Engine: Shorts depth-meter label clipped ("00 M" in Short03 at 44 s) and the preview subtitle `[:40]` cut:
    **not addressed.**
New optional item: s065's Caribbean inset appears at 0.882 and is on screen for only about 0.7 s, in both the main
video and Short01. If the director touches s065 again, `appear` 0.75 gives it about 1.4 s.

### Regression sweep
In the 35 samples I found no black, blank or frozen frames and no glitches. Doug is on-model throughout, and the
counter still reaches 56 in the outro. Thumbnail unchanged (22:06), still PASS. Shorts end cards are fine: the title
reads, the "WHAT HAPPENS NEXT? TAP BELOW" arrow points down, and subtitles are legible.

### Required before PASS
- R1 (s139 counter plate y 230), then re-render s139 into final.mp4 and re-render Short03. Re-screen only s139
  (503.4-506.0 s) and Short03 (40-44 s).

VERDICT: FAIL

## Post-render review, round 2 fix check (showrunner, after final.mp4 and Short03 re-render)
R1 (s139 counter hidden by title plate during the zoom) fixed: counter moved to y 230, x 1380. Checked frame at 505.6 s in
final.mp4 and Short03 at 42 s: counter plate whole, clear of the title plate and the caption. QC exit 0, no problems.
All blocking items from the round-2 screener are resolved; the rest are non-blocking.

VERDICT: PASS
