# 024-moose-deadlier-than-bears: decisions

## 2026-10-21: episode pick and brief (creative director)
- Picked backlog #52 moose (7.2), the ep 024 `animals` candidate from the 10-18 memo and my 10-18 decisions. It is the top eligible idea:
  #45 (7.1) is too close to 021's orca frame, #33 (6.9) is crowded and follows 023's era axis, #38 (6.8) is `places` (Own 4) right after
  020, and #40 (6.7) has a weak engine.
- Engine: OctoLab "Walruses Are Terrifying... Here's Why" 2.54M (41.9x) and the polar bear video 2.87M (47.4x). Demand 10 (clean), 0
  format-phrase copies.
- Row #52 had been dropped from `data/ideas.md` by mistake in the 022 brief commit (45e0493). Restored from 0658b6b and marked in-production.
- Formula: "Why X Is Deadlier Than Y" (T9 family). No T1 (2 strikes, 3rd pending) and no T2 (dropped) wording.
- New axis for the channel: severity measured against a bear, in three bands. Episode-only BEAR / MOOSE scoreboard (ends BEAR 5, MOOSE 11).
- Main risks: safety advice (none allowed anywhere) and over-claiming "deadlier" (ADF&G's exact wording, the honesty line in the boss,
  road deaths as sourced numbers only).
- Variety: 021-024 are four single-animal episodes in a row, so the next pick should be a list episode or the prehistoric compilation.
- The stage stays `idea`. The series bible will be updated when the script is approved (counter 195 to 203, the scoreboard, death 200 flat).

## 2026-10-21: script gate, draft 3 (creative director): CHANGES REQUESTED, stage stays `scripted`
The screener passed draft 3, and the script mostly delivers the brief: the title promise is in the first sentence, "The Deer." comes at
words 29-30, the twist lands by about 0:41, there are three spoken bands, 11 items, deaths 196-203 with death 200 flat, no safety tips,
ADF&G's exact injury wording, the honesty line is in the boss, both sober cards have no names, and the length is 3,037 words. Two on-screen
or internal errors would draw "the video is wrong" comments and hurt the credibility of an episode whose whole pitch is about evidence.
They have to be fixed before approval. Both are wording-only fixes and need no new research.

Required:
1. **The Wolves, the arithmetic doesn't add up (lines 330-338).** The narration and card say "77 TESTED, 6 KILLED", but the next card
   says RAN 41 / KILLED 5 and STOOD 36 / KILLED 0. 41 + 36 = 77, but 5 + 0 = 5, not 6. Mech's summary doesn't explain the sixth kill
   in the ran/stood split. Fix: remove the total-kills figure. Change the sentence to "...holding them at bay or chasing them for long
   distances." (end it there) and the card label to "77 TESTED". Keep the RAN/STOOD card and its sentence as they are. Don't add an
   unsourced explanation for the sixth kill.
2. **The Train, a continuity error (line 316).** "For the first time all episode, Doug got out of the way of something" is wrong: in
   The Apples, Doug "backed out of the garden very slowly". Replace it with a line that is true. For example: "Doug stepped off the line,
   which was the first sensible thing he had done all winter, and the narrator found it a little hard to watch." (The Snow and The
   Train are both winter, and Doug died in The Snow, so the line holds.)
3. **The Train, TTS (line 294, screener note 2).** Change "somewhere between one and one and a half meters of snow" to "about one to
   one and a half meters of snow." You're editing the script anyway, so fix this now rather than in the narration pass.

Optional (writer's call): screener note 1, end The Hooves on a short punch ("It's standing on the weapon.").

Re-screening: the screener only needs to confirm that fixes 1-3 are in, Flesch is still 72 or below, and the word count is still at
least 2,950. Then the script comes back to me. The series bible update (counter 195 to 203, the BEAR / MOOSE scoreboard, death 200
flat) waits for approval.

## 2026-10-21: script gate, draft 4 (creative director): APPROVED, stage to `script_approved`
- The screener's scoped re-check passed: fixes 1-3 are in (The Wolves card "77 TESTED" with no total-kills figure, so the RAN/STOOD card
  adds up; a true continuity line in The Train; TTS-safe snow depth), and the optional Hooves punch is done.
