# 039 decisions

## 2026-11-08 Script gate (draft 4): APPROVED
- Screener PASS (draft 4, 0 fact errors, policy 0 items, 2,076 words, about 10.7 min).
- Against brief: 9 items on the kinship axis in brief order, with all four spoken bands. Item 1 is named by word 34 and its twist lands at about word 122. The payoff promise is sentence two, and the boss delivers it. Seven deaths (302-308) and two survivals (Monkey Hunt, Bonobo), as briefed. "Doug did not agree to this.", "cousin?", "hi friend?", "wait" and the costume logic line are each used once. One 011 callback sentence, with no strength, 8-to-1 or 150+ facts repeated.
- Deviations are all fact-driven and documented (spear "probably started with the females", not "invented"; fruit tree, not fig; scarce food cut from Foudouko). Accepted.
- Gore/kids: every death cuts to black before contact. No body, cannibalism or injury detail. Infants are mentioned only as "the smallest". No "civil war". Human attacks are given as counts only, with none fatal. The honesty line is limited to the IUCN status.
- Notes for downstream (non-blocking): the director keeps the s137 "young chimp knocked into the air" beat cartoon-light. The FAMILY TREE values come from facts.md only. Titler: the title is still the CD pick or one of the brief's allowed leads. "Kill" is honest per item, and line 171 states the scientific sense of "relative".

## 2026-11-08 Director: shotlist
- 208 shots (s001 thumbnail), 9 chapters, all 2,076 spoken words in order, Doug in 80% of shots, no shot over 45 words, every shot gets a new element at least every ~4.4 s at 195 wpm.
- FAMILY TREE sign is a HUD next to the counter (cream board x 1090-1228, y 98-266; red dot climbs one twig per item, red ring from The Old King) plus a `SPLIT: ...` label right-aligned at x 1814, y 238. Values are exactly the facts.md set (more than 60 / about 25-30 / about 8-10 / about 6-7 / about 1-2 million years ago, SAME SPECIES x2, SAME GROUP x2); the label is stamped red from s204 (death 308) to the end.
- Gorilla charge (s059-s061, CD note): the silverback charges (shake), a small chimp *silhouette* tumbles through the air with motion dashes, no contact and no landing; then the ring of nine male silhouettes. No young gorilla is drawn anywhere.
- Every death is a cut to a near-black frame with only the cap (hollow lip, fruit tree, maize sack, ridge, nest, crown, chalk line); the field guide NO lands on the next shot (CHIMPANZEE page, 3 stamps per row, MAYBE at s113, smudged from s133, sticky RELATED. at s206).
- Item 9 infant victims appear only as the text "17 OF THE SMALLEST." on a plain sober card (s190), no Doug, no drawing. Endangered card s199 has no HUD and no Doug.
- Shorts: short01 The Gorilla s059-s073 (+ spoken hook "In twenty nineteen, chimpanzees were first recorded killing gorillas." over s052), short02 The Neighbours s138-s149 (ends "It was real estate."), short03 The Split s182-s191 (ends "friendly terms for years"). Titles/descriptions left to the titler.

## 2026-11-08 Director: keyframe round 1 fixes applied (art_review + visual_review)
Edited shotlist.json directly (fur_legs and s091 changes kept). 54 shots re-rendered, `validate shotlist` OK. s001 is left to the graphic designer.
- Split line through Doug (s003, s004, s200-s202): the line now runs only on the ground, starting 40 px below his feet. In s122 the line stops 40 px above his cap and Doug is raised (feet at about y 995).
- BONOBO tag (s111-s113): moved off his face onto his lap and chest. In s111 Doug and the costume are at 0.6 and the red arrow ends on the tag.
- Maps (s029, s051, s085, s086, s103): `africa_map` is now 0.8 at x 600, so the frame's right edge is at about x 960. The pins, labels and the s103 arrow moved with it.
- Text against the HUD panel: s131, s160, s174 and s183 moved to y 340-345. s162 EXILED is at (760, 380). s145 bars are rescaled (37 at y 362, still in proportion to 15).
- Chalkboard run: s170 is now a 5-calendar exile timeline (THIS LONG) with no board. s172 is the night set, with three young males facing Foudouko, a "!", FIERCE, and Doug in costume.
- Labels cut by lines: s005 title moved to clear sky (1150, 520). s157 title moved to (860, 370). In s077-s079 the branches end below the labels, with Doug lifted clear of HUMAN. In s196-s198, SAME GROUP is a cream-boxed label right of the trunk top, and the s198 arrow is retargeted. The stamped box in s204 moved clear of the trunk.
- s064/s062: added a small `silverback_gorilla` (0.4) at x 1540. THE SMALLEST plus a red arrow point at it in s064, and the "?" sits over it in s062.
- s099: ACROSS A RIVER moved to empty space at (1400, 560), and a blue river band now runs along the ground strip.
- s031: wordart moved to x 1180 and Doug to x 1650.
- s067: re-staged with no asset change. The tree is at 600, the chimp at 200 and the gorilla at 1050 (0.5). The elephant is now 0.85 in its own space on the right, about 1.4 times the gorilla's height, with its own arrow to the tree.
- s194/s195: Kasakela and Kahama heads are larger, with pale backing discs. The dark discs are gone, and each Kahama head gets a red X in turn in s194 ("one by one"); all are X'd in s195. The labels share y 845 and THE FOUR-YEAR WAR moved up (955).
- s182-s186: every chimp head has a pale backing disc, and the s184-s186 dots are now head icons (0.18).
- Variety: s041 is now a branch of 9 colobus with 8 red Xs (89%), FIRST RECORDED and Doug. s045 is a 1.8x push-in on Doug and the three colobus males.
- Smaller fixes: in s046 Doug sits alone and sad (no lone cap). In s042 SAFEST SPOT and in s132 WRONG SIDE moved into clear sky. In s054 the tallies and 2014-2018 moved into the sky right of the tree. In s087 PATHS was dropped. In s100/s101 there are now small BONOBO labels. In s009 YOUR ARM sits at Doug's pointing hand. s174's paper crown is now 0.5. s012's "?" shifted up and left. In s018 Doug is at x 1180 (0.36) with the spear carriers moved right.
- Kept as designed: s199 endangered card with no caption bar or HUD (a deliberate sombre card, see the shotlist decision above). s044 is unchanged because the s045 push-in breaks the branch run.

