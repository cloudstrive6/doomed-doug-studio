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

## Round 3 (2026-10-05)

Re-checked keyframes s001, s042, s044, s047, s076, s088, s132, s179, s180, s232, s233 and s261 at full resolution, plus `build/thumbnail.png` at 1280x720, 320x180 and 168x94.

### Keyframes

VERDICT: PASS

- Item 1 (s076) is fixed. The arrow ends at about y≈520, below the NETHERLANDS box, so the word is no longer struck through.
- Item 2 (s047) is fixed. Doug stands on an ice floe to the right of the last pillar, and no pillar touches his cap.
- Item 3 (s088) is fixed. The NORTH ATLANTIC box sits fully inside the map frame, over the ocean.
- s042, s044, s132, s232, s233 and s261 are clean. Text is legible and does not collide, Doug is on-model and readable, and each drawing matches its narration. s132 has nine towers stacked to the "3 KM" mark.
- Optional, not blocking (director): in s179 and s180 Doug's feet are at about y≈735 while the ground line is at y≈760, so he hovers slightly above the jungle floor. Set Doug's hip y about 25 px lower in both shots if anyone touches them again.

### Thumbnail (build/thumbnail.png and keyframe s001)

VERDICT: FAIL (one regression from the polish pass, a one-line fix)

- Year Without a Summer tile is fixed. The pale-blue ice block with its blue outline survives at 168x94, and Doug clearly reads as frozen in the deck chair.
- The other tiles are unchanged and still PASS. All labels read at 320x180, and the grid reads as nine distinct colour blocks at 168x94.

Required:
1. **Sturtian tile (thumbnail.json, the `doug` element at x=590, y=612, pose "float"): Doug's body, arms and legs render in white ink.** The engine's auto-contrast switched to white because his hips sit on the dark pond. On white ice and a yellow sky the white limbs vanish, so at feed size the tile reads as a floating head over the pond. This is the same white-Doug-on-ice problem that blocked round 1, and it also shows in keyframe s001. (graphic designer)
   Fix: add `"ink": "#000000"` to that doug element. The water ellipse drawn after him (x=645, y=624) already hides his legs below the waterline. Then re-render `python -m studio thumbnail` and keyframe s001, and confirm that the black torso and arms show above the water at 168x94.

### Round 3 fix: thumbnail ink applied

VERDICT: PASS

- Sturtian tile: added `"ink": "#000000"` to the `doug` element (x=590, y=612, pose "float") in thumbnail.json. Re-rendered `python -m studio thumbnail` and keyframe s001.
- At 1280x720, 1920x1080 (s001) and 168x94, the black torso and arms show clearly above the pond, and the tile now reads as Doug floating in the meltwater pond rather than as a floating head.
- Optional, not blocking (graphic designer): now that the legs are black, two small leg tips show below the pond's bottom outline at the tile's bottom border (about y≈960 in s001). They are invisible at 168x94. Raise Doug a little or widen the lower water ellipse if anyone touches the tile again.

## Post-render review (final.mp4, thumbnail, Shorts)

What I checked: all 33 frames in `build/samples/` (taken every 30 s, starting at 15 s), mapped to their shots with `timing.json`. Frames at full resolution for s116, s249, s255 and s064. `build/qc.json` (no problems, 997.7 s). `build/thumbnail.png` and `thumbnail_small.png` against the title in `metadata.json`. The three `build/shorts/*_preview.png`. One frame every 2 s from each of `short01.mp4`, `short02.mp4` and `short03.mp4` (1080x1920).

### Main video: VERDICT: PASS
- No black, blank, frozen or glitched frames. Chapter labels are legible in every sample. Doug is on-model in all of them (red cap, white head) and readable on every background, including the dark-navy space shots and the brown greenhouse shot.
- Every picture matches its narration. Two examples: s249 starts as a blank clock face, then the hands, "1 DAY" and "ABOUT 11 AM" appear. s255 shows the METHANE circle, a red X and an arrow to CARBON DIOXIDE and WATER. The X partly covers the H in METHANE, but the word is shown clean first, so this is fine.
- No gore. The deaths are cartoon (the frozen-in-ice end card in s271). Nothing reads as a kids' show.
- Optional (director): in s116 and s117 (frame at about 6:44) the dam inset fills only the left third of a white frame, which leaves a lot of dead space. This is acceptable because the REPEAT panels fill in during s117.

