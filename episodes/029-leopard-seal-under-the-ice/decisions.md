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
