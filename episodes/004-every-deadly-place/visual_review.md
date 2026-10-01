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

## Round 2: keyframe re-check, 2026-10-01

Scope: every changed shot at full resolution (s011, s030, s062 to s064, s067, s101, s103, s104, s137, s141, s142,
s145 to s151, s154, s157, s162, s171 to s173, s175, s176, s183, s195, s197, s222 to s225, s240, s244, s251, s252,
s263, s265, s266, s268, s273 to s282), plus their unchanged neighbours (s136, s138, s249, s250, s262, s264, s267,
s269), to re-check the variety runs.

### Round 1 blocking fixes: status
1. s063, s064: **fixed.** Doug's head, torso and both arms now show above the sand line, and the legs are cut away
   below it. "Sunk to the waist" reads, and he's on-model.
2. s067: **fixed.** The QUICKSAND end is down and Doug's end is up, which matches "half as dense".
3. s224: **fixed.** The bolt's tip lands in the Venezuela circle, and "MOST LIGHTNING" now sits above the map frame.
4. s197: **fixed.** The canyon now has visible life: a bird, a fern, two green shoots and a jackal. "Life was doing
   fine" reads in 1 second.
5. s176: **fixed.** Ghost Doug is in open water at the top left, clear of the crystals.
6. s030: **fixed.** The halo is now a yellow-green glow with no red spray. The silhouette tease still works.
7. Text over drawings: **fixed** in s151 (clears the crystal by a few px; see A4), s154, s157, s162, s175 and s225.
8. Variety runs: **fixed.** s147 (wide shot from behind, over the peaks), s148 (face close-up with clock), s137
   (climber close-up with hemoglobin inset), s251 (lake = 2 soccer fields), s252 (pull-back to the volcano), s263
   (volcano inset), s266 (split with Nyos) and s268 (push-in with animals and warning sign). No run of 4 or more
   near-identical frames is left in these sections.
9. s278 to s282: **fixed.** The orange lava band stays behind the cap, ghost and suitcase, so continuity holds.

Round 1 advisories: s062 is still unchanged, with Doug fully on the surface (fine to leave). s101 is OK: the label now
sits over the suitcase and the arrow points at his crusted flip-flops. s131 wasn't touched. s195, s222, s240 and s244
are fixed.

Policy: no new gore. The s268 animal silhouettes are plain black shapes. The Nyos panel in s266 is a neutral
diagram, with no joke and no figure.

### Required fixes (blocking)
1. **s266 (director): the Nyos hill spills into the left panel.** The Nyos hill poly is `smooth: true` and starts at
   (960,760), so the smoothing makes it bulge about 75 px left of the divider line, between roughly y=840 and y=1080.
   A dark green lobe then crosses into the mazuku panel, past the split line. Fix it in one of two ways:
   - Set `smooth: false` on that poly.
   - Or add a clip vertex so the shape can't cross x=960. For example, start the points at [960,1120], [960,760],
     ..., and draw the left-panel ground poly after the Nyos hill.
2. **s282 (director): the arrow points at nothing, which contradicts "still has room".** All 9 sticker slots are
   full. The arrow (to [1392,796]) hits the bottom-right corner or wheel, so the final image says "no room". Show an
   empty slot and point the arrow at it. For example:
   - Drop the sticker scale to about 0.8 and tighten the rows so a clear brown strip shows at the bottom of the
     case.
   - Then add a white dashed rounded-rect "empty sticker" outline there, about 90x45, and aim the arrow at its centre.

### Advisory (non-blocking)
- A1. s279: the marshmallow is golden-toasted, but "more than the marshmallow can say" needs it worse off than the cap.
  Make the marshmallow charred black (dark fill, or a black spray of density 0.5 or more) with a small smoke wisp.
- A2. s150: "1/3 OF A BREATH" touches the foot of the DOUG flagpole. Shift it right about 30 px or down about 30 px.
- A3. s263: the volcano inset floats in the sky with no frame. Put a thin black inset box (or a white-bordered
  circle) around it so it reads as a cutaway, not a flying volcano.
