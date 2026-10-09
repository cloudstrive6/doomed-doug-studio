# Script review: 010-every-venom, draft 1

Script screener, 2026-10-09. Inputs: style bible (3.x and section 7), series bible, brief, script.md (draft 1), facts.md.
I recomputed the stats myself and they match the writer's footer. Spoken words: 2,948. Average sentence: 15.8 words. Longest sentence: 35 words.
Flesch is about 68. Item 1's name comes at spoken word 33, and its twist ("Here's the problem") at word 132.

| Check | Result |
|---|---|
| 1. Facts | **FAIL**: 1 error, 1 overclaim, 1 misattribution, 1 unsourced line |
| 2. Opening | **8/10**. Rule 14 is violated once (see section 2) |
| 3. Structure & pacing | **8/10** |
| 4. Voice & humour | **8/10** |
| 5. TTS readiness | PASS |
| 6. Policy | PASS (0 items) |
| 7. Length | PASS (2,948, brief target 2,900-3,400) |

---

## 1. Facts

I verified 19 claims against the live source (WebFetch) or by search. I re-opened the facts.md entries marked "search snippet" wherever the page would load.

**Confirmed:**
- **Platypus, morphine:** the 1992 MJA case report says pain did not respond to morphine. The patient was spurred in the hand.
  I could not open PubMed (cookie wall) or the Davidson page (404). The claim rests on Wikipedia and secondary accounts.
- **Hornet (WSDA):** 5 cm long, 7.5 cm wingspan, longer stinger, can sting more than once, venom "more powerful than any local bee or wasp", a colony destroyed "in a matter of hours", eradicated in late 2024.
- **Japan sting deaths:** 191 deaths from wasps and bees, 2008-2018, average 17 a year. Swatting can release the alarm pheromone (nippon.com).
- **Scorpions:** 1.2 million stings, more than 3,250 deaths, seven high-risk areas, 2.3 billion people (Chippaux & Goyffon 2008).
  The NBC article confirms the UV glow, that all three hypotheses fail, and that "some think it has no function".
- **Saw-scaled viper:** the Warrell (Nigeria, 1970s) abstract says it "probably bites and kills more people than any other species of snake". Its victims fill 10% of hospital beds in the savanna region.
- **Snakebite (WHO):** 5.4 million bites a year and 81,410 to 137,880 deaths a year.
- **Komodo:** Goldstein 2013 studied 16 captive dragons and isolated no virulent species.
- **Blue-ringed octopus:**
  - Golf-ball size and a flash in 0.3-0.5 s (Physics Today).
  - The Australian Museum confirms brown until disturbed, tetrodotoxin and "several fatalities in Australia".
- **Black mamba (NatGeo):** olive to grey skin, a blue-black mouth lining, 14 ft maximum and 8.2 ft typical, 12.5 mph, "almost always fatal" before antivenom.
- **Inland taipan (Australian Museum):** "most toxic of all snake venoms in LD50 tests on mice", a handful bitten and all survived, darker in winter.
- **Irukandji:**
  - MJA 2002: named in 1952, several small carybdeid species, onset about 30 minutes, two deaths in 2002 caused by severe hypertension.
  - Australian Geographic (Gershwin): fingernail size, a transparent cube-shaped bell, and the certainty of dying.
- **Box jellyfish:**
  - NOAA: "considered the most venomous marine animal", death "within a few minutes", swims at up to 4 knots.
  - Australian Museum: 30 cm bell, up to 60 tentacles in four clumps, 3 m tentacles, swims toward movement.
  - MJA 1996: at least 63 deaths since 1884.

**FAIL items:**

1. **Funnel-web death count is wrong (fact error).** Script line 267: *"Male spiders are thought to be behind all thirteen recorded deaths from this species."*
   The Australian Museum page (re-opened) gives two facts:
   - the 13 recorded deaths are for funnel-webs as a group;
   - the male Sydney funnel-web is "**probably responsible for most** of the thirteen recorded deaths".

   The other sentence on that page, "only male spiders have been responsible for all recorded funnel-web envenomation deaths", is also about the group, not this species.
   The script attaches "all thirteen" to *this species*, which the source does not support. facts.md has the same mistake (it marks this row "verified").
