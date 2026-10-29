# 031 Why the Polar Bear Is the Scariest Animal to Be Hunted By: script review (draft 1)

Screener, 2026-10-29. I recomputed the stats from script.md myself (spoken lines only, with stage directions, headings and comments removed):
**2,098 words, 188 sentences, average 11.2 words (12.0 with the item-name and band lines left out), longest 34, Flesch about 79 (heuristic syllable count).**

| Check | Result |
|---|---|
| 1. Facts | **FAIL**: 1 overclaim (Togunov), 1 misattributed source (Churchill "not fed"), 1 row whose source doesn't support the line as spoken (overheating). 20 claims checked on the web |
| 2. Opening / hook | **8 / 10**. Every retention-update rule is met. Writer rules 9 and 14 are violated |
| 3. Structure and pacing | **8 / 10** |
| 4. Voice and humour | **7 / 10**. Rule 9 misses badly, and one twist marker is lifted from Paint Explainer |
| 5. TTS readiness | Pass (2 advisories) |
| 6. Policy | Pass (0 items) |
| 7. Length | Pass (2,098 words, about 10:46) |

---

## 1. Facts

| # | Claim (script) | Verified against | Result |
|---|---|---|---|
| 1 | "in most of them, the bear was hunting" | Wilder et al. 2017 USGS abstract (fetched): "bears acted as a predator in most attacks" | OK |
| 2 | 73 attacks in 144 years, "extremely rare" | Same abstract: "extremely rare. From 1870–2014, we documented 73 attacks" | OK |
| 3 | "probably ... more than a kilometer away, through a meter of snow" | SeaWorld Senses (fetched): "most likely ... more than 1 km ... and 1 m under the snow" | OK (see flag ruling B) |
| 4 | "the bears traveled crosswind more often than in any other direction, most of all at night in winter" | Togunov et al. 2017 (fetched, full text). Crosswind travel was **not** the overall pattern. In winter, fast movement in slow winds was mostly crosswind. Slow movement or fast winds were mostly downwind. Freeze-up was mostly downwind, break-up was cross-tail wind, and summer showed no orientation | **FAIL**: overclaim. Required fix 1 |
| 5 | Koon: less than a thousandth of a percent of red light, late 1990s | Alaska Science Forum, 28 May 1998 (fetched): "less than .001 percent of red light" | OK |
| 6 | Infrared tracking from the air failed; the coat is about as cold as the snow | Inside Science / AIP (fetched): "they still blended in with the surroundings"; Koon: "the pelt is the same temperature as its surroundings" | OK |
| 7 | Seals dive from several hundred meters; charges 15 to 80 m, average 41 m; Stirling's 15 to 30 m by telescope; 62 structures and 6 seals; 1 of 10 charges; "inefficient" | Gjertz & Lydersen 1986 (PDF text extracted): every figure matches verbatim | OK |
| 8 | 2014 dive, 3 min 10 s, three seals, missed all three, emaciated | Guinness (fetched) | OK |
| 9 | 45 to 50 m without coming up for air | IFLScience (fetched): "45 to 50 meters without surfacing" | OK |
| 10 | Aquatic stalk out of sight; 300 m in a series of dives; "only some polar bears are thought to master it" | Lone et al. 2018 (fetched) | OK |
| 11 | At least 40 km/h; walks at 5 to 6 km/h; paws up to 30 cm, like snowshoes on thin ice | Parks Canada Wapusk (fetched) | OK |
| 12 | "Moving fast for long can put a polar bear at risk of overheating, and that's why it doesn't do long chases" | facts.md cites Parks Canada, but Parks Canada says "**when the weather is hot**". The script drops that condition on sea ice, so the cited row doesn't support the line. McGill Office for Science and Society (fetched) does support it without the weather condition: "Older and larger bears ... quickly overheat" | **FAIL** (sourcing). Required fix 3 |
| 13 | Usain Bolt, about 37.5 km/h | 100 / 9.58 = 37.6 km/h | OK |
| 14 | February 2019, Belushya Guba, at least 52 bears, "mass invasion of residential areas" | TIME (fetched): declared 9 Feb by the Novaya Zemlya administration; at least 52 since December | OK |
| 15 | Holding facility; five air-conditioned cells for summer; helicopter; released when the bay freezes | Manitoba Polar Bear Alert page (fetched) | OK |
| 16 | "According to people who work around the facility, the bears get water or snow, but they are not fed" | Churchill Wild (fetched): "provided with water or snow, but are not fed". HuffPost UK, 19 Dec 2011 (fetched): "Snow is pushed through the cages, but they get no food", with facility staff quoted. No source contradicts it. **But** Churchill Wild is a tour operator, not facility staff, so the spoken attribution misdescribes the source. facts.md also leans on Wikipedia, which cites a fan site | **FAIL** (attribution). Required fix 2 |
| 17 | Manitoba: "true predators and can view people as a potential food source" | Manitoba Churchill safety guide PDF (text extracted): "Unlike other bears, the polar bears of Canada's Arctic are true predators and can view humans as a potential food source." | OK |
| 18 | Svalbard: suitable means of scaring; governor recommends a firearm; loaded firearms forbidden in town | Sysselmesteren firearms page (fetched): all three lines verbatim | OK |
| 19 | Pagano 2024: 20 bears, August to September, Manitoba; 19 of 20 lost mass; about 1 kg a day; berries, bones, antlers | USGS abstract (fetched): 20 bears, Aug-Sep 2019-2022, 0.4-1.7 kg/day, 19 of 20. The mean of about 1 kg is in the WSU release | OK |
| 20 | 2010 to 2014 most attacks; no clear trend 1960 to 2009; 88 percent July to December since 2000 | Hakai Magazine (fetched): all three verbatim | OK (see flag ruling C) |

