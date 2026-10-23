# 026 Script Review: Why the Deep Sea Turns Animals Into Terrifying Giants (draft 3)

Script screener, 2026-10-23. Inputs: style bible, series bible, brief, script.md (draft 3, commit 944761c), facts.md, my draft 2 review, the 311ea70 → 944761c diff, and a grep of every earlier script for repeated gags.

**VERDICT: PASS**

Both draft 2 blocking fixes are resolved, and nothing regressed. The word counts I re-measured match the writer's footer exactly.

| Check | Result |
|---|---|
| Facts | **PASS**: 0 errors (10 claims checked on the web this round, plus the changed lines) |
| Opening / hook | **8 / 10** |
| Structure & pacing | **8 / 10** |
| Voice & humour | **8 / 10** |
| TTS readiness | **PASS** |
| Policy | **PASS**: 0 items |
| Length | **PASS**: 3,040 spoken words (brief 3,000-3,300), about 15:35 |

## Draft 2 fixes: status
| # | Fix | Status |
|---|---|---|
| 1 | Giant Cell at 320 words or fewer | **Resolved.** The item is 314 words without the outro (333 with it), against the brief's cap of 320. The callback is now one spoken sentence of 17 words: "The cable passes the depth of the deepest fish ever filmed, the snailfish from Doug's first trip." It is also strictly true now. PRESSURE? is a stage direction only. The *Syringammina* line is cut, and its facts.md row is deleted. The footer counts are updated. |
| 2 | New sea spider death | **Resolved.** In the new death, Doug puts a stethoscope to a leg and hears digestion, then the spider steps on him. There is no breath-hold and no "blend in". It comes from the gut-in-the-legs and gut-pump facts. The Doug line is 19 words, and the death is cut on the step. The cap leaves on the leg. "It has the legs for it" is gone, so the item has two joke lines plus the Doug beat. The grep found no repeat: 015's stethoscope was a vet-and-breath-mint gag, and in 010 Doug stepped on a snake, not the reverse. |

Draft 2 advisories:
- **Done:** "Here's what makes it worse." is now "The catch is that". Greenland Shark is down to 286, inside its 240-290 band. Flesch is 71.45, up from 71.87. Item 1 lost 4 words above the twist, which is now at word 141.

## 1. Facts: PASS (10 checked on the web this round)
| # | Claim | Verdict | Source |
|---|---|---|---|
| 1 | Greenland shark: "one of the slowest fish ever measured for its size, cruising slower than most people walk" (reworded) | PASS | Watanabe et al. 2012, "The slowest fish": 0.34 m/s, the lowest for its size. "For its size" covers the later dwarf-seahorse caveat. |
| 2 | Snailfish callback: the deepest fish ever filmed, and the cable passes "the depth of" it | PASS | UWA, Smithsonian and NPR: 8,336 m, Izu-Ogasawara. With "depth of", the trench mismatch I noted in draft 2 is gone. |
| 3 | Sea spider: the weak heart barely moves blood beyond the middle; the gut pumps in the legs (2017) | PASS | Woods et al. 2017, *Current Biology*, via Cosmos: 12 species. The script says "in sea spiders". |
| 4 | *C. colossea* has a leg span of about 70 cm and a body of about 7 cm | PASS | Guinness and Wikipedia |
| 5 | Lives from about 400 to more than 5,000 m | PASS | Wikipedia: 420-5,200 m |
| 6 | Xenophyophores at 10,641 m, Sirena Deep, July 2011, Scripps; often more than 10 cm; "scientists call them the largest single cells" | PASS | Scripps and UCSD. The claim is attributed to scientists, which is fine. |
| 7 | Toba isopod: January 2009, about 50 g fish, died February 2014, more than five years | PASS | SoraNews24 and Practical Fishkeeping |
| 8 | Colossal squid: first live footage in March 2025 near the South Sandwich Islands, a juvenile of about 30 cm | PASS | Schmidt Ocean Institute and National Geographic |
| 9 | Oarfish: 2019 study, more than 300 sightings against more than 200 earthquakes since 1928, one possible match | PASS | Orihara et al. 2019, *BSSA*: 336 sightings, 221 earthquakes |
| 10 | Bigfin: deepest squid filmed in the Philippine Trench; about 70 ever seen | PASS | Guinness and Smithsonian (6,212 m); MBARI (about 70) |
| 11 | Supergiant amphipod: 2025, about 200 records from about 3,900 to almost 9,000 m, more than half the oceans, populations connected | PASS | Maroni et al. 2025, *R. Soc. Open Sci.*: 195 records, 3,890-8,931 m, about 59% |

