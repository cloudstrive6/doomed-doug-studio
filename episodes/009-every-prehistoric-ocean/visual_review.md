# Visual review: 009-every-prehistoric-ocean

## Round 2: pre-render keyframes (2026-10-08)

Round 1 result: FAIL with 9 blocking fixes (snorkel s024–s027, ARMORED s026, s310 sharks, s276 tusks, s334 contrast, s187 label, s140 fossils, Endoceras variety, Tylosaurus variety) and 11 advisories.

Scope: I re-checked all 29 re-rendered contact sheets (s001–s337) against `shotlist.json`, and zoomed in on s027, s132, s140, s231, s276, s310 and s334. The "thumbnail pending" tile at s001 is expected.

### Blocking fixes from round 1

1. **s024–s027 snorkel: fixed.** Doug wears mask and snorkel in all four shots. In s027 the SNORKEL arrow tip lands on the snorkel tube. Continuity holds into s028–s029, where the snorkel floats away.
2. **s026 ARMORED: fixed.** The label now sits at lower left beside the trilobite row, well clear of the Anomalocaris silhouette.
3. **s310 sharks: fixed.** "USUAL DRAWING" sits above the top shark. The bottom shark is visibly longer and shallower-bodied, with "SLIMMER" under it, so the comparison reads.
4. **s276 tusks: fixed.** The elephant has ivory tusks and the red X is centred on them. The saddle blanket is gone.
5. **s334 THE WHOLE NIGHT: fixed.** The label is now in the sky at left, outlined, and legible against light blue.
6. **s187 TWO-METER HEAD: fixed.** The text sits in open water at upper right, clear of the pliosaur.
7. **s140 fossils: fixed.** A dig pit now holds a half-buried skull, a vertebra row and a flipper bone between the two scientists, with one "SKULL, BACKBONE, FLIPPER" caption below.
8. **Endoceras variety (s040–s048): fixed.** The run is now broken up: s041 is a Harvard museum case with the missing tip circled, s042 is the scientist with a "MISSING PART?" clipboard and pencil, s044 is the truck, s046 is a close-up cone with a dashed "ESTIMATED" tip, and s048 is the 2025 study on a monitor with "GENEROUS". No run of four near-identical frames is left.
9. **Tylosaurus variety (s228–s232): fixed.** The front-on mouth now alternates with s230 (a tight push-in on the backward palatal teeth with yellow arrows) and s231 (a side-on Tylosaurus with a roof-of-mouth inset, a fish at the jaws and a THROAT arrow).

### Round 1 advisories that also landed
s053 (Endoceras now lies alongside the shell), s141 (FREEING THE BONES nudged clear of the scientist), s160 and s327 (NOPE and NOT PROVEN stamps now have a white fill), s260 (SCAVENGING uses a horizontal strike-through), s262–s264 and s289–s292 (moon icon now anchored to the HUD label), s311 (STREAMLINED moved below the shark) and s207 (tail no longer clipped).

### Regression check
- Doug is on-model (red cap, white head) and readable in every shot, including the dark Livyatan and Megalodon backgrounds.
- The death counter runs 74 → 84 in order. The s213 "81 (swallowed)" gag stays crossed out and the counter holds at 80 until s237.
- The s132 circle is still on the tail card (the middle card).
- I found no new overlaps, cropped text or stray marks.
- There is no gore. Deaths stay cartoon only (splash, ghost, floating cap, and the s330 black frame with the HUD still showing).
- Nothing reads as a kids' show.
- Header and name spellings are unchanged and correct.

