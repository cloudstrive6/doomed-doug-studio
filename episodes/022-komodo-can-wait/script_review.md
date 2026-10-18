# 022 Script review: draft 1 (screener, 2026-10-18)

VERDICT: FAIL

The gates that fail are facts (3 errors) and the Script Writer rules (9, 13/14). Hook 8, structure 7, voice 7, policy clean.
This needs a light revision, not a rewrite. Every fix below is a line edit.

| Check | Result |
|---|---|
| 1. Facts | **FAIL**: 3 errors (a misattributed statistic and two over-claims) and 1 internal contradiction |
| 2. Opening | **8/10**. Item name at word 25, twist marker at word 101 (about 0:31), no greeting |
| 2b. Writer rules violated | **4** (Frame in The Buffalo), **9** (average sentence length; The Crowd), **14** (a lifted PE tic). Borderline: 7 |
| 3. Structure and pacing | **7/10** |
| 4. Voice and humour | **7/10** |
| 5. TTS | **FAIL** (minor): "IUCN", "DNA" |
| 6. Policy | **PASS**. No gore, adult-coded, original narrative, no safety advice, title promise kept |
| 7. Length | **PASS**: 2,940 spoken words (brief 2,900-3,300), about 15:05 at 195 wpm |

---

## 1. Facts

I re-opened all six claims the writer flagged, plus 22 others (28 in total).

### The writer's flagged list
| Claim | Result |
|---|---|
| Iron-coated teeth, 2024, King's College London | **OK**. KCL press release (fetched): iron on the "cutting edges and tips", orange, keeps the serrations sharp, *Nature Ecology & Evolution* 2024. Change the facts.md tag from Search to Fetched. |
| Columbus Zoo feeding order | **OK**. The page (fetched) says the biggest male eats first, then smaller males, then females, then "the younger ones, who come down from the trees to eat once the adults have left." Change to Fetched. |
| Attacks on people rare | **OK**. AP/NBC 2009 (fetched): "Komodo dragon attacks are still rare, experts note." The line has no attribution and is sober. Advisory: the brief asked for an IUCN or park-authority source. Add one to facts.md if you can; this is not blocking. |
| 70/20/10 "Fry figures" | **ERROR: misattributed.** Smithsonian magazine (fetched) gives the figures to **Tim Jessop** (an ecologist, then at the University of Melbourne), not to Fry. Fry speaks in the paragraph before it. Fry et al. 2009 (PNAS, fetched) has no such percentages, and neither does Fry's venomdoc page. See fix 1. |
| 71% habitat | **OK as worded**. NHM (fetched): "the most extreme predictions suggest that the dragons could lose up to 71% of their habitat in the next 45 years". It links this to rising seas (the caption) and rising temperatures. "Fewer than 1,400 adult dragons" and "Vulnerable to Endangered" also check out. Keep 71%. |
| Comparison objects | **OK**. Copenhagen cycling averages 15.3-16.9 km/h (Bicycle Accounts), so 20 km/h is "a little faster". Steinway D is 480 kg (several dealers agree). Britannica gives a breed range of 400 kg (wenzhou, carabao) to 900 kg. A quarter is 24.26 mm, a tennis ball 56-59.4 g, a track lap 400 m, a team 11 players, a marathon 42.2 km. Asian elephant pregnancy is 18-22 months. 4,000,000 / 5,000 is 800. The arithmetic holds. The repetition problem is in section 4. |

### Others verified (all OK against the fetched source)
Smithsonian National Zoo: 16-20 km/h, hours beside a game trail, 4 km for carrion, up to 80%, cannibalism of young, ritual combat, islands.
SDZWA: larger dragons sit and wait while medium ones forage (Harlow 2010), up to 10 km a day, the 50 kg female and 31 kg boar in 17 minutes, cool nights delaying digestion up to 5 days, one large ungulate a month (see fix 2).
San Diego Zoo: about 60 teeth and 4-5 sets, 5.5 lb in one minute, decoy nests, the hatchling up the nearest tree.
Fry 2009 PNAS: 6.5 times less than *C. porosus*, postcranial pull, sharks and Smilodon, Megalania at least 575 kg and over 5.5 m.
Bull 2010: 20 feeding observations, 70% with more than one lizard, "tens of lizards ... over several days", up to 90 kg, buffalo the largest ungulate, the stalked-deer caption.
Jessop 2018 via National Geographic: ten sites, only two of over a thousand recaptures moved, open water "exceptionally rare", 7 miles a day, inbreeding.
Hocknull 2009: insular giantism rejected, Australian fossils referable to *V. komodoensis*, 900,000 years of stable size, the Stegodon idea rejected, "long-term survivor". ScienceDaily: fossils from 300,000 to about 4 million years old.
National Geographic: Flora and Sungai, four young, over two years, Liverpool and Watts, all male.
Venomdoc: buffalo attacks "invariably unsuccessful", introduced about 300 years ago.

