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
