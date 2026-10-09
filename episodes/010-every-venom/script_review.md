# Script review: 010-every-venom, draft 3 (round 3)

Script screener, 2026-10-09. Inputs: style bible (3.x and section 7), series bible, brief, script.md (draft 3, commit bf0e93a), facts.md, and the draft 2 to draft 3 diff.
I recomputed the stats:
- Spoken words: 3,044, which matches the footer. No digits or symbols in the spoken text.
- "Platypus." comes at spoken word 33 and the twist at word 133. The opening is unchanged.
- "Here's" markers: 3. "actually": 1. No "it gets worse" left.

| Check | Result |
|---|---|
| 1. Facts | **PASS**. 0 errors; the round 2 taipan item is fixed |
| 2. Opening | **8/10**. Rules 1-14 all OK; the round 2 style-bible 3.5 deviation is fixed |
| 3. Structure & pacing | **8/10** |
| 4. Voice & humour | **8/10** |
| 5. TTS readiness | PASS, with one recommended edit (line 375, "that that") |
| 6. Policy | PASS (0 items) |
| 7. Length | PASS (3,044, brief target 2,900-3,400) |

---

## 0. Round 2 fixes

| # | Fix | Status |
|---|---|---|
| 1 | Taipan's misleading cause of survival | **FIXED.** "mice are not people, which turns out to matter here" is cut. The ranking sentence now comes straight after the claim (line 291), so "That ranking" has its antecedent. Line 307 now ends "survived with fast medical treatment". facts.md row 194 is updated with the museum quote. |
| 2 | Hornet marker (style bible 3.5) | **FIXED.** Line 93: "The nasty twist is in the venom itself. It calls for backup." It names the twist and doesn't announce escalation. The phrase is not used anywhere else and is not a PE phrase. |
| A1 | Taipan lab hedge | **APPLIED.** Line 309: "the snake with the most toxic venom ever measured". |
| A2 | Funnel-web female sentence | **APPLIED** (cut). |
| - | Line 375 "its" ambiguity | **APPLIED**, but the new wording creates "that that" (see section 5). |

## 1. Facts: PASS

I checked 16 claims this round against live pages (WebFetch) or by search. The focus was the four changed items.

**Inland taipan** (Australian Museum, re-opened today):
- "rated as the most toxic of all snake venoms in LD50 tests on mice": matches lines 291 and 309.
- "only a handful of people have ever been bitten... all have survived... due to the quick application of correct first aid and hospital treatment": line 307 ("fast medical treatment") is accurate and phrased as history, not advice.
- Average 2 m, darker in winter, Channel Country of SW Queensland and NE South Australia, "shy... relatively placid", feeds "entirely" on small to medium mammals. All confirmed.
- 1979 ranking: Broad, Sutherland and Coulter, Toxicon 1979. Confirmed.

**Taipan consistency with the rest of the script:**
- The item now gives one reason for zero deaths (rare bites, all treated), plus the callback at line 313 ("common, nearby and easy to step on"). The two don't conflict.
- It also fits the axis comment ("a healthy adult who gets no help"). Its place under "Fast killers" is coherent, and the survival is played as the narrator's disappointment, not as the snake being harmless.

**Asian giant hornet:**
- WSDA (invasivespecies.wa.gov) confirms: 2 in long, about 3 in wingspan, stinger longer than a honeybee's, venom "more powerful than any local bee or wasp", stings repeatedly, and "complete destruction of a healthy colony in a matter of hours" in late summer.
- nippon.com: "191 people died after being stung by wasps and bees, for an average of 17 deaths per year", 2008-2018. It also says swatting can make them "release alarm pheromones to rouse an excited swarm". Lines 91 and 97 match.
- Ono et al. 2003, Nature 424:637 found a multi-component alarm pheromone "in the venom of the world's largest hornet". Line 97 matches.

