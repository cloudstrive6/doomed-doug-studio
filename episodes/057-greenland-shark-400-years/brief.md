# Episode 057: Why the 400-Year-Old Greenland Shark Is the Creepiest Fish Alive (brief)

Creative director, 2026-11-24. Backlog idea **#99** (7.7 in `topics`, `ocean`).
Before writing it I read `config/channel.yaml`, the style bible (1.4 title rules, 2 thumbnails, 3.2, the 2026-10-27 retention update,
writer rules), the series bible (Openings, Outro, running gags, costume gag, LIVE feed, episode log to 056), `data/ideas.md`, the 11-22 memo
and its CD decisions, the 050–056 `metadata.json`, the 056 brief, the 026 script (it already has a Greenland shark item) and
`python -m studio signals "greenland shark"` (`data/signals/2026-11-24.json`). The stage stays `idea` until draft 1.

## 0. Why this idea, and why now
- **Lane rule (D4).** `python -m studio topics` (11-24): #98 pilot whales is first at 8.2 but stays held for orca spacing (≥3 slots after 055,
  so 058 or later; memo §4.3, CD 11-22 #2). Next is **#99 Greenland shark, 7.7**, a single famous animal (+0.5). The last two episodes are
  055 `ocean` and 056 `animals`, so the same-playlist default (#133 botfly) does not apply. 056's brief already named #99 as the 057 pick.
- **Engine (rule a).** Depth Theory "Why You'd Never Want To Meet A Greenland Shark": **756K at 13 days, 2,419 vph** today (signals 11-24).
  The same Depth Theory formula on the sperm whale has 9.47M (memo 11-22), so the formula is a proven 1M+ outlier and this animal is live on
  it right now. Other copies: BlackWater "We Were Wrong About How Old Sharks Can Get" 595K; Below The Photic 126K at 11 d. Demand **10/10**
  ("greenland shark age", "greenland shark eye parasite", "greenland shark meat" are all autocomplete, and every one is an item below).
  Saturation: 8 recent 100K+ copies, so the angle must be ours (an age axis, not a "reasons" list).
- **Live-engine experiment (CD 11-22 #3):** engine vph_recent on brief day = **2,419**, under the 3,000 bar. 057 is **not** a test episode;
  it ships normally and does not count for or against the experiment (055 is the test).
- **Not a repeat of 026.** 026 item 6 (death 214) already said: about 5 m, maybe the longest-living vertebrate, eye-lens dating against the
  bomb-carbon pulse, the oldest about 392 years, maturity about 150 years, and the Mayflower anchor. Here:
  - The bomb-carbon method is explained once, freshly worded, in item 9 only (≤3 sentences). **The Mayflower anchor is banned.**
  - **One 026 callback**, one line, in item 8 or 9 ("Doug has met this shark once before, two kilometres down. It didn't remember him.
    It hasn't been long enough.").

## 1. Working title and the format it borrows
- **Working title: "Why the 400-Year-Old Greenland Shark Is the Creepiest Fish Alive"** (64 characters).
  - Animal named in words 3–6 (v2 rubric: as early as possible), dread adjective "Creepiest" (style bible 1.4), the age as the scale claim.
  - Honesty: the oldest estimate is **392 ± 120 years** (Nielsen et al. 2016). "400-Year-Old" is acceptable rounding only because the script
    says the range out loud. If the titler wants to be safer: "Nearly 400-Year-Old".
  - Borrows Depth Theory's single-animal frame and our own 027/037 "Why the [famous animal] Is…" shape. Never Depth Theory's wording.
- **Leads for the titler** (10 candidates in `title_candidates.json`; D4 is a lint only, hand-pick if the top 3 are within 4 raw points):
  - "The Greenland Shark Lives 400 Years, and Almost Nobody Has Seen One Born" (only if item 2's single pregnant female holds up; trim)
  - "Why the Greenland Shark Is Still Growing at 400 Years Old" (only if the growth source supports "still growing")
  - "The Greenland Shark Has Parasites in Its Eyes and Lives 400 Years" (body-horror angle, the parasites bonus; 62)
- **Banned in the title:** "Waiting 400 Years to Eat Doug" (the backlog wording: there is no confirmed Greenland shark attack on a person,
  so it promises something the video doesn't deliver), "Oldest Animal" (the quahog clam Ming was older; the shark is the longest-lived
  **vertebrate** known), "Immortal", "Older Than Shakespeare"/any date anchor the low end of the range can't support, "You'd Never Want to
  Meet", "Nobody Talks About" (competitor wording), "Every Age"/"Every Century" (reads as the blocked era lane).
- **Thumbnail (the opening image; archetype C hero close-up):**
  - A huge, slow, grey-brown Greenland shark face under a ceiling of sea ice, small eye with a pale **copepod dangling from it** (cartoon
    streamer, not gore), a seal-sized gap in its mouth line.
  - Above the ice, through a hole: Doug in his cap holding a **birthday cake crowded with candles**, peering down. Cartoon, cold blue palette
    (art bible ocean colours).
  - Text ≤3 words, not in the title: **"STILL GROWING"** (if item 3 supports it) or **"HALF BLIND"**. Never "400", "OLD" or "SHARK".

## 2. Axis and items
**Declared axis: the age of the shark Doug meets, in years, monotonic from 0 to about 392.** Each item is a shark at a sourced (or
"about") age, and the fact attached to that stage of its life. Most extreme last: the oldest shark ever dated. This is a single animal's
lifespan, **not** an era/deep-time axis: no geology, no "when Earth was", no world-history tour (one anchor line per item at most).
Item 1 is a cold open on an adult of unknown age (the strongest hook, the eye parasite); then the axis starts at birth.

**Spoken bands (short headers):**

| Header | Items |
|---|---|
| (no header: cold open) | 1 |
| **"Year zero."** | 2 |
| **"Decades."** | 3–4 |
| **"A century."** | 5–6 |
| **"Centuries."** | 7–9 |

- **Episode-only device: SHARK AGE** (staging only, never read aloud; the art director approves it). A crude birthday card under the death
  counter: "SHARK AGE: ?" at item 1, then 0, ~10, ~50, ~100, ~100, ~150, ~250, and finally "~392 (±120)" with a red stamp. Monotonic after
  item 1. It is not THE WAIT (022, a stopwatch), NOW SERVING (056) or THE RING (055). No field guide (`ocean`).
- **No costume engine** this time (055 and 056 both ran one). One costume at most: a **seal costume** at item 4 only if the art director
  confirms it reads differently from 051's.
- **The narrator's running observation:** the shark never chases Doug. It waits for things to end up in the water. Doug keeps ending up in
  the water. Say the rule once (item 4 or 5), then let the pictures do it.

**Words:** 215–255 per item, 9 items, 1,950–2,350 in total. If long, cut item 6 first, then item 3. Never cut items 1, 4, 5 or 9.

Every number below is a lead. The writer verifies each one in `facts.md`. **If a fact can't be sourced, cut it; don't hedge it.**

| # | Item (name sentence) | Facts to research (2–4) | Everyday scale analogy | Doug beat |
|---|---|---|---|---|
| 1 | **The Eye.** (cold open; one of the three strongest) | The copepod *Ommatokoita elongata* attaches to the shark's cornea; prevalence is very high in some populations (Berland 1961; Borucinska et al. 1998, *J. Fish Diseases*, for the corneal damage; give the source's share). It's often called blind, but recent work found its retina is adapted to dim light and still functional in old animals (find the 2024–25 vision paper, e.g. the Fogg/Valenzano retina study; attribute it). **Twist (by 0:45):** a crustacean is hanging off its eyeball for life, and it still catches seals (item 4 pays this off). | A passenger who has ridden on your eyeball for decades, and you still drive. | Doug, under the ice with a torch, says hi to the copepod ("hi friend?"; it is the only one who waves back). The shark turns, very slowly. **Death 415**, cut away, played flat. |
| 2 | **The Pup.** ("Year zero.") | Live-bearing; born around 40 cm. Almost everything known about its birth rests on **one pregnant female** recorded in 1957 (Koefoed: about 10 near-term embryos, ~37 cm; verify). Nobody has found a nursery or seen a birth (source a review, e.g. Nielsen et al. 2020 or the IUCN assessment). | Knowing how humans are born from one hospital note from 1957. | Doug finds a pup and holds up a "WELCOME" banner. It swims past. **Survival** ("Doug is fine. The pup will think about him in about 150 years."). |
| 3 | **The Growth.** ("Decades.") | Grows roughly **1 cm a year or less** (Nielsen et al. 2016 or Hansen 1963 tagging recapture: give the source's figure). Your fingernails grow about 3–4 cm a year (sourced). Max length about 5–6 m in the literature (give the source's number; 026 said "about five", so use the max-recorded figure only if sourced). | Your fingernails outgrow it. | Doug with a tape measure, checking a ~10-year-old shark "for a year". The narrator states the Arctic water temperature (near −1.8 °C, sourced) and no survival time. **Death 416**, frost-white flat Doug, cap on the tape. Played flat. **No cobwebs** (056) and **no out-waiting** (022). |
| 4 | **The Slowest Shark.** ("Decades.") | Tagged sharks cruise about **0.34 m/s** (about 1.2 km/h) with one tail-beat cycle every ~7 s, the slowest relative to size of any fish measured (Watanabe et al. 2012, *J. Animal Ecology* or *JEMBE*: check). **Twist:** seals turn up in its stomach anyway (Leclerc et al. 2012; McMeans et al. 2015; Nielsen et al. 2019 diet; give a share). One idea: it takes them asleep (attributed: "researchers think", Watanabe et al.). | Slower than a shopping trolley rolling across a car park, and it still catches things. | Doug, asleep on a floe edge (seal costume optional, see above). The rule line: "The Greenland shark doesn't chase. It waits for things to end up in the water." **Death 417**, cut away. |
| 5 | **The Menu.** ("A century.") | Stomach contents include **land mammals**: reindeer, polar bear remains, horse/moose (find primary records: e.g. Leclerc et al. 2011/2012, the 2016 Norwegian reindeer report, the polar-bear record; name only what's sourced). It's a scavenger that turns up at carcasses fast (baited-camera studies, e.g. Devine et al. 2018). **Twist:** things on land fall in, and the shark is already there. | The Arctic's lost-property office, except everything handed in gets eaten. | Doug picnicking on the ice. Crack. **Death 418**, played flat: "The shark wasn't involved. It was only the next step." No body shown in the water: a hole, the cap on the edge. |
| 6 | **The Meat.** ("A century.") Cut first if long. | Its flesh is **toxic when fresh** (high TMAO, broken down to trimethylamine; Anthoni et al. 1991 or a food-science review). In Iceland it's fermented and hung to dry for months as *hákarl* (source the process length). One line only on effects, **no symptoms list, no preparation steps**. | Food that needs four months of waiting before it stops being a weapon. | Doug at an Icelandic counter, one cube of hákarl. **Survival** ("Doug is fine. He has been asking for water for an hour."). |
| 7 | **The Teenager.** ("Centuries.") | Females mature around **4 m, roughly 150 years old** (Nielsen et al. 2016: give the paper's range). So a population takes generations of people to recover; it's caught as bycatch and listed as Vulnerable (IUCN 2020; one line). Anchor (one, sourced and safe at the low end): born before the light bulb. | Becoming an adult after your great-great-grandchildren would have. | Doug, a "CONGRATULATIONS" card for the 150-year-old. It ignores him. **Survival**, and the narrator is **quietly disappointed** (the only time). Re-hook: "And this one isn't even old yet." |
| 8 | **The Deep.** ("Centuries.") | Recorded down to about **2,200 m** (Herdendorf & Berra 1995 or a tagging study; give the source's maximum), living in water near freezing. The cold slowing its metabolism is the leading explanation for the long life (attributed: "the main idea is"). Its genome (2024 preprint/2025 paper: about twice the size of ours, extra DNA-repair genes; verify the venue and wording). | A body in permanent slow motion: a fridge for a lifetime. | Doug in a crude submersible ("For this part, Doug has a submersible.") going down past a ~250-year-old shark. 026 callback line (once). **Death 419**, cut away (the sub light fades, cap drifts up). |
| 9 | **The Oldest.** ("Centuries.", the boss; about 1,900 words in) | Nielsen et al. 2016 (*Science*): 28 sharks dated from the eye-lens nucleus (formed before birth) against the 1950s–60s bomb-carbon pulse; the largest, a **502 cm female, 392 ± 120 years**. Say the range. Even the low end (272 years) makes it older than the United States. Kicker: it is still growing, and it still has more time than Doug. | A birthday cake that needs about 392 candles, give or take 120. | **The payoff promised in the opening.** Doug lowers a candle-crowded birthday cake through the ice hole. The candles melt the edge; Doug goes in with the cake. A very large, very slow shape below. **Death 420**, cut to black, played flat. |

**Expected deaths: 6** (counter 414 to 420). Survivals at items 2, 6 and 7. The writer may turn one more death into a survival, but not the boss.

**Closing (after the boss kicker, `ocean` standard: the LIVE feed):** the ship's monitor, red "LIVE" tag, the cap drifting down into frame and
settling on the upturned cake on the seabed; the shark passes over both, very slowly, and leaves them (not the cap on the shark's back:
that was 026's image). SHARK AGE card ticks to "~392 (±120) + 1 MIN". One fresh dry kicker about the
cap (e.g. "The cap has now spent more time with the oldest vertebrate on Earth than anyone alive."). Must not be a 026, 050 or 055 line.

## 3. The opening (series bible "Openings", style bible 3.2 and the retention update)
- **No hook section.** The thumbnail image (the shark face under ice, copepod on the eye, Doug with the cake above) is the first frame.
- **First sentence (the cold-open fact, sourced):** "Some of the sharks swimming under the Arctic ice right now were alive before the United
  States existed." Source: Nielsen et al. 2016 (low end of the oldest estimate, 272 years, is 1744). Doug's line comes second.
- **Payoff promise by 0:10:** "By the end of this, Doug is holding a birthday cake over a hole in the ice, for a shark that's been alive for
  about four hundred years." The writer may tighten it but must keep it specific.
- **"The Eye." by word 35.** Its twist (a parasite hangs off its eyeball for life and it still hunts) lands by 0:45, about 145 words.

## 4. Running gags
- **Death counter**, starting at **414** (after 056). Deaths are played flat.
- **"Doug did not agree to this."** once, at item 8 (the submersible).
- **"Doug is fine."** at items 2, 6 and 7, each written fresh. No "Eventually.", "Indoors.", "Doug floats." or "Doug is in the middle.", and
  not 056's "He has never been more insulted."
- **Narrator quietly disappointed** at item 7 only.
- **Cap survives:** on the tape measure (3), the ice edge (5), drifting up from the sub (8), and riding the shark in the LIVE feed closing.
- **"hi friend?"** once (item 1, to the copepod).
- **Callbacks:** 026 once (item 8 or 9). Nothing else. Not 029 (leopard seal under ice) or 031 (polar bear).
- **Outro (rule from 048):** after the closing kicker, ≤30 words: the death counter plus one fresh deadpan subscribe line tied to the counter
  (the birthday idea fits: a number that only goes up, faster than the shark's). Not a 048–056 line or the bible's example; no comment prompt.
- **Do not reuse:** the suitcase, the time machine, the field guide, THE MENU, THE WAIT, NOW SERVING, THE RING, cobwebs, the out-waiting
  boss, the 026 frost-on-the-shark's-back death, the Mayflower anchor.

## 5. Playlist
`ocean` (Doug vs. the Ocean). The previous two are 055 `ocean` and 056 `animals`, so there's no same-playlist pair. 058 may be #98 pilot whales
(`animals`, orca spacing satisfied) or the parasites pick if 057's result argues for it.

## 6. Length and payoff
- **Target 10–12 min**, about **1,950–2,350 words** at ~195 wpm (standing rule), 9 items, 215–255 words each.
- **Payoff promise line (opening):** "By the end of this, Doug is holding a birthday cake over a hole in the ice, for a shark that's been alive
  for about four hundred years."

## 7. Risks
- **Gore.** No bite wounds, no damaged eyes in close-up (the copepod is a pale cartoon streamer, the eye a simple dot), no partly eaten
  carcasses: stomach contents are a list in narration, illustrated as a crude list card or silhouettes, never remains. Deaths are X eyes,
  frost-flat or cut to black.
- **Medical/safety advice (medium: items 3 and 6).** No cold-water survival times or advice, no hypothermia symptoms. Hákarl: no
  preparation steps, no dose, no symptoms list; one line that fresh meat is toxic and why. No alcohol gag.
- **Kid appeal (medium: birthday cake, pup, banners).** The cake and cards are deadpan office-party humour, not a kids' party; the pup isn't
  cute (no big eyes). Made-for-kids stays No.
- **Misleading packaging.** No implication that it hunts or attacks people. "Oldest vertebrate known", never "oldest animal". The age is
  always an estimate with its range. "Blind" only as "often called blind", corrected by item 1's source.
- **Overclaims to avoid:** "512 years old" as a fact (it's the top of the error bar); "lives 500 years"; the 1957 single-female claim unless a
  source says it; polar bear predation (remains in a stomach ≠ killed a polar bear; say "remains"); sleeping-seal hunting as fact (it's a
  hypothesis); the genome as "the secret of immortality".
- **Strong sources needed:** Nielsen et al. 2016 (*Science*) for age, growth and maturity; Watanabe et al. 2012 for speed; Berland 1961 /
  Borucinska et al. 1998 for the copepod; the 2024–25 retina paper for vision; Leclerc/McMeans/Nielsen diet papers for stomach contents;
  Anthoni et al. 1991 (or a food-chemistry review) for TMAO; Herdendorf & Berra 1995 (or tag data) for depth; IUCN for status; the genome
  paper (verify it's published or say "a 2024 study" with the preprint named in `facts.md`). Never a competitor video, listicle or aquarium
  blog for a number.