### Errors and over-claims (each needs a fix)
- **F1** (The Follow): the 70/20/10 figures are attributed to Fry's team. The source is Jessop.
- **F2** (The Fast): "An animal that only needs a dozen meals a year". SDZWA says a large dragon *takes* about one large ungulate a month, "supplemented by smaller prey" (birds, rats). That is not a total of 12 meals, and it is not what the dragon *needs*. This is the "dozen meals a year" lead the brief and facts.md both cut, brought back as arithmetic.
- **F3** (The Swim, kicker): "Out here, every island comes with its own set, already waiting on the beach." This is false as a general claim. Wild populations live only on Komodo, Rinca, Flores, Gili Motang and Nusa Kode, and other islands in the park, such as Padar, have none. facts.md files it as narrator framing, but the viewer hears a fact.
- **F4** (The Last Giant): "It outwaited every giant lizard that ever lived." Hocknull's claim is narrower: the dragon is the "isolated long-term survivor" of the *giant varanids*. The brief said "Don't claim more than the source."
- **Contradiction** (The Follow and The Swim): back to back, the script says "up to ten kilometers in a day" (SDZWA) and then "up to about eleven kilometers a day" (Jessop, 7 mi). Each is sourced, but two different maximums on consecutive on-screen labels read as an error.

---

## 2. Opening (8/10) and Script Writer rules

- The opener is 22 words, the title promise plus Doug, and "The Ambush." lands at word 25. There is no greeting, channel name or subscribe ask. The twist marker "Here's the problem." is at word 101 (about 0:31), and the twist line follows by about word 160. Pass.
- Deductions: item 1 runs 233 words (the brief wanted 240-270, the bible 240-280). The first death lands at about 1:10, inside the brief's 1:20.

Writer rules (section 7) checked 1 to 14:
- **Rule 4 (violated, minor):** The Buffalo's frame runs 37 words, over the 35 limit ("The water buffalo is the biggest prey ... thought about it.").
- **Rule 9 (violated):** the average sentence is **13.6 words** (the floor is 14). **The Crowd has no sentence of 6 words or fewer.** My heuristic Flesch score is about 72.9, at or just above the 72 ceiling. The longest sentence is 29 words, which passes.
- **Rule 14 (violated):** "To put that in context," (The Fast) is a Paint Explainer verbal tic. Style bible 3.4 quotes it verbatim as his phrase, and it is 5 consecutive words.
- **Rule 7 (borderline, advisory):** The Teeth's kicker ("...flicked its tongue and quietly started counting.") works as a bridge into The Tongue. It is acceptable as a kicker on the clock device. Don't add more like it.
- Rules 1, 2, 3, 5, 6, 8, 10, 11, 12 and 13 pass. There are 12 items. The axis is declared, the clock is monotonic and the boss is the most extreme. Twist markers never repeat back to back, and the tic words are at 0. The outro is 24 words.

## 3. Structure and pacing (7/10)
- The time axis is clean and monotonic (0 S to 4,000,000 YR), and the six spoken headers are well placed. The boss is the most extreme item. The ending follows the bible: kicker, closing image, then an outro of 30 words or fewer. All running gags from the brief are present: the counter goes 178 to 186, "did not agree", "Doug is fine." twice, "hi friend?", the flowers, the cap in five places, field guide FRIEND? then NO, and the single 010 callback.
- Weaknesses: the back third sags. Two of the last four items are survivals, and The Virgin Birth has no danger at all. Items 9-11 run 228-238 words, against the bible's 260-300 for the "darkest material". The Tongue (216) and The Meal (215) are under the brief's 220 floor. At 15:05, the total sits right on the channel's 15-minute floor, so any trim in revision drops below it. **Do not cut; add words where fixes allow.**

## 4. Voice and humour (7/10)
- The deadpan holds and the persona is consistent. Lines that land: "The thermos was not technically food", "Doug was not required.", "full, not friendly", "Doug lasted nine hours, and the dragon has been doing this for about four million years."
- Repetition: consecutive Doug beats open the same way ("Doug ran for nearly an hour" in The Tongue, then "Doug ran for an hour" in The Follow). The concert grand piano is used twice (The Buffalo, The Last Giant), and the football comparison twice (The Follow, The Crowd).
- The Buffalo's kicker undercuts the thesis: "Doug could not outrun anything" implies a chase in a video about not chasing.
- Clunky sentence (The Buffalo, 28 words with a double "and"): "The dragon usually loses, and Fry's team say ... and Smithsonian magazine adds ...".

## 5. TTS
- "IUCN" (The Last Giant) and "DNA" (The Swim) are abbreviations. Two colons ("says it plainly:", "is the logic:") are tolerable. The pronunciation notes cover Rinca, Sungai, Megalania, Stegodon and Hocknull. Numbers are all spelled out.

## 6. Policy: PASS
- **Advertiser-friendly:** no blood, wounds or carcasses. "Go down", "lasts" and "survives" stay clinical, and the "blood loss" wording in the source is correctly left out. Cannibalism is one plain line, the attacks card is sober with no joke beside it, and the script is free of profanity.
- **Made for kids:** the tone is adult-coded and the virgin-birth item is clinical. One wording slip is covered in fix 10.
- **Inauthentic or repetitive content:** the episode has an original narrative engine (THE WAIT clock and the hunt sequence), not a list read-out.
- **Safety and title:** no safety advice, and the "can sprint" line is kept. The title promise is delivered. No spent 010 facts and no bacteria material appear.

