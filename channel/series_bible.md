# Doomed Doug: series bible

Owned by the creative director. Every agent reads this. Update it when an episode adds lore.

## Premise
Every video, the narrator sends **Doug** somewhere nature really doesn't want him, and walks the audience through
it stop by stop, getting worse each time. Real science, crude MS Paint drawings, deadpan dark comedy.
Lane: disturbing science & nature (deep sea, parasites, prehistoric oceans, deadly places, extreme environments).

## Doug
- Stick man, round white head, dot eyes, **red baseball cap** (his signature; it's the one thing that always
  survives). Drawn by `studio/doug.py`; his look never changes.
- Personality: cheerful, gullible, optimistic, never learns. Says very little (speech bubbles of 1–4 words:
  "wait what", "nope", "hi friend?"). He always volunteers or is "volunteered".
- He dies a lot, cartoonishly (X eyes, lying flat, ghost Doug floats up). He is always back, unexplained, in the
  next segment or episode. Never graphic.

## The narrator
- Deadpan, calm, slightly sadistic documentary voice. Treats Doug as an expendable test subject but is secretly
  fond of him. Talks to the viewer directly ("you", "we").
- Delivers the real science straight, then undercuts it with one dry line about Doug.
- Never mean to the viewer, never preachy, never gross for its own sake.

## Running gags (use 2–3 per episode, don't overdo)
- "Doug did not agree to this." (episode opener or first danger)
- **Doug death counter**: an on-screen label "DOUG DEATHS: N" that ticks up at each death. Cumulative across the
  channel. Current total: **114** (7 after 001, plus 11 in 002, plus 9 in 003, plus 9 in 004, plus 10 in 005, plus 10 in 006, plus 9 in 007, plus 9 in 008, plus 10 in 009, plus 9 in 010, plus 7 in 011, plus 7 in 012, plus 7 in 013 (final package approved); update after every episode). The next episode's
  counter starts at 114. The 100th death (011, elephant) got one flat line; don't make a milestone bit of later round numbers.
- The red cap floating alone after a death.
- Doug trying to befriend the thing that will kill him.
- Narrator: "Doug has died. Again." / "Doug is fine." (Doug is not fine.)
- Doug survives the boss and the narrator is quietly disappointed (established in 001).
- The cap always survives, even when Doug does not (001: stolen by the Bobbit Worm and recovered; the only thing to float up from the Black Swallower; 002: floats alone in the hotel pool and the amoeba lake, briefly worn by Buddy the raccoon and taken back).
- **The costume gag** (from 002): when a killer only targets animals, Doug is zipped into a costume of the host
  (002: cockroach, ant, cricket, snail, rat) and plays it completely straight. The red cap always sits on top of the
  costume. The costume comes off at the zone shift to human hosts. On death the costume goes flat (X eyes, cartoon only).
  Played deadpan and adult-coded: no mascot voices, no cute framing. The narration states once that the animal-only
  parasite can't infect people ("which is exactly why Doug is dressed as a cricket"). Library precedent:
  `assets/library/squid_costume.json`.
- **The time machine** (from 003): a crude MS Paint phone booth, our own design (art director owns the drawing). It is
  how Doug reaches deep time and the standard vehicle for the `prehistoric` playlist. Never explained, never
  breaks down on purpose; Doug steps out hopeful, the door opens onto the danger. It always survives (003 ends with a
  pigeon sitting on its roof). Do not use it outside time-travel episodes.
  007 (QC passed, final package approved): it comes home to 2026 as a block of clear ice with the cap frozen on top, cracks open,
  and Doug gives a thumbs up inside (the counter does not go down). Use this ice-block return once; don't repeat it.
  009 (final package approved): it comes home to 2026 with a Megalodon tooth in the door and the cap on the roof; the cap is "the only one who lasted the whole night". Used once; don't repeat the tooth-in-the-door ending.
- **Doug's suitcase** (from 004): a battered MS Paint suitcase that is the standard prop of the `places` playlist,
  the way the time machine belongs to `prehistoric`. Doug carries it into the opener with no stickers on it. Every time he
  dies at a place, a crude travel sticker with the place's name (for example "DEATH VALLEY") lands on it. Survivals get
  no sticker. The episode ends on the full suitcase next to the cap, and the outro may say "The suitcase still has room."
  It always survives and is never explained. The art director owns the drawing. It is a stickered travel variant and must
  stay distinct from the over-packed `assets/library/suitcase.json` ("HEAVY" tag). Use it only in `places` episodes.
- **The LIVE feed** (from 006): the standard closing image for `ocean` episodes. After the boss death, cut to the
  surface ship's monitor showing the submersible camera with a red "LIVE" tag; the cap drifts into frame and settles
  into the scenery, then one dry kicker about the cap. The narrator watches, never intervenes. Use it only in `ocean`.
