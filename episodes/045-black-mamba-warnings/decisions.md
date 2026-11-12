# 045-black-mamba-warnings: decisions

## 2026-11-12, creative director: script gate (APPROVED)
- Read: script.md draft 2 (with the screener's two fixes applied), script_review.md (draft 2 re-screen: FAIL on 2 one-word overstatements
  only; hook 8, structure 8, voice 8, TTS PASS, policy PASS, 2,047 words, about 10.5 min). The screener said that once those two words were
  fixed, the draft passes without another full screen.
- Fixes checked in script.md: line 11 now says "is usually heading home" and line 37 says "usually turns defensive". Both match ADW/WP. R1 is applied
  too (line 87, "homes, factories and businesses"). The opening still lands "The Speed." at spoken words 34-35. I counted it myself.
- Opening: thumbnail A, then sentence 1 gives a number plus the myth reframe, the payoff promise ("bitten a day's ride from antivenom") lands at
  about 0:08, and "Here's the problem." lands at about 0:34. The item 1 twist is a new fact, not a restatement. I would click, and I would keep watching.
- Escalation: It leaves / It warns / It strikes, ending on the most extreme item (the bite far from antivenom). The boss pays off the 0:05 promise.
  The title "the snake Africa fears most" is sourced per the screener and matched in-script at line 107. The script never claims the mamba hunts or chases
  people. The facts used up in 010 are not reused as new: only the mouth callback, and the speed is re-examined with a new e-bike analogy.
- Gore and kids: no strike is shown, no wound is described, deaths cut to black, mambalgins are framed as mice-only, and the survival and
  "don't kill or catch it" lines are attributed statements, not advice. The tone is adult-coded deadpan. Counter 343 to 350, 7 deaths, deaths 348 and 350 flat.
- Non-blocking, for the director: the "It strikes." band is spoken after the Second Strike kicker, which is correct per the axis comment (before
  item 7). Stage it as the band card over the dendrotoxin opener, not as a beat of item 6. Screener advisory A1 (the "hood" repetition in item 5)
  is left as written; it is acceptable at 222 words.
- Process note: status.json was moved to script_approved (note "CD approval") and committed before this gate ran. This time the outcome is the
  same, but from now on the stage moves only after this entry is written.
- Series bible: the 045 row and the counter total (350) are added at final approval, as for 040-044.
SCRIPT: APPROVED

## 2026-11-12, director: shotlist
- 206 shots, all 2,047 spoken words in order (checked by the generator against script.md), max 22 words per shot, Doug in 163 shots (79%).
  9 chapters. Generator: `episodes/045-black-mamba-warnings/build/gen_shotlist.py` (git-ignored scratch; re-run it to rebuild).
- Bands: per the CD note, "It strikes." is staged as the opening card of The Dendrotoxin (s137, `chapter` on that shot, `topbar: false`).
  For consistency, "It leaves." (s005) and "It warns." (s070) are staged the same way, as the opening cards of The Speed and
  The Head Lift. They use white section-header text (art bible "Section header cards") and are never shown as a beat of the previous item.
- HUD: DOUG DEATHS label at (1590,162) plus a WARNINGS LEFT chalk label at (1590,238), size 30, green board `#2f5a3a`. It reads 3 from s002,
  2 from the Head Lift title (s071), 1 when the mouth opens (s096) and 0 from The Second Strike (s114). At 0 the board turns red
  `#e0201b` with white text, because red text on the green board did not read in keyframes. The second-meter zone rule applies (glyph tops at y >= 290 over x 1300-1860).
  The HUD is hidden on the four sober cards (s182-s185, 1962 antivenom figures), following the 027 precedent.
- Colour ramp, light to dark across the severity axis: midday `#8fd3ff` -> sunrise `#f6dcae` -> gold `#f6c45a` -> dusk `#f2a24a` -> red dusk `#b8573a` ->
  night falling `#3b3550` -> night `#1b2f5a` (Dendrotoxin, with cream diagram cards) -> lab/library (Painkiller) -> night `#101c38` with sober cards
  `#15181a` (Long Ride) -> dawn coda. Death beats are `#0b0f14` cards with an on_back Doug, a ghost and the field guide.
