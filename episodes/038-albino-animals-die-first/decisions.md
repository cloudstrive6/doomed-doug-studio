# 038 decisions

## 2026-11-05: script gate (draft 2): GO
Creative director. Read script.md (draft 2 + R1/R2), script_review.md (re-screen), facts.md, brief.md.

- Screener's two blockers are closed: R1 aircraft 610 m now sourced (facts.md, Queensland ministerial statement 85169, 2018);
  R2 narration reads "about two point six billion letters", matching the label and the "more than eighty years" maths.
- Everything else passed the re-screen: facts 40+ re-verified, opening 8/10, structure 8/10, voice 8/10, policy PASS, 1,999 words (~10.3 min).
- Why I'd click and keep watching: concrete death-and-number first sentence, payoff promise at ~0:09, item 1 name at word 33 and a real twist
  (uncle/niece genome) by ~0:36; a clean time-left axis from decades to about a day, with the fence/law/zoo thread giving every item a reason
  to lead into the next. The title's "First" is backed by four attributed sources (SC Aquarium 24 h, BTO, Missouri DoC, Smithsonian).
- Brief deviations accepted (all fact-driven): "Day one." band instead of "Minutes."; cats not hawks at Olney; Turner thesis for the lions;
  Migaloo "points to a true albino", last reported 2020, never "alive today".

Notes carried downstream (not blocking):
1. Director: Claude's shot must not imply a whole life in San Francisco (he lived at St. Augustine first; 17 years at the museum). Keep "1995 TO 2025" label only.
2. Director/illustrator: kid-appeal risk is HIGH on white baby animals. No big cute eyes, no pastel, hatchlings drawn in the channel's plain style; sunburn only as costume colour.
3. Editor: if item 1 runs long in timing, "all afternoon" in the Doug beat is the first cut.
4. Series bible: deaths 295-301 (300 played flat) get logged at final approval, per the usual pattern.

## 2026-11-05: shotlist (director)
184 shots, every spoken word once and in order (checked word by word against script.md), Doug in 142/184 (77%), 8 chapters.
- **HUD:** `DOUG DEATHS` 294 to 301 plus the episode's TIME LEFT sign as a wood-fill label under it (blank in the cold open, then DECADES, YEARS, "?", ABOUT A DAY; red text from death 301). No exact numbers on the sign.
- **Death grammar:** every death is a cut to black (`#0b0f14`) with the counter ticking, the WHITE ANIMALS field guide page getting its new line in red (older lines drawn as grey pencil scribbles to keep on-screen words at 8 or fewer) and ghost Doug floating up. No dead Doug bodies and no predation on screen. The cap is shown alone afterwards (deck chair, grass, swamp).
- **CD notes applied:** Claude's shots show "1995 TO 2025" and "behind glass" only, with the Louisiana farm on a map. There is no San Francisco map and no "whole life there" visual. The sunburn gag is three colour versions of the gorilla suit (white, pink, red); Doug's face is never sunburned (no `sunburn` gear). Snowflake's eyes are pale blue. Every new animal request says: no big cute eyes, no pastel, unsmiling, pink eyes only on true albinos.
- **Skittles line:** shown as five plain candy dots, with no brand name or logo on screen.
- **Survival (Migaloo):** no field guide stamp. The narrator's pencil taps the WHITE WHALE line.
- **Shorts:** short01 s160-s172 (the boss: 24 hours, ending "almost never gets to grow up outside a zoo"), short02 s050-s058 (white lions, ending on the hunting study), short03 s096-s100 (the $750 squirrel fine, ending on the bottle-of-water line). Titles are left blank for the titler.
- **Thumbnail:** s001 is `scene_ref: thumbnail`, so `thumbnail.json` is still needed from the graphic designer.

