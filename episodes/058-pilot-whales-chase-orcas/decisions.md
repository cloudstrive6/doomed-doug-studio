# 058 decisions

## 2026-11-25 · Script gate (draft 2 + outro fix): APPROVED
Creative director. Read brief.md, script.md, facts.md and script_review.md (draft 2 screen).

- The draft 2 screen failed on one required fix only (outro CTA copied from 049) and stated "Fix that one sentence and the script
  passes; no other re-check is needed". All other gates passed: facts 0 errors, opening 8, structure 8, voice 8, TTS/policy/length PASS.
- Fix verified: l.256 now ends "Subscribe before Doug finds a worse pod." Grep of `episodes/0*/script.md` finds it only in 058. One CTA,
  no comment prompt, outro 26 words (cap 30). No other line changed; 2,160 spoken words, about 11.1 min at 195 wpm.
- Would I click and keep watching: yes. Cold open with a death stake in sentence 1, "The Speaker." at word 34, twist by about word 88, a
  specific payoff (Doug as the orca who can't porpoise), honest "why" (two hypotheses, attributed, neither ruled out).

### Sign-off (a): item 6 reversal. APPROVED
The brief was wrong. The documented case is a female killer whale (Sædís) seen with a newborn long-finned pilot whale calf, August 2021,
off Snæfellsnes (Mrusczok et al. 2023, *Canadian Journal of Zoology*, doi 10.1139/cjz-2022-0161; Dalhousie 2023). No source exists for
pilot whales with an orca calf. The script's version is better than the brief's: it gives the pilot whales a plausible motive (orcas
taking calves), clearly labelled "a suggestion, not a finding", and the re-hook into item 7 ("That calf had a family") now makes literal
sense. Conditions for downstream: the calf is drawn plain (dot eye, no cute proportions); the "NOT HERS" label stays; no packaging may
say "adopted" or imply pilot whales raised an orca.

### Sign-off (b): dropping "A Third Their Weight". APPROVED, with a wider rule
NOAA maxima give about 10 t vs about 2.3 t (roughly a quarter), and comparing maxima of two species is shaky anyway. Titler rules:
- No weight or size ratio in the title or thumbnail: not "a third", "a quarter", "four times", or "half their size" (lengths are about
  9.8 m vs 6.7 m, so "half" also fails).
- Allowed scale wording, if any: "Smaller" / "Much Smaller" (the script says "the bigger animal, by a long way"), or no scale phrase.
  Preferred leads remain brief §1 ("Why Orcas Flee When Pilot Whales Show Up", "Why the Ocean's Top Predator Runs From Pilot Whales").
- Location claims stay honest: "off Iceland" / "the bay"; no "out of fjords" (per facts.md title notes).

### Notes downstream
- Editor: check Chirp reads "Sædís" (SIGH-deess); if not, write "Saedis" in narration text.
- Art director: approve the WHO RAN scoreboard and the orca costume (new gear) before keyframes.
- Counter 420 to 425 (deaths at items 1, 2, 4, 7, 8). Series bible lore is updated at packaging/upload, not here.

## 2026-11-26 Director: WHO RAN board tallies moved (visual screener round 1, fix #1). FOR CD SIGN-OFF
The screener flagged the board as reading backwards: header "WHO RAN", but the tally ticks piled up under PILOT WHALES (7 by the end),
which says "pilot whales ran 7 times", the opposite of the thesis. Meanwhile the red ORCAS stamp sat under EVERYONE ELSE, so the board
contradicted itself.
- Change: every tick now lands in the **EVERYONE ELSE** column (s002-s219). The **PILOT WHALES column stays empty all episode**:
  they never ran, and that's the joke. At the boss (s216 from 0.88, s217-s219) the red **ORCAS** stamp goes on a second line under
  the ticks, in the same column.
- Each tick still marks a beat where someone other than the pilot whales backed off (Doug included). No narration changes.
- The board asset (`who_ran_board`) artwork is unchanged; only its description changed (tally zone usage). The tick and stamp positions
  live in `build/lib058.py` (`tick_lines`, `hud`).
- I rejected the screener's alternative of renaming the header to "WHO BACKED OFF?" / "NOT PILOT WHALES" because it's weaker.
- CD: please confirm this reading of the device. Thumbnail and packaging don't use the board, so nothing changes there.
