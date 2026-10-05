# Visual review: 008-ocean-food-chain

## Round 1: pre-render keyframes (2026-10-05)

Scope: all 321 keyframes (`build/keyframes/s001..s321.png`), re-rendered from the current `shotlist.json` with
`python -m studio keyframes 008-ocean-food-chain` (27 contact sheets). Before that, `build/contact/` held only a stale partial
`sheet_01`. I checked the suspect shots at full 1920x1080.

VERDICT: FAIL

Overall the episode is in good shape. Doug is on-model in every costume (red cap and white head always visible while
he's alive). The death counter climbs correctly, 65 to 74, with exactly 9 deaths (s032, s059, s077, s137, s163, s193,
s219, s247, s277). Both survivals (trevally s111, orca s310/s318) carry no increment. Section cards are consistent
(REEF / OPEN WATER / APEX / NO PREDATORS), the creature drawings are recognisable, and every death is a cartoon death.
s290 (livers removed) is not depicted, which is correct. The tone is never nursery-like. The fixes below are what
blocks a PASS.

### Required fixes

1. **s246, s047, s270, s279: red silhouette glow reads as blood in the water** (director, with art director if needed).
   `glow_r` draws a red speckled cloud around the silhouette. In s246 that cloud sits in the water directly under Doug,
   one shot before his death, so it reads as a blood pool. In s270 the red clouds around the orcas next to the whales
   read the same way. Remove `glow_r` from those four silhouette assets. If the art director prefers to keep a menace
   cue, they can add a non-red glow colour option (for example dark navy or white) and use that instead.
2. **s059: Doug is not identifiable in his own death shot** (director). Only `reef_fish_costume_flat` with X eyes is
   visible, with no cap and no head, so it reads as "a fish died". Every other death keeps the cap (see s032, s219).
   Add `{"type":"asset","name":"doug_cap","x":1080,"y":890,"scale":0.5}` (on the sand at the crack mouth). Keep it in
   s060 too, so the ghost-with-cap and the cap on the floor stay consistent.
3. **s077: same problem as s059** (director). Only `crab_costume_flat` is visible, with no cap. Add `doug_cap` beside
   the crab, for example `x≈1330, y≈890, scale 0.5`. Carry it into s078.
4. **s018: stray zigzag line** (director). The "crack" line `[[1430,600],[1470,650],[1440,700],[1480,740]]` hangs
   below the snail in open water and looks like a drawing error. Move it onto the shell, for example
   `[[1400,500],[1425,535],[1405,565],[1435,600]]` (black, width 4), or use `snail_shell_cracked` as in s032.
5. **s189 and s317: white "flash" blob reads as grey static** (director). The `spray` with r 90–100 and density
   0.4–0.5, at (1500,300) in s189 and (1300,500) in s317, renders as a fuzzy grey noise disc. On s189 it also floats in
   an aerial river view. Replace it with a recognisable camera-flash cue: the `highspeed_camera` asset or a small
   phone/camera icon plus a white starburst. Otherwise remove it, since the "BULL SHARK, 2014" and "2024" labels already
   carry the beat.
6. **s312: "RIP DOUG" on the gravestone is illegible** (director). `red_x` at (1450,450) sits on top of the engraving,
   so the joke ("we are slightly less pleased") loses its setup. Let the text read first. Either shrink the `red_x` to
   about 0.6 and give it `appear: 0.6`, or replace it with a single red diagonal stroke from the top-left to the
   bottom-right corner of the stone that leaves "RIP" and "DOUG" readable.
7. **s060: wordart "INFORMANT" is printed across the grouper's body** (director). The key subject (the head-standing
   grouper) is half covered. Move the wordart to the empty upper right, for example `x 1450, y 330`, below the counter,
   or to the left at `x 520, y 560`.
8. **s061: title "GIANT PACIFIC OCTOPUS" overlaps the octopus head and arms** (director). Move the octopus down or
   right (for example `y 640`), or the title up to `y 250`, so the text sits on clear water.
