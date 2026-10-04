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
  channel. Current total: **46** (7 after 001, plus 11 in 002, plus 9 in 003, plus 9 in 004, plus 10 in 005, QC passed; update after every episode). The next episode's
  counter starts at 46.
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
- **Doug's suitcase** (from 004): a battered MS Paint suitcase that is the standard prop of the `places` playlist,
  the way the time machine belongs to `prehistoric`. Doug carries it into the opener with no stickers on it. Every time he
  dies at a place, a crude travel sticker with the place's name (for example "DEATH VALLEY") lands on it. Survivals get
  no sticker. The episode ends on the full suitcase next to the cap, and the outro may say "The suitcase still has room."
  It always survives and is never explained. The art director owns the drawing. It is a stickered travel variant and must
  stay distinct from the over-packed `assets/library/suitcase.json` ("HEAVY" tag). Use it only in `places` episodes.
- Named animal "friends" who get Doug killed: **Buddy** the raccoon (002, raccoon roundworm). Reuse sparingly.

## Series / playlists (config `youtube.playlists`)
- `ocean`: Doug vs. the Ocean (layers, trenches, creatures by depth)
- `parasites`: Doug vs. Parasites
- `prehistoric`: Doug vs. Prehistoric Earth (surviving a night in every era/ocean)
- `places`: Doug vs. Deadly Places (volcanoes, quicksand, sinkholes, caves, deserts, poles)
- `compilations`: Full Series & Marathons (stitched 35–60 min and iceberg videos)

## Episode log
| # | Title | Published | Deaths added | Notes |
|---|---|---|---|---|
| 001 | How Doug Would Die in Every Layer of the Ocean | pending (QC passed, awaiting scheduled upload) | 7 (total 7) | Pilot. Survived: Bobbit Worm (cap stolen), Giant Squid, Barreleye, Vampire Squid (glowing goo), Challenger Deep (found a plastic bag). Deaths by zone: sunlight 2, twilight 1, midnight 2, abyss 1, hadal 1. |
| 002 | What Dying From Every Parasite Would Feel Like (working) | pending (QC passed 2026-09-30, awaiting scheduled upload) | 11 (total 18) | Counter 7 to 18, one death per item, no survivals. Act 1 in costume (jewel wasp, zombie ant fungus, horsehair worm, broodsac, toxoplasma), act 2 "Human hosts." (blood flukes, kissing bug, malaria, raccoon roundworm, sleeping sickness, brain-eating amoeba). Introduced the costume gag and Buddy the raccoon. |
| 003 | How Doug Would Die in Every Mass Extinction (working) | pending (QC passed 2026-10-01, awaiting scheduled upload) | 9 (total 27) | Counter 18 to 27, Big Five in order. Survived: Ozone Hole (sunburn), Pangaea Splits ("Doug is fine."). Introduced the time machine. Befriended the moss and a Lystrosaurus; one costume callback (ammonite); marshmallow then fire extinguisher at the volcanic extinctions; cap ends as a fossil in the iridium layer. |
| 004 | What Dying in Every Deadly Place on Earth Would Be Like | pending (QC passed 2026-10-01, final package approved, awaiting scheduled upload) | 9 (total 36) | Counter 27 to 36, 11 places in severity bands "Hours." / "Minutes." / "Seconds.". Survived: Lake Natron (flamingo costume, a costume-gag callback) and Lake Maracaibo ("Doug is fine."). Introduced Doug's stickered suitcase (`places`). Lake Nyos played straight with no joke. Boss: Nyiragongo lava lake. Shorts held pending crop fixes. |
| 005 | The Creepiest Fossils That Still Look Alive | pending (QC passed 2026-10-02, final package approved, awaiting scheduled upload) | 10 (total 46) | Counter 36 to 46, 12 finds ordered by age (28 kyr to 506 Myr) in two bands, "Frozen." / "Stone.". Rule: the fossil is the spoiler, and Doug visits each find on its last day by time machine. Survived: Blue Babe ("Doug is fine.", narrator disappointed). Zhùr the wolf pup played straight with no death and no joke. Befriended Sparta and the Gogo fish. Costume gag once (squid, ichthyosaur). One Devonian-reef callback to 003. Boss: Stanleycaris (three eyes, brain preserved). New poses: thumbs_up, sit_thumbs_up. |
