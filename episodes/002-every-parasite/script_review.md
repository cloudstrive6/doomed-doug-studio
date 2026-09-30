# 002 Every Parasite: script review (draft 2)

Screener, 2026-09-30. Inputs: style bible, series bible, brief.md, script.md (draft 2), facts.md, decisions.md, and the
draft 1 review (7 required fixes, 6 advisories).

VERDICT: PASS

Short version: all 7 required fixes from round 1 are done and hold up on re-check. There are no fact errors and no policy
items, and every score meets its bar. The jewel wasp 22 mm figure still cannot be checked against the primary source,
because the Hawaii repository is still refusing connections. It is not contradicted, the script only uses it as a relative
size, and secondary sources agree, so it does not block. See section 1 and advisory A1.

| Check | Result |
|---|---|
| Facts | PASS: 0 errors. 20 claims re-checked; 1 left unverified at primary level (22 mm, not blocking) |
| Opening / hook | **8/10** (was 7) |
| Structure and pacing | **8/10** |
| Voice and humour | **8/10** (was 7) |
| TTS readiness | PASS |
| Policy | PASS: 0 items |
| Length | PASS: 3,103 spoken words (brief 3,000 to 3,400), about 15:55 at 195 wpm |

---

## Round 1 fixes: status

| # | Fix | Status |
|---|---|---|
| 1 | Opener: remove "in this video" and make the claim true | **Done.** "Every parasite on this list can kill the animal it lives in." "Can" covers Toxoplasma and the raccoon. Item 1's name is at spoken word 33. |
| 2 | Malaria Doug beat: "smallest" and the incomplete list | **Done.** "After everything so far ... the most ordinary thing on the list." |
| 3 | Broodsac: songbird/snail claim | **Done.** The frame now opens on the caterpillar mimicry. Nandy et al. 2022 checked: "resembles like crawling caterpillar which attracts its definite host, insectivorous birds". |
| 4 | Raccoon prevalence | **Done.** CDC DPDx checked word for word: "sometimes in excess of 80%". |
| 5 | Jewel wasp: replace Wikipedia | **Done**, except the 22 mm length (see below). Arvidson 2018, Herzner 2014 and NHMU were all checked word for word. |
| 6 | Broodsac pulse rate | **Done.** Nandy 2022 checked: day means of 99 and 66 beats a minute against night means of 77 and 31 ("dozens of times a minute, faster in daylight"). "Stop completely in the dark" has been cut. |
| 7 | Flesch 73.2 | **Done.** 71.1 (textstat 0.7.13). Confirmed. |

## 1. Facts

**Jewel wasp 22 mm (re-checked as requested): UNVERIFIED at primary level. Not contradicted. Does not block.**
- **Primary source (Williams 1942, ScholarSpace PDF):** `ECONNREFUSED` on WebFetch, and curl timed out, on 2026-09-30.
  The Cal Academy mirror returned 403. I could not read the primary text, the same result the writer got.
- **Secondary sources:**
  - Wikipedia: "The female is about 22 mm long", citing Williams 1942. This is the same chain the writer relied on.
  - Orkin: "22-28 millimeters". Low reliability. It also says "about an inch".
  - A search-index excerpt for the literature gives "2–3 cm long". I could not reach the paper behind it.
- **What the script actually says:**
  - "a little shorter than a paperclip" holds anywhere from 20 to 28 mm.
  - "cockroaches nearly twice its own length" uses the American cockroach at an average of 4 cm (UF/IFAS IN298,
    checked). That gives 1.8 times at 22 mm. It weakens to about 1.4 to 1.6 times if the wasp is 25 to 28 mm.
    This line depends on the 22 mm figure.
- Non-blocking action is in A1.

**Re-checked this round (draft 2 claims, plus draft 1 claims I had not checked before):**

| Claim | Source checked | Result |
|---|---|---|
| Stings to the thorax and head; antennae clipped; roach led by the stumps; burrow sealed | Arvidson et al. 2018 (full PDF) | OK |
| Grooming lasts a few minutes while the wasp finishes the burrow | NHMU | OK |
| Twigs, leaves and stones; eggs hatch on day 3; roach dead about a week after the egg | Herzner et al. 2014, PLOS ONE (7.9 ± 2.1 days) | OK |
| American cockroach about 4 cm | UF/IFAS IN298 | OK |
| Broodsac mimics a caterpillar; pulses faster in light | Nandy et al. 2022 | OK |
| Infected snails in Poland travel farther, sit higher and are more exposed; more than half stay fully exposed | Wesołowska and Wesołowski 2014 (abstract, plus indexed 53% against 28%) | OK |
| Raccoons: more than four in five in parts of the US; egg about the width of a hair; infective in 2 to 4 weeks | CDC DPDx | OK |
| Oxford rat study, 2000; infected rats lost their aversion, and some were attracted | Berdoy, Webster and Macdonald 2000 | OK |
| Infected crickets more likely to jump into water | Thomas et al. 2002 (48.7% against 13.3%) | OK |
| Ross, 1897, parasite found in a mosquito; Nobel Prize | Nobel/Britannica summaries | OK |
| 663 sleeping sickness cases in 2020 | PLOS NTD 2021 | OK |
| Naegleria grows up to 46 °C / 115 °F | Minnesota Department of Health | OK |

