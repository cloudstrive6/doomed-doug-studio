# Script review: 040 The Most Horrifying Things Nature Kept Trapped the Longest (round 2, draft 2)

Script screener, 2026-11-08. I re-read script.md, facts.md and brief.md (draft 2) against my round 1 fixes and checked every changed line.

VERDICT: FAIL

There is one required fix, a single line. Everything else from round 1 landed. Scores: hook 8, structure 8, voice 8. Policy: 0 items. Length: 2,017 spoken words (my count matches the writer's), within 1,950-2,350.

## Round 1 fixes: status
| # | Fix | Status |
|---|---|---|
| 1 | "only took mammoths" changed to "mostly took mammoths" (item 6 kicker, item 7 Doug beat) | LANDED (lines 300, 336). Now consistent with the short-faced bears at line 310. |
| 2 | URL for "millions of times less energy" | LANDED. facts.md row 147 cites the AFP story on Vietnam News, which I verified in round 1. FLAG 9 updated. |
| R | Sober bridge at the end of item 1 | ADDED, but it introduces a new fact error. See required fix 1. |
| R | "the only person on this list who walked out" | LANDED, and it is true (items 1, 3 and 4 did not survive). |
| R | yedoma pronunciation | LANDED (script comment, and config/channel.yaml line 57). |
| R | Thumbnail A worm/seafloor mismatch | Noted in brief.md and facts.md FLAG 10. Not blocking. The opening stage direction in script.md (line 16, "dark layered seafloor mud ... huge curled worm") still describes the old image. The graphic designer and director should follow the brief note, not that line. |

## Required fixes
1. **Fact error in the new item 1 bridge: "That cave closed in about a day."** It comes straight after "Within a week, the cave was sealed with explosives and cement." A listener hears "closed" as "sealed", and the cave was sealed about a week later, not after a day. The writer meant the 27 hours he was trapped (facts.md, Draft 2 corrections). Change the line to say the cave held him, for example: "That cave held him for about a day. The next trap took months to let go." Keep it sober, with no joke. Nothing else needs to change.

## Re-checks on draft 2
- **Opening:** unchanged. The item name is at word 34 and the twist at word 97. Retention rule 6 at the end of item 1 is now met once fix 1 is made.
- **Rules (section 7):** rule 11 is now met. No new violations, apart from the factual wording in fix 1.
- **TTS:** the new lines are clean, with no symbols or numerals.
- **Policy:** the new bridge has no joke, no injury detail and no name. 0 items.

---

# Round 1 (draft 1), kept for the record

# Script review: 040 The Most Horrifying Things Nature Kept Trapped the Longest (draft 1)

Script screener, 2026-11-08. I read the style bible (including the Retention update of 2026-10-27), the series bible, brief.md, script.md and facts.md.

VERDICT: FAIL

The draft is close. The verdict is FAIL only because of two fact items. Both are one-line fixes. There are no policy items, and all three scores meet the bar (hook 8, structure 8, voice 8).

## Required fixes
1. **Fact error: the mammoth sinkhole did not take only mammoths.** The script contradicts itself. Item 7's first sentence says the sinkhole also gave up "giant short-faced bears", and facts.md row 120 sources that. Two lines are therefore false:
   - Item 6 kicker: "The next trap was picky too. It only took mammoths, and mostly the young males." Change this to something true, for example "The next trap mostly took mammoths, and mostly the young males."
   - Item 7 Doug beat: "The sinkhole only took mammoths, so Doug went as one, young, male and unsupervised." Change it to "mostly took mammoths" (or similar). Keep the costume logic, but drop "only".
2. **Fact without a source URL: "The microbes down there get millions of times less energy than microbes near the surface" (item 8).** facts.md row 138 and FLAG 9 say "search text" and give no URL, which fails Script Writer rule 11. I traced the quote: it is Morono's line in the AFP wire story, carried by Vietnam News (https://vietnamnews.vn/life-style/770283/scientists-revive-microbes-from-100-million-years-ago.html). It is **not** in the EurekAlert/URI release, which I fetched. Add that URL to row 138. If it can't be added, cut the sentence.

## Recommended (not blocking)
- **Item 1 ending (retention rule 6).** Item 1 ends on a full stop at about 1:25: "Within a week, the cave was sealed with explosives and cement." There is no lean into the next item. The sober tone is correct and is required by the brief. But a short, sober bridge would help before "Months.", for example a line saying the cave held him for hours and the next trap held on for months. Use the writer's own wording, and don't make a joke near the real case.
- **"Two months is the longest any person on this list was held and walked out."** This is true, but he is the only person on the list who walked out, so the superlative is empty. Consider "the only person on this list who walked out".
- **Pronunciation:** add "yedoma" (YED-oh-mah) to the pronunciation comment and `voice.pronunciations`.
- **Note for the thumbnail (outside script scope):** in thumbnail A, the worm sits in *seafloor* mud. The worms came from Siberian permafrost, and the seafloor item is microbes. Tell the graphic designer, so the opening image doesn't show a mismatch the script never pays off.

## 1. Facts: 13 claims checked by web search
| Claim | Result |
|---|---|
| Mammoth Site re-dated to 160,000-232,000 years, *Quaternary Research*, 11 Aug 2026, IRSL on feldspar | Confirmed (USGS publication page; Mammoth Site release). The order change is justified. |
| Old radiocarbon put it at about 26,000 years | Consistent (published radiocarbon range about 23-42 ka) |
| Nutty Putty sealed with explosives and cement about a week later | Confirmed (KSL; UPI 4 Dec 2009; Salt Lake Tribune: concrete plug) |
| Extraction judged too dangerous; family part of the decision | Confirmed (KSL) |
| Swedish car: since 19 Dec, found in Feb 2012 by snowmobilers, forest track near Umeå, no food, ate snow | Confirmed (NBC, The Local, Irish Times) |
| Hibernation idea came from a doctor | Confirmed; the script correctly frames it as an idea |
| Hoyo Negro: the most complete skeleton older than 12,000 years | Confirmed (ScienceDaily, Northwestern) |
| More than 26 large mammals, including sabre-toothed cats and ground sloths; a gomphothere | Confirmed (ScienceDaily) |
| Naia dated 12,000-13,000 years | Confirmed |
| Ötzi: pneumatic drill damage; bow broken during recovery, the lower part recovered a year later | Drill confirmed (Wikipedia). The bow detail rests on Wikiwand/Wikipedia; acceptable. |
| Seafloor: up to 99.1% alive, 101.5 Ma, nearly 6,000 m, 100 m below the seafloor, oxygen in all cores, fewest nutrients | Confirmed (EurekAlert, fetched) |
| "Millions of times less energy" | Quote exists (AFP via Vietnam News), but there is no URL in facts.md. See fix 2. |
| Sinkhole "only took mammoths" | Contradicted by the script and by facts row 120. See fix 1. |

Arithmetic I checked: 86,400 × 5,300 / 101.5M = 4.5 s; 0.76 mm / 1,000 nm = 760; 61 m is more than 48.8 m. All correct. The facts.md FLAGS (Ötzi gully dispute, Seafloor oxygen reversal, the two doctors) are handled honestly in the script.

## 2. Opening / retention test: 8/10
- First sentence: "Utah sealed a cave, because the last man who went too deep is still inside." Concrete, a death stake, no scene-setting. PASS. It has no number, but the death stake satisfies the rule.
- Payoff promise by about 0:10: "By the end, Doug spends a hundred million years under the seafloor, and his neighbour wakes first." Specific, unresolved, and paid off in item 8. PASS. It is slightly vaguer than the brief's "the thing buried next to him".
- Item 1 (Nutty Putty) is one of the three strongest, and it opens on the 10 by 18 inch gap fact. PASS.
- The item name is at word 34 (35 or fewer). There is no greeting, channel name or subscribe ask. PASS.
- The twist marker "Here's the problem." is at word 97 (145 or fewer). PASS.

Script Writer rules (section 7) violated: **rule 11** (fix 2). Rules 1 and 3 are superseded by the Retention update: 8 items and 2,003 words are correct. Retention rule 6 is weak at the end of item 1 (recommended above). All other rules are met:
- Rule 4: every beat is present. Doug beats run 18-29 words.
- Rule 5: the axis is declared and the boss is last.
- Rule 7: there are no transition sentences between items.
- Rule 8: each item has a scale analogy (carry-on, duvet, garage, football field, ten storeys, bank card, six storeys, one-day clock).
- Rule 9: average sentence 14.3 words, longest 33, and every item has a sentence of 6 words or fewer.
- Rule 12: the outro is 18 words.
- Rule 13: "actually" appears once, and all 8 twist markers are different.

## 3. Structure and pacing: 8/10
- The duration axis rises cleanly: 27 hours, then 2 months, 5,300 years, 12,000 years, 46,000 years, 48,500 years, 160,000-232,000 years and 101.5 million years.
- The re-dating is integrated well: it gets a new "Hundreds of thousands of years." band and becomes a mini-twist inside item 7.
- Item lengths are 227-268 words, close to the 200-260 band (the boss is allowed to run longer).
- The death counter goes from 308 to 315 with 7 deaths. Item 2 is a survival with no sticker. Death 310 is played flat. The suitcase ends full, and the cap survives every item.
- The ending follows the bible: the boss kicker, then a one-line counter update and a comment CTA, with no recap.

## 4. Voice and humour: 8/10
- The narration is deadpan and dry. "Possibly in the Cretaceous." and "makes it look like a lunch break" land.
- The narrator's disappointment at the survival ("The suitcase stays empty, which was not the plan.") is on-model.
- The costume logic line is varied the second time ("young, male and unsupervised").
- No competitor phrasing was spotted.
- "Doug has died. Again." appears 6 times. That is the series tic and acceptable, but it is near the point of fatigue.

## 5. TTS readiness: PASS
- All numbers are spelled out, with no symbols or parentheses in the narration.
- "DNA" is the only abbreviation; Chirp reads it fine.
- Add "yedoma" to the pronunciations.

## 6. Policy: PASS (0 items)
- Real deaths: there are no names. Nutty Putty gets only the one plain "strain" clause. There is no injury or rescue-injury detail, and no Doug joke on the same card as a real case. Ötzi gets only "the drill damaged him", which the brief allows. Hoyo Negro is described as "a young woman", with no age and no nickname.
- No gore, no profanity and no shock-for-shock.
- The tone is adult-coded, with no kids-show framing.
- The virus item states plainly that the virus is amoeba-only and gives the paper's "totally negligible" risk line. There is no "zombie" and no pandemic angle.
- There is no safety or medical advice; the hibernation idea is framed as an idea.
- The narrative and commentary are original and distinct from earlier episodes. There is no overlap with 004, 012, 020 or 030.

## 7. Length: PASS
2,003 spoken words (my count matches the writer's), about 10.3 minutes at 195 WPM. That is within 1,950-2,350, at the low end. Don't cut anything further when making the fixes.
