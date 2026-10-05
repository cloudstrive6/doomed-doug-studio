# Decisions: 007 Every Time Earth Froze

## 2026-10-05: script gate, APPROVED (draft 2 + CD edits)
- Screener: draft 2 PASS (facts 0 errors, hook 9, structure 9, voice 8, TTS/policy PASS, 3,121 words). Round-1 fixes F1-F4,
  rule 7, rule 14 and bible 3.5 verified in the text.
- Against the brief: all 11 items in the briefed order, axis monotonic (1816 to 2.4 Ga), four headers, counter 56 to 65
  (9 deaths, survivals at Frost Fairs and Sturtian), befriending flower/Meganeura/algae with the algae paid off, one
  callback each to 003 and 004, no banned props or winter-cartoon tone, real victims get plain lines only, Younger Dryas
  impact skipped, Snowball/slushball and Huronian hedged. "Year Without a Summer" is said at words 31-34 and the twist lands at about 27 s.
  I would click and keep watching: the Thames card, "We are counting this as one" and the chloroplast payoff all land.
- CD edits applied directly to script.md (small, no re-screen needed; new total about 3,113 words, still in range):
  1. Opener: "again and again" changed to "many times", so "every one of them" has a noun to refer to.
  2. Doggerland: "However, that's not the disturbing part." came straight after the line about people on the coast, which
     read as if their deaths weren't the disturbing part. Changed to "But the wave isn't what finished Doggerland."
  3. Item 11: "the algae ... carries" changed to "carry".
  4. Closing kicker moved before the 2026 cut (it played after Doug's thumbs up). "The first great freeze" changed to "This freeze"
     to keep the Pongola caveat honest.
- **Closing image: APPROVED** with the following direction. After death 65 and the kicker, cut to a plain sunny 2026 field,
  dial "2026". The time machine lands as a block of **clear blue-white ice** (never brown or stone, so it can't read as 003's fossil)
  with the cap frozen on top. It cracks, the cap drops onto Doug's head (Doug is never shown capless), and he does `thumbs_up`.
  The counter stays at 65. Final frame is Doug with his thumb up in the cracked ice, then the 18-word outro. No pigeon and no snowman-like shapes.
- **FROZEN meter: APPROVED for the director**, with the art-gate decision on reusable lore still open. Rules:
  - It sits in a corner next to the death counter, the same size class as 001's depth meter, with a small "FROZEN" label that is legible at 1080p.
  - It is **monotonic** and never goes backwards. Suggested white fill per item: 1 speck, 2 about 8%, 3 about 15%, 4 about 20%, 5 about 25%,
    6 top third, 7 adds a south polar cap (about 40%), 8 half, 9 fully white, 10 fully white, 11 fully white and then
    frosts over with icicles at "The big scene globe turns fully white" ("maxed out").
  - The item-11 dark-to-white change happens on the **big scene globe**, not on the meter. The script's stage directions have been corrected to say this.
  - It updates on the item-name shot, never mid-sentence. Keep it clear of maps and left-edge labels (006 carry-over: the meter covered map shots).
- Carry to the titler: don't say "first ice age" anywhere (Pongola about 2.9 Ga). "First Snowball" is OK only with "possibly" in the description.
  The thumbnail must not use a "Snowball Earth" label (brief 7). Use T1 "What Dying Every Time Earth Froze Would Be Like" unless the titler's data says otherwise.
- Carry to the editor: preview the pronunciations of Bretz, CN Tower, Dryas octopetala, Sumbawa and Storegga in `narrate`.

SCRIPT: APPROVED

## 2026-10-05: thumbnail choice (creative director): A (3x3 grid) wins, GO conditional on visual-screener PASS
- Candidates: the archetype B ice core (11 bands, per brief 7) and the archetype A 3x3 grid (the brief 7 fallback). I compared
  `build/thumb_compare_168.png` and both 1280x720 renders.
- At 168x94 the ice core fails the condition the brief set for it. The bands are slivers, the scenes inside are specks (you can't make out the dragonfly, the
  door or the palm trees), and the alternating labels are grey mush. The column also leaves about 60% of the frame as white margin. The grid at the same
  size reads at once: nine saturated colour blocks, a white ball on navy as the boss tile, and labels that are still mostly readable.
  That triggers the brief's own fallback. The grid drops Frost Fairs and Doggerland exactly as specified, keeps the order, and ends on First Snowball.
- It also fits the style bible better: archetype A is the default grammar (2.A), and 002 and 004 both shipped grids. Doug is small
  and in one tile only (never the hero). No label shares a word with the title, there's no "Snowball Earth" and there are no photos.
- Files: the grid is now `thumbnail.json` (`_note` updated), and the ice core is kept as `thumbnail_b.json` and marked rejected. I ran `python -m studio
  thumbnail` to produce `build/thumbnail.png` and `validate` returned OK. s001 uses `scene_ref: thumbnail`, so the opening image is now the grid
  with no shotlist change. The "thumbnail column" stage direction at script line 6 is outdated wording only.
- Optional notes for the designer (not blocking): "Year Without a Summer" is set smaller than the other labels. Fine, but if
  it can go up a size without wrapping, do it. The Last Glacial Maximum tower is small, so at 168px the tile reads as "ice wall", which is acceptable.
- Still needed: the visual screener's thumbnail pass (feed-size legibility, policy) on `build/thumbnail.png` and on s001 in the keyframes.

THUMBNAIL: APPROVED (A grid), pending visual-screener PASS

2026-10-05 Showrunner: packaged. Rounds: script 2 (draft 1 FAIL on 4 facts + 3 style; draft 2 PASS, CD approved with small edits); art assets 1 (30 drawings approved, minor map fixes); keyframes 3 (R1 FAIL 35+22 fixes, R2 FAIL 9 fixes, R3 PASS); thumbnail: grid chosen over ice core (illegible at feed size), polished, Sturtian-tile ink fix. Editor raised speaking_rate 1.10 -> 1.15 (196.7 wpm, ~16.6 min). Risks: pronunciation of J Harlen Bretz / CN Tower / Dryas octopetala / Storegga unverified (no audio listen; no phoneme override in tts.py); music null; no draft render yet (CI final render + QC next); optional thumbnail leg-tip nit in Sturtian tile.
