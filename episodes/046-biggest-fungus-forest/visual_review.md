# 046 Visual review

## Round 1: keyframes (2026-11-13)

Scope: contact sheets 01-16, s002-s184 + endslate (s001 thumbnail placeholder ignored).

Overall: strong episode. Doug on-model and readable throughout, chapter cards clear, costumes (vine, tomato,
aspen, pine, Douglas fir) read instantly, deaths are cartoon (squashed tomato, ghost, cap on mushrooms), no gore,
no kids-show tone, HUD counter increments correctly 350 -> 356. Failing on a handful of shots where the picture
contradicts the line or the key subject is not visible, plus map placement.

VERDICT: FAIL

### Required fixes
1. **s076** (director): the red X sits over Doug, so "It looks like a normal tree. It isn't." reads as "Doug isn't".
   Move `red_x` onto the nuytsia_tree crown (or swap for a "?" over the tree); Doug can stay with a sideways look.
2. **s099** (director): red X over the new shoots contradicts the line ("the root sends up new shoots to replace it").
   Remove the `red_x`; keep the up-arrow and sprout, optionally add a second sprout. The X belongs at s101/s103.
3. **s135, s154, s158, s166** (illustrator + director): `pnw_map` has no visible WA/OR border, so "OREGON" and
   "WASHINGTON" labels sit on what looks like one state, and both circles are far too far west.
   Illustrator: add a dashed state border along the Columbia and small "WA" / "OR" labels to `pnw_map`.
   Director: move the Mount Adams circle (s135, s158 trophy start, s166 start) to ~42% across the map just north of
   the Columbia; move the Malheur/Blue Mountains circle (s154, s158 trophy end, s166 end) to ~75% across, in
   north-east Oregon.
