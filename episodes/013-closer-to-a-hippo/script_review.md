# Script review: 013-closer-to-a-hippo (draft 3, round 3)

Script screener, 2026-10-09. This is a scoped re-screen, as round 2 promised. I checked the three flagged lines, the word count, and the diff
from draft 2 to draft 3 (commit a47fbd2) for new issues. Everything outside the diff carries over from round 2 without change.

## Scorecard

| Check | Result |
|---|---|
| 1. Facts | **PASS**: F6 and F7 are fixed, and no other fact error is open |
| 2. Opening | **8/10** (unchanged, the opener is not in the diff) |
| 3. Structure & pacing | **8/10** (unchanged) |
| 4. Voice & humour | **7/10**: R3 is fixed and the replacement line works |
| 5. TTS readiness | PASS (1 advisory carried over: the editor must audition "hipposudoric") |
| 6. Policy | PASS (0 items) |
| 7. Length | **PASS**: 2,904 spoken words (brief 2,900-3,300), about 14:54 at 195 wpm |

**Script Writer rules violated (section 7):** none. The rule 11 issues from round 2 (F6 and F7) are fixed.

---

## Round 2 fixes: did they land?

| # | Fix | Status |
|---|---|---|
| 1 | F6, The Charge: change "frequently" to "sometimes" | **Landed.** The line now reads "limited and sometimes contradictory". This is the exact wording of the PeerJ abstract (PMC11227274), and it matches facts.md row 69 |
| 2 | F7, The Canoe: delete "great" | **Landed.** The line now reads "one of the last hippo strongholds in Africa". This matches the Mongabay headline ("one of Africa's last strongholds") and facts.md row 123 |
| 3 | R3, The Mouth: replace the soft recap | **Landed.** The new line is "There is no distance left to close now. Doug has closed all of it himself, on foot, on purpose, holding a salad, and smiling the whole way." It does not summarise earlier items, and it no longer claims this is Doug's first deliberate approach. "On foot" matches the setting, because Doug is standing at the river's edge. The line also lands the distance axis at zero |

## Length
- The edits change the count by -10 words: F6 is a straight swap (0), F7 drops one word (-1), and R3 goes from 36 words to 27 (-9).
- Starting from the round 2 measurement of 2,914, draft 3 comes to **2,904**. This matches the writer's own count. I ran a separate diff count on draft 2 and draft 3 and it also gives -10.
- The total is at or above the 2,900 floor, so this check passes. The margin is now only **4 words**. Any later edit that cuts words, from the director or the editor, must add the same number back. If words need to be added, put them in The Night Walk (222 words).

## New issues from the diff
None that block the script. Two advisories:
- "There is no distance left to close now." comes about 300 words after the item's opening line, "There is nowhere closer to go." The two lines make the same point. That works as a bookend, but it is close to repeating itself. The writer may change one of them but does not have to.
- "holding a salad" means the lettuce. This wording was already in draft 2. It is a joke, not a mistake.

## Carried over (advisory only, not required)
- The Honk: "louder replies" is stronger than the source, which says "responding vocally". "Stronger replies" would be safer.
- The Shallows: the subject changes from plural to singular ("Their bodies ... Its closest living relatives").
- facts.md row 57 still lists a Night Walk line that is no longer in the script. Add Science News (Milius, 2004) to facts.md as a second source for the red sweat pigments.
- Residual policy risk: keep "cocaine" out of the title, the thumbnail and the tags.

---

VERDICT: PASS

There are zero fact errors and zero policy items. Hook 8, structure 8, voice 7. The spoken word count is 2,904, which is within the brief's
2,900-3,300 range. The script can go to `script_approved`.