### Advisory (non-blocking, fix if cheap)
1. **s231:** the yellow "toward the throat" arrow is drawn across the top of the head, over the eye. *Director:* lower it about 25 px so it runs along the jawline or into the mouth.
2. **s276:** the tusks are small and partly hidden behind the trunk, so the X covers most of them. *Illustrator:* lengthen the tusks about 1.4× so they stick out past the trunk. Or *director:* shift the X about 30 px right onto the exposed tips.
3. **s334:** "THE WHOLE NIGHT" is smaller than the other green callouts. *Director:* bump the size about 1.3× if it still fits left of the time machine.
4. **s011, s012, s065–s070, s085, s258:** the round 1 advisories 10, 11 and 17 (compound eye on a stalk, claw shape, goldfish stand-in) are unchanged. They are acceptable as they are.

VERDICT: PASS

## Round 3: thumbnail at feed size (2026-10-08)

Scope: `build/thumbnail.png` (1280x720), `build/thumbnail_small.png` (320x180), plus a 168x94 mobile downscale. I checked them against the `metadata.json` title and thumbnail_brief and against style bible §2A.

- **Grammar:** this is an Archetype A 3x4 grid on white with thick rounded frames and a single comic-font label per tile, matching the brief. Tiles darken in era order from pale Cambrian blue to near-black navy, and Megalodon sits alone on the darkest tile at bottom right. There is no title text or logo, and no label repeats a title word (Dying/Every/Prehistoric/Ocean/Sea/Like).
- **Readability:** at 320x180 all 12 labels are readable and every tile reads as a sea monster. The teeth on Pliosaurus, Livyatan and Megalodon carry the threat. At 168x94 the labels blur, which is normal for this archetype, and the grid still reads as a table of contents for ocean monsters.
- **Spelling:** all 12 names are spelled correctly and none is cropped.
- **Doug:** zoomed in, he is on-model: red cap, white round head, stick body, shock mouth, mask, snorkel and fins. He is a speck at feed size. That is intended, because the style bible says the stick man is never the hero.
- **Policy and kid appeal:** there is no blood or gore. The Helicoprion whorl is a cartoon. Angry brows and teeth on most predators keep it in nature horror. The grid does not read as a dinosaur picture book or as a kids' show.
- **Misleading:** no. The title promises deaths in prehistoric oceans, and the grid shows the monsters at each stop, all of which are in the video.

### Advisory (non-blocking)
1. **Megalodon tile (bottom right):** YouTube's duration badge will cover the right part of the "Megalodon" label. *Graphic designer:* if cheap, nudge the label about 20 px left within the tile. The shark itself stays clear of the badge.
2. **Anomalocaris tile:** Doug faces right, away from the Anomalocaris, and the dark mask band over his eyes reads slightly like lettering when zoomed in. *Graphic designer:* optionally set `facing: "left"` so his shock is aimed at the threat. This is invisible at feed size, so it is not required.
3. **Silhouette variety:** six tiles are grey right-facing fish shapes (Dunkleosteus, Helicoprion, Cymbospondylus, Xiphactinus, Basilosaurus, Megalodon). They are acceptable because the tile colours and labels separate them, but this is worth noting for the next grid episode.

VERDICT: PASS

## Thumbnail v2 (2026-10-08)

Scope: revised `build/thumbnail.png` (1280x720) and `build/thumbnail_small.png` (320x180), plus a 168x94 mobile downscale and zoomed crops of both Dougs and the bottom row. Title: "What Dying in Every Prehistoric Ocean Would Be Like".

