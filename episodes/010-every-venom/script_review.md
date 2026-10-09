# Script review: 010-every-venom, draft 2 (round 2)

Script screener, 2026-10-09. Inputs: style bible (3.x and section 7), series bible, brief, script.md (draft 2, commit a61e8ca), facts.md, and the draft 1 to draft 2 diff.
I recomputed the stats and they match the writer's footer:
- Spoken words: 3,054. Sentences: 193. Average sentence: 15.8 words. Longest: 34 words.
- Flesch is about 68.
- "Platypus." comes at spoken word 33 and the twist at word 133.
- No digits or symbols in the spoken text.

| Check | Result |
|---|---|
| 1. Facts | **FAIL**: 1 misleading causal claim (inland taipan). Draft 1 had the same line and I missed it in round 1 |
| 2. Opening | **8/10**. Rules 1-14 all OK; one style-bible deviation (3.5) |
| 3. Structure & pacing | **8/10** |
| 4. Voice & humour | **8/10** |
| 5. TTS readiness | PASS |
| 6. Policy | PASS (0 items) |
| 7. Length | PASS (3,054, brief target 2,900-3,400) |

---

## 0. Round 1 fixes

| # | Fix | Status |
|---|---|---|
| 1 | Funnel-web deaths (line 269) | **FIXED.** The new text says the group has 13 deaths, all caused by males, and the male of this species "probably caused most". The Australian Museum page, re-opened today, matches word for word. |
| 2 | Viper kicker hedge (line 193) | **FIXED.** "The snake that probably kills more people than any other..." keeps the source's "probably". |
| 3 | Rule 14 match "the most disturbing thing" (line 369) | **FIXED.** It is now "But the worst part is that it is not drifting." The nearest same-family marker is "What's truly unsettling" in the Irukandji item before it, so the markers still rotate. |
| 4 | Nature 2005 attribution (line 375) | **FIXED.** The line now says "a different, smaller species of box jellyfish". The study was on *Tripedalia cystophora*, and its lenses gave nearly aberration-free images while the eyes see a blur (Lund LUP record and press coverage). This is correct. |
| 5 | Unsourced insect-sting line (line 47) | **FIXED.** The general claim is cut. The new frame, "Its sting does not stop when the ant lets go...", rests on the 24-hour and poneratoxin rows. |

The optional fixes were also applied:
- Line 31 now says "morphine gave him little relief".
- "double bed" appears once (was 3).
- "fingernail" appears once (was 2).
- "Here's" twist markers: 3 (was 5).
- The late items were lengthened.

## 1. Facts

This round I checked 22 claims against live pages (WebFetch) or by search. That covers every new or changed claim plus a resample of earlier ones.

**New claims, confirmed:**
- **Scorpion heart claim (line 145):** the Frontiers in Pharmacology 2021 review (Das et al.) supports both parts:
  - "Indian red scorpion sting is often characterized by myocarditis..."
  - "...reducing the heart's pumping ability"

  The same page also confirms catecholamine release, 5-9 cm, nocturnal, and "one of the world's deadliest scorpions". Line 145 is supported.
- **Taipan diet (line 303), Australian Museum:** "feed entirely on small to medium-sized mammals, particularly the Long-haired Rat."
  The script's "almost nothing but small mammals" is more cautious than the source. Captive snakes also take chicks. Acceptable.
- **"Fierce snake" (line 305):** the museum lists "Fierce Snake, Small-scaled Snake, Lignum Snake". Confirmed. The museum also confirms "shy... relatively placid" and the warning display before a strike.
- **Taipan size and colour:** an average of 2 m, darker in winter and lighter in summer (museum). Confirmed. "As long as a door is tall" (about 2-2.1 m) is fine.
- **Mamba (NatGeo):** up to 14 ft and 8.2 ft average, olive to gray, 12.5 mph, blue-black mouth, "almost always fatal". All confirmed.
  - "past four meters, about the length of a family car" (4.3-4.8 m) is fine.
  - "still longer than a sofa" (2.5 m against about 2-2.2 m) is fine.
  - "half an hour, roughly the length of a lunch break" is fine.
