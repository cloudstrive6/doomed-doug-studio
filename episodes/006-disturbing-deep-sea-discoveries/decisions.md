# Decisions: 006 Disturbing Deep Sea Discoveries

## 2026-10-04: script gate (draft 2), APPROVED
- Screener round 2: PASS, no required fixes. Facts 0 errors, hook 8, structure 8, voice 8, policy 0 items.
- Checked against the brief: depth axis 20 m to 9,533 m, 12 items, gauge drops at every item, "Sunlit." / "Pitch black." /
  "Rock bottom." headers (the last at about 65%). "The Sharkcano." is at spoken words 31-32 and the twist lands at about word
  140 (inside 0:45). Counter 46 to 56 with survivals at the crop circles and the golden orb. Befriending at 1, 8 and 12, the
  cap survives at 1, 5, 6, 9 and the finale, one 001 callback, no costume, suitcase or time machine. Nothing from 001's item
  list returns. Sharks never hurt Doug. Brine, acid, heat and pressure deaths are all cartoon with zero bodily description.
  Mining is neutral and dark oxygen is stated as contested (both sides plus the April 2026 editor's note). The golden orb is
  identified (NOAA/Smithsonian, April 2026), so it plays as the anticlimax and the "unexplained" promise rests honestly on
  Kavachi's sharks, Taam Ja', the Upsweep and dark oxygen. The working title does not say "Can't Explain".
- CD polish applied myself (no fact changes): line 37 "They were swimming inside the crater" became "That's the crater"
  (removes the repeated "swimming inside"); line 151 kicker now opens "A hundred and twenty thousand years of venting."
  (removes the echo of line 141); line 25 split into two sentences ("...standing on end. That's how close..."). Footer
  stats updated: 3,173 words, about 16:16, inside the 3,100-3,400 target.
- Lore: the "LIVE" feed ending is adopted as the standard closing image for `ocean` episodes (series bible updated).
  The death count (46 to 56) and the episode-log row go into the series bible at QC, per existing practice.
- Notes for the director/editor: the fingernail pressure analogy is used twice on purpose (two men at 1,600 m, a small car
  at 9,533 m); stage it as a visual callback. Respell "Taam Ja'" in the TTS input if Chirp mispronounces it.

## 2026-10-04: thumbnail + Shorts titles, APPROVED (CD side)
- Thumbnail (`build/thumbnail.png`, `thumbnail.json`): approved with no changes. Archetype A 3x3, white canvas, depth-ordered
  tiles turquoise to navy to black, boss "9,533 m" bottom-right with red glow, tiny Doug in the brine lake as the one
  human-for-scale gag. No label repeats a title or alt-title word (title = depth frame, grid = items). Readable at 320 px and
  168 px: every subject keeps its silhouette, and labels are 2 words or fewer. No gore, no shark attack, no Titan imagery.
  Weakest tile is "Blue Hole" (abstract shaft plus "?"), but the label and the "?" carry it, so it stays.
  Labels are short forms of the chapters (Brine Lake = Jacuzzi of Despair, Iron Snail = Scaly-Foot Snail, Tar Volcano = Asphalt
  Volcano, 9,533 m = Deepest Ecosystem). This is accepted because "of" and "Deep" are title words.
  A visual-screener pass on the thumbnail is still required at the package gate.
- Shorts titles and descriptions written by CD (titler job), all sourced in facts.md:
  1. "This Blue Hole Is So Deep the Cable Ran Out First" (Taam Ja', 420 m, Dec 2023)
  2. "The Ocean's Loudest Mystery Sound Turned Out to Be Ice" (Bloop = icequakes; Upsweep still unresolved)
  3. "This Underwater Lake Kills and Preserves Whatever Falls In" (Jacuzzi of Despair)
  `python -m studio shorts validate` OK; `validate metadata` OK.
