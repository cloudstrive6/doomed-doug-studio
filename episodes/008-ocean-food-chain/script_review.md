# Script review: 008 Every Step of the Ocean Food Chain (round 3)

Screener, 2026-10-05. Reviewed draft 3 (commit 5a8d7fd) against the style bible, the series bible, brief.md and facts.md.
Draft 3 changed only the Great White item, the facts.md entry for item 9, a blank line at line 72, and the header comments.
I re-ran the whole-script checks to make sure nothing regressed.

VERDICT: PASS

| Check | Result |
|---|---|
| Facts | **0 errors.** The round-2 fix is done, and both new claims are verified against the full text of the paper. |
| Hook | **9/10** (unchanged) |
| Structure & pacing | **8/10** |
| Voice & humour | **8/10** |
| TTS readiness | Pass |
| Policy | Pass |
| Length | Pass: 3,044 spoken words (brief 2,900-3,400), about 15:37 at 195 wpm |
| Script Writer rules violated (section 7) | **None** |

## Required fixes
None.

## Round-2 fix: verification
| # | Fix | Status |
|---|---|---|
| 1 | Seal Island count | **Done.** Line 325 now says "Along with more than two thousand real attacks, they recorded over a hundred strikes on fake seals". facts.md now says "2,088 natural predations (1997-2003)" and has the full-text PDF URL. I re-read the PDF: the abstract and the Results both say 2088, and there were 121 decoy strikes. |
| Adv. | Blank line between the moray diagram and "But that's not the disturbing part." | **Done** (line 72). |

## 1. Facts: the new Great White lines (checked against the full text of Martin et al. 2005)
| # | Claim (line) | Result |
|---|---|---|
| 1 | "more than two thousand real attacks" (325) | OK. The abstract and the Results both say "2088 natural predatory interactions". |
| 2 | "over a hundred strikes on fake seals" (325) | OK (121). |
| 3 | "Over a whole day, it's closer to a coin toss." (323) | OK. The Results say "Mean predatory success rate was 47.3%". This is set against 55% in the first hour after sunrise. |
| 4 | "zigzags, or does a headstand underwater to look for the shark" (323) | OK. The Methods say seals switch "from directional porpoising to either zigzag evasive manoeuvres or head-stand subsurface scanning, with indications of a shark in pursuit". "To look for the shark" is a fair plain-English version of "subsurface scanning". |
| 5 | Over half succeed just after sunrise, success falls with light, they stop hunting (321) | Still OK (55%; they stop at about 40%). |

The round-1 checks (16 claims) and round-2 checks (13 claims) still hold. No other factual line changed.

## 2. Opening: 9/10
- The opening is unchanged. "Mantis Shrimp." comes at words 32-33, and the twist ends at about word 121.
- Script Writer rules 1-14 all pass. Whole-script stats were re-run on draft 3:
  - Average sentence length is 14.4 words and the longest is 34.
  - Flesch reading ease is about 71.
  - "essentially" and "incredibly" are each used once, and "However" and "actually" are not used.
  - The twist markers come in this order: disturbing, problem, impossible, worst, strange, problem, disturbing, strangest. No marker appears twice in a row.
  - The Great White kicker (the Farallon line, 23 words) is still the last sentence of the item.

## 3. Structure & pacing: 8/10
- The Great White is now 267 words, so it meets the 260 floor for items 9-11. The point lost in round 2 for this is resolved.
- Every item is within the bible's range.
- Section headers fall at about 28%, 53% and 87%.
- The running gags, both survivals and the ending are unchanged.
- The creative director still has to approve the position of "No predators." (87% rather than the brief's 70%).

## 4. Voice & humour: 8/10
- "Closer to a coin toss" is plain, deadpan and original. It does not appear in the competitor data.
- The new paragraph adds no joke lines, so the joke density is unchanged.

## 5. TTS readiness: Pass
- There are no digits, symbols or parentheses in the spoken lines.

## 6. Policy: Pass
- The new lines describe evasive behaviour only, with no injury detail.
- There are no other policy changes.

## 7. Length: Pass
- 3,044 spoken words.

## Advisory (not blocking; the writer can take or leave these)
- Line 323, "A seal that realizes it's being chased zigzags": TTS may read this as "chased zigzags" for a moment. Preview it with
  `narrate`. If it stumbles, "When a seal realizes it's being chased, it zigzags, or ..." reads cleanly.
- Line 323, "Over a whole day": this comes straight after "they stop hunting", so "Averaged over every attack, it's closer to a
  coin toss" would match the paper's "mean predatory success rate" more exactly. The current wording is acceptable.
- Creative director: approve the position of "No predators." at the script gate.
