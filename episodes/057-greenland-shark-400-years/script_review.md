# 057 script review (draft 2)

Script Screener, 2026-11-24. This re-screen checks draft 2 against the draft 1 fixes (F1–F4, R1–R6). I re-read script.md and facts.md,
re-checked the new or changed claims at the source (web), and recounted the script. Draft 1's 16 source checks still stand for the
unchanged lines.

**VERDICT: FAIL**. One required fix remains, in item 6: the new sandwich analogy turns a lab chemical reading into a "safe to eat" claim
and a five-week safety timeline. Everything else from draft 1 is fixed, and all the score gates pass.

| Check | Result |
|---|---|
| Facts | **FAIL**: 1 item (F5). F1 is fixed |
| Hook | 9/10 (R4 fixed) |
| Structure & pacing | 8/10 (F2 fixed) |
| Voice & humour | 8/10 (F3 and F4 fixed) |
| TTS | PASS |
| Policy | PASS on wording. F5 also touches the no-safety-advice rule, and fixing F5 clears it |
| Length | PASS: 2,108 spoken words by my count, 10.8 min at 195 wpm |

## Draft 1 fixes

| Fix | Draft 2 | Status |
|---|---|---|
| F1 reindeer (l.132) | "One Greenland shark was reportedly found with a whole reindeer inside it." Horse is given as "Other reports". The polar bear is primary-sourced (Nielsen 2019). facts.md marks the reindeer and horse rows secondary-only. Save Our Seas ("an entire reindeer") supports the singular, attributed wording | **Fixed** |
| F2 cap kicker (l.282) | "The shark went past the cap without a second look. It has plenty of time to come back for it." It's about the cap and it's dry. It's new: no match in the series bible or in 026, 050 or 055 | **Fixed** |
| F3 lifted marker (l.266) | "Now take the low end:" is our own wording, and it doesn't repeat items 7 or 8 | **Fixed** |
| F4 item 3 joke stack | The newborn line, the fingernail "outgrow" joke and the clipboard line are cut. What's left is the Doug beat, "Doug has died. Again." and the kicker. That fits rule 10. Item length 231 | **Fixed** |
| R1 worldwide (l.206) | "a year worldwide"; facts.md updated | Done |
| R2 item 6 analogy | Swapped for an everyday-object analogy, but the new wording adds a fact error (F5) | **See F5** |
| R3 Hansen (l.80) | "only a few centimeters in total" | Done |
| R4 payoff (l.12) | "a shark that's about four hundred years old" | Done |
| R5 (l.160) | "The shark has a plan for that too." It no longer suggests a bad outcome | Done |
| R6 (l.16) | "swim around with" | Done |
| Staging note (party hat) | Gone from l.198; director note in facts.md | Done |

## 1. Facts: FAIL (1 item)

New or edited claims checked:

| # | Claim (script line) | Source checked | Result |
|---|---|---|---|
| 1 | Reindeer, singular and "reportedly"; horse "reports mention"; polar bear from "one scientific survey" (l.132, l.136) | Save Our Seas; Nielsen 2019 Table 2 (*Ursus maritimus*) | OK |
| 2 | Item 3 added lines: "The biggest Greenland shark ever dated was about five meters long. At less than a centimeter a year, a body that size is not built in a decade, or even in a century." (l.86) | Nielsen 2016 (502 cm, 392 ± 120, low end 272 > 100); NOAA (< 1 cm/yr) | OK. The claim stays safely qualitative and doesn't imply 500 years by linear growth |
| 3 | Fingernails about 4 cm a year, "more than four times faster" (l.82) | Yaemsiri 2010 (3.47 mm/month = 4.2 cm/yr) against < 1 cm/yr | OK |
| 4 | Hansen shark grew "only a few centimeters" in 16 years (l.80) | Sources give 6–10 cm | OK |
| 5 | Fermented about 8 weeks, dried 5; TMAO below detection within 5 weeks (l.174) | Matís study page for Jensen et al. 2023 (fetched): "fermented for eight and seven weeks … then dried for five weeks"; TMAO "below the limit of detection within five weeks" | OK |
| 6 | **"It's a sandwich you have to leave in the fridge for five weeks before it's safe to eat"** (l.176) | Same page: the study measured TMAO only. It doesn't address food safety, and spoilage organisms *increased* during fermentation and fell only during drying. The study product was fermented 8 weeks and dried 5 more. Fermentation isn't refrigerated | **FAIL (F5)** |
| 7 | 2014 Icelandic government release: almost all Greenland sharks landed are bycatch (l.178) | government.is, 29 Jan 2014 (title and summary) | OK |
| 8 | "at least three thousand five hundred of them a year worldwide" (l.206) | COSEWIC 2025 "global estimates" | OK |

