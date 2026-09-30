# Visual review: 002-every-parasite

## Round 1: keyframes (pre-render), 2026-09-30

Scope: `build/contact/sheet_01..21` (s002-s247; s001 thumbnail pending, not reviewed), with full-size checks of
`build/keyframes/s066, s087, s100, s148, s178, s179, s190, s216`.

VERDICT: FAIL

### Policy (brief section 8): clean
- **Gore:** none found. The four items to watch are all handled at diagram level:
  - Jewel wasp (s010/s011/s019/s020): arrows to the thorax and head, an egg on the outside, egg to larva icons. Nothing inside the roach.
  - Horsehair worm (s050, s060, s066): a dotted silhouette, then a floating cap and ghost Doug. No worm is drawn leaving the body.
  - Baylisascaris (s182-s186): dashed paths on a grey silhouette and head.
  - Naegleria (s225/s227): a dashed nose-to-nerve path on a head silhouette. No brain is drawn.
  - Deaths are X eyes, ghost Doug or a floating cap every time. The red blood cells are textbook discs.
- **Death-toll beats:** the Doug deaths and the real numbers are always in separate shots, and the numbers are shown
  straight: s127 then s128/s129, s148 then s149/s150, s169 then s171/s172, and the Naegleria stats (s233-s236) come well before the s243 death. s172
  ("3 IN 4: UNDER FIVE") is a plain map with no Doug gag.
- **Kid-appeal:** the costumes read as deadpan, adult-coded props (zipper onesies). The hearts in s063/s065/s100/s107 are
  single icons, not a cutesy framing. Nothing looks like a nursery show.
- **Doug on-model:** red cap and white head in every shot, and readable on every background, including the night navy
  (s064-s066) and dark maroon (s130, s216, s228, s231). The one exception is s148 below.

### Required fixes
1. **s148 (director): Doug is broken, and there is a stray line.** Doug uses `pose: lie` with `rotate: -90` and nothing
   covering the body (in s025/s087/s108/s127/s169 a costume, float or hammock hides it). What renders is a cap and head
   with three whisker-like lines and no torso or arms, so he looks off-model. There is also a lone brown diagonal line at
   (1100,900)-(1180,700) that reads as a render glitch.
   - Fix: remove the stray `line`, or replace it with a recognisable prop.
   - Fix: give Doug something to lie on (the `bed` asset from s146 fits the story, "wakes up fine for 20 years" ->
     dies), or use the floating ghost-Doug death used elsewhere.
2. **s100 (director): the key label is hidden.** The rat (asset at 700,330, scale 0.6) sits on top of the "CAT" corner
   label, so only a "C" shows. The shot is about the rat going to the cat corner, and the viewer can no longer see which
   corner it is.
   - Fix: keep the red circle idea from s099 and move the rat just below the label (for example y 400). Or move the
     label up and left (for example 640,240) so "CAT" is fully visible above the rat.
3. **s179 (director): the label covers the raccoon's face.** The "LATRINE" label (950,740) sits over the raccoon's head.
   - Fix: move the raccoon left (x 520) so it stands beside the latrine box, and place the label on or just above the
     box's right half (for example 1000,760), clear of the raccoon.
4. **s178 (director/illustrator): "millions of them" shows nothing.** The two `spray` layers (#fff3c4 / #c9b27a at
   density 0.03-0.08) are invisible on #f6d9cf, so the right half of the frame is empty under "MILLIONS".
   - Fix: reuse the egg-ellipse grid from s177, denser and smaller (or a large cloud of small outlined egg dots)
     spreading from the raccoon, so the viewer sees eggs.

### Non-blocking polish (recommended, not required for PASS)
- **s066, s087, s243, s247 (director): the DOUG DEATHS label covers the moon or sun.** The label at (1480,165) sits on
  the sun or moon at (1640,190), which looks sloppy. In s087 it also touches the bird silhouette's beak, and in s066 it
  crowds "TAXI". Move the sun or moon for these shots, or drop the counter's y to about 120 and x to about 1380.
