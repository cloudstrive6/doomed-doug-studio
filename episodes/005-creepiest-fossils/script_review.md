# Script review: 005 Creepiest Fossils (draft 3, round 3)

Screener, 2026-10-01. Inputs: style bible section 7, brief, script.md (draft 3), facts.md, round-2 review. Metrics recomputed independently.
Scope: verify the draft-3 fixes, then run a regression sweep (word count, sentence stats, TTS characters, tic counts, marker rotation,
segment bands, opener timing).

**VERDICT: PASS**

| Check | Result |
|---|---|
| Round-2 fixes | F3 verified. Optional A4 and marker variation applied |
| Facts | 0 FAIL items. 1 advisory (A6) |
| Hook | **8/10** (unchanged) |
| Structure & pacing | **8/10** |
| Voice & humour | **8/10** |
| TTS | PASS (no digits, symbols or parentheses in the narration) |
| Policy | PASS |
| Length | 3,252 spoken words (brief 3,100-3,400), about 16:41. PASS |

---

## 0. Draft-3 fixes
| Fix | Status |
|---|---|
| F3 Gogo | Done. "As a group, arthrodires ranged from small bottom feeders to six-meter top predators, longer than a family car." I re-checked Curtin: the range ("moochers of the ocean floor to six-metre apex predators") describes the group. facts.md now notes that the range is order-level (Dunkleosteus) and that the Gogo fish were small. The analogy stays (rule 8). The Doug beat ("biggest armored fish he can find") now reads as relative, so it no longer puts a six-meter fish on the reef. Sentence is 19 words |
| A4 Messel hedge | Done in the frame ("nine suspected pairs… every pair seems to have died") and the twist ("as of that study, no other… were known"). Re-checked NatGeo: nine suspected pairs over 30 years, each male-female, Joyce quote matches. See A6 |
| Twist markers | Lyuba is now "Then the mud did something strange." Zhùr is now "Then scientists checked her diet." No marker appears twice in a row. The "The [adjective] part" pattern is down from 6 to 4 |

## 1. Regression sweep
- **Opener:** item 1 name still at spoken words 30-34, and the twist is still at word 137. There is no greeting, channel name or subscribe ask. Rules 2 and 6 PASS.
- **Rule 4 frames:** the new Messel frame is 27 words (limit 15-35). The Gogo item is 257 words, and Messel is 263. Both are inside the brief's 240-280 band.
- **Rule 9:** 211 sentences, average 15.4 words, max 30. PASS.
- **Rule 13:** "actually" 2, "essentially" 1, "However" 0, "incredibly" 0. Rotation is OK.
- **TTS:** I scanned the narration for digits and the characters `% & / ( )`. None found.
- **Script Writer rules 1-14:** I found no violations.
- I found no other text changes outside the three fixes.

## 2. Advisory (not blocking)
- **A6 Messel internal consistency.** The frame is now hedged, but line 174 still says flatly: "Over about thirty years, researchers have
  recovered nine pairs… Each pair is a male and a female, preserved together while mating." NatGeo puts only two couples with tails in
  mating position. The Joyce 2012 paper interprets all nine as couples that died during copulation, so this line is sourced and is not
  a FAIL. Optional: to match the frame, change it to "preserved together, apparently while mating."
- Lyuba and Zhùr markers are softer pivots than a classic marker. They still flag the twist, so they are acceptable.

## Required fixes
None. The script is cleared for `script_approved`.