Every other change in the diff is wording only ("hangs", "deliberately", "comfortable, warm chimney"), so no claims changed. The new Doug beat maps to a facts.md row marked as cartoon premise.

## 2. Opening (8/10) and Script Writer rules 1-14
| Check | Result |
|---|---|
| Item 1's name | Word 32-33 (within 35) |
| Before item 1's name | No greeting, channel name or "in this video" |
| Twist | "Here's the problem." is at word 141, within about 145 |

**Rules violated: none.**

| Rule | Measured |
|---|---|
| 1 | 3,040 words |
| 3 | 11 items |
| 4 | **Acceptable at item 11.** The first beat after "The Giant Cell." is now the 17-word one-line callback the brief allows, followed by a 32-word frame. |
| 5 | Monotonic, 250 → 10,641 m |
| 7 | Clean |
| 8 | Clean |
| 9 | Average 14.5, max 34, Flesch 71.45 (cap 72) |
| 10 | Sea spider now has two jokes plus the Doug beat |
| 11 | Clean |
| 12 | Outro 19 words |
| 13 | Markers rotate. "The catch is that" is new, and "It gets stranger." now stands alone. |
| 14 | Clean |

## 3. Structure & pacing (8/10)

Word counts per item:

| Item | Words |
|---|---|
| Opener | 31 |
| Giant Oarfish | 267 |
| Japanese Spider Crab | 273 |
| Giant Phantom Jelly | 255 |
| Giant Isopod | 288 |
| Colossal Squid | 283 |
| Greenland Shark | 286 |
| Giant Tube Worm | 260 |
| Bigfin Squid | 240 |
| Giant Sea Spider | 262 |
| Supergiant Amphipod | 262 |
| The Giant Cell | 314 + outro 19 |

- **The boss is inside both the brief cap (320) and the bible band (300-380).** The reveal is no longer held back.
- **Escalation and gags hold:**
  - Depth bands: Big. / Bigger. / Too deep.
  - The counter goes from 210 to 218, with eight deaths in order.
  - There are three "Doug is fine." lines.
  - The cap appears in every item.
  - The clipboard reasons build up as before.
  - The ending is the LIVE feed per the bible.
- **Advisory, carried over:**
  - Isopod (288) and Spider Crab (273) are over the bible's 230-270 band for items 2-4.
  - Both are inside the brief's 260-290 average.

## 4. Voice & humour (8/10)
- The narrator stays consistent, and no competitor phrasing was found.
- The new death is fresh and specific to the animal.
- "The spider needs that leg back immediately." is a dry, adult-coded punchline.
- Minor, not blocking: "Doug has died. Again." appears at deaths 212 and 218. That is fine as a deliberate bookend.

## 5. TTS readiness: PASS
- No digits, symbols, abbreviations or parentheses in the spoken text. "8,336 M" appears only in a stage direction.
- Respellings cover every hard word.
- "Izu-Ogasawara" stays in the pronunciation list but is no longer spoken. This is harmless.

## 6. Policy: PASS
- **Advertiser-friendly:**
  - The step death is cut on the moment, with X eyes and no crushing description.
  - There is no on-screen suffocation beat now.
  - No profanity.
- **Made for kids:** the tone is adult-coded, and there are no nursery words.
- **Inauthentic or repetitive content:** the narrative and why-thread are original, and the 001 and 023 overlaps are cleared.
- **Advice and title promise:** no advice. The honesty line is present, and the title promise is delivered.

## 7. Length: PASS
3,040 words, about 15:35, inside 3,000-3,300.

## Advisories for downstream (not blocking)
- **Length:** only 40 words above the floor. Do not cut further in direction or edit without re-counting.
- **Item 1:** do not add words above the twist (word 141).