9. **s105: the red arrow cuts through "HUNT THE SKY"** (director). Start the arrow above the wordart line, or move the
   wordart to `y 230`, so the arrow runs from the fish's nose up into clear sky.
10. **s282: the orca's dorsal fin pokes through "KILLER WHALE"** (director). Move the wordart to `y 250`, or the orca
    down to `y 640`.
11. **s191: the tide table floats about 180 px above Doug's hand** (director). Narration says he is "holding a tide
    table". Move `tide_table` down to Doug's hand height (about `x 790, y 730`) as in s192, and keep the "x2" label
    next to it.

### Advisory (fix if cheap; not blocking)

- **s316, s317 (illustrator/director):** the salmon "hat" sits on the orca's back behind the blowhole, not on its head.
  Shift `salmon` forward to about `x 1180, y 500` so it rests above the eye patch ("like hats").
- **s058 (director):** the moray approaching from the right is a featureless black smear cut off at the frame edge.
  Either use the normal moray asset (as in s059) or keep the silhouette but show the head end.
- **s058–s060 (director):** the head-standing grouper's tail is tucked under the "GIANT MORAY" topbar label. Lower the
  grouper about 40 px.
- **s113, s122, s125 (director):** the title "GOLIATH GROUPER", the "SWALLOWED WHOLE" box and "BOOM" all touch the
  grouper's dorsal fin. Nudge the labels up 30–50 px. On s125, "SWIM BLADDER" has no pointer. Add a short arrow to the
  belly.
- **s015–s019 (director):** the "DOUG DEATHS" counter sits on the slow-motion inset's top-right border. Shrink the
  inset to `w 1500` or start it at `y 220`.
- **s186, s212, s213, s288, s289 (director):** labels or animal icons straddle the map frame border ("TORRES STRAIT",
  "16 MARATHONS", "+1,800 KM", the orcas and the crossed-out shark). Keep them fully inside or fully outside the map.
- **s290 (director):** the red X sits on the east coast (near Durban), not at Gansbaai or over the sharks. Move it onto
  the shark icons, or drop it.
- **s235, s236 (illustrator/director):** the sunrise sun is an unfilled yellow outline arc and reads as a stray curve.
  Fill it (`#ffd54a`) as on the other suns.
- **s299 (director):** "15 OF ~40". The 15 patterned orca icons look almost the same as the 25 silhouettes at
  playback size. Outline the 15 in red or grey out the other 25.
- **s094:** "ILE AUX GOELETTES" is missing its accents (Île aux Goëlettes). Fine if the font can't render them.
- **Variety:** s119–s122 (grouper big close-up on the wreck, four in a row) and s259–s261 (whale on black with click
  arcs) are the closest the episode comes to stale runs. Each shot adds a new label or arrow, so this isn't blocking,
  but one camera move (`zoom_in` on the mouth for s121–s122) would help.

### Not issues (checked)

- s255 ends on a cropped Eiffel Tower at the top edge. That is the end state of its `pan_down` through 6 towers, which
  is intended.
- s158–s160 is an x-ray of the shark's stomach (cans, bottle, sacks). It's schematic and not gore.
- s032, s137, s163, s193, s219, s247, s277 are cartoon deaths (X eyes, cap, splash). No blood, organs or dismemberment.
- s161 "EPISODE 6: 0 SHARK DEATHS" matches the series bible (006: "Sharks never hurt Doug").

Re-screen after fixes: re-run `keyframes --shots` on the changed ids and send me the new sheets.

## Round 2: keyframe fixes re-screen (2026-10-05)

