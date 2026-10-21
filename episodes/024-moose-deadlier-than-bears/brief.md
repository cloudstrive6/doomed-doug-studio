# Episode 024: Why Moose Are Deadlier to Doug Than Any Bear (brief)

Creative director, 2026-10-21. Backlog idea #52 (score **7.2**, the top eligible backlog idea; it was named the ep 024 `animals`
candidate in the 10-18 memo and my 10-18 decisions). The stage stays `idea` until draft 1.

## 0. Why this idea, and why now
- **Ranking:** #47 (8.2) is 022 and #42 (7.2) is 023. The highest backlog rows left are #52 moose (7.2), #45 bull sharks (7.1), #33 every era
  (6.9), #38 natural disasters (6.8) and #40 rabies (6.7).
  - #45 sits on 021's "Why most X…, but Y…" orca frame and is an ocean predator again. It is too close to 021.
  - #33 is crowded (10 copies) and comes straight after 023's era axis. It is too close to 023.
  - #38 is `places` (Own 4, the weakest playlist), and 020 was `places`. #40 has a weak engine (Interest 3, Eng 6).
  - #52 has the strongest engine of the eligible ideas: OctoLab's single-animal "X Are Terrifying… Here's Why" (walrus 2.54M, **41.9x**;
    polar bear 2.87M, 47.4x). Demand is 10 and clean ("moose attack": man/car/bear/Alaska, no kids' content), and there are **0** copies
    of the format phrase.
- **Housekeeping:** row #52 disappeared from `data/ideas.md` in the 022 brief commit (45e0493). I restored it from the 10-18 growth commit
  (0658b6b) and marked it in-production.
- **Not done by us (rule b):** moose appeared once in 011 (one wolf-pack line) and once in 021 (prey item: weight and swimming between
  islands). We have never done the moose as a danger to people.
- **Lane (rule c):** a large wild animal that injures people. Nature horror, with real wildlife-agency data.
- **Back-to-back checks against 020-023:**
  - Playlist: 020 `places`, 021 and 022 `animals`, 023 `prehistoric`. 024 is `animals`, with 023 between it and 022 (the plan from 10-18).
  - Title formula: 021 "Why Orcas Kill Everything… Except Doug" (T9), 022 "How the Komodo Dragon Kills Doug…" (T2 shape),
    023 "Would a Hippo Survive…?" (T11). This title is a "Why X Is Deadlier Than Y" comparison (T9 family, the "X Is Terrifying"
    single-animal engine). It opens with "Why" like 021, but 021 publishes today and 024 comes three slots later, and the comparison
    is a different frame from 021's exception. **No T1 wording** (2 strikes, 3rd pending) and **no T2 "How Every…" wording** (dropped).
  - Axis: 020 depth, 021 prey size, 022 time, 023 eras backwards. **024 is a comparison-severity axis against bears** (see 2). We have
    not used that axis before.
  - Biome: boreal forest, snow, lakes and roads. None of 020-023 is set there.
  - **Variety note for the next pick:** 021-024 are four single-animal episodes in a row (orca, Komodo, hippo, moose). After 024, the next
    episode should **not** be a single-animal deep dive. Lead candidates are a list episode in `parasites` (#40 rabies, #43 viruses) or
    the #20 prehistoric compilation.

### Overlaps resolved (spent material, don't reuse)
- **021 moose:** the ADF&G weight (542-725 kg), swimming between islands, sodium in water plants, orcas killing moose (Icy Strait 1993).
  None of these comes back. Use height for size, not weight. Item 2 is about diving depth, not about swimming between islands or why.
- **011:** "wolves hunt in packs and bring down moose" was one line. Item 10 is about the moose winning, and the pack line is not repeated.
- **018 item names:** "The Kick", "The Swim" and "The Road" are cassowary chapter names. Here they are **The Hooves**, **The Dive** and
  **The Highway**.
- **013:** no canoe (Doug uses a paddleboard), no "closer you get" distance meter.
- **021:** no costume gag (Doug wore a moose costume in 021). Item 8's cardboard antlers are a hat, not a costume, and Doug never pretends
  to be a moose.

## 1. Working title and proven outlier
- **Working title:** **Why Moose Are Deadlier to Doug Than Any Bear** (44 characters, 9 words). "Deadlier" is the dread word, "Than Any
  Bear" is the scope device, and "to Doug" keeps the claim honest (see Risks: over-claiming).
- **Borrowed from:** OctoLab "Walruses Are Terrifying... Here's Why" 2.54M (41.9x) and "Why Polar Bears Are The Weirdest Apex Predator
  on Earth" 2.87M (47.4x). Supporting evidence: Rocky Mountain PBS "Colorado's Most Dangerous Animal" (moose), 247K (signals), and the
  autocomplete "moose attacks bear". We borrow the single-familiar-animal-as-horror frame. We don't borrow their wording ("Terrifying…
  Here's Why", "Weirdest"), their animal or their structure.
- **Delivers what it promises:** every item compares the moose with a bear on a scoreboard, Doug dies to moose 8 times and to bears 0
  times, and the boss is the statistic that actually makes the moose deadlier to people.
- **Alternates for the titler (leads; 5 are required):**
  - "Why the Moose Hurts More People Than Any Bear" (needs a death verb or dread word added, or keep only as an A/B variant)
  - "The Deadliest Animal in Alaska Isn't the Bear" (only if the facts back "deadliest"; see Risks)
  - "Why Moose Are Scarier Than Bears, and Doug Didn't Listen"
  - "Every Reason a Moose Is Deadlier Than a Bear" (T8 shape; 018 used "Every Reason", so this is a fallback only)
  - **Banned:** "Terrifying… Here's Why" (OctoLab's wording), "Weirdest", "What … Would Be Like" (T1), "How Every…" (T2), ALL CAPS,
    "?!", any cartoon-moose or children's-book reference, "for kids".

## 2. Escalation axis and items
**Axis: severity, measured against a bear.** Three bands. First the things a moose does that a bear also does, then the things a moose
does that a bear doesn't, then the things that make a moose worse than a bear for people. Most extreme last.

**Episode-only device, proposed: the BEAR / MOOSE scoreboard.** A crude two-column chalkboard ("BEAR | MOOSE") beside the death counter.
After each item the narrator's hand adds a tick to whichever animal is the bigger danger to people on that trait. In band 1 both columns
get a tick (it's a tie). In bands 2 and 3 only the moose column does. It is monotonic and ends at **BEAR 5, MOOSE 11**. Every tick is
the narrator's judgement from sourced facts, never a study's result. The art director may cut it if the screen is busy (the death counter
always stays). `chalkboard.json` exists as a base.

**Field guide** (`animals` standard prop): a MOOSE page. FRIEND? box empty at item 1, "NO" stamped at the first death, "MAYBE" pencilled at
the survivals and erased again. Closing: see item 11.

**Bears in this episode:** a grizzly (`grizzly_bear.json`) appears as a reference figure in band 1 (beside the moose, for the comparison)
and in the thumbnail. **A bear never kills Doug and never attacks anything on screen.**

Spoken section headers (two-word style):
- **"Like bears."** (opener, items 1-5)
- **"Unlike bears."** (before item 6, about 45%)
- **"Worse than bears."** (before item 10, about 80%)

Every number below is a lead. The writer verifies each one in facts.md. If a fact fails, cut it; don't hedge it.

### Like bears.

**1. The Deer** (hook item; death 196; scoreboard BEAR 1, MOOSE 1)
- Facts:
  - The moose is the largest living member of the deer family (ADF&G, Smithsonian or NPS; verify).
  - Bulls stand about 1.8-2.1 m at the shoulder (ADF&G; verify the range and the units). Use height, not 021's weight.
  - **The thesis fact:** Alaska's Department of Fish and Game says moose injure more people in Alaska each year than bears do (find
    ADF&G's exact wording and the scope: Alaska, injuries, "each year"). If the wording is weaker, use the exact wording; don't upgrade it.
- Analogy idea: the shoulder against a standard interior door (about 2 m; source a door height). Doug's cap comes up to its chest.
- Twist (must land by 0:45): **it's a deer, and in Alaska it puts more people in hospital than the bears do.**
- Doug beat: Doug walks up with an apple, field guide open at MOOSE, FRIEND? box empty ("hi friend?"). The narrator points out the ears
  going back and the hair on the hump standing up (behaviour, not advice; see Risks). Doug keeps holding out the apple. Death 196 (a
  cartoon trample, cut to black on the first hoof). Cap on the apple. Field guide: "NO".

**2. The Dive** (Doug SURVIVES; "Doug is fine."; scoreboard BEAR 2, MOOSE 2)
- Facts:
  - Moose feed on underwater plants and can dive several metres to reach them (ADF&G or NPS; verify a depth such as "up to about
    6 m" and a time underwater; cut either if unsourced).
  - They can close their nostrils underwater (verify the anatomy source).
  - Bears swim too (one line, source a grizzly or brown bear swimming fact).
  - **Not** the 021 material (no swimming between islands, no sodium).
- Analogy idea: the dive depth against a sourced everyday height (a two-storey house).
- Twist: **the lake isn't where you escape from a moose. It's where the moose eats.**
- Doug beat: Doug paddles a paddleboard out to the middle of a lake, very pleased with his escape. The water bulges under him and a moose
  head comes up wearing pondweed. It chews and ignores him. "Doug is fine." Field guide: "MAYBE".

**3. The Calf** (death 197; scoreboard BEAR 3, MOOSE 3)
- Facts:
  - Cows with young calves are among the most dangerous moose, in late spring and early summer (ADF&G or NPS; verify).
  - Calves are born in May-June, and twins are common (ADF&G; verify).
  - Bears are major predators of moose calves in parts of Alaska (an ADF&G or peer-reviewed calf-mortality study, e.g. Ballard or Boertje;
    verify the share and the region, or say "a large share" with the source's own wording).
- Analogy idea: a newborn calf's weight against a sourced everyday weight (a large dog).
- Twist: **the cow is that aggressive because a bear really is coming for the calf, and Doug is standing where the bear would.**
- Doug beat: Doug finds a calf alone in the willows ("hi friend?"). The narrator explains that a calf that looks alone usually isn't.
  Death 197. Cap in the willows. The grizzly reference figure watches from far away and does nothing.

**4. The Apples** (Doug SURVIVES; "Doug is fine."; narrator quietly disappointed; scoreboard BEAR 4, MOOSE 4)
- Facts:
  - In 2011 a moose was found stuck in an apple tree in Gothenburg, Sweden, reported as drunk on fermented apples (BBC or Swedish press;
    verify the year, the place and how it got down).
  - Whether moose really get drunk on fermented fruit is debated. Use a source that discusses the evidence, or say "reported as" and
    "nobody tested it".
  - Bears also eat fermented fruit (verify a source, or cut the bear line and give the tie tick on "both raid orchards", sourced).
- Analogy idea: none needed; the image does the work.
- Twist: **the most dangerous animal in the orchard is up the tree, and it can't get down.**
- Doug beat: Doug walks into a Swedish garden under an apple tree. Above him: a moose in the branches. Doug moves away very slowly.
  "Doug is fine." The narrator is quietly disappointed. Adult-coded, dry, no hiccups or cartoon-drunk sounds.

**5. The Run** (death 198; scoreboard BEAR 5, MOOSE 5)
- Facts:
  - Moose can run at up to about 55 km/h in short bursts (ADF&G; verify the figure and the units).
  - Long legs let them cross deep snow, bogs and fallen logs that slow other animals (verify a source on leg length or gait in snow/bogs).
  - Grizzlies are also fast, roughly similar speeds (NPS; verify). This is the last tie.
- Analogy idea: the speed against a sourced fastest human sprint (about 44 km/h peak).
- Twist: **the bear and the moose are equally fast. Only one of them is fast in a swamp.**
- Doug beat: Doug runs into a bog, looks back, and the moose is walking through it as if it were a lawn. Death 198. Cap on a tussock.
  **No escape tips**, no "run behind a tree" (see Risks).

### Unlike bears.

**6. The Hooves** (death 199; scoreboard BEAR 5, MOOSE 6)
- Facts:
  - Moose fight by striking with their front hooves and stomping, not by biting (ADF&G; verify).
  - 1995, University of Alaska Anchorage: a man was killed by a moose that students had been harassing (Anchorage Daily News, ADF&G or a
    published account; verify the year, the age and the circumstances). **Sober card: no name, no Doug, no joke.**
- Analogy idea: the hoof against a sourced everyday object (a dinner plate), or none.
- Twist: **a bear fights with its mouth. A moose fights with its feet, and it's standing on them already.**
- Doug beat: before the sober card, Doug in a boxing stance. Death 199 (cartoon, cut to black on the first strike). The sober card comes
  after, in silence except for the narration. Cap flat on the snow.

**7. The Snow** (death 200, **played flat, no milestone bit**; scoreboard BEAR 5, MOOSE 7)
- Facts:
  - In deep-snow winters many moose move into Anchorage (ADF&G has an estimate of the winter moose population in the Anchorage area;
    verify).
  - Hungry, tired moose in late winter are more likely to be aggressive and won't leave packed paths and roads (ADF&G; verify).
  - Grizzlies and black bears spend the winter in dens (NPS or ADF&G; verify).
- Analogy idea: snow depth against a sourced everyday height (a kitchen counter), or the Anchorage moose count against a sourced number.
- Twist: **for the worst months of the year, every bear is asleep, and every moose is awake, hungry and standing on the only path.**
- Doug beat: Doug shovels a narrow path from his front door. A moose steps into the path from the other end and doesn't move. Doug waits.
  The moose waits. Death 200, flat ("Doug has died. Again."). Cap on the shovel.

**8. The Rut** (death 201; scoreboard BEAR 5, MOOSE 8)
- Facts:
  - In the autumn rut (September-October), bulls become aggressive (ADF&G; verify the months).
  - Moose antlers grow fresh every year and are shed every winter. A large bull's antlers can span about 1.5-1.8 m (ADF&G; verify the
    span and a growth rate; antler is often called one of the fastest-growing tissues: only with a source).
  - Two bulls were found with locked antlers, frozen in ice, near Unalakleet, Alaska, in 2016 (news photo; verify the place, year and
    source). The bulls died; show **only the antlers above the ice** if at all, no bodies.
- Analogy idea: the antler span against a sourced everyday width (a double bed).
- Twist: **the moose grows a brand-new weapon every summer and throws it away every winter. A bear has to keep the same teeth.**
- Doug beat: Doug wears cardboard antlers (a hat, not a costume) to "blend in". A bull takes this as a challenge. Death 201. Cardboard
  antlers and cap on the moss.

**9. The Train** (Doug SURVIVES; "Doug is fine."; narrator quietly disappointed; scoreboard BEAR 5, MOOSE 9)
- Facts:
  - In deep-snow winters moose walk along railway tracks and stand their ground against trains (Alaska Railroad and ADF&G accounts; verify).
  - The Alaska Railroad has hit hundreds of moose in a single bad winter (verify the winter and the number).
- Analogy idea: a locomotive's weight against the moose (both sourced).
- Twist: **a moose will not get off the track for a train.**
- Doug beat: Doug stands on the track waving at the moose ("hi friend?"). A horn. The moose turns to face the train, not Doug, and Doug
  steps off the other side. "Doug is fine." **No moose death on screen**: cut away on the horn. The moose deaths are a number only.

### Worse than bears.

**10. The Wolves** (death 202; scoreboard BEAR 5, MOOSE 10)
- Facts:
  - Isle Royale, Lake Superior: wolves and moose have been studied there since 1958, one of the longest-running predator-prey studies
    in the world (Michigan Tech, Isle Royale Wolf-Moose Project; verify).
  - Healthy adult moose often stand their ground, and wolves usually give up on them; most kills are calves, old or sick moose (Mech or
    Peterson; verify the wording).
  - Moose reached the island in the early 1900s, wolves around 1949 (verify).
- Analogy idea: the study's length against a sourced span (older than the first Moon landing).
- Twist: **a whole wolf pack, and the moose just stands there until the wolves leave.**
- Doug beat: Doug joins the wolf pack as the newest member ("hi friends?"). The moose turns to face them. The wolves leave one by one.
  Doug doesn't notice. Death 202. Cap in the snow among wolf tracks going away.

**11. The Highway** (the boss; death 203; scoreboard BEAR 5, MOOSE 11)
- Facts:
  - Newfoundland had no moose until people released them: two in 1878 and four in 1904 (Government of Newfoundland and Labrador or Parks
    Canada; verify). Today there are well over 100,000 (verify the current estimate and the year).
  - Moose-vehicle collisions on the island run to hundreds a year, with human deaths (provincial data; verify the numbers and the period).
    Newfoundland has no grizzlies (verify; black bears only).
  - A moose's body sits at windshield height on long legs, so these collisions are far more dangerous than hitting a deer (an insurance
    or transport-agency source; verify). **No injury description at all**: say "far more dangerous", never what happens to people.
  - One line for scale: in North America, fatal bear attacks are rare, a few a year at most (a peer-reviewed review such as Bombieri et
    al. 2019 or Herrero; verify).
- Analogy idea: the six released moose against today's count (sourced arithmetic).
- Twist: **the deadliest thing a moose does to people isn't an attack. It just stands in the road, and somebody brought it here on
  purpose.**
- Doug beat: night. Doug drives a small car (`small_car.json`) down an empty Newfoundland highway, singing. The narrator calmly lists
  the numbers. A dark shape, too tall for the headlights. Cut to black before any contact. Death 203. The cap on a yellow moose-crossing
  sign the next morning. **Sober card** for the collision numbers (no names, no Doug, no joke).
- **Honesty line (required, roughly):** "To be fair to the bears: meet one alone in the woods, and it is the more dangerous animal. It's
  just that there are far more moose, and they live where people drive." (The writer can find better wording; the point must stay.)
- **Closing image:** the field guide open on two pages. BEAR: Doug deaths 0. MOOSE: Doug deaths 8. The scoreboard reads BEAR 5,
  MOOSE 11. Kicker (one line, roughly): "Doug has now been killed by a moose eight times. He has never met a bear."
- **Outro:** 30 words or fewer, final counter (203) and one dry line. No recap, no subscribe pitch.

Deaths: 8 (196-203). Doug survives: The Dive, The Apples, The Train. 11 items.
**Option for the writer:** if the draft runs under 2,900 words, add **"The Ghost Moose"** between items 9 and 10 (winter ticks: tens of
thousands on one moose, which rub off their hair and leave them pale grey; verify a count and the climate link from a peer-reviewed or
agency source; Doug tries to help with a comb, survives, "Doug is fine."; scoreboard MOOSE 10, the ending moves to MOOSE 12). Use no
skin or blood imagery; the moose is just pale. No other additions.

## 3. The opening (style bible 3.2)
- No hook section. **Item 1's name is spoken within the first 35 words.** Its twist lands by 0:45 (aim for 30-40 s).
- Draft beat (the writer may rewrite; the first sentence must state the title promise):
  > "Doug is going to find out why moose hurt more people than bears do. Doug did not agree to this. Like bears. The Deer."
  (24 words, the item name at words 23-24.) The twist (more people injured than by bears in Alaska) follows within about 15 seconds.
- **The one callback** (to 021) goes in item 1, after the twist: "The last time Doug saw a moose, he was wearing one." No other episode
  callbacks.
- No "in this video", no summary, no "hey guys".
- **The thumbnail is the opening image** (1.5-4 s).
  - **Proposal A: archetype C hero.** A huge bull moose head-on at the detailed cartoon tier, ears back, hump hair up, antlers filling the
    top of the frame. Beside it, much smaller, a grizzly glancing at it nervously. Tiny red-capped Doug between them. Flat pale-snow
    background. Text: **"WRONG ANIMAL"** in white bold sans with a dark outline (no title words: Moose, Deadlier, Bear). Fallback
    **"NOT THE BEAR"** only if "WRONG ANIMAL" doesn't read at 168x94; it repeats "Bear" from the title, so it is second choice.
  - **Proposal B for the A/B test: archetype A grid, 3x3.** Nine chapters, each tile the moose doing one thing (diving, in the apple tree,
    on the track, facing wolves, on the night road…) with Doug small in each. Labels are chapter names.
  - The moose must read as heavy and dangerous. Never cute, never cartoon-mascot.

## 4. Running gags
- **Death counter:** "DOUG DEATHS" starts at **195** and ends at **203**. **Death 200 is played flat** (item 7). No milestone bit.
- **"Doug did not agree to this."** in the opener.
- **The field guide** (MOOSE page, see 2), and the two-page closing.
- **"Doug is fine."** at The Dive, The Apples and The Train. **Narrator quietly disappointed** at The Apples and The Train.
- **Befriending the killer:** "hi friend?" (items 1, 3, 9), "hi friends?" to the wolves (item 10). Four is the maximum.
- **The cap survives:** apple (1), willows (3), tussock (5), snow (6), shovel (7), moss beside the cardboard antlers (8), wolf tracks (10),
  moose-crossing sign (11).
- **Episode-only:** the BEAR / MOOSE scoreboard.
- **Callbacks:** one only, to 021 ("he was wearing one"), in item 1.
- Not used: suitcase, drill pod, time machine, LIVE feed, costume gag, THE MENU, THE WAIT, HIPPO SURVIVED tally, Buddy, "had the death
  drawn already", "sharpened the pencils", the out-waiting folding-chair boss (022, used once; item 7's stand-off must be over in two
  shots, no chair).

## 5. Playlist key
`animals` (Doug vs. Animals).

## 6. Target length
15-17 min at about 197 wpm: **2,950-3,350 spoken words**.
- Item 1: about 260-290 words; the first death lands by about 1:20.
- Items 2-10: about 230-270 words each.
- The Highway (boss): 330-390 words, including the honesty line and the closing image.
- Outro: 30 words or fewer.

## 7. Risks
- **Safety advice (HIGH, the main risk of this episode):** "moose attack" content is full of what-to-do tips, and the channel never gives
  medical or safety advice. **No tips anywhere:** no "run", "get behind a tree", "curl up", "brake, don't swerve", "slow down at dusk".
  Warning signs (ears back, hump hair up) can be described as moose behaviour, never as instructions. The description gets no safety
  section either. If a viewer would act on a line, cut it.
- **Over-claiming (HIGH):** the title says "deadlier". The script must:
  - use ADF&G's exact injury wording (Alaska, injuries) and never upgrade it to "kills more people" unless a source says so;
  - put the road deaths on the moose's side only with sourced numbers, and say that they are collisions, not attacks;
  - include the honesty line in item 11 (a bear is the more dangerous animal one-on-one);
  - give every scoreboard tick as the narrator's judgement.
  If the facts can't carry "deadlier", the titler switches to "Why Moose Hurt More People Than Bears" with a death verb added.
- **Real deaths (MEDIUM):** the 1995 Anchorage death and the Newfoundland road deaths go on sober cards with no names, no Doug and no
  jokes. The road deaths are numbers only. No 2026 news events.
- **Gore (MEDIUM):** cartoon deaths, cut to black on first contact. No blood, no wounds, no crash imagery, no dead moose (train, locked
  antlers or road). The locked-antler item shows antlers above the ice at most.
- **Kid-appeal (MEDIUM):** a moose, a grizzly and a stick man can drift toward a children's book. Countermeasures: the dry adult narrator,
  adult-coded lines (the drunk-moose item stays dry, no hiccups), the moose drawn heavy and menacing, agency data on screen as evidence
  cards, no kids' tags, made_for_kids false.
- **Facts that need strong sources (cut if unsourced):**
  - The Deer: largest deer; shoulder height; **ADF&G's injury comparison (exact wording)**.
  - The Dive: dive depth and time; nostrils; bear swimming.
  - The Calf: cow aggression season; calving dates and twins; bear predation on calves.
  - The Apples: the 2011 Gothenburg moose; the drunk-moose debate; bears and fermented fruit.
  - The Run: moose top speed; leg/gait in snow or bog; grizzly speed; human sprint peak.
  - The Hooves: front-hoof fighting; the 1995 UAA death.
  - The Snow: Anchorage winter moose numbers; late-winter aggression; bear denning.
  - The Rut: rut months; antler span, growth and shedding; the 2016 Unalakleet locked antlers.
  - The Train: moose on rail lines; the Alaska Railroad numbers.
  - The Wolves: Isle Royale dates and study length; adult moose standing their ground; wolf prey selection.
  - The Highway: Newfoundland introduction dates and numbers; current population; collision and death numbers; no grizzlies on the
    island; collision danger vs deer; North American fatal bear attack rate.
- **Myths to avoid:** "moose are the most dangerous animal in North America" as fact (the deer family as a whole is counted by road
  collisions, mostly white-tailed deer; don't say it about moose); "moose can't see well" as fact without a source; "drunk moose" as
  fact; "moose are attracted to cars"; anything from Bullwinkle or other cartoons; any viral video as evidence.
- **Duplication:** don't reuse OctoLab's wording or structure. Our twists carry the video:
  - it's a deer, and it hurts more people than the bears
  - the lake is where the moose eats
  - Doug is standing where the bear would
  - the dangerous one is up the tree
  - only one of them is fast in a swamp
  - it fights with its feet
  - the bears are asleep, the moose is on the path
  - a brand-new weapon every year
  - it won't get off the track for a train
  - the wolves leave
  - it just stands in the road, and somebody brought it here on purpose
- **Assets:** the director files these in `asset_requests.md`. In the library already: `moose.json` (bull), `grizzly_bear.json`,
  `grey_wolf.json`, `grey_wolf_sitting.json`, `small_car.json`, `car_half.json`, `field_guide*.json`, `chalkboard.json`, `snowy_fir.json`,
  `pine_tree.json`, `snow_dust_cloud.json`, `canoe_paddle.json` (paddleboard base).
  - New: a cow moose and a calf, a moose head surfacing with pondweed, a moose in an apple tree, a bull moose charging head-down,
    two pairs of locked antlers above ice, a paddleboard, a snow shovel, cardboard antlers (hat), a train front on a snowy track, a
    yellow moose-crossing sign, a night road with headlights, the BEAR / MOOSE scoreboard, an Isle Royale map, a Newfoundland map.
  - The thumbnail hero moose (head-on) and the grizzly at the detailed cartoon tier.

## 8. Shorts candidates (one famous creature or fact plus a hard number)
- Newfoundland's moose come from a few animals released in 1904, and now there are 100,000+.
- Moose dive several metres to eat underwater plants.
- Two bull moose found frozen in ice with their antlers locked (2016).
- A moose stuck in an apple tree in Sweden (2011).
