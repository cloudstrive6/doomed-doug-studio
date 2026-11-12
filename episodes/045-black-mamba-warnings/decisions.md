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