- **Readability:** the 3x4 Archetype A grid is unchanged in structure. At 320x180 all 12 labels are readable, spelled correctly and uncropped. At 168x94 the labels blur, as expected for this archetype, but the grid still reads at once as "a list of sea monsters". The tiles still darken in era order, ending on Megalodon on the darkest tile.
- **Doug (on-model):** both Dougs (Anomalocaris tile and Megalodon tile) have the red cap, white round head, stick body, open shock mouth, blue mask, snorkel and fins. Both now face left, toward their threat, so round 3 advisory 2 is resolved. The eyes show through the mask and no longer read as lettering. In the Megalodon tile Doug is white-on-navy and is the only light speck in the corner, so he reads as "tiny man next to giant teeth" even at 320 px.
- **Creatures:** every tile is recognisable as its animal type. Anomalocaris has frontal appendages and stalked eyes. Endoceras is a striped cone shell with tentacles. Jaekelopterus is a sea scorpion with claws. Dunkleosteus has an armoured head plate. Helicoprion shows the tooth whorl. Cymbospondylus is an ichthyosaur. Pliosaurus is a toothy marine reptile. Xiphactinus is a fanged fish. Tylosaurus is a gaping mouth with eyes in the corners. Basilosaurus is an eel-like whale. Livyatan and Megalodon are giant jaws. The Tylosaurus mouth is the most abstract tile, but its teeth, eyes and palatal tooth rows make it a maw rather than a red blob.
- **Gore and policy:** there is no blood, wound or body part. The dark red on Tylosaurus, Livyatan and Megalodon is gum or mouth interior, drawn flat with no drips or pooling, so it is acceptable. Nothing is cutesy and there is no nursery palette. It reads as nature horror, not a kids' dinosaur book.
- **Misleading:** no. Every creature shown appears in the video, and the grid delivers on "every prehistoric ocean".

### Advisory (non-blocking)
1. **Megalodon tile label:** this is carried over from round 3 advisory 1. The label is still centred, so YouTube's duration badge (bottom right, about 80x40 px at full scale) may clip the final "n". *Graphic designer:* if cheap, shift the "Megalodon" label about 20 px left. Do not move the shark or Doug.
2. **Silhouette variety:** the grey right-facing fish shapes are unchanged. They are acceptable for this episode, and this note is kept for the next grid.

VERDICT: PASS

## Round 4: thumbnail v2 (2026-10-08)

Scope: `build/thumbnail.png` (1280x720) and `build/thumbnail_small.png` (320x180), a 168x94 downscale, and a simulated YouTube duration badge (desktop feed: about 44x20 px at 8 px inset on a 360 px card, which is roughly x 1095-1251, y 620-691 at full res; the mobile badge is similar). This round supersedes the unnumbered "Thumbnail v2" section above, which did not test the badge position.

- **CD changes applied:** Endoceras, Pliosaurus and Basilosaurus are flipped. Crops now vary across the grid (full body: Endoceras, Helicoprion, Cymbospondylus, Pliosaurus, Basilosaurus; mid: Anomalocaris, Jaekelopterus, Dunkleosteus; tight: Xiphactinus, Tylosaurus, Livyatan, Megalodon). Basilosaurus is a long eel-whale across the tile. Tylosaurus is a front-on gaping maw. Megalodon is a tight jaw crop of more than 40% of the tile with a tiny Doug. The palette gradient, labels, frames and order are unchanged. The "stamp sheet" problem from v1 is fixed.
- **Legibility:** at 320x180 all 12 labels are readable. At 168x94 they blur, as expected for Archetype A, but the grid still reads as a set of sea monsters. Spelling is correct and nothing is cropped by the frames.
- **Bottom row at 320x180:** Tylosaurus, Livyatan and Megalodon read as three distinct animals. Tylosaurus is a front-on red-and-green maw. Livyatan is a brown-grey side-on whale head with a brow and an eye. Megalodon is a pale grey and white three-quarter jaw on navy. They differ in colour, angle and shape, and Basilosaurus breaks up the run. The only overlap is that Livyatan and Megalodon share the same zigzag tooth row with red gums. That is acceptable.
- **Doug:** both Dougs are on-model, with red cap, white head, stick body, shock mouth, mask, snorkel and fins, and both face their threat. The Megalodon-tile Doug is the only light speck on navy and sells the scale at 320 px.
- **Policy:** there is no gore. The mouth interiors are flat dark red with no drips or pools. The tone is nature horror, not a kids' picture book.
- **Misleading:** no. Every creature shown is in the video.
- **Duration badge (blocking):** with the badge simulated, it covers **Doug's legs and fins in the Megalodon tile**, from his waist down (his body runs y about 575-645 and the badge starts at y about 620). Only a floating head and cap remain, so the one human-scale cue the CD asked for is half hidden. The badge also covers "odon" of the label, which then reads "Megal…".