Scope: the 70 changed shots (the director's list; a diff of `shotlist.json` against the previous commit confirms exactly
these 70 ids changed), viewed on the 6 contact sheets and at full size where in doubt. Unchanged shots: I re-rendered a
sample (s001, s032, s111, s160, s219, s255, s277, s310) and every one is pixel-identical to its round-1 render, so the
round-1 fixes broke nothing outside the changed set. (I re-ran `keyframes --shots` on the 70 ids afterwards, so
`build/contact/sheet_01..06` again shows the changed set.) I also screened the thumbnail.

VERDICT: FAIL

All 11 round-1 required fixes have landed correctly:
- s047, s246, s270 and s279 now use a dark navy glow. No red remains in the water, and nothing reads as blood.
- s059 and s060 show the cap on the sand at the crack mouth, so Doug's death is identifiable. s077 and s078 show the
  cap beside the crab costume.
- s018: the crack lines now sit on the shell.
- s189 now has a tripod camera with a starburst, which is clear. The flash blob is gone from s317.
- s312: "RIP DOUG" reads first, and the red X is in the corner.
- The overlaps are cleared on s060 (INFORMANT), s061 (title), s105 (HUNT THE SKY), s282 (KILLER WHALE) and s191 (the
  tide table is in his hand).

Most of the advisories were taken too:
- The moray in s058 is now the real asset, and the grouper tail in s058–s060 is clear of the topbar.
- s113, s122 and s125 labels are clear, and SWIM BLADDER has an arrow.
- The s015–s019 counter is clear of the inset.
- The s186, s212, s213, s288 and s289 labels and icons are off the map border, and s290 points to Gansbaai.
- The suns in s235 and s236 are filled.
- The 15 orcas in s299 are outlined in red.
- The salmon in s316 and s317 sits forward over the eye patch.
- The new `water_splash` asset reads as a splash in s096, s101, s102, s109, s110, s163, s223, s233, s243 and s247.

The death counter is still correct at 65→74.

Two changed shots still carry defects that block a PASS. Round 1 missed both, but each shot was edited in this round:

### Required fixes

1. **s110: the speech-bubble tail is a broken horizontal sliver** (director). With the bubble at `x 650, y 260` and
   `tail [880, 300]`, the tip sits at the same height as the tail base. The engine therefore draws a thin double line
   that runs out through the bubble's right edge, which looks like a drawing error. Set the speech element to
   `"x": 780, "y": 150, "tail": [900, 280]`. I test-rendered this: it gives a clean wedge pointing down at Doug's head.
2. **s110: the grey `spray` "puff" (x 1350, y 640, r 70, color #222222) reads as grey static** on the trevally's back
   (the same defect class as round-1 fix 5). It does not read as "the tern got taken". Remove it. If a cue is wanted,
   use 2–3 small white feather shapes with black outlines (about 30x10 px `poly`) drifting around (1300–1420,
   600–680) with `appear 0.375`, or a short label "GULP" at (1350, 640). The tern is underwater at the fish's mouth, so
   don't try to draw it in the jaws.
3. **s193: the white lunge streak ends inside the crocodile's mouth** (director). The `curve` `[[0,760],[500,700],[800,720]]`,
   width 10, runs behind the body and pokes out between the jaws, so it reads as the croc holding a white stick. End it
   behind the tail: `"points": [[0,770],[150,752],[280,745]]`. I test-rendered this and it reads as a clean motion trail.

### Advisory (not blocking)

- **s109 (director):** the `red_x` "miss" mark at (1050, 540) lands on the trevally's face, so it reads as "this fish
  is crossed out" rather than "missed Doug". Move it into the gap between the fish's nose and Doug (about `x 1120, y 470`,
  scale 0.25), or swap it for a "MISS" label.
- **s077 (director):** the cap sits right against the crab's red claw in the same red, so it partly merges. Nudge
  `doug_cap` about 50 px right (and the same in s078).
- **s212 (director):** the 8 stacked finish-line banners along the route look like garbled red and white blocks at
  playback size. Fewer and larger banners (3–4 at scale 1.3), or a single banner plus the "16 MARATHONS" wordart,
  would read faster.