## 2026-11-08 Creative director: thumbnail gate (A/B/C)
No thumbnail screener report exists yet (visual_review defers s001 and `thumbnail_b`/`_c` to the post-render round), so this is a provisional decision: each thumbnail still has to pass the visual screener at feed size.
- **A `thumbnail.png`: APPROVED.** The brief's hero, read at feed size: one huge male chimp with hair on end, a bitten spear that points up and touches nothing, tiny Doug in costume with the cap on top, and "HE'S FAMILY" (no title word). The sunburst frames the threat. I'd click it. It's also the s001 opening image.
- **B `thumbnail_b.png`: APPROVED WITH ONE MUST-FIX.**
  1. The small quadruped chimp in the middle reads as a juvenile/baby at feed size, and the brief says "never a baby chimp". Scale it to adult size (similar to the left chimp) or remove it. Keep the spear's gap from Doug's head at least as wide as it is now (no contact).
- **C `thumbnail_c.png`: REJECTED (not a click as it stands).** Four neutral animals standing still: no threat, and no gap.
  1. Use the style bible 2A grammar: 6 tiles (2x3) on white, with the chapter names as labels in the bible's comic font, ending on THE SPLIT.
  2. The BONOBO tile is a black blob at `_small` size. Lighten the face, or give it a lighter tile colour so it reads.
  3. The BUSHBABY's eyes read as sunglasses (meme/kid tone). Draw open, round, reflective eyes.
  4. The last tile needs stakes: Doug between two chimps facing opposite ways (the split), with the red split line on the ground (not through Doug) and a red "?" or arrow on Doug.
  5. Re-run `_small` and send it to the visual screener.

## 2026-11-08 Director: keyframe round 2 fixes applied (art_review round 2 + visual_review round-2 leftovers)
Edited shotlist.json directly. Narration, splits and shorts ranges are unchanged. Re-rendered s077, s140, s143, s183, s185, s186 and s204 only. `validate shotlist` and `shorts validate` both OK. Thumbnail files were not touched.
- s140 (blob run s138-s143): re-staged as a day scene. A line of 4 knuckle-walking `chimpanzee` crosses a dashed boundary from green NGOGO ground onto the dark northeast ground. The lead chimp pops in at 0.3, a red curved arrow points onward, Doug (shock) stands on the dark side, and "2009" sits in clear sky at (620, 440).
- s143: 1.8x push-in (group, as in s045) on shocked Doug with the "!". The pitch grid is dropped, and only the edge of the grown blob shows for context.
- s185 (crowd run s182-s186): re-staged as two detailed `chimpanzee_sitting` (0.75) turned away from each other at x 560 (flipped) and 1360, with a wide gap. "2015" sits in the sky, and the "?" and Doug in costume (shrug, confused) are in the gap. This differs from s191, where the chimps face each other across the dashed line.
- s183 and s186: Doug and the costume are raised 40 px (y 957 and 980). His feet are now at about y 1003 and 1020, which is inside the y 1040 limit. In s186 he is still between WESTERN and CENTRAL.
- s204: the SAME GROUP stamp box moved 17 px right (x 847), so it is about 31 px clear of the trunk.
- s077: the "!" moved from the empty space to the right of the CHIMP/HUMAN fork (1150, 720).
- s009 arm: not done. The locked rig's `point` arm is about 120 x scale long, so a 600 px arm under the ruler would need a scale of about 5 or an off-model arm. That is the art director's call (a new pose). YOUR ARM stays beside the pointing hand.
