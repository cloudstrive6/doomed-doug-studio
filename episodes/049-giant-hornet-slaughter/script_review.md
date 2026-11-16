# 049 script review (draft 2): Script Screener, 2026-11-16

VERDICT: FAIL

Hook 7/10 · Structure 8/10 · Voice 8/10 · Facts: 0 errors · Policy: 0 items · Length 2,002 words (target 1,950–2,350, OK)

All five round-1 fixes landed correctly. There are two new required fixes, and each is a one-line edit. The first is the
opening promise line, which you asked me to test. The second is a continuity bug that was already in draft 1 and that I missed last round.
No new research is needed. After these two edits I expect a PASS with hook 9.

## Required fixes

1. **Opening promise, line 9: it works without "By the end", but the payoff noun is now ambiguous.**
   "Doug ends up holding open a tree that could have produced nearly two hundred queens."
   - What works: "ends up" reads as a forward promise, so dropping "By the end" costs nothing. The line is specific (a tree,
     a number), unresolved, matches the boss, and no longer overclaims. It lands at spoken word 31, about 0:09.
   - What fails: draft 1's "hornet" was dropped, so the line now just says "queens". The sentence right before it ends on
     "thirty thousand honeybees", and honeybee colonies have queens and nest in tree hollows. A stranger who just clicked can
     read this as a tree that produces bee queens, which sounds harmless. The open loop only grips if they hear *hornet* queens.
   - Word budget: "The Hunter." sits at spoken words 34–35, which is the limit. Adding "hornet" without cutting something
     pushes it to 35–36 and breaks writer rule 2.
   - **Change it to:** "Later, Doug holds open a tree that could have produced nearly two hundred hornet queens." That is 15 words,
     the same count as now, so "The Hunter." stays at 34–35. Any 15-word version that includes "hornet" and keeps "could have produced
     nearly" is fine.

2. **Continuity: line 167 refers to a nickname the viewer hasn't heard yet.**
   "But here's what the nickname leaves out."
   This is in The Sting, item 6. "Murder hornet" is first said in The Hitchhiker (line 221), two items later. Before that, the only
   name the episode uses is "northern giant hornet". The twist marker therefore points at nothing. Change it to a
   marker that doesn't depend on the nickname, for example "But here's what the scary reputation leaves out." Don't use a marker
   that's already used elsewhere. The markers currently rotate cleanly, so keep it that way.

## Advisory (not blocking)
- Line 239, "One tagged hornet flew straight home": WSDA tagged several hornets and lost the signal before it found the tree. "Straight" is colour,
  not a source claim. Dropping it ("One tagged hornet led them home, to a hollow inside a tree...") is safer.
- Line 55, "roughly a walk to the corner shop", is used for 1–2.5 km. Most corner shops are well under a kilometre away. "Roughly a twenty-minute walk" would be truer.
  This is not required.
- The Japan figure is now "about twenty a year". That is consistent with the Toyo Keizai lead, kango-roo's summary of MHLW data ("毎年20人前後") and nippon.com
  (2008–18 average just over 17). It is acceptable as worded, and the per-year card numbers are gone, so last round's caveat is closed.
- Shaanxi: Xinhua/China Daily give 1,640 injured, and other reports give 1,600 or 1,675. "Around sixteen hundred" and "ABOUT 1,600" are fine.

## Round-1 fixes: status
1. Payoff no longer overclaims. It now says "could have produced". DONE (see new fix 1 for the noun).
2. "made it famous as the murder hornet". DONE. Dictionary.com and Global Voices confirm the name was popularised in English in May 2020 and comes from an older Japanese term.
3. The "Asian giant hornet" name moved out of item 1 and into the Hitchhiker rename beat, so item 1 now opens on "the largest hornet in the world" and the AA battery. DONE.
4. "they wear face masks too" is now descriptive. DONE.
5. The Toll now has "Doug has nothing to add." DONE.