- **s193 (director):** the sand puff is a large speckled disc that hazes over the croc's tail. Dropping `density` to
  0.35 would keep the cue and lose the haze.

### Thumbnail (`build/thumbnail.png`, `build/thumbnail_small.png`): PASS

I checked it at 1280x720, 320x180 and a 168x94 downscale.
- It uses archetype B: a pyramid with 11 tiles (the limit is 12) and labels outside the triangle, alternating sides,
  each 4 words or fewer.
- All 11 creatures stay recognisable at 168x94, and the labels are still legible at 320x180. The orca alone at the
  apex makes the threat obvious.
- It complements "How Every Step of the Ocean Food Chain Would Kill Doug" without repeating it. There is no title text
  on the image. It isn't misleading, since every tile is a chapter.
- There is no gore and no kids-show tone.
- Advisory (graphic designer): Doug, in the snail costume in the mantis shrimp tile, is about a 3 px red dot at 168x94.
  That is within the bible's "small scale figure" rule, but scaling him about 1.3x, so the white head and red cap read
  at feed size, would tie the image to "Doug" in the title.

Re-screen after fixes: re-run `keyframes --shots s110,s193` (plus s109/s077/s078/s212 if the advisories are taken) and
send me the sheet.

## Round 3: round-2 fixes re-screen + thumbnail v2 (2026-10-05)

Scope: s077, s078, s109, s110, s186, s193, s212, s251, s288 and s001, all viewed at full size from `build/keyframes`.
I also checked the revised thumbnail (`build/thumbnail.png`, `build/thumbnail_small.png`) at 1280x720, 320x180 and a
168x94 downscale. The `shotlist.json` diff against the previous commit touches only these shots.

VERDICT: PASS

All three round-2 required fixes have landed:
1. s110: the speech-bubble tail is now a clean wedge that runs from the bubble down toward Doug's head. The broken
   sliver is gone.
2. s110: the grey `spray` static is gone. Three small white outlined feather shapes now drift above the diving
   trevally. With "wait what" and the "?" on Doug, they read as "the tern got taken".
3. s193: the lunge streak now ends behind the croc's tail (about x 280). Nothing pokes out of the jaws, and it reads
   as a motion trail.

All four round-2 advisories were taken:
- s109: the red X now sits in the gap between the fish's nose and Doug, so it reads as "missed".
- s077 and s078: the cap is now about 50 px clear of the crab's claw, and the two no longer merge.
- s212: the route now carries 4 banners at scale 0.8 instead of 8 small ones, and they read as finish-line banners.
  The "16 MARATHONS" label is clear of the map.
- s193: the sand-puff density is now 0.35, so the croc's tail reads through it.

The other shots:
- s186, s251 and s288: the labels are clear of the map borders and the counter.
  - s186: "TORRES STRAIT" and its arrow point at the strait.
  - s251: the "WHOLE SEASON" calendar fits the line, and ghost Doug matches the counter (73).
  - s288: PORT and STARBOARD each sit over an orca, and both orcas have the collapsed dorsal fin.
- The death counter still matches the shots: 68 (s077–s110), 70 (s186), 71 (s193, s212), 73 (s251), 74 (s288).

### Thumbnail v2 and s001 (s001 is the same image at 1920x1080): PASS
- The darkening climb works. The bands go from bright at the base, to navy (great white) and deep red (sperm whale),
  to the near-black apex with the orca on a flat red halo. The orca is the single strongest focal point at all three
  sizes, which makes the threat obvious.
- The deep-red sperm whale tile is a flat colour block with a clean grey whale on it. It does not read as blood.
- The mantis shrimp's club is extended toward Doug, which reads as a strike at 320x180.
- Doug in the snail costume has a visible white head and red cap. He is small at 168x94 but identifiable as a figure
  beside the shrimp, which is enough for archetype B.
