# Visual review: 030-trapped-in-amber

## Round 1: pre-render keyframes (2026-10-28)

Screened all 19 contact sheets (s001 to s216 plus the endslate) and checked the flagged shots at full resolution in
`build/keyframes/`. s001 is the thumbnail placeholder and was skipped as instructed.

### What works
- Doug is on-model in every shot (red cap, white head, stick body), including the cockroach costume (s072 to s074) and
  the ghost and cap death beats.
- The death counter runs cleanly from 240 to 246 (s031, s075, s103, s129, s179, s210). The topbar chapter labels match the chapters.
- All text is spelled correctly and none of it is cropped (Deinocroton draculi, Xiaophis myanmarensis, Oculudentavis,
  Enantiornithines, Myitkyina, Kachin State, vertebrae).
- No gore and no kids-show tone. The blood-fed tick (s007, s008) and the "traces of iron from the blood" shot (s195)
  don't show any blood. All six deaths are cartoon offscreen or ghost-and-cap beats. The RIP DOUG headstones (s154) are fine.
- Strong set pieces: the resin-on-the-beach sequence (s091 to s095), the tide death (s101 to s103), the specimen-tray
  running gag, the market stall (s197 to s199), and the cap in the resin drop (s211).

### Problems
The main failure is variety. About 95 of 216 shots use the same composition: an amber bead in the centre, Doug small
at the left, a label above and wordart below, and most of them have no camera move. That gives runs of 4 to 8
near-identical frames all through the episode.

VERDICT: FAIL

### Required fixes
1. **Director (variety).** Break up every run below so that no more than 3 consecutive shots share the centred-bead
   framing. Re-stage at least half the shots in each run using one of these: an extreme close-up of the specimen
   (group scale 2 to 3, cropped), a `zoom_in` or custom camera move, a cutaway to the living animal in its forest or
   beach set, Doug interacting with the bead (magnifier, standing beside a giant bead, side switch), or a split
   comparison.
   - s006, s007, s009, s010, s011 (tick). For example, s009/s010 could be a close-up of the swollen tick with a
     "DRACULA" nameplate, and s011 a cutaway of the tick on the living feather.
   - s033 to s037 and s040 to s042, s045 to s047, s049 (web). For example, s035 could be a forest cutaway of the
     spider frozen mid-lunge, and s046/s047 a close-up of the two spiders.
   - s055 to s062 (hell ant, 8 in a row). For example, s058/s059 could be a live hell ant in the forest set, and
     s061 a close-up of the jaws and horn with the nymph.
   - s066 to s071 (vampire ant, 6 in a row). For example, s068/s069 could be a live-action cutaway of the ant
     piercing its prey (no fluid shown).
   - s080 to s084, s087 to s090, s096 to s100 (ammonite).
   - s107 to s114 and s117 to s120 (snake). For example, s112 could be a vertebrae close-up with the "97" count.
   - s131 to s133, s135, s141 to s144 (Oculudentavis).
   - s157 to s164 (hatchling, 8 in a row).
   - s183 to s187, s189, s191, s192 (tail).
   - s202 to s205: four identical map frames. Re-stage at least two of them. For example, s203 could show a mine
     entrance in Kachin, and s204/s205 a journal page with a "NOT PUBLISHED" stamp.
2. **s004 (director).** The red arrow from "FIRST DINOSAUR TAIL" lands on the fern at the dinosaur's feet, and the
   tail is half hidden behind the tree trunk at x 1145 to 1235. Make the arrow end on the tail (around x 1050, y 600)
   and move the trunk or the silhouette so the whole tail is visible.
3. **s012 (director).** The picture contradicts the narration. The tick in its bead is drawn about 3 times wider than
   the penny's edge, so the viewer sees a tick that is bigger than a penny is thick. Show the coin's edge thickness
   next to a tick at true relative scale (tick about 2/3 of the edge, with a zoomed inset if needed), or drop the
   full-size bead from this shot.
4. **s065 (director).** "Shorter than a grain of rice" doesn't read: the hell ant (scale 1.05) is as long as the rice
   grain. Scale the ant to about 0.7 and line up the left ends of the ant and the rice so the difference is obvious.
5. **s046 and s047 (director).** The adult male spider (`amber_spider`, scale 1.05 at 140,110) sticks out past the
   bead's right edge, so it reads as outside the amber. Scale it to about 0.8 and move it fully inside the bead,
   then move the "?" and the ADULT MALE label to match.
6. **s172, s173, s174 (director).** Doug stands on the tree trunk at x about 450 (trunk at x 425 to 515). His black
   body lines disappear against the dark trunk and only his head reads. Move Doug to x about 620, clear of both trunks.
7. **s134 (illustrator).** The "THUMBNAIL" comparison is a pink oval with a white circle, which reads as an egg.
   Draw a recognisable thumb tip (thumb outline with a nail), or a hand with the thumb raised.
8. **s048 (illustrator).** "SPIDER EGGS" is one blank white oval, which reads as a single egg or a balloon. Draw a
   silk egg sac with visible clustered eggs.

### Advisory (fix if cheap)
- s032, s054 (director): the dashed "drop" line above the newest tray slot isn't connected to anything (it ends about
  140 px above the bead) and reads as a stray mark. Either extend it to the bead with a small motion tick or remove
  it. s076, s104, s130, s155 and s181 use the same line. It is fine where it visibly links a label to a slot.
- s153, s154 (illustrator): the `old_drawing_card` asset has an empty white title plate in its top right corner.
  Fill it (for example "1890s") or remove it.
- s121, s128 (illustrator): the big snake silhouette reads as a black rope, especially where it wraps the branch in
  s121. A pale eye or tongue glint would make it read as a snake in under a second.
- s165 to s167 (illustrator): the rough amber lump reads as a potato or rock. Add amber colour, translucency and one
  glint so it reads as raw amber.
- s202 to s205 (director): the map doesn't highlight Kachin State. Add a red outline on the region next to the
  "KACHIN STATE" label.
- s210: a 1.2 s black frame with only the counter. This is acceptable as a cut-to-black death (precedent: 024) and is
  noted here only so the editor doesn't flag it as a blank frame in QC.
