# 025: script review (draft 1)

Script screener, 2026-10-22. Read: style bible, series bible, brief, script.md, facts.md. Web-checked 24 claims.

| Check | Result |
|---|---|
| 1. Facts | **FAIL**: 3 items (F1-F3) |
| 2. Opening | **8/10**. Rules 2 and 6 met. Script Writer rule violated: **5** (see F3) |
| 3. Structure and pacing | **6/10** |
| 4. Voice and humour | **8/10** |
| 5. TTS readiness | **FAIL**: 1 item (T1), plus 1 advisory |
| 6. Policy | **PASS**: 0 items |
| 7. Length | **PASS**: 2,976 spoken words (my count matches the writer's). The brief's band is 2,950-3,350, so there are only 26 words of headroom |

## 1. Facts

### Verified against sources (24)
| # | Claim | Source checked | OK |
|---|---|---|---|
| 1 | Oxygen peak estimated at about 27-35% | Harrison 2010; Scott & Glasspool 2006 (older model 32-35%, newer about 30%) | yes |
| 2 | Fires possible in wet swamps at about 25% O2 | Scott & Glasspool 2006 ("even in wet mire settings") | yes |
| 3 | Up to 40% of a coal layer is charcoal | Scott & Glasspool 2006 | yes |
| 4 | Bojophlebia wingspan "nearly 40 cm", Ar/Ar 309 Ma, Prague museum | Sroka et al. 2015 PDF (text extracted) | yes |
| 5 | Bojophlebia is no longer a mayfly; sister group of the rest of Hydropalaeoptera | Wikipedia, ZooBank | yes |
| 6 | Megarachne: 1980 "largest spider", 50 cm leg span vs Theraphosa 30 cm, 2005 eurypterid, about 54 cm, raking blades | Selden et al. 2005 | yes |
| 7 | Megarachne: second, more complete specimen; freshwater floodplain; museum spider models | Wikipedia (Megarachne) | yes |
| 8 | Meganeura: about 65-75 cm, Commentry, about 300 Ma, leg-spine "flying trap", griffinfly not dragonfly | Wikipedia (Meganeura) | yes |
| 9 | Largest living odonate about 19 cm (Megaloprepus) | Guinness | yes |
| 10 | First pterosaurs "tens of millions of years" later | NHM: about 215 Ma | yes |
| 11 | Insect size tracked O2 for the first 150 Myr, then decoupled when birds arrived | Clapham & Karr 2012 | yes |
| 12 | 2026 Nature study: tracheoles take about 1% of flight muscle | Snelling et al. 2026 (Greifswald, ScienceDaily, Sci.News) | yes |
| 13 | Pulmonoscorpius: about 70 cm (largest individual), 341 Ma, Latin "lung", book lungs mean fully terrestrial, probable diet | Wikipedia (Pulmonoscorpius) | yes |
| 14 | Pulmonoscorpius "the size of a house cat", small pincers, venom | Countryfile | yes |
| 15 | East Kirkton scorpions are the earliest shown for certain to be terrestrial; book lungs came from gills | Selden & Jeram 1989; still the standard reading | yes |
| 16 | Hibbertopterus trackway: 6 m x 0.9-0.98 m, about 330 Ma, trackmaker about 1.6 m x 1 m, Whyte 2005, largest walking-arthropod trackway | Whyte 2005 (Nature abstract) | yes |
| 17 | Near St Andrews, Fife; how it breathed on land is unknown; sweep feeder in freshwater swamps and rivers; H. scouleri grew larger | Wikipedia (Hibbertopterus) | yes |
| 18 | Crassigyrinus: "tadpole from hell", 2-3 m, coal swamps in Scotland and North America, crushed fossils, moray-eel head redrawn as a crocodile shape, "almost a century", eyes, lateral lines, "practically anything" | NHM 2023 | yes |
| 19 | Arthropleura: January 2018, found by a former PhD student, 75 cm moulted segment, "as big as a car", about 45 Myr, extinct in the Permian | Cambridge | yes |
| 20 | Arthropleura is older than the O2 peak, so oxygen "cannot be the only explanation"; possible predator (Davies); open coastal woodland; no head found | Cambridge | yes |
| 21 | Arthropleura up to 2.6 m, 345-290 Ma, 4 cm juvenile from France, millipede body with centipede-like head, scavenger on decaying plants | ESRF 2024 | yes |
| 22 | Arthropleura about 50 kg | Cambridge (paired with **2.7 m**, see F3) | yes |
| 23 | **Megarachne "had no pincers at all"** | not in any cited source | **NO, F1** |
| 24 | **Crassigyrinus "Technically, it was a tadpole"** | contradicted by NHM ("early tetrapod") | **NO, F2** |

### FAIL items
- **F1. Megarachne pincers (line 104):** "It had no pincers at all."
  facts.md cites Wikipedia for this, but neither Wikipedia nor Selden et al. 2005 says it. Eurypterids have small pincer-tipped
  chelicerae. The 2005 paper only shows that Hünicken's supposed fangs were a carapace ridge. The claim is unsourced and probably
  false. Doug's beat doesn't depend on it, because the river kills him either way.
- **F2. Crassigyrinus kicker (line 284):** "Technically, it was a tadpole."
  Crassigyrinus was an adult early tetrapod, not a larva. "Tadpole" comes from its nickname, and the script has already, and
  correctly, cut the name meaning. As written, the kicker states something false as "technically" true.
- **F3. The writer's flagged weak spot: Crassigyrinus vs Arthropleura size order.** Confirmed as a real problem, not just a weak spot.
  - NHM (Porro) gives Crassigyrinus as "around two to three metres". Arthropleura is "up to 2.6 m" (ESRF) or "around 2.7 m"
    (Cambridge). Both of the boss's numbers are top-end estimates.
  - The writer's justification compares Crassigyrinus's *midpoint* (2.5 m) with Arthropleura's *maximum* (2.6 m). That is two
    different methods. On a like-for-like basis (top vs top) the tadpole is longer (3 m vs 2.6-2.7 m), and on midpoints nobody can
    say which is bigger.
  - So Script Writer **rule 5** ("the last item must be the most extreme on that axis") cannot be shown to hold. The episode axis is
    body size, not "bug size".
  - The on-screen meter also breaks. The tape reads "ABOUT 2 TO 3 M" at item 8, then drops to "ABOUT 2.6 M" at the boss, so it is not
    monotonic, which the brief requires.
  - The boss stage direction says the tape "passes the top of the Doug silhouette" at item 9. A 2-3 m animal at item 8 has already
    passed it.
  - Viewers who know Crassigyrinus is "2-3 m" will see the "biggest" claim fail on screen.

## 2. Opening: 8/10
- Item 1's name falls at words 32-33. Nothing comes before it except the title promise and "Doug did not agree to this."
- The twist marker ("Here's the problem.") is at about word 114, roughly 35 s in. The fire payoff lands at about word 170.
- What costs points:
  - Item 1's first death comes at about 1:35. The brief asked for about 1:20.
  - The "A quick word on 'bugs'" aside (line 40) is a slow meta-beat just before the first death.
- Rule-by-rule (section 7, rules 1-14):
  - **Rule 5 violated (F3).**
  - Rule 8 is borderline at item 1: "one breath in five" is a ratio, not an everyday object. The brief suggested that analogy, so
    this is advisory only.
  - All other rules pass:
    - Item count is 9 and every item has a 1-5 word name.
    - Twist markers rotate with no repeats.
    - "actually" is used once; "However", "essentially" and "incredibly" are not used.
    - Average sentence length is 14.4-15.3 words, the longest is 34-35, and every item has a sentence of 6 words or fewer.
    - Flesch is 71.3.
    - There are no transition sentences.
    - The outro is 24 words.

## 3. Structure and pacing: 6/10
- **Escalation:** sizes rise from about 40 cm to 2.6 m in two bands, and the survivals at 4 and 7 are spaced well.
  - The axis is broken at the top (F3), and that is the main deduction.
- **Segment lengths:** items 1-8 run 299-332 words, all inside the brief's bands.
  - The boss is 447 words including the 24-word outro, so about 423 words. That is just over the brief's 360-420 (advisory).
- **Running gags:** all present and within limits.
  - The counter runs 203 to 210, and death 210 is flat.
  - "Doug did not agree to this." appears once.
  - "Doug is fine." appears twice, with the narrator disappointed both times.
  - "hi friend?" is used three times, at items 4, 8 and 9.
  - The cap appears at every death.
  - There is exactly one callback, to 007.
- **Ending:** the closing kicker follows the brief, and the outro is 24 words with one CTA.
- **Advisory, title promise:** the title is "...Bugs Could Kill Doug", but bugs directly cause only 3 of the 7 deaths. The others are
  fire, peat, the river and a non-bug. The outro owns this ("Bugs that noticed him: almost none"), so it is not a policy issue. It is
  still a retention risk worth the creative director's attention.

## 4. Voice and humour: 8/10
- **Lines that land:**
  - "a brave place to land"
  - "the one direction that peat never comes from"
  - "it was trying to put Doug back"
  - "that was the whole of his plan"
  - the leaf hat that is "slightly insulted"
- The narrator persona is consistent. The third-person "The narrator..." lines have precedent in 003, 019, 023 and 024.
- **No competitor lifting found.**
  - "Here comes the strange part" stays at the 3-word limit against PE's "Here comes the crazy part". This is advisory: it is the
    closest thing to a noun-swapped PE tic, so rotate it out next episode.
- **Weak twist marker (advisory):** "The worst part is how it breathed." (line 200). Book lungs aren't "worst". The real payoff is that
  it was on land. Consider "The surprising part is..." or a similar marker.

## 5. TTS readiness
- **T1 (required):** "near St Andrews" (line 226). Chirp may read "St" as "Street". Write "Saint Andrews".
- **Advisory:**
  - Add pronunciations for **Palaeodictyoptera** ("PAY-lee-oh-DIK-tee-OP-ter-uh"), **eurypterid** ("yoo-RIP-ter-id") and
    **West Lothian** ("west LOH-thee-un") to the editor's guide.
  - No digits, symbols or parentheses appear in the spoken text.

## 6. Policy: PASS
- **Advertiser-friendly:** no gore. Every death is cartoon (soot, sinking, cut-before-landing, cut-to-black) and there is no profanity.
- **Made-for-kids risk:** low.
  - The cupcake bubble "happy trip!" and the garden-pond tadpoles are the softest beats.
  - The surrounding narration is dry and adult-coded, so this passes.
- **Inauthentic or repetitive content:** each item has its own narrative and twist, and the oxygen thread runs through the episode with a
  sourced resolution.
- **Advice and claims:** there is no medical or safety advice. The oxygen link is stated as debated three times, with no
  over-claiming.

VERDICT: FAIL

## Required fixes
1. **F1, line 104:** "It had no pincers at all."
   - Cut this sentence.
   - The next sentence should start "Its front limbs carried blades..." (drop "Instead,").
   - Remove the "no pincers" row from facts.md, item 3.
2. **F2, line 284:** "Technically, it was a tadpole. Nothing about it was small, except the legs."
   - Replace the first sentence with a true one that keeps the joke, for example "Technically, the museum calls it a tadpole."
   - Keep the second sentence.
   - The kicker must still be 8-25 words.
3. **F3, Crassigyrinus vs Arthropleura.** Keep the order, since the brief locks the boss to last. Make the ranking honest and the meter
   consistent, all three of these:
   - (a) **Add one spoken line in The Millipede**, after the size paragraph (line 296), saying plainly that the tadpole from hell may
     have been just as long, but Arthropleura is the largest bug, the largest land arthropod known. Source it with the existing NHM and
     ESRF rows.
   - (b) **Fix the tape measure so it never goes down.**
     - Item 8 shows the range as a dashed bracket, "2 TO 3 M?", rather than a reading.
     - The boss shows Arthropleura's solid reading.
     - Change the line 298 direction "passes the top of the Doug silhouette" to match, because Doug was already passed at item 8.
     - Alternatively, the creative director approves a one-off break in monotonicity; that decision must be written into the script
       header.
   - (c) **Rewrite the axis comment (line 1) and deviation 4.** Drop the "middle of each range" argument. Say the boss is the largest
     *bug*, and that the one non-bug overlaps it and is acknowledged on air.
4. **T1, line 226:** change "St Andrews" to "Saint Andrews".
5. After these edits, **re-count**: spoken words must stay at 2,950 or more (the draft is at 2,976, and fix 1 removes 6 words). The
   boss segment should come down toward 420 words or fewer.

Advisory (not blocking):
- Line 58: "a little wider than a bowling pin is tall". The source gives "nearly 40 cm" against a 38 cm pin, so "about as wide as" is
  safer.
- Line 238: "it's the largest trackway ... found so far" is a 2005 statement. Use "was the largest found at the time" or attribute it to
  2005.
- Line 200: swap the "worst part" marker.
- Rotate out "Here comes the strange part" in future episodes.
- Add the TTS pronunciations listed in section 5.