### Thumbnail: VERDICT: PASS (unchanged from the round 3 approval)
- The nine labelled freeze tiles are legible at 320x180, and Doug is frozen in the deck chair in the top-left tile. It complements "What Dying Every Time Earth Froze Would Be Like" without repeating its words, and it is not misleading.

### Shorts: VERDICT: FAIL
Titles, subtitles, the @DoomedDoug tag and the end card all pass. The title is red with a black outline and readable. Subtitles stay at 2 lines or fewer. On the end card, the red arrow points down to the link and Doug is pointing at it. The failure is that Shorts keep only x 260..1660 of the 1920 frame, and several shots put Doug or a key drawing outside that band:

1. **short01, s108 (director):** the CN Tower is at x=1680, so its label is cut to "CN TOW". This is the payoff comparison of the Short ("deeper than the CN Tower"). Move the `cn_tower` asset and the `CN TOWER` label to x=1580. That still clears the ice dam, whose right foot is at x=1480.
2. **short03, s256 and s262 (director):** Doug is at x=1700, and in the Short he is sliced in half at the right edge. Set Doug's x to 1560 in both shots. The globes end at x≈1180 (s256) and x≈960 (s262), so nothing collides. In s262, check that he stays clear of the OXYGEN MAKERS label and the microbe.
3. **short03, s258 (director):** Doug is at x=1750 and is completely off-screen in the Short, apart from a red sliver of cap. Set Doug's x to about 1600 (y unchanged), or scale `north_america_map` to 0.85 and move it to x=820 so he has room inside the safe band.
4. **short02, s047 (director):** Doug is at x=1770 and is off-screen during "a new bridge with only five arches". Set his x to 1560. Optional: in s044, move the `question_mark` from x=1780 to 1560 so the "strange part" beat shows Doug puzzled.
5. **short01, s106 (director, minor):** in the hook frame, Doug at x=1790 is off-screen. Set his x to about 1600.

After these shotlist fixes, run `python -m studio shorts render 007-every-time-earth-froze`. All of these x positions are also safe in the 16:9 frame. Re-rendering final.mp4 is optional: the only change there is that Doug sits about 150 px further left in 6 shots. Either re-render final.mp4 for consistency or accept the small difference.

## Post-render review, round 2 (re-render 12:10 UTC: final.mp4, thumbnail, Shorts)

What I checked: all 33 frames in `build/samples/` (taken every 30 s), plus `build/qc.json` (no problems, 997.7 s). `build/thumbnail.png` and `thumbnail_small.png` against the title in `metadata.json`. The three `build/shorts/*_preview.png`. One frame every 2 s from each of `short01.mp4` (48.0 s), `short02.mp4` (55.9 s) and `short03.mp4` (53.9 s), all 1080x1920. I also checked every Shorts shot in shotlist.json for Doug, asset or label x positions outside the safe band of x 330..1590.

The round 1 Shorts fixes are all in the shotlist and in the render. s047 Doug is at 1460. s044 has the question mark at 1470 and Doug at 1560. s106 Doug is at 1600. In s108 the CN Tower is at 1570 and its label at 1540, and "CN TOWER" now reads in full in short01. In s256 and s262 Doug is at 1560, and in s258 he is at 1580 with the map scaled to 0.9 at x 860. Doug is fully visible in all of these.

### Main video: VERDICT: PASS
- No black, blank, frozen or glitched frames.
- Chapter labels are legible in every sample.
- Doug is on-model in all of them and readable on every background, including the navy space shots and the brown greenhouse shot.
- The pictures match the narration.
- The deaths are cartoon only, ending on the frozen-in-ice end card. There is no gore and nothing reads as a kids' show.
- The 6 shots moved for the Shorts still look natural in 16:9 (for example, s108 CN Tower and s256 Doug).

### Thumbnail: VERDICT: PASS
- The 3x3 grid of freeze tiles is unchanged from the round 3 approval. Every label reads at 320x180.
- Doug is frozen in the deck chair in the first tile, and in the Sturtian tile his black ink body reads clearly.
- It complements the title without repeating its words.
- Note, not blocking (youtube-titler): `metadata.json` → `thumbnail_brief` still describes the old archetype-B ice-core column, but the approved thumbnail is the archetype-A grid. This is internal text only. Update it if anyone touches metadata.