- I applied screener note 1 myself (wording only): in The Train, the second "Doug stepped off" now reads "That was the first sensible
  thing Doug had done all winter, and the narrator found it a little hard to watch." Re-measured spoken text: Flesch 70.3, 3,021 words
  (about 15:30). No facts changed, so no re-screen is needed.
- Why I'd click and keep watching: the title promise lands in the first sentence, the scoreboard gives a visible reason to wait for
  "Worse than bears.", and the evidence-led twists hold up to "the video is wrong" comments.
- Carry to the titler: keep "to Doug" in any "Deadlier" title (the sources support injuries, not deaths). No T1 or T2 wording.
- Series bible updated: counter 195 to 203 (death 200 flat), BEAR / MOOSE scoreboard logged as an episode-only device, episode log row.
- Variety reminder: 021-024 are four single-animal episodes in a row, so 025 should be a list episode or the prehistoric compilation.

## 2026-10-21: thumbnail gate (creative director): A APPROVED, B APPROVED, C NEEDS FIX
I viewed all three at 1280x720 and at feed size, and read visual_review.md (PASS, C labels soft) and art_review.md (A > B > C).

- **A (`thumbnail.png`, "WRONG ANIMAL"): APPROVED, lead variant and the opening frame (s001).** The glaring head-on bull fills
  the frame, and the small sweating grizzly next to screaming Doug makes the pitch before anyone reads the title: the bear is scared
  too. The text is heavy and legible at 168 px and shares no word with the title. The video delivers what it promises (BEAR 0 / MOOSE 8).
  I'd click it.
- **B (`thumbnail_b.png`, "35 MPH"): APPROVED, A/B variant.** One focal point, readable peril, and a crisp number. 35 mph is the NPS
  figure (facts.md line 70) and is the same as the script's 56 km/h, so it isn't misleading even though the narration uses km/h. It is
  less surprising than A because there's no bear, but it's a clean peril test. I'd click it.
- **C (`thumbnail_c.png`, chapter grid): NEEDS FIX, do not upload as a test variant yet.** At 168 px the labels are thin grey strokes,
  and the six tiles become brown shapes on colour. The labels carry an archetype-A grid, and here they don't hold up, so I wouldn't
  click it. Doug is a dot in four tiles and missing from two. Required changes to `thumbnail_test_c.json` (graphic designer):
  1. **One-word labels:** Calf, Dive, Rut, Hooves, Train, Highway (drop "The"; Title Case, per the bible's 1-4 word rule).
  2. **Heavier, bigger labels.** The tile `label` already uses ComicNeue-Bold at 58 px, and that weight is too light. Set each tile's
     `label` to "" and add a `text` element under each tile instead: font ComicNeue-Bold, size about 84, color #000000,
     `outline` #000000, `outline_width` 3 (a black-on-black stroke works as faux-bold, so it still reads as the bible's
     no-outline bold comic label). The cap height should be about 60-70 px. Shrink the tile height from 242 to about 225 if you need
     room so labels don't touch the next row or the bottom edge (keep a margin of 8 px or more).
  3. **Bigger Doug in every tile.** Raise Doug's scale from 0.2 to about 0.32-0.35, so the red cap stays a visible red dot at
     168 px, and keep him smaller than the moose so he still works as the scale figure.
  4. **Add Doug to Train and Highway.** Train: Doug standing just off the track beside the moose (pose stand, expression shock),
     which matches the script beat where he steps off the line. Highway: Doug cowering at the roadside between the car and the moose
     (cower, shock). No injury imagery.
  5. Leave the subjects, background colours, frames and white canvas as they are. Re-render `thumbnail_c.png` and
     `thumbnail_c_small.png` and check that every label reads at 168x94. The visual screener only needs to re-check C (labels
     legible at feed size, Doug visible in 6 of 6 tiles, nothing cropped), and then it comes back to me.
- The stage stays `art_approved`. Packaging can go ahead with A as the primary and B ready. C is added to the test only after its re-check.