---

## Required fixes (numbered)

1. **F1, The Follow.** "Fry's team, who study the dragon's bite, report that about seventy percent of bitten animals go down within minutes." Re-attribute the figures to field ecologist Tim Jessop, for example "Ecologist Tim Jessop, who has tracked these dragons in the field, found that about seventy percent...". Fix the facts.md line "(Fry, quoted in Smithsonian magazine)" to Jessop. The later "Fry's team say buffalo..." line is correct and stays.
2. **F2, The Fast.** Change "An animal that only needs a dozen meals a year can afford to wait for any one of them." to wording tied to the source, for example "An animal that only has to land one big meal a month can afford to wait for any one of them." Also change "A large dragon needs about a dozen big ones." to "A large dragon gets by on about a dozen big ones, plus the odd small snack." (or similar: not "needs", and not a total).
3. **F3, The Swim kicker.** Replace "Out here, every island comes with its own set, already waiting on the beach." with a line that doesn't generalise to every island, for example "The islands next door come with their own set, already waiting on the beach." Keep 8-25 words.
4. **F4, The Last Giant.** Change "It outwaited every giant lizard that ever lived." to "It outwaited every other giant monitor lizard." (or "every giant lizard it ever shared the world with"). Keep "The one thing it cannot wait out is the sea rising around its islands."
5. **Distance contradiction.** The Follow says "up to ten kilometers in a day" and The Swim says "up to about eleven kilometers a day". Use one figure in both places, and update the labels to match ("UP TO 10 KM A DAY" / "UP TO 11 KM A DAY"). Simplest: in The Swim, say "up to about ten kilometers a day ... roughly a quarter of a marathon" (10/42.2 is about 0.24) and keep 7 mi ≈ 11 km as the source note. Or cut the number from The Swim and keep "almost all of it happens inside the same valley."
6. **Rule 14.** In The Fast, replace "To put that in context," with our own wording, for example "For comparison," or "Compare that with you."
7. **Rule 9, The Crowd.** Add at least one sentence of 6 words or fewer, for example after "...than there are players on a football team.": "Nobody counts the guests." (or similar).
8. **Rule 9, average sentence length.** Raise the average from 13.6 to 14 or more by merging a few short non-punch pairs into mechanism sentences, without adding any sentence over 35 words. Candidates: in The Teeth, "In two thousand twenty-four ... at the edges. The cutting edges ..."; in The Swim, "Komodo dragons can swim ..." with "In two thousand eighteen ...". Keep the punch lines short. Aim for a Flesch score of 70 or below.
9. **Rule 4, The Buffalo frame.** Bring it to 35 words or fewer. For example, cut "which is not long by dragon standards," or merge it so the frame is 2 sentences totalling 35 words or fewer.
10. **Kid-appeal wording, The Nursery.** "A newborn weighs about eighty grams" becomes "A hatchling weighs about eighty grams". The brief allows only "hatchling" or "young dragon".
11. **TTS, The Last Giant.** "the IUCN moved the Komodo dragon" becomes "the International Union for Conservation of Nature moved the Komodo dragon". **The Swim:** "their DNA shows" becomes "their genes show".
12. **Repeated Doug-beat opener.** In The Follow, change "Doug ran for an hour, checked behind him, ..." so it doesn't echo The Tongue's "Doug ran for nearly an hour". For example: "Doug jogged on, checked behind him every few minutes, saw absolutely nothing, and sat down on a log for lunch."
13. **Repeated analogies.** The concert grand piano appears in The Buffalo and The Last Giant, and football in The Follow and The Crowd. Swap one of each for a new sourced everyday object (for Megalania, for example, a sourced small-car or motorbike weight; for the four-hour wait, for example, a sourced flight time or film length), with the source and arithmetic in facts.md.
14. **The Buffalo kicker.** "...but Doug could not outrun anything, and he did not weigh four hundred kilograms." "Outrun" implies a chase and cuts against the title. Rewrite to the wait thesis, for example "The buffalo was a long-term project. Doug was a short one, and he did not weigh four hundred kilograms."
15. **The Buffalo twist line (clarity).** Split "The dragon usually loses, and Fry's team say buffalo almost always escape the first attack, and Smithsonian magazine adds that dragons seldom succeed in killing animals this large." into two sentences.

### Advisory (not blocking)
- Make up the words lost in fixes 8 and 9 in The Tongue, The Meal and items 9-11. The video must stay at or above 2,900 words and 15:00.
- facts.md: change the iron-teeth and Columbus feeding-order entries from Search to Fetched (both confirmed). Add a park-authority or IUCN source for attack rarity if one exists.
- Smithsonian National Zoo does describe ritual combat as "wrestling upright", so the rearing-up drawing is sourced after all. Note it in facts.md.
