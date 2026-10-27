# Episode 029: decisions

(The pick itself is recorded in `brief.md` section 0 and growth memo `data/insights/2026-10-25.md`, CD decision 7.)

## 2026-10-27, creative director: script gate (draft 3)
1. **Script APPROVED.** Screener round 3 PASS (facts PASS with 0 fail items, hook 8, structure 8, voice 8, TTS/policy/length PASS).
   2,013 spoken words, about 10:19. This is the first episode inside the 10-12 min retention band, as decision 27 in 028 required.
2. **Read against the brief, it delivers:**
   - **Opening:** the first sentence is concrete (1916, the seal bursting out, the chase). The payoff promise ("Doug ends up under
     that ice, singing back to one") ends at word 30, and The Song pays it off exactly. "The Chase." is at words 34-35, and the
     shadow twist comes at about word 110.
   - **Axis:** position (on the ice, in a boat, in the water, under the ice), with four spoken bands and 9 items. Item 1 is one of
     the strongest. The boss is where the seal actually lives, so the escalation is about place, not gore.
   - **Counter:** 234 to 240, six deaths and two survivals. Death 240 is played flat, with no milestone bit.
   - **Real death:** The Snorkeller follows decision 7. It has a sober card, no name, no detail and no joke, and it includes
     Muir et al.'s honesty line.
   - **Kid appeal:** the narrator is deadpan, nobody says "nursery rhyme", and no penguin is shown being caught.
   - **Gags:** "Doug did not agree to this" (once), "Doug has died. Again." (once), costumes twice, one 016 callback and no 021
     callback, so it is not repetitive.
3. **The brief deviations in the script's header comment (1-9) are accepted.** All of them are fact-driven and narrow claims to what
   the sources say: "most" crabeaters and not 78%, Krause's 69.3%, Sperou's hedge, no gape angle and no "hang upside down".
4. **Notes for the director (not blocking; the stage directions can change without a new screen):**
   - **The Snorkeller:** drop Doug from the respect shot (script line 300) and use the two sober cards only, as the brief said
     ("no Doug on this item"). Doug was just killed at 239. If he appears alive and bareheaded beside a real death, it reads as
     him making the moment about himself, and a cap left alone on the ice is our death image.
   - **Item 1:** keep the 1916 meal flashback clearly marked (a "1916" caption or sepia), as the screener noted, so death 235
     does not read as the end of the item.
   - **Gift / Seal Eater:** the seal stays menacing and reptile-headed even in the "MAYBE" beat. Do not give it big cute eyes.
5. **Notes for the titler:**
   - Do not open with "Why" (024 and 026 already did).
   - The title and thumbnail must not lead on the 2003 death or imply that leopard seals routinely kill people. The video's
     own honesty line says they don't.
   - "Deadliest hunter" is fine for penguins and seals. "Deadliest to humans" is not.
6. **Series bible:** the episode log row and the counter total (to 240) are added at the final package gate. This keeps the
   running total from moving before the episode is locked.

## 2026-10-27, director: shotlist
1. **264 shots**, every spoken word once and in order (2,013 words, ~11 min including holds). Doug is in 92% of shots. The longest
   line is 17 words, and every shot over ~10 words gets an `appear` build.
2. **1916 is always framed.** Every Shackleton beat sits inside a brown-framed sepia card with a "1916" tag, and present-day Doug
   stands beside it on the snow. Death 235 (s029-s031, silent: the shape stops under his shadow, then black, then the cap on the snow
   with a ghost) is followed by the meal flashback in the same sepia frame. That frame also carries a "BACK IN 1916" caption above it,
   and ghost Doug watches from outside the frame (s032-s035), so the item clearly continues after the death.
3. **The Snorkeller (s213-s224): no Doug, no counter, no joke.** These are white-text cards on `#15181a`, and the title is white
   (027 Legend precedent). Per CD note 4, the bareheaded respect shot (script line 300) is dropped. The closing line, "earns its
   reputation...", goes back to card 1 with a 1.2 s hold. The kicker before it (s212, "it killed a person") is a plain black frame
   with no counter.
4. **Silent beats** (empty narration and `min_duration`, the 024 pattern) carry the stage-direction-only moments: the death-235
   slide, the penguin-costume hop, the selfie flash, the krill gulp, the crabeater splash and costume (239), and the cut to black and
   field guide NO stamp (240). The last one is the cap dropping into the crack.
5. **Upside-down Doug** (s252-s256) is a `group` with `rotate: 180` holding a plain Doug with `mask`, which is the art-bible
   ceiling-hang convention with no costume. The seal sings facing away until s256, where it flips to face him.
6. Gift and Seal Eater: the seal is never given cute eyes (CD note 4, carried into the asset requests). No penguin is ever shown
   caught: "then dead ones" is covered by the live penguin darting away and a "FIRST LIVING ONES" label.
7. Shorts: The Visitor (s072-s091), The Gift (s129-s147) and The Seal Eater (s184-s198), not item 1 and not The Snorkeller. Titles
   are left for the youtube-titler.
- validate.py: length-rule cutoff moved to 2026-10-27T12 (028 old rule, 029 new)
- Thumbnails round 2 (graphic designer, 2026-10-27): A and B water changed to `#3a9ad9` + `#6fc1ee` speckle (art bible). A: the seal sits fully under
  the floe with a gap of water, Doug's shadow is larger and darker with the seal's eye lined up under it, and IT FOLLOWS is raised 30 px. B: Doug
  shrunk 0.65x to 0.38x (small scale figure, style bible 7.10). C: the 2x2 grid is replaced by a spec-compliant 3x2 grid of 6 tiles with labels
  under the tiles (Chase, Visitor, Head, Gift, Sieve, Song). Ice Edge and Seal Eater are skipped because they contain title words, and The
  Snorkeller is never used on a thumbnail. At 168x94 the C labels are only marginally legible, but the tile subjects read. Visual screener
  recommends B as the lead challenger.

## 2026-10-27, creative director: thumbnail gate (A/B/C, visual screener round 2 PASS)
Read against the lead title "How the Leopard Seal Kills Doug From Under the Ice" and the alts. I checked all three at full size and at 168x94.
1. **A (`thumbnail.png`, "IT FOLLOWS"): APPROVED, lead and opening image (s001).** It is the title drawn as a picture: Doug strolls
   on the floe, unaware and smiling, while the spotted seal lies under his shadow, eye on him. The irony (he doesn't know, we do) is the click.
   No text overlaps the title words. At feed size the shadow, the seal and the red cap all read. It is also the only variant that pays
   off "From Under the Ice" literally, so it stays primary, following the 026-028 convention (A = s001 = primary).
2. **B (`thumbnail_b.png`, "CORNERED"): APPROVED, test arm and my bet for the CTR winner.** It has the strongest single focal point on the
   board: the reptile head towering over tiny, terrified Doug on a floe. It is honest: the seal comes at Doug from the water (Chase, Ice
   Edge). It does not show the "under" idea, which is why it is a test and not the lead. If Test & compare picks B, accept it with no further gate.
3. **C (`thumbnail_c.png`, 3x2 grid): APPROVED as a test arm, CONDITIONAL on one fix (graphic designer, `thumbnail_test_c.json`, Sieve tile):**
   the red cap inside the open red mouth, with pink-red krill sprayed around it, reads as blood spray around a bite at feed size (screener R3).
   We don't ship anything that reads as blood on packaging. Fix: (a) close the seal's mouth to a toothy grin with the cap brim poking out of
   the lips, **or** draw the inside of the mouth dark grey, not red; and (b) recolour the krill orange (`#f39c3c`-ish) and keep them in
   the cloud ahead of the snout, with no specks scattered around the jaw. Re-render `thumbnail_c.png` and `thumbnail_c_small.png`.
   No re-screen is needed if only the Sieve tile changes, but the graphic designer must eyeball the 168x94 image to confirm the red-spray read is gone.
   **If C is not fixed before upload, ship A primary + B as the only test variant. C never ships with the current Sieve tile.**
4. Stage is unchanged. The thumbnails do not block packaging, because A + B are cleared now.
- 2026-10-27: scripted 3 rounds (draft1 FAIL hook/facts, draft2 FAIL word-count, draft3 PASS); assets 2 rounds; keyframes 2 rounds (AD+VS PASS); thumbs A lead/B/C approved; validate cutoff fixed in studio/validate.py. Risks: IPA pronunciations (Owha etc.) unchecked by ear; sieve head asset plain; marina water colour #2f7fbf.

## 2026-10-27, creative director: final package gate
Inputs: visual_review.md round 3 (main PASS, Shorts FAIL now fixed in shorts.json with the re-render queued, which does not hold the long video),
build/qc.json (698.5 s, no problems), metadata.json, build/chapters.txt, thumbnails A/B/C at full size and at 168x94, samples f_001-f_004, and the script opening.
1. **Title: keep the lead, "How the Leopard Seal Kills Doug From Under the Ice".** No alt is clearly stronger. "Deadliest Hunter... Antarctic Ice"
   is a search phrase, but it drops Doug and the "under" twist, and A only pays off the lead. "Above and Below" is weaker and more generic.
   The lead is honest: the seal comes at Doug from the water in every death, and the boss is under the ice.
2. **Thumbnails: A primary (= s001), B test, C test, all three ship.** I checked C: the Sieve tile now has a dark mouth interior and orange krill
   in the cloud ahead of the snout. At 168x94 it reads as "cap in the mouth", not as blood, so the condition from the thumbnail gate is met.
   If Test & compare picks B or C, accept it with no further gate.
3. **Description: one edit made by me.** "is the deadliest hunter under the Antarctic ice" became "hunts from under the Antarctic ice". The
   superlative has no source (orcas exist), and we never approve unsourced claims. I re-ran `validate metadata`: OK. The chapters match
   build/chapters.txt (9 items plus intro, starting at 0:00). The sources, disclaimer and AI-use block are fine.
4. **First 60 s: pass.** The first sentence is concrete (1916, the seal bursts out and chases one of Shackleton's men). The payoff promise
   ("Doug ends up under that ice, singing back to one") lands by about 0:10. "The Chase." comes at words 34-35, and the shadow twist
   ("the ice was a floor... a window") arrives well inside 45 s. f_001-f_004 are clean: chapter tag and counter are legible, the explorers are
   bearded and not Doug, there is no gore, and the rifle beat cuts away.
5. Series bible updated: the death counter is now 240 and the 029 row is added to the episode log.
6. Non-blocking notes for later: R1 (plain Sieve head asset) goes to the illustrator backlog; the IPA pronunciations still need a listen
   during the owner's review window.

- 2026-10-27 showrunner: workflow reported QC exit 1 but qc.json has no problems and a re-run of qc exits 0; main PASS, shorts FAIL (end cards fixed, .rerender=shorts queued). Main video approved.
FINAL: APPROVED
