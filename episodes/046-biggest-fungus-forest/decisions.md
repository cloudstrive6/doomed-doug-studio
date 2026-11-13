# 046 decisions

## 2026-11-13, creative director: script approval (draft 2)
- Read: brief.md, script.md (draft 2), script_review.md round 2 (PASS, 0 fact errors, 8/8/8), facts.md (Malheur age, Pando wording, tyre analogy).
- Approved. The axis holds (inside something, under the ground, under a forest), every item opens on its hook, the honesty line (Shark Bay seagrass)
  keeps the title promise exact ("biggest fungus ever found"), item 3 stays a tape-measure gag with no anatomy and no food-safety or medical advice,
  and the costumes play deadpan.
- One edit made (the screener's optional polish): the payoff promise in sentence 2 was vague ("one fungus eating a whole forest"). It now reads "By the
  end, Doug is standing on one fungus bigger than a thousand football pitches, and it has been eating that forest for thousands of years." (Sourced:
  965 ha is about 1,350 pitches, and the age is at least 2,400 years per Guinness and Ferguson et al. 2003.) Adds about 13 words, still inside the target length.
- Kept "It doesn't need sunlight. It has a vine." It is set up for the dodder's "It has a tomato." and it's the better joke; item 1's density is acceptable.
- Series bible: counter total 356, 046 log row added, deaths 353 and 356 noted as played flat.
SCRIPT: APPROVED

## 2026-11-13, director: shotlist (184 shots), asset requests, Shorts
- Shotlist: 184 shots, narration matches the approved script word-for-word (2,015 spoken words), Doug in 68% of shots, and no
  build-free stretch over about 4.6 s by estimate. Generator: `build/gen_shotlist.py` (git-ignored scratch, as in 045).
- HUD: DOUG DEATHS top right, plus the HOW BIG meter (a `label` at (1600, 238) with `tape_measure` at 0.17). It is unspoken, from s005
  (1 M) to the boss (ABOUT 965 HECTARES, stamped red from the boss title card on).
- Overgrowth deaths: death 354 uses `doug_fuzz_silhouette` (its single use this episode, art bible rule). Death 355 uses a new,
  separate drawing, `pine_costume_fuzz` (the pine costume overgrown, a faint foxfire glow, cap on top), so the fuzz silhouette is not
  used twice. The other deaths: 351 is the flat tomato suit in dodder threads plus the cap and the AGAIN stamp; 352 is a black card
  with the handset, the cap and ghost Doug; 353 is the cap on the bitten aspen sprout (flat); 356 is the fallen Douglas-fir suit with
  the cap in the honey mushrooms (flat).
- Item 3 has no worm drawing at all (brief sec 7). The tape measure, the bus and the calendar carry it.
- Section headers "Under the ground." / "Under a forest." are white header cards with `topbar: false`. "INSIDE SOMETHING." is shown
  above the item 1 title, unspoken.
- Shorts (`shorts.json`): short01 Pando (s097-s108 + hook), short02 Cable-Cutting Tree (s080-s089 + hook), short03 Blue Mountains
  (s173-s181 + hook). Each ends on its Doug beat. **The titles are working placeholders** (the validator needs a non-empty title),
  and the youtube-titler owns the final titles and descriptions.

## 2026-11-13, creative director: thumbnail gate (packaging variants A/B/C)
- Read: metadata.json packaging.variants, build/thumbnail.png, thumbnail_b.png, thumbnail_c.png (plus the _small feed-size renders).
  visual_review.md has no thumbnail-specific pass yet, so the visual-screener still needs to clear the final three after these fixes.

**A: "A Fungus Under Oregon Has Been Killing Trees for 2,400 Years" / ALL ONE THING: APPROVE.**
The white bootlace web under a thin strip of dead conifers is the strongest image of the three, and "ALL ONE THING" adds a new
idea to the title rather than repeating it. Panicked Doug in the fir costume reads at feed size. Optional polish, not blocking:
the black blobs with white tufts in the web don't read as anything. Either make them small honey-mushroom knots or remove them.

**B: "Scientists Found a Fungus Killing Trees Across 965 Hectares" / 1,350 PITCHES: REVISE.**
1. The dead patch looks like grey and brown cobblestones, worst at feed size (_small). Draw the dead trees as bare grey spiky
   crowns or snags seen from above, so the patch reads as dead forest, not gravel.