- **s190 (director): Doug's body is lost against the sofa.** His black stick body disappears into the dark-red cushions
  and only the head reads. Seat him on the lighter left arm, or lift him a little so his legs hang in front of the
  lighter cushions.
- **s136 (director): the label overlaps the window.** "BITE, EYES, MOUTH" overlaps the window frame's lower-left corner.
  Nudge it left and down.
- **s180 (illustrator): the hair and the egg don't match.** The "HUMAN HAIR" bar is much thicker than the egg beneath it,
  which contradicts "SAME WIDTH". Make the bar about the egg's height.
- **s243-s247 (director): five near-identical closing shots.** These are five lake-plus-cap compositions in a row. The
  changing captions and counter card carry them, and it works as a coda. A small camera push on s245 or s246 would
  still help.

Everything else passes: pictures match the narration, subjects read in about a second, text is spelled correctly and
uncropped, and drawings are recognisable (wasp, ant, cricket, snail, cat, raccoon, mosquito and tsetse all read at
contact-sheet size). Re-render s087 (if the polish is taken), s100, s148, s178 and s179, and send the new contact tiles
back for a quick round 2.

## Round 2: re-rendered keyframes (pre-render), 2026-09-30

Scope: `build/contact/sheet_01..03` (the 25 re-rendered shots: s014, s015, s062, s064-s066, s087, s099, s100, s136,
s148, s170, s178-s180, s190, s239-s247), with full-size checks of `build/keyframes/s066, s087, s100, s148, s178,
s179, s180, s190`.

VERDICT: FAIL (two small fixes; everything else from Round 1 is resolved)

### Round 1 required fixes
1. **s148: partly fixed.** The stray brown line is gone, and Doug now lies dead in the `bed` asset with X eyes on the
   pillow. The trypanosome silhouette with its red glow reads as "the parasite", and the counter and wordart are
   clean. **Still wrong:** three thin black limb lines stick out from Doug's neck across the pillow and above the
   blanket (roughly x 590-775, y 685-705). These are the same "whisker" lines Round 1 flagged as off-model, and they
   are visible at contact-sheet size. s136 uses the identical bed and Doug setup and shows the same lines.
2. **s100: fixed.** The "CAT" label is fully visible, and the rat and heart sit just beside it. It reads at once.
3. **s179: fixed.** The raccoon stands clear on the left, and "LATRINE" sits on the box, away from its face. The arrow
   to the house door makes "close to homes" obvious.
4. **s178: fixed.** A clear cloud of outlined eggs now fills the right half under "MILLIONS".

### Round 1 polish: status
- s066, s243, s247: fixed. The counter no longer touches the moon or sun, and "TAXI" has room.
- s190: fixed. Doug sits on the sofa arm, and his body reads against the wall.
- s180: fixed. The hair bar and the egg are now the same height.
- s136: fixed. The label is clear of the window. See the limb-line note under fix 1.
- s243-s247: accepted as a coda. The ghost Doug in s246/s247 gives enough change.
- **s087: not fixed, and now worse.** The sun was moved, but the "DOUG DEATHS: 11" label (1480,165) still sits on the
  bird silhouette and now covers the top-right of its head and beak.

### Required fixes (Round 2)
1. **s148 and s136 (director): hide Doug's limb lines.** Pull the blanket up to his chin. After the `doug` element, add
   an outlined blue rect (fill about `#3b6fc6`, black outline) at x 595-1105, y 668-712, with a white fold strip at its
   left end, so no stick lines show between the head and the blanket. Or lower Doug about 25 px (y 725) if that puts
   the limbs under the existing blanket and the head stays on the pillow. Check the result at full size.
2. **s087 (director): move the counter off the bird.** Move the `DOUG DEATHS: 11` label to x about 1560, y 120, clear
   of the bird's head (bird bbox roughly x 1045-1310, y 160-350) and the sun (1720,330). Or move the songbird down and
   left (for example 1120,300).

