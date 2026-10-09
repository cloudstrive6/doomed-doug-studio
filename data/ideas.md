# Idea backlog (ranked by the growth analyst)

Score = expected views/speed (1–10). "Engine" = the proven outlier formula it borrows. Views, outlier_x and vph come from
`data/competitors/2026-10-09.json` unless marked "signals" (`python -m studio signals`, `data/signals/2026-10-09.json`; older
rows may cite `2026-10-01.json`) or "style bible". Status: backlog / in-production / published. Never delete published rows.
Last re-rank: 2026-10-09 (memo `data/insights/2026-10-09.md`).

**Scoring: weights moved to the "≥3 episodes with 7-day data" tier** (eps 001–003 are past day 7):
Score = 0.30 Eng + 0.20 Interest + 0.15 Demand + 0.10 Sat + 0.25 Own, each component 0–10.
- **Eng:** 10 = ≥5M or ≥10x on ≥1M; 8 = 2–5M at ≥3x or repeated hits; 6 = ~0.5–1.5M or a small-channel ≥5x; 4 = weak (<2x) or style bible only; 2 = unproven.
- **Interest:** best `vph_recent` of the engine video(s) (signals `vph_best` or median where the engine isn't watched): ≥3000 = 10, 2000+ = 8, 1000+ = 6, 500+ = 4, 200+ = 3, <200 = 1.
- **Demand:** the `signals` demand score for the TOPIC query. Where the autocomplete is polluted by games or kids' content, the score is lowered and the reason noted.
- **Sat:** `signals` recent 100K+ copies for the FORMAT phrase: ≤3 = 10, 4–8 = 5, 9+ = 2. `?` = not queried yet (scored 5).
- **Own (per playlist, 10-09)** [inference from small samples, deliberately held to the 3–7 range until views pass 3 digits]:
  parasites **7** (ep 002 has the best long video: 8 views, 6.7% CTR, 241 s AVD; Shorts average 612 views), places **6** (Lake Natron Short 601),
  prehistoric **5** (003/005/007 have 4/8/1 long views; bison Short 1,069, extinction Shorts 14–29), ocean **3** (001/006/008 have 6/0/0 long views; Shorts average 59),
  animals* / compilations **5** (no data).

Playlist keys: ocean, parasites, prehistoric, places, compilations. `animals*` = proposed "Doug vs. Animals". The 10-09 memo asks the creative director
to create it, because the top 3 ideas sit there.

## Ranked backlog
| # | Working title | Playlist | Engine (proven outlier) | Eng | Interest (vph) | Demand | Saturation (format) | Own | Score | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| 32 | **NEW** Every Animal Doug Could Beat in a Fight (Ranked) | animals* | Fossil "Which Human Species Could You Beat in a Fight?" 1.11M (48.3x, 25 d) | 10 | 10 (3,245) | 10 ("animal fight") | 10 ("which animal could you beat in a fight" 2) | 5 | **8.8** | backlog (recommended ep 011) |
| 35 | **NEW** Hippos Are Terrifying… Here's Why | animals* | OctoLab "Why Polar Bears Are The Weirdest Apex Predator" 2.77M (46.6x, 9.4 d) + "Walruses Are Terrifying… Here's Why" 2.49M (41.9x); KPassionate cocaine-hippo 5.14M (signals) | 10 | 8 (hippo topic best 8,140; OctoLab 1,064) | 10 ("hippo", partly kids' content) | 10 (0) | 5 | **8.4** | backlog (single-animal format test; follow-up to #32) |
| 14 | What Dying From Every Venom Would Feel Like | animals* | T1 frame: quack doc "Every Deadly Disease" 6.10M (83.9x), genetic disease 486K (6.7x), drug overdose 165K in 2.4 d; Simple Paint poison | 10 | 10 (quack doc overdose 3,259) | 7 ("venomous animals") | 10 (0) | 5 | **8.3** | backlog (**recommended ep 010**; the ep 002 day-7 hold has expired) |
| 33 | **NEW** How Fast Doug Would Die in Every Prehistoric Era | prehistoric | Joe Bartolozzi "How Fast You'd Die In Every Prehistoric Era" 2.38M in 4.3 d (signals); Fossil "How Long You'd Last in Every Prehistoric Era" 10.82M (469x) | 10 | 10 (22,963 / 8,818) | 9 ("prehistoric animals") | 2 (10) | 5 | **7.8** | backlog (crowded and overlaps 003/009; space it ≥3 weeks after 009) |
| 34 | **NEW** Every Way Nature Could Trap Doug | places | Simple Paint "The Most Horrifying Ways People Got Trapped" 2.64M (9.8x, 7.4 d, 14,948 lifetime vph) | 8 | 6 (1,043) | 6 ("trapped" scores 10 but is Minecraft-polluted) | 10 (0) | 6 | **7.0** | backlog (caves, crevasse, tar pit, sinkhole, mudflat, tidal flat) |
| 36 | **NEW** The Deeper Doug Digs Into Fossils, the Scarier They Get | prehistoric | Spinosnack "The Deeper You Look Into Fossils, The Scarier It Gets" 406K (3.76x, 6.2 d); series 1.03M; Mr. Science depth gradient 17M | 6 | 8 (2,604) | 9 ("fossils") | 10 (1) | 5 | **7.0** | backlog (T6; overlaps 005, so use different specimens) |
| 10 | The Deadliest Predator From Every Period of Earth's History | prehistoric | ExtinctZoo "Earth's Deadliest Predator From Every Single Period" 2.25M (2.71x) + sea version 2.78M (3.35x) | 8 | 6 (1,138) | 10 | 5 (6) | 5 | **6.9** | backlog (overlaps 009) |
| 27 | The Prehistoric Animals Scientists Drew Completely Wrong | prehistoric | ExtinctZoo "The Extinct Animals That Never Were" 1.20M (1.45x, 10.4 d) | 6 | 6 (1,697) | 10 ("extinct animals") | 10 (0) | 5 | **6.8** | backlog |
| 8 | What Dying From Every Brain Parasite Would Feel Like | parasites | Bacterium "Every IMPOSSIBLE Parasite…" 344K (37.6x); Mr. Death brain-eating amoeba 285K (signals); **our Naegleria Short 1,100 (best on channel)** | 6 | 3 (392) | 9 ("brain eating amoeba") | 10 (2) | 7 | **6.5** | backlog (T1; space from ep 002, which shares Naegleria) |
| 37 | **NEW** Why Nobody Talks About the Cassowary | animals* | OctoLab "Why Nobody Talks About The Second Biggest Animal on Earth" 797K (13.4x) | 6 | 4 (cassowary median 561) | 9 ("cassowary") | 10 (2) | 5 | **6.5** | backlog |
| 9 | The Most Disturbing Fungi Scientists Have Ever Found | parasites | Bacterium "Every IMPOSSIBLE Fungus…" 428K (44x), Pt. 2 105K (16.3x); our zombie-ant Short 692 | 6 | 3 (fungus median 961; Bacterium 98) | 8 ("fungus") | 10 (1) | 7 | **6.4** | backlog |
| 22 | The Deeper Doug Digs Into Earth, the Creepier It Gets | places | Depth gradient: Mr. Science 17.05M; Spinosnack fossils 406K (2,604 vph) | 6 | 8 (2,604) | 3 (?) | 10 (?) | 6 | **6.4** | backlog |
| 6 | Why the Mariana Trench Gets Deadlier the Deeper Doug Goes | ocean | BeyondTheBlue "Why We Can't Truly Explore the Mariana Trench" 1.44M (4.34x); "Nothing About The Mariana Trench Is Normal" 2.63M | 8 | 8 (2,072) | 8 | 2 (11) | 3 | **6.2** | backlog (overlaps 001) |
| 29 | What Doug Would Find Under Antarctica's Ice | places | Mr. Science "When Antarctica Was a Jungle" 4.42M (3.4x); Spinosnack Mediterranean 468K (5.59x) | 8 | 6 (1,938) | 5 | 2 (10) | 6 | **6.1** | backlog |
| 26 | The Worst Prehistoric Deaths Doug Could Possibly Have | prehistoric | ExtinctZoo "Prehistoric Human Deaths That Make Stubbing Your Toe…" 1.71M (2.06x) | 6 | 6 (1,618) | 5 | 10 (2) | 5 | **6.0** | backlog (T5) |
| 20 | Doug vs. the Ocean: Full Series (1 Hour) | compilations | Paintify "Every Unexplored Place on Earth (Full Series)" 1.25M (4.63x) | 6 | 6 (1,067) | 8 | 5 (?) | 5 | **6.0** | backlog (now possible: 001+006+008; consider a prehistoric compilation of 003/005/007/009 instead, since ocean is our weakest playlist) |
| 28 | Deep Sea Creatures That Shouldn't Exist | ocean | Bluntly Explained "Every Black Hole That Shouldn't Exist" 1.29M (7.94x); Curious Fing 1.52M (signals) | 8 | 4 (451) | 8 | 5 (7) | 3 | **5.7** | backlog |
| 30 | Nothing About the Oarfish Is Normal | ocean | Mr. Science oarfish 3.04M (2.32x); OctoLab "Nothing About Octopus Is Normal" 183K (3.07x) | 6 | 4 (579) | 8 | 10 (0) | 3 | **5.6** | backlog (T6) |
| 17 | Terrifying Animals You Should Be Glad Are Extinct | prehistoric | ExtinctZoo "Prehistoric Creatures You're Glad Are Extinct" 1.28M (1.6x) | 4 | 3 | 10 | 10 (0) | 5 | **5.6** | backlog |
| 19 | What a Parasite Does to You, Day by Day | parasites | Kurzgesagt 13.3M (style bible), superseded by #2/#8 | 4 | 1 | 9 | 10 (0) | 7 | **5.5** | backlog (reserve) |
| 18 | Real Animal Diseases Worse Than Any Horror Movie | parasites | Casual Geographic 10M (style bible) | 4 | 3 | 9 | 5 (?) | 7 | **5.4** | backlog (reserve) |
| 12 | Every Way Nature Can Kill Doug, From Least to Most Painful | places | Simple Paint "The Most Horrifying Ways Nature Can Kill You" 928K (3.9x) | 6 | 3 | 3 | 10 (2) | 6 | **5.4** | backlog |
| 23 | The Deep Sea Iceberg Explained (1.5 h+) | compilations | quack doc icebergs 474K (8.8x); Snook 2.28M (style bible) | 6 | 3 | 8 | 5 (?) | 5 | **5.4** | backlog (around upload 12–15) |
| 7 | What Happens If You Fall Into Every Deadly Place on Earth | places | Paintify "Every Unexplored Place on Earth" 1.55M (5.97x) | 6 | 3 (214) | 7 | 2 (11) | 6 | **5.2** | backlog (largely covered by 004) |
| 31 | Every Horrifying Place in the Ocean Doug Could Sink Into | ocean | Paintify "Every Horrifying Place In The Ocean" 512K (1.97x) | 5 | 3 (378) | 8 | 10 (0) | 3 | **5.1** | backlog (overlaps 001) |
| 13 | The Deadliest Man-Eating Animals in Recorded History | animals* | Simple Paint "The Deadliest Man-Eaters to Ever Exist" 1.24M (5.3x) | 6 | 6 | 1 | 5 (8) | 5 | **4.9** | backlog |
| 21 | Disturbing Ocean Facts That Will Ruin Your Day | ocean | Autocomplete phrasing only (unproven) | 2 | 1 | 8 | 5 (?) | 3 | **3.3** | backlog |

## Published / in-production history (pre-publish score kept, results added)
| # | Title (episode) | Playlist | Formula | Engine | Pre-pub score | Status / result to 10-09 [F] |
|---|---|---|---|---|---|---|
| 1 | How Doug Would Die in Every Layer of the Ocean (001) | ocean | T2 | Mr. Science depth gradient 17.05M (13.0x) | 7.4 | published 09-30 01:00Z, 9eiX84Ik1Sc · 6 views at day 9 · 121 imp, 2.5% CTR · AVD 27 s |
| 2 | What Dying From Every Parasite Would Feel Like (002) | parasites | T1 | quack doc "Every Deadly Disease" 5.63M (103.9x) | 8.7 | published 10-01 16:00Z, xra1KWBfC7A · 8 views at day 8 (**best long video**) · 45 imp, 6.7% CTR · AVD 241 s (24.6%) |
| 5 | How Doug Would Die in Every Mass Extinction (003) | prehistoric | T2 | Mr. Science deep time 4.07M; Fossil every era 8.98M | 8.6 | published 10-02 16:00Z, AcL4RwsVa_w · 4 views at day 7 · 18 imp, 5.6% CTR · AVD 240 s |
| 4 | What Dying in Every Deadly Place on Earth Would Be Like (004) | places | T1 | Simple Paint worst places in space 1.91M (8.06x) | 6.7 | published 10-03 16:00Z, _fudGWs5yJU · 4 views at day 6 · 66 imp, 0% CTR · AVD 98 s |
| 15 | The Creepiest Fossils That Still Look Alive (005) | prehistoric | T4 | ExtinctZoo roadkill fossils 4.22M (5.1x) | 8.1 | published 10-04 16:00Z, lgpGaCCrv3Q · 8 views at day 5 · 19 imp, 0% CTR · bison Short 1,069 |
| 16 | The Most Disturbing Discoveries at Every Depth of the Ocean (006) | ocean | T3 | PE anomalies Pt. 2 4.71M (6.64x) | 7.1 | published 10-05 16:00Z, wIjpa2amtsw · 0 views in analytics at day 4 · 9 imp |
| 24 | What Dying Every Time Earth Froze Would Be Like (007) | prehistoric | T1 | Mr. Science "When Earth Had Supermountains" 2.62M | 8.0 | published 10-06 16:00Z, SAcFbGY0KBg · 1 view at day 3 · 2 imp |
| 11 (+25 absorbed) | How Every Step of the Ocean Food Chain Would Kill Doug (008) | ocean | T2 | BTB fear chain 2.61M (8.1x); OctoLab orca 7.63M | 6.6 (#25: 7.0) | published 10-07 16:00Z, QTOdC67HcZY · 0 views in analytics at day 2 |
| 3 | What Dying in Every Prehistoric Ocean Would Be Like (009) | prehistoric | T1 | Fossil "Every Prehistoric Era" 10.82M (469x); ExtinctZoo sea animal every period 2.78M | 6.9 → **re-scored 7.8** on 10-09 (Eng 10, Interest 10 from BTB copy 12,114 / Fossil orcas 12,217 vph, Demand 7, Sat 5, Own 5) | published (scheduled 10-10 16:00Z, wbBQSRcTLGU) · 3 Shorts still need Related links (`shorts pending`) |

Formula strike count (day-7 long views below the channel median of 6, rule = drop at 3): T1 0 · T2 1 (003) · T3/T4 not yet at day 7.