Arithmetic comparisons (Empire State 443 m, NBA court 28.65 m, Olympic pool 50 m, 1 L = 1 kg, 12 in = 30.5 cm) are all correct.

### Rulings on the writer's flags
- **A. Churchill "not fed": accepted with a fix.** The claim stands on two independent outlets (Churchill Wild, and HuffPost UK 2011 quoting facility staff) and nothing contradicts it. The **attribution** is wrong. Fix 2 changes it.
- **B. Smell range: accepted.** "Probably more than a kilometer ... through a meter of snow" matches SeaWorld's "most likely" exactly. Derocher's "never tested" is the reason for the hedge, and there is no 32 km anywhere. Keep it as worded.
- **C. Attack trend from the press: accepted.** Hakai's figures are the study's own analysis, reported with the lead author. Alaska Public Media corroborates the 2010-2014 peak, and the abstract supports the "hungry bears on land" link. Keep the wording. Don't add a definition of "predatory".
- **D. Sentence length: rejected.** The brief does **not** ask for short TTS sentences. There is no such instruction in brief.md, and the script header's "as the brief asks" is incorrect. Writer rule 9 applies, and 030 draft 1 (an average of 13.85) got a required fix for the same thing. See fix 5.

## 2. Opening (retention update first, then 3.2 and writer rules 2 and 6): 8 / 10
- Sentence 1 has a concrete death stake (attacks, and the bear was hunting). It is sourced, with no scene-setting. Pass. It has no number, which is why it scores 8 and not 9.
- The promise "By the end, one hunts Doug the way it hunts seals." lands at about word 27 (about 0:08). It is specific and paid off by the boss. Pass.
- Item 1 is one of the three strongest and opens on its best fact (smells the seal under snow, jumps on the roof) in sentences 1-2. Pass.
- "The Nose." comes at words 32-33, with no greeting, channel name or subscribe ask before it. Pass.
- The twist marker comes at word 143 (no later than about 145). Pass, but its content is fact 4, which needs fix 1.
- Doug's first line comes after the fact. Death 247 lands at about 1:03. Pass.

**Writer rules (section 7), violated:**
- **Rule 9:** the average sentence is 11.2 words (band 14-19) and Flesch is about 79 (band 60-72). The other limits pass: the longest sentence is 34 words, and every item has a sentence of 6 words or fewer.
- **Rule 14:** "The insane part is" (The Charge) is a Paint Explainer marker, quoted in style bible 3.3. That is 4 consecutive words.
- **Rule 4 (minor, sanctioned by the brief):** the kickers "So Doug went somewhere with walls." (6 words) and "So Doug went camping." (4 words) are under the 8-word minimum. The brief wrote the first one, so this is advisory only.
- Rule 1 is overridden by the retention update.
- **All other rules pass:** 2, 3 (9 items, each with a name sentence), 5 (the axis is declared and the boss is at zero), 6, 7, 8 (one analogy per item), 10, 11 (except the fixes above), 12 (the outro is 23 words with no recap), and 13 (no tic words, no back-to-back marker).

