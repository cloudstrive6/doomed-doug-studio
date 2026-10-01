# Episode 004: Every Deadly Place, script review (draft 1)

Script screener, 2026-10-01. Inputs: style bible, series bible, brief.md, script.md (draft 1), facts.md.
Metrics were recomputed independently from script.md, counting spoken lines only.

| Check | Result |
|---|---|
| 1. Facts | **FAIL**: 3 errors and 1 unsourced claim (F1-F4), plus 1 advisory |
| 2. Opening | **9/10**. Rules violated: **9** (Lake Nyos), **14** (PE tic phrase) |
| 3. Structure & pacing | **8/10** |
| 4. Voice & humour | **8/10** |
| 5. TTS readiness | PASS (1 cosmetic note) |
| 6. Policy | **FAIL**: 1 item (P1, Nyiragongo ruling) |
| 7. Length | PASS: 3,169 words, about 16:15 at 195 wpm (brief 3,100-3,400) |

---

## 1. Facts

I checked 16 claims against the web, along with every number that sounded surprising.

**Confirmed:**
- Death Valley: the 134 F record from 1913 and the 2025 BAMS dispute ("12-16 degrees cooler", which supports "closer to 120").
- Snake Island: the 2008 first estimate (2,358 snakes) and the current range of 2,000-4,000.
- Morecambe Bay: Bonn 2005 (about half as dense; pulling a leg free takes the force needed to lift a small car).
- Lake Natron: pH 9-10.5, the 75% flamingo share and the Brandt quote, all from Smithsonian and NBC.
- Cave of Crystals: the pumps stopped in October 2015, the cave reflooded, and growth can resume.
- Dallol: more than 100 m below sea level (Gómez et al. 2019 gives 124-155 m for the Dallol area, so it holds).
- Lake Nyos: at least 1,700 dead.
- Lake Kivu: about two million people in the basin.
- Lake Maracaibo: 233 flashes per square kilometre per year, 297 nights a year, and the CDC figure that almost 90% of people struck by lightning survive.
- Nyiragongo: 120,000 left homeless in 2002, the 2021 flow stopped a few hundred metres from the city, the 1977 flows reached 60 km/h, and the mazuku sources check out.

**Errors:**
- **F1. Everest, time of useful consciousness (contradicted by the cited FAA table).** Script, line 197: "at the height of
  Everest's summit, that time is somewhere between one and five minutes." The FAA table (AC 61-107) gives 3-5 min at
  25,000 ft, **2.5-3 min at 28,000 ft** and **1-2 min at 30,000 ft**. The summit is at 29,032 ft, so it sits between the
  28,000 and 30,000 ft rows. facts.md skipped the 28,000 ft row. **Fix:** "somewhere between one and three minutes", and
  add the 28,000 ft row to facts.md.
- **F2. Death Valley, "while officials review it" (unsupported).** Line 25: "...but the record stands while officials
  review it." Researchers have asked the WMO and the NCEC to review the record, but no official review has been opened
  or announced. facts.md only supports "it stays official unless they rule otherwise". **Fix:** "...but for now the
  record still stands."
- **F3. Opener, "kill anyone who stays" (false, and the script contradicts it).** Line 9: "Eleven places on Earth kill
  anyone who stays." Doug and the flamingos stay at Natron and live. Almost 90% of lightning victims survive (item 10),
  and people live around Lake Maracaibo. Climbers stand on Everest. This is the first line of the video and it sets the
  title promise. **Fix:** make it true, for example "Eleven places on Earth that can kill anyone who stays." Keep the
  word count so that "Death Valley." still lands within 35 words.
- **F4. Natron kicker, unsourced superlative.** Line 143: "The most caustic lake in Tanzania is also the main nursery
  of the lesser flamingo." facts.md has no source for "most caustic lake in Tanzania". The only support I could find is
  listicles. **Fix:** source it from an institutional source or cut the superlative, for example "A lake this caustic
  is also the main nursery of the lesser flamingo."