- One-off capless upright Doug (art bible "Capless upright Doug"): s066-s068, the snake eagle costume. The script puts the "cap on top" of
  the eagle head, so Doug wears `gear: ["cap_off"]` and `doug_cap` sits on the hood. There is one cap per frame.
- s091 silhouette glow is the purple `#5e4670` (it sits on the red-dusk ground). Long stick on s134/s135 lies beside Doug's feet, not across his body.
- The library scene drops the script's "cap on the desk" and the Second Strike stick drops "cap on the end of the stick". Doug keeps his cap
  on in both, so we avoid two more capless one-offs. The 010 callback uses grey paint spray only (s110-s111), with no sign.
- Shorts (shorts.json, titles left for the titler): short01 s051-s059 The Snake Eagle (~33 s), short02 s160-s175 The Painkiller (~55 s),
  short03 s072-s078 The Head Lift (~26 s). Each one ends on its payoff, with a short outro and the simple end card.

## 2026-11-12, creative director: package (thumbnails A/B/C + ranked titles)
- Read: metadata.json `packaging` (D4 gate, 10 ranked, top 3 paired), visual_review.md round 2 (thumbnails PASS at 168x94, policy clean),
  `package check --dry-run` OK, and all three PNGs at full size and feed size.
- B, "Why the Black Mamba Warns You Three Times Before It Kills" + "DOUG IGNORED THEM": APPROVE. It is the strongest of the three. The crossed-out
  tally of 3, the open black mouth (the namesake and the episode's real fact) and the oblivious sweat-drop Doug tell the whole story at feed size. The title is
  delivered by the script's three-warning axis. No gore, and the irony is adult-coded.
- A, "Every Reason the Black Mamba Is Africa's Scariest Snake" + "IT'S GOING HOME": CHANGES REQUIRED. This is the launch variant, and at 168 px it reads as
  a calm green snake in profile next to a mound. The title says "scariest", but nothing in the frame is scary, and Doug, who is the joke (he is standing in its doorway),
  shows up as a red dot.
  1. Doug: scale 0.42 -> about 0.65, still standing in the hole/doorway, with his shock face readable at 168x94. Shift the mound and text as needed. The text may overlap the mound top, but not Doug.
  2. Snake threat: the head is the hero. Swap `black_mamba_hood` for `black_mamba_hood_gape` (the inky-black mouth, no fangs dripping), or at minimum enlarge the
     head so it is about 1.5x its current size and aim it at Doug/the hole, not at empty sky. Keep the "it just wants to go home" twist with the arrow.
  3. Keep the arrow, the text and the orange sun. Re-check the small version.
- C, "Why Black Mamba Bites Are Deadliest a Day's Ride From Help" + "FLAT TYRE": CHANGES REQUIRED.
  1. Text: the channel language is en-US (config), so it should read "FLAT TIRE". Keep the British spelling in the narration only if the script already has it.
  2. Mamba: drop the black silhouette with the red rim. It looks like a cut-out, not a black mamba, and it breaks the A/B creature look. Use the green
     `black_mamba_reared` (or `_gape`) unsilhouetted, as in A/B, so the three variants test packaging, not two different snakes.
  3. Help: the hospital is a grey block at feed size. Replace it with a small clinic hut with a large red cross, about 2x the current icon height,
     still at the far right end of the dashed route, so "a day's ride" reads as distance and not as a city.
  4. The snake still bites no one, and the bike and Doug stay the focal point.
- After the A and C fixes: the visual screener re-checks A and C at 168x94, and then I give the final package approval. B does not need re-review.
PACKAGE: B APPROVED; A, C CHANGES REQUIRED

## 2026-11-12, creative director: package re-review (thumbnails A and C, round 2)
- Read: the diffs to thumbnail.json, thumbnail_test_c.json, metadata.json and title_candidates.json; build/thumbnail.png, thumbnail_c.png and both
  `_small` (168x94) versions. `package check --dry-run` OK, `validate packaging` OK. No visual screener round-3 entry is in visual_review.md yet (see below).
- A, "IT'S GOING HOME": APPROVE. All three notes are applied.
  1. Doug is now at scale 0.65 in the mound doorway. At 168 px the cap and the shock face both read, and the text sits on the mound top without touching him.
  2. The snake is `black_mamba_hood_gape`, scale 2.1, tilted so the inky open mouth is aimed straight at Doug. The frame is now scary, which fits "scariest".
  3. The arrow (mouth to hole), the text and the sun are kept, so the "it just wants to go home" twist still reads.
  Non-blocking: Doug is wider than the hole, so he reads as standing in front of the doorway rather than inside it. That is fine at feed size, so leave it.
- C, "FLAT TIRE": APPROVE. All four notes are applied.
  1. The text and the metadata/title_candidates thumb_text now say en-US "FLAT TIRE". The narration keeps "flat tyre" (script lines 17/357/359). The TTS sounds the same, so there is no change.
  2. The mamba is the green unsilhouetted `black_mamba_reared`, the same creature look as A/B. The A/B/C test now varies packaging only.
  3. The clinic is a thatched hut with a large red-cross board at the far right end of the dashed route. It reads at 168 px, and "a day's ride" reads as distance.
  4. Nobody is bitten. The bike, the flat front tire and Doug's shock face are the focal point.
- Policy: no blood, wounds or fangs in flesh. Adult-coded deadpan, not kid-coded. Each thumbnail is delivered by its paired title and by the script.
- Sequencing (per the 2026-11-12 package entry): the visual screener re-checks A and C at 168x94 and logs round 3 in visual_review.md before the stage moves to
  `packaged`. If the screener passes, this approval stands with no further CD pass. If it fails, the fixes come back to me.
PACKAGE: APPROVED (A, B, C), pending the visual screener round-3 PASS on A and C
- 2026-11-12 showrunner: script 2 rounds (+CD), art 2 rounds, thumbnails 2 rounds (A,C revised). Editor raised voice.speaking_rate 1.09->1.15 (wpm 193.9); watch next episode's pace. Runtime 11.4 min. Risks: antivenom 1962 figures via Wikipedia; Benin delay data is all-snakebite.

## 2026-11-12, creative director: final package approval (post-render)
- Read: metadata.json (title, alt_titles, description, tags, packaging), build/chapters.txt, build/thumbnail.png, build/samples f_001-f_003,
  script.md opening, visual_review.md round 4 (main PASS, shorts PASS), status `built`, QC passed.
- Title: keep "Every Reason the Black Mamba Is Africa's Scariest Snake" (55 chars, search-friendly, T8). No alt swap: the strongest alt
  ("Why the Black Mamba Warns You Three Times Before It Kills") already runs as test variant B with its own thumbnail, so swapping would collapse the A/B/C test.
- Thumbnail A: the open inky gape aimed at Doug in the mound doorway carries "scariest", and the arrow carries the twist. Matches the opening frame and the title.
- Description: chapters match build/chapters.txt exactly (9 items, 0:00 to 9:41, all at least 10 s apart). Sources are listed, plus the cartoon/not-medical-advice
  disclaimer and the AI-use note. Every promise (the 20 km/h "chase", going home, the bite a day's ride from antivenom) is delivered.
- First 60 s: "The Speed." lands at spoken words 34-35, the twist "Here's the problem." comes at about 0:33, and the payoff promise is in sentence 2. Frames: horse
  legend, SHY at 40 m, counter 343 -> 344 by the mound. HUD, counter and WARNINGS LEFT 3 read clearly. Cartoon death only, adult deadpan, no kid-coding.
- Text-only fix made: in metadata.json `thumbnail_brief`, `packaging.candidates[0].concept`, `packaging.variants[0].thumb_idea` and title_candidates.json,
  "mouth closed" is now "inky-black mouth open with small fangs aimed at Doug" and "no fangs" is now "no dripping fangs", so the text matches the approved image.
  Re-ran `validate metadata`, `validate packaging` and `package check --dry-run`: all OK.
- Accepted as non-blocking (no re-render): the s083 zoom clips "DOUG DEATHS: 345" to "34" for about 0.5 s. Director: next episode, keep HUD-bearing zooms at 1.04
  or below. Art director: move the HUD to a screen-fixed overlay (engine backlog).
- Stale stage direction: script.md still describes thumbnail A as "mouth closed". It is never spoken, so it has no effect on the output and is left as is.
FINAL: APPROVED
