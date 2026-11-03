# 036 Army Ant Swarm: script review (draft 2)

Script screener, 2026-11-03, re-screen. Read: style bible (retention update 2026-10-27, 3.2, 3.3, section 7), series bible, brief.md, script.md (draft 2), facts.md (draft 2), decisions.md, and the draft 1 to draft 2 diff, including config/channel.yaml.

**VERDICT: FAIL**

Draft 2 fixes all four draft 1 fact items and the rule 8 gap. Hook, structure, voice and policy are unchanged and still clear the PASS bar. One fact item remains, and it was introduced by the new Road Crew analogy (F5). It is a one-sentence fix. Once it is in, this script passes.

| Check | Result |
|---|---|
| Facts | **1 FAIL item** (F5, new). F1-F4 from draft 1 are fixed. |
| Hook / opening | **8 / 10** (unchanged; item 1's name still at word 35) |
| Structure and pacing | **8 / 10** |
| Voice and humour | **8 / 10** |
| TTS readiness | Pass |
| Policy | Pass (0 items) |
| Length | 2,168 spoken words (my count; about 11.1 min), inside 1,950-2,350. Pass. |

---

## 1. Facts

### Draft 1 items: verification of the fixes
| # | Draft 2 line | Check | Result |
|---|---|---|---|
| F1 | L270 "About a century ago, the naturalist William Beebe found a ring..." and label "BRITISH GUIANA" (L268) | The book was published in 1921 and the observation came before that, around 1916-1920 (Kalacoon or Kartabo). That is 106-110 years ago, so "about a century ago" holds whichever station it was. No year is on the label. The stage direction "1920s explorer" describes a costume style and is not spoken, so it is acceptable. | **FIXED** |
| F2 | L478 "The biggest army ant colonies on Earth only catch what can't get out of their way." | H&W: *D. wilverthi* up to 22 million is the largest army ant colony; driver ants kill creatures "too sluggish to get out of the way". The claim is now scoped correctly. | **FIXED** |
| F3 | L364 "In cool weather, the colony keeps the nest warmer when the young inside are pupae than when they are larvae. Scientists think it may be saving energy on the larvae." | This matches the Baudier 2019 abstract ("When ambient temperature was low ... pupal bivouacs were warmer"; "potentially conserved energy by investing less metabolic heating in larval brood"). The condition is present and the cause is framed as a hypothesis. | **FIXED** |
| F4 | L190 "Even those enormous jaws can't cut, unlike the jaws of their African relatives." | This is H&W nearly word for word ("lacking a cutting or shearing edge ... unlike their African relatives the 'driver ants'"). It also sets up the L452 callback ("these jaws do cut") cleanly. | **FIXED** |

### New and changed lines
| Line | Claim | Screener check | Result |
|---|---|---|---|
| L92 | Ocellated antbird about the length of a pencil | Wikipedia, re-fetched: "17.5 to 20 cm long" and an "obligate ant follower" of *Eciton burchellii* swarms. A standard unsharpened pencil is about 19 cm (7.5 in), which falls inside the bird's range. The label "ABOUT 19 CM" is fine. | **VERIFIED** |
| L176 | Soldier about 12 mm, roughly two grains of rice end to end | ADW, re-fetched: "worker sizes range from 3mm to 12mm". Soldiers are the largest caste. Wikipedia gives the same range, and one hobbyist site says 14 mm, so "about" is right. Long-grain rice is 6-8 mm, so two grains are 12-16 mm and "roughly" covers it. | **VERIFIED** (the soldier length is inferred from the top of the worker range; this is acceptable with "about") |
| L224 | "The workers range from about three millimeters long to twelve, so the smallest plug is about the size of a sesame seed." | The size range (ADW) and a sesame seed of about 3-4 mm are both fine. **The "so the smallest plug" step is not sourced.** Powell & Franks 2007, the Bristol release, NatGeo and Science News all say only that pluggers size-match to holes and that a big ant leaves a small hole "for a smaller comrade". They also say plugging is done by "a minority of ant workers". No source says the 3 mm minims plug holes, or gives any plug size. | **FAIL (F5)** |
| L400 | "And she does it again every few weeks, for years." | The laying burst comes once per statary phase, in a cycle of about 2-3 weeks statary plus 2-3 weeks nomadic (H&W). "For years" rests on the 4.5-year marked queen. | **VERIFIED** |
| L400 | Marked queen found again 4.5 years later | Split out as recommended. Same H&W source. | **VERIFIED** |

Unchanged claims were verified against sources in the draft 1 review (22 claims, plus the 5 writer flags) and still stand.

### FAIL item
- **F5. L224 and the stage direction at L222.** "...so the smallest plug is about the size of a sesame seed." This is the writer's inference, not a sourced fact, and the "3 MM" label on "the smallest ant in the smallest hole" depends on it. (My draft 1 suggestion for this item said "only from a sourced length". No sourced plugger length exists.)

---

## 2. Opening: 8 / 10 (unchanged)
The first 37 spoken words are unchanged from draft 1. The concrete first sentence with a number, the payoff promise at word 32, item 1's name at words 35-37, no greeting, and the twist marker at word 140 all still pass. The risk is the same as before: one more word ahead of "The Swarm Front." pushes the name past 35.

### Script Writer rules 1-14
- **Rule 8: now met in every item.** The Followers has the pencil, The Soldiers has the rice, and The Road Crew has the sesame seed (the analogy survives the F5 fix, see below).
- Rule 11: violated only by F5.
- Rule 13: the twist markers still rotate. "The surprising part" (L234) is new wording and repeats none of the others.
- Sentence stats (my count): 154 sentences, average 14.1 words, longest 34. No new sentence is over 30 words.
- Every other rule passes, as in draft 1.

## 3. Structure and pacing: 8 / 10
- Segment words (my count): Front 231, Followers 205, Menu 194, Soldiers 209, Road Crew 199, Spiral 223, Night Move 195, Living Nest 210, Queen 211, Driver Ants 257. None is over the 260 maximum. Menu, Night Move and Road Crew are 1-6 words under the retention band's 200. These were not flagged in draft 1 and are not blocking. Do not pad them.
- The axis, escalation, death counter (281-287), running gags and ending are unchanged and all pass.

## 4. Voice and humour: 8 / 10
- The new lines are flat-factual and fit the narrator's deadpan voice. The Queen split reads better than draft 1 did.
- L364's "Scientists think it may be saving energy on the larvae." is a slightly limp end to the twist, but it is accurate. It doesn't block.
- "The narrator would like that noted." (L474) is still the creative director's decision, as in draft 1.

## 5. TTS readiness: pass
- No digits, symbols, parentheses or abbreviations are in the spoken text.
- Rettenmeyer, Beebe and Guiana are now in `config/channel.yaml` `voice.pronunciations`, with correct IPA.

## 6. Policy: pass (0 items)
None of the changes affects advertiser-friendliness, the made-for-kids signals, originality, advice or the title promise.

## 7. Length: pass
2,168 spoken words, about 11.1 min at 195 WPM.

---

## Required fix
1. **F5, L224 (and L222).** Replace "The workers range from about three millimeters long to twelve, so the smallest plug is about the size of a sesame seed." with a line that compares worker size only and makes no claim about the plugs. For example: "The smallest workers are only about three millimeters long, about the size of a sesame seed." Change the L222 stage direction to match: show a small worker beside a sesame seed, labelled "3 MM", **not** "the smallest ant in the smallest hole". Update the facts.md row to drop "smallest plug" and keep the ADW and sesame sources.

After that, the script needs only a quick check of that line. Everything else meets the PASS thresholds.

Sources checked this pass: https://en.wikipedia.org/wiki/Ocellated_antbird, https://animaldiversity.org/accounts/Eciton_burchellii/, https://www.bristol.ac.uk/news/2007/5465.html, https://www.nationalgeographic.com/science/article/army-ants-plug-potholes-with-their-own-bodies, Crossref record for doi 10.1016/j.anbehav.2006.11.005 (no abstract available).