- **Funnel-web, "Bites from females have not killed anyone" (line 269):** supported. The museum says "bites by these females have not caused any deaths". "These females" means female Sydney funnel-webs, and the claim also follows from "males caused all of them". See advisory A2.
- **Comparisons:** staple (about 12.7 mm, so "a little longer" fits a 15-18 mm spur) and guitar (about 1 m). Both pass the arithmetic check.

**Resampled, confirmed:**
- **Box jellyfish (NOAA):** "most venomous marine animal", death "within a few minutes", speeds "approaching four knots" (about 7.4 km/h, so "about seven kilometers an hour" is fine), *Chironex fleckeri*.
- **Komodo:** 3.13 m is the longest verified. Four deaths in the 35 years to 2009 (2009 press reports). Later park data to 2012 gives 5 deaths, but the script's window ends in 2009, so it is correct.
- **Taipan:** "only a handful of people have ever been bitten", all survived.

**FAIL item:**

1. **The taipan line implies the wrong reason for zero deaths (misleading claim).** Line 301:
   *"...and mice are not people, which turns out to matter here."*
   - The clause tells viewers that the mouse ranking doesn't carry over to humans, and that this explains why nobody has died.
   - The Australian Museum gives a different reason: the handful of bite victims survived **because of prompt first aid and hospital treatment**. Bites are also rare because the snake is remote and shy.
   - The script's own callback (line 313) gives the correct reason ("common, nearby and easy to step on"), so the item contradicts itself.
   - It also clashes with the declared axis ("a healthy adult who gets no help"), which puts this snake among the "Fast killers".
   - The brief's own fallback wording (section 4, item 10) is "very few bites, all survived with treatment".

**Advisory (not blocking):**
- **A1. Line 309:** "the most toxic snake on Earth" drops the "in lab tests on mice" hedge that line 291 sets up. This is the same pattern as the viper kicker in round 1. A wording such as "the snake with the most toxic venom ever measured" keeps the hedge.
- **A2. Line 269:** "Bites from females have not killed anyone" repeats "Males caused all of them". The museum also warns that females of other funnel-web species shouldn't be assumed safe. Cutting the sentence saves 7 words and loses nothing.

## 2. Opening and Script Writer rules (section 7): 8/10

The opening is unchanged from draft 1:
- "Platypus." comes at word 33, with nothing banned before it.
- The twist comes at word 133.
- The score stays 8. The frame line is still functional, not clip-worthy.

| Rule | Status |
|---|---|
| 1 Word count | OK (3,054) |
| 2 Opening | OK |
| 3 Item count and names | OK (12) |
| 4 Beats | OK. The new bullet-ant frame is 21 words; every kicker is 8-25 words |
| 5 Axis | OK. But see fact item 1: line 301 undercuts the taipan's place on the axis |
| 6 Twist by word 145 | OK (133) |
| 7 Transitions | OK |
| 8 Scale analogies | OK. Every item has one, and the new ones are sourced as common knowledge |
| 9 Sentences and Flesch | OK. Average 15.8, max 34, a sentence of 3 words or fewer in every item, Flesch about 68 |
| 10 Humour | OK. The mamba now has two gag tags ("very close", "could not read") within about 20 s. That is borderline but deadpan |
| 11 Sources | OK. Every new claim has a row in facts.md |
| 12 Ending | OK (16-word outro) |
| 13 Tics and markers | OK. "actually" appears 1 time; no marker is repeated back-to-back |
| 14 PE wording | OK. "The disturbing part is" (line 215) shares only 3 words with PE's "The most disturbing part is", which is at the limit and allowed |

**Style-bible deviation (not a numbered rule):**
- Line 93 replaces the hornet marker with *"And then it gets worse."* Style bible 3.5 is explicit: "Escalation is structural (the axis), not rhetorical. He does not say 'it gets worse'."
- It is also the weakest marker in the script, because it announces escalation instead of naming the twist.

