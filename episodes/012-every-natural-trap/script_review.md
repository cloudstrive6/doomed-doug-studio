# Script review: 012 Every Natural Trap (draft 3)

Script screener, 2026-10-09, final re-screen. I read the style bible section 7, the brief, script.md (draft 3), facts.md, and the draft 2 to draft 3 diff (commit 6553b7e). Measurements come from textstat 0.7.13 on spoken text only. Comments, markdown headings and bracketed stage directions were removed. The headers and outro that are spoken were kept.

| Check | Result |
|---|---|
| Draft 2 fixes 1-3 | **All 3 applied and correct** |
| 1. Facts | PASS: 0 errors (13 claims re-checked on the web) |
| 2. Opening / hook | **8/10**, PASS |
| 3. Structure & pacing | **8/10** |
| 4. Voice & humour | **8/10** |
| 5. TTS readiness | PASS |
| 6. Policy | PASS: 0 items |
| 7. Length | PASS: 2,949 spoken words, about 15:07. The brief's band is 2,900-3,300 |
| Section 7 rules 1-14 | All met. No violations |

---

## Draft 2 fixes: verification
| # | Fix | Status |
|---|---|---|
| 1 | F1, Dead Sea rate | Done. Line 173 now reads "by twenty fifteen around four hundred new holes were being reported every year". This matches NBC 2015 (re-read on the page today: "400 sinkholes are now reported... every year", article dated 2015-07-18). "The sea is still shrinking" is supported by current sources (UNEP, about 1 m a year; the 2026 *Water* review, 0.7-1.5 m a year). The facts.md row is updated. The kicker is 19 words |
| 2 | Rule 4, Slot Canyon kicker | Done. "Nobody ever said the water was finished with it." is 9 words, and the joke is intact |
| 3 | Rule 9, Flesch | Done. **My textstat run gives 70.85**, which matches the writer's 70.8 and is inside 60-72. There are 174 sentences, the average is 16.9 words and the longest is 33 words (none over 35). The gag fragments are kept |

## 1. Facts (13 claims re-checked on the web, all OK)
- **Dead Sea (NBC 2015, re-read):** a 100 ft drop since 1980; about 30% from mineral extraction; as many as 5,000 sinkholes since the 1980s; up to 80 ft across; a salt layer 10,000 years old; the resort parking lot; 400 a year (now dated).
- **The sea is still shrinking:** about 1 m a year today (UNEP hotspots; the 2026 MDPI *Water* review).
- **Antelope Canyon:** 12 August 1997, 11 dead, very little rain at the site (NOAA record via Wikipedia).
- **Brinicle:** filmed in 2011 for BBC *Frozen Planet* at Little Razorback Island. Miller's quote is "five, six hours".
- **Avalanche:** n = 638 complete burials in open terrain, with survival falling steeply after 18 minutes (Brugger). The line stays in the past tense and is attributed to one study, so it remains true despite the 2024 JAMA update.
- **Tsanfleuron:** the couple vanished in 1942 and were found in July 2017 by a Glacier 3000 worker. The director's crevasse quote is correct.
- **Valais:** police keep a register of about 300 missing since 1925 (Blick, Futura; Reuters gave 280 in 2017).
- **La Brea:** about 90% of mammal fossils are carnivores (NHM and UCMP), and the dire wolf is the most common large animal. Over 600 species is a fair floor (Carleton counts 624).
- **Altamura:** found in 1993 in Lamalunga; 172 ± 15 to 130.1 ± 1.9 ka (Lari 2015); covered in calcite and left in place to avoid damage; a scapula fragment was retrieved.
- **Amber:** about 70,000 droplets of 2-6 mm; 1 fly and 2 gall mites; about 230 Myr; about 100 Myr older than any earlier amber arthropod; the mites probably fed on the tree that preserved them (Schmidt 2012 PNAS, ScienceDaily, Live Science).
- **The merged sentences change no claim.** "Colder and saltier", "scientists decided that moving the skeleton could cause damage" and "someone had got there first, a Neanderthal" are all still covered by their rows.

## 2. Opening: 8/10
- "Tree well." starts at spoken word 32. Nothing banned comes before it.
- The twist is flagged by "Notice what is missing." at word 116 and ends at word 144 ("...safest place on the whole mountain."). The merge added 3 words, but the twist still lands inside the 145-word limit (rule 6). **It is now tight.** Do not add words before line 25 in later edits.

**Section 7 rules:** rules 1-14 are all met. Notes on the ones checked:
- Rule 4: the kickers are 9-22 words, and every Doug beat is unchanged.
- Rule 9: average 16.9, max 33, Flesch 70.85, and every item has a sentence of 6 words or fewer.
- Rule 13: "actually" appears 2 times, and the other tics 0 times. No twist marker appears twice in a row.
- Rule 14: no new phrasing was added.

## 3. Structure and pacing: 8/10
- Nothing has changed since draft 2. The axis is monotonic, the boss is the most extreme item, and the headers are at 52% and 74%. There are no transitions. Every gag is present, the counter runs from 100 to 107, and the outro is 18 words.
- Advisory: Brinicle is 329 words against a target of 290-320, and Amber is 425 against 380-420. Crevasse is at the top of its band at 350.

## 4. Voice and humour: 8/10
- The rule 9 miss is fixed. The merges read naturally and give the mechanism lines a longer rhythm, while the deadpan beats stay short. The narrator persona is consistent. The voice is adult and dry, with US dialect throughout.

## 5. TTS readiness: PASS
- The spoken text has no digits, symbols, abbreviations or parentheses.
- The editor should preview Tsanfleuron, Lamalunga, Valais and brinicle with `narrate`.

## 6. Policy: PASS, 0 items
- No injury or death-process description and no profanity.
- Real victims get dates and counts only, with no jokes in their fact lines.
- The tone is not kids-coded.
- The narrative is original.
- There is no safety or rescue advice.
- The title promise holds: 7 deaths in 9 traps.

## 7. Length: PASS
2,949 words, about 15:07 at 195 wpm.

---

VERDICT: PASS

Required fixes: none.

Advisories (not blocking):
- Keep the 18-minute avalanche line in the past tense.
- The Tree Well twist now ends at word 144, so do not lengthen lines 7-25.
- Brinicle and Amber are a few words over their targets. The editor can trim them if pacing calls for it.