- All 11 labels are legible at 320x180, and none touches the pyramid edges. The labels avoid every title word. The
  image complements "How Every Step of the Ocean Food Chain Would Kill Doug" and isn't misleading.
- There is no gore and no kids-show tone.

### Advisory (not blocking)
- **s186 (director):** the red dashed crossing line `[[1166,395],[1166,215]]` runs about 30 px above the top border of
  the map, into the sky-blue surround. Ending it at `[1166, 250]` would keep it inside the frame.
- **Thumbnail (graphic designer):** the green and white striped eye-stalks of Doug's snail costume cross the black
  band border into the octopus tile. Lowering Doug about 10 px, or scaling him to 0.95x, would keep the base band
  clean.

Next: art can advance. Post-render screening (samples, qc.json, shorts) follows the final render.

## Round 4: post-render (final.mp4 19:19, thumbnail, Shorts 19:20-19:21) (2026-10-05)

Checked: all 33 samples (every 30 s, 15 s to 975 s) mapped to their shots via timing.json, plus full-res frames at
497 s (s158) and 588.5 s (s188); qc.json (1001.3 s, no problems); thumbnail.png and thumbnail_small.png; all three
Short previews, plus 9 frames per Short (0.3 s, 1.5 s, 20/35/50/65/80 %, end card -3 s and last frame). Each flagged
element was traced to its shotlist x position and compared against the Shorts safe band, x 260..1660 of the 1920 frame.
The Shorts zoom of 1.25 keeps only x 192..1728, and it needs a margin.

### Main video: PASS
- There are no black, blank, frozen or glitched frames. Every sample matches its narration:
  - 135 s: the scientists filming in 2007
  - 345 s: Doug in the tern costume, "higher than every real bird"
  - 405 s: the menu with SHARKS circled
  - 675 s: Doug coming up through the breathing hole in the seal costume
  - 855 s: the dead squid costume in the sonar rings, with the cap floating off
  - 975 s: the 1987 North America map
- The DOUG DEATHS counter runs in order: 65, 66, 67, 68, 69, 70, 71, 72, 73, 74. It matches the round-3 tally.
- Doug is on-model in every costume (crab, tern, shark, turtle, seal, squid). His red cap and white head are always
  readable.
- There is no gore. The breach and the squid-costume death are cartoon only, and nothing reads as a kids' show.
- The 585 s sample (s188) shows only Doug on a split tan and green field. That's because it lands 0.025 s into the
  shot. At 588.5 s the 2014 label, the boat and NORTHERN AUSTRALIA are all in. This is fine.
- Advisory (director): in s188, "tourists on a river cruise" is drawn with `fishing_boat`, which has a rod. A boat
  without the rod would match the narration better. This isn't blocking.
- Advisory (director): in s178, the "27 CROCS" plate overlaps the map's top-left border, and nothing marks Queensland
  or the Kennedy River. This isn't blocking.

### Thumbnail: PASS (unchanged from round 3)
The thumbnail is the same image approved in round 3. The darkening pyramid and the orca on the red halo still read at
320x180. Doug in the snail costume sits next to the mantis shrimp, and the image fits the title. The eye-stalk advisory
from round 3 still applies and is optional.

### Shorts: FAIL (all three)
These parts pass: the red hook titles are readable, subtitles are 2 lines or fewer and legible, the @DoomedDoug tag
shows, and on every end card the red arrow points down to the link with Doug beside it. The failures are crop problems
of the same kind fixed in episodes 005, 006 and 007:

1. **Counter plate in all three Shorts (director):** every shot in the Short ranges has "DOUG DEATHS: NN" at x 1580.
   Its right half runs past the crop, so every Short shows "DOUG DEATHS:" with no number for the whole runtime. The
   shots are s098-s111 (68), s116 (68), s128-s136 (68), s137-s138 (69) and s305-s312 (74). Move the plate to x 1380
   in those shots (the 006 rule). For a steady plate in the main video, you can instead move it to x 1380 in every
   shot of the episode, after checking for label collisions.
