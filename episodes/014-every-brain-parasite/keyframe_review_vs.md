# 014 Every Brain Parasite: keyframe visual screen (visual-screener)

## Round 1 (2026-10-11), keyframes s001-s256, 22 contact sheets + spot checks at 1080p

Scope: cropping, legibility, invisible elements, Doug on-model, broken drawings, gore/kid-appeal, variety.

Overall the episode is clean. Doug stays on model through all costume phases (killifish, ant, sheep), the counter runs
114 -> 121 without errors (the s167 119 -> s168 "sigh" 118 gag reads correctly), all deaths are cartoon (X eyes, cap off,
ghost), and there is no gore or kids-show tone. Medical diagrams (grey heads/bodies, cysts as pale circles) stay
schematic. Section cards (STEERS YOU. / LIVES IN YOU. / EATS YOU.) are white per art bible, item cards red.
The fixes below block the gate.

### Required fixes

1. **s223 (director + illustrator): the mandrill is invisible.** The 1986 San Diego mandrill is a dark silhouette under a
   dark-red speckle disc on the near-black Balamuthia background; at 1080p only a red-noise circle is visible, so the key
   subject of the shot is not readable at all. Use the colour `mandrill` asset (as in s227) at the same position with no
   speckle disc, or, if a "mystery" look is wanted, a mid-grey `#8a8a8a` silhouette with a white outline (auto-ink) and
   no spray. Keep the "?" .
2. **s194 (director / art director): speckle spray drawn over Doug, so he's off model.** The dark circular spray behind
   Doug on the "EATS YOU." card is rendered on top of him: his white head, cap and brim are covered in dark noise, so he
   looks dirty/textured, and the disc itself is invisible against `#5c1a26`. Put the spray layer below Doug in the
   z-order, or drop it. Doug's head must be clean white.
3. **s156 (illustrator / director): scale contradicts the label.** The ~1 cm larva is drawn over a 0-30 cm ruler, where it
   spans about 13 cm, while the label says "ABOUT 1 cm". Replace with a short 0-3 cm (or 0-2 cm) ruler scaled so the larva
   covers 1 cm, or shrink the larva to one major tick. (Optional, same idea: s151 "5 cm / 4 YEARS" over a 30 cm ruler,
   so highlight 0-5 cm with a red bracket.)
4. **s246 (director): "155" wordart crosses the US map land mass** (glyph bottoms sit on the northern border /
   Montana-Dakotas). Art bible: wordart must not cross map frames or land. Shrink the map to about 0.85 and move it down, or
   move "155" into the clear left margin (about x 300, y 520).
5. **s132 (director): "30%" wordart sits inside the map frame** on the Antarctica ice edge. Shrink and raise the map
   (about 0.85) and put "30%" in the freed strip below the frame, or in the right margin outside the frame.
6. **s221 (director): "the dirt" is invisible.** The arrow points at a dark speckle patch on the dark brown ground that
   can't be seen at 1080p. Add a white `label` "DIRT" at the arrow tail, or use a lighter soil mound (`compost_heap` /
   lighter `#7a5a3a` patch) under the arrow.
7. **s067-s070 (director): run of 4 near-identical compositions.** Same grey sheep-head diagram, same position, only the
   cyst size/label changes (and it returns in s072, s073). Break the run: e.g. make s069 the golf ball / ruler scale
   comparison without the head, or push in to a cyst close-up, or show Doug-in-sheep-costume holding his head for s068.

### Minor (fix if touching the shot anyway)

8. **s189 (director):** "MORE CASES" wordart bottom is at about y 1048, outside the y ≤ 1040 safe area. Raise it about 20 px
   or shrink the map 0.9.
9. **s218 (director):** "Doug affectionately pats a horse", but Doug's hand stops about 60 px short of the horse. Move Doug
   right or the horse left so the hand touches the neck/shoulder.
10. **s250 (director):** the "TINY SCRATCH" arrow tip lands on the cap brim, not the back of the hand. Retarget the arrow to
    the raised hand (about 15 px lower and further left) and add a small red scratch line on the hand.
11. **s164 (director):** the worm-with-suitcase sits outside the head outline (behind the skull). Move it about 30 px
    right so it's inside the head, since the narration says it's strolling across his head.
12. **s104 (director):** the "STIFF NECK" arrow points at Doug's face. Retarget it to the neck.
13. **s047 (director):** the night/morning split line runs under the left edge of the counter box. Shift the split to
    x ≤ 1280 or start the right panel below y 260.

### Checked and OK
- Doug costumes (s024-s029 killifish, s030-s060 ant, s061-s085 sheep) are recognisable, and cap/white head are kept.
- Recognisability: heron, horn snail, ant, cow, sheep, sheepdog, rat, slug, frog, crab, shrimp, cat, horse, amoeba,
  mandrill (s227), ruler/fingernail and maps all read at a glance.
- Death beats s028, s059, s084, s141, s193, s220, s252 are cartoon (X eyes, cap off, ghost). There's no blood. s141 has
  the cause inset and no gore.
- Text: spelling correct across labels (NEUROCYSTICERCOSIS, HALICEPHALOBUS, BALAMUTHIA MANDRILLARIS, GNATHOSTOMA). There's
  no cropping, and the counter zone is clear on all title cards.
- Tone: adult deadpan, no nursery framing; "vegetarian" sign (s139-s140) is legible at 1080p.

VISUAL: FAIL. Required fixes are s223, s194, s156, s246, s132, s221 and s067-s070 (items 1-7). Items 8-13 are minor.

## Fixes round 1 (director, 2026-10-11)

All changes are in `shotlist.json`, with narration unchanged. The listed shots were re-rendered and checked, and `validate shotlist` passes.
- **s223, s194, s018 (art director):** verified. The mandrill/heron glow spray now sits behind the black silhouette, so the mandrill reads as a solid shape on the red disc. Doug's head in s194 is clean white.
- **s156:** replaced the 30 cm ruler with a drawn 0-3 cm ruler (1 cm = 260 px). The larva spans exactly 0-1 cm under a red bracket, with "ABOUT 1 cm" beneath. **s151** (optional): added a red bracket over 0-5 cm and moved the label above it.
- **s246:** shrank the US map to 0.9 and moved it to y 610. "155" now sits clear above the land.
- **s132:** shrank the world map to 0.7 and moved it to y 560, with the circles rescaled to match. "30%" is now below the frame at y 950.
- **s221:** the dirt is now a lighter brown soil patch (#8a6a45) with speckle, the red arrow is retargeted, and a white "DIRT" label sits at the tail.
- **s067-s073:** broke up the run. s069 is now a cyst close-up with no head (big cyst, a slow zoom_in 1.06, a dashed 5-6 cm line and the label, with sheep-Doug in shock). s070 is a scale comparison with no head (cyst > golf ball at the true ~5.5 : 4.3 ratio, plus labels and "BIGGER"). The sheep-head diagram now appears in s067-s068 and s072-s073 only, with the pasture shot s071 between them.
- **Minor:** s189 "MORE CASES" raised to y 998. s218 Doug moved to x 990 so his hand touches the horse (the speech bubble moved with him). s250 arrow now points to the raised hand, with a small red scratch line. s164 worm moved inside the head (x 640). s104 arrow now points to the neck. s047 day/night split moved to x 1280, left of the counter box.
- **AD advisory s118-s126:** s120 ("something else entirely") is now a big shocked Doug reaction close-up with "!" and "SOMETHING ELSE", which breaks up the grey diagram run.