Policy is still clean in all 25 shots: no gore, cartoon deaths only, and nothing kids-show. Doug has his red cap and
white head and reads in every shot. Re-render s087, s136 and s148 only, then send the tiles back for a quick round 3.

## Round 3: re-rendered keyframes (pre-render), 2026-09-30

Scope: full-size `build/keyframes/s087, s099, s100, s136, s148` (rendered 12:29, after the round 3 shotlist change).

VERDICT: PASS

### Round 2 required fixes
1. **s148 and s136: fixed.** The new blue blanket strip with its white fold covers Doug up to the chin. At full size and
   in a 3x crop of the pillow area, no stick-limb lines show between the head and the blanket in either shot. s148 reads
   at once: dead Doug (X eyes) in bed, the glowing trypanosome silhouette, "DID NOT FORGET", and "DOUG DEATHS: 14",
   all clear and separate. In s136 the red arrow lands on Doug's face, "BITE, EYES, MOUTH" sits clear of the window, and
   the warning triangle is clean.
2. **s087: fixed.** The songbird silhouette now sits lower (about x 1065-1330, y 285-470), and "DOUG DEATHS: 11"
   (about y 130-200) is fully clear of its head, its beak and the sun. "BILLBOARD", the snail-costume Doug on the plant,
   the bird and the ghost Doug each have their own space.

### Also checked
- **s099: pass.** Rat in the CAT corner, a red circle on CAT, the arrow from the centre, "LOST THEIR FEAR" legible, and
  rat-costume Doug on-model.
- **s100: pass.** "CAT" is fully visible, the heart sits just beside the rat, and "DRAWN TO IT" is legible.

### Non-blocking polish (optional)
- **s099 to s100 (director):** Doug in the rat costume drops about 70 px between these consecutive shots (y 780 to 850),
  so he visibly jumps at the cut. Set both shots to the same y, for example 850.
- **s136/s148 (director):** The added white fold at x 595-640 sits above and left of the bed asset's own fold (about
  x 645-685), so the blanket edge looks stepped. This is only visible close up, so it is fine to leave.

Policy is clean in all five shots: no gore, cartoon deaths only, nothing kids-show, and Doug is on-model with his red
cap and white head. Keyframe screening is complete for this round. No stage was changed.

## Thumbnail: `thumbnail.json` (archetype A grid) and s001 opening frame, 2026-09-30

Scope: I re-rendered `build/thumbnail.png` and `build/thumbnail_small.png` (320x180) with `python -m studio thumbnail`,
and the s001 keyframe (`build/keyframes/s001.png`, which uses `scene_ref: thumbnail`) with `keyframes --shots s001`.
I read them against the title "What Dying From Every Parasite Would Feel Like" and the `thumbnail_brief`.

VERDICT: FAIL (one layout fix; everything else passes)

### What passes
- **Feed size (320x180):** all nine tiles and all nine labels are readable. The saturated fills keep neighbouring
  tiles apart, and the red Brain-Eating Amoeba boss tile is the first thing the eye lands on. The grid reads as "every
  parasite", so it complements the title without repeating it. The labels are the chapter names and use no title or
  alternate-title words.
- **Doug:** the roach-costume Doug in the Jewel Wasp tile is on-model (red cap, white head, shocked face). At feed size
  he is only a red-cap dot, as the brief intends ("tiny Doug").
- **Drawings:** every creature is recognisable (wasp, ant, worm, broodsac snail, cat and rat, kissing bug, tsetse fly,
  mosquito, amoeba). There are no stray lines and nothing crosses a tile frame.
- **Policy:** there is no gore, no human bodies and no wounds. The tone is not kids-show.
- **Accuracy:** nothing is misleading, since all nine tiles are chapters in the video.
- **s001:** the grid matches "Every parasite on this list can kill the animal it lives in". It renders identically at
  1920x1080, with no top bar and no overlap.