2. **s105, short01 (director):** the "HUNT THE SKY" wordart at x 1450 runs to about x 1785. It reads "HUNT THE SK" in
   both the Short and its preview frame. Move it to x 1300, y 450, so its right edge is at or below 1640 and it
   clears the tail of the red arrow at (900, 400).
3. **s102, short01, hook frame (director):** the "IN FLIGHT" wordart at x 1450 touches the right edge. Move it to
   x 1350.
4. **s100, short01 (director):** Doug in the tern costume at x 1700 is cut in half at the right edge. Move Doug and
   `tern_costume` to x 1550.
5. **s104, short01 (director):** Doug in the tern costume at x 250 is clipped at the left edge. Move Doug and
   `tern_costume` to x 400. The surface line is at y 300, so y 290 can stay.
6. **s129, short02 (director):** Doug in the shark costume at x 1720 shows as a grey sliver at the right edge, next to
   the map. Move Doug and `shark_costume` to x 1580. The map's right edge is at about x 1500, so they stay clear of it.
7. **s305, short03, opening shot (director):** the three-panel row spans x 80..1840.
   - The left panel (the great white with the red X) is cut off at the left edge.
   - The right panel (the sperm whales forming a circle) is almost entirely outside the crop. The narration says
     "makes sperm whales form a circle" but the picture never shows it.
   - Fix: refit the row inside 260..1660, for example panels w 440 at x 270, 740 and 1210, with the content centred in
     each:
     - `great_white_shark` and `red_x` at x 490, scale 0.35 and 0.3
     - `blue_whale` at x 960, scale 0.42, with the small orca at x 1060
     - the seven `sperm_whale_top` at about 0.85x their current offsets around x 1430, scale 0.15

Non-blocking:
- s309, short03: the second orca and its exit arrow run to x 200. The orca leaving the frame is intentional, so this
  is acceptable.
- The decorative sun at x 180 (s098, s099, s107, s111) is half-cropped. It's harmless.

### Routing
All fixes go to the director, in shotlist.json. Then run `python -m studio keyframes 008-ocean-food-chain --shots
s098,s099,s100,s101,s102,s103,s104,s105,s106,s107,s108,s109,s110,s111,s116,s128,s129,s130,s131,s132,s133,s134,s135,s136,s137,s138,s305,s306,s307,s308,s309,s310,s311,s312`,
then `python -m studio shorts render 008-ocean-food-chain`. Every new x position is also safe in 16:9. Re-render
final.mp4 so the counter and s305 match the Shorts. The re-screen will cover all three Shorts plus a spot check of
s098, s105, s129 and s305 in final.mp4.

Per-Short status: short01 FAIL (fixes 1-5), short02 FAIL (fixes 1 and 6), short03 FAIL (fixes 1 and 7).

VERDICT: FAIL

## Round 5: post re-render (final.mp4, samples 23:17-23:19, Shorts 23:14-23:15) (2026-10-05)

Checked: all 33 samples; qc.json (1001.26 s, no problems); full-res spot frames from final.mp4 at s098, s103 (start
and end), s105, s128 (mid and end), s129 and s305; thumbnail.png and thumbnail_small.png; metadata.json; all three
Short previews, plus 14 frames per Short (0.3, 1.5, 3, 5 s, 15-85 %, end card -3 s and last frame) and full-res frames
of s103 (short01) and s138 (short02). Every counter plate at x 1380 was checked against the chapter topbar under each
shot's camera move.

### Round-4 fixes: all resolved
1. The counter plate is at x 1380 in all 34 Short-range shots. Every Short now shows the full "DOUG DEATHS: 68 / 69 /
   74" for its whole runtime.
