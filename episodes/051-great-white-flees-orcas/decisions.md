## 2026-11-18: script draft 3, CD gate: CHANGES REQUESTED (not staged)
Screener PASS (8/8/8, facts clean, 2,055 words). The script is strong and the facts are solid, but the boss's headline fact is spent early.

Required:
1. **Item 7 steals the boss reveal.** The Replacements opens with "In 2019, shark spotters in False Bay recorded no white sharks for the entire
   year", and its tally board reads "WHITE SHARKS: 0". The Empty Bay's punch is that same zero ("2011: 300+" wiping to "2019: 0"), so the boss opens
   on a repeat. Fix: item 7's name sentence leads with the newcomers only, e.g. "In two thousand nineteen, shark spotters in False Bay counted one
   hundred and one bronze whalers." Keep "With the great whites gone, they moved in" as the bridge. Tally board: "BRONZE WHALERS: 101" only (drop
   "WHITE SHARKS: 0"). The zero is spoken and drawn for the first time at item 9. Keep item 7 within 200-260 words.

Optional (writer's call, do not let these grow the script):
2. Payoff line: "their bay" is ambiguous right after the Farallones sentence. Consider "Doug is the last great white in a bay the real ones gave up
   on, and the orcas come back."
3. Screener polish 1 and 2 (line 201 "had stayed roughly stable since"; line 157 split the "because").

Note for the titler (not a script change): the script says "up to a year", which is the source's wording. Prefer "Up to a Year" or a title without
the duration over a flat "for a Year", per brief 1.

Route: the writer applies 1 (and any of 2-3). The screener does a quick delta check of item 7 and item 9 only. Then the script comes back to the CD for
approval. No full re-screen is needed.

## 2026-11-18: script draft 4, CD gate: APPROVED (script_approved)
Screener PASS on the delta check (8/8/8, 2,049 words, about 10.5 min, 0 new fact errors). Verified myself:
1. Fix 1 applied. Item 7 opens on "one hundred and one bronze whaler sightings" (facts row 108), the tally board is "BRONZE WHALERS: 101" only, and
   the 2019 zero is spoken and drawn for the first time at The Empty Bay ("2011: 300+" wiping to "2019: 0"). The boss owns its reveal again.
2. Optional 2 applied. The payoff line is now unambiguous and The Empty Bay pays it off.
3. Polish 2 (line 157 "because") was not taken. That is acceptable and the writer's call.
Death counter 380 to 386 (six deaths, items 1, 3, 4, 5, 7, 9). Series bible to be updated at upload.
Titler reminder: say "Up to a Year" or leave out the duration. Do not use a flat "for a Year".

## 2026-11-18: shotlist (director)
207 shots, 9 chapters, Doug in 77% of shots, deaths 380 to 386 (s027, s070, s093, s116, s155, s200), every spoken word once
and in order. Choices for the art director and editor:
- **Item palette (021 regional ramp, darkening toward the boss):**
  - The Exit and The Liver: `#3a9ad9`.
  - The Cousins: kelp `#4f8a7f` (a green ground, so the wordart uses the white/yellow override).
  - Then one step darker per item: The Empty Cages `#2f7fbf`, The Seals `#2a6aa6`, The Year `#1f5a94`, The Replacements
    `#1a4a7c`, The Move `#17426f`.
  - The Empty Bay: dusk `#14365e` under the `#e88a4a` / `#f2a24a` sky.
  - "Used to be" cards at The Empty Bay (s184-s186, s196) use the old-map history colours: sea `#3f6f86`, sky `#e9dcc0`.
  - No depth-ramp hex is used anywhere.
- **SHARKS GONE meter** (relabelled `wait_stopwatch`, staging only):
  - It's "--" until The Exit. It changes where the script's stage directions put it: ABOUT 5 MIN (s006), HOURS (s038),
    WEEKS (s068), MONTHS (s096), ABOUT 1 YEAR (s117), YEARS (s136, at the "Years." header), and turns red at The Empty Bay
    (s181).
  - It only goes up.
- **Costumes:** Doug is plain between costume beats.
  - Seal costume: s022-s026, The Seals beat, and the 008 callback s196.
  - Shark costume: The Liver beat, The Empty Cages beat, The Year, The Replacements beat, The Empty Bay.
  - Sevengill costume: s067-s069.
  - At The Move the costume is "on the back seat" (script), so that Doug is plain.
- **Field guide (GREAT WHITE):**
  - empty at s021;
  - NO written by the narrator's hand at s028;
  - MAYBE pencilled at s133;
  - MAYBE rubbed out at s199;
  - the "AFRAID OF ONE THING." sticky note at s203.
- **No gore:** the beached sharks are clean outlines with X eyes, the liver is an icon or a cutaway shape, and every death is
  a splash, a cut to black or a flat costume with the cap in frame.
- **Shorts:**
  - short01 is The Liver, s031-s040, with a hook.
  - short02 is The Year, s118-s127.
  - short03 is The Empty Bay, s182-s191.
  - Each one ends on its own payoff line. Titles and descriptions are left for the titler.

## 2026-11-18: package A/B/C, CD gate: CHANGES REQUESTED (B only; not staged)
I reviewed `build/thumbnail.png`, `thumbnail_b.png` and `thumbnail_c.png` at full size and feed size (`*_small.png`), paired with
their titles in `metadata.json` `packaging.variants`. `package check --dry-run` returns OK. There is no visual-screener report on
the thumbnails yet (`visual_review.md` round 3 covers keyframes only and skipped s001). Staging `packaged` needs that screener PASS too.

- **A: APPROVED.** Title "Why the Deadliest Shark Flees Orcas for Up to a Year" with the text "IN MINUTES".
  - The text and title work as a pair: it leaves in minutes and stays away up to a year. Both claims are sourced (MBA release on Jorgensen et al. 2019).
  - The image reads at feed size: a big shark bolting left, two bent fins, and Doug left behind. I would click it.
  - Optional polish, not blocking: give the shark a worried eye or a sweat drop so it reads as afraid as well as fast.
- **C: APPROVED.** Title "Why the Scariest Sharks Gave Up False Bay to Orcas" with the text "ZERO IN 2019".
  - The crossed-out fin, Doug alone and the fins on the horizon tell the whole story at small size.
  - "ZERO IN 2019" is sourced (Shark Spotters Annual Report 2019) and the video pays it off at The Empty Bay. I would click it.
- **B: CHANGES REQUESTED.** Title "Why Great White Sharks Flee the One Animal That Kills Them" with the text "GONE ALL SEASON".
  - I accept the designer's single scene in place of the three-panel grid. Doug in the shark costume standing on a surfacing orca,
    unaware, is a stronger peril image than the grid, and it keeps B different from A and C.
  - The current render does not deliver that image yet. Required changes:
  1. The orca does not read as an orca. The rotated silhouette shows no dorsal fin, no eye patch and no white belly, so at feed size
     it is a black hill. Draw it as the normal (not silhouette) `orca`, or add `orca_fin_bent` rising right behind Doug, plus a visible
     white eye patch. The bent fin is the episode's visual signature in A and C, and B needs it too.
  2. Remove the red speckle spray and the red rim. A red glow and red spatter on a black body in water reads as blood in a
     shark-and-orca predation episode. That is gore-adjacent, and we do not want it on a thumbnail. Use a white water break or foam
     line around the back instead.
  3. Pay off "GONE ALL SEASON" in the picture. Right now nothing in the frame is gone. Add two or three small great white fins on the
     horizon heading out of frame left with speed lines, or one fin with a small "BYE" arrow. Keep them small so Doug and the orca stay the hero.
  4. Anchor the exclamation mark to Doug (just above his head, near the cap) or drop it. At (1130, 300) it floats in empty sky
     and reads as a stray element.
  5. Keep the orange sky and white text. That is a good contrast with A (yellow) and C (cyan). Check the result at 168 px after the changes.
  - Re-render `build/thumbnail_b.png` and `_small.png`, then have the visual screener check all three variants. If B passes both the
    screener and the four points above, the CD will approve it without another full round.

## 2026-11-18: package A/B/C re-check, CD gate: APPROVED (all three; staging still waits on visual-screener round 5)
I reviewed the re-rendered `build/thumbnail.png`, `thumbnail_b.png` and `thumbnail_c.png` at full size and at feed size (`*_small.png`).

- **B: APPROVED.** All four required changes are in.
  1. The orca now reads as an orca at 168 px: the normal asset with only a slight tilt, a tall dorsal fin, a white eye patch, a grey saddle
     and a white belly. It reads as an orca, not a black hill. A straight fin instead of the bent fin is acceptable here, because the eye patch carries the read.
  2. There is no red anywhere in the water. The JSON has no red rim or red texture, and a white foam ring sits around the back. The gore-adjacent risk is gone.
  3. "GONE ALL SEASON" now pays off in the picture: three small great white fins on the horizon head out of frame left with speed lines.
     They stay small, so Doug and the orca are still the heroes.
  4. The "!" now sits just above Doug's head beside the costume fin, so it belongs to him.
  5. The orange sky and white text are kept, and the contrast with A (yellow text, amber sky) and C (cyan) still holds at feed size.
  Doug standing on the orca's back in the shark costume, shocked, is a peril image I would click.
- **A: APPROVED.** The orca fins have moved clear of the final "S" and are now separate shapes at feed size (the screener's round 4
  fix 1). The sweat drops and worried brow I asked for as optional polish are in, so the shark reads as afraid as well as fast.
- **C: APPROVED.** It is unchanged. The fin tip under "ZERO" is still the screener's non-blocking note and is not required.

Condition: do not stage `packaged` until the visual screener's round 5 check of A and B passes. Round 4 failed and no round 5
report exists in `visual_review.md` yet. If round 5 passes with no new blocking item, this approval stands without another CD round.
- 2026-11-18: 051 packaged. Script 4 rounds (facts, sentence avg, CD reveal fix), art 3 rounds (+1 visual pass), thumbnails 2 rounds (B reworked), editor narrate+validate OK. Risks: 'up to a year' must stay literal; 101 bronze whaler 'sightings'; 11.6 min runtime; opening minute not eyeballed in draft.
