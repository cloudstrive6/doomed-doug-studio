# 022 Script review: draft 2 (screener, 2026-10-18)

VERDICT: FAIL

Facts, policy and TTS are now clean, and all 15 round-1 fixes landed. The draft fails on two new "must" violations
of the Script Writer rules: **rule 4** (Doug beats over 30 words) and **rule 10** (joke density in The Meal and The
Fast). Both come from the padding added to win back the words cut in round 1. The fix is four line trims and two cut
sentences, about 40 words in total. Length stays in range afterwards (about 3,075 words).

| Check | Result |
|---|---|
| 1. Facts | **PASS**: 0 errors. 12 claims re-verified (all changed lines), 2 advisories |
| 2. Opening | **8/10**: item name at word 25, "Here's the problem." at word 98 (about 0:30), no greeting |
| 2b. Writer rules violated | **4** (four Doug beats over 30 words), **10** (The Meal, The Fast). Round-1 violations of 4 (frame), 9 and 14 are fixed |
| 3. Structure and pacing | **8/10** (up from 7) |
| 4. Voice and humour | **7/10** |
| 5. TTS | **PASS**: IUCN and DNA are gone, numbers are spelled out, the two colons are tolerable |
| 6. Policy | **PASS** |
| 7. Length | **PASS**: 3,117 spoken words (brief 2,900-3,300), about 16:00 at 195 wpm |

My counter gives an average sentence of 14.5 words (rule floor 14), a longest sentence of 35 words (the limit is
35, and two sentences sit exactly on it: Ambush "In a short burst..." and Tongue "A Komodo dragon smells..."), and a
Flesch score of 71.9 (ceiling 72). All three pass with no margin, so **do not lengthen any sentence while fixing**.

---

## 1. Facts: changed claims (all fetched this round)

| Claim (draft 2) | Result |
|---|---|
| 70/20/10 now attributed to "Ecologist Tim Jessop, who has spent years tracking these dragons in the field" | **OK**. Smithsonian magazine (fetched) attributes the figures to Jessop, a University of Melbourne ecologist who has spent "more time studying dragons in the field than anyone since Auffenberg". F1 is fixed. |
| "The same Tim Jessop led a team ... ten sites ... two thousand eighteen" | **OK**. National Geographic (fetched) names Jessop (Deakin) as lead author. Search confirms that the Melbourne Jessop and the Deakin Jessop are the same person, who has run Komodo field monitoring since 2002. |
| "kills about one large animal a month", "only has to land one big meal a month", "gets by on about a dozen big ones, plus the odd small snack" | **OK**. SDZWA diet sheet (fetched): "about 1 large prey ungulate (deer or boar) per month", "supplemented with small prey, such as birds and rats". It is no longer framed as a need or a total. F2 is fixed. |
| Titanic, 194 minutes, less than 4 hours | **OK**. The Numbers (fetched): 194 min, and 240 - 194 = 46. See advisory A1 on "credits". |
| Megalania at least 575 kg, "heavier than a typical adult horse" | **OK**. PetMD (fetched): "The average adult horse weighs around 1,100 pounds, equal to about 500 kilograms." 575 is more than 500. The repeated piano is gone. |
| "The island next door came with its own set" | **OK**. It now refers to the one island Doug reaches, not to every island. NatGeo (fetched) lists wild populations on Flores, Komodo, Rinca, Padar and Gili Motang, so the neighbouring islands do have dragons. F3 is fixed. See advisory A2. |
| "up to about ten kilometers a day" in both The Follow and The Swim, with matching labels | **OK**. SDZWA gives 10 km. NatGeo/Jessop gives "up to seven miles per day" (11.3 km), which is consistent. The contradiction is resolved. |
| "their genes show the populations are becoming somewhat inbred" | **OK**. NatGeo: "evidence in the dragons' DNA that the animals are becoming somewhat inbred." |
| "It outwaited every other giant monitor lizard" | **OK**. This matches Hocknull 2009's "isolated long-term survivor" of the giant varanids. F4 is fixed. |
| International Union for Conservation of Nature, 2021, Vulnerable to Endangered | **OK** (NHM, verified in round 1). It is now spoken in full. |
| "eighty percent ... a meal that weighs almost as much as you do" | **OK** as arithmetic. See fix 6, which cuts this line for joke density anyway. |
| "a hatchling weighs about eighty grams" | **OK** (SDZWA). The wording now follows the brief. |

### Advisories (not blocking)
- **A1 (Follow).** "Four hours is longer than the whole of the film Titanic, with time left over for the credits and a snack." The 194 minutes already include the credits. Change to "with time left over for a snack", which keeps the joke and drops the nitpick.
- **A2 (facts.md).** The narrator-framing note says "islands such as Padar have none", but the NatGeo source it cites lists Padar as a wild population. The Padar population is generally reported as lost in the 1970s or 1980s. This line is not spoken, so either cite a source for Padar or delete the parenthetical.

## 2. Opening (8/10) and Script Writer rules

- The opener is unchanged and strong: "The Ambush." lands at word 25, and the twist marker arrives at word 98. Item 1 is now 239 words, against a brief target of 240-270.
- **Rule 4 (violated): Doug beats must be 15-30 words.** The padding pushed four of them over:
  - Ambush, **36** words including the gag line ("Doug studied the field guide carefully on the way in ... which is exactly where the dragon was not. Doug did not agree to this.")
  - Tongue, **37** ("Doug ran for nearly an hour, found a big rock and hid behind it, convinced that ... He held his breath, and he did not make a single sound.")
  - Buffalo, **34** ("Doug stood beside the buffalo for several days to show solidarity, holding his sign up the whole time so that nobody could miss the message. The dragon studied the two of them very carefully.")
  - Nursery, **34** ("Doug climbed the tree to escape the adult, which was the one sensible thing he did all episode. The young dragon was already up there, and it had been eating nothing but insects for months.")