2. **The viper kicker drops the hedge (overclaim).** Line 191: *"The deadliest snake on Earth is very easy to step on, and Doug stepped on it."*
   The only source is the hedged "probably" (line 179), and "deadliest" can be heard as "most toxic", which the taipan item later says is a different snake.
3. **The 2005 Nature study is attributed to the wrong species.** Line 371 sits in the *Chironex* item and says the study looked at "box jellyfish eyes".
   Nilsson et al. 2005 studied *Tripedalia cystophora*, a small Caribbean box jellyfish, not *Chironex fleckeri*. Viewers will hear it as a finding about this animal.
4. **Unsourced claim (rule 11).** Line 47: *"Most insect stings fade within a few minutes of the moment they happen."* There is no row for it in facts.md.

**Advisory (not blocking):**
- **Platypus, line 31:** "even strong doses of morphine gave him almost no relief." One secondary account says repeated doses eventually brought the pain down to a tolerable level.
  "Morphine gave him little relief" is safer. If the writer can open the MJA PDF, keep the wording only if the paper supports it.
- **Funnel-web, lines 274-275:** the toxin cited is robustoxin. The museum calls it a male-specific component, so "the male's venom" is fine.

## 2. Opening and Script Writer rules (section 7)

- "Platypus." is at spoken word 33, inside the 35-word limit but tight. Nothing comes before it: no greeting, no channel name, no "in this video", no subscribe ask.
- The twist lands at word 132 (about 41 s), under 145. It is a strong one: a joke animal that morphine can't touch.
- The opener follows the brief and lands "Doug did not agree to this."
- **Score 8/10.** The frame line is a plain inventory sentence and has no stakes hook. It does its job but won't be clipped.

**Rule-by-rule:**

| Rule | Status |
|---|---|
| 1 Word count | OK (2,948) |
| 2 Opening | OK |
| 3 Item count and names | OK (12 items, standalone name sentences matching the headings) |
| 4 Beats | OK. Every item has frame, mechanism, flagged twist, kicker of 8-25 words, and a Doug beat |
| 5 Axis | OK. Declared in the header; the boss is the most extreme |
| 6 Twist by word 145 | OK |
| 7 Transitions | OK (section headers only) |
| 8 Scale analogies | OK. One per item or more |
| 9 Sentences and Flesch | OK. Average 15.8, max 35, at least one short sentence per item, Flesch about 68 |
| 10 Humour | OK. Deadpan, no gross-out |
| 11 Sources | **VIOLATED** (line 47, see fact item 4) |
| 12 Ending | OK. The closing-image line plus a 16-word outro. "Nine pages say no and three say maybe" is a tally, not a recap; acceptable |
| 13 Tics and markers | OK. "actually" 1, "However" 0; no twist marker repeats back-to-back |
| 14 PE wording | **VIOLATED**: line 365, *"But the most disturbing thing about it is..."* contains the 4-word run "the most disturbing thing", which matches the PE fragment quoted in style bible 3.3 ("...the most disturbing thing yet") |

## 3. Structure & pacing: 8/10

- **Escalation:** Pain only, then Slow killers, then Fast killers. The order is clear, and the box jellyfish works well as the boss: it is the only animal that comes to Doug.
  - Placing the taipan survival in "Fast killers" is a deliberate brief call, and the item-6 callback justifies it.
  - Section headers fall at about 15% and 52%. The midpoint shift is on target.
- **Running gags:** 4 used:
  - "Doug did not agree to this."
  - "Doug is fine." twice, plus the taipan disappointment
  - "Doug has died. Again." twice
  - the cap (swatter, water, torch beam, guide)

  The cat costume is inverted correctly and stated once. The field guide closes the episode. That is within the bible's 2-3 "core" gags plus props.
