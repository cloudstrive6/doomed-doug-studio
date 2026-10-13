# Visual review: 017-most-disturbing-fungi

## Round 1: keyframes (2026-10-13)

Scope: all 266 keyframes (`build/keyframes/s001–s266.png`, contact sheets `build/contact/sheet_01–23.png`, full-res crops for anything borderline). Note: `python -m studio keyframes` was re-run by another agent while this review was in progress. Everything here is from the finished render (17:17 UTC).

### What's working
- Death counter continuity is correct: 139 at the start, +1 on each of the 8 deaths (s029, s056, s079, s106, s131, s178, s229, s261), 147 at s264. The "Doug is fine" beats (s154, s204) leave it unchanged.
- Doug stays on-model throughout: red cap and white head, readable in every costume (cicada, fly, spider, frog, bat). Costume "eye" baubles don't hide the cap. Doug is missing only where he should be: the s001 cold-open grid, the sober cards, and s262/s263, where the cap-only gag is deliberate.
- The real-victim cards (s099, s152, s168, s192, s223, s243) are sober: flat dark or plain background, white text, no Doug, no counter, no jokes. That's the right tone.
- Deaths are all cartoon: X-eyes, ghost, empty costume. No blood, organs or dismemberment. Nothing reads as a kids' show.
- Creatures are recognisable: cicada, nymph, house fly, orb-weaver, frog, bat, ergot spur, rye, tomb, Douglas fir. Maps read clearly.
- Variety is fine. The repeated compositions (s127–s130 alarm, s262–s263 cap) are deliberate rhythm gags, not stale runs.

### Fixes required

**Text colliding with the death counter (director: composition)**
1. **s015**: "DOESN'T STOP" runs under the DOUG DEATHS box. Move the title left or down (top-left at y ≈ 140, or under the cicada) so it clears the counter by at least 20 px.
2. **s023**: "CAN'T INFECT PEOPLE" overlaps the counter. Shrink it or move it down to about y ≈ 200, centred left of x ≈ 1050.
3. **s024**: "DRESSED AS A CICADA" overlaps the counter. Same fix: move it down or left, or reduce the size.
4. **s141**: "MORE THAN A DOZEN" overlaps the counter ("DOZEN" is cut by the box). Move it to the left half or below the hair strip.
5. **s198**: "ABOUT AS WELL" overlaps the counter. Move it above the bars on the left, or down between the bar tops and the counter.
6. **s157**: "INTO A COUNTY" touches the counter edge (about 0 px gap). Shift it left or down for at least 20 px clearance.

**Text colliding with drawings or the frame edge (director: composition)**
7. **s036**: "BEFORE SUNSET" runs into Doug's head (the final T is hidden). Move Doug further right or down, or move the text left.
8. **s030**: "GETS THE REST" overlaps the yellow sun. Move the sun clear of the text or drop the text below it.
9. **s088**: "MORE THAN HALF" ends about 20 px from the right frame edge, outside title-safe. Pull it in so it sits at least 96 px from the edge (e.g. centre it over the bars).
10. **s061 / s062**: the "GUNPOWDER STORE" label is cut off by the spider ("GUNPOWD…", "GUNPOWDER ST…"). Move the label clear of the spider (e.g. under the ceiling line on the left).
11. **s108**: "WHITE-NOSE SYNDROME" runs into the hanging bat's wing tip. Move the bat left or up, or lower the title.
12. **s125**: "ENDANGERED" overlaps the bottom of the hanging bat. Lower the title by about 60 px or move the bat right.
13. **s206**: "CRYPTOCOCCUS GATTII" runs into the right-hand fir tree. Shrink the title or move that tree out of the title band.
14. **s242**: the "WHO, 2022: CRITICAL PRIORITY" label covers the hospital's roof red-cross sign. Move the label above the roof line or to the left of the building.

**Picture doesn't match narration (director)**
15. **s061**: narration is "a spider coated in white fungus", but the lit spider is a black silhouette with a red halo. Use the white fungus-coated spider asset from s062 here, lit by the beam.
16. **s099**: narration is "greatest recorded loss of biodiversity caused by a disease", but the card repeats s097's "90 SPECIES, PRESUMED EXTINCT". Change the card text to "GREATEST RECORDED LOSS OF BIODIVERSITY TO A DISEASE" and keep the sober style.
17. **s192**: the sober card "10 OF 12 RESEARCHERS DIED" sits under narration about lung infections in weak immune systems, and it states as fact a claim the script hedges ("according to later accounts"). Move this card to s186, worded "ACCORDING TO LATER ACCOUNTS: 10 OF ~12 DIED". Give s192 a lung or spore visual instead (e.g. spores drifting toward a pair of lungs, or a "WEAK IMMUNE SYSTEMS" label).
18. **s097**: 8 of 20 frog silhouettes are crossed out (40%), but 90 of 501 is about 18%. Cross out 4 of 20 (or 2 of 10). As drawn, the visual overstates the stat.

**Possible gore read (art director: style)**
19. **s047, s061, s257**: the "menace" effect is red speckle sprayed around a black silhouette. On s257 (black blob on the brick wall) it reads as blood spatter. Swap the red stipple for a dark grey or purple glow, or the plain warning-icon treatment, everywhere this effect is used.

**Drawing / clarity (illustrator / director)**
20. **s210 / s211** (illustrator): the "porpoise" is drawn as a fish (salmon shape), and the narration also names ferrets, which aren't shown. Replace the fish with a porpoise (dorsal fin, tail flukes, blunt snout) and add a ferret (or at least fix the porpoise).
21. **s249** (director): the horse is drawn on top of the cat, making a tangled shape. Space them apart (cat left, horse right, about 150 px gap).
22. **s167** (director): the 370-hospitals grid is pasted over the village huts, so the buildings overlap. Drop the huts from this shot (plain ground) so the grid reads cleanly.
23. **s234** (director): the "footnote: new yeast" text on the paper is about 18 px tall and unreadable at feed size. Make it a large label (≥ 36 px), or circle the footnote line with a separate "FOOTNOTE" label.

### Advisory (not blocking)
- s007: the red arrow sweeping in from the Atlantic onto the eastern US implies something arriving from overseas, which isn't what the line is about (years underground). Consider dropping it or swapping in a "brood region" circle.
- s002: "STARTED ON PEOPLE" has no person in shot. A small "PEOPLE" silhouette would make the line land.

VERDICT: FAIL