### Shorts
**short02: PASS.**
- The title is readable and subtitles stay at 2 lines or fewer.
- The end card arrow points down, with Doug pointing at it.
- s047 is fixed: Doug is on the new bridge.
- Optional (director):
  - In s048 Doug is at x=120, so he is off-screen in the Short during "new embankments made the river deeper". The narration does not need him there.
  - In s053 ("Doug is fine") the `printed_card` at x=1680 is cut in half at the right edge. Moving Doug and the card about 120 px left would show the card he is holding.

**short03: PASS.**
- s256, s258 and s262 are fixed: Doug is fully inside the frame.
- The title, subtitles, end card and arrow all pass.
- Optional (director): in s260 the scientist (x=300) and Doug (x=1650) touch opposite edges. Both are fully visible and readable.
- s264's FROZEN meter sits outside the crop. This is acceptable because the Short's narration does not refer to it.

**short01: FAIL.** One shot left with the same Doug-sliced-at-the-edge defect as round 1:
1. **short01, s111 (director):** "When this one failed, the whole lake emptied in about two days." Doug is at x=1700 (scale 0.55), and in the Short only half of him shows at the right edge (frame at about t=18 s) while the dam bursts. Set the `doug` element's x to 1560, y unchanged. The dam's right foot is at about x=1440, so he still clears it. This is also safe in 16:9.
   - Optional while there:
     - s110: check that `warning_triangle` (x=300) is not clipped at the left edge, and move it to x=400 if it is.
     - s116: the dam inset is clipped at the left edge in the Short. Move the inset group about 150 px right.

After the fix, run `python -m studio shorts render 007-every-time-earth-froze` (only short01 changes) and re-screen short01 around t=16–20 s. Re-rendering final.mp4 is optional: in 16:9 the only change is Doug sitting 140 px further left in s111.

Main video and thumbnail: PASS. short02 and short03: PASS. short01: FAIL (s111 Doug x 1700 → 1560).

VERDICT: FAIL

## Post-render review, round 3 (short01 re-render 12:21 UTC)

What I checked: `build/shorts/short01_preview.png`. Frames from `short01.mp4` (1080x1920, 48.0 s) at t = 8, 10, 12, 14–22 (every 1 s), 19.3, 19.6, 19.9, 24–40 (every 2 s), 44 and 47 s. A full-resolution crop of the right edge at t=18.5 s. The s106–s117 elements in `shotlist.json`.

**s111 fix is confirmed.** In `shotlist.json`, the s111 `doug` element is at x=1560 (y=700 and scale 0.55 unchanged).
- In the Short (t≈17–19.6 s), Doug is fully in frame in his panic pose: cap, head, raised arms and both feet, with about 70 px clear of the right edge.
- He stands just right of the bursting dam and does not touch it.
- The "ABOUT 2 DAYS" label appears at about t=19.5 s and is fully visible.
- This matches "When this one failed, the whole lake emptied in about two days."

**s110:** `warning_triangle` (x=300) and "NOT BUILT TO LAST" are both fully visible at t≈15 s, so the left edge does not clip them. Doug is on top of the dam and on-model.

**s116/s117 (optional item from round 2, not taken up):**
- The left inset (DAM FORMS) is cut at the left edge, and in s117 the BURST/REPEAT inset is cut at the right edge.
- The DAM FORMS, LAKE FILLS and REPEAT labels, the tally marks and "DOZENS OF TIMES" all read in full, so the beat still lands.
- Not blocking.

**Rest of short01:**
- The title is readable throughout.
- Subtitles stay at 2 lines or fewer, legible on every background.
- The hook (s106) and the s108 "CN TOWER" frame look as they did in round 2.
- In s112, Doug runs from the wall of water fully in frame.
- On the end card, the red arrow points down to the link and Doug is pointing at it.
- There are no black, blank or glitched frames and no gore.

Long video, thumbnail, short02 and short03 passed in round 2 and have not changed. short01: PASS.

VERDICT: PASS
