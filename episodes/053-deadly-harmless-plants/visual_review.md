# 053-deadly-harmless-plants: visual review

## Round 1: pre-render keyframes (2026-11-20, visual screener)

Scope: contact sheets 01-17 (s002-s195), plus full-size keyframes for s013, s020, s058, s063, s101, s155, s188, s190.
s001 is not reviewed because it uses `scene_ref: thumbnail` and the thumbnail is not delivered yet. Re-check it once the
thumbnail exists.

VERDICT: FAIL

The episode is close. There is no gore. Skin reactions are flat cartoon pink or red only: s056-s060 flush, s138 and
s142-s143 sunburn, s183-s188 manchineel. The s132-s136 skin cross-section is flat bands, with no blisters, wounds or
drips. Deaths are cartoon only: X eyes, ghost Doug, RIP stone, and soldiers with closed eyes. Doug is on-model in every
shot. His red cap is always visible, and his ink whitens on the dark night, rainforest and herbarium backgrounds. The
HUD text, labels and WordArt are spelled right and none of them are cropped. Nothing has a kids'-show tone: the angry
sun and the narrator's hand gag are adult-coded. Four shots have a picture that misreads or hides the key subject. They
are quick fixes, but they should be made before the render.

### Required fixes

1. **s013 (director, composition).** The label "USDA" sits directly under the water hemlock root, so the root reads
   as a plant called "USDA". Relabel it `WATER HEMLOCK` at (520,900). If you want the source on screen, add a small
   `USDA` tag at size 28 above the "=" sign (about 760,300).
2. **s063, and also s062, s078 and s079 (director, composition).** The oleander bushes straddle the upper road lane
   and the median, and the red car in s063 is drawn on top of the bush row, so it looks like it is driving through the
   hedge. Lower the bush row about 50 px so the bases sit inside the median band (y 750-830). In s063, put the red car
   in the upper lane, layered behind the bushes, at about y 640. In s079, remove the small red car that sits on top of
   the bushes, or move it into a lane.
3. **s003 and s126 (director, composition).** This was optional in art_review.md. I am making it required. On the
   title cards, the WordArt covers the umbels, and the umbels are the one feature that identifies hemlock and
   hogweed at the moment each plant is introduced. Raise the title about 60 px or drop the plant about 60 px so the
   whole umbel is clear.
4. **s190, with s191 and s192 for continuity (director, composition).** The narration says "The cap sat *under* that
   tree all night", but the cap hangs on the right-hand branch at about 40 px. It reads as a red blob at feed size and
   is in the wrong place. Put Doug's cap on the sand under the canopy (about x 1000, y 800) and scale it about 2x so it
   is unmistakably the red cap. Keep the drips falling onto it.

### Recommended (non-blocking polish)

5. **s101 (director, composition).** The Greek helmet is stacked on top of Doug's cap and seems to float. A stray
   helmet crest pokes out of the field-guide top edge. The "breakfast" plate (honeycomb slab) reads as toast. Drop the
   stacked helmet, and add a small `HONEY` label on the plate.
6. **s102 (director).** Known issue, still open: the dropped helmet reads as a red blob. Rotate it 30 or remove it.
7. **s166 (director).** Known issue, still open: Doug overlaps the trunk. Move him about 80 px right.
8. **s124 (director).** Known issue, still open: the "HIS ARM" label is jammed under the CONTACT label. Lower it
   about 40 px.
9. **s108-s111 and s113-s122 (illustrator / art director, continuity).** The cow switches from a brown Hereford
   (s108-s111) to a black-and-white Holstein (s113-s122) within the same story. Pick one design for the whole White
   Snakeroot segment.
10. **s083, s094 and s194 (illustrator).** The honey jar label is a blank white box. Write `HONEY` on it so the jar
    reads instantly, especially at the s194 line-up size.
11. **s155 (director).** The wooden tray with eight dark wells reads as a muffin tin or a mancala board, not as old
    specimens. Either label it `HERBARIUM DRAWER`, or show the pressed-leaf sheet from s156 sliding out of a drawer.
12. **s182-s186 (director, variety).** These are 5 consecutive near-identical wides: tree, Doug, fire and guide.
    s015-s018 is a run of 4 (pot, fire, hemlock and guide). Punch in on one beat in each run, for example s184 as a
    close-up of Doug biting the green apple, and s017 as a close-up of the soup bowl.
13. **s020, s042 and s092 (art director).** The grey/purple `glow` behind the silhouettes renders as a grainy smudge
    that looks like dirt or static on the grey-green backgrounds. The red s162 glow reads fine. Shrink `glow_r` about
    40%, or use a warmer and denser glow colour.
14. **s035 and s036 (director).** The SAFE label box crosses the berry outline, and the NOT SAFE arrow line runs
    through the "N". Nudge both labels about 30 px right/up.
15. **s189 (editor).** This black "Again." frame is intentional. It is 1.4 s, with the HUD visible. Make sure the QC
    black-frame check does not flag it, and do not extend it.

Route for round 2: director fixes 1-4, then regenerate keyframes for s003, s013, s062, s063, s078, s079, s126 and
s190-s192. Send them back to me, together with s001 once the thumbnail exists.