- Named animal "friends" who get Doug killed: **Buddy** the raccoon (002, raccoon roundworm). Reuse sparingly.

## Series / playlists (config `youtube.playlists`)
- `ocean`: Doug vs. the Ocean (layers, trenches, creatures by depth)
- `parasites`: Doug vs. Parasites
- `prehistoric`: Doug vs. Prehistoric Earth (surviving a night in every era/ocean)
- `places`: Doug vs. Deadly Places (volcanoes, quicksand, sinkholes, caves, deserts, poles)
- `animals`: Doug vs. Animals (venom, animal fights, single-animal deep dives; created 2026-10-09 for ep 010). Proposed standard
  prop: Doug's field guide (a "FRIEND?" box per animal, red "NO" after each death, "MAYBE" for survivals), used in 010 and approved by the art director; reuse it in later `animals` episodes. 011 added a "WIN?" box under FRIEND? for fight episodes (ticked for survivals Doug technically wins).
- **Used-once lines** (don't reuse): "Doug agreed to this. He would like that noted." (011, polar bear; the inversion of "Doug did not agree to this.").
- `compilations`: Full Series & Marathons (stitched 35–60 min and iceberg videos)

## Episode log
| # | Title | Published | Deaths added | Notes |
|---|---|---|---|---|
| 001 | How Doug Would Die in Every Layer of the Ocean | pending (QC passed, awaiting scheduled upload) | 7 (total 7) | Pilot. Survived: Bobbit Worm (cap stolen), Giant Squid, Barreleye, Vampire Squid (glowing goo), Challenger Deep (found a plastic bag). Deaths by zone: sunlight 2, twilight 1, midnight 2, abyss 1, hadal 1. |
| 002 | What Dying From Every Parasite Would Feel Like (working) | pending (QC passed 2026-09-30, awaiting scheduled upload) | 11 (total 18) | Counter 7 to 18, one death per item, no survivals. Act 1 in costume (jewel wasp, zombie ant fungus, horsehair worm, broodsac, toxoplasma), act 2 "Human hosts." (blood flukes, kissing bug, malaria, raccoon roundworm, sleeping sickness, brain-eating amoeba). Introduced the costume gag and Buddy the raccoon. |
| 003 | How Doug Would Die in Every Mass Extinction (working) | pending (QC passed 2026-10-01, awaiting scheduled upload) | 9 (total 27) | Counter 18 to 27, Big Five in order. Survived: Ozone Hole (sunburn), Pangaea Splits ("Doug is fine."). Introduced the time machine. Befriended the moss and a Lystrosaurus; one costume callback (ammonite); marshmallow then fire extinguisher at the volcanic extinctions; cap ends as a fossil in the iridium layer. |
| 004 | What Dying in Every Deadly Place on Earth Would Be Like | pending (QC passed 2026-10-01, final package approved, awaiting scheduled upload) | 9 (total 36) | Counter 27 to 36, 11 places in severity bands "Hours." / "Minutes." / "Seconds.". Survived: Lake Natron (flamingo costume, a costume-gag callback) and Lake Maracaibo ("Doug is fine."). Introduced Doug's stickered suitcase (`places`). Lake Nyos played straight with no joke. Boss: Nyiragongo lava lake. Shorts held pending crop fixes. |
| 005 | The Creepiest Fossils That Still Look Alive | pending (QC passed 2026-10-02, final package approved, awaiting scheduled upload) | 10 (total 46) | Counter 36 to 46, 12 finds ordered by age (28 kyr to 506 Myr) in two bands, "Frozen." / "Stone.". Rule: the fossil is the spoiler, and Doug visits each find on its last day by time machine. Survived: Blue Babe ("Doug is fine.", narrator disappointed). Zhùr the wolf pup played straight with no death and no joke. Befriended Sparta and the Gogo fish. Costume gag once (squid, ichthyosaur). One Devonian-reef callback to 003. Boss: Stanleycaris (three eyes, brain preserved). New poses: thumbs_up, sit_thumbs_up. |
| 006 | The Most Disturbing Discoveries at Every Depth of the Ocean | pending (QC passed 2026-10-04, final package approved, awaiting scheduled upload) | 10 (total 56) | Counter 46 to 56, 12 discoveries ordered by depth (20 m to 9,533 m). Survived: crop circles and the golden orb. Sharks never hurt Doug. Befriended at items 1, 8 and 12. Introduced the LIVE-feed closing image for `ocean` episodes. Boss: 9,533 m deepest ecosystem. |
| 007 | What Dying Every Time Earth Froze Would Be Like | pending (QC passed 2026-10-05, final package approved, awaiting scheduled upload) | 9 (total 65) | Counter 56 to 65, 11 freezes ordered by age (1816 to about 2.4 Ga) in four bands: "Cold snaps.", "Ice age.", "Deep time.", "Snowball.". Survived: Frost Fairs ("Doug is fine.") and Sturtian (narrator quietly disappointed). Befriended the Dryas flower, Meganeura and the algae (algae pays off at the boss). Introduced the FROZEN globe meter next to the counter (monotonic, episode-specific). One callback each to 003 and 004. Ending: time machine returns to 2026 as an ice block, used once. Boss: the first Snowball (Huronian, possibly caused by life). |
| 008 | How Every Step of the Ocean Food Chain Would Kill Doug | pending (QC passed 2026-10-05, final package approved, awaiting scheduled upload) | 9 (total 74) | Counter 65 to 74, 11 food-chain steps. Survived: Giant Trevally (miss) and the orca (ends with the cap under a new owner). Boss: orca. |
| 009 | What Dying in Every Prehistoric Ocean Would Be Like | pending (QC passed 2026-10-09, final package approved, awaiting scheduled upload) | 10 (total 84) | Counter 74 to 84, 12 predators by era (508 Myr Anomalocaris to Megalodon) in three spoken bands "Paleozoic." / "Mesozoic." / "Cenozoic.". Introduced the NIGHT CLOCK ("DOUG LASTED", moon icon) beside the counter, episode-specific, shrinking from hours to 3 s. Survived: Endoceras ("Doug is fine.") and Xiphactinus (narrator had already written a death). Callbacks to 003 and 008 (moray, sperm whale, food chain). Boss: Megalodon (highest trophic level ever measured). |
| 010 | How Every Deadly Venom Would Kill Doug | pending (final package approved 2026-10-09 after s286 fix, QC clean; awaiting scheduled upload) | 9 (total 93) | Counter 84 to 93, 12 venomous animals on a severity axis in three spoken bands "Pain only." / "Slow killers." / "Fast killers.". First `animals` episode; introduced Doug's field guide (FRIEND? / NO / MAYBE). Inverted the costume gag once (cat costume vs funnel-web). Survived: platypus ("Doug is fine."), bullet ant (less sure), inland taipan (narrator quietly deletes the death). Callbacks to 001 (cone snail) and in-episode (saw-scaled viper at the taipan). Ends with ghost Doug asking "friend?". Boss: box jellyfish. |
| 011 | Every Animal Doug Could Beat in a Fight, Until He Dies | pending (QC clean, final package approved 2026-10-09, awaiting scheduled upload) | 7 (total 100) | Counter 93 to 100, the first time we reach 100. 10 animals on a severity axis in three spoken bands "Doug wins." / "Doug loses." / "No contest.", framed by the real "which animal could you beat" polls. Survived: goose (cap stolen, Doug briefly capless, cap recovered), house cat ("Doug is fine.", less sure), gorilla (no fight; narrator had the death drawn already). Field guide gained a WIN? box. Callbacks to 010 (platypus, death drawn already). Hippo deliberately held back for a future episode (outro hook). Boss: African bush elephant (death 100). |
| 012 | What Dying in Every Natural Trap Would Be Like | pending (QC clean, final package approved 2026-10-09, awaiting scheduled upload) | 7 (total 107) | Counter 100 to 107, 9 traps on a duration-of-entrapment axis (minutes to 230 Myr) in three spoken bands "Short stay." / "Long stay." / "Permanent stay.". Second `places` episode (suitcase, 7 stickers). Survived: Brinicle (sea-star costume; "the sticker had already been printed") and Dead Sea Sinkholes ("Doug is fine."). Costume gag twice (sea star, gall mite). Callbacks to 004 (Morecambe Bay) and 002 (ant costume). Real deaths (Antelope Canyon 1997, Tsanfleuron) on sober cards, no Doug, no jokes. Boss: Triassic amber; "preserved" death variant (capless upright Doug mid-wave in the bead, cap on top), approved one-off, not a precedent. |
| 013 | Why Hippos Get Deadlier the Closer Doug Gets | pending (final package approved 2026-10-09; post-fix re-render and visual re-screen pending) | 7 (total 114) | Counter 107 to 114, 10 items on a distance axis (11,000 km to 0 m) in three spoken bands "Far away." / "On land." / "In the water.". First single-animal deep dive; pays off 011's held-back hippo (one callback, opener). Episode-only DISTANCE TO HIPPO meter (monotonic). Survived: Cocaine Hippos ("Doug is fine."), The Honk ("Doug is fine. Probably.", dung spray), The Red Sweat (sunburnt; "Doug survived this one, which was not the plan."). Cap sits upright on the empty canoe seat; closing cap drifts past hippo ears. Field guide HIPPO: FRIEND? NO. Boss: The Mouth (lettuce "accepted"; cut to black). Thumbnail: VEGETARIAN hero yawn + lettuce. First T6 gradient title. |
