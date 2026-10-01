# Visual review: 004-every-deadly-place

## Round 1: keyframes (pre-render) and thumbnail, 2026-10-01

Scope: all 24 contact sheets (s001 to s282), with full-resolution keyframes checked for s030, s063, s067, s068, s072,
s176 and s197, plus `build/thumbnail.png` and `build/thumbnail_small.png` (also tested downscaled to 168x94).

### Overall
- Style is consistent and on-bible. Doug (red cap, white head) is on-model and readable in almost every shot. The
  suitcase sticker gag accumulates correctly, and the death counter runs 27 to 36 with survivals at Natron (s101) and
  Maracaibo (s241 to s244).
- Policy: no gore anywhere. Doug's deaths are cartoon only (X eyes, ghost, ice block, floating cap). The dead
  birds and bats at Natron (s094 to s096) and the mazuku animals (s268, s269) are small grey or black silhouettes with
  no injury detail. Nothing reads as a kids' show: no nursery framing, and the flamingo chicks (s102) are factual.
- **Lake Nyos (sombre item): PASS.** s205 to s222 carry no visual jokes. The casualty shot (s212) shows only the gas
  cloud over an empty hillside, with no figures or bodies. Doug's beat (s220, s221) is deadpan: he lies down with no
  ghost, no gag props and no expression gag. The sticker is a plain dark oval. Nyos is not on the thumbnail or in the
  s001 grid. The only polish item is #12 below.
- Thumbnail: PASS with one advisory (see the Thumbnail section).

### Required fixes (blocking)
1. **s063, s064 (director): Doug is broken.** The sand rect (top y=600) is drawn after Doug, so it hides his torso and
   arms. What's left is a head sitting on two long legs, which looks off-model. Make "sunk to the waist" read: either
   draw the sand rect before Doug and add a foreground sand band at waist height, or move the sand top down to Doug's
   hip line so the torso and both arms show above the sand. Keep the leg cut-away lines below the sand.
2. **s067 (director): the seesaw says the opposite of the narration.** The plank runs from (560,800) to (1360,700), so
   Doug's end is down, which reads as "Doug is heavier/denser than quicksand". Flip the tilt so the QUICKSAND block's
   end is down and Doug's end is up. Use s210 (CO2 side down) as the correct model.
3. **s224 (director): the lightning bolt is in the wrong place.** It sits over North America while the red circle marks
   Venezuela. Move the bolt so it strikes inside or right beside the Venezuela circle. The "MOST LIGHTNING" wordart also
   sits on the map's top border. Move it above the map frame or into the empty Pacific area.
4. **s197 (director, illustrator only if no asset exists): the punchline is invisible.** The narration is "life was
   doing fine", but the two green `spray` patches (density 0.08 on #d98c4a orange) can't be seen at any size, so the
   frame shows an empty canyon and a thumbs-up. Replace them with visible life: library shrubs or cacti, a bird, or
   a lizard if one exists. Otherwise raise the density to at least 0.35 and use a darker green outline.
5. **s176 (director): ghost Doug is lost against the crystal.** The ghost's thin grey body sits on top of the
   cream crystal at the top left, so only a floating head reads. Move the ghost into open blue water, e.g. around
   (450,180) clear of the crystals.
6. **s030 (director): the red halo reads badly.** The red speckle halo around the black snake silhouette looks like
   blood mist, especially in motion. Keep the silhouette tease but change the halo to the channel's yellow/white glow
   or a plain "?" so nothing red sprays around an animal.
7. **Text over drawings (director): move wordart off the drawings into clear space.**
   - s151: "CAVE OF CRYSTALS" title crosses two crystals. Move it up to about y=180 above the crystals, or remove the
     top-left crystal for this shot.
   - s154: "MOST BEAUTIFUL" sits on the top crystal. Move it to the clear upper right.
   - s157: "SLOWLY" overlaps a crystal. Move it to the clear area at the right of the frame.
   - s162: "REAL KILLER" sits on the bottom crystal. Lift it to clear dark space, e.g. y=300 on the left.
   - s175: "KEEP GROWING" crosses the large crystal. Move it to the clear water at the lower left or upper right.
   - s225: "ISN'T CLOSE" overlaps the lightning bolts. Move it to the open sky above the clouds or onto the water band
     below the bolts.
8. **Variety runs of 4 or more near-identical compositions (director).** Fix each run with one camera change (close-up,
   zoom/push, low angle or reframed inset):
   - s145 to s150 (6 shots, the same summit frame): make s147 ("admire the view") a wide shot from behind Doug looking
     out over the peaks, and s148 a close-up on Doug's face with the clock.
   - s262 to s269 (8 shots, the same forest hollow): make s266 a split frame with a small Nyos lake inset, and s268
     a push-in on the hollow showing the animal silhouettes and the warning sign.
   - s249 to s252 (4 shots, the same crater top view): make s251 a side-by-side with two soccer fields at the same scale
     as the lake, and s252 a pull-back that shows the volcano.
   - s136 to s139 (4 shots, the same mountain with Doug at the lower left): make s137 an inset of blood cells
     next to a climber close-up instead of the full mountain.
9. **s278 to s282 (director): continuity break.** The lava lake (orange band) disappears after s277, leaving a dark
   plain, so it looks like a different place. Keep the orange lava band in the background of the aftermath and end
   card. It can be lower in frame so the cap, ghost and suitcase stay clear.

### Advisory (non-blocking, fix if cheap)
10. s062 ("so you sink"): Doug stands fully on the surface. Have him sunk to the knees so the sink starts here.
11. s131 ("twenty-three Empire State Buildings"): only a dashed line and "x23" are shown. Add a small stack of
    building silhouettes beside the mountain, or a single building with "x23".
12. s222: the moon is half-hidden behind the DOUG DEATHS box. Move the moon to around x=1500, y=180. You could also
    drop the counter here, since the Nyos close is calmer without it.
13. s101: the red arrow points at empty ground, and the "NO STICKER" label isn't explained by the narration. Either
    point the arrow at the suitcase's empty sticker slot or drop the arrow.
14. s195: the "NO MICROBIAL LIFE" wordart touches the bottom of the circle. Nudge it down about 40 px.
15. s240, s244: the wordart crosses the fishing line. Shift it right or down by about 60 px.

### Thumbnail (graphic designer)
- 1280x720 and 320x180: PASS. The 3x3 grid follows the brief: severity order, hot-to-cold-to-lava colour run, and
  Nyiragongo as the bottom-right boss with a warning sign. Labels contain no title words and Nyos is excluded. The
  labels read at 320 px. At 168x94 the labels blur, as expected for this archetype, but the colour blocks, sun, snakes,
  volcano and lightning still read. It complements the title, isn't misleading, and matches the s001 opening frame.
- Advisory: Doug (Natron tile) is the only human and is small at feed size. Consider making the Natron tile's Doug
  about 15% bigger, or giving his tile a thicker red border so "Doug goes to all of these" reads at 168 px. The
  Antarctic tile (a warm red cabin) reads cosy rather than deadly. A frost spray or a frozen thermometer next to the
  cabin would add threat. Neither is blocking.

VERDICT: FAIL (fixes 1 to 9: director re-blocks s030, s062 optional, s063, s064, s067, s136 to s139, s145 to s150, s151, s154, s157,
s162, s175, s176, s197, s224, s225, s249 to s252, s262 to s269, s278 to s282; then re-run keyframes for those shots for round 2)