- A4. s151: the title clears the top crystal by only a few px, and the DOUG DEATHS box nearly touches it. Lift
  the wordart about 20 px, or drop it to size 0.9.

VERDICT: FAIL (required fixes 1 and 2: the director re-blocks s266 and s282, then re-runs keyframes for those 2 shots. No
illustrator, art director or graphic designer work is needed.)

## Round 3: keyframe re-check, 2026-10-01

Scope: s266, s282 (round 2 blocking fixes), plus s279, s263, s150 and s151 (round 2 advisories). All six were viewed
at full resolution from `build/keyframes/`.

### Round 2 blocking fixes: status
1. s266: **fixed.** The Nyos hill now stops at the divider. The left (mazuku) panel's ground line is clean from
   x=0 to x=960, and no green lobe crosses the split. MAZUKU / SAME GAS / LAKE NYOS read as a clean side-by-side,
   and the red X on the lake lands "no lake needed" in 1 second.
2. s282: **fixed.** A white dashed empty-sticker outline now sits at the bottom right of the case, below
   NYIRAGONGO. The red arrow's head lands inside it, so "STILL HAS ROOM" now matches the picture. The 9 stickers
   are still legible at the smaller scale.

### Round 2 advisories: status
- A1. s279: **fixed.** The marshmallow on the stick is now a charred black block with a grey smoke wisp, so it's
  clearly worse off than the intact red cap. It's small at lower left, but it's the only stick prop in frame, so the
  eye finds it.
- A2. s150: **fixed.** "1/3 OF A BREATH" now sits well above the DOUG pennant and touches nothing.
- A3. s263: **fixed.** The volcano now sits in a white-bordered navy inset box and reads as a cutaway. Doug is
  gritted in the mazuku hollow, with a red "!" beside the inset.
- A4. s151: **fixed (tight).** The wordart now clears the DOUG DEATHS box easily. Its baseline is still only about
  5 to 10 px above the top crystal's upper-left tip. That's legible, so it isn't blocking.

### New observations (non-blocking)
- s282: the arrow shaft clips the lower-right corner of the NYIRAGONGO sticker on its way to the slot. It still
  reads correctly. If the director touches this shot again, start the arrow lower (around y=700) so it clears the
  sticker.

Policy: no gore. The ghost Doug in s279 and s282 is the standard cartoon death. The tone is adult and not cutesy.

VERDICT: PASS

## Thumbnail final, 2026-10-01

Scope: `build/thumbnail.png` (1280x720), `build/thumbnail_small.png` (320x180), plus a 168x94 downscale for feed
size. Checked after the creative director's tweaks: a bigger Natron Doug and icicles on the Antarctic tile.

- Natron Doug: **reads.** He's now as tall as the left flamingo, and the red cap and white head pop against the pink.
  At 168x94 the red cap is still a clear dot of red with a white face under it, so "Doug is in this" now reads at feed
  size, which closes the round 1 advisory. The flamingo costume is on-brief (`thumbnail.json` note) and fits the
  locked design: cap and head unchanged. His body is cut off by the tile's lower edge, which reads as standing
  waist-deep in the lake. That's fine.
- Antarctic tile: **improved.** Two clusters of three icicles hang from the top corners, with frost sprays under them
  and frost sparkle around the window. The cabin now reads as besieged by cold rather than cosy. The icicles still
  show as white teeth at 168 px. They touch the tile border and nothing else, and they stay clear of the antenna and
  the label.
- Whole grid: all 9 labels are spelled correctly and uncropped. They're legible at 320 px and blur at 168 px, as
  expected for this archetype, but the colour blocks and icons (sun, snakes, Doug, cabin, peak, crystals, cones,
  lightning, volcano and warning sign) carry the read. The severity colour run and the Nyiragongo boss tile are
  intact. It complements "What Dying in Every Deadly Place on Earth Would Be Like" and isn't misleading. No gore, and
  it isn't kid-coded.
- Non-blocking: none.

VERDICT: PASS
