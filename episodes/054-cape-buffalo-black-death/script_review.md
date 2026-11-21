# 054 script review (round 3, draft 2), script screener, 2026-11-21

**VERDICT: FAIL** (1 required fix, a one-line on-screen sign. Everything else passes.)

Draft 2 is confirmed. script.md and facts.md were saved at 17:25. The header and footer say "draft 2", and status.json has a "draft 2" entry at 17:25:26. I checked every round 1 fix against the file text, not against the writer's notes.

| Check | Result |
|---|---|
| Facts | **FAIL**: 1 item (the on-screen sign at line 240, see fix 1). The spoken narration is clean. |
| Hook | **8/10**: passes the gate |
| Structure & pacing | **8/10** (R3 applied) |
| Voice & humour | **8/10** |
| TTS | PASS: no digits, symbols, parentheses or abbreviations in spoken lines |
| Policy | PASS (0 items) |
| Length | PASS: 2,115 spoken words, about 10.8 min (target 1,950–2,350) |
| Writer rules violated (1–14) | none (rule 1 is overridden by the retention update) |

## Fix status (round 1 numbering)

| # | Item | Now (line) | Status |
|---|---|---|---|
| 1 | F1: weight sourced to a booking site | 62 "A big bull can weigh more than eight hundred kilograms." Label 60 "800+ KG" / "ABOUT 730 KG". Facts rows updated to ADW. | **FIXED** |
| 2 | F2: "almost completely black" | 22 "Old bulls are often seen caked in a crust of dried mud." Label is "DRIED MUD". | **FIXED** |
| 3 | F3: "every single resident" | 324 "every adult resident" (and the stage direction at 322) | **FIXED** |
| 4 | F4: "up to half a tonne each" | Spoken line 242 is fixed ("the cows weigh up to half a tonne and the bulls weigh more"). **The sign at line 240 now says "MOST OF US: HALF A TONNE+", which is false** (see fix 1). | **PARTLY FIXED** |
| 5 | F5: "lying down" with no source | 126 now cites Ryan & Jordaan 2005, *Koedoe* 48(2). "Lying down" is cut. | **FIXED** |
| 6 | F6: universal negative | 334 "we could not find any published count behind that number" | **FIXED** |
| 7 | H1: garden-path opener | 8 "Hunters call this animal the Black Death. It eats grass, and a bull can outweigh a small car." | **FIXED** |
| 8 | Rule 9: Carrier short sentence | 218 "It just stands there, chewing." (5 words, a new punch, not a split fact sentence). The item now has 2 sentences of 6 words or fewer. | **FIXED** |
| 9 | Rule 4: Bodyguards frame | 234: 21 words | **FIXED** (and the optional Lion Killer frame at 272 is now 19 words) |
| R3 | Megaherd "Here's the problem." | 326, now flags the 5,000-strong moving herd | **APPLIED** |
| — | Voting URLs in facts.md | Present (item 5 row and brief-check row) | **APPLIED** |

## Required fixes
1. **Line 240, sign text**: `"WE ARE WATCHING. MOST OF US: HALF A TONNE+"`. ADW (fetched) says "females weigh up to 500 kg". A breeding herd is mostly cows and young animals, so "most of us" are at or under half a tonne, not over it. The sign contradicts the spoken line under it and its own facts.md row. Round 1 asked for the sign to be changed to match the spoken line. Change it to, e.g., `"WE ARE WATCHING. COWS: UP TO HALF A TONNE. BULLS: MORE."` (or `"WE ARE WATCHING. EVERY ONE OF US: A PIANO+"`). Update the facts.md item 7 "Sign:" note to match. No other change is needed. After that edit, the script is a PASS without another full screen.

## Recommended (not blocking)
- **Line 324, piano**: facts.md supports "every adult outweighs an upright piano" with National Geographic's 660 lb (300 kg) lower bound. That figure covers all African buffalo, including forest buffalo. Against heavy uprights (Steinway, up to 302 kg) it is a tie at the bottom end. Add a Cape-buffalo-specific adult female weight to the facts row, or say "a piano" without "upright". Either way the claim holds for Cape buffalo, whose cows weigh well above 300 kg.
- **Lengths**: the Megaherd is 270 words, which is over the retention update's 200–260 per item. As the boss item it may be the longest (3.6), so this is acceptable. The Vote, at 208, is below the brief's 215 but inside the bible's band. Leave both.
- **Sentence average 14.1**: this is just inside the 14–19 band. Do not shorten any more sentences in later edits.

