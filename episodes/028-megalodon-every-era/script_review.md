# Script review, round 3: 028 Could Megalodon Survive Every Deadly Era Before and After It? (draft 3)

Screener, 2026-10-27. This is a delta screen. I checked only the round-2 fix lines (F5, F6, S3, M3, M4, M5, A1, A2), using `git diff 756245f 227b451`, plus a scripted sanity pass over the whole narration. Comments and stage directions were excluded from all counts. Everything else is as reported in round 2.

| Check | Result |
|---|---|
| 1. Facts | **PASS**: F5 and F6 fixed, M3-M5 fixed. I re-opened the NHM page today. |
| 2. Opening / hook | **8 / 10**. Rule 11 is clear now. Rules 1-14 pass. |
| 3. Structure & pacing | **8 / 10**. S3 is fixed: every segment is inside its range. |
| 4. Voice & humour | **8 / 10** |
| 5. TTS | **PASS**. The narration has no digits, symbols or parentheses. |
| 6. Policy | **PASS**: no policy items |
| 7. Length | **PASS**: 3,031 spoken words against 2,950-3,350 (matches the writer's footer). |

## Round-2 fixes: verification

| # | Line | Status |
|---|---|---|
| F5 | 66: "Five stops on this list come after the megalodon's time. This one is long before it, ..." | **Fixed.** I recounted the stops after its time: Supernova, Orcas, Ice Age, Canal and Trench, so 5 is right. facts.md has the count as a framing row. The old 30-word sentence is now two sentences. |
| F6 | 374: "Re-checked, the teeth that started the rumour turned out to be as old as every other megalodon tooth." | **Fixed.** NHM was re-opened today. It says the 1959 "findings and method were ultimately completely disproven in the 1970s" and "the teeth come from well within megalodon's expected timeline". facts.md now has rows for both this line and "it didn't hold up" (line 370). |
| S3 | 52: "The newborn swims on into the shallows without looking back. Its first meal was unhatched eggs. Doug was its second." | **Fixed.** The Nursery is 247 words without the cold open (range 240-280). The line comes after the twist and calls back to the cold open's oophagy fact, which facts.md cites to Shimada 2025. The joke lands, and it implies the death without describing it. |
| M3 | 338: "ships using it pass the very rocks where megalodon pups once grew up" | **Fixed.** The claim is now limited to the Gatún rocks, and facts.md has a row for it. |
| M4 | 290: "huge areas of the world's shallow continental shelves" | **Fixed.** This matches "large areas" and "exposed" in the sources. |
| M5 | 268: "as far as we can tell, its body was built to hold heat in" | **Fixed.** The line is now hedged as reasoning, and the facts.md row cites Griffiths 2023 for endothermy. |
| A1 | Cold open: "a full-grown one" | **Applied.** The cold open is 33 words, and "The Nursery." is at words 34-35, inside the 35-word limit. |
| A2 | 46: "on the newer estimate, it is about twice as long as he is" | **Applied.** This is now accurate: 3.6-3.9 m against Doug's 1.8 m. |

## Whole-script sanity check

- **Duplication: clean.** There are 12 `##` sections (the cold open plus 11 items), each appears once, and they are in the declared order. The only repeated paragraph is "Doug has died. Again.", and the only repeated short sentences are "Doug has died." and "Doug is fine.". These are the intended series gags.
- **Hook position:** the item 1 name is at words 34-35. The twist flag "Here's the twist" starts at word 141, inside about 145 words.
- **Segment lengths** (each includes its spoken item name):

  | Segment | Words |
  |---|---|
  | Nursery | 249 |
  | Mosasaur | 264 |
  | Ichthyosaur | 268 |
  | Supernova | 257 |
  | Rival | 276 |
  | Orcas | 264 |
  | Hothouse | 259 |
  | Ice Age | 276 |
  | Canal | 258 |
  | Trench | 259 |
  | Boss, including the 19-word outro | 368 |

- **Longest sentence:** 32 words. No new sentence is over 20.
- **Header comment:** it matches the body (draft 3, deaths 227-234, chalkboard ends 4 / 11).

## Advisory (not blocking)

- **Line 374:** "as old as every other megalodon tooth" is a slightly loose reading of NHM's "well within megalodon's expected timeline", because megalodon teeth range from about 20 to 3.6 million years old. It is acceptable as spoken shorthand. If the writer touches the line again, "turned out to be millions of years old, like every other megalodon tooth" would match NHM exactly.

VERDICT: PASS
