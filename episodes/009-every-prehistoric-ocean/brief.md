# Episode 009: One Night in Every Prehistoric Ocean (brief)

Creative director, 2026-10-08. Backlog idea #3, "Surviving One Night in Every Prehistoric Ocean" (6.9 at the 10-01 re-rank). The engine
has moved a lot since then (see section 0). The stage stays `idea` until draft 1.

## 0. Why this idea, and why now
- **The queue is empty.** Ep 008 went live today (Thu 8 Oct, 05:00 NZDT) and nothing else is scheduled. Ep 009 is needed now, so it can't
  wait for a data read.
- **#14 Venom (8.4)** is still on hold. The 10-01 decision was to wait for ep 002's day-7 data. Ep 002 went public 2026-10-01 16:00Z, so it
  reaches day 7 today, but analytics lag 24-72 h and the newest pull is 10-04. Venom is the planned **ep 010** once that data lands. It
  also takes the channel out of the prehistoric/ocean rotation.
- **#27 Drawn Wrong (7.9)** is prehistoric too, and its engine is 359K (no 1M+ outlier). It fails rule (a).
- **The engine for #3 is now the hottest in the lane** (`data/competitors/2026-10-08.json`):
  - Fossil, "How Long You'd Last in Every Prehistoric Era": **10.6M, 476x, 15,215 vph_recent**. This is the highest vph of any long video in
    the file, and it is still accelerating (8.98M on 10-01).
  - ExtinctZoo, "The Deadliest Sea Animal From Every Single Period": **2.75M (3.3x), 1,224 vph**. This is the list version of the topic.
  - Fossil, "Could You Survive Every Prehistoric Apex Predator?": 301K (13.5x). Fossil, "...Every Ice Age Continent": 305K (13.7x).
  - **Warning:** BeyondTheBlue, "How Long You'd Last in Every Prehistoric Ocean" is at **311K with 6,704 vph**. It is a fresh copy of this
    exact concept. Interest is live, but the lane is getting crowded (same pattern as BTB vs. our ep 001). We differentiate on
    **title wording, item twists and the Doug mechanic**. We do **not** use "How Long You'd Last" in the title.
- **Lane balance:** this is a prehistoric episode (003, 005, 007 were too), but it is also an ocean episode, and the premise names
  "prehistoric oceans". The last episode (008) was `ocean`, so this is not back-to-back. After this, the next two episodes must come from
  outside `prehistoric` (Venom first).

### Overlaps resolved
- **003 (mass extinctions)** used the ocean *events* (Dead Reefs, Hot Tub Ocean, Purple Oceans, Acid Seas) and mentioned Dunkleosteus in one
  sentence as a victim. This episode is about the **predators**, not the extinctions. No item may be an extinction event. The Dunkleosteus
  item gets one callback line ("Doug has seen this fish before. It was dying at the time.").
- **005 (fossils)** ended on Stanleycaris, a Cambrian radiodont, and had an ichthyosaur skin item. Anomalocaris (item 1) is a relative:
  give it one callback line at most. Cymbospondylus (item 6) is a different, much older and much bigger ichthyosaur. No skin or soft-tissue facts.
- **008 (food chain)** used the moray's second jaw, the saltwater crocodile and the sperm whale. One callback is allowed at Tylosaurus
  (the teeth on the roof of its mouth, "the moray's idea, but bigger"). No more than that.
- No modern animals as items. The great white may appear only inside the Megalodon item (the competition fact).

## 1. Working title and proven outlier
- **Working title:** **What Dying in Every Prehistoric Ocean Would Be Like** (T1, 51 chars, 9 words; death verb "Dying", scope device
  "Every"). Ep 008 was T2-style, so T1 is not back-to-back.
- **Engine:** Fossil, "How Long You'd Last in Every Prehistoric Era" (10.6M, 476x, 15,215 vph). Support: ExtinctZoo, "The Deadliest Sea Animal
  From Every Single Period" (2.75M, 3.3x). The T1 frame is PE's top skeleton: "What Dying on Every Planet Would Be Like" (12.7M).
