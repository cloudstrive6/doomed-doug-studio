# Script review: 017 The Most Disturbing Fungi Scientists Have Ever Found (draft 2, round 2)

Script Screener, 2026-10-13. Read: style bible section 7, brief, script.md (draft 2), facts.md, round 1 review, and the git diff from draft 1 to draft 2.
This round re-checks the two blocking fixes, the facts that were added, and every line that changed.

VERDICT: FAIL

| Check | Result |
|---|---|
| 1. Facts | **1 error**, introduced in draft 2 (chytrid "of the rest", fix 1). All 3 new facts hold. Round 1's F1 is fixed. |
| 2. Opening | **8/10**. The rule 14 violation is fixed, and no rules are violated now. |
| 3. Structure & pacing | **7/10** |
| 4. Voice & humour | **8/10** |
| 5. TTS readiness | Clean. The Pseudogymnoascus and bangbangus pronunciations are now in the comment. |
| 6. Policy | Clean (0 items) |
| 7. Length | 2,920 spoken words, recounted. That is about 14:58 at 195 wpm, inside 2,900-3,300 and 20 words above the floor. |

There is one blocking fix, and it is three words long. Everything else passes.

---

## 1. Facts

**Round 1 blocking fix:**
- **F1 (ergot, 1711): FIXED.** The sentence is cut, and so is its facts.md row. The replacement line about rye bread
  ("hit hardest among people who lived largely on rye bread") matches the Microbiology Society page ("subsisted on a diet high in rye"). OK.

**New facts verified this round:**

| Claim (draft 2) | Check | Result |
|---|---|---|
| "Viewers of the BBC's Springwatch nicknamed it Gibellula bangbangus, after the gunpowder store." | WWT page fetched: "named by BBC Springwatch viewers in honour of its discovery site". The discovery site was the gunpowder store. Winterwatch is the series that was filming (2021), and Springwatch viewers gave the nickname, so the two programme names don't contradict each other. | OK |
| "The same compounds did little or nothing to breast, liver or lung cancer cells." | Penn Engineering page fetched: "the compounds had little to no effect on breast, liver or lung cancer cells" | OK |
| "Valley fever doesn't spread from person to person, so every one of those cases came straight out of the dust." | CDC fact sheet and archived CDC page: "Valley fever cannot spread from person to person." CDPH says it is not contagious. The "out of the dust" part is a fair inference, because infection is by inhaling airborne spores. | OK. Advisory: facts.md quotes the CDC sheet as "cannot be spread from an infected person or animal to another person". Search results show "does not spread from person to person". Paste the exact wording. |
| "Spores left in the soil by an earlier generation infect the young cicadas as they dig their way up." | Cooley 2018 (round 1, OK) | OK |
| "...and the fungus gets the rest." | No timing claim now, so no source is needed | OK |

**F2 (new in draft 2): the chytrid recovery denominator is wrong.**
- Script line 147: "Ninety of those species are presumed extinct, and only about one in eight of the rest shows any sign of recovery."
- Scheele et al. 2019, *Science* 363:1459, abstract: "only **12% of declined species** show signs of recovery".
  "Declined species" means all 501, including the 90 that are extinct. That gives about 60 recovering species.
- "Of the rest" moves the denominator to the 411 that are not extinct. Sixty of 411 is about one in seven, not one in eight. Draft 1 had it right
  ("of the affected species"), and the edit broke it. facts.md row 91 still cites "12%" without saying what it is a percentage of.

**Facts.md housekeeping (advisory):**
- Row 91 still lists "Declines peaked in the 1980s". The script no longer says this, so drop it or mark it as cut.
- The citation swap for item 9 (EID 16(2) and 15(8)) is done. OK.

## 2. Opening (8/10)
- "Massospora." is spoken word **33**, and the twist marker comes at word **126**. No greeting, channel name or subscribe ask comes before them.
- The opener now says "taken over", which is accurate for all 10 items.
- **Rule check (section 7, rules 1-14):**
  - Rule 1: OK (2,920 words).
  - Rules 2-7: OK.
  - Rule 8: OK. Item 8 is still borderline (time anchor only) but acceptable, as in round 1.
  - Rule 9: OK. Average 14.2 words per sentence (at the floor), longest 33, Flesch about 67.
  - Rule 10: OK.
  - Rule 11: **see F2**.
  - Rule 12: OK.
  - Rule 13: OK. The 10 markers are all different.
  - **Rule 14: FIXED.** The boss now says "And here's where it gets personal." This phrase isn't in the style bible's PE marker list or in `data/` competitor material.

## 3. Structure & pacing (7/10)
- **Segment word counts, item name to kicker, Doug beats included:**

  | Segment | Words |
  |---|---|
  | Opener plus item 1 | 275 |
  | Fly | 283 |
  | Spider | 279 |
  | Chytrid | 290 (down from 307) |
  | White-nose | 285 |
  | Valley fever | 287 |
  | Ergot | 284 (down from 299) |
  | Tomb | 271 |
  | Cryptococcus gattii | 264 |
  | Boss | 380 plus a 22-word outro |

  All segments are now within the 250-290 range, and the boss is within 330-380.
- **First death** is at about word 261, around 1:20. That is closer to the brief's "about 1:00" than draft 1 was.
- **Advisory:** opener plus item 1 (275) is now just under the brief's 280-310 guide. It isn't blocking.
- **Escalation dips** (white-nose after chytrid, the Tomb after ergot) are unchanged. As in round 1, that is the creative director's call.
- **Running gags:** all present. Death count runs 139 to 147, with survivals at items 6 and 8. The ending follows the bible.

## 4. Voice & humour (8/10)
- The chytrid costume line now uses the "which is why" form, which fixes the logic.
- The new Valley Fever sentence and the bangbangus line read naturally, and the persona is consistent.
- No competitor phrases.

## 5. TTS readiness: clean
- No digits, symbols or parentheses are spoken.
- **Advisory:** "Gibellula bangbangus" is a new tongue-twister. Preview it with `narrate`.

## 6. Policy: 0 items
- The Tomb now attributes the death count ("according to later accounts"), and the stage directions hold a beat after the sober card. A2 and A3 are resolved.
- The new cancer line widens the caveat, so the risk of a medical promise is lower than in draft 1.
- There is still no gore, no kids framing and no medical advice. The title promise is delivered.

## 7. Length
2,920 spoken words, about 14:58. That is inside the brief's 2,900-3,300 range. Fix 1 changes no words.

---

## Required fixes

1. **F2 (fact, rule 11).** Chytrid, line 147: "and only about one in eight of the rest shows any sign of recovery."
   - Change "of the rest" to "of all the declining species", or restore draft 1's "of the affected species".
     Either keeps the 12% of 501 denominator.
   - If you'd rather keep "the rest", the figure becomes "about one in seven". That needs facts.md to show the arithmetic (60 of 411), and the
     paper's species count has to be confirmed first. The first option is safer.
   - Update facts.md row 91 to say "12% of the 501 declined species" and drop the 1980s clause.
   - The word count must stay at 2,900 or more. The first option adds 2 words (2,922). The draft 1 wording keeps the total at 2,920.

**Recommended, not blocking:**
- Put the exact CDC wording in facts.md row 117.
- Preview "bangbangus" in `narrate`.
- Opener plus item 1 is at 275. That's fine, but don't trim it further.

When fix 1 is made as written, no other changes are needed for a PASS. A re-screen of that one line is enough.
