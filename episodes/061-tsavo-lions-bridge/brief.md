# Episode 061: Why the Tsavo Lions Hunted Railway Workers for Nine Months (brief)

Creative director, 2026-11-28. Backlog idea **#129** (7.2 in `topics`, top pick that passes every rule), `animals`.
Read before writing: `config/channel.yaml`, the style bible (3.2, 3.3, the 2026-10-27 retention update, writer rules), the series bible
(Openings, Outro, the field guide, used-once lines, episode log to 060), `data/ideas.md` rows #129 and #13, the 11-22 memo and its CD
decisions, and the 052–060 `metadata.json`. Stage stays `idea` until draft 1.

## 0. Why this idea, and why now
- **Lane rule (D4).** `python -m studio topics` (11-28) lists #107 great white (7.5), #89 mountain lion (7.5), #120 mantis shrimp (7.3), then
  **#129 Tsavo lions (7.2)**. Skipped: #107 is the great white again (051 and 059) and has no 1M+ outlier on the formula (Paint Explainer 146K);
  #89 and #120 have no watched-channel outlier (rule a; #89's demand is polluted by GTA streams). #129 is the first pick with a proven engine,
  and the 060 brief named it the runner-up for 061.
- **Engine (rule a).** Simple Paint "The Deadliest Man-Eaters to Ever Exist" **1.24M (5.3x)**, plus Acontece no Mundo "The Only 4 Animals That
  Hunt Humans to Eat" 523K at 34 d (644 vph, signals 11-22). Not live (under 3,000 vph), so 061 is **not** a live-engine test episode.
  Demand 8 ("tsavo man eaters"), saturation 10 (3 copies of the "why the Tsavo lions" phrasing).
- **#13 overlap.** #13 "The Deadliest Man-Eating Animals in Recorded History" uses the same engine. The row says pick one: we pick #129 (one
  famous story, a sourced death count and a twist). #13 goes on hold for at least 10 episodes, and if it is made later, Tsavo gets one sentence.
- **Playlist spacing.** 059 `ocean` (what-if), 060 `ocean`, so 061 `animals` resets the run. No orcas, no sharks, nothing at sea.
  Lions appeared as the *victims* in 052 (honey badger) and 054 (cape buffalo). Here they are the hunters and the story is a human-history
  event, so the topic is different. No callbacks to 052 or 054 except at most one sentence.

## 1. Working title and the format it borrows
- **Working title: "Why the Tsavo Lions Hunted Railway Workers for Nine Months"** (58 chars). Famous named animals in words 2–4, a concrete
  sourced duration, no negation. It borrows Simple Paint's man-eater outlier (one famous killer, its body count) in our "Why X" single-animal frame.
- **Leads for the titler** (10 candidates; hand-pick if the top 3 are within 4 raw points):
  - "The Two Lions That Stopped a Railway for Nine Months"
  - "Why Two Maneless Lions Hunted a Railway Camp in 1898"
  - "The Tsavo Man-Eaters Were Real, and Their Hair Kept a Record" (only if facts.md supports the hair/isotope wording)
- **Banned in the title:** "135 people" or any victim count stated as fact (the count is disputed; that is the twist), "the deadliest
  lions ever", "Ghost and the Darkness" (a film title), "?", ALL CAPS words, "Doug Gets Eaten".
- **Thumbnail (the opening image; archetype C hero):** night, a lantern-lit canvas tent (library `canvas_tent`/`tent`) seen from outside; two big
  maneless lion heads pushing through the tent flap, eyes lit; tiny Doug in a camp bed inside, blanket to his chin, looking at the camera.
  Text ≤3 words, not repeating the title: **"NO MANES"** or **"9 MONTHS"**. Never a number of victims, never "MAN-EATER", no blood, no rifles.