- **Alternates for the titler:**
  - "How Doug Would Die in Every Prehistoric Ocean" (T2, 45 chars). Note: 001 and 003 used this exact skeleton.
  - "The Deadliest Thing in Every Prehistoric Ocean" (T3-style, 46 chars)
  - "Why the Prehistoric Ocean Got Deadlier the Longer It Went On" (T6)
  - Banned wording: "How Long You'd Last" (Fossil, BTB), "Every Single Period" (ExtinctZoo), "Could You Survive" (Fossil).

## 2. Escalation axis and items
**Axis: era (oldest to youngest), about 508 million years ago to about 3.6 million years ago.** Predators get bigger, and Doug lasts
less time at every stop. The final item is the most famous and the highest-ranking predator ever measured.

**Episode mechanic (new, episode-specific): "one night".** At each stop, the time machine drops Doug at sunset in that era's sea with a
snorkel (`snorkel_gear.json`). His job is to last until sunrise. A small **night clock** sits next to the death counter (moon icon plus
"DOUG LASTED: 4 h 12 min"). It freezes when he dies and the next item resets it. The times are jokes, not science claims: never present them
as calculated. The trend should be roughly downward (hours, then minutes, then seconds), and the boss should be the shortest. The art director
owns the clock design (`clock.json` exists as a base). This is our answer to the "how long you'd last" engine. Use it in this episode only, the
way 007's FROZEN meter was used only once.

Spoken section headers (2 words or fewer): **"Paleozoic."** (before item 1), **"Mesozoic."** (before item 6, about 45%), **"Cenozoic."**
(before item 10, about 78%). Backgrounds get darker and colder at each era, ending in deep navy for the Miocene.

Each item lists 2-4 facts to research. The writer must find and cite the exact paper or cut the claim. Don't trust citations in this
brief: they are leads.

### Paleozoic.

**1. Anomalocaris** (Cambrian, about 508 Ma; the hook item)
- Facts: about 1 m long or less (sourced), one of the largest animals of its time; huge compound eyes with thousands of lenses
  (Paterson et al. 2011, *Nature*); a 2023 study found its grabbing appendages were built for **soft, fast prey**, too delicate to crack
  trilobite shells (Bicknell et al. 2023, *Proc. R. Soc. B*).
- Analogy idea: an animal the length of a sourced everyday object (a skateboard or a bath towel), the biggest thing in the sea.
- Twist (must land by 0:45, about 145 words; aim for 25-35 s): **it couldn't crack the armoured animals, so it went for soft ones.** Everything
  in the Cambrian sea had a shell except one thing.
- Doug beat: Doug hides among the trilobites, feeling safe, and taps one on the shell. He is the only soft thing in the water. Death 75.
  Night clock: hours. One callback to 005's Stanleycaris at most.