## 3. Structure and pacing: 8 / 10
- **Distance axis:** the bands are monotonic (a kilometer, a hundred meters, ten meters, zero). Each item is one hunt stage, and the boss runs the whole sequence.
- **Items are 209-273 words**, inside the retention range of 200-260. The boss has 273 (brief range 260-300).
- **The Swim is 252**, over the brief's 240 for items 2-8. Advisory: trim the Stirling sentence, or the line "Only some polar bears are thought to master it."
- **Survivals sit at item 4 (about 40%) and item 6 (about 60%)**, as the brief asked.
- **Every kicker leans forward**, so the 90-second re-hook rule is met.
- **Gags all match the brief:** the counter goes 246 to 253 with 250 played flat, "Doug did not agree to this." appears once, "Doug is fine." appears twice, the costume appears once, the befriending lines are all there, the field guide gets its second NO, and the cap survives every death.
- **Exactly two callbacks** (008 and 011), and nothing from 029.
- **The ending** is the boss kicker, then the closing image, then an outro of 23 words or fewer.
- **Weak spot:** the boss's "hunts Doug the way it hunts seals" is paid off by a montage recap, not a new on-screen hunt. It is acceptable, but it is the reason for 8 and not 9.

## 4. Voice and humour: 7 / 10
- **The jokes land and stay deadpan:**
  - "Doug built the bear a lunchbox."
  - "The facility has a menu, and the menu is empty."
  - "NO BEARS, in capital letters, which Doug feels is firm."
  - "The berries were science. Doug was dinner."
- **Density** is about one joke per item, which is within rule 10.
- **The narrator persona is consistent.** The honesty line is clean. The climate lines are flat, one per item, and never a sermon.
- **What holds it down:** the run of short declaratives makes the TTS read sound choppy (rule 9), and one marker is lifted from Paint Explainer (rule 14). The twist markers lean on "Here's the ..." four times ("problem", "catch", "twist", "part that matters"). Advisory: vary two of them.

## 5. TTS readiness: pass
No symbols, parentheses, abbreviations or digits in the spoken lines. Pronunciations are supplied. Advisories:
- "It says NO BEARS, in capital letters": write the spoken text as "No Bears" (the caption can stay in capitals), so the voice doesn't spell it out.
- Spelling is mixed: "traveled" (The Nose) against "travelling" (The Tent). Use "traveling", since the voice is en-US.

## 6. Policy: pass (0 items)
- **Advertiser-friendly:** every death cuts to black, there is no gore and no profanity, and the seals always escape.
- **Not made for kids:** no cubs, no nursery framing, and the tone is adult.
- **Original:** the narrative and the per-item story are distinct to this episode.
- **No safety advice:** the Svalbard firearm recommendation is reported as the governor's wording and is not endorsed. The Manitoba guide is quoted for its "true predators" line, not for instructions.
- **No real people:** no named victims and no incidents.
- **Title:** it is honest, because the hunt is the video and "extremely rare" is stated.

## 7. Length: pass
2,098 spoken words at 195 wpm is about 10:46, inside the 1,950-2,350 target. Fix 5 should add only connective words, not new content.

---

VERDICT: FAIL

Required fixes:
1. **The Nose, line 47.** "they found the bears traveled crosswind more often than in any other direction, most of all at night in winter."
   - Change it to roughly: "they found that in winter, bears on the move mostly traveled crosswind, most of all at night."
   - Update facts.md row "Researchers in Hudson Bay..." to quote the winter result ("Fast polar bear movements (>2 km/h) while wind was slow ... were predominantly cross-wind") and the night pattern.