4. **s167** (director): the root-to-root connection (the whole point of the line) is a near-black curve on
   near-black soil (#1d1a18) and is invisible. Recolour the connecting roots to the rhizomorph tan (or white) at
   width >= 6, and add a small arrow along it.
5. **s147, s149** (director/illustrator): foxfire is "a weak greenish glow" but the glow is a faint grey speckle;
   at s149 ("lit from underneath") the key subject barely reads. Give the rhizomorph_web a visible green glow
   (green spray/glow_r around the threads, e.g. #8fe36a at higher density). Keep it dim-ish but clearly green.

### Should fix (text over drawings)
6. **s003** (director): "1,000 PITCHES" is struck through by rhizomorph lines. Move the wordart to y ~ 600 over a
   clear patch, or add a dark backing/outline so the lines do not cross the letters.
7. **s074, s075** (director): "CHRISTMAS TREE" / "GOLDEN-ORANGE" green wordart sits on the orange crown/trunk and
   loses contrast. Move both to the empty right-hand sky (x ~ 1450, y ~ 420) above Doug.
8. **s093** (director): "ONE LIVING THING" runs through the trunks and over Doug's head. Raise it to y ~ 330 above
   the canopy line, Doug stays where he is.
9. **s096** (director): "ONE TREE" overlaps the right edge of the 60-pitch grid. Shift grid left ~120 px or move
   the wordart below/right of the grid.
10. **s072, s112** (director): chapter-title wordart overlaps the tree crowns ("TREE" over the nuytsia crown,
    "FUNGUS" over the trees). Raise the title ~80 px or shrink/lower the drawings so the title sits on sky.
11. **s070** (director): nuytsia silhouette crown is clipped by the top edge and sits under the chapter label.
    Lower the tree ~120 px or scale to ~0.8.

### Nice to have
12. **s120-s123** (director): four consecutive near-identical rhizomorph-on-brown frames (s122 and s123 are almost
    the same picture). Recompose s123 ("still the same individual"): e.g. pull out wide over the forest with one
    tinted outline over the whole web and the DNA strand + "SAME ONE" larger and centred.
13. **s028** (illustrator/director): the dodder seedling is a black silhouette (looks like a cane/hook) while it is
    orange in every later shot. Fine as a teaser, but an orange outline would tie it to s033.
14. **s097, s127** (illustrator): balance scales hang level with weight on one pan only; tip the loaded pan down.
15. **s175** (director): 965 HA square vs the "20X" rectangle is ~48x in area; resize to ~20x (e.g. big rectangle
    ~ 300x200 px vs a 55x55 px square).

## Round 2: keyframes (2026-11-13)

Scope: re-screen of all 16 contact sheets against round 1 fixes 1-15.

Fixed and confirmed: 1 (s076 X on crown), 2 (s099 X removed, arrow + shoots), 4 (s167 tan roots + arrow, reads
clearly), 5 (s147/s149 foxfire now visibly green), 6 (s003), 7 (s074/s075 wordart on clear sky), 8 (s093),
9 (s096), 10 (s112; s072 now only grazes the crown, acceptable), 11 (s070), 12 (s123 recomposed with outline and
SAME ONE), 15 (s175 now ~20x). Not done, still nice-to-have only: 13 (s028), 14 (s097/s127 level scales).

Map (fix 3): the new `pnw_map_states` works. The dashed WA/OR border along the Columbia plus WA/OR/ID/MT labels
make the states read instantly, and at s135 the Mount Adams circle now sits correctly in south-central Washington
just north of the border. Keeping the circles in place was acceptable for Mount Adams. The Oregon end is not:
because the map's bottom edge cuts Oregon off just south of the Columbia, the Malheur/Blue Mountains marker is
drawn on the map's black bottom frame line, half outside the map, in s154 (circle), s158 (trophy end point) and
s166 (circle at end of the dashed line). This is the key subject of all three shots and reads as "off the map".

VERDICT: FAIL

### Required fixes
1. **s154, s158, s166** (director): move the Blue Mountains marker inside the map, about 60-70 px up and slightly
   right, to roughly (790, 745) in frame coordinates (inside the Oregon strip, west of the Snake River/ID line), so
   the whole circle/trophy sits on green below the dashed border. In s154 move the "OREGON" label off that spot
   (e.g. drop it, since the map already says OR, or place it below the map next to "965 HECTARES"). Keep the s158
   trophy arrow and s166 dashed link ending on the new position.

## Round 3: keyframes (2026-11-13)

Scope: s154, s158, s166 after the Blue Mountains marker move to (790, 745). Keyframes re-rendered after the
shotlist change (18:04:41 vs 18:04:19).

- **s154**: red circle now sits fully on green inside the Oregon strip, below the dashed WA/OR border and west of
  the Snake/ID line, well clear of the bottom frame. The extra "OREGON" label is gone (map's OR label suffices).
  "965 HECTARES" and Doug (shock, right) read cleanly. Fixed.
- **s158**: arrow runs from the WA trophy to the new spot; the 1998 trophy sits on the circle inside the map. The
  cup's rim just touches the dashed border and covers most of the circle, but the trophy's base is clearly in
  Oregon and the "record moved from WA to OR" reads in one second. Acceptable.
- **s166**: both circles inside the map; the white dashed link ends on the new Oregon circle. Fixed.

No new issues. Round 2 nice-to-haves 13 (s028) and 14 (s097/s127) remain optional.

VERDICT: PASS

## Round 4: thumbnails A/B/C (2026-11-13)

Scope: build/thumbnail.png, thumbnail_b.png, thumbnail_c.png and their 168x94 `_small` versions, checked against
the paired titles in metadata.json packaging.variants.

### A: "ALL ONE THING" / "A Fungus Under Oregon Has Been Killing Trees for 2,400 Years"
- Feed size: text fully readable; the white root web filling the lower two thirds is the clear focal mass; Doug's
  red cap and white head pop against the orange sky even at 168 px. Strong "something huge is under him" read.
- Doug on-model (red cap, white head, shock face) in the Douglas-fir costume; small, which sells the scale.
- No gore, not kid-coded. Complements the title (Under Oregon, killing trees) without repeating it.
- Minor, non-blocking: the black filled blobs with white bristle tufts in the web (about (380,370), (510,440),
  (960,440), (450,690)) read at full size like ticks/bugs rather than root swellings. Invisible at feed size.
- **VERDICT A: PASS** (optional: illustrator drops the bristle tufts or makes the swellings white like the strands).

### B: "1,350 PITCHES" / "Scientists Found a Fungus Killing Trees Across 965 Hectares"
- Feed size: text readable, red ring and Doug readable. Doug on-model (cap, white head, sweat drop, shock).
- Problems:
  - No fungus anywhere in frame: it is a grey/brown patch of tree-tops in a green canopy. The threat is not
    obvious; it reads as "clearing" or "dead patch", not "a fungus did this".
  - Scale is wrong for the concept: Doug is about 280 px tall, roughly a third of the ring's height, so the
    "town-sized" patch reads as a yard. The concept asked for tiny Doug.
  - "PITCHES" without "football" is ambiguous (baseball pitches, sales pitches, tent pitches); a cold viewer
    cannot decode the number in one second.
- **VERDICT B: FAIL**

### C: "IT'S UNDERNEATH" / "The 2,400-Year-Old Fungus Quietly Killing an Oregon Forest"
- Feed size: text readable; Doug's big head/cap is the focal point; mushroom clusters and dying trees read.
- Doug on-model, calm/deadpan face fits "quietly"; honey mushrooms are recognisable. No gore, not kid-coded.
- Minor, non-blocking: the green "glow under the soil" ellipse reads as a lawn/pond at feed size and is mostly
  hidden by the text; a few faint white root lines running down from the mushrooms into the dark soil would
  sell "underneath" better.
- **VERDICT C: PASS**

### Required fixes
1. **Thumbnail B** (graphic designer): shrink Doug to about 90-110 px tall (head about 40 px) at the ring's
   centre, keeping cap and shock face, so the ring reads as enormous around him.
2. **Thumbnail B** (graphic designer): show the culprit: a few white rhizomorph strands / honey-mushroom clusters
   inside and creeping out past the red ring edge, so "fungus" reads in one second.
3. **Thumbnail B** (graphic designer): replace "1,350 PITCHES" with unambiguous text, e.g. "ONE FUNGUS"
   or "THIS IS ONE FUNGUS" (pairs with the 965-hectare title without repeating the number); if a number is kept,
   it must name the unit ("1,350 FOOTBALL FIELDS" is too long at feed size, so prefer the word option).

VERDICT: FAIL (A PASS, B FAIL, C PASS)

## Thumbnail round 3 (2026-11-13): final check A / B (revised) / C

### A: "ALL ONE THING": unchanged, still reads at 168x94 (cap + white head on orange, white web below, text clear).
- **VERDICT A: PASS**

### B (revised): "1,350 FOOTBALL PITCHES" / "Scientists Found a Fungus Killing Trees Across 965 Hectares"
- Text fix works: the unit is named, spelled right, not cropped, and you can still read it at 168 px (it's thin, but OK).
- The rhizomorph strands now show up inside the ring and run out past it. Fungus fix done at full size.
- Fails at feed size (checked thumbnail_b_small.png at 168x94 and blown up 5x):
  - Doug at ~110 px full size is ~14 px tall in the feed, with a head of ~4 px. He shows up only as a red dot. The
    viewer can't see Doug or his reaction, so the thumbnail has no character and nothing to look at first.
  - The grey dead-crown "snowflakes" read as snowflakes or frost, not dead trees. Together with the black-and-white
    strands, the patch looks like a cracked brown blob. You can't tell in 1 second that a fungus killed this patch.
- Doug size: I'd go with the creative director's ~225 px (at least 200 px, so his head is ~8 px or more in the feed).
  At 110 px he disappears. Don't use Doug's size to show scale. Let the patch show it: push the red ring to bleed off
  the left, right and bottom edges so the patch has no visible end.
- **VERDICT B: FAIL**

### C: "IT'S UNDERNEATH": the glowing green root lines under the soil now sell "underneath" even at feed size. Doug's
head and cap are the focal point and he is on-model. No gore, not kid-coded.
- **VERDICT C: PASS**

### Required fixes (graphic designer)
1. **Thumbnail B**: make Doug ~225 px tall (head ~80 px) at ring centre with the shock face and cap. Keep the dark
   clearing behind him so he stands out.
2. **Thumbnail B**: enlarge the red ring/patch so it bleeds off the left, right and bottom frame edges. Scale comes
   from the patch having no end, not from Doug being tiny.
3. **Thumbnail B**: swap the grey snowflake crowns for solid grey/brown dead-crown blobs (like the canopy circles
   but grey), or remove them. Keep the white rhizomorph strands as the only light linework so "fungus" reads.

VERDICT: FAIL (A PASS, B FAIL, C PASS)

## Thumbnail round 4 (2026-11-13): re-check B after the 3 round-3 fixes

### B: "1,350 FOOTBALL PITCHES" / "Scientists Found a Fungus Killing Trees Across 965 Hectares"
Checked build/thumbnail_b.png (1280x720) and build/thumbnail_b_small.png (168x94, also blown up 5x).
- Fix 1 (Doug ~225 px): **done.** Doug is ~225 px tall with a ~80 px head, centred on the dark clearing. He is
  on-model (red cap, white head, sweat drop, shock face). At feed size the cap and white head are the first thing you see.
- Fix 2 (ring bleeds off the edges): **done.** The brown patch runs off the left, right and bottom edges with no
  visible end, so the scale now comes from the patch. Text is spelled right, not cropped, and readable at 168 px.
- Fix 3 (snowflake crowns): **not done as asked, and it causes a new misread.** The crowns are now solid *black*
  blobs that still have the white bristle tufts on top, and they sit where the strands end. Also, the strands changed
  from white to thick black with a thin white halo, so dark linework now dominates the patch. At full size and in the
  feed, the blobs look like ticks or spiders sitting on a black web or on cracks in the ground. It doesn't read as
  fungus, and a viewer could expect a spider/insect video (a packaging-mismatch risk).
- **VERDICT B: FAIL**

### Required fixes (graphic designer)
1. **Thumbnail B, dead-crown blobs**: remove all the white bristle tufts. Either make the blobs grey-brown
   (e.g. #6b5a48 with a dark outline) so they read as dead tree crowns or stumps, or delete them.
2. **Thumbnail B, rhizomorph strands**: switch back to white-dominant strands (white/cream core about 10-14 px with a
   thin 3-4 px black outline), keeping the current layout. That way the web reads as pale fungus threads, not as
   black cracks or a spider web. Keep everything else (Doug, clearing, ring bleed, text) unchanged.

VERDICT: FAIL (B: Doug and scale fixed; blob tufts and black strands read as spiders/web)

## Thumbnail round 5 (2026-11-13): re-check B after the 2 round-4 fixes

### B: "1,350 FOOTBALL PITCHES" / "Scientists Found a Fungus Killing Trees Across 965 Hectares"
Checked build/thumbnail_b.png (1280x720), a 2x crop around Doug, and build/thumbnail_b_small.png (168x94, blown up 5x).
- Fix 1 (blob tufts): **done.** The bristle tufts and the black crown blobs are gone. All that's left is a small dark
  ring cap on some strand tips. It reads as the cut end of a root or tube, not as a creature, and it is barely
  visible at feed size. No tick/spider read remains.
- Fix 2 (white-dominant strands): **done.** The strands are now a cream core with a thin black outline, in the same
  layout. At full size and in the feed they read as pale fungal threads spreading through the soil, not as cracks or a web.
- Kept from round 4: Doug is on-model and centred on the dark clearing (red cap, white head, sweat drop, shock face),
  and he is the first thing you see at 168 px. The patch bleeds off three edges, so the scale sells the title. The text
  is spelled right, not cropped, and legible small. No gore, not kid-coded, and it matches the title (fungus across a
  huge area).
- Minor, not blocking: at feed size Doug's thin white limbs fade into the clearing, but the cap and head carry him.
- **VERDICT B: PASS**

VERDICT: PASS (B)