### Required fix
1. **Thumbnail, bottom-row labels (graphic designer): lift the grid off the bottom edge.** The descenders of "Sleeping
   Sickness" and "Brain-Eating Amoeba" end at y 704, only 15 px (2%) above the bottom edge. In s001 they are 21 px
   from the edge. The top margin is just 8 px, so the grid looks jammed against the frame at both edges. This is the
   creative director's note, and it is confirmed.
   - **Change:** set every tile to `h: 160` and move the rows to `y: 20` (row 1), `244` (row 2) and `468` (row 3). The
     row pitch stays at 224.
   - **Inner elements:** scale each tile's inner elements by 160/172 (about 0.93) around the tile centre. That means
     x' = tile_x + 200 + (x - tile_x - 200) * 0.93, y' = new_y + 80 + (y - old_y - 86) * 0.93, and scale * 0.93.
   - **Checked:** I test-rendered this layout (the file is `/tmp/thumb_test.json`). The last dark pixel is at y 680, a
     39 px margin, and the top margin is 20 px. Nothing crosses a tile frame, and all labels still read at 320x180.
   - **After the change:** re-render the thumbnail and s001.

### Non-blocking notes
- **Duration badge:** YouTube's badge (bottom-right, about x 1125-1270, y 635-705 at 1280 scale) will still cover
  "Amoeba" after the fix. "Brain-Eating" plus the red boss tile still carry the threat, so this is acceptable. If the
  designer wants the full word visible, shorten the tile label to "Brain Amoeba" (the thumbnail only; the chapter name
  can stay).
- **Zombie Ant Fungus tile (illustrator/designer, optional):** the fungus stalk stands on its own at the right edge, so
  at feed size it reads as a twig, not as something growing out of the ant. Moving the stalk so it rises from the ant's
  head (about x 640, y 95) would sell "zombie" in one glance.

No stage was changed.

## Thumbnail round 2: fixed `thumbnail.json` and s001, 2026-09-30

Scope: I re-rendered `build/thumbnail.png`, `build/thumbnail_small.png` and `build/keyframes/s001.png` from the
committed `thumbnail.json` (commit 8503278) and checked them against the round 1 fix and brief section 8.

VERDICT: FAIL (one policy fix in the Zombie Ant Fungus tile; everything else passes)

### Round 1 fix: done
- **Margins:** the tiles are now `h: 160` on rows y 20 / 244 / 468. The first dark pixel is at y 17 (the tile frame)
  and the last is at y 680, a 40 px bottom margin. Nothing crosses a tile frame. s001 matches at 1920x1080.
- **Feed size (320x180):** all nine labels read, and the red boss tile still pulls the eye. Doug in the roach costume
  is on-model. The labels share no word with the title or the alternate titles.