- **Item lengths:** several items run under the bible template:
  - Scorpion 225 and mamba 225 (template 240-290 for items 5-8).
  - Funnel-web 241, taipan 241 and Irukandji 237 (template 260-300 for items 9-11).

  The brief allows 240-280, and the total is within target, so this is not blocking. Lengthening the late items is the easiest way to move the runtime toward 16 minutes.
- **Hornet:** the twist comes after the death statistics, so the item spends about 60 words on numbers before its hook. It still reads fine.

## 4. Voice & humour: 8/10

- The narrator persona is consistent: dry, a little sadistic, and secretly fond of Doug.
- The best lines:
  - "everyone she knew"
  - "wearing the boot at the time"
  - "the spider checked"
  - "quietly deleting it"
  - "Doug's instincts were completely correct"
- Repetition to trim:
  - "double bed" is used 3 times (Komodo, mamba, taipan).
  - "fingernail" is used twice (platypus, Irukandji).
  - "Here's the..." starts 5 of 12 twist markers. That is legal but noticeable.
- 20 sentences run 30-35 words, mostly mechanism lines. The punches still land because every item has short sentences.
- "Doug is fine, the narrator says" (line 71) has the narrator quoting himself in the third person. It works as a gag. Keep it to this one instance.

## 5. TTS readiness: PASS

- No digits, symbols, parentheses or abbreviations in the spoken text. NOAA is spelled out.
- Accented "Sateré-Mawé", poneratoxin, tetrodotoxin and Irukandji are covered by the pronunciation notes. The editor should preview them with `narrate`.

## 6. Policy: PASS

- **Advertiser-friendly:** only clinical one-liners ("stops blood from clotting", "cardiac arrest"). There is no wound, swelling or bleeding description. All deaths are cartoon only. No profanity.
- **Human deaths:** numbers only, with no names or ages. The funnel-web 15-minute record is given without an age.
- **Made for kids:** the tone is adult-coded throughout. The cat costume and "so pretty" are played against the narrator's indifference, not for cuteness.
- **Inauthentic or repetitive content:** each item is an original mini-story with its own twist and Doug beat, not a list read-out.
- **Medical advice:** none. There are no first-aid, treatment or "you should" lines. Antivenom appears only as history or as flat fact.
- **Title promise:** the title "How Every Deadly Venom Would Kill Doug" fits, because the opener says up front that the first venoms "only hurt", and there are 9 deaths in 12 items.
- **Cultural respect:** the Sateré-Mawé passage is factual, has no joke, and Doug doesn't wear the glove.

## 7. Length: PASS

2,948 spoken words, about 15:07 at 195 wpm. Brief target: 2,900-3,400.

---

VERDICT: FAIL

Required fixes:
1. **Line 267.** Replace *"Male spiders are thought to be behind all thirteen recorded deaths from this species."* with a sourced version. For example: *"Funnel-web spiders have thirteen recorded deaths, and males are behind all of them, most from this species."* Correct the facts.md row to match the museum's "most".
2. **Line 191.** Hedge the kicker. *"The deadliest snake on Earth..."* should become something like *"The snake that probably kills the most people is very easy to step on, and Doug stepped on it."*
3. **Line 365 (rule 14).** Remove the 4-word PE match "the most disturbing thing". For example: *"But the worst part is that it is not drifting."* No "The worst part is" marker sits next to it, so rotation is unaffected.
4. **Line 371.** Attribute the Nature study correctly. For example: *"In two thousand and five, a study in the journal Nature looked at a smaller cousin and found its box jellyfish lenses remarkably well made..."* Alternatively, say "box jellyfish eyes" only in a sentence that doesn't imply *Chironex*. Update facts.md with the species.
5. **Line 47.** Either add a source to facts.md for "most insect stings fade within a few minutes", or rewrite the frame so it makes no general claim. For example: *"Most ants are a nuisance. This one is barely getting started."*

Optional:
- Soften line 31 to "morphine gave him little relief".
- Swap one or two of the three "double bed" analogies.
- Add about 15-25 words to items 5 and 8-11.

Re-screen after fixes. The hook, structure and voice scores already meet the bar.
