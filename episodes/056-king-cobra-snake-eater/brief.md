# Episode 056: Why King Cobras Hunt the Deadliest Snakes in Asia (brief)

Creative director, 2026-11-23. Backlog idea **#124** (7.7 in `topics`, `animals`). It was a provisional pick in CD decision 2 of
`data/insights/2026-11-22.md`, and this brief confirms it after the brief-day re-check below.
Before writing it I read `config/channel.yaml`, the style bible (1.4 title rules, 3.2, the 2026-10-27 retention update, writer rules), the series
bible (Openings, Outro, running gags, costume gag, episode log to 055), `data/ideas.md`, the 11-22 memo, `data/competitors/2026-11-23.json`,
`data/signals/cache.json` ("king cobra"), the 045 black mamba metadata and script (to avoid repeats), and the 055 brief.
The stage stays `idea` until draft 1.

## 0. Why this idea, and why now
- **Lane rule (D4).** In `python -m studio topics` (11-23), #98 pilot whales is first at 8.2, but it is held for orca spacing: it has to be at
  least 3 slots after 055, so 058 or later (memo §4.3, CD decision 2). #99 Greenland shark and #124 king cobra are tied at 7.7. The last two
  episodes are 054 `animals` and 055 `ocean`, so the same-playlist default (#133 botfly) does not apply.
- **Brief-day re-check (CD decision 2):** I searched `competitors/2026-11-23.json` for a live Greenland shark engine and found none. The
  only ≥3,000 vph same-animal engine in the set is OctoLab's sperm whale (4,549 vph), and 055 already uses it. #99 still has nothing above
  1,547 vph, so there is no reason to swap and **#124 stands**. This is a no-engine episode (the live-engine experiment does not apply), and
  056 gives the rough no-engine comparison for that experiment.
- **Formula engine (rule a, the honest version):** there is no 1M+ king cobra explainer. The formula engine is OctoLab's single-animal "Why
  [Animal] Is …" series: sperm whale 2.27M (4,549 vph today), polar bear 3.4M, walrus 2.6M. The demand comes from search: "king cobra" scores
  9, with suggestions "king cobra vs black mamba" and "king cobra vs python". The top results are live rescue clips (6.8M and 8.0M, about 22K
  vph), and "why the king cobra eats other snakes" has only 2 copies. Our own 045 black mamba was the most-viewed long video in the week of
  11-13. That breaks my usual 1M+ rule, and CD decision 2 allowed it on these grounds.
- **Not a repeat of 045.** 045 covered The Speed, The Home, The Snake Eagle, The Head Lift, The Gape and the Hood, The Second Strike, The
  Dendrotoxin, The Painkiller and The Long Ride. 045's axis was the mamba's warnings. **This episode's axis is what the king cobra eats.**
  - Banned here: speed, the hood display as an item, the head lift/rear-up as an item, snake eagles, the second strike, dendrotoxins,
    mambalgins, antivenom distance and anything about a human bite.
  - Male combat wrestling had one line in 045 (script l.157), so it does not become an item here. One line at most in item 9, if any.
  - **One 045 callback, at most:** "Doug has met a black mamba. This one eats things like it." It goes in item 4 and is only valid if the
    writer sources king cobras eating other elapids. Item 4 sources that anyway.

## 1. Working title and the format it borrows
- **Working title: "Why King Cobras Hunt the Deadliest Snakes in Asia"** (50 characters).
  - The animal is in the first 2 words (v2 rubric +), and the dread adjective is "Deadliest" (style bible 1.4).
  - It is honest if items 1 and 4 hold up: the common krait and the Indian/spectacled cobra are 2 of India's "Big Four", the snakes behind most
    of India's snakebite deaths, and both are recorded as king cobra prey.
  - It drops the backlog's "Only Hunts Other Snakes". CD decision 4 scores "only eats"-type negation/limitation titles as a minus
    (041/042/044 sat at ≤1%).
- **Leads for the titler** (10 candidates go in `title_candidates.json`; the D4 gate is a lint only, and if the top 3 are within 4 raw points
  the titler and CD pick by hand):
  - "King Cobras Eat the Deadliest Snakes in Asia, Even Each Other" (62; only if item 9's cannibalism is sourced)
  - "Every Snake the King Cobra Eats, From Rat Snakes to Other King Cobras" (68; too long, so trim it, but the scope device is good)
  - "Why the Deadliest Snakes in Asia Are Afraid of the King Cobra" (**only if** a source reports prey snakes fleeing or avoiding it.
    Otherwise it is banned as a misleading claim)
- **Banned in the title:** "Scariest Snake" (045's "Africa's Scariest Snake" formula), "Only", "Won't", "Doesn't Need", "Think Twice",
  "vs Black Mamba" (045 never matched them up, so it would be a promise we don't keep), "Kills an Elephant" (see Risks), and any copy of
  the rescue-clip wording. "Doug" is optional (CD decision 5).
- **Thumbnail (it is the opening image; hero close-up archetype C plus a small queue):**
  - A huge reared king cobra (olive/khaki with pale bands, **not** 045's grey mamba and not the hooded Naja `cobra_hooded`), with the tail
    end of a black-and-yellow banded krait hanging from its mouth. Cartoon, no blood.
  - Beside it, a short queue of snakes waiting, with Doug last in a **snake costume**, cap on top, holding a deli ticket.
  - Text ≤3 words that are not in the title: "NEXT IN LINE" or "NOW SERVING 9". Never "DEADLIEST", "KING" or "COBRA".

## 2. Axis and items
**Declared axis: how dangerous the snake on the menu is.** It runs from harmless rat snakes, through venomous elapids (kraits, cobras) and
heavyweight pythons, to its own kind. The boss is another king cobra. This is a severity axis, **not 045's warnings axis**.
Item 1 is a cold open from the venomous band, the strongest hook (Openings rule). The axis then starts from the bottom.

**Spoken bands (short headers):**

| Header | Items |
|---|---|
| (no header: cold open) | 1 |
| **"Harmless."** | 2–3 (allowed after item 1, never before) |
| **"Venomous."** | 4–5 |
| **"Bigger."** | 6–7 |
| **"Family."** | 8–9 |

- **Episode-only device: NOW SERVING** (staging only, never read aloud; the art director approves it). A deli-counter ticket display beside
  the death counter. It ticks up one number per item. Doug holds a paper ticket with "9" on it the whole episode, and his number is called
  at the boss. It is adult-coded queue bureaucracy, not the MENU (021), the PLATE (048), SHARKS GONE (051), HEAD COUNT (054) or THE RING
  (055). No field guide.
- **Costume gag (the episode's engine):** the king cobra hunts snakes, which is exactly why Doug is dressed as one. Say the rule line once,
  at item 1, and vary it afterwards. Costumes: krait (item 1), rat snake (2, 3), cobra (4), python (6), **king cobra** (9, the boss). Doug
  wears costumes in no more than 6 items. They are new gear, so the art director signs off on all of them: **one base snake-costume drawing
  with palette/band variants** to keep the illustrator's load down. The cap always sits on top. The costumes read as zipped tube suits with
  Doug's face showing, never as cute mascots.

**Words:** 215–255 per item, 9 items, 1,950–2,350 in total. If the draft runs long, cut item 7 first, then item 5. Never cut items 1, 4, 6 or 9.

Every number below is a lead. The writer verifies each one in `facts.md`. **If a fact can't be sourced, cut it; don't hedge it.**

| # | Item (name sentence) | Facts to research (2–4) | Everyday scale analogy | Doug beat |
|---|---|---|---|---|
| 1 | **The Krait.** (cold open; one of the three strongest) | The common krait (*Bungarus caeruleus*) is one of India's "Big Four". Krait bites often happen at night, to people asleep on the floor, and the bite can be nearly painless (Million Death Study: Mohapatra et al. 2011, *PLoS NTD*, or WHO; state it at population level, with no symptoms and no treatment). Kraits themselves eat other snakes. **Twist (by 0:45):** king cobras eat kraits (find a diet record: Marshall et al. telemetry in Thailand, or a dietary review such as Jones et al.; if only *B. fasciatus*/*B. candidus* is recorded, name the krait that is). The thing a whole country fears at night is a menu item. The genus name *Ophiophagus* means "snake eater". | A night-time burglar so feared that people sleep off the floor, and he's somebody's takeaway. | Doug, in a **krait costume**, is the most feared thing in the room for about four seconds. Rule line: "The king cobra hunts snakes, which is exactly why Doug is dressed as one." NOW SERVING: 1. **Death 409**, cut away. |
| 2 | **The Scent Trail.** ("Harmless.") | King cobras find prey by following other snakes' chemical trails with tongue flicks (source chemosensory trailing in *Ophiophagus*, or say "by smell" with a general snake chemoreception source). Common prey includes rat snakes (*Ptyas*), per a diet record. They range widely: telemetry home ranges in the km² (Marshall et al. 2019 or similar, exact figure). | A bloodhound that only hunts other bloodhounds. | Doug, in the **rat snake costume**, crosses a rice paddy and leaves a dotted trail. He hides up a tree, and the dotted line goes up the trunk after him… and the cobra finds a real rat snake first. **Survival** ("Doug is fine. Someone else wasn't."). |
| 3 | **The Swallow.** ("Harmless.") | It swallows prey head first. Snakes can "walk" their jaws over prey (the left and right jaws move independently; source a general snake feeding paper). A king cobra can swallow a snake close to its own length (find a sourced length ratio or a documented case, or cut the number). The longest venomous snake: typically 3–4 m, the record about 5.5–5.85 m (sourced, give the source's figure). | Eating a garden hose longer than you are, without using your hands. | Doug, still in the rat snake costume, is the hose. NOW SERVING: 3. **Death 410**, played flat (the costume's tail end goes in last and the cap stays outside). |
| 4 | **The Cobra.** ("Venomous.") | Spectacled/monocled cobras (*Naja*) are also Big Four or medically significant, and they are recorded as king cobra prey (source). The king cobra is **not a true cobra**: it has its own genus, *Ophiophagus*, separate from *Naja* (source). Its threat sound is a low "growl" (Young 1991, the low-frequency hiss; source it). **No hood item** (045). One line on the hood at most. | A shark that hunts other sharks, and isn't even technically a shark. | Doug, in a **cobra costume** with a cardboard hood, tries to bluff with his own hiss. The growl wins. **Death 411**, played flat. 045 callback (one line, sourced). |
| 5 | **The Dose.** ("Venomous.") | The venom isn't the most toxic drop for drop. What makes it dangerous is the **volume** of a single bite (sourced yield in mg or ml, e.g. from a venom-yield table or the Clinical Toxinology Resources database). Its main toxins are neurotoxins (one plain line, no mechanism tour, nothing like the 045 dendrotoxin). Prey snakes are subdued and then swallowed (source). | Not the strongest coffee in the world, but a bucket of it. | Doug, out of costume, holding a measuring jug "for science". The cobra ignores him because he isn't a snake. **Survival** ("Doug is fine. He has never been more insulted."). |
| 6 | **The Python.** ("Bigger.") | Pythons (*Python bivittatus* or reticulated) are recorded as king cobra prey (source the record). There are reports where both snakes died: the cobra was unable to swallow it, or the python constricted it (find a sourced, documented case, otherwise cut that part). The size comparison is the stake. **Twist:** sometimes the dinner fights back, and nobody wins. | Trying to eat a sofa that is also hugging you. | Doug, in a **python costume**, tries the hug from his side. **Death 412**, cut away (two snakes knotted, cap on top, the narrator declines to say who won). |
| 7 | **The Fast.** ("Bigger.") Cut first if long. | After a large meal a king cobra can go a long time without eating (sourced figure, weeks or months; cut it if only zoo anecdotes exist). Snakes' low metabolism (one general source). Ties back to item 6: one big snake lasts a long time. | One Christmas dinner that lasts until Easter. | Doug, waiting at the counter with his ticket while NOW SERVING doesn't move for a very long time; **cartoon cobwebs** build up on Doug and the cap (never a skeleton). **Death 413**, played flat ("Doug died waiting. The cobra did not."). |
| 8 | **The Nest.** ("Family.") | It is the only snake known to build a nest: the female gathers leaf litter into a mound with her body (source; Whitaker & Captain, *Snakes of India*, or a herpetology paper). She guards it for weeks (sourced duration) with roughly 20–40 eggs (sourced). She leaves before the eggs hatch (source). One explanation is that it stops her eating her own young; use it **only** if a source says so, attributed ("some herpetologists think…"). Hatchlings are venomous from birth and hunt snakes from the start (source). | A parent who builds a nursery, guards it for two months, then moves out the night before the baby arrives. | Doug "helps" rake leaves. The mother rears up and Doug freezes. She is guarding, not hunting, and he isn't a snake today. **Survival**, and the narrator is **quietly disappointed** (the only time in the episode). Re-hook: "She leaves before they hatch. There's a reason the babies should be glad about that." |
| 9 | **The Other King.** ("Family.", the boss; about 1,900 words in) | Cannibalism: king cobras are recorded eating other king cobras (find a documented field record; Thai telemetry or a natural-history note in *Herpetological Bulletin* or *Herpetological Review*; quote the source's details: sizes, sex, place). **Kicker fact:** in 2024 the "king cobra" was split into four species (Das et al. 2024, *European Journal of Taxonomy*), so there are four kings, and each one will eat the others' relatives (wording must match the paper; keep it light, never "the others" as a fact unless sourced). Status: Vulnerable (IUCN), one line. | Being at the deli and realising the person behind you in the queue has ordered *you*. | **The payoff promised in the opening.** Doug, in a **king cobra costume** (the cap on the hood), holding ticket 9. NOW SERVING flips to 9. A bigger king cobra rears behind him. **Death 414**, cut to black, played flat. |

**Expected deaths: 6** (counter 408 to 414). Survivals at items 2, 5 and 8. The writer may turn one more death into a survival, but not the boss.

**Closing (after the boss kicker, `animals` standard):** the empty deli counter, NOW SERVING blinking "10". The ticket "9" and the cap lie on
the leaf litter of the empty nest from item 8. One fresh dry kicker, for example "the cap is the one thing in the forest that isn't on the
menu". It must not be a 045, 051, 054 or 055 line.

## 3. The opening (series bible "Openings", style bible 3.2 and the retention update)
- **No hook section.** The thumbnail image (the reared king cobra, the krait tail, the queue, Doug last) is the first frame.
- **First sentence (the cold-open fact, sourced):** "Two of the snakes that kill the most people in India are on the king cobra's menu."
  Source: the Big Four (Mohapatra et al. 2011 / WHO) plus the item 1 and item 4 prey records. If either prey record fails, rewrite the line
  to what is sourced, and the title changes with it. Doug's line comes second.
- **Payoff promise by 0:10:** "By the end of this, Doug is dressed as a king cobra, standing in front of the one thing that eats king cobras."
  The writer may tighten it but must keep it specific.
- **"The Krait." by word 35.** Its twist (the king cobra eats it) lands by 0:45, about 145 words.

## 4. Running gags
- **Death counter**, starting at **408** (after 055). Deaths are played flat.
- **"Doug did not agree to this."** once, at item 4 (he agreed to the costume, not to the hiss-off).
- **"Doug is fine."** at items 2, 5 and 8, each written fresh. No "Eventually.", "Indoors.", "Doug floats." or "Doug is in the middle.".
- **Narrator quietly disappointed** at item 8 only.
- **Costume gag:** snake costumes, the rule line once (item 1). The **king cobra costume** at the boss is the episode's thumbnail-adjacent
  image.
- **Cap survives:** outside the swallowed costume, knotted pythons, cobwebs, on the leaf mound, and in the closing.
- **"hi friend?"** once at most (item 2, to the real rat snake).
- **Callbacks:** 045 once (item 4, sourced). Nothing else.
- **Outro (rule from 048):** after the closing kicker, ≤30 words: the death counter plus one fresh deadpan subscribe line tied to the
  counter (the deli-ticket idea fits, e.g. a number that only goes up). It must not be one of 048–055's lines or the bible's example, and
  there's no comment prompt.
- **Do not reuse:** the suitcase, the time machine, the field guide, THE MENU, THE RING, the 045 snake eagle or mamba drawings for the king
  cobra (new drawing required, distinct silhouette: longer, olive with pale chevron bands, narrow hood), and any 045 fact.

## 5. Playlist
`animals` (Doug vs. Animals). The previous two are 054 `animals` and 055 `ocean`, so this doesn't make two `animals` episodes in a row
right after 055. 057 should not be `animals`: next in line are #99 Greenland shark (`ocean`) or the parasites pick #133 botfly. #98 pilot
whales is allowed from 058.

## 6. Length and payoff
- **Target 10–12 min**, about **1,950–2,350 words** at ~195 wpm (standing rule), 9 items, 215–255 words each.
- **Payoff promise line (opening):** "By the end of this, Doug is dressed as a king cobra, standing in front of the one thing that eats king
  cobras."

## 7. Risks
- **Gore.** No envenomation symptoms, no bite wounds, no human victim imagery. Prey is "swallowed", and there is no partially digested or
  regurgitated prey. Deaths are X eyes or cut to black. The knotted python and cobra (item 6) are drawn as a cartoon tangle.
- **Medical/safety advice (high: the Big Four).** No first aid, no antivenom guidance, no "what to do if bitten", no symptom lists. The
  Big Four appear only as a sourced population statistic. Krait night bites are one sober line, with no victim and no detail.
- **Kid appeal (medium: costumes, the nest, hatchlings).** The costumes are deadpan tube suits, not plush. The hatchlings are not cute (no
  big eyes) and there's no "mommy snake" tone. The queue and deli ticket are adult bureaucracy humour. The made-for-kids setting stays No.
- **Misleading packaging.** No "vs black mamba". No "kills an elephant": it is widely repeated but needs a primary source for an actual
  elephant death, and if there isn't one, the claim stays out of the script and the title (an "enough venom to kill an elephant" yield
  comparison is allowed only if sourced, as a dose comparison). No "only eats snakes": they also take monitor lizards and other prey
  sometimes, so say "mostly snakes" with the sourced share. No claim that prey snakes fear it unless sourced.
- **Taxonomy trap.** Since Das et al. 2024 "the king cobra" is four species. Facts from Thailand or India may belong to different species
  now. The writer words it as "king cobras" and names the population where it matters.
- **Overclaims to avoid:** venom "most potent" (false, volume is the point); exact max length without a named record; fasting "for a
  year" without a source; cannibalism framed as routine (say "has been recorded"); the egg-eating motive for leaving the nest unless
  attributed.
- **Strong sources needed:** Mohapatra et al. 2011 (*PLoS NTD*, Million Death Study) and WHO for the Big Four; a primary diet record for kraits,
  *Naja*, pythons and conspecifics (Marshall et al. Thai telemetry papers; *Herpetological Bulletin*/*Herpetological Review* notes); Young 1991
  for the growl; Das et al. 2024 (*Eur. J. Taxonomy*) for the split; Whitaker & Captain or a peer-reviewed source for nesting; IUCN for status;
  a venom-yield source (Clinical Toxinology Resources or a toxicology paper). Never a rescue-clip channel, a listicle or a competitor video
  for a number.