**Advisory (not blocking):**
- A1. Line 131, "The stone animals are real, but the poses aren't." The animals are preserved or calcified, not stone,
  so this line half-endorses the myth the item is busting. Suggest "The preserved animals are real".
- A2. Line 299, Lake Kivu "about two thousand times as much gas". EarthDate (UT Austin) does say this, so it is sourced.
  However, the published volumes (about 256-300 km³ CO2 plus about 60 km³ methane, against Nyos) put the ratio in the
  hundreds, and other outlets say "300 times". "Hundreds of times as much gas" is true under every source.
- A3. Line 169: the −98 °C figure is a snow-surface temperature, and the NWS frostbite chart uses air temperature. The
  "more than fifty degrees colder" comparison holds either way, because the air in the hollows was about −94 °C
  (Scambos 2018), but "air there" would be cleaner.

## 2. Opening: 9/10

- "Death Valley." is spoken at words 33-34. The writer reported 31-32; both are within 35. Nothing comes before it:
  no greeting, channel name or subscribe ask.
- The twist marker "Here's the problem." lands at word 133, under the 145-word limit.
- The opener is a strong stakes line plus "Doug did not agree to this." It loses one point only for F3.

**Script Writer rules (section 7), checked 1 to 14:**
- **Rule 9 violated:** Lake Nyos has no sentence of 6 words or fewer apart from the name. Its shortest is "That day,
  it all came out at once." at 8 words.
- **Rule 14 violated:** line 161, "To put that in context," is five consecutive words of a documented Paint Explainer
  tic (style bible 3.4: "use this *type* of tic but write our own").
- **Rules 1-8 and 10-13: pass.**
  - Rule 9 metrics: average sentence 15.9 words, maximum 34, Flesch about 67.
  - Rule 13: twist markers rotate with no repeats in a row, and "However" appears once.
  - Rule 12: the outro is 20 words.
- **Brief deviation:** "Doug is fine." is used at both survivals (line 141 at Natron and line 331 at Maracaibo). The
  brief allows it "at one of them".

## 3. Structure & pacing: 8/10

- The axis is declared in the header. The section headers are in place: "Minutes." at about 37% and "Seconds." at about 72%.
- Every item opens on its exact name, and there are no transition sentences.
- Segment lengths are within the brief's ranges, with two trivial overruns: Death Valley 281 (limit 280) and Dallol
  294 (limit 290). Nyos is 252, which is fine for the sombre beat.
- The counter runs from 27 to 36 and matches the death plan. The ending matches the bible: the last kicker, then a
  20-word outro.
- Gags present: the death counter, "did not agree", the disappointed narrator, befriending the snake, the flamingo
  costume, the lone cap (Morecambe, Maracaibo, the rim), one 003 callback, and the suitcase.
- Deductions:
  - "Doug is fine." is used twice.
  - The survivable lightning stop sits inside "Seconds.", which muddies the axis. The brief chose this for the comic
    release, so it is acceptable.

## 4. Voice & humour: 8/10

- Deadpan holds throughout. The best lines:
  - "Doug is watching the wrong thermometer."
  - "He is completely right. / Then the tide arrives."
  - "The timer is optimistic."
  - "briefly that includes him"
  - "The extinguisher runs out first."
- Joke density is about one per minute. Nyos is clean, with zero jokes.
- The narrator persona is consistent, and nothing is gross for its own sake.
- One point is lost for the rule 14 tic.

## 5. TTS readiness: PASS

- Spoken lines contain no digits, symbols, abbreviations or parentheses. Every number is written out.
- "NASA" reads fine. The pronunciation list for the editor is good.
- Cosmetic: the quotation marks around "living" (line 133) are harmless for Chirp but can be dropped.

## 6. Policy

**Passing:**
- Gore: no injury described, and all deaths are cartoon. The Dallol gas and the off-screen lava flash were handled well.
- Profanity: none.
- Kid appeal: the voice is adult-coded throughout (the smug quicksand expert, the selfie timer). No nursery framing.
- Inauthentic content: each stop is an original mini-story with its own myth-bust or twist. It is not a list read-out.
- Advice: none. The quicksand and lightning facts are stated as findings, not instructions.
- Title: the working title plus the "11 of the deadliest" description line is honest.