## 2. Opening: 9/10
- The first sentence is unchanged and passes. The payoff promise now says "years" and "shark". "The Eye." is still at word 33, with nothing
  before it that breaks the rules. The twist is at about word 118.
- Writer rules 1–14: no violations. Rule 1 is overridden by the retention update. Rule 9: average 14.0 words per sentence (at the floor), max 31.
  Rule 13: twist markers are never back to back.

## 3. Structure & pacing: 8/10
- The axis is still monotonic and the boss is the most extreme. Items run 211–257 words, all inside the bible's 200–260. Running gags and the
  counter (414 to 420) are unchanged and correct. The LIVE feed closes on a kicker about the cap.
- Nit (not blocking), l.86: "The biggest Greenland shark ever dated was about five meters long" uses the same wording as the boss reveal at
  l.256 ("The biggest Greenland shark ever dated was a female…"). Consider "The biggest ones reach about five meters" so the boss line stays fresh.

## 4. Voice & humour: 8/10
- The deadpan holds and I found no lifted competitor phrase. "It has plenty of time to come back for it." is a good last beat.
- Nit, l.88: "This isn't a sick or hungry shark, since everything about this animal runs slowly" reads awkwardly with "since". Consider
  "This isn't a sick or hungry shark. Everything about this animal runs slowly…".

## 5. TTS: PASS
No symbols, abbreviations or digits in the narration. The pronunciation notes are unchanged.

## 6. Policy: PASS on wording
Advertiser-friendly, adult-coded and original. The title promise is supported by the spoken range. The one concern is F5: "five weeks before
it's safe to eat" gives viewers a safety timeline for a food the script calls poisonous, which goes against the no-safety-advice rule
(brief §7). The F5 fix removes it.

## 7. Length: PASS
2,108 spoken words, 10.8 min. That is inside 1,950–2,350 and `target_minutes: [10, 12]`.

## Required fixes
1. **F5 (fact and safety), l.176:** "It's a sandwich you have to leave in the fridge for five weeks before it's safe to eat, which is the exact
   opposite of how sandwiches work." The study showed only that one chemical fell below detection at five weeks. It never called the meat safe
   at that point, the full process ran about thirteen weeks (eight fermenting, five drying), and fermentation isn't done in a fridge. Remove
   "safe" and the fridge, and tie the time to the whole process. For example: "It's a sandwich you have to leave alone for about three months
   before anyone will eat it, which is the exact opposite of how sandwiches work." Update the facts.md row for The Meat to match: 8 + 5 weeks ≈ 3
   months; the analogy makes no safety claim.

Once F5 is fixed, the script passes. The two nits are optional.

Sources checked: [Matís, Jensen et al. 2023 study page](https://matis.is/en/?p=50964) ·
[Government of Iceland, 29 Jan 2014](https://government.is/news/article/2014/01/29/Almost-all-Greenland-sharks-caught-on-Icelandic-fishing-grounds-are-by-catch-in-fishery-for-other-species.-nbsp) ·
[Save Our Seas](https://saveourseas.com/worldofsharks/species/greenland-shark) ·
[Nielsen 2019 Frontiers](https://www.frontiersin.org/articles/10.3389/fmars.2019.00125/full) ·
[COSEWIC 2025](https://www.canada.ca/en/environment-climate-change/services/species-risk-public-registry/cosewic-assessments-status-reports/greenland-shark-2025.html) ·
[Nielsen 2016 Science](https://pubmed.ncbi.nlm.nih.gov/27516602/) · draft 1 sources unchanged.