- **Rule 10 (violated): at most one joke line per 60 seconds.**
  - The Meal (about 76 s) now has four joke lines: "and then asking whether there is dessert", the picnic peace treaty, "The picnic is not.", and "The thermos was not technically food".
  - The Fast (about 82 s) has four: "plus whatever happens near the fridge at midnight", "plus the odd small snack", the wave, and the narrator's disappointment.
  - Both new lines are padding. The originals were the better jokes.
- Rules 1, 2, 3, 5, 6, 7, 8, 9, 11, 12, 13 and 14 pass:
  - Every item has a sentence of 6 words or fewer.
  - "To put that in context" is gone, and "Compare that with you." is our own wording.
  - The tic words appear 1 time in total, and twist markers never repeat back to back.
  - The Buffalo frame is now 28 words.

## 3. Structure and pacing (8/10)

- The clock is monotonic, the headers are unchanged, and the boss is the most extreme item. The ending follows the bible, and the outro is 24 words. All running gags are still present.
- Every item is now inside the brief's 220-270 range (231-266), and the boss is 369 words. This fixes the round-1 sag, where items ran under the floor.
- The back third still has two survivals in its last four items, but it holds at this length.

## 4. Voice and humour (7/10)

- Round-1 repeats are fixed: the "ran for an hour" echo, the second piano, and the second football analogy. The Buffalo kicker ("The buffalo was a long-term project. Doug was a short one, ...") is now the best kicker in the script.
- Good additions: "the whole island is something to taste", "Nobody counts the guests.", "which is exactly where the dragon was not", "the one sensible thing he did all episode".
- Weak additions:
  - "Dessert" and "fridge at midnight" read as filler (see fix 6).
  - The Virgin Birth now ends on "He left the flowers by the nest anyway, which nobody asked for either." This buries the stronger, on-theme line "nobody here was waiting for him, and nobody ever had been." See fix 7.

## 5. TTS: PASS
There are no abbreviations, symbols or parentheses in the spoken text, and every number is spelled out.

## 6. Policy: PASS
- **Advertiser-friendly:** still clinical, with no gore. The new lines add no injury detail, and the script has no profanity.
- **Made for kids:** the tone is adult-coded, and "newborn" is now "hatchling".
- **Original narrative:** yes. The WAIT clock and the hunt sequence give the episode its own story.
- **Safety and title:** no safety advice, and the title promise is kept.

---

## Required fixes (numbered)

1. **Rule 4, Ambush Doug beat.** Bring it to 30 words or fewer including "Doug did not agree to this." For example: "Doug studied the field guide and kept a close eye on the trail ahead, which is exactly where the dragon was not. Doug did not agree to this." (27 words)
2. **Rule 4, Tongue Doug beat.** Bring it to 30 words or fewer. Keep either the "convinced..." clause or "and he did not make a single sound", not both. For example: "Doug ran for nearly an hour and hid behind a big rock, convinced that what cannot see him cannot find him. He held his breath." (24 words)
3. **Rule 4, Buffalo Doug beat.** For example: "Doug stood beside the buffalo for several days, holding up his sign in solidarity. The dragon studied the two of them very carefully." (23 words)
4. **Rule 4, Nursery Doug beat.** For example: "Doug climbed the tree to escape the adult, the one sensible thing he did all episode. The young dragon was already up there, and it was tired of insects." (29 words). Any version of 30 words or fewer is acceptable.
5. **Rule 10, The Fast.** Cut ", plus whatever happens near the fridge at midnight". Keep "plus the odd small snack", which carries the sourced qualifier from fix F2.
6. **Rule 10, The Meal.** Cut "For a person, that would mean finishing a meal that weighs almost as much as you do, and then asking whether there is dessert." The item keeps its water-bottle analogy for rule 8.
7. **Virgin Birth kicker.** Cut "He left the flowers by the nest anyway, which nobody asked for either." The kicker reverts to "Doug survived, but only in the technical sense, because nobody here was waiting for him, and nobody ever had been." That sentence is 20 words, inside the 8-25 kicker range.

After these fixes, re-check the average sentence length (14 or more) and the Flesch score (72 or below). The cuts
remove mostly long sentences, which can tip both the wrong way. If they do, merge one short non-punch pair, for
example in The Fast: "The rest of the time, it digests, it basks in the sun, and it waits." Also apply advisories A1 and A2.
Round 3 only needs a re-screen of these lines.

---

## Round history
- **Round 1, draft 1: FAIL.** The script had 3 fact errors: the 70/20/10 figures attributed to Fry instead of Jessop, "a dozen meals a year" as a need, and "every island". It also had 1 over-claim ("every giant lizard") and contradicting 10 km and 11 km labels. Writer rules 4, 9 and 14 were violated, and IUCN and DNA were TTS problems. Hook 8, structure 7, voice 7. There were 15 fixes, and all were applied in draft 2.
- **Round 2, draft 2: FAIL.** Facts, TTS and policy are clean. Hook 8, structure 8, voice 7. New violations of rules 4 and 10 come from the padding. This round has 7 line-edit fixes.