2. **The Town, line 213.** "According to people who work around the facility, the bears get water or snow, but they are not fed."
   - Churchill Wild is a tour operator, not facility staff. Change the line to "Reports from Churchill say the bears get water or snow, but no food." (or state it flatly).
   - In facts.md FLAG 1, replace the Wikipedia citation with HuffPost UK, 19 Dec 2011 (https://www.huffingtonpost.co.uk/2011/12/19/polar-bear-prison-churchill-polar-bear-jail-canada_n_1157689.html: "Snow is pushed through the cages, but they get no food"), alongside Churchill Wild.
   - The closing kicker "It will not be fed. That is the policy." can stay.
3. **The Charge, line 181.** "Moving fast for long can put a polar bear at risk of overheating"
   - The cited Parks Canada line is conditional on hot weather.
   - Either add McGill OSS (https://www.mcgill.ca/oss/article/did-you-know/polar-bears-can-run-40-km-hour: "Older and larger bears ... quickly overheat") to facts.md and reword to "Big adult bears overheat quickly when they run", or keep Parks Canada and add its condition.
4. **The Charge, line 177.** "The insane part is that it hardly ever needs to run."
   - This is a Paint Explainer marker (rule 14). Replace it with our own wording, for example "The strangest thing about the charge is how rarely it happens."
5. **Whole script (rule 9).** The average sentence is 11.2 words and needs 14 or more; Flesch is about 79.
   - Merge choppy runs into mechanism sentences, about 30 merges. Candidates:
     - line 67, the three sentences after "black"
     - line 135, "It's called an aquatic stalk. The bear swims..."
     - line 145, "It missed all three. The bear was described as emaciated..."
     - line 167
     - line 205, the four sentences about the facility
     - line 269, "More than half of them ate berries. It barely helped. Nineteen of the twenty..."
     - line 299
   - **Do not merge:**
     - the first two sentences of each item
     - the band and name lines
     - the punch lines: "Doug is fine.", "Doug is not a seal.", "There is no seal.", "Doug was dinner."
   - Delete the header comment's claim that the brief asks for short sentences.
   - If Flesch is still above 72 once the average is in band, hand it to the creative director (precedent: 030 advisory A2).

Advisory (not blocking):
- Trim The Swim to 240 words or fewer.
- Vary two of the four "Here's the ..." markers.
- Write "No Bears" in the spoken line.
- Use "traveling".

---
---

# Round 2: draft 2 re-screen

Screener, 2026-10-29. I recomputed the stats from script.md myself (spoken lines only):
**2,085 words, 137 sentences, average 15.2 words, longest 34, Flesch 76.8 (textstat dictionary count) / 78.8 (my heuristic). The writer's figure is 75.6.**
At 1.34 syllables per word, even the top of the sentence band (19 words) gives Flesch of about 74.5, so with this vocabulary rule 9's two limits can't both be met.

| Check | Result |
|---|---|
| 1. Facts | **FAIL** (minor). The 3 draft-1 fact fixes are applied. 1 new claim has no source row, 1 word overstates the source, and 1 facts.md source description is wrong (my round-1 error). 12 claims checked on the web this round |
| 2. Opening / hook | **8 / 10**. Unchanged and still passing. "Here's the problem." is now at word 145, right on the limit |
| 3. Structure and pacing | **8 / 10** |
| 4. Voice and humour | **8 / 10** (up from 7). Rule 9 Flesch ruled below |
| 5. TTS readiness | Pass. Both advisories are done |
| 6. Policy | Pass (0 items) |
| 7. Length | Pass (2,085 words, about 10:42) |

## Fix-by-fix check
| # | Fix | Status | Notes |
|---|---|---|---|
| 1 | Togunov crosswind (line 47) | **Applied, one word off** | I re-fetched PMC5389353: "Fast polar bear movements (>2 km/h) while wind was slow (<36 km/h) were predominantly cross-wind", and the abstract says "most frequently at night during winter". The corrigendum (PMC5977406) says "the key results during winter are fully supported". **But "in light wind" is narrower than the paper.** "Slow" means anything under 36 km/h, which is a fresh breeze. "Light wind" is a specific low range (Beaufort 2, about 6-11 km/h). See fix 2 |
| 2 | Churchill "no food" (line 217) | **Applied** | "Reports from Churchill say..." is accurate. **Correction to my round 1:** HuffPost UK 2011 (re-fetched) states "Snow is pushed through the cages, but they get no food" in its own words, and the person it quotes is Alison Hood of the Born Free Foundation, not facility staff. facts.md FLAG 1, the row at line 108 and script header comment 7 all repeat my "quoting facility staff". See fix 3. The spoken line doesn't change |
| 3 | Overheating (line 183) | **Applied** | McGill OSS (re-fetched): "Older and larger bears, on the other hand, quickly overheat." The line "big adult bears overheat quickly when they run" matches. The insulation link is a reasonable reading of Inside Science and is recorded as framing in facts.md |
| 4 | "The insane part is" | **Applied** | Now "What's odd about the charge is how rarely the bear uses it." No PE overlap. "The disturbing part is" (On Purpose) shares only 3 words with PE's "The most disturbing part is", which is allowed |
| 5 | Rule 9 merges | **Applied** | The average went from 11.2 to 15.2, inside the band. The longest sentence is 34 words (limit 35). Every item still has a sentence of 6 words or fewer, the punch lines are intact, and the header claim about the brief is gone. Flesch is still above 72 (ruled below) |
| Adv. | Swim trim, markers, "No Bears", "traveling" | All done | The Swim is 228 words. Only one "Here's the ..." remains, and no marker repeats in back-to-back items |

## 1. Facts (round 2)
I re-verified fixes 1 to 3 above, plus these claims:

| Claim | Verified against | Result |
|---|---|---|
| Six to ten in the village at a time; rubbish; walking into buildings; at least 52 | Mental Floss (fetched) | OK |
| Pads rough; claws thick, sharp and curved, for ice and slippery prey | WWF-Canada (fetched) | OK |
| When not hunting, often sleeping or resting | SeaWorld behavior (fetched), verbatim | OK |
| Thermal image: nose, mouth and eyes glow; the rest "barely registers" | Open University 4.1 (fetched). The ears are warm too, and the feet give off "a moderate amount" of heat. "Mostly its face" holds | OK |
| Ice-free season up about 3 weeks, 1979 to 2015, western Hudson Bay | Cordova Times report on Pagano 2024 (search); facts.md quotes the full text | OK |
| NPI: smell food at great distances, drawn to campsites and cabins | npolar.no is behind Cloudflare. **Found the wording verbatim** in the NPI-published booklet "Polar Bears in Svalbard" (2005, Aars, Andersen et al.), https://aurora.unis.no/doc/Polar_bears_Svalbard.pdf : "Polar bears can smell food over very long distances and dangerous situations can arise when bears are attracted by food at campsites or cabins." | OK (advisory: add this URL; the check becomes Read) |
| **"which may be why it tried so hard"** (The Swim, line 147) | **No row in facts.md.** This is a causal claim, and rule 11 says unsourced claims are cut, not hedged. The Local, 14 Aug 2015 (fetched), supports it: "A starving polar bear in Svalbard has made the species' longest ever recorded dive in a desperate bid to catch a seal." | **FAIL** (no source in facts.md). Fix 1 |

## 2. Opening: 8 / 10
- The first 145 spoken words didn't change apart from fix 1, which comes after the twist marker.
- "The Nose." is at words 32-33 and "Here's the problem." is at word 145. Every retention-update rule still passes.
- It is still 8 because sentence 1 has no number.

**Writer rules (section 7), violated:**
- **Rule 9:** Flesch only (ruled below).
- **Rule 11:** fix 1.
- **Rule 4:** advisory only. The kickers "So Doug went somewhere with walls." and "So Doug went camping." are sanctioned by the brief. The Swim's Doug beat runs about 33 words against the 15-30 limit.
- **Rule 14:** resolved.
- **Every other rule passes.** That includes rule 13: there are no tic words, and no twist marker repeats in back-to-back items.

## Rule 9 Flesch ruling: acceptable for this episode, not blocking
- **The 030 precedent applies directly.** That script had an in-band average (15.27) and Flesch 75.4. The CD accepted it for that episode only (030 decisions.md item 2), because closing the gap would have meant merging about 24 punch lines.
- **031 is the same case and slightly stronger.** The average (15.2) is in band, and the gap can't be closed by merging alone. At this script's word length, Flesch reaches 72 only with an average of about 21 words, which breaks rule 9's own 14-19 band. The only other lever is longer words, which hurts a TTS read built for retention.
- **Rule 9 counts toward the voice score**, not toward facts or policy, and voice is 8 even with it.
- **For the CD:**
  1. Record 031 as the first of the "next two scripts" from 030 decision 2.
  2. Note that 031 measures 76.8 by dictionary count, which is **above** the 60-76 widening proposed there.
  3. My recommendation: widen the band to 60-80, or drop Flesch and rely on the sentence-length band.

## 3. Structure and pacing: 8 / 10
- **Items are 207-239 words**, and the boss is 275.
- **The distance bands, survival positions, counter (246 to 253, with 250 and 253 played flat), gags, the two callbacks and the 23-word outro** are all unchanged and correct.
- **Every kicker still leans forward.** The merges didn't flatten any of them.
- **The weak spot is the same as before:** the boss pays off its "hunts Doug the way it hunts seals" promise with a montage recap.

## 4. Voice and humour: 8 / 10
- The merges read as mechanism sentences, and the choppy TTS rhythm is gone.
- The deadpan lines are intact.
- The PE lift has been removed, and the twist markers now vary.
- The persona is consistent, and the climate lines are still flat, one each.

## 5-7. TTS / Policy / Length
- **TTS:** no digits, symbols, parentheses or abbreviations in the spoken lines. "No Bears" and "traveling" are fixed.
- **Policy:** 0 items. Nothing new was added. Deaths cut to black, there are no real victims, and the Svalbard firearm line is still reported, not endorsed.
- **Length:** 2,085 words, inside 1,950-2,350.

---

VERDICT: FAIL

All three fixes are small and need no new research. A round 3 only has to check these lines.

Required fixes:
1. **The Swim, line 147.** "the bear was described as emaciated, which may be why it tried so hard."
   - Add a facts.md row: The Local (Norway), 14 Aug 2015, https://www.thelocal.no/20150814/hungry-polar-bear-makes-record-dive : "A starving polar bear in Svalbard has made the species' longest ever recorded dive in a desperate bid to catch a seal."
   - Or cut ", which may be why it tried so hard".
2. **The Nose, line 47.** "bears moving fast in light wind mostly traveled crosswind"
   - Change "in light wind" to "when the wind wasn't strong". The paper's "slow" wind is anything under 36 km/h.
   - Mirror the change in the facts.md row.
3. **facts.md FLAG 1 and the item 6 row (line 108), plus script header comment 7.**
   - Replace "quoting facility staff" with: "the article's own statement; it quotes the Born Free Foundation, not facility staff".
   - This is a documentation correction to my round-1 note, and the spoken line stays as it is.

Advisory (not blocking):
- Add the NPI 2005 booklet URL to the NPI row in item 7, and change its check to Read.
- Trim The Swim's Doug beat to 30 words or fewer, for example by cutting "lying on the edge of a floe".
- CD: decide on the Flesch band (see the ruling above).

---
---

# Round 3: draft 3 re-screen

Screener, 2026-10-29. Recomputed: **2,072 spoken words (about 10:38), 137 sentences, average 15.1.** "The Nose." is at words 32-33 and "Here's the problem." is at word 144.

## Fix-by-fix check
| # | Fix | Status |
|---|---|---|
| 1 | The Swim, line 147: causal clause | **Applied.** ", which may be why it tried so hard" is cut. The line now reads "It missed all three, and the bear was described as emaciated." facts.md row 79 (Guinness, "emaciated") covers it |
| 2 | The Nose, line 47: "in light wind" | **Applied.** It now says "bears moving fast when the wind wasn't strong mostly traveled crosswind, most of all at night", which matches Togunov's "slow (<36 km/h)". The facts.md row at line 47 is mirrored |
| 3 | HuffPost attribution in the docs | **Applied.** facts.md FLAG 1 (line 13), the FLAG 1 row (line 108) and header note 7 all say "the article's own statement; it quotes the Born Free Foundation, not facility staff". The spoken line is unchanged |
| Adv. | NPI booklet URL; Swim Doug beat | **Done.** The URL was added and the check changed to Read. The Doug beat is now 28 words |

## Regression check
- Only lines 47, 147 and 151 changed in the spoken text. Each change removes words, and none adds a claim.
- Opening, escalation, gags, the counter (246 to 253), the callbacks, the outro, TTS (no digits, symbols or parentheses) and policy are all unchanged from round 2.
- The Swim is 213 words, and every item is inside its range.

| Check | Result |
|---|---|
| Facts | Pass (0 errors) |
| Hook | 8 / 10 |
| Structure | 8 / 10 |
| Voice | 8 / 10 (the round 2 Flesch ruling stands; it is not blocking) |
| TTS / Policy / Length | Pass / Pass (0 items) / Pass |

Carried forward for the CD (not blocking): the Flesch band decision from the round 2 ruling. 031 measures 76.8 by dictionary count.

VERDICT: PASS
