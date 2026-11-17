# 050 decisions

## 2026-11-17, creative director: script approved (draft 2 + CD polish)
- Screener PASS on draft 2 (facts zero errors; opening 8, structure 8, voice 8; 2,123 words, about 10.9 min). All nine draft 1 fixes verified.
- Would I click and keep watching: yes. The opening is a concrete image ("octopuses punching fish"), the payoff promise (6,957 m) lands by about 0:09,
  "The Punch." is at words 33-34, and the escalation is a clean monotonic depth gradient with four spoken bands. Death/survival rhythm
  (dies, fine, fine, dies, fine, dies x4) avoids a dead middle, and the Brooder's sober card gives the one quiet beat before the bottom band.
- **Garden death signed off: depth, not steam.** The brief asked for "cartoon steam" at the warm vent. The source puts the vents at about 11 °C,
  so steam would be a false image. The new line ("it was warm, but it was also three thousand two hundred meters down, and the suit was not
  built for that") is accurate and sets up "The last stop is more than twice as deep." Staging: no steam, no scalding; the "faint shimmer over the
  cracks" is allowed (it is real seep shimmer), but the art must not draw it as boiling.
- CD polish applied (no fact changes, about -3 words):
  1. Punch: "its arms and body instead of its brain" -> "their arms and body instead of their brain".
  2. Mimic: "Its body is only about six centimeters long" -> "Its body only grows to about six centimeters long" (the figure is a maximum).
  3. Brooder: "Down there the water is cold, and cold slows everything down" -> "Down there, the chill slows everything down".
  4. facts.md: SeaLifeBase added as the institutional source for the mimic size.
- Notes for the director/art: the cap goes onto the shell pile at the Thrower and is simply back on Doug at the Blanket (standard cap-survives
  rule; do not stage a retrieval). Seven Arms death cuts on "started at the top": no bite shown. The Deepest sub crumples with no Doug visible.
  No cute eyes or smiles on any octopus (kid-appeal risk on an octopus episode is higher than usual).
- Playlist `ocean` (playlist reset after three `animals`). Counter 374 -> 380.

## 2026-11-17, director: shotlist (214 shots), asset requests (53), Shorts picks
- HUD on every story shot: DOUG DEATHS (1590,162), `depth_icon` + DEPTH label (1590,238, stamped red-on-pink at item 9),
  and an episode-only "ARMS: 8" size-28 label at (1590,284). The reserved zone therefore runs to y ~300 (wordart and labels
  over x 1300-1860 stay at glyph top ≥ 312; checked in the generator). The ARMS edit is a full-frame cream card at s120
  ("has eight arms."): 8 struck out, "7?" written, "7?" struck out, 8 rewritten, with `narrator_hand_pencil`; the HUD stays 8.
- Backgrounds follow the ocean ramp: items 1-4 surface `#3a9ad9` (reef / open sand / shell bed / blue open water with a
  sky strip), item 5 twilight `#1b4f86`, item 6 `#0f2a4f` (037's ~1,000 m step), items 7-8 midnight `#0b2447` (canyon wall,
  then seamount slope), item 9 hadal `#020308`. s190 ("more than twice as deep") is a tall 1920x2700 `pan_down` from 3,200 M to 6,957 M.
- Section headers ("The reef." / "Open water." / "The deep." / "The bottom.") are white 140 px header cards, `topbar: false`.
- Cap continuity, logged one-offs: s072 Doug sits capless (`cap_off`) while `doug_cap` sits on the shell pile (one cap per
  frame); the cap is simply back from item 4 (CD note). s157 brooder death: `on_back` with `cap_taken` and `doug_cap` on his chest
  (the script's "cap on his chest"). Death images: goatfish / man-of-war / jelly / suit costumes flat with printed X eye and the cap on
  top (375, 376, 377, 379); 378 Doug `on_back` dead; 380 crumpled sub with no Doug visible, then ghost Doug at the LIVE monitor.
- Seven Arms death cuts on "started at the top": s137 is the hold with shake, s138 ("Doug has died. Again.") is the flat costume. No bite.
- Garden: shimmer over cracks is pale blue `#8fb8d8` wavy lines, no steam, no boiling (CD note).
- Sober beats s158-s160 on `#15181a`: no Doug, no counter, white "53 MONTHS", the empty egg cases, the optic-gland diagram.
- s001 `scene_ref: thumbnail` waits for the graphic designer's thumbnail.json (validate flags it until then).
- Shorts: short01 Brooder s146-s157 with hook (53 months, ends "Doug ran out first."), short02 Blanket s083-s094 with hook
  (size gap, ends on the death payoff), short03 Deepest s192-s201 (6,957 m opener, ends on 700 kg per thumbnail). Titles and
  descriptions are left blank for the youtube-titler.

## 2026-11-17, creative director: package approved (thumbnails A/B/C + ranked titles)
- `validate packaging` OK, `package check` OK. Pairings: A "The Creepiest Octopus at Every Depth, Down to 6,957 Meters" + IT PUNCHES;
  B "Why Octopuses Get Creepier All the Way Down to 6,957 Meters" + IT LIVES HERE; C "Every Reason the Octopus Is the Ocean's Creepiest Animal" + 53 MONTHS.
  Each text adds to its title rather than repeating it (no OCTOPUS/CREEPIEST/DEPTH/6,957 on the images).
- **A fixed by CD before approval:** Doug + goatfish costume scaled 0.42 -> 0.80 and moved to (185, 640) in `thumbnail.json`, re-rendered.
  At 168 px Doug was a speck; now the cap, shocked face and costume read, and the octopus's arm tip lands on his face, so "IT PUNCHES"
  is shown, not just said. Octopus eyes are half-lidded and menacing, no smile: eerie, not cute.
- B: approved as is. Yellow sub against black reads instantly at feed size, dent cracks visible, red cap in the porthole, the dumbo is
  pale and blank-eyed (no mascot face). Strongest peril image of the three.
- C: approved as is. Beard + calendar pages tell the waiting joke at a glance; the mother's fate is not drawn. Weakest of the three at
  small size (Doug's face is small) but the 53 MONTHS text carries it.
- Policy: cartoon only, no gore, no kid-coded cuteness, titles promise what the video delivers (depth gradient to 6,957 m, the punch,
  the 53-month brooder are all in the script).
- 2026-11-17: packaged. Script 2 rounds (fact fixes), art 3 rounds (arm sac redraw, keyframe fixes), thumbnails approved after A Doug upscale. Risks: sourcing partly via press releases; no-Doug title test continues.
