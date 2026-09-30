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