### Fixes
1. **Megalodon tile Doug (graphic designer, blocking):** move Doug up so that his whole figure, fins included, sits above y ≈ 610 at full res and stays on the navy gap right of the jaw. That is about 40-50 px up. If that pushes him into the white jaw edge, nudge the shark about 30 px left or down instead of shrinking Doug below scale 0.12. Do not move him left over the teeth, because white on white disappears.
2. **"Megalodon" label (graphic designer, recommended, not blocking):** this has been flagged for the third round. The label's right edge sits under the badge. Shift it left so it ends before x ≈ 1085, or accept "Megal…" in feed. The jaws carry the tile without the label.
3. **Livyatan (advisory):** the jaw is wider than in v1 and the teeth read at 168 px, but it is still a narrow band. If the designer is re-rendering anyway, opening it about 20% more would separate it further from Megalodon.

VERDICT: FAIL

## Thumbnail v3 (2026-10-08)

Scope: `build/thumbnail.png` (1280x720), `build/thumbnail_small.png` (320x180), the designer's `build/thumb_badge_mock.png`, and my own badge overlays. I used three badge boxes at full res: the round 4 box (x 1095-1251, y 620-691), a desktop estimate (x 1120-1266, y 640-706) and a mobile estimate (x 1126-1254, y 630-694). I also checked 2x crops of the bottom-right corner and 320x180 and 168x94 downscales. Title: "What Dying in Every Prehistoric Ocean Would Be Like".

- **Doug vs badge (round 4 fix 1): fixed.** Doug now spans about y 525-592 at full res, from the cap to the fins. He sits on the navy gap right of the jaw, with a clear margin from the white jaw edge. His lowest pixel is about 28 px above the most conservative badge top (y 620). He is fully visible in all three overlays and remains the only light speck in the corner at 320 and 168 px. He is still on-model (red cap, white head, mask, snorkel, fins) and faces the shark.
- **Megalodon label vs badge (round 4 fix 2): fixed.** The label now spans x 905-1079 and ends 16 px before the most conservative badge left edge (x 1095). "Megalodon" reads in full in every overlay.
- **Label ownership: acceptable, with a small cost.** The Megalodon tile runs x ≈ 941-1256 (centre ≈ 1098). The label is centred at x ≈ 992, about 105 px left of the tile centre, and its first ~36 px ("M") start under the Livyatan tile and gutter. The gap between "Livyatan" (ends x 858) and "Megalodon" is only 47 px, so the bottom row reads "Livyatan  Megalodon" as a pair. Even so, about 80% of the word sits under its own tile, and the left-to-right order matches the tiles. The Livyatan label stays centred under its tile. At 320x180 and 168x94 nobody would swap the two names. This is a visible asymmetry in the full-screen opening frame, where there is no badge, but it does not mislabel anything.
- **Regressions: none found.** The other 11 tiles, labels, frames, palette gradient, Anomalocaris Doug and the Megalodon jaw are unchanged from v2 round 4. There is no new clipping, stray line or overlap. The gore and policy checks from round 4 still hold.
- **Note on the designer mock:** in `thumb_badge_mock.png` the drawn badge (about x 1095-1252, y 620-691) and the magenta outline (about x 1145-1265, y 660-704) do not match. Both boxes are clear of Doug and the label, so it does not affect the verdict.

### Advisory (non-blocking)
1. **"Megalodon" label (graphic designer, optional polish):** to make the label read as part of its tile without bringing back the badge clash, either (a) left-align it to the tile's inner frame (start x ≈ 958) and set this one label at about 75% font size so it ends ≤ x 1090, or (b) leave it as is. Do not centre it under the tile again, because that puts "odon" back under the badge.
2. **Livyatan jaw width and silhouette variety:** this is carried over from round 4 and is still optional.

