# Facts: 012 What Dying in Every Natural Trap Would Be Like (working)

Every factual claim in script.md is listed here with its source. Fiction and framing are not claims. That covers Doug, his deaths,
the suitcase and stickers, the cap, the costumes, the speech bubbles, "picnic spot", "the better skier", "the sticker had already
been printed", "the costume department", "match the decor" and the hotel "stay" headers. Everyday comparisons are marked
"common knowledge" and checked by arithmetic.

Checked 2026-10-09 (draft 1); updated for draft 2 per script_review.md fixes 1-10 (see "Draft 2 changes" below), and for draft 3 per the draft 2 review (see "Draft 3 changes"). "Verified" means I read the claim on the page with WebFetch or a public API. "Search snippet" means
the page blocked WebFetch or was an image or scanned PDF, so the claim was confirmed only through search-result text that quotes the
page. The screener should re-open those if possible.

**Safety-advice check:** nothing in the script tells anyone how to avoid or escape a trap. I cut these on purpose: ski with a partner,
tree-well "don't struggle" advice, NPS "get to high ground", "check the forecast" and "tell someone your route", avalanche beacons, air
pockets and rescue windows framed as advice, crevasse probes and roping up, and La Brea's fences framed as warnings. The 18-minute
avalanche figure is a study result about survival odds, not an instruction. Doug's "checking the sky" beat shows that looking up does
NOT help; it is not a tip.
**Real victims:** Antelope Canyon 1997 (date and count only), Tsanfleuron 2017 (year missing, year found, the director's crevasse quote),
the Valais missing list (a count only) and Altamura (dates only). I did NOT use names, ages, nationalities, families, the condition of
remains, objects found with the bodies, or the sole survivor. There are no jokes in these fact lines. Doug beats come after them and are
about Doug.
**Children check:** the La Brea "many of the bison were young" detail is not used. No children appear anywhere.
**Myanmar amber:** not used. The only amber specimens are the Triassic Dolomites droplets (Schmidt et al. 2012). The general behaviour
line ("catching prey, laying eggs, hatching") is sourced to Dominican-amber and general reviews, not Burmese specimens.

## Draft 3 changes (script_review.md, draft 2 review)
1. **F1, Dead Sea kicker:** "the holes keep coming, at a rate of around four hundred new ones every year" became "The sea is still
   shrinking, and by twenty fifteen around four hundred new holes were being reported every year." The figure is now dated to its
   source year, NBC News 2015. No current rate is claimed. The screener pointed to newer mapping that suggests a lower rate today:
   702 new sinkholes on the western shore from 2005 to 2021 (Gutiérrez et al. 2023), and about 500 at Ghor Al-Haditha from 2018 to 2022
   (EGU23-13530). Neither is used. "The sea is still shrinking" is sourced to current reporting: the State Comptroller via Ynet, about 1.15 m a year, and a 2026 Water review.
2. **Rule 4, Slot Canyon kicker:** now "Nobody ever said the water was finished with it." That is 9 words, and the joke is unchanged.
   No new claim.
3. **Rule 9, Flesch:** 30 short sentence pairs in mechanism and fact passages were merged. Gag lines are unchanged ("Doug has died.
   Again.", "Doug is fine.", the section headers and the item names). Measured with textstat 0.7.13 `flesch_reading_ease` on spoken text
   only (HTML comments, markdown headings and bracketed stage directions removed). Draft 2 measured 73.7 on the same meter, which
   matches the screener. Draft 3 measures **70.8**, with 174 sentences averaging 16.9 words, a 33-word maximum and 2,949 words. The merges
   only reword. Three rewordings touch a claim row, and each source still covers it: Dead Sea "blamed on the mineral industry"
   (same NBC 2015 statement), Altamura "scientists decided that moving the skeleton could cause damage" (IFLScience, irreparable damage)
   and the Altamura reveal "someone had got there first, a Neanderthal".
4. **Advisory, avalanche:** the 18-minute line stays in the past tense ("survival odds dropped steeply after about eighteen minutes")
   and stays attributed to one Swiss study. The 2024 JAMA Network Open update, which shortens the over-90% phase to about 10 minutes,
   is noted under the flagged items. The line is not made present tense.

Advisories not applied: Brinicle is 329 words (target 290-320) and Amber is 425 (target 380-420), each a few words over.
The brinicle size analogy is also unchanged, because there is still no source for the length.

## Draft 2 changes (script_review.md)
1. **F1 opener:** "Most hold you for minutes" became "Some hold you for minutes". Only the tree well and slot canyon act in minutes.
2. **Hook:** the twist ("No avalanche. No cliff. No storm. The tree built this trap...") moved up behind the marker "Notice what is missing."
   It now ends at spoken word 141 (the limit is 145). No change to facts.
3. **F2 Dead Sea level:** the claim is now time-boxed: "Between nineteen eighty and twenty fifteen, its surface dropped by about
   thirty meters". This matches NBC 2015's "about 100 feet since 1980" exactly. No present-tense total is claimed, so no 2025 level
   source is needed. Supporting rate: the Ministry of Environmental Protection 2015 report (via Globes) gives 1.2 m a year by then, so
   "roughly one meter a year" is a fair average over 1980-2015.
4. **F3 thirty percent:** the attribution to a GSI geologist is removed. The script now says "About thirty percent of the drop has been
   blamed on mineral extraction", and the source is NBC 2015 as reporting.
5. **F4 sinkhole count:** "As many as five thousand" became "More than five thousand". Source: Israel's Ministry of Environmental
   Protection, about 5,500 by 2015 (Globes). NOT used: the 2019 Solid Earth preprint (more than 6,000), because its authors have
   **withdrawn** it (copernicus page, verified).
6. **F5 dire wolf count:** the count is CUT. The script keeps only "the single most common large animal dug out of the asphalt is the
   dire wolf". Sources disagree on "individuals" against "specimens", and the NHM count PDF is an image I can't read.
7. **F6 mite size:** now "about a fifth of a millimeter long, roughly the width of two human hairs". *Triasacarus* is 210 microns long,
   about 0.2 mm, which Live Science compares to twice a hair's diameter.
8. **F7 Altamura DNA:** now "one of the oldest Neanderthals ever to give up genetic material". Sima de los Huesos (about 430,000 years,
   Meyer et al. 2016, *Nature*) is older.
9. **Rule 14:** "The most disturbing part is" was replaced with "This is where it gets slow." That marker is used only once.
10. **Rule 4:** the Tree Well kicker is now 22 words ("Over nine American winters...").

Advisories applied: "car park" became "parking lot" and "football pitch" became "football field". La Brea is now "more than six
hundred species". The Dead Sea STAY tag is now "UNTIL SOMEONE LOOKS DOWN". The NCEI Storm Events record ID was added for the 1997
flood. Draft 2 reported Flesch as 71.8 from a rough syllable count; superseded by the draft 3 textstat measurement. NOT applied: the brinicle size analogy. No source gives the filmed brinicle's length, so the temperature
comparison stays.

## Flagged items from the brief (status)
- **Tree well 90% experiment:** kept, but the original experiment reports were not found. deepsnowsafety.org (a collaboration that
  includes the Northwest Avalanche Institute) states it directly, and Wikipedia says "two experiments conducted in North America".
  The script says "two supervised experiments in North America" and "nine out of ten". The screener may want a primary source.
- **Tree well death count:** the brief asked for a count with a year range. I used Wikipedia's "nine-year US period, two thirds of
  snow immersion suffocation deaths were in tree wells" as the kicker, NOT a per-season count. An earlier draft line ("about four a
  season") was cut, because the Baugher 2012 ISSW paper is a scanned PDF I could not read.
- **Antelope Canyon water rise "within minutes":** no figure specific to 1997 is used. The "within minutes" claim is the general NPS
  statement about slot-canyon flash floods. The wall-of-water height, three to nine meters (10-30 ft), is from the NOAA/NCDC narrative,
  read through a site that reproduces it (usdeadlyevents.com). I could not open the NOAA database directly.
- **Brinicle growth time:** "about five or six hours" is the cameraman's own figure (quoted on geogarage, reproducing the BBC report).
- **Avalanche speed:** "about one hundred and thirty kilometers an hour" is the "up to 80 miles an hour" quote from a Kachina Peaks
  Avalanche Center forecaster (80 mph is about 129 km/h). The brief's "130 km/h or more" is not claimed; the script says "about".
- **Avalanche survival figure:** this is Brugger et al. 2001, published in *Resuscitation*, not *Nature*. Survival in 638
  complete burials in open areas drops from 91% at 18 min to 34% at 35 min. Only "dropped steeply after about eighteen minutes" is
  spoken. Note: a 2024 JAMA Network Open update, with Brugger as co-author, shortened the over-90% phase to about 10 minutes (per the screener). The script attributes the 18-minute figure to "a Swiss study",
  which is accurate for that study.
- **Avalanche debris weight:** the brief suggested a car or a piano. Measured debris density is about 300 kg per cubic meter (Maseguchi)
  and 200-560 kg per cubic meter in distal deposits. "Around three hundred kilograms" equals about four adults at about 75 kg each.
- **Dead Sea rate:** the brief's "more than about 1 m a year" is not claimed. The GSI geologist's figure is about 100 ft since 1980,
  "a rate of three feet a year" (NBC 2015). Draft 2 says "between nineteen eighty and twenty fifteen... about thirty meters", which is roughly one meter a
  year. A kitchen counter is about 0.9 m tall (common knowledge).
- **Dead Sea sinkhole count:** superseded in draft 2; see change 5 above.
- **La Brea thin-layer depth:** CUT. No source gives a depth.
- **La Brea carnivore share:** Smithsonian prints "roughly 90 percent of the mammal fossils found are predators", and the museum says
  "the majority". The script uses Smithsonian's figure.
- **La Brea duration:** "the last fifty thousand years" is from the museum's own collections page. Smithsonian says seepage began
  "some 40,000 years ago". The script says "roughly the last fifty thousand years" for the fossil record and "tens of thousands of
  years" for the restocking trap, which is true under both figures.
- **Altamura "never removed":** corrected. The skeleton has stayed in the cave, but a fragment of the right scapula was taken out
  (Lari 2015). The script says the shoulder-blade piece is "the only part that has ever left the cave".
- **Amber "older than most dinosaurs":** reworded to "the earliest dinosaurs had only just appeared" (Martínez et al. 2011, *Science*:
  earliest dinosaurs about 230 Ma, mid-Carnian). Pangaea was still whole: USGS dates the breakup to 225-200 Ma.
- **DNA in amber:** not mentioned.
- **Bog option:** not used.

## Opener
| Claim | Source |
|---|---|
| One trap holds you for about 230 million years (amber) | See Amber below (Schmidt et al. 2012) |
| "Some hold you for minutes": tree well and slot canyon act in minutes | Tree well and slot canyon rows below (NPS: "within minutes or even seconds") |

## 1. Tree Well
| Claim | Source |
|---|---|
| Lower conifer branches shelter the trunk area from snowfall, so snow doesn't build up near the trunk; a well of loose, low-density snow forms around it | Wikipedia, Tree well: "A tree's branches shelter the area around its trunk from snowfall" (verified) https://en.wikipedia.org/wiki/Tree_well ; Last Frontier Heliskiing: "the branches at the lower reaches of the tree tend to prevent snow from accumulating around the trunk" (verified) https://www.lastfrontierheli.com/news/treewell-dangers-what-you-need-to-know/ |
| The branches can hang over and hide the well; the surrounding snow is loose and doesn't hold a climber | Wikipedia, Tree well (verified, as above); Ski Utah summary via search snippet https://www.skiutah.com/blog/authors/lexi/tips-on-tree-well-safety-for-skiers |
| Wells observed as deep as about 6 m | Wikipedia, Tree well: "observed as deep as 20 ft (6 m)" (verified). Analogy: a front door is about 2 m, so three doors is about 6 m (common knowledge) |
| People often fall in head first | Wikipedia: "Frequently victims fall into wells head-first" (verified); Whitefish Pilot, quoting Paul Baugher (NW Avalanche Center): "falls headfirst into the pit" (verified) https://whitefishpilot.com/news/2011/jan/12/expert-tree-wells-remain-unsung-hazard-9/ ; deepsnowsafety.org: "usually headfirst" (verified) https://deepsnowsafety.org/what-is-a-snow-immersion-suffocation/ |
| Two supervised experiments in North America; 90% of volunteers placed in tree wells could not get themselves out; experts were on hand | deepsnowsafety.org: "90% of people involved in tree well / SIS hazard research experiments could not rescue themselves" (verified, URL above); Wikipedia: "two experiments conducted in North America, 90% of volunteers temporarily placed in tree wells were unable to rescue themselves" (verified); PDX Monthly, experts on hand (search snippet) https://www.pdxmonthly.com/travel-and-outdoors/2010/04/tree-wells-040110 |
| The danger is highest during and just after a heavy snowstorm | Wikipedia, Tree well (search snippet and fetch): "risk is greatest during and immediately following a heavy snowstorm" |
| In one nine-year US period, about two thirds of snow immersion suffocation deaths were in tree wells | Wikipedia, Tree well (verified): "In a nine-year U.S. period, two-thirds of people who suffocated in snow immersion died in tree wells" |

## 2. Slot Canyon
| Claim | Source |
|---|---|
| Slot canyons are cut by water and are much deeper than they are wide | Wikipedia, Slot canyon https://en.wikipedia.org/wiki/Slot_canyon (search result); NPS Zion, flash floods (verified) https://www.nps.gov/zion/planyourvisit/flash-flood.htm |
| Antelope Canyon is about 37 m (120 ft) deep at its deepest | Wikipedia, Antelope Canyon: "about 120 feet (37 m)" (verified) https://en.wikipedia.org/wiki/Antelope_Canyon ; Showcaves: "at some points 36 m deep" (verified) https://www.showcaves.com/english/usa/gorges/Antelope.html . Analogy: about 3 m a story, so 12 stories is about 36 m (common knowledge) |
| In places only a few meters wide; "narrower than a living room" | Showcaves: "only a few meters wide" (verified). A living room is about 4-5 m wide (common knowledge) |
| Dry most of the year; floods after rare rains | Showcaves: "dry most of the year, but sometimes after one of the rare rains it floods" (verified) |
| Slot canyons gather runoff from a wide area, sometimes miles away | NPS Zion: floods "often caused by storms miles away" (verified); Ropewiki flash flood (search snippet) https://ropewiki.com/Flash_flood |
| NPS: flash floods often come from storms miles away, can happen under sunny skies, and can rise within minutes | NPS Zion: "often caused by storms miles away"; "even with sunny skies overhead"; "rises quickly, within minutes or even seconds" (verified) |
| 12 August 1997: a thunderstorm a few miles upstream sent a flash flood through Lower Antelope Canyon; 11 people died | Wikipedia, Antelope Canyon: "On August 12, 1997, eleven tourists… killed in Lower Antelope Canyon by a flash flood"; storm "7 miles (11 km) upstream" (verified). NOAA/NCDC Storm Events narrative: storm "3 to 5 miles upstream" (reproduced at https://usdeadlyevents.com/?p=1507, search snippet). The script says "a few miles", which covers both |
| Very little rain fell on the canyon that day | Wikipedia, Antelope Canyon: "Very little rain fell at the site that day" (verified) |
| The official weather record describes a wall of water 3-9 m high | NOAA NCEI Storm Events Database, Coconino County AZ, 12 Aug 1997, event ID 5611379 (older NCDC ID 282022): "a 10-30 foot wall of water" https://www.ncdc.noaa.gov/stormevents/eventdetails.jsp?id=5611379 (database not reachable from here; narrative confirmed via the reproduction at https://usdeadlyevents.com/?p=1507 and by the screener). 10-30 ft is 3.0-9.1 m |
| The Navajo name for the upper canyon means "the place where water runs through rocks" | Showcaves: "The Navajo name for Upper Antelope Canyon is Tse' bighanilini which means the place where water runs through rocks" (verified) |

## 3. Brinicle
| Claim | Source |
|---|---|
| Brinicles grow downward from Antarctic sea ice toward the sea floor | Geogarage, reproducing BBC News 2011 (verified) https://blog.geogarage.com/2011/11/brinicle-ice-finger-of-death-filmed-in.html ; Discover Wildlife (verified) https://www.discoverwildlife.com/animal-facts/marine-animals/ice-brinicles |
| Freezing sea ice pushes out salt; the brine is colder and saltier, so denser, and sinks | Discover Wildlife: freezing "pushing salt into the water below… a dense brine that sinks" (verified); Geogarage, Dr Mark Brandon's explanation (verified) |
| Surrounding seawater about minus 2 degrees Celsius, close to freezing | Geogarage: water about -1.9 °C (verified); Discover Wildlife: about -2 °C (verified). A fridge runs at about +4 °C (common knowledge) |
| Brine freezes the water it touches into a fragile hollow tube around the plume | Geogarage: "a fragile tube of ice around the descending plume" (verified) |
| Known to scientists for decades; first filmed forming in 2011 | Discover Wildlife: known "for several decades", first filmed 2011 (verified); Geogarage: "the first ever footage of a brinicle forming" (verified) |
| BBC crew under the ice at Little Razorback Island, near Mount Erebus; time-lapse; about five or six hours | Geogarage: "Little Razorback Island… off the foothills of Mount Erebus"; "the whole thing only took five, six hours" (verified) |
| Weddell seals broke off brinicles and knocked the filming gear over | Geogarage: "The large weddell seals in the area had no problems barging past and breaking off brinicles as well as the filming equipment"; "a seal knocked it over" (verified) |
| At the seabed it spreads a web of ice that freezes everything in its path; slow sea urchins and sea stars are frozen where they are | Geogarage: the ice web "froze everything it touched, including sea urchins and starfish" (verified); Discover Wildlife: "forms a web of ice, trapping everything in its path"; slow-moving starfish and urchins encased (verified) |
| Some sea stars crawl toward it | Discover Wildlife: some sea stars move toward the brinicle (verified) |
| No danger to a person | Inference from the above: it is a slow, fragile ice tube that only traps animals that can't move away within hours (Geogarage: "fragile"). Framing for the costume gag, not a safety claim |

## 4. Avalanche
| Claim | Source |
|---|---|
| A slab avalanche: a layer breaks from a weaker layer below and slides as a sheet, then breaks up | Avalanche.org encyclopedia, "Slab avalanche": slabs "release due to a sequence of fracture mechanical processes" (verified page; the weak-layer and single-sheet wording is the standard definition, so the screener may confirm it) https://avalanche.org/avalanche-encyclopedia/avalanche/slab-avalanche/ |
| Reaches up to about 130 km/h (80 mph) almost immediately; "can bury people basically like concrete" | AZFamily 2024, quoting Mathieu Brown, Kachina Peaks Avalanche Center (Flagstaff, northern Arizona): "Avalanches almost immediately reach speeds of up to 80 miles an hour and hence can bury people basically like concrete" (verified) https://www.azfamily.com/2024/01/20/flagstaff-avalanche-center-measures-risks-shares-how-prevent-them-northern-arizona . Highway fast-lane traffic is about 110-120 km/h (common knowledge) |
| Debris grains bond after stopping; this is called sintering | ISSW 2002 (Montana State), "Frictional heating of avalanching snow and the sintering of avalanche debris" (search snippet) https://arc.lib.montana.edu/snow-science/item/813 |
| Lab work suggests the first bonds between touching grains form in under a second | Journal of Glaciology, "Experimental and numerical investigation of the sintering rate of snow": "rapid (sub-second) formation of the initial bond" (search snippet) https://resolve.cambridge.org/core/services/aop-cambridge-core/content/view/0EE38666F876660D5D5176418E1A8356/S0022143000204310a.pdf/experimental-and-numerical-investigation-of-the-sintering-rate-of-snow.pdf |
| A powder avalanche cloud can weigh as little as about a bag of sugar per cubic meter | Powder-cloud densities of 1-30 kg per cubic meter and 4-25 kg per cubic meter (search snippets of the Cambridge Annals of Glaciology paper "Structures of snow cloud in dry snow avalanches") https://resolve.cambridge.org/core/services/aop-cambridge-core/content/view/E2EDB64F56E53CFB9062ED7CB3977CCD/S0260305500011459a.pdf/structures-of-snow-cloud-in-dry-snow-avalanches.pdf . A bag of sugar is 1 kg (common knowledge); "as little as" is the low end |
| Settled debris about 300 kg per cubic meter; about four adults | Maseguchi avalanche debris "average density near 300 kg m-3" (search snippet) https://resolve.cambridge.org/core/services/aop-cambridge-core/content/view/79EFDCCD6EB1925C42C5E03B4FAD0286/S0260305500011198a.pdf/simulation-of-a-destructive-avalanche-at-maseguchi-japan.pdf ; distal deposits 200-560 kg per cubic meter (search snippet). 4 × 75 kg = 300 kg (common knowledge) |
| A Swiss study of 638 people fully buried in open terrain: survival drops steeply after about 18 minutes | Brugger et al. 2001, *Resuscitation* 51:7-15, "Field management of avalanche victims": "Survival probability in completely-buried victims in open areas (n=638) plummets from 91% 18 min after burial to 34% at 35 min" (verified, Europe PMC abstract, PMID 11719168) https://europepmc.org/article/MED/11719168 |
| A finished avalanche looks almost like the fresh slope it replaced | Narration framing over the cartoon. Not a factual claim |

## 5. Dead Sea Sinkholes
| Claim | Source |
|---|---|
| About one third salt; close to ten times saltier than the ocean; people float | Salinity 34.2% (2011) and density 1.24 kg per liter, about 9.6 times ocean salinity (search snippets: WorldAtlas https://www.worldatlas.com/articles/is-it-possible-to-drown-in-the-dead-sea.html ; How It Works https://www.howitworksdaily.com/question-of-the-day-why-do-we-float-in-the-dead-sea/ ). Flag: no Britannica or USGS page found |
| Between 1980 and 2015 the level dropped about 100 ft (about 30 m), about 3 ft (about 1 m) a year | NBC News 2015, quoting GSI geologist Gidi Baer: "dropped by about 100 feet, which is a rate of three feet a year" (verified) https://www.nbcnews.com/news/world/sinkholes-threaten-israels-dead-sea-tourist-trade-n392461 . Kitchen counter is about 0.9 m (common knowledge) |
| About 30% of the drop has been blamed on the mineral industry (mineral extraction; no attribution to a named person) | NBC News 2015, the reporters' own statement that about 30 percent of the drop is caused by mineral extraction (URL above; screener confirmed it is not a Baer quote) |
| A buried salt layer about 10,000 years old, once in salty water; fresh groundwater dissolves it; cavities grow until the roof fails | NBC News 2015: layer "formed 10,000 years ago"; fresh water dissolves it; "cavities are formed and grow until the roof can't stand the weight" (verified); Geological Survey of Israel / Abelson et al.: dissolution of salt by groundwater following the retreat of the Dead Sea level (search snippet) https://www.gov.il/BlobFolder/reports/abelson-et-al-report-2009-27/he/report_2009_GSI-27-2009.pdf |
| More than 5,000 sinkholes since the 1980s | Israel Ministry of Environmental Protection annual report, via Globes: "As of 2015, there were 5,500 such sinkholes" (search snippet) https://en.globes.co.il/en/article-dead-sea-level-falling-12-meters-per-year-1001223618 ; NBC News 2015: "As many as 5,000… since the 1980s" (verified); University of Haifa's Michael Lazar, more than 6,000 on the western side alone (2022, search snippet) https://ynetnews.com/environment/article/s1z11u6vik . The Solid Earth 2019 preprint is NOT used (withdrawn by its authors, verified) |
| Some about 25 m (80 ft) across, about as wide as a tennis court is long | NBC News 2015: "can measure 80 feet in diameter" (verified). 80 ft is 24.4 m; a tennis court is 23.77 m long (common knowledge) |
| Swallowed roads, buildings and a resort parking lot, often without warning | NBC News 2015: "buildings and roads in their path without warning"; Mineral Beach parking lot engulfed (verified) |
| By 2015, about 400 new ones were being reported a year (draft 3: dated to 2015, not a current rate); the sea is still shrinking | NBC News 2015: "400 sinkholes are now reported around the body of water every year" (verified). The figure is from 2015 and is spoken as a 2015 figure. Still shrinking (present tense, checked 2026-10-09): Ynet on Israel's State Comptroller report, northern basin expected to keep falling about 1.15 m a year (search snippet) https://www.ynetnews.com/environment/article/syklzsw7fx ; Water 2026 review, 0.7-1.5 m a year across studies (search snippet) https://mdpi-res.com/d_attachment/water/water-18-01537/article_deploy/water-18-01537.pdf ; MoEP 2015 via Globes, 1.2 m a year. Newer rates from the screener are not used: Gutiérrez et al. 2023, 702 from 2005 to 2021 on the western shore; EGU23-13530, about 500 from 2018 to 2022 at Ghor Al-Haditha |
| Callback: Doug was swallowed at Morecambe Bay in 004 | channel/series_bible.md and 004 (in-universe) |

## 6. Crevasse
| Claim | Source |
|---|---|
| A glacier is flowing ice; it cracks as it flows over bumps and around bends | NASA Earth Observatory, "Out of the Crevasse Field" (verified) https://science.nasa.gov/earth/earth-observatory/out-of-the-crevasse-field/ ; general glaciology |
| Crevasses are tens of meters deep; one in Antarctica was 25 m deep | NASA: "tens of meters deep, tens of meters across"; the crevasse "Mongo" was "82 feet (25 meters) deep" (verified). Eight stories is about 24 m (common knowledge) |
| Wind-blown snow hardens into a snow bridge that hides the crevasse | NASA (Bindschadler): snow "stretches across the top" (verified); transantarcticmountains.com, wind-drift hardening (search snippet) https://transantarcticmountains.com/?p=389 |
| A snow bridge can be a few meters or a few centimeters thick | NASA, Bindschadler: "It can be a few meters thick, or it can be centimeters thick" (verified) |
| Remains in one Swiss glacier travelled about 10 km at about 120 m a year (a computer model) | Swissinfo: remains moved "around 10km in the ice at an average speed of 122 metres a year" (verified) https://www.swissinfo.ch/eng/cold-cases--swiss-glaciers-reveal-grisly-surprises/48778902 . An American football field is about 110 m including end zones (common knowledge) |
| A Swiss couple missing since 1942 were found in July 2017 on the shrinking Tsanfleuron Glacier, 75 years later | NBC News 2017 (verified) https://www.nbcnews.com/news/world/swiss-couple-missing-75-years-found-melting-alps-glacier-n784311 ; NPR 2017 https://www.npr.org/sections/thetwo-way/2017/07/18/537917006/bodies-found-in-swiss-glacier-believed-to-be-couple-missing-since-1942 (timed out; search snippet) |
| The ski company director: probably fell into a crevasse; as the glacier receded it gave them up | NBC News 2017, Bernhard Tschannen, Glacier 3000: "We think they may have fallen into a crevasse… As the glacier receded, it gave up their bodies" (verified) |
| Valais police list about 300 people missing since 1925; retreating ice keeps returning climbers missing for decades | Swissinfo: "some 300 people who have gone missing since 1925"; record melting means "more and more bodies of mountaineers and hikers who have been missing for decades" emerge (verified); 2026 Trift Glacier find, 1992 hikers (search snippet, ITV) https://www.itv.com/news/2026-08-20/melting-glacier-reveals-bodies-of-hikers-missing-for-three-decades-in-swiss-alps |

## 7. Tar Pit
| Claim | Source |
|---|---|
| In a city park in Los Angeles (Hancock Park), with the museum on site | La Brea Tar Pits FAQs (search snippet) https://tarpits.org/la-brea-tar-pits/faqs ; Wikipedia, La Brea Tar Pits (search snippet) https://en.wikipedia.org/wiki/La_Brea_Tar_Pits |
| Not tar: natural asphalt, a low-grade crude oil seeping up | Smithsonian Magazine: "low-grade crude oil, known to geologists as asphalt, began seeping to the surface" (verified) https://www.smithsonianmag.com/arts-culture/evolution-world-tour-la-brea-tar-pits-california-7746080/ |
| Up to a dozen gallons a day still bubble up; about four big buckets | Smithsonian: "as many as a dozen gallons of asphalt per day can bubble to the surface" (verified). 12 US gal is about 45 L, about four 11-liter buckets (common knowledge) |
| Today it catches lizards and pigeons; staff mark spots with traffic cones or fences | Smithsonian: "small animals such as lizards and pigeons continue to get stuck"; "marks the spots with traffic cones, or fences them off" (verified) |
| Leaves, sand or water hid the asphalt; in warmer seasons it was soft and sticky | Carleton University Hooper Museum: "covered with debris such as leaves, sand, and water"; "In the warmer seasons the asphalt became very soft and sticky" (verified) https://hoopermuseum.carleton.ca/PleistoceneWebsite/tarpits03.htm |
| More than three million specimens | Smithsonian: "more than three million specimens" (verified) |
| More than 600 species | Screener's range is 624 (Carleton Hooper Museum species lists) to "over 660" (UCMP Berkeley); search snippet: "more than 650 species". "More than six hundred" is true under all of them |
| The collections represent about the last 50,000 years of southern California life | La Brea Tar Pits (NHM LA), Mammal Collections: "represent the last 50,000 years of southern California life" (verified, URL above) |
| Roughly 90% of mammal fossils are predators | Smithsonian: "roughly 90 percent of the mammal fossils found are predators" (verified); museum: "the majority… have been large carnivores" (verified) |
| The dire wolf is the most common large animal dug out (draft 2: count cut) | La Brea Mammal Collections: "Our most common mammals include dire wolves" (verified); NHM Los Angeles "Tar Pits Fossil Count" sheet, "most common large animal at the Tar Pits" (search snippet) https://nhm.org/sites/default/files/2021-12/tar_pits_fossil_count.pdf |
| The carnivore-trap explanation: stuck herbivores drew in predators and scavengers, who got stuck too; ancient bison as the example herbivore | Mammal Collections: "large herbivores entrapped in asphalt attracted predators and scavengers, who themselves became entrapped"; ancient bison is the most common herbivore (verified) |
| "Tens of thousands of years" | Consistent with Smithsonian (about 40,000 years) and the museum (50,000) |
| Still bubbling today, a short walk from the museum | Smithsonian (verified); tarpits.org FAQs (search snippet). Flag: the museum building has been temporarily closed for construction, so the script says "the museum built to hold everything it ever caught" rather than claiming it is open |

## 8. Altamura Cave
| Claim | Source |
|---|---|
| Found in 1993 by cavers in Lamalunga Cave near Altamura, southern Italy; a Neanderthal | Lari et al. 2015, *Journal of Human Evolution*, "The Neanderthal in the karst" (abstract verified via Europe PMC, DOI 10.1016/j.jhevol.2015.02.007): "In 1993, a fossil hominin skeleton was discovered in the karst caves of Lamalunga, near Altamura"; *Homo neanderthalensis*. Wikipedia, Altamura Man: found by speleologists (search snippet) https://en.wikipedia.org/wiki/Altamura_Man |
| Researchers think he fell into a sinkhole and could not get out | IFLScience: "The team believe that the man had probably fallen into a sinkhole and gotten stuck" (verified) https://www.iflscience.com/neanderthal-altamura-man-suffered-an-unfortunate-death-and-became-embedded-in-a-cave-wall-over-128000-years-ago-82189 |
| Drip water carries dissolved calcite; this is how stalactites and stalagmites grow | IFLScience: dissolved calcite in rainwater accumulates in the cave (verified); general speleology |
| Calcite "cave popcorn" coated the bones and cemented him to the cave | IFLScience: "nodules… caused by deposits of calcite" (verified); Wikipedia: "pearl-like coralloid, calcium deposits otherwise known as cave popcorn" (search snippet); Uniroma1 / PNAS 2025 coverage: "covered in a thick layer of calcite, or 'cave popcorn'" (search snippet) https://www.uniroma1.it/en/notizia/neanderthal-nose-altamura-skeleton-reveals-new-details-about-facial-morphology-and |
| Dated between about 130,000 and 170,000 years ago | Lari et al. 2015: "172 ± 15 ka to 130.1 ± 1.9 ka" (verified abstract) |
| Written history is about 5,000 years old; more than 25 times longer | Writing began about 3200 BC (common knowledge); 130,000 / 5,000 = 26 |
| Left in place, because scientists judged that moving it could cause irreparable damage | IFLScience: "left where it was, as disturbing it could have caused irreparable damage" (verified); Uniroma1/PNAS 2025: not removed, to prevent damage (search snippet) |
| A fragment of shoulder blade is the only part that has left the cave | Lari et al. 2015: "the retrieval from the cave of a fragment of bone (part of the right scapula)" (verified); IFLScience: a shoulder blade fragment was sampled (verified). Flag: calcite samples were also taken in 2011, but those are not part of the skeleton |
| One of the oldest Neanderthals ever to give up genetic material | Lari et al. 2015: "the most ancient Neanderthal from which endogenous DNA has ever been extracted" (true in 2015, verified). Since then, Meyer et al. 2016, *Nature* 531:504, nuclear DNA from Sima de los Huesos, about 430,000 years old, classed as early Neanderthals (search snippet; Max Planck press release https://www.mpg.de/10364707/hominins-sima-de-los-huesos ; ScienceDaily https://www.sciencedaily.com/releases/2016/03/160315120946.htm ). Hence "one of the oldest" |
| 2025: researchers described the first preserved nasal cavity in the human fossil record, using endoscopic probes in place | Buzi et al. 2025, PNAS, "The first preserved nasal cavity in the human fossil record: The Neanderthal from Altamura" (title verified via Europe PMC, DOI 10.1073/pnas.2426309122); endoscopic probes in situ (search snippet of Sapienza/Pisa press releases) https://www.unipi.it/en/news/the-unprecedented-state-of-preservation-of-a-fossil-from-southern-italy-sheds-light-on-neanderthal-facial-morphology/ |

## 9. Amber
| Claim | Source |
|---|---|
| Amber is fossilized tree resin and is used in jewelry | Popular Science, quoting the AMNH amber collection: "Amber is fossilized tree resin and has been celebrated for its beauty for thousands of years" (search snippet) https://www.popsci.com/animals/amnh-amber-fossils/ |
| Wounded trees bleed resin that seals wounds and defends against attackers | Popular Science: "wound-sealing resin" (search snippet); resin-biology review: "defense against herbivores and pathogens, and as a healing mechanism, sealing wounds" (search snippet) https://repository.urosario.edu.co/bitstreams/c3216841-2437-4306-9d20-5f679ea9e332/download |
| Small animals that touch fresh resin stick and get sealed in | Popular Science: resin "envelop[s] buggy bystanders in an effective glue trap" (search snippet); ScienceDaily 2012 (verified) https://www.sciencedaily.com/releases/2012/08/120827180021.htm |
| Amber preserves wings and fine hairs, and sometimes behavior: catching prey, laying eggs, hatching | Palaeodiversity 2019, "Caught in the act of hatching", on "frozen behaviour" in Dominican amber: mating, egg laying, capturing prey, hatching (search snippet) https://bioone.org/journals/Palaeodiversity/volume-12/issue-1/pale.v12.a12/Caught-in-the-act-of-hatching--a-group-of/10.18476/pale.v12.a12.pdf ; "Paleoethology: fossilized behaviours in amber" (search snippet) https://revistes.ub.edu/index.php/GEOACTA/article/view/1900 . Wings and sensory hairs: secondary summary (search snippet); screener may want a primary source |
| Dolomites, northern Italy: about 70,000 droplets screened, mostly 2-6 mm long | Schmidt et al. 2012, PNAS 109:14796, "Arthropods in amber from the Triassic Period", DOI 10.1073/pnas.1208464109; ScienceDaily: "About 70,000 of the miniscule droplets were screened"; "most between 2-6 millimeters long" (verified). A pea is about 7-10 mm (common knowledge) |
| Three held arthropods: part of a fly and two gall mites | ScienceDaily (verified); search snippet of the PNAS summary: "one partial midge fly… and two new species of gall mites" |
| The bigger mite (*Triasacarus fedelei*) is 210 microns long (about a fifth of a millimeter), roughly the width of two human hairs | Live Science 2012: "just 210 microns long, or about twice the diameter of a human hair" (search snippet) https://www.livescience.com/22725-ancient-mite-trapped-amber.html |
| About 230 million years old; the oldest arthropods in amber; about 100 million years older than any found before | ScienceDaily: "an age of 230 million years"; "about 100 million years older than any other amber arthropod ever collected" (verified) |
| The mites probably fed on the leaves of the tree that preserved them; they look like modern gall mites | ScienceDaily: "likely fed on the leaves of the tree that ultimately preserved them"; "surprisingly similar to ones seen today" (verified) |
| The earliest dinosaurs had only just appeared about 230 million years ago | Martínez et al. 2011, *Science* 331:206, "A basal dinosaur from the dawn of the dinosaur era": "some 230 million years ago… (mid Carnian), the earliest dinosaurs" (search snippet) https://ri.conicet.gov.ar/handle/11336/69202 |
| The continents were still joined as Pangaea | USGS, This Dynamic Earth: "Pangaea began to break up about 225-200 million years ago" (verified) https://pubs.usgs.gov/gip/dynamic/historical.html |
| Resin can't trap a person | Inference: the trapped animals are millimeter-scale (droplets 2-6 mm). Framing for the costume gag |
| Callback: the 002 ant costume | channel/series_bible.md (002 costume gag) |

## Outro
Death counter 100 to 107: channel/series_bible.md (current total 100). Seven deaths: tree well, slot canyon, avalanche, crevasse,
La Brea, Altamura, amber. Two survivals: brinicle and Dead Sea. Each death is one this trap really causes or caused: tree well and
avalanche (snow immersion and burial deaths, sources above); slot canyon (Antelope 1997); crevasse (Tsanfleuron 2017); La Brea
(animals; Doug is in the role of an animal walking in); Altamura (the Neanderthal); amber (gall mites, Doug in costume).