2. s105: "HUNT THE SKY" is fully in frame in short01 and its preview, and it clears the red arrow.
3. s102: "IN FLIGHT" sits inside the crop.
4. s100: Doug in the tern costume is fully visible.
5. s104: Doug in the tern costume is fully visible at the surface.
6. s129: Doug in the shark costume is whole and readable to the right of the map.
7. s305: all three panels are in frame, in both short03 and final.mp4. The panels show the crossed-out great white,
   the blue whale with the orca, and the seven sperm whales in a circle, so the picture now matches "makes sperm
   whales form a circle".

### Main video: FAIL (one regression from fix 1)
There are no black, blank, frozen or glitched frames. The counter runs 65 to 74 in order, Doug is on-model, there is
no gore and nothing reads as a kids' show. The thumbnail is unchanged and still passes.

The regression is that s103 and s128 have `zoom_in` camera moves. As the zoom plays, the newly moved plate (x 1380,
y 165) is pulled up and left until it slides under the chapter topbar. For the last ~1 s of each shot, the topbar
covers the "D" of "DOUG DEATHS". This was checked on frames at 328.75 s and 405.25 s.
- s103: the camera targets (1153, 648) at zoom 1.1, and the "GIANT TREVALLY" topbar covers the plate.
- s128: the camera targets (1100, 800) at zoom 1.08, and the "GOLIATH GROUPER" topbar covers the plate.

These two shots were not overlapped in round 4, when the plate was at x 1580. No other x 1380 shot has a zoom; the
others are static or shake (±8 px), and they all clear the topbar.

1. **s103 (director):** change `camera` to `{"move": "zoom_in", "x": 960, "y": 540, "zoom": 1.1}` (a centred zoom),
   or remove the camera move. With the centred zoom the plate ends at about y 105..150, below the topbar.
2. **s128 (director):** same fix: `{"move": "zoom_in", "x": 960, "y": 540, "zoom": 1.08}`, or remove the camera move.
   Do not just move the plate down; that would make it jump between s127 and s128 and between s128 and s129.

Then re-run `python -m studio keyframes 008-ocean-food-chain --shots s103,s128` and re-render final.mp4. Shorts render
without the topbar, so they are unaffected and do not need a re-render. The fixed shots do change in short01 (s103)
and short02 (s128), but a centred zoom keeps the content inside the 192..1728 crop, so re-rendering the Shorts is
optional.

Advisory (director, not blocking):
- The plate jumps 200 px when the main video enters and leaves the Short ranges (s097 to s098, s111 to s112, and
  similar). You can leave it, or move the plate to x 1380 episode-wide after checking every zoom shot against the
  topbar the same way.
- The round-4 advisories for s188 (the rod on the tourist boat) and s178 (the 27 CROCS plate) still stand.

### Shorts: PASS (all three)
- short01: the hook frame (s102) shows "20+" and "IN FLIGHT" in full. In s103, Doug in the tern costume is near the
  left edge but whole. The rest of the shots are clean, and in s110 the trevally takes the tern.
- short02: the counter shows 68, then 69 after the death. The menu, the 2014 Bonita Springs map with Doug, and the
  blacktip on the line all read clearly. In s138, the ghost Doug at x 1650 and "EATS SHARKS" are in frame.
- short03: the s305 panels read as one row inside the crop. The rudder-theft orcas, ALIVE, the SURVIVED staircase and
  the RIP DOUG headstone all read clearly.
- In all three Shorts, the red hook title reads in 3 lines, the subtitles are 2 lines or fewer, @DoomedDoug shows,
  and the end card "WHAT HAPPENS NEXT? TAP BELOW" has Doug beside a red arrow pointing straight down.
- Note: the short01 preview catches the subtitle mid-reveal ("hunt the sk"). This is the word-timed reveal, not a
  crop, and the video plays correctly.

### Routing
Director: fixes 1-2 (s103 and s128 camera moves), in shotlist.json. Then the editor re-renders final.mp4. The
re-screen will check s103 and s128 at the end of each shot.

VERDICT (main): FAIL
VERDICT (shorts): PASS