The draft 1 checks (WHO, CDC and PMC figures for malaria, schistosomiasis, Chagas, HAT, Naegleria, Toxoplasma and
Baylisascaris) are unchanged in the script and still stand.

## 2. Opening (hook 8/10) and rule audit

- **Item 1's name:** at spoken word 33 (limit 35).
- **Twist:** "isn't paralyzed" is at word 117 (limit about 145).
- **Before item 1:** no greeting, no channel name, no "in this video", no subscribe ask.
- **Stakes and gag:** the stakes line and "Doug did not agree to this." are both in place.
- **Why not higher:** "can kill the animal it lives in" is a slightly softer promise than draft 1. It is true now, which
  matters more.

**Script Writer rules violated:**
- **Rule 8 (advisory, carried over):** Broodsac, Toxoplasma and Sleeping Sickness still have no everyday-object *scale*
  analogy. The writer says no sourced size fits. The brief chose these analogies, so this is accepted, the same as in
  round 1.
- **Rule 4 (minor):** the Blood Flukes kicker runs about 27 spoken words against a limit of 25, because the numbers are
  spelled out. See A4.
- **Rule 7 (borderline):** the Toxoplasma kicker "But the cat is not the last host on this list." works as a lead-in to
  "Human hosts." See A3.

**Rules met:**
- **1:** 3,103 words.
- **2:** met.
- **3:** 11 items, and every name sentence matches its heading.
- **5:** the axis is stated in the header, and Naegleria is last.
- **6:** met.
- **9:** average sentence 16.0 words, longest 34, every item has a sentence of 2 words or fewer, Flesch 71.1.
- **10:** met.
- **11:** met.
- **12:** the outro is 24 words.
- **13:** zero tic words, and all 11 twist markers are different.
- **14:** met.

## 3. Structure and pacing (8/10)

- **Segment lengths:**
  - Item 1: 269 words (target 240 to 280).
  - Items 2 to 10: 265 to 287 words (target 250 to 290).
  - Boss: 339 words (target 320 to 380).
  - All within range.
- **Zone shift:** "Human hosts." falls at 44.5%.
- **Death counter:** runs 7 to 18, one death per item.
- **Running gags:** all present. "Did not agree" appears in the open and the outro. "Doug has died. Again." appears once.
  The floating cap appears twice. Doug befriends the killer (the cat, then Buddy). The cap survives (Buddy scene, outro).
- **Blood Flukes frame:** now opens on the flukes themselves (A3 from round 1 taken).
- **Ending:** the best kicker in the script, then a clean outro.

## 4. Voice and humour (8/10)

- **Voice:** deadpan and consistent throughout.
- **Twist markers:** the five "Here's..." openers from draft 1 are gone.
- **Jokes:** they land and are spaced within the rule-10 limit.
- **Readability:** grade 7.6.
- **Competitor wording:** none found.
- **Why not higher:** "And that's where it gets worse." (Kissing Bug) is the one rhetorical escalation line. Style bible
  3.5 prefers structural escalation. See A5.

## 5. TTS readiness: PASS

No digits, symbols, abbreviations or parentheses in the spoken lines. Dates and numbers are written out. The
pronunciation notes are in the header.

## 6. Policy: PASS, 0 items

- **Gore:** none. The inside-the-body steps get one clinical sentence each.
- **Advice:** no medical or safety advice.
- **Tone:** adult-coded. Buddy and the costumes are played deadpan, with no nursery framing.
- **Originality:** an original two-act narrative, not a list read-out.
- **Title:** the "Would Feel Like" promise is kept, with one sensation line in every item.
- **Death tolls:** stated straight, with no joke in the same beat.

## 7. Length: PASS

3,103 spoken words, about 15:55. The brief targets 3,000 to 3,400 words, so this is inside the word band. It is a little
under the brief's 16 to 17 minute estimate; the editor's pacing will decide the final runtime.

---

## Required fixes

None.

## Advisory (do not block)

- **A1. Jewel wasp 22 mm.**
  - In facts.md, change the note "Screener: re-check if the server is back" to record that the server was still
    unreachable for the screener on 2026-09-30, and add the Wikipedia and Orkin figures as corroboration.
  - If the Williams PDF becomes reachable before the render, read the size line. If it gives more than about 24 mm,
    soften "nearly twice its own length", for example to "much bigger than itself".
- **A2. Jewel wasp, "underground burrow".** Sources say "burrow" or "nest". *A. compressa* often uses existing crevices,
  so "underground" is not sourced. Dropping the word costs nothing.
- **A3. Toxoplasma kicker.** "But the cat is not the last host on this list." reads as a transition, and it is a little
  confusing, because the cat is Toxoplasma's final host. Consider ending on the preceding sentence and letting
  "Human hosts." do the transition.
- **A4. Blood Flukes kicker.** It is about 27 spoken words; trim to 25 or fewer, for example drop "preventive".
- **A5. Kissing Bug twist marker.** Consider replacing "And that's where it gets worse." with a non-rhetorical marker
  (style bible 3.5).
- **A6. Creative director, carried over.** Style bible 3.7, example hook 2, still contains "in this video" and breaks
  Script Writer rule 2. Please fix it before the next episode copies it.
