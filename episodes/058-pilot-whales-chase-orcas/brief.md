# Episode 058: Why Orcas Run From Pilot Whales a Third Their Weight (brief)

Creative director, 2026-11-25. Backlog idea **#98** (7.7 base, **8.2** in `topics` with the single-famous-animal bonus; first on the list), `animals`.
Read before writing: `config/channel.yaml`, the style bible (1.4, 3.2, 3.3, the 2026-10-27 retention update, writer rules), the series bible
(Openings, Outro, costume gag, used-once lines, episode log to 057), `data/ideas.md` row #98, the 11-22 memo and its CD decisions, the 051–057
`metadata.json`, and the **021, 048, 051 and 055 scripts** (they hold every orca and blackfish fact we have already used). Stage stays `idea` until draft 1.

## 0. Why this idea, and why now
- **Lane rule (D4).** `python -m studio topics` (11-25) puts #98 first (8.2). The last two episodes are 056 `animals` and 057 `ocean`, so the
  same-playlist default (#133 botfly) doesn't apply.
- **Orca spacing (CD 11-22 #2, memo §4.3): satisfied, just.** #98 had to sit at least 3 slots after 055 (056, 057, 058). The orca run is still
  heavy (048 false killer whale, 051 great white flees orcas, 055 sperm whale circle), so the conditions below are hard rules, not taste:
  - **Pilot whales are the subject.** Orcas appear as the thing being chased, in items 1 and 6–8 only. No orca hunting scenes, no orca prey list.
  - **Not used again:** 021's MENU and prey-costume ladder, 051's SHARKS GONE tracker and liver facts, 055's RING card and the 1997 Pitman attack,
    048's prey-offering, "no record of killing a person in the wild".
  - **One callback each, one line max:** 055 (the Gulf of Mexico pilot-whale harassment sentence is already in 055's script; item 5 may build on
    it with new detail but must not re-describe the ring) and 048 (false killer whales are the pilot whale's close relative; optional).
- **Engine (rule a).** Beyond the Blue "The Only 3 Animals That Make Orcas Run Away": **1.50M, 4.91x, vph_recent 2,361** today
  (`data/competitors/2026-11-25.json`); ApexMorph's same frame 4.05M (memo 11-22); BTB "Why Are Orcas Terrified of Pilot Whales?" 1.78M (5.5x).
  Two smaller channels have "Why The Entire Ocean is Terrified of Pilot Whales" (532K and 75K), so the angle must be ours.
- **Live-engine experiment (CD 11-22 #3):** engine vph_recent on brief day = **2,361**, under the 3,000 bar. 058 is **not** a test episode.
- **Real science, recent:** Selbmann et al. 2022 (*Acta Ethologica*, Iceland: killer whales avoiding/fleeing long-finned pilot whales) and
  Curé et al. 2012 (*PLoS ONE*, pilot whales approach killer-whale sound playbacks). The honest answer to "why" is two hypotheses (mobbing a
  predator, or competition), and the script says so: the title's "Why" is delivered as "here is what scientists think, and here is the evidence".

## 1. Working title and the format it borrows
- **Working title: "Why Orcas Run From Pilot Whales a Third Their Weight"** (52 characters). Famous animal in word 2 (v2 rubric).
  "A third their weight" only if `facts.md` sources it (adult male orca roughly 6+ t vs long-finned pilot whale male roughly 2–2.3 t; NOAA
  species pages are fine). If it doesn't hold, use "Half Their Size" (length) or drop the scale claim.
- **Leads for the titler** (10 candidates; D4 is lint only, hand-pick if the top 3 are within 4 raw points):
  - "Why the Ocean's Top Predator Runs From Pilot Whales"
  - "Why Orcas Flee When Pilot Whales Show Up" (short; strongest plain promise)
  - "Pilot Whales Chase Orcas Out of Iceland's Fjords, and Nobody Is Sure Why"
- **Banned in the title:** BTB's "Only 3 Animals"/"Make Orcas Run Away"/"Terrified of", "The Entire Ocean", "Killer Whales" alone (kids and
  captivity searches), 051's "Deadliest ... Flees" shape, any "?", ALL CAPS, "Doug" is allowed (the no-Doug rule is void, CD 11-22 #5).
- **Thumbnail (the opening image; archetype C hero):** a tight wall of black, round-headed pilot whales charging left-to-right; ahead of them a
  large orca fleeing out of frame with a sweat drop, and tiny Doug in an orca costume (cap on top) between the two, looking back.
  Text ≤3 words, not repeating the title: **"WRONG WAY"** or **"THEY CHASE"**. Never "ORCA", "PILOT", "RUN".

## 2. Axis and items
**Declared axis: severity of what the pilot whales stand up to**, from prey to the ocean's top predator. Item 1 is a cold open off the axis (the
strongest hook: they swim *toward* orca sounds). Then the axis runs prey → people → sharks → giants → orcas. Most extreme last: real orcas, in
real flight. Not an era/deep-time axis.

**Spoken bands:**

| Header | Items |
|---|---|
| (no header: cold open) | 1 |
| **"Prey."** | 2 |
| **"People."** | 3 |
| **"Sharks."** | 4 |
| **"Giants."** | 5 |
| **"Orcas."** | 6–8 |

- **Episode-only device: WHO RAN** (staging only, never read aloud; the art director approves it). A crude two-column scoreboard under the
  death counter, "PILOT WHALES | EVERYONE ELSE". The pilot-whale column only gains ticks; at the boss, a big red "ORCAS" is written under
  EVERYONE ELSE. Not the 024 BEAR/MOOSE board (that ticks per trait between two named animals; this one is who backed off). No field guide.
- **Costume:** one new **orca costume** (art director; it must read as an orca at thumbnail size: white eye patch, white belly, tall fin, cap on
  top). It appears in items 1, 7 and 8 only. Item 2 may reuse `squid_costume` (no redraw). No other costumes; no costume ladder (021).
- **The narrator's running observation:** pilot whales don't run from things. They go and look. Say it once (item 2 or 3), then let the pictures do it.

**Words:** 8 items, 245–290 each, 1,950–2,350 total. If long, cut item 4 first. Never cut 1, 6 or 8. If a fact can't be sourced, cut it; don't hedge it.

| # | Item (name sentence) | Facts to research (2–4) | Everyday scale analogy | Doug beat |
|---|---|---|---|---|
| 1 | **The Speaker.** (cold open; one of the three strongest) | Curé et al. 2012 (*PLoS ONE*, Norway): playbacks of killer-whale sounds made long-finned pilot whales **approach the speaker**, group up and call more; give the paper's numbers (n groups, how close). **Twist (by 0:45):** most animals flee that sound; these came to find it. Second twist line: the authors' reading (mobbing, as small birds mob an owl; attribute it). | Small birds mobbing an owl, except each bird weighs as much as a car. | Doug in the orca costume, holding the underwater speaker (`loudspeaker` asset), pleased with his impression. The pod arrives. **Death 421**, cut away; the speaker is still playing. Played flat. |
| 2 | **The Sprint.** ("Prey.") | Aguilar Soto et al. 2008 (*J. Animal Ecology*, Tenerife): short-finned pilot whales sprint at depth (around 1,000 m; up to ~9 m/s, give the paper's figure) after large prey, earning "cheetahs of the deep". Diet mostly squid (source). | A car doing city speed, a kilometre under the sea, in the dark. | Doug in the reused squid costume at depth. "hi friend?" **Death 422**, cut to black, the costume floats up flat (`squid_costume_flat`). |
| 3 | **The Longline.** ("People.") | Pilot whales take hooked fish off longlines (depredation; NOAA / Garrison 2007 or a Hawaii/Atlantic fisheries report; give what's sourced). Fishermen lose catch and bait; the whales learn the boats (attribute any "learn" claim). No whale-injury or entanglement imagery. | Someone eating your shopping out of the trolley while you push it. | Doug the fisherman reels in an empty hook, three times, while a black round head surfaces beside the boat. **Survival** ("Doug is fine. Doug's dinner is not."), written fresh. |
| 4 | **The Whitetip.** ("Sharks.") Cut first if long. | Oceanic whitetip sharks are often seen **following short-finned pilot whale pods** (source a paper or NOAA/Hawaii observation; give the leading idea: the shark follows them to food). The shark trails them; it doesn't take them on. Keep it light: #132 oceanic whitetip is its own backlog idea, so no whitetip "greatest hits" (no shipwreck stories). | A dog following the person carrying the shopping. | Doug, between the pod and the following shark. The pod leaves. The shark stays. **Death 423**, cut away, cap floats. |
| 5 | **The Sperm Whale.** ("Giants.") | Weller et al. 1996 (*Marine Mammal Science*, Gulf of Mexico): short-finned pilot whales harassed a group of sperm whales, each animal many times their weight (give the source's numbers). One-line 055 callback only, no re-telling of the ring. Long-finned/short-finned size facts for scale (NOAA). | Picking a fight with a bus because it was parked near you. | Doug in a dinghy between the two species. **Survival**: the narrator is **quietly disappointed** (the only time). |
| 6 | **The Calf.** ("Orcas.") | 2021, off Iceland: a group of long-finned pilot whales seen with a **killer whale calf** among them (Icelandic Orca Project / Selbmann et al.; source the report, use their wording, "adopted" in quotes or attributed). Other "adoption" cases are a hypothesis; say so. **Twist:** the animal they chase out of fjords is the one they apparently raised. | Finding a wolf cub in the sheepdog's basket. | Doug offers the calf a fish. **Survival** ("Doug is fine."), written fresh. Re-hook: the calf has a family, and they are about to meet. |
| 7 | **The Family.** ("Orcas.") | Long-finned pilot whales stay with their mother's group for life, males and females (Amos et al. 1993, *Science*, Faroese genetics; cite the finding only, **no reference to the hunt**). Short-finned females live decades past their last calf (Marsh & Kasuya 1986; menopause shared with only a few mammals, Ellis et al. 2018). **Twist:** an orca facing a pod faces a whole family that never splits up (the narrator's framing). | A family reunion where every cousin turns up, every time, forever. | Doug in the orca costume meets the matriarch. **Death 424**, cut away; the cap on a grandmother's head for one beat, then floats. |
| 8 | **The Chase.** ("Orcas.", the boss; about 1,750 words in) | Selbmann et al. 2022 (*Acta Ethologica*, Icelandic coastal waters): in recorded encounters, killer whales avoided pilot whales or **left at high speed** (porpoising), with pilot whales approaching or following; give the paper's counts. Orcas there are the bigger animal (sizes from NOAA). Both hypotheses, attributed: mobbing a predator, or competition over food. Kicker: the top predator of the ocean leaves the fjord; Doug, the slowest orca there has ever been, does not. | A pub emptying because one family walked in. | **The payoff promised in the opening.** Doug in the orca costume, in the middle of a fleeing orca pod. The orcas porpoise away. Doug can't porpoise. The wall of black heads turns to him. **Death 425**, cut to black, played flat. WHO RAN gets "ORCAS" stamped red. |

**Expected deaths: 5** (counter 420 to 425). Survivals at items 3, 5 and 6. The writer may turn one more death into a survival, but not the boss.

**Closing (after the boss kicker):** the empty fjord; the orca costume floating flat with the cap on it; the pilot-whale pod slowly circling it
once and leaving (they investigate; they don't eat it). One fresh dry kicker about the cap. Not the LIVE feed (`animals`, not `ocean`).

## 3. The opening (series bible "Openings", style bible 3.2, retention update)
- **No hook section.** The thumbnail image is the first frame.
- **First sentence (sourced, concrete):** "When scientists played the sound of hunting killer whales into the sea off Norway, one kind of whale swam
  toward it." (Curé et al. 2012). Doug's line comes second.
- **Payoff promise by 0:10:** "By the end of this, Doug is dressed as an orca, and the real orcas are leaving without him."
- **"The Speaker." by word 35.** Its twist (they approach the sound everything else flees) lands by 0:45, about 145 words.

## 4. Running gags
- **Death counter** starts at **420** (after 057). Deaths are played flat.
- **"Doug did not agree to this."** once, at item 8 (zipping the orca costume back up).
- **"Doug is fine."** at items 3 and 6, written fresh. Not 056/057 lines.
- **Narrator quietly disappointed** at item 5 only. **"hi friend?"** once (item 2).
- **Cap survives:** floats at 4, on the grandmother at 7, on the flat orca costume at the closing.
- **Outro (rule from 048):** ≤30 words, the death counter plus one fresh deadpan subscribe line tied to the counter. Not a 048–057 line.
- **Do not reuse:** THE MENU, THE RING, SHARKS GONE, NOW SERVING, SHARK AGE, the field guide, the blowhole costume, the fish-into-the-boat
  ending, the LIVE feed.

## 5. Playlist
`animals` (Doug vs. Animals). 056 was `animals`, 057 `ocean`, so no same-playlist pair. 059 should leave orcas entirely for at least 4 slots
and should not be `animals` if 058's run makes it two in three; the parasites pick (#133 botfly) is the default if in doubt.

## 6. Length and payoff
- **Target 10–12 min**, about **1,950–2,350 words** at ~195 wpm, 8 items, 245–290 words each.
- **Payoff promise line:** "By the end of this, Doug is dressed as an orca, and the real orcas are leaving without him."

## 7. Risks
- **Gore.** No bites, wounds, blood or injured whales. No entanglement or hooked-whale imagery in item 3. Deaths are cut-aways, X eyes, flat
  costumes. Pilot whales are never drawn attacking Doug on screen; they arrive, then cut.
- **Policy / sensitive topics.** **No Faroese grindadráp** in words or pictures (Amos et al. 1993 used samples from it; cite the finding only).
  **No mass strandings** (Farewell Spit, Macquarie Harbour): real mass deaths, a different tone, and they break the axis. No captivity.
- **Kid appeal (medium: whale calf, costumes).** The calf is not cute (no big eyes); the orca costume is deadpan, adult-coded. Made-for-kids No.
- **Misleading packaging.** Orcas don't flee pilot whales everywhere: the evidence is Iceland (and playbacks in Norway). The script says
  "in Iceland" at item 8 and the title must not imply a global rule it can't back ("Everywhere", "Always" banned). "Terrified" is not a
  measured state: say "leave" or "avoid", or attribute it.
- **Overclaims to avoid:** "pilot whales kill orcas" (no source); "adopted" as fact (attribute); the "why" as settled (two hypotheses);
  the weight ratio without a source; any claim from a competitor video.
- **Strong sources needed:** Selbmann et al. 2022 (*Acta Ethologica*), Curé et al. 2012 (*PLoS ONE*), Aguilar Soto et al. 2008, Weller et al. 1996,
  Amos et al. 1993, Marsh & Kasuya 1986 / Ellis et al. 2018, NOAA species pages for sizes, a fisheries source for depredation, a paper or
  agency source for whitetips following pilot whales, and the Icelandic Orca Project / Selbmann report for the calf. Never a competitor video or listicle.