**P1. Nyiragongo: the writer's tragedy/joke question. RULING: apply the rule strictly and cut the Goma sentences.**

The brief contradicts itself here. Item 11 asks for one sentence each on 2002 and 2021, while section 8 says "no jokes
within the item that mentions them". **Section 8 wins**, because it is the risk rule and item 11 is a research list.
Reasons:
1. The item is the comic climax: the marshmallow, "The extinguisher runs out first", and a cap joke as the kicker.
   Putting real displacement of a city (120,000 homeless; the 2002 eruption also killed about 250 people, which the
   script leaves out but viewers will know) in the same 2-minute segment as a played-for-laughs death is the
   juxtaposition that sensitive-events review and comment sections punish. A paragraph of spacing does not change
   the segment.
2. Goma is in an active conflict zone, and the brief limits this item to geology only.
3. The item doesn't need those sentences. The 1977 drain at 60 km/h already shows the lava outrunning traffic, and
   the mazuku twist carries the escalation.

**Required for P1:**
- Cut line 351 entirely. Both sentences, "In two thousand two, lava from cracks on the volcano's flank ran into Goma
  ... In two thousand twenty-one, another flow stopped about three hundred meters from the edge of the city.", are
  **41 words**.
- Rewrite line 355, "After two thousand two, the lava lake came back.", so that it does not anchor on the 2002
  eruption. Either use a sourced, non-casualty version (for example "When the lake drains, it eventually refills," from
  the GVP eruption history) or cut it.
- The writer's arithmetic is off: removing 41 words takes the item from 364 to **323**, which is below the brief's
  330-380. Backfill about 15-40 words of sourced geology, such as the lava lake's size against a stadium (brief item
  11, GVP).
- Keep the 1977 sentence. It is geology with no casualties stated.
- Keep "about twelve kilometers north of the city of Goma" (line 341). It is location only.

## 7. Length: PASS
3,169 spoken words, about 16:15 at 195 wpm. After the P1 cut and backfill, the total stays at about 3,150 or more,
still inside 3,100-3,400.

---

VERDICT: FAIL

**Required fixes:**
1. **(F3)** Line 9: change "Eleven places on Earth kill anyone who stays." to a true statement, for example "Eleven
   places on Earth can kill anyone who stays." "Death Valley." must stay within the first 35 words.
2. **(F2)** Line 25: change "but the record stands while officials review it" to "but for now the record still stands".
3. **(F4)** Line 143: source "the most caustic lake in Tanzania" from an institutional source, or reword without the
   superlative ("A lake this caustic is also the main nursery of the lesser flamingo.").
4. **(F1)** Line 197: change "between one and five minutes" to "between one and three minutes". Add the FAA
   28,000 ft row (2.5-3 min) to facts.md.
5. **(P1)** Line 351: cut both Goma sentences. Line 355: rewrite or cut "After two thousand two, the lava lake came
   back." Backfill Nyiragongo to 330 or more with sourced geology (lake size suggested), and add the source to facts.md.
6. **(Rule 14)** Line 161: replace "To put that in context," with our own wording (for example "For scale,").
7. **(Rule 9)** Lake Nyos: add one sentence of 6 words or fewer, for example by splitting line 287 into "Then it all
   came out." Keep it clinical, with no joke.
8. **(Brief, running gags)** Line 141: drop "Doug is fine." at Natron, because it is reserved for Maracaibo. Keep
   "We'll be honest, this was not the plan." or something similar.

**Recommended (not blocking):** A1 ("preserved animals"), A2 (Kivu "hundreds of times"), A3 ("air there"), and trim
Death Valley and Dallol by a few words each to bring them inside their ranges.

Once these are fixed, the script should pass. Expected scores are hook 9, structure 8, voice 8. Re-screening only
needs the changed lines and facts.md.