## 2026-11-05: thumbnail gate (A/B/C): A CHANGES, B APPROVE, C CHANGES
Creative director. Read metadata.json (title "Why Nature Kills Albino Animals First, Then Doug", thumbnail_brief), visual_review.md
round 1 (A PASS, B PASS, C FAIL), the round 3 thumbnail.json/test diffs, and looked at all three PNGs at 1280x720 and 168x94.
Rendered 18:32, after art round 3. Screener's C fix 4 is applied (the lioness is now full-body on gold, so no polar-bear read). The A heron
was moved down and enlarged. There has been no visual-screener re-check since then, so this verdict is mine alone.

Shared checks: none of the three reads as being about people, and none uses the forbidden words. There is no gore and no fluffy baby animal.
Doug is on-model with the red cap readable at feed size in A and B.

### B (`thumbnail_b.png`, "SPOTTED"): APPROVE. Recommended as the primary test slot.
This is the clearest version of the episode's thesis at feed size. The heron's beak points straight at the glowing white "hatchling" (Doug),
and the normal dark hatchling goes unnoticed. The picture shows *why* white dies first, and the title adds the "then Doug" turn. The tone
is adult-coded (a predator's eye view, Doug's shock), not cute. I'd click it.
Advisory, not blocking: at 168x94 the dark hatchling still reads a little like a striped caterpillar. If the designer takes another
pass, scale it up about 1.3x and sink its belly into the waterline.

### A (`thumbnail.png`, "NO HIDING"): CHANGES (small)
The giant pink-eyed white jaw is a strong stop. The changes:
1. **Move the text clear of the duration badge.** "NO HIDING" runs to x≈1115 with its baseline at y≈665, so the "NG" sits under YouTube's
   bottom-right timestamp and progress bar. Move it up to a baseline around y 600 and left (or centre it under the jaw, between x≈470 and
   x≈1010) so the whole word survives the overlay.
2. **Make the heron read as a bird, or cut it.** At 168x94 it is still a black hook inside a red speckled blob. The red spray halo around a pointed
   beak reads as a blood splash at feed size, which is the wrong signal for advertisers. Swap the red halo for the yellow or white glow used
   on Doug, and show the eye and the beak tip clearly (B's heron drawing reads well). If it still doesn't read, drop it. The jaw carries the
   threat on its own.
3. (Story note) With the heron unclear, the albino animal is the *predator* in this picture, which works against "Nature Kills Albino
   Animals First". Fix 2 is what restores "the white one is being seen". Don't change the jaw.

### C (`thumbnail_c.png`, grid): CHANGES
The lioness fix landed. As a whole, though, it reads as a flat animal flashcard set: three calm white animals on purple, orange and navy, and only one
panel with any danger in it. With no labels, that is the most kid-coded package of the three, and it gives a viewer no reason to click.
1. **Put death pressure in every panel**, one cue each and no gore. Gorilla: a hard sun disc and glare in the corner (the sun is what killed
   Snowflake). Lioness: dark lion or hunter silhouettes in the tall grass, or her body standing out bright against a dusk savanna.
   Squirrel: a cat silhouette or cat eyes in the dark behind it. Keep the gator and Doug panel as it is.
2. **Gorilla face**: the pink, flat face with blue eyes and brows reads half-human at full size. Darken the face edges, widen the nostrils and the
   muzzle, add a heavier brow ridge, and drop the eyebrow strokes so it is unmistakably an ape. A white humanoid in an "albino ... die
   first" thumbnail is exactly the people-read we must avoid.
3. **Squirrel**: drop the raised "begging" paws pose, which is the cute read. Use a side-on alert crouch with the same pink eye.
4. Optional: mute the purple and navy fields toward the episode's night/swamp darks, so the grid feels like a horror ToC rather than
   a nursery palette.
C re-enters the test only after a visual-screener re-check of fixes 1 to 3.

Routing: graphic designer applies A fixes 1-2 and C fixes 1-3. The visual screener re-checks A and C at 1280x720 and 168x94. If A is not
fixed before packaging, ship B as `thumbnail.png`.
- 2026-11-05: script 3 drafts (2 screener rounds + CD), art 3 rounds + thumbnail 3 rounds (C swapped gorilla tile for deer), 11.0 min. Risks: albinism-of-people framing avoided; kid-appeal on white animals; thumbnail C weaker.
