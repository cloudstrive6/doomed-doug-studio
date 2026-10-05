# Visual review: 007-every-time-earth-froze

## History
- **Round 1 (2026-10-05), keyframes: FAIL.** 14 blocking and 8 should-fix items. The worst were white-ink Doug vanishing on ice (s036-s038, s050, s051), a mask-rect notch in the horizon (s238), the medal covering Bretz's face (s120, s125), and text collisions and occlusions (s003, s040/s054/s055, s044/s046, s088, s110, s114, s118, s147/s172/s195, s189, s223). Other items: a floating Doug (s214), a weak tsunami (s071), and two runs of near-identical compositions (s062-s065, s238-s244).

## Round 2 (2026-10-05)

Keyframes were re-rendered from the current shotlist with `python -m studio keyframes`, because the old contact sheets had been overwritten by an s001-only run. All 23 sheets and 276 shots were inspected, with full-resolution crops of the round-1 shots and of any new suspects.

### Keyframes

VERDICT: FAIL (one small required fix. Only the listed shots need re-checking.)

Round-1 items verified as fixed: 1 (Doug is black-ink and readable in s036-s038, s050, s051), 2 (s238 horizon is clean), 3 (medal on Bretz's chest in s120 and s125), 4 (s118 label is clear), 5 (s114), 6 (card text sits inside the border in s040, s054, s055), 8 (s214 Doug at the water surface), 9 (s223 has one range tag), 10 (s147, s172 and s195 counter and badge are clear), 11 (s110), 12 (s044 and s046 wordart is in the water and ice), 13 (s071 uses the blue wave), 14 (s189 "CLOSE TO FREEZING" is outlined wordart), 15 (s059, s062, s073 and s134 wordart is off the map), 16 (s024 bottle is in hand), 17 (s185 canopy is visible), 18 (s142 bubble tail points at Doug), 19 (s003), 20 (s060, s061, s133 and s137 feet are on the line), 21 (s064 punch-in, and the pond run now varies between wide, close-up, time machine and gravestone).
Partly fixed and accepted: 22 (s104 and s105 still use the plain green map, but the border line and the CANADA/USA/WASHINGTON/IDAHO labels now place it).

Required:
1. **s076: the red walking arrow runs straight through the "NETHERLANDS" label, so the word looks struck through.** (director)
   Fix: end the arrow before the label (arrow head at x≈1440, y≈480 in 1920 space), or move the label up about 70 px so the arrow passes under it.

Should fix (do with item 1, not blocking):
2. **s047: Doug stands in the river directly under the right-hand pillar of the 1831 bridge, so the pillar ends in his cap and looks like it is stabbing his head.** (director) Move Doug about 120 px left, into the gap between pillars (x≈1430-1460), or drop him in front of the pillar's base.
3. **s088: the "NORTH ATLANTIC" label still straddles the map's right border (it is about 60 px outside the frame line).** (director) Move it about 80 px left so the whole box sits inside the map, over the Atlantic.

Checked and OK this round: no gore (ice-block and ghost deaths only), adult deadpan tone, Doug on-model throughout, the death counter runs 56 -> 65 at the right shots, the s001 opening image is the approved grid, and there are no new runs of 4 or more near-identical compositions.

### Thumbnail (build/thumbnail.png, archetype A 3x3 grid)

VERDICT: PASS

Checked at 1280x720, 320x180 and 168x94:
- At 320x180 all nine labels are readable, and every tile is a distinct saturated colour block. At 168x94 the grid still reads as a table of contents with nine colour blocks, and the white ball on navy is clearly the boss tile. The labels are soft but mostly decodable, which is normal for this archetype.
- The format matches style bible 2.A: white canvas, black rounded frames, comic labels and no title text. Doug appears small in one tile only.
- Policy: no gore, nothing misleading. Every tile depicts something that is in the episode. Not kids-coded.
- Complements the title: the labels are chapter names, and there is no "Snowball Earth" label.

Recommended polish (graphic designer, optional, not blocking):
4. **Tile 1 (Year Without a Summer): at 168 px the ice block around Doug disappears, so he reads as relaxing in a deck chair rather than frozen. The tile carries the only "dying" cue for the title.** Give the ice block a pale-blue fill (about #cfe9ff at 60%) and a 5-6 px blue outline so "frozen Doug" survives feed size.
5. **Tile 8 (Sturtian): the lone time-machine door on yellow is a grey rectangle at feed size and says nothing about a freeze.** Replace it with the Sturtian payoff, Doug in the meltwater pond with the algae on white ice, or at least add a white ice ground so the tile reads as cold.
6. **The "Year Without a Summer" label is set smaller than the others and is the least legible at 168 px.** Raise it one size if it fits the tile width. Otherwise leave it.
7. Note: "Antarctica Freezes" shares a stem with "Froze" in the title. This is acceptable because it is the chapter name. Flagged only for the creative director's awareness.