**2. Endoceras** (Ordovician, about 460 Ma)
- Facts: a straight-shelled nautiloid; the largest known shell fragments suggest a total length of several metres (sourced, with the
  estimate's uncertainty stated plainly); cephalopods were the top predators of the Ordovician seas (sourced); it is related to today's
  nautilus (sourced).
- Analogy idea: a shell as long as a sourced object (a car, or a canoe).
- Twist: **the giant size rests on an incomplete fossil.** The real number is an estimate, and scientists argue about it. Say so in one
  line; don't overclaim.
- Doug beat: **Doug survives.** It is slow and Doug climbs inside the empty end of an old shell for the night. Sunrise. "Doug is fine."
  The night clock reaches morning. No death.

**3. Jaekelopterus** (Early Devonian, about 390 Ma; a sea scorpion)
- Facts: the largest arthropod ever found, about 2.5 m, estimated from a 46 cm claw (Braddy, Poschmann & Tetlie 2008, *Biology Letters*);
  sea scorpions (eurypterids) lived in brackish and coastal water (sourced); compare with the largest living arthropod (sourced).
- Analogy idea: the claw as long as a sourced object (a baseball bat is too long; find a match), the whole animal longer than a sofa
  or a grown man lying down.
- Twist: it is known from a claw. Everything else is scaled up from that one claw, and the scale is still terrifying.
- Doug beat: Doug tries to befriend it like a lobster at a restaurant tank ("hi friend?"). Death 76.

**4. Dunkleosteus** (Late Devonian, about 370 Ma)
- Facts: armoured placoderm with bony blades instead of teeth; one of the strongest bites known in fish, with a very fast jaw opening that
  sucked prey in (Anderson & Westneat 2007, *Biology Letters*); a 2023 study cut its length estimate to about 3.4 m but made it far chunkier
  (Engelman 2023, *Diversity*).
- Analogy idea: the new length compared with a sourced object (a family car), and the jaw-opening speed compared with something everyday
  (only if the paper supports a time in milliseconds).
- Twist: **scientists shrank it**, and the shorter, heavier version is worse news for Doug.
- Doug beat: one callback to 003 ("Doug has seen this fish before. It was dying at the time."). Doug waves at an old friend. Death 77.

**5. Helicoprion** (Permian, about 290-270 Ma)
- Facts: a spiral "tooth whorl" fossil that puzzled scientists for about a century; CT scans showed it sat inside the lower jaw and the
  animal was a relative of ratfish, not a true shark (Tapanila et al. 2013, *Biology Letters*); body-size estimate (sourced, with range).
- Analogy idea: the whorl compared with a sourced everyday spiral (a cinnamon roll, a coiled garden hose).
- Twist: for 100 years nobody knew **where the spiral went**. The drawings over the years put it in strange places (one line, sourced;
  this also tests demand for the "drawn wrong" idea, #27).
- Doug beat: Doug holds up three old reconstructions and tries to guess which one is right. It finds him first. Death 78.

### Mesozoic.

**6. Cymbospondylus** (Middle Triassic, about 244 Ma; *C. youngorum*)
- Facts: one of the first giant animals on Earth, with a skull about 2 m long and a body around 17 m (Sander et al. 2021, *Science*);
  ichthyosaurs reached whale size within a few million years of their origin (same paper); this happened soon after the end-Permian
  extinction (sourced dates only).
- Analogy idea: the length compared with a sourced object (a city bus, `school_bus.json` if the size fits).
- Twist: **the ocean that had just been emptied produced its first giant almost immediately.** One-line callback to 003's end-Permian is
  allowed, but don't explain the extinction again.
- Doug beat: Doug arrives with a "the ocean is recovering" sign. It has recovered. Death 79.

**7. Pliosaurus** (Late Jurassic, about 150 Ma)
- Facts: the Weymouth Bay pliosaur skull, about 2 m long (Benson et al. 2013, *PLoS ONE*, *Pliosaurus kevani*); bite force and feeding
  estimates (Foffa et al. 2014, *Palaeontology* or *Proc. R. Soc. B*, verify); the large Dorset skull found in 2022-23 (sourced to the
  museum or a reliable outlet; mention only if solid).
- Analogy idea: a skull as long as a sourced object (a door lying down, or a grown man).
- Twist: **the TV version was wrong.** Older documentaries made its relative Liopleurodon about 25 m long; the real animals were much
  smaller (sourced). Then: smaller didn't help.
- Doug beat: Doug is relieved by the size correction and relaxes. Death 80.

**8. Xiphactinus** (Late Cretaceous, about 85 Ma; Western Interior Seaway)
- Facts: a bony fish about 5 m long (sourced); the famous Kansas "fish-within-a-fish" fossil, a Xiphactinus with a nearly 2 m Gillicus
  inside it (Sternberg Museum / Everhart, sourced); the likely reading is that swallowing such a big meal killed it (state as the
  usual interpretation, not fact).
- Analogy idea: swallowing a fish about as long as a sourced object (a grown man, a ladder).
- Twist: **its biggest meal killed it.**
- Doug beat: **Doug survives.** He is swallowed whole and the fish, true to form, gives up. Doug climbs out at sunrise. "Doug is fine."
  The narrator is quietly disappointed. No death. (Cartoon only: no stomach interior detail, just a dark frame with Doug's cap glowing.)

**9. Tylosaurus** (Late Cretaceous, about 85-80 Ma; a mosasaur)
- Facts: one of the largest mosasaurs (length sourced with range); stomach contents including a plesiosaur (Everhart 2004 or the correct
  citation), and any recorded Xiphactinus link only if sourced; a second set of teeth on the roof of the mouth (pterygoid teeth)
  to ratchet prey inward (sourced).
- Analogy idea: length compared with a sourced object (a lorry, a bowling lane).
- Twist: the teeth on the roof of its mouth. One callback to 008's moray ("the moray's idea, scaled up").
- Doug beat: Doug, fresh out of the Xiphactinus, is the only thing in the water with no armour and a red cap. Death 81. The cap floats.

### Cenozoic.

**10. Basilosaurus** (Eocene, about 40-34 Ma)
- Facts: the name means "king lizard" because the first scientist thought it was a reptile; it is an early whale (sourced); about 17-20 m
  long with tiny hind legs (sourced); stomach contents from Wadi Al-Hitan, Egypt, show it ate young *Dorudon* (Voss et al. 2019, *PLoS ONE*).
- Analogy idea: the hind legs compared with a sourced everyday object (about the size of a human arm or a child's leg, use the paper's
  number).
- Twist: **it was a whale that ate other whales**, and it still had legs. State the prey fact flatly and clinically, no injury detail.
- Doug beat: Doug laughs at the tiny legs. Death 82.

**11. Livyatan** (Miocene, about 9-10 Ma; Pisco, Peru)
- Facts: a sperm whale relative with teeth up to about 36 cm, the largest teeth of any animal used for eating (Lambert et al. 2010,
  *Nature*); unlike modern sperm whales, it had functional teeth in both jaws (sourced); likely hunted baleen whales (sourced as a
  hypothesis).
- Analogy idea: one tooth as long as a sourced object (a forearm, a wine bottle, a school ruler).
- Twist: the genus is named after the biblical sea monster, and a second fact: it shared its sea with the next item.
- Doug beat: one callback to 008's sperm whale ("Doug has been clicked at by its descendant. This one had teeth."). Death 83.

**12. Megalodon** (the boss; Miocene to Pliocene, about 23-3.6 Ma)
- Facts: size estimates and their uncertainty, including the recent slimmer-body reconstruction (Shimada et al. 2025, *Palaeontologia
  Electronica*, verify) and older estimates; nitrogen- and zinc-isotope studies place it at a **higher trophic level than any marine
  animal ever measured** (Kast et al. 2022, *Science Advances*; McCormack et al. 2022, *Nature Communications*); bite marks on fossil whale
  bones (sourced); extinction around 3.6 Ma, and the zinc study suggests competition with the early great white may have played a role (state as
  a hypothesis).
- Analogy idea: a tooth the size of a sourced object (a human hand), and the body compared with something big and everyday (a row of
  cars or buses, whichever the numbers support).
- Twist: **it ate the predators that ate the predators.** It sat above the top of the food chain (a straight callback to 008's climb in
  one line).
- Doug beat: the shortest night clock of the episode (seconds). Death 84. The cap floats up into the Pliocene sunrise.
- **Closing image:** the time machine is back in 2026, door shut. A giant tooth is stuck in the door, and the cap sits on the roof.
  Kicker about the cap. Do **not** reuse 007's ice block.

Deaths: 10 (75 to 84). Survivals: Endoceras and Xiphactinus.

## 3. The opening (style bible 3.2)
- No hook section. **"Anomalocaris." must be spoken within the first 35 words.** Its twist (it couldn't crack shells, so it hunted soft
  prey) must land by 0:45, aimed at 25-35 s.
- Draft to beat (the writer may rewrite; the word count is the constraint):
  > "Every ocean Earth has ever had, one night each. Doug has a time machine, a snorkel, and until sunrise. Doug did not agree to this.
  > Paleozoic. Anomalocaris."
  (about 27 words)
- **The thumbnail is the opening image** for 1.5-4 s. Suggested archetype **A, a 3x4 grid**: 12 predators on saturated backgrounds, with
  Megalodon in the bottom-right tile on the darkest one. Alternative **B**: a vertical era stack (Cambrian at the top in pale blue, Miocene
  at the bottom in near-black) with the monsters in bands and a tiny Doug in the top band. The graphic designer decides after a feed-size
  test. Labels may not repeat title words (Dying, Every, Prehistoric, Ocean). Label the creatures by name.

## 4. Running gags
- "Doug did not agree to this." (opener)
- **Death counter**: "DOUG DEATHS" starts at 74 and ends at 84.
- **Night clock** (new, this episode only): "DOUG LASTED" next to the counter.
- **Time machine** (standard for `prehistoric`): it drops Doug at sunset at every stop. The door opens onto the danger. Closing image as above.
- **"Doug is fine."** at Endoceras. At Xiphactinus, the narrator is quietly disappointed.
- **Befriending the killer:** "hi friend?" at Jaekelopterus; waving at the Dunkleosteus "old friend".
- **The cap survives:** floats at Tylosaurus, rises into the sunrise at Megalodon, sits on the time machine at the end.
- Callbacks: 003 (Dunkleosteus, one line), 008 (moray at Tylosaurus and sperm whale at Livyatan, one line each). Optional one-liner to 005
  at Anomalocaris. No more than four callbacks in total.
- Not used: costume gag (no prey costumes this time; the snorkel is the gear), suitcase (`places` only), LIVE feed (`ocean` only), Buddy.

## 5. Playlist key
`prehistoric` (Doug vs. Prehistoric Earth).

## 6. Target length
15-18 min at about 197 wpm: **2,900-3,400 spoken words**. Item 1 about 250, items 2-11 about 230-270 each, Megalodon (boss) 330-380
including the closing image. Outro of 30 words or fewer: final counter (84) plus one CTA asking which era Doug should visit next. No recap.

## 7. Risks
- **Gore:** it is a predator episode, so use the strictest line. Every death is cartoon only: swallowed off-screen, a splash, X eyes, a
  ghost Doug, the floating cap. No bite or injury description on Doug. Fossil bite marks and stomach contents are stated clinically, in one
  line each. Don't show carcasses; bones and fossils are fine at the illustration tier. No real kill footage.
- **Kid-appeal risk (medium-high):** dinosaur-era sea monsters attract kids. Keep the narrator dry and adult: the jokes are about scientists
  revising numbers, Doug's poor decisions and the narrator's indifference, never about cuteness. Creatures stay at the detailed cartoon tier
  and look dangerous, not plush. The thumbnail must look like nature horror, not a dinosaur picture book.
- **Facts that need strong sources (cut the claim if it can't be sourced):** Anomalocaris appendage study and eye lens count; Endoceras
  length (an estimate from fragments: say so); Jaekelopterus length from the claw; Dunkleosteus bite force, jaw speed and the 2023 size
  revision; Helicoprion jaw position and ratfish relationship; Cymbospondylus size and timing; Pliosaurus skull length and the Liopleurodon
  TV-size claim; the Xiphactinus fish-within-a-fish interpretation; Tylosaurus stomach contents and pterygoid teeth; Basilosaurus "king
  lizard" naming and Dorudon stomach contents; Livyatan tooth length and "largest teeth used for eating"; Megalodon size range, trophic level
  claims and extinction hypothesis. Every size figure must give the range or say "estimated".
- **Dates:** give each era's date as "about N million years ago" and match the ICS chart (cite it once in facts.md).
- **Medical/safety advice:** none.
- **Duplication:** don't reuse ExtinctZoo's or Fossil's wording or item order. Our twists (soft prey, scientists shrank it, where did the spiral
  go, its biggest meal killed it, above the top of the food chain) carry the video.