## 3. Structure & pacing: 8/10

- Item lengths now all sit inside the brief's bands, or within 6 words of them:
  - Platypus 215 and bullet ant 235 (band 210-240).
  - Komodo 234 and octopus 234 (band 240-280; 6 short, not material).
  - Scorpion 254, mamba 246, funnel-web 257, taipan 266, Irukandji 244.
  - Box jellyfish 349 (band 320-380).
- The escalation, the section headers at about 15% and 52%, the boss, the running gags and the guide close are all unchanged and still work.
- **Taipan flow:** line 301, "That ranking comes from...", now comes two paragraphs after the ranking it refers to (line 291). The size and colour material sits in between. "That ranking" no longer has a clear antecedent when heard aloud. Fixing fact item 1 is the natural moment to move it (see fix 1).

## 4. Voice & humour: 8/10

- **New lines that work:**
  - "Its other common name is the fierce snake. Scientists describe it as shy and relatively placid": good deadpan irony with no extra joke needed.
  - "felt a tiny prickle and ignored it" makes the Irukandji beat more accurate (the sting is mild) and sets up the kicker better.
  - "It is a small animal with a very specific target" is a clean scorpion kicker.
- **Weaker:**
  - "And then it gets worse" (see section 2).
  - Line 375, "It found that its eye lenses...": "its" can be heard as the Australian box jellyfish again, the error we just fixed. "...found that that species' eye lenses" or "found that their lenses" is clearer.
- **Persona:** consistent throughout.

## 5. TTS readiness: PASS

- Nothing new to flag. There are no digits, symbols, parentheses or abbreviations.
- "Long-haired rat" and "fierce snake" read cleanly.
- The pronunciation notes still cover the hard words.

## 6. Policy: PASS

- **Advertiser-friendly:** the new heart line is clinical ("inflammation of the heart muscle"), with no gore or graphic description. No profanity.
- **Made for kids:** the tone is still adult-coded. "Not a mouse" and the sign gag are played dry.
- **Original content:** each item is still a distinct mini-story.
- **Medical advice:** none. If fix 1 adds "with hospital treatment", that is a flat historical fact like the antivenom lines, not advice. It must not become a "what to do" line.
- **Title promise:** unchanged and honest (9 deaths in 12 items).

## 7. Length: PASS

3,054 spoken words, about 15:40 at 195 wpm. Brief target: 2,900-3,400.

---

VERDICT: FAIL

Required fixes:
1. **Line 301 (fact, misleading cause).** Cut *"...and mice are not people, which turns out to matter here."* Then:
   - Keep the sourcing. For example: *"That ranking comes from a nineteen seventy-nine study that compared snake venoms on lab mice."*
   - Move that sentence to directly after line 291 so "That ranking" has its antecedent.
   - Change line 307 to give the real reason, per the Australian Museum. For example: *"Only a handful of people have ever been bitten by one, mostly people handling captive snakes, and every one of them survived with fast hospital treatment."*

   Keep the line 313 callback as the explanation. Update the facts.md row for "all survived" to note "with prompt first aid and hospital treatment".
2. **Line 93 (style bible 3.5).** Replace *"And then it gets worse."* with a marker that names the twist instead of announcing escalation. It must not start with "Here's" (the viper item uses that) or "The worst part" (the Komodo item, next, uses that). For example: *"The real danger is what the venom says. It calls for backup."*

Optional:
- A1: line 309, keep the lab hedge ("the snake with the most toxic venom ever measured").
- A2: line 269, cut "Bites from females have not killed anyone."
- Line 375: change "its eye lenses" to "that species' eye lenses".

Hook, structure and voice clear the bar, and policy is clean. Once fix 1 is made and facts.md is updated, the only blocker is gone. Fix 2 is a two-line edit. Re-screen only the taipan and hornet items after the edits.