## 1. Facts: 15 claims re-verified this round, 0 errors
Fetched or searched again today:
- Herald/WSDA: 76 emerged queens, 108 capped cells, "nearly 200 queens" could have come from the nest, and only a small share of queens start colonies. These match lines 9 and 245.
- KUOW/AP: dental floss and radio trackers, a basketball-sized nest.
- WSDA/USDA, 18 Dec 2024: as little as 90 minutes, BC Aug 2019, WA Dec 2019, DNA showing two introductions, three nests in 2021, half of detections from the public, three years without detections, eradicated.
- RIKEN rr/8130: "almost 100 kilometers a day", 17 amino acids, a drink "consumed by millions of people a year". RIKEN's history page says 80 km. The script attributes the 100 km figure to Riken, which the news page supports.
- Sugahara & Sakamoto 2009: the ball stays at or below 45.9 °C, the hornet's lethal limit is 45–46 °C, the bees' is 50–51 °C, the hornet dies in under 10 minutes, and CO2 helps.
- CPSC: hot tubs never above 104 °F (40 °C).
- ESA, 25 Jul 2022: renamed northern giant hornet, replacing "murder hornet" and "Asian giant hornet".
- Shaanxi 2013: 42 dead (Xinhua), about 1,600 injured, attacks since July, officials blamed the (Asian) giant hornet.
- Japan: about 20 sting deaths a year (MHLW, via secondary sources), not species-specific.
- Arithmetic: 8 × 0.76 mm = 6.1 mm; 12.19 m / 5 cm ≈ 244; 100 km / 42.195 km ≈ 2.4 marathons; 46 − 40 = 6.
- Everything else (NYT 1995 figures, WSU FS347E quotes, BC release) was verified last round, and that text is unchanged.

## 2. Opening: hook 7/10 (expected 9 after fix 1)
- First sentence: concrete, with numbers and a death stake that the title promises. PASS.
- Payoff promise by 0:10: specific and unresolved, and "By the end" isn't needed. **MISS until "hornet" goes back in (fix 1).**
- "The Hunter." at words 34–35. There is no greeting, channel name, "in this video" or subscribe ask before it. PASS, but there's no slack left.
- Twist "Here's the strange part." at word about 100 (about 0:31), inside 145. PASS.
- Item 1 opens on its best fact (largest hornet, battery scale), and the meat-ball loop follows inside 145 words. PASS.
- Writer rules (section 7): rule 1 is superseded by the retention update. No rule from 2 to 14 is violated. Rule 9 is now met in every item (each has a sentence of 6 words or fewer).
  Twist markers rotate with no repeats in a row, and the outro is 17 words. The Sting marker is a continuity issue (fix 2), not a rule-13 breach.

## 3. Structure and pacing: 8/10
9 items, each 200–260 words (Nest 245 plus a 17-word outro). The axis rises from bee to hive to person to continent, the boss is the most extreme item, the honesty line comes after the death, and there are re-hooks at the band changes.
Gags are present: counter 368 to 374, "did not agree" once, "hi friend?" once, the costume arc, the field guide, the quietly disappointed narrator, and the tracked cap. The mid-video dip at The Heat Ball remains a soft spot, not a blocker.

## 4. Voice and humour: 8/10
135 sentences, average 14.8 words, maximum 35, Flesch about 70. Deadpan and consistent. No competitor phrasing. Joke density is within rule 10.

## 5. TTS readiness: PASS
No digits, symbols, abbreviations or parentheses in the spoken lines. Keep the pronunciation hints for Nanaimo, Shaanxi and Riken in the narrate step.

## 6. Policy: PASS
- Advertiser-friendly: cartoon deaths, no gore, no profanity.
- Made-for-kids: adult-coded tone.
- Inauthentic content: original narrative.
- Medical and safety advice: none. The masks line is descriptive, and the public reporting is told as history.
- Title promise: still delivered ("Twenty or thirty" is spoken, never "thirty" alone).

## 7. Length: PASS
2,002 spoken words, about 10.3 minutes.

VERDICT: PASS (fixes verified)
