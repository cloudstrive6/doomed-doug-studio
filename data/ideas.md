# Idea backlog (ranked by the growth analyst)

Score = expected views/speed (1–10). "Engine" = the proven outlier formula it borrows. Views, outlier_x and vph come from
`data/competitors/2026-10-17.json` unless marked "signals" (`python -m studio signals`, `data/signals/2026-10-17.json`; older
rows may cite the `2026-10-09.json` / `2026-10-01.json` snapshots) or "style bible". Status: backlog / in-production / published. Never delete published rows.
Last re-rank: 2026-10-17 (memo `data/insights/2026-10-17.md`).

**Scoring: weights moved to the "≥10 episodes with 7-day data" tier** (eps 001–010 are past day 7 as of 10-17):
Score = 0.20 Eng + 0.15 Interest + 0.10 Demand + 0.10 Sat + 0.45 Own, each component 0–10.
- **Eng:** 10 = ≥5M or ≥10x on ≥1M; 8 = 2–5M at ≥3x or repeated hits; 6 = ~0.5–1.5M or a small-channel ≥5x; 4 = weak (<2x) or style bible only; 2 = unproven.
- **Interest:** best `vph_recent` of the engine video(s) (signals `vph_best` or median where the engine isn't watched): ≥3000 = 10, 2000+ = 8, 1000+ = 6, 500+ = 4, 200+ = 3, <200 = 1.
- **Demand:** the `signals` demand score for the TOPIC query. Where the autocomplete is polluted by games or kids' content, the score is lowered and the reason noted.
- **Sat:** `signals` recent 100K+ copies for the FORMAT phrase: ≤3 = 10, 4–8 = 5, 9+ = 2. `?` = not queried yet (scored 5).
- **Own (per playlist, 10-17)** [inference; held to the 3–7 range because long-video day-7 counts are single digits; Shorts lifetime views are the stronger signal]:
  parasites **6** (002 day-7 6.8, about the median; Shorts median 692 / mean 615; 014 got 137 imp but has a 14 s AVD), animals **6** (010 day-7 11.0, the top long video; 011 has 18 views at day 6, our fastest start;
  orca Short 1,411 is the best Short), places **5** (004 day-7 4.5; 012 has 2 views at day 5; Shorts median 605), prehistoric **5** (day-7 4.0/10.0/3.3/8.8; 12 Shorts, median 437, four ≥1,000),
  ocean **5**, up from 3 (day-7 4.4/11.2/6.3; 006/008 Shorts 1,136, 830, 1,012, 1,411), compilations **5** (no data).
- **Formula status (day-7 vs channel median 6.6):** T2 **dropped** (3 strikes: 001, 003, 008). T1 2 strikes (004, 007), and 012 is likely the 3rd on 10-19, so new ideas avoid T1 titles until 014/016 are judged.
  T3/T4 0 strikes. T6/T7/T8 not judged yet.

Playlist keys: ocean, parasites, prehistoric, places, animals, compilations.

## Ranked backlog
| # | Working title | Playlist | Engine (proven outlier) | Eng | Interest (vph) | Demand | Saturation (format) | Own | Score | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| 39 | **NEW** Why Orcas Hunt Everything Except Doug | animals | OctoLab "Why The Ocean's Deadliest Predator Refuses To Kill Us" 8.08M (122x); "Why The World's Largest Predator Refuses to Kill Us" 274K (4.15x, 9 d); PT/ES clones 4.51M / 2.98M (signals); **our Short "Orcas Hunt Great Whites but Have No Record of Killing Us" 1,411 (best Short)** | 10 | 8 ("orcas" median 2,830; OctoLab 1,165) | 9 ("orcas") | 5 ("why orcas refuse to kill us" 5, of which 4 are non-English clones; BTB is the only English one) | 6 | **7.3** | backlog (**recommended ep 021**; new formula "Why X Refuses to Kill Us"; 008's orca facts limited to one callback) |
| 38 | **NEW** Every Natural Disaster Doug Could Survive, Until He Can't | places | Simple Paint "How to Survive Every Natural Disaster" 677K in 2.0 d (2.42x, 14,100 lifetime vph); "How To Survive Every Apex Predator" 514K (9 d); ROUNDUP "Weather moments but they get increasingly more terrifying" 8.34M (signals) | 8 | 10 (13,181) | 9 ("natural disasters" scores 10 but has kids/Roblox suggestions) | 10 ("what dying in every natural disaster feels like" 0; the 17 on "how to survive every natural disaster" are mostly Roblox/Minecraft, the only English competitor is Simple Paint) | 5 | **7.3** | backlog (**recommended ep 022**; T7 skeleton, not T1; science only, no 2026 events (Nepal floods, Hurricane Isaias); no lightning/Nyos (004) or frozen-Earth items (007)) |
| 42 | **NEW** Would the Hippo Survive Every Prehistoric Era? | prehistoric | Fossil "Would Orcas Dominate Every Prehistoric Ocean?" 2.66M (**92.1x**, 9.9 d); Fossil "How Long You'd Last in Every Prehistoric Era" 11.62M (402x) | 10 | 10 (7,287) | 9 ("prehistoric animals", 10-09) | 5 ("could today's animals survive prehistoric earth" 6) | 5 | **7.2** | backlog (new formula "Would X Survive/Dominate Every Era"; pays off 013's hippo; keep ≥3 episodes away from 019) |
| 33 | How Fast Doug Would Die in Every Prehistoric Era | prehistoric | Joe Bartolozzi "How Fast You'd Die In Every Prehistoric Era" 2.38M in 4.3 d (signals); Fossil "How Long You'd Last in Every Prehistoric Era" 11.62M (402x, vph_recent 1,694) | 10 | 10 (Fossil orcas 7,287; BTB prehistoric ocean 4,139) | 9 ("prehistoric animals") | 2 (10; BTB copied our 009 frame on 10-16) | 5 | **6.9** | backlog (crowded; overlaps 003/009; held to ≥10-31; #42 is the less crowded way into this engine) |
| 6 | Why the Mariana Trench Gets Deadlier the Deeper Doug Goes | ocean | BeyondTheBlue "Why We Can't Truly Explore the Mariana Trench" 1.55M (5.21x); "37 Minutes of Everything We Know About The Deepest Place on Earth" 1.13M (3.8x); "Why No One Talks About The Second Deepest Trench" 741K in 4 d | 8 | 10 (6,745) | 8 | 2 (11) | 5 | **6.4** | backlog (overlaps 001; T6 if made) |
| 40 | **NEW** What Rabies Does to Doug, Hour by Hour | parasites | Mr. Death "What Dying from Rabies Feels Like" 613K (signals); Bacterium "Every IMPOSSIBLE Virus That Actually Exists" 77K (10.9x) | 6 | 3 (412) | 9 ("rabies", partly vlog content) | 10 ("what rabies does to your body" 1) | 6 | **6.3** | backlog (timeline format, not T1; 011 mentions rabies once, so no overlap) |
| 44 | **NEW** Could Doug Survive Every Apex Predator? | animals | Simple Paint "How To Survive Every Apex Predator" 514K (1.84x, 9 d); Fossil "Could You Survive Every Prehistoric Apex Predator?" 405K (14.0x) | 8 | 4 (Simple Paint 846) | 10 ("apex predator") | 2 ("how to survive every apex predator" 10) | 6 | **6.1** | backlog (overlaps 011; only after #39) |
| 10 | The Deadliest Predator From Every Period of Earth's History | prehistoric | ExtinctZoo "The Deadliest Sea Animal From Every Single Period" 2.95M (3.65x); land version 2.25M (2.71x) | 8 | 4 (876) | 10 | 5 (6) | 5 | **6.0** | backlog (overlaps 009) |
| 20 | Doug vs. Prehistoric Earth: The Full Series (1.5 h) | compilations | Spinosnack "The Deeper You Look Into Fossils, The Scarier It Gets – The Movie" 1.17M (**9.81x**, 14.9 d); Paintify "Every Unexplored Place on Earth (Full Series)" 1.41M (5.09x, 1,028); BTB "37 Minutes…" 1.13M (3.8x, 2,194) | 8 | 8 (2,194) | 3 ("prehistoric full series" 1) | 5 ("prehistoric full series" 7, mostly film clips) | 5 | **5.9** | backlog (**cheap: no new script or art**; 003/005/007/009/015/019 once 019 is live on 10-19; was an ocean compilation, switched to prehistoric because that playlist has 6 episodes and the strongest Shorts) |
| 30 | Nothing About the Oarfish Is Normal | ocean | Mr. Science "Nothing about Oarfish Is Normal" 3.30M (2.43x); OctoLab "Nothing About Octopus Is Normal" 218K (3.3x) | 6 | 4 (833) | 8 | 10 (0) | 5 | **5.9** | backlog (T6) |
| 28 | Deep Sea Creatures That Shouldn't Exist | ocean | Bluntly Explained "Every Black Hole That Shouldn't Exist" 1.38M (8.6x); Curious Fing 1.52M (signals) | 8 | 3 (460) | 8 | 5 (7) | 5 | **5.6** | backlog |
| 26 | The Worst Prehistoric Deaths Doug Could Possibly Have | prehistoric | ExtinctZoo "Prehistoric Human Deaths That Make Stubbing Your Toe…" 1.89M (2.34x) | 6 | 4 (785) | 5 | 10 (2) | 5 | **5.6** | backlog (T5) |
| 19 | What a Parasite Does to You, Day by Day | parasites | Kurzgesagt 13.3M (style bible), superseded by #2/#8 | 4 | 1 | 9 | 10 (0) | 6 | **5.6** | backlog (reserve; #40 uses the same timeline format with a stronger engine) |
| 17 | Terrifying Animals You Should Be Glad Are Extinct | prehistoric | ExtinctZoo "Prehistoric Creatures You're Glad Are Extinct" 1.28M (1.6x) | 4 | 3 | 10 | 10 (0) | 5 | **5.5** | backlog |
| 43 | **NEW** The Most Disturbing Viruses Nature Ever Made | parasites | Bacterium "Every IMPOSSIBLE Virus That Actually Exists" 77K (10.9x, 7.7 d); their fungus/parasite versions 506K (71.5x) / 353K (49.8x) | 6 | 1 (8) | 3 (format phrase 0; topic not queried) | 10 ("the most disturbing viruses in nature" 2) | 6 | **5.4** | backlog (T4; Bacterium's 3rd category, so the "IMPOSSIBLE" frame travels; don't repeat 002/014 items) |
| 18 | Real Animal Diseases Worse Than Any Horror Movie | parasites | Casual Geographic 10M (style bible) | 4 | 3 | 9 | 5 (?) | 6 | **5.4** | backlog (reserve) |
| 13 | The Deadliest Man-Eating Animals in Recorded History | animals | Simple Paint "The Deadliest Man-Eaters to Ever Exist" 1.24M (5.3x) | 6 | 6 | 1 | 5 (8) | 6 | **5.4** | backlog |
| 12 | Every Way Nature Can Kill Doug, From Least to Most Painful | places | Simple Paint "The Most Horrifying Ways Nature Can Kill You" 928K (3.9x) | 6 | 3 | 3 | 10 (2) | 5 | **5.2** | backlog (overlaps #38) |
| 23 | The Deep Sea Iceberg Explained (1.5 h+) | compilations | quack doc icebergs 474K (8.8x); Snook 2.28M (style bible) | 6 | 3 | 8 | 5 (?) | 5 | **5.2** | backlog |
| 31 | Every Horrifying Place in the Ocean Doug Could Sink Into | ocean | Paintify "Every Horrifying Place In The Ocean" 596K (2.15x) | 5 | 1 (133) | 8 | 10 (0) | 5 | **5.2** | backlog (overlaps 001) |
| 7 | What Happens If You Fall Into Every Deadly Place on Earth | places | Paintify "Every Unexplored Place on Earth" 1.60M (5.79x) | 6 | 3 (214) | 7 | 2 (11) | 5 | **4.8** | backlog (largely covered by 004) |
| 21 | Disturbing Ocean Facts That Will Ruin Your Day | ocean | Autocomplete phrasing only (unproven) | 2 | 1 | 8 | 5 (?) | 5 | **4.1** | backlog |

Considered and not added (10-17 signals): "mosquito" (demand 10 but results are 100% kids' songs), "zombie animals" (kids' content), "deadliest lake" (Nyos already in 004, interest median 50 vph),
"tsunami" (demand and vph driven by 2026 news and Minecraft; folded into #38).

## Published / in-production history (pre-publish score kept, results added)
Results are to 10-17 [F]: day-7 views (interpolated), lifetime views, thumbnail impressions + CTR (`reach`, through 10-15), AVD (28-day window).
| # | Title (episode) | Playlist | Formula | Engine | Pre-pub score | Status / result |
|---|---|---|---|---|---|---|
| 1 | How Doug Would Die in Every Layer of the Ocean (001) | ocean | T2 | Mr. Science depth gradient 17.05M (13.0x) | 7.4 | published 09-30, 9eiX84Ik1Sc · day-7 **4.4** (strike) · 19 lifetime · 203 imp, 5.4% CTR · AVD 128 s |
| 2 | What Dying From Every Parasite Would Feel Like (002) | parasites | T1 | quack doc "Every Deadly Disease" 5.63M (103.9x) | 8.7 | published 10-01, xra1KWBfC7A · day-7 **6.8** · 29 lifetime (most of any long video) · 106 imp, 4.7% · AVD 326 s |
| 5 | How Doug Would Die in Every Mass Extinction (003) | prehistoric | T2 | Mr. Science deep time 4.07M; Fossil every era 8.98M | 8.6 | published 10-02, AcL4RwsVa_w · day-7 **4.0** (strike) · 7 lifetime · 35 imp, 5.7% · AVD 426 s |
| 4 | What Dying in Every Deadly Place on Earth Would Be Like (004) | places | T1 | Simple Paint worst places in space 1.91M (8.06x) | 6.7 | published 10-03, _fudGWs5yJU · day-7 **4.5** (strike) · 9 lifetime · 93 imp, 0% · AVD 244 s · quicksand Short 1,225 |
| 15 | The Creepiest Fossils That Still Look Alive (005) | prehistoric | T4 | ExtinctZoo roadkill fossils 4.22M (5.1x) | 8.1 | published 10-04, lgpGaCCrv3Q · day-7 **10.0** · 15 lifetime · 31 imp, 0% · AVD 246 s · foal Short 1,120, bison 1,068 |
| 16 | The Most Disturbing Discoveries at Every Depth of the Ocean (006) | ocean | T3 | PE anomalies Pt. 2 4.71M (6.64x) | 7.1 | published 10-05, wIjpa2amtsw · day-7 **11.2** (best) · 12 lifetime · 21 imp · AVD 401 s · blue hole Short 1,136 |
| 24 | What Dying Every Time Earth Froze Would Be Like (007) | prehistoric | T1 | Mr. Science "When Earth Had Supermountains" 2.62M | 8.0 | published 10-06, SAcFbGY0KBg · day-7 **3.3** (strike) · 6 lifetime · 35 imp, 2.9% · AVD 509 s · 2 Shorts ≥1,032 |
| 11 (+25 absorbed) | How Every Step of the Ocean Food Chain Would Kill Doug (008) | ocean | T2 | BTB fear chain 2.61M (8.1x); OctoLab orca 7.63M | 6.6 (#25: 7.0) | published 10-07, QTOdC67HcZY · day-7 **6.3** (strike) · 9 lifetime · 38 imp, 2.6% · AVD 253 s · orca Short 1,411 (best), trevally 1,012 |
| 3 | What Dying in Every Prehistoric Ocean Would Be Like (009) | prehistoric | T1 | Fossil "Every Prehistoric Era" 10.82M (469x) | 6.9 → 7.8 (10-09) | published 10-09, wbBQSRcTLGU · day-7 **8.8** · 10 lifetime · 88 imp, 1.1% · AVD 538 s |
| 14 | How Every Deadly Venom Would Kill Doug (010) | animals | T2 | quack doc "Every Deadly Disease" 6.10M (83.9x) | 8.3 | published 10-10, jX15nlPn0WE · day-7 **11.0** · 101 imp, 1.0% · AVD 6 s (5 search viewers left after 10 s) |
| 32 | Every Animal Doug Could Beat in a Fight, Until He Dies (011) | animals | T7 | Fossil "Which Human Species Could You Beat in a Fight?" 1.11M (48.3x) | 8.8 | published 10-11, Df1Lh4okCsk · 18 views at day 6 (fastest start) · 87 imp, 1.1% · AVD 14 s (all 5 window views from search) |
| 34 | What Dying in Every Natural Trap Would Be Like (012) | places | T1 | Simple Paint "Most Horrifying Ways People Got Trapped" 2.64M (9.8x) | 7.0 | published 10-12, stnN_nfr0gQ · 2 views at day 5 · 37 imp, 0% (likely T1's 3rd strike at day 7) |
| 35 | Why Hippos Get Deadlier the Closer Doug Gets (013) | animals | T6 | OctoLab polar bear 2.77M (46.6x) / walrus 2.49M (41.9x) | 8.4 | published 10-13, NyDbJUUWj0M · 4 views at day 4 · 60 imp, 1.7% |
| 8 | What Dying From Every Brain Parasite Would Feel Like (014) | parasites | T1 | Bacterium "Every IMPOSSIBLE Parasite…" 344K (37.6x) | 6.5 | published 10-14, fBb8dNJZl8s · 14 views at day 3 · 137 imp (108 on day 1), 2.2% · AVD 14 s |
| 36 | The Deeper Doug Digs, the Scarier the Fossils Get (015) | prehistoric | T6 | Spinosnack "The Deeper You Look Into Fossils…" 406K (3.76x) | 7.0 | published 10-15, Jq-QkuNetWU · 4 views at day 2 · 46 imp on day 1 |
| 29 | What Dying at Every Depth Under Antarctica Would Be Like (016) | places | T1 | Mr. Science "When Antarctica Was a Jungle" 4.42M (3.4x) | 6.1 | published 10-16, 0BLUItULl8I · 2 views at day 1 |
| 9 | The Most Disturbing Fungi Scientists Have Ever Found (017) | parasites | T4 | Bacterium "Every IMPOSSIBLE Fungus…" 428K (44x) | 6.4 | published 10-17 16:00Z, RKLHNVqC5OA |
| 37 | Every Reason the Cassowary Is the Most Terrifying Bird Alive (018) | animals | T8 | OctoLab "Why Nobody Talks About The Second Biggest Animal" 797K (13.4x) | 6.5 | uploaded, scheduled 10-18 16:00Z, WqT0axnzOP4 |
| 27 | The Creepiest Prehistoric Animals Scientists Drew All Wrong (019) | prehistoric | T4 | ExtinctZoo "The Extinct Animals That Never Were" 1.20M (1.45x) | 6.8 | uploaded, scheduled 10-19 16:00Z, shkSsjg9278 |
| 22 | Why the Ground Gets Deadlier the Deeper Doug Goes (020) | places | T6 | Mr. Science depth gradient 17.05M; Spinosnack fossils 406K | 6.4 | uploaded, scheduled 10-20 16:00Z, YDF-ckpVZf0 |

Formula strike count (day-7 views below the channel median of 6.6; rule = drop at 3): **T2 3 = dropped** (001, 003, 008; 010 above) · T1 2 (004, 007; 002, 009 above; 012/014/016 pending) · T3 0 · T4 0 · T6/T7/T8 not yet at day 7.