## Hook (8/10)
- First sentence: "Hunters call this animal the Black Death." It is a concrete death stake that the title promises, and it is attributed as a nickname. The second sentence gives the grass-eater versus small-car contrast. It parses cleanly when heard.
- Payoff promise at word 18–31 (about 0:09): "Later, Doug faces a thousand buffalo beside a lion, and the lion runs." It is specific, it does not resolve, and the lion does not die.
- "The Dagga Boy." is at words 32–34 (the limit is 35). There is no greeting, channel name or subscribe ask before it.
- Item 1 opens on its best fact (guides say the lone old bull is the dangerous one). Its twist marker, "Here's the strange part.", comes at word 128 (the limit is about 145). The twist itself, "The Black Death is mostly retired", is strong.
- Why not 9: sentence 1 has no number, and "It eats grass" is a mild beat right before the promise.

## Structure (8/10) and voice (8/10)
- The axis holds (one bull, then the herd, then a megaherd), with band headers in order. There are 6 deaths (396 to 402) and survivals at items 2, 3 and 7, as in the brief. "Doug did not agree to this." is used once, at item 1. The cow costume appears once. Nothing marks 400 as a milestone. The outro is 18 words, with the counter plus one fresh subscribe line.
- Twist markers rotate, and none repeats back to back. "actually" is used once. Every kicker is 8–25 words and leans into the next item. No sentence is over 35 words (the longest is 32).
- The tone is deadpan and adult-coded. There is no nursery framing, no cute calf, and the Battle at Kruger is told flat.

## Fact checks this pass (changed claims re-fetched)
| Claim | Check | Result |
|---|---|---|
| "herds rested more by day and fed more at night when the weather was hotter" (126) | Ryan & Jordaan 2005, *Koedoe* 48(2), a98, abstract fetched: more feeding at night (44.5% vs 32.0%) and more resting by day (28.4% vs 16.0%); in the hotter wet season, more resting by day and feeding at night. Lower Sabie is in Kruger. | OK |
| "A big bull can weigh more than eight hundred kilograms" (62) / outweighs a small car (8) | ADW fetched: "males can weigh over 835 kg while females weigh up to 500 kg" | OK |
| Car "ABOUT 730 KG" (60) | First-generation Smart Fortwo: 730 kg kerb weight (Wikipedia, Conceptcarz, Carsopedia); 795–805 kg with driver. Still under 835 kg. | OK |
| Cows up to half a tonne, bulls more (242) | ADW, as above | OK |
| Sign "MOST OF US: HALF A TONNE+" (240) | ADW, as above | **FAIL** (fix 1) |
| Old bulls caked in dried mud; udaka; leave at about 12 (22, 32) | Africa Geographic fetched | OK |
| Boss is solid bone covered in keratin (58) | Africa Geographic fetched | OK |
| Lions killed by horns and weight; a pride or coalition needed (276, 286) | Africa Geographic fetched | OK |
| Buffalo outrun lions by about 10 km/h (280) | ADW fetched | OK |
| Battle at Kruger: September 2004, Kruger watering hole, filmed from a vehicle, uploaded 2007, tens of millions of views, calf survives (248–256) | Wikipedia fetched (Transport Dam; 2 crocodiles, so "a crocodile" is true but incomplete; over 90 million views by 2023) | OK |
| Unchanged claims (oxpeckers, Ndlovu & Combrink 2015 6/855, Weeks 2000, Prins and the voting, Anipedia Corridor disease 80%, Botswana fences 10,000+ km, Londolozi super-herds, Discover Wildlife 3,000 and 5,000) | Checked in round 1; the wording is unchanged | OK |

Sources for this pass: https://koedoe.co.za/index.php/koedoe/article/view/98 · https://animaldiversity.org/accounts/Syncerus_caffer/ · https://africageographic.com/stories/buffalo-godfather-of-the-african-bushveld/ · https://en.wikipedia.org/wiki/Smart_Fortwo · https://www.conceptcarz.com/s8664/smart-fortwo.aspx · https://en.wikipedia.org/wiki/Battle_at_Kruger