**Sydney funnel-web** (Australian Museum group page):
- 13 recorded deaths; "only male spiders have been responsible for all"; the male Sydney funnel-web "probably responsible for most".
- Antivenom in 1981, "no deaths have occurred since"; males wander at night November-April.
- The toxin "severely and similarly affects the nervous systems of humans and monkeys, but not of other mammals". All confirmed.
- Australian Geographic has Dr Robert Raven (Queensland Museum) saying "death has occurred with funnel webs in 15 minutes", and a male that "reached 10cm stretched out". Lines 267 and 271 match.

**Box jellyfish:**
- NOAA: "the most venomous marine animal", death "within a few minutes", speeds "approaching four knots" (about 7.4 km/h).
- Australian Museum: up to 30 cm bell, up to 60 tentacles in four clumps, up to 3 m, and "can swim toward movement".
- Fenner and Williamson, MJA 1996: "at least 63 recorded deaths in tropical Australian waters... since 1884".
- All confirmed, as is the 2005 Nature (*Tripedalia*) attribution.

No unsourced claims were found in the changed lines.

## 2. Opening and Script Writer rules (section 7): 8/10

- The opening is unchanged from round 2: the name at word 33, nothing banned before it, the twist at word 133.
- Rules 1-14: no violations.
  - Rule 13: the markers still rotate. The hornet's "The nasty twist" doesn't match its neighbours (bullet ant "But that's not the disturbing part", Komodo "The worst part"). Box jellyfish's "But the worst part" is 6 items after the Komodo's, so it isn't back-to-back.
  - Rule 14: no PE wording.
- The round 2 deviation from style bible 3.5 ("And then it gets worse") is gone.

## 3. Structure & pacing: 8/10

- The changed items are within their bands: hornet 250, funnel-web 250, taipan 260, box jellyfish 350 including the outro.
- **Taipan flow is better.** The claim and its source now sit together, then "Doug has been sent to find it." gives a clean short beat before the setting.
- Escalation, section headers, boss, running gags and the guide close are unchanged and still work.

## 4. Voice & humour: 8/10

- "The nasty twist is in the venom itself. It calls for backup." is a better setup for the swatter kicker than the old line.
- The taipan reads cleaner without the mice aside, and the "quietly deleting it" kicker still lands.
- **Minor, not blocking:** line 283, "It does not matter.", is unchanged from draft 2. Its antecedent (the costume logic from line 277) is two sentences back, after the evolution line. It still works as deadpan.
- The persona is consistent throughout.

## 5. TTS readiness: PASS (one recommended edit)

- **Line 375:** "It found that that species' eye lenses are remarkably well made..."
  - Spoken aloud, the possessive apostrophe disappears, so this comes out as "found that that species eye lenses". Heard, it sounds like a stumble.
  - It's grammatical and Chirp will read it, so I'm not treating it as blocking. It should still be changed before `narrate`.
  - Suggested wording: *"In two thousand and five, a study in the journal Nature looked at a different, smaller species of box jellyfish, and found remarkably well-made eye lenses, even though the eyes seem tuned to see a slightly blurry picture."*
  - This keeps the attribution fix and removes the "its"/"that that" problem. No re-screen is needed for this edit alone.
- Nothing else to flag. There are no digits, symbols, parentheses or abbreviations, and the pronunciation notes cover the hard words.

## 6. Policy: PASS

- **Advertiser-friendly:** no gore. Deaths are cartoon only, and there is no profanity.
- **Made for kids:** adult-coded throughout.
- **Original content:** every item is a distinct mini-story with its own Doug gag.
- **Medical advice:** none. "Survived with fast medical treatment" is a historical statement with no instructions.
- **Title promise:** honest (9 deaths in 12 items).

## 7. Length: PASS

3,044 spoken words, about 15:37 at 195 wpm. Brief target: 2,900-3,400.

---

VERDICT: PASS

There are 0 fact errors and 0 policy items. Hook 8, structure 8, voice 8.

Recommended before narration (not blocking, no re-screen needed):
1. Line 375: remove "that that species'" (see section 5 for wording).
