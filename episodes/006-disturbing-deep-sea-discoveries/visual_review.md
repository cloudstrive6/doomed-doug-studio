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