### Required fix
1. **Thumbnail and s001, Zombie Ant Fungus tile (graphic designer): the stalk must not grow out of the ant.** The
   `fungus_stalk` (x 655, y 121, scale 0.37, rotate -22) now rises out of the ant's head, with a pale socket ring where
   it goes in. That is something leaving or growing out of a body, which brief section 8 ("Never draw ... anything
   leaving, entering or growing inside a body") rules out. It also contradicts the episode's own gore-watch decision
   (decisions.md, shotlist: "The fungus stalk stands on the leaf, not on an ant"). The thumbnail is the most-seen image,
   so it cannot be looser than the video. I retract my optional round 1 note that suggested this move; it was wrong.
   - **Change:** put the stalk beside the ant, upright and larger: `x: 775.0, y: 170.0, scale: 0.5`, and remove
     `rotate`. The anchor is bottom-centre, so the base sits on the tile floor to the right of the ant's mandibles.
     Leave the ant unchanged.
   - **Checked:** I test-rendered this change (`/tmp/thumb_r2.json`). The stalk stands clear of the ant with a gap of
     about 80 px. At 320x180 it reads as a stalk with a spore capsule, not a twig, and it is bigger than before. It does
     not touch the tile frame or the label, and nothing else moves.
   - **After the change:** re-render the thumbnail and s001 (`keyframes --shots s001`). No other tile changes.

### Non-blocking
- The duration-badge note from round 1 still applies ("Amoeba" sits under the badge at feed size). It is acceptable.

No stage was changed.

## Thumbnail round 3: fungus stalk position, 2026-09-30

Scope: I checked the already-rendered `build/thumbnail.png`, `build/thumbnail_small.png`, `build/keyframes/s001.png`,
`build/samples/f_001.png`..`f_003.png`, and one frame at 0.5 s from `build/final.mp4` (the samples start at 30 s, so
none of them show the opening image). Nothing was re-rendered and no stage was changed.

VERDICT: PASS

- **Round 2 fix: done.** `thumbnail.json` has `fungus_stalk` at x 775, y 170, scale 0.5, with no rotate. In the
  thumbnail, s001 and the opening frame of final.mp4, the stalk stands upright on the tile floor at the right edge,
  well clear of the ant. Nothing leaves, enters or grows out of a body. The ant, the tile frame and the label are
  untouched, and the other eight tiles are unchanged from round 2.
- **Feed size (320x180):** the stalk reads as a stalk with a spore capsule. All nine labels are legible, the red
  Brain-Eating Amoeba tile still pulls the eye, and Doug in the roach costume is visible in the Jewel Wasp tile.
  The thumbnail fits the title "What Dying From Every Parasite Would Feel Like" and does not mislead.
- **Samples f_001..f_003:** no black frames or glitches. The text is legible, Doug is on-model, and the tombstone
  gag is cartoon only.
- **Non-blocking (unchanged):** "Amoeba" sits under the duration badge at feed size. This is acceptable.

## Post-render: final.mp4, thumbnail, Shorts, 2026-09-30

Scope: 33 sample frames from `build/final.mp4` (every 30 s from 0:15, 982 s total), `build/qc.json`,
`build/thumbnail.png` and `thumbnail_small.png` against `metadata.json`, and the three Shorts (previews plus 6 frames
each extracted from `build/shorts/short0*.mp4`).

VERDICT: FAIL (the main video and thumbnail pass; three Shorts shots have Doug or a key drawing cut off at the side)

### Main video: pass
- `qc.json` reports no problems. There are no black, blank, frozen or glitched frames in the samples. Every frame
  matches its narration, including the s109 "HUMAN HOSTS" split screen (intentional, not a broken wipe) and s212
  "I feel totally fi", which is the scripted speech-bubble gag.
- Doug is on-model everywhere (red cap, white head). All five costumes read. Deaths are cartoon only, with no gore.
  The top-bar chapter labels match the description timestamps. The closing card reads "DOUG DEATHS: 18".

### Thumbnail: pass
- The round 2 fix is in: the `fungus_stalk` stands on its own at x 775 and does not touch the ant. It reads at
  320x180. All nine labels are legible, the red Brain-Eating Amoeba boss tile pulls the eye, and Doug in the roach
  costume is visible. It fits the title "What Dying From Every Parasite Would Feel Like" and does not mislead.

### Shorts: required fixes
Shorts show the 16:9 drawing zoomed 1.25x and centre-cropped (`studio/shorts.py`), so only **x 192..1728** of the
1920 frame survives. Three shots put key elements outside that range:
1. **s052 (short01, and the frame used for its preview), director:** Doug in the cricket costume at x 350 loses his
   antennae and back legs at the left edge. **Change:** move the `doug` and the `cricket_costume` to x 470 (both
   elements, same y and scale). This leaves a clear gap to the `horsehair_worm` coil, which starts at about x 600.
2. **s049 (short01), director:** the water `ellipse` (x 420, rx 300) spans x 120..720, so the pond is sliced off at
   the left edge. **Change:** set x 520 and rx 280 (x 240..800). Move the larva dot and its red ring by the same
   +100 px. The leaf at x 1100 is unaffected.
3. **s029 (short02), director:** Doug in the ant costume at x 1650 sits across the right crop line, and his costume
   legs are cut off. **Change:** move the `doug` and the `ant_costume` to x 1560 and scale 0.42. Check the keyframe
   to confirm he doesn't touch the carpenter ant's mandibles, which end at about x 1480.
- **After the changes:** run `python -m studio keyframes 002-every-parasite --shots s029,s049,s052`, then
  `python -m studio shorts render 002-every-parasite`. These shots look the same in 16:9, so `final.mp4` does not
  need a full re-render for picture reasons. It is the editor's call whether to re-render it so it matches the
  shotlist again.

### Shorts: otherwise fine
- Hook titles are legible, subtitles are legible (2 lines max, white with a black outline) and the @DoomedDoug tag
  is readable. All three end cards (blue, WordArt, Doug pointing) have the red arrow pointing straight **down**
  inside the safe area. End-card text: "WHAT HAPPENS NEXT? TAP BELOW", "THE WORST PART? TAP BELOW", "ALL 18 DEATHS:
  TAP BELOW". Durations are 49.3, 56.4 and 34.6 s.

### Non-blocking
- **short02 title (youtube-titler):** "This Fungus Makes Ants Bite Down and Never Let Go" wraps to three lines and
  leaves "Go" alone on the last line. A title of 42 characters or fewer would fit in two lines, for example "This
  Fungus Makes Ants Bite and Never Let Go".
- **short03 opener s229 (director):** the "whole list" line-up (wasp 0.35, cat 0.3, raccoon 0.4, mosquito 0.35,
  Doug 0.25) is thumbnail-sized in the Short, so frame 1 of the Short is mostly empty pink. Consider starting short03
  on the next shot, or accept it.
- **s116 (director):** the "79 COUNTRIES" WordArt sits on the bottom border of the world map. It is readable, but
  moving it to y 1000 below the map would be cleaner.

No stage was changed.

## Post-render round 2: re-rendered final.mp4 and Shorts, 2026-09-30

Scope: frames extracted from `build/shorts/short02.mp4` (s027, s029), `build/shorts/short03.mp4` (s232-s235),
`build/shorts/short01.mp4` (s049, s052) and `build/final.mp4` (s027 at 99.5 s, s232-s235 at 930-945 s), plus the 33
new samples in `build/samples/` (21:40 render).

VERDICT: PASS

### Earlier fixes verified
- **s027 (short02):** the nest (x 1600, rx 80) sits fully inside the crop, right of the arrow and under the right-hand
  tree canopy. "HIGH UP" and the red arrow both read. It is also correct in 16:9.
- **s029 (short02):** Doug in the ant costume at x 1560 is complete, with nothing cut off, and he is clear of the
  carpenter ant's mandibles.
- **s049 / s052 (short01):** the pond and the larva ring are entirely inside the frame. Doug in the cricket costume
  keeps his antennae and legs, and he doesn't touch the worm coil.
- **s232:** the chart is empty on the first frame and the red line is in by 0.6 s ("The statistics are grim."), in
  both short03 and final.mp4. The line no longer arrives after the narration.
- **s233 (short03):** Doug at x 1600 is fully inside the right edge of the crop (cap and legs intact) beside the
  USA map. "1962-2024" and "167 CASES" arrive on cue.
- **s235:** "FATALITY RATE" is up from the start of "That's a fatality rate". "97%" lands on "ninety-seven percent"
  and the warning triangle on "the illness moves fast". The timing matches the narration in both the Short and the
  main video.

### Samples: pass
- `qc.json` has no problems. All 33 samples are clean, with no black, frozen or glitched frames. Doug is on-model
  throughout, the text is legible, deaths are cartoon only and the end card reads "DOUG DEATHS: 18".

### Non-blocking (unchanged, accepted)
- The short02 title still wraps to leave "Go" alone on the third line (youtube-titler, optional).
- The s229 opener in short03 is still small (director, optional).
- s116 "79 COUNTRIES" still sits on the map border. It is readable.

No stage was changed.