2. Nothing in the frame says fungus. Let the white rhizomorph web show through the gaps inside the red outline, or put a ring of
   honey mushrooms round Doug's feet. The subject of the title has to be visible.
3. "PITCHES" is ambiguous for a US-heavy feed (sales or baseball pitches). Change it to "BIGGER THAN A TOWN" or "1,350 FOOTBALL
   PITCHES" if it fits on one line at the current size. Don't use "FOOTBALL FIELDS" with 1,350, because the number is for
   soccer pitches.
4. Make Doug about 30% smaller and drop the grey shadow ellipse. The concept is scale, and at the moment he fills a third of the patch.

**C: "The 2,400-Year-Old Fungus Quietly Killing an Oregon Forest" / IT'S UNDERNEATH: REVISE.**
1. The "glow under the soil" is a flat green ellipse that reads as a pond or rug. Replace it with a faint foxfire-green web of
   rhizomorphs branching through the brown soil band below the mushrooms (thin glowing lines running off the left and right
   edges), so "IT'S UNDERNEATH" points at something visible.
2. Let the text bar sit over the glowing web, not over plain brown soil, so the eye goes from text to threat.
3. Keep deadpan Doug and the honey mushrooms, which are good. Optionally darken the purple sky a step toward dusk so the glow carries.

PACKAGE THUMBNAILS: A APPROVED; B, C REVISE (send back to graphic-designer)

## 2026-11-13, creative director: thumbnail gate, round 2 (B and C re-renders)
**C: APPROVE.** The glowing green web through the soil, running off both edges, now makes "IT'S UNDERNEATH" point at something
real. The darker sky helps. Deadpan Doug over the threat is the joke.

**B: REVISE (round 2).** The dead snags and the visible web fix the gravel problem, but at feed size (_small) the patch is now noise,
and Doug is lost in it.
1. Clear a small bare-soil disc (no snags, no web) round Doug, and bring him back up to about 0.5 so the cap and face read at 168 px.
2. Thin the snags by about a third, and keep the web as the dominant shape inside the outline.
3. Text: "PITCHES" stays ambiguous. Decision: thumb_text becomes "1,350 FOOTBALL PITCHES" (3 words, passes `package check`). Per D4 the
   youtube-titler changes that candidate's thumb_text in metadata.json and re-runs `package 046-biggest-fungus-forest rank`. Then the
   designer swaps the text at about 95 px. B is not approved until both are done.

**A:** approved as is. The black fans are part of the `rhizomorph_web` silhouette, and fixing them would mean an edit to the library
asset. That isn't worth it for this episode.

PACKAGE THUMBNAILS: A, C APPROVED; B REVISE (designer: layout; titler: thumb_text "1,350 FOOTBALL PITCHES" + re-rank)

## 2026-11-13, creative director: thumbnail gate, round 3 (B layout)
- **B layout: APPROVED.** The bare-soil disc puts Doug's cap and face on a clean spot at 168 px, the web is the main shape, and the
  red outline still says "this whole area". The only thing left is the text.
- **B overall: still REVISE**, because the text must change to "1,350 FOOTBALL PITCHES". It is waiting on the youtube-titler, who
  edits thumb_text and re-runs `package 046-biggest-fungus-forest rank`. Then the designer swaps the text at about 95 px and re-renders.
  Once that is done and `package check` prints OK, B is approved. A layout pass is not needed.

## 2026-11-13, creative director: thumbnail gate, round 4 (B text + Doug size)
- **B: APPROVED.** The text "1,350 FOOTBALL PITCHES" fits on one line, is clear at 168 px, and is no longer ambiguous. `package check` prints OK.
- **Doug size:** I accept about 110 px instead of the ~225 px I asked for in round 2, following the visual-screener. B sells scale, so a
  small Doug on the bare-soil disc is the point. At 168 px his face doesn't read, but the red cap does, as a clear speck in the clean
  spot at the centre of the patch, and that is enough for this concept. A and C carry the readable-face Doug.

PACKAGE THUMBNAILS: A, B, C APPROVED
- 2026-11-13: packaged. Script 2 rounds (screener FAIL on hook/facts, then PASS); art 3 rounds (map border + label overlaps); thumbnails 5 rounds (B redrawn repeatedly; CD and screener disagreed on Doug size, final B follows screener's fixes, Doug ~225px). Risk: weakest proven-outlier evidence in recent briefs; no-'Doug' title experiment, readout day 7. Optional unaddressed: balance-scale tilt s097/s127, black blobs in rhizomorph_web drawing.