VERDICT: PASS

## Post-render (2026-10-08)

Scope: `build/final.mp4` (1920x1080, 1033.4 s), the 34 frames in `build/samples/`, `build/qc.json`, `build/thumbnail.png` and `build/thumbnail_small.png`, `metadata.json`, the three Shorts (`short0N_preview.png`, plus 5 frames from each mp4 and full-res crops). I also scanned the final at 1 fps for edge artifacts. Nothing was re-rendered.

### Main video
- **qc.json:** there are no problems. I saw no black, blank or frozen frames in the samples. The pacing reads, and the Doug Deaths counter climbs 74 to 83 in order with no jumps.
- **Content:** every sample is clean. Topbar labels, the counters and green callouts are legible and spelled right. Doug is on-model in every frame. Creatures are recognisable. There is no gore (Tylosaurus mouth interior is flat red, Doug's deaths are cartoon). The tone is not kid-like. The dark Xiphactinus stomach frame still shows Doug and the "?".
- **Edge artifact (blocking): CONFIRMED VISIBLE in the final.** The left-edge risk from the keyframes survived into the encode, along with a related problem on the top edge.
  - **Left column x=0:** there is a full-height, 1 px near-white line (about RGB 242,251,255) on navy or dark-teal scenes, while x=1 is the scene colour (about 14,23,48). Example: final.mp4 at 960 s (Megalodon "BIG PREY"). The 1 fps scan finds column 0 brighter than column 3 in **176 of 1033 seconds (17%)**, in about 85 separate runs across the whole episode (12 s to 1007 s). Most are on underwater and dark shots, the worst in the Livyatan and Megalodon chapters (about 860 to 1007 s). It switches on and off with the shots, so it flickers at cuts instead of sitting still.
  - **Top row y=0 (new):** there are broken 1 px white dashes along the top edge, sometimes on the bottom row too. They line up with the light-ray shapes on underwater backgrounds (e.g. 900 s, 960 s and 990 s). About 160 of the 688 seconds scanned have them.
  - **Visibility:** on cream or white scenes it cannot be seen. On dark scenes in the YouTube player (black surround, theatre mode or fullscreen) it reads as a thin white frame line that blinks between shots. It is subtle, but it is a render defect on our darkest and most important climax shots, and the fix is cheap.
- **Thumbnail:** this is unchanged from the approved v3. Its edges are clean (white surround, no stray line). It is readable at 320 px, complements the title "What Dying in Every Prehistoric Ocean Would Be Like", and is not misleading. **Pass.**

### Shorts
- **Titles, layout and end card:** the three titles are red, readable and spelled right. The drawings are not cut off at the sides. The "?" and the "FOOD CHAIN" label sit about 30 px in from the left edge, which is tight but fine. The subtitles are large and legible. Each end card reads "WHAT HAPPENS NEXT? TAP BELOW" with the arrow pointing **down**. The @DoomedDoug handle is legible.
- **Stray line (blocking):** this is the same top-row artifact as the main video. In Shorts the 16:9 scene sits as a band in mid-frame, so the dashes are not at a screen edge. They show as a broken white line across the top of the art band, at about y=578 of 1920 in short01. It is visible in `short01_preview.png` (dark Megalodon scene, about 6 s of the clip) and faintly in `short02_preview.png` at the top of the blue band. Against the navy band in short01 it is clearly a stray line.
- Short03 shows no visible line in the frames I checked, but it comes from the same renderer.

### Fixes
1. **Edge pixels (art director / editor, engine, blocking for both main and Shorts):** the outermost pixel row and column of underwater and dark scenes are being drawn white. The left column is full height. The top row (and sometimes the bottom row) has dashes where the light-ray polygons and their outlines meet the frame edge. Fix it at the source in `studio/paint.py`/`scene.py`: fill the background past the canvas edge, and stop stroking the ray or background outlines where they touch the frame border. Do not just patch the episode. If a hotfix is needed instead, overwrite the 1 px border with the neighbouring pixel at assemble time. Re-render final.mp4 and all three Shorts, then re-run `qc` and re-sample. I will re-check 900 s, 960 s and 990 s, and the top of the art band in short01 and short02.
2. No other changes are needed. The thumbnail, metadata and shot content all pass.

VERDICT (main): FAIL
VERDICT (shorts): FAIL

## Post-render round 2 (2026-10-09): re-render after `_clean_edges`

Scope: `build/final.mp4` (re-rendered 23:51, after commit afdc9e6 with the fix), all 34 `build/samples/`, `build/qc.json` (no problems), a full-res 1 fps scan of the outer 6 px on all four sides of the final (1033 s), full-res frames at 0/30/240/270/390/840/900/960/990/1005 s, the thumbnails, `metadata.json`, and the three Shorts (2 fps scan, 285 frames, plus the previews). Nothing was rendered to disk.

### Edge line: NOT FIXED, now 2 px deep
- **Main video:** I found a bright edge line in **242 of 1033 seconds (23%)**. By side: top 240 s, left 53 s, bottom 15 s, right 8 s. Round 1 had 176 s. At full res the white is now **2 px deep** (rows/columns 0 and 1, e.g. (243,255,255)), and the scene colour starts at row/column 2 (e.g. (10,23,42)). Clear examples: 960 s (s312 Megalodon "BIG PREY": dashes along the top and a white line on the lower-left edge), 990 s (s321), 1005 s (s327), and 16 s/58 s (left edge). The 640 px samples show it too: f_001, f_003, f_009, f_010, f_014, f_029 (top) and f_034 (left).
- **Root cause (reproduced in memory with `ShotRenderer` on s312):** boil variant 0 is clean, but **variants 1 and 2 are not.** There the wobble/boil pulls the background and ray polygons in by 2 px, so the white canvas (`background: #ffffff`) shows through a 2 px ring. `_clean_edges` copies only the 1 px neighbour, which is also white, so the line survives. It flickers at 8 fps boil rate on dark shots. The round-1 fix was checked only on variant 0 (keyframes), which is why it looked fixed.
- **Shorts:** the same defect is clearly visible. short01 has white dashes across the top of the art band at y≈578/610/636 in about 26 of 106 frames, and a full-height white line at x=0 on the art band (e.g. frame 36 s, the "which suggests competition may" shot). short03 has dashes at y≈612/636 and a left-edge line (about 7 frames). short02 had no hits in the scan, but it uses the same renderer.

### Everything else
- The content of all 34 samples is unchanged from round 1 and clean: Doug is on-model, labels and counters are legible, the death counter runs 74 to 83, there is no gore, and the tone is not kid-like. QC has no problems.
- **Thumbnail:** this is the approved v3, unchanged, with clean edges. It is readable at 320 px, complements the title "What Dying in Every Prehistoric Ocean Would Be Like", and is not misleading. **Pass.**
- **Shorts layout:** the titles are readable, the drawings are not cut off, the subtitles are legible, and the end cards point down. These all pass apart from the edge line.

### Fixes (engine, art director / editor)
1. `studio/scene.py` `_clean_edges` / `render_still`: make the bleed robust for every boil variant, not just variant 0. Do one of the following (both is best):
   (a) Before drawing, fill the canvas with the colour of the first full-bleed background element instead of `#ffffff`. Or draw edge-touching background rects and ray polys with an outset of at least ceil(wobble_px + boil_px) + 2 ≈ 5 px past the canvas.
   (b) Widen `_clean_edges` to overwrite the outer **4 px** ring from the row/column at depth 4.
2. Verify on **all boil variants** (`ShotRenderer(...).frames()` for s312, s321, s327, s006, s019): no pixel in the outer 4 px may be white where pixel 5 is dark. Then re-render the final and Shorts, and re-run the edge scan.

VERDICT (main): FAIL
VERDICT (shorts): FAIL