## 2. Axis and items
**Declared axis: time in 1898 at the Tsavo bridge camp**, from the first attacks (March) to the night the second lion is shot (29 December).
Monotonic, never jumps back. Most extreme last: Doug up a tree in the dark with the second lion. Not depth, not era (this is nine months of one
year, a human-history timeline; validate's era block does not apply, and the script must never say "era" or "period").

**Spoken bands** (two-word sentences, no header before item 1):

| Header | Items |
|---|---|
| (none) | 1 |
| **"Week one."** | 2 |
| **"Months in."** | 3–6 |
| **"December."** | 7–9 |

- **Episode-only device: DAYS WITHOUT AN INCIDENT** (staging only, never read aloud; the art director approves the drawing). A crude
  construction-site safety board beside the death counter, chalk number. It counts up through survivals and is wiped to **0** at every death;
  at the boss it is wiped and then the whole board falls over. New to the channel (not 043's fingerpost, 051's stopwatch or 060's tape measure).
- **The field guide** (animals standard prop, `field_guide_lion_hyena` exists): one page, "TSAVO LIONS (x2)", FRIEND? box. "NO" after item 2,
  "MAYBE" at item 6, a second red "NO" at item 9. Optional; the director decides.
- **Costume gag: none** (the lions hunted people, so there is no reason for one). The narrator says this once, flat, at item 2.
- **Gear:** Doug's bandage (022) at item 3 only. No hard hat, no rifle, ever.

**Words:** 9 items, 215–260 each, 1,950–2,350 total. If long, cut item 4 first, then item 7 (fold the walkout into item 8). Never cut 1, 5 or 9.
If a fact can't be sourced, cut it.

| # | Item (name sentence) | Facts to research (2–4) | Everyday scale analogy | Doug beat |
|---|---|---|---|---|
| 1 | **The Man-Eaters of Tsavo.** (cold open; one of the three strongest; March 1898) | The Uganda Railway (Mombasa to Lake Victoria) and its bridge over the Tsavo River; Lt. Col. John Henry Patterson arrives in March 1898 to build it; thousands of workers, many indentured labourers from British India. Patterson's later count (his 1907 book, and the 135 figure he gave; source the exact claim and year). **Twist (by 0:45):** Yeakel et al. 2009 (*PNAS*) read the lions' own hair and bone chemistry and estimated about **35** people between them (give the paper's per-lion split, about 11 and 24). The man who shot them overstated it about fourfold; it is still about 35 real people. | The railway's length as a familiar drive (writer sources the km and picks the comparison). | Doug's first day: lunchbox, clipboard, a tent at the very edge of camp "because the view is nicer". **Survival** ("Doug is fine. Doug has a view."), written fresh. Re-hook: the lions already know where the edge of camp is. |
| 2 | **The Tent.** ("Week one.") | Patterson's account of the first named victim taken from inside a tent at night (Ungan Singh, a jemadar; attribute "Patterson wrote"). The lions came into camp at night, past campfires. Adult male lion size (Field Museum / a reputable source; give kg). One line: no costume today, because these lions did not need a reason. | A lion's weight against something in a home (fridge, sofa). | Doug zips the tent shut and gives the zip a thumbs up. Silhouette of a lion head against the canvas, cut to black. **Death 431**, played flat. The real victim is never drawn and never joked about. |
| 3 | **The Thorn Fence.** ("Months in.") | Bomas: thorn-bush fences built around the camps, fires kept burning all night, tins rattled; the lions got in anyway (Patterson's account; give his wording on how: pushed through or over). The workers moved camps; the lions followed. | A garden hedge against a delivery van. | Doug builds the thorniest fence in Kenya and gets stuck in it. **Survival** with the 022 bandage ("Doug is fine. The fence works on Doug."), written fresh. |
| 4 | **No Manes.** ("Months in.") Cut first if long. | Both lions were adult **males with almost no mane**; maneless or thin-maned males are common in Tsavo (Kays & Patterson 2002, or Field Museum; source the hypothesis that heat plays a role and attribute it). Patterson's descriptions vs the mounts. | A security guard looking for a man with a beard while two shaved men walk past. | Doug on watch with a sketch of a "big lion with a mane"; two maneless males stroll past and he waves them through. **Death 432**, cut away. |
| 5 | **The Broken Tooth.** ("Months in.", the "why" item) | Patterson & Neiburger 2000: one lion had a broken canine with a root abscess (dental injury hypothesis; attribute). Hypotheses for why they hunted people: injury, a rinderpest outbreak in the 1890s that killed prey, the caravan route (attribute all as hypotheses; Kerbis Peterhans & Gnoske 2001). **Twist:** DeSantis & Patterson 2017 (*Scientific Reports*) dental microwear shows they did **not** crunch bones like starving lions; people were part of the menu, not a last resort. | A toothache that makes you order soup, except the soup is people (writer: rephrase so it lands on Doug, not on victims). | Doug as a dentist with a tiny mirror and a "FREE CHECK-UP" sign. "hi friend?" (once). **Death 433**, cut to black at "open wide". |
| 6 | **The Trap.** ("Months in.") | Patterson's trap: a cage built in two compartments, armed men as bait behind iron bars, a falling door; the lion got in, the men panicked and fired wildly, and it escaped (Patterson's account; source the detail or simplify). No shots drawn; muzzle flashes off-screen as cartoon "BANG" text at most, never at an animal. | A bus shelter you are told is lion-proof. | Doug volunteered as the bait. **"Doug did not agree to this."** He survives behind the bars; the only casualty is his lunchbox. **Survival**, narrator **quietly disappointed** (the only time). |
| 7 | **The Walkout.** ("December.") Cut second if long (fold into 8). | Workers stopped a passing train and left; construction halted for about three weeks (Patterson's account; source the number). The story reached Parliament: Prime Minister Lord Salisbury spoke about the Tsavo lions in the House of Lords (verify the year and wording, or drop). | An office where everyone leaves at once and you are still at your desk. | Doug is the last worker in camp, holding a shovel, waving at the departing train. **Death 434**, played flat, the DAYS WITHOUT AN INCIDENT board wiped by a paw. |
| 8 | **The Platform.** ("December.", 9 Dec 1898) | Patterson sat at night on a flimsy wooden platform (a machan) near bait; the first lion stalked **him** in the dark before he shot it (Patterson's account; give the date 9 December 1898). Its body length from the Field Museum mount or Patterson (give the source's number). The lion's death is stated in one sentence, never shown. | A wobbly stepladder at 3 m, in the dark. | Doug on the platform next to Patterson (Patterson drawn as a plain stick figure with a hat, never with a weapon pointed at anything). The platform creaks; Doug holds very still. **Survival.** Re-hook: there were two lions. |
| 9 | **The Last Lion.** ("December.", 29 Dec 1898, the boss; most extreme) | Twenty days later Patterson hunted the second lion; by his account it took several shots and kept charging before it died near a tree (give his account's wording; attribute "Patterson wrote"). Construction resumed; the bridge was finished (source the date, early 1899). | A car that keeps driving after the brakes, the engine and the wheels are gone. | **The payoff promised in the opening.** Doug up a thin tree at night, the second lion below, looking up, patient. The board is wiped and falls over. **Death 435**, cut to black on the lion's eyes. No wound, no blood, no lion death on screen. |

**Expected deaths: 5** (counter 430 to 435). Survivals at 1, 3, 6 and 8. The writer may turn one more death into a survival, never the boss.

**Closing (after the boss kicker):** Patterson sold the two skins to the **Field Museum in Chicago in 1924 for $5,000** (source); they were
mounted and are still on display. In 2024 de Flamingh et al. (*Current Biology*) pulled hair out of the lions' broken teeth and read its DNA:
giraffe, zebra, wildebeest, oryx, waterbuck, and people (give the paper's list exactly). Final image: the two maneless lions in a museum glass
case, the red cap on the floor of the case, a small museum label beside it. One fresh dry kicker about the cap. Never the famous photo of
Patterson posing over a dead lion.

## 3. The opening (series bible "Openings", style bible 3.2, retention update)
- **No hook section.** The thumbnail image is the first frame.
- **First sentence (sourced, concrete):** "In 1898, two lions stopped a railway in Kenya, and the man who finally shot them said they had eaten 135
  people." (attributed claim; the writer sources the exact number Patterson gave.) Doug's line comes second.
- **Payoff promise by 0:10:** "By the end of this, Doug is up a tree in the dark with the second lion, and it does not stop."
- **"The Man-Eaters of Tsavo." by word 35.** The Yeakel twist (about 35, from the lions' own hair) lands by 0:45, about 145 words.

## 4. Running gags
- **Death counter** starts at **430** (after 060). Deaths played flat, all cut-aways.
- **"Doug did not agree to this."** once, at item 6 (bait). **"Doug is fine."** at items 1 and 3, written fresh.
- **Narrator quietly disappointed** at item 6 only. **"hi friend?"** once (item 5).
- **Cap survives:** left on the tent pole at 2, on top of the thorn fence at 3, on the departing train at 7, in the museum case at the close.
- **Outro (rule from 048):** ≤30 words: the death counter plus one fresh deadpan subscribe line tied to it. Not a 048–060 line.
- **Do not reuse:** 060's DISTANCE TO FISH, 043's fingerpost, 051's SHARKS GONE, NOW SERVING, THE RING, "Back then, the lions had a pulse."
  (023), any costume ladder, 052's weigh-in scale.

## 5. Playlist
`animals` (Doug vs. Animals). 060 and 059 were `ocean`. 062 should not be `animals` if a strong `parasites` or `ocean` pick exists: the parasites
default is #133 botfly; #130 box jellyfish is the ocean option.

## 6. Length and payoff
- **Target 10–12 min**, about **1,950–2,350 words** at ~195 wpm, 9 items.
- **Payoff promise line:** "By the end of this, Doug is up a tree in the dark with the second lion, and it does not stop."

## 7. Risks
- **Real victims (highest risk).** About 35 real people died, most of them workers from British India and local Africans. They are never drawn,
  never named in a joke, never a punchline. The narrator says once, straight, that they were real people and the railway kept going anyway.
  Only Doug dies on screen. No remains, no "cave of bones" (the cave story is disputed; leave it out).
- **Gore and violence.** Cartoon only: silhouettes, cut to black, X eyes. No blood, no claws in skin, no dragging shown. Rifles are never aimed at
  an animal on screen and no lion is shown dying; their deaths are one stated sentence each. No trophy imagery.
- **Colonial history.** Stay factual and neutral: name it a British colonial railway once, attribute Patterson's claims as his, no hero framing
  of the hunter, no stereotyped drawings of workers (plain stick figures, same as Doug minus the cap).
- **Kid appeal (medium).** Lions read as Lion King: draw them crude, lean, blank-eyed, never smiling or cute. Humour adult-coded and dry.
  Made-for-kids No.
- **Misleading packaging.** Never state 135 as fact; the video's own twist is that it was about 35. The title's "nine months" must match facts.md
  (March to December 1898).
- **Strong sources needed:** Patterson 1907 *The Man-Eaters of Tsavo* (primary, attributed), Yeakel et al. 2009 (*PNAS*), Patterson & Neiburger
  2000 (dental), DeSantis & Patterson 2017 (*Scientific Reports*), de Flamingh et al. 2024 (*Current Biology*), Kerbis Peterhans & Gnoske 2001
  (*J. East African Natural History*), Field Museum pages for the 1924 purchase and the mounts, Hansard for Salisbury (or drop it).
  Never a competitor video, a film, or a listicle.
