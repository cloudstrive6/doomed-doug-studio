# 016 Every Layer of Antarctica: visual review

## Round 1: pre-render (keyframes + thumbnails), 2026-10-12

Inputs: `shotlist.json` (274 shots), `build/contact/sheet_01..23.png`, full-size keyframes for the edge cases
(s012, s025, s090, s138, s254, s273), `thumbnail.json` / `thumbnail_b.json`, `build/thumbnail*.png` and
`build/thumb_compare_168.png` / `thumb_compare_small.png`.

What works: Doug is on-model in every shot (red cap, white head) and readable on every background, including
the dark Denman canyon. The death counter runs 130 to 139, and the 9 deaths match the 9 suitcase stickers
(Erebus and Whillans are "Doug is fine" stops, so leaving them out is correct). Every death is a cartoon
crush, freeze or flood with X-eyes and no gore. Blood Falls is clearly rust and is labelled NOT BLOOD. The
three ice-encasement deaths (s151, s219, s244) have different silhouettes, as the CD asked. Nothing reads as a
kids' show. Chapter cards, maps and the HUD are consistent. Spelling is clean throughout.

### VERDICT: FAIL

The required fixes are mostly small: crops, overlaps, one render glitch, one unreadable reveal and four long
static runs. I will re-check only the listed shots plus the thumbnail.

#### Required fixes

1. **s012, director.** "PERFECTLY CLEAR" ends at x≈1880, and the 1.05 zoom centred on x=800 pushes the final "R"
   off-frame. It also sits across the glacier edge line. Move the wordart to x≈1500, y≈300 at size 72 (fully on
   the light-blue side, right edge ≤1800), or drop the zoom.
2. **s025, director.** "JOINED THE PHOTO" starts at x≈8 (no safe margin) and the shake move will clip the "J".
   It also runs through the falling ice chunk. Move it to x≈1300, y≈300 (right of the chunk, below the HUD) at
   size 76.
3. **s254, director.** The "DENMAN: 8 TIMES LOWER" label at y≈1055 is cut off by the bottom frame edge. Move it to
   y≈960 inside the canyon (x≈1300), or shorten it to "DENMAN".
4. **s090, director/illustrator.** The "permanently dark" overlay is a hard rectangle (x 0–960) that cuts the
   camera robot in half and paints over the seabed line, so it reads as a render glitch. Darken the whole
   water band (x 0–1920, y 430 to the seabed curve) or use a soft gradient, and keep the robot fully on one tone.
5. **s162, illustrator/director.** The narration names the tardigrade ("water bear"), but the drawing is a black
   blob with a red outline, so the viewer can't tell what it is. Show the actual tardigrade asset (as in
   s163/s166) at that spot. Save silhouette reveals for "something swam up" beats only.
6. **s187, director.** Doug stands on top of the buried-volcano panel (about x 1755, y 240–420 full-size), so his
   head overlaps the "ICE ABOVE DOUG" HUD box, and "COMPLETELY BURIED" crowds him. Move him off the HUD: either
   onto the green ground beside Fuji (x≈900, feet at y≈1050) or drop him from this shot.
7. **s178 / s181 / s182, director.** "RADAR MAPS" (s178) and "91 VOLCANOES" (s181) start on top of the radar
   screen's right border. Shift them right by about 40 px or shrink them to size 64. In s182 the "UNDER THE ICE" label
   sits on the scientist's head. Move it up to y≈540 full-size (under "138").
8. **s146, director.** The "WHAT ARE THEY EATING?" bubble covers the "625 TO 1,500 KM" label, and its tail
   crosses the dashed line. Move the bubble to the left above the scientist (x≈500, y≈200 full-size), with the tail
   pointing down to his head.
9. **Text overlapping drawings, director.** Each of these needs a move of about 60–150 px so the wordart is clear of
   the line art:
   - s004 / s005: "ON THE ROPE" / "DID NOT AGREE" sit on the generator and the tripod leg. Raise them to y≈300
     full-size (open sky).
   - s045: "ON A VOLCANO" sits on the crater and steam. Move it to y≈200.
   - s107: "HOT-WATER DRILL" touches the tripod head. Move it left (x≈550) or up (y≈250).
   - s138: "TOTAL DARKNESS" runs into the sponges. Shorten it to size 72 or move it to x≈450. There is also a
     stray dashed-line fragment at x≈1660–1700, y≈868 to delete.
   - s142: "CANNOT MOVE" overlaps the sponge rim. Move it to x≈1350.
   - s205: the "DEC 2012" label overlaps "CAMP". Put the label above the wordart (y≈250 full-size).
   - s213: "CALLED OFF" crosses the tripod leg. Move it to x≈1300 full-size, left of the tripod.
   - s253: "GO DEEPER" overlaps the trench box. Move it to x≈1500 (right of the trench) or down below the boxes.
   - s272: "ONLY THE CAP" crosses the tripod leg. Move it to y≈300 full-size (sky) or to the left (x≈500).
10. **s115, illustrator/director.** The sample tubes are dark red and amber in a rack, which reads as blood vials
    in an episode that has just spent a chapter saying "it isn't blood". Recolour the liquid pale blue/clear
    with the green microbes visible.
11. **Variety, director.** These runs of near-identical compositions have no camera moves. Break each one with a
    zoom or close-up on at least two shots:
    - **s070–s077 (8 shots, Thwaites underside).** Zoom 1.3 into a single slot for s073 ("melting their walls
      sideways"), and turn s076/s077 into a simple two-bar graphic (1/10 of the area vs more than 1/4 of the melt).
    - **s256–s261 (6, Denman canyon).** Zoom into the canyon floor for s259 and s260, and push in slowly on s261.
    - **s235–s240 (6, Vostok borehole).** Close-up on the hole bottom for s237/s238 (water surging up), and zoom
      in for s239.
    - **s178–s182 (5, radar screen).** Zoom into the screen for s179 (cone) and s181 (91 triangles).
    - **s191–s195 (5, buried volcano row).** Zoom on the melt lens for s193/s194.
    - **s054–s057, s111–s114, s126–s129, s160–s163 (4 each).** Add a slow zoom_in (1.08–1.15) on alternate shots.

#### Thumbnail

- **A (`thumbnail.png`, archetype B column): PASS with fixes, keep as primary.** It matches the brief and the
  title (depth-by-depth), it isn't misleading, and every band subject reads at 320 px. At 168 px, though, the
  thin regular-weight labels blur and Doug is a red speck.
  12. **Graphic designer.** Set the labels bold at a larger size (about 44 → 52 px), give Doug about 1.6× scale on
      the rope, and move "See-Through Fish" in so it has at least 24 px of left margin (it starts at x≈8 now and
      will hit YouTube's rounded corner). Keep the ash spray from the volcano band from leaking into the sponge band.
- **B (`thumbnail_b.png`, "4 KM DOWN"): PASS as the A/B alternate.** It reads well at 168 px: big text, Doug
  obvious, depth implied. The threat is weak (an empty canyon), and the red-speckle glow looks like noise at feed
  size. Optional: replace the speckle with a soft red gradient on the canyon floor.

#### Advisory (not blocking)

- s036: the ice chimney is tiny next to the "ICE CHIMNEYS" wordart. Scale it to about 2×.
- s056: "the air is the dangerous part" has no visual. A faint grey-green haze would help.
- s012/s013: the black pentagon "spout" is hard to read. A dark crack in the ice face would read better.
- s161: the crustacean carcasses read as seeds or potatoes. Adding a segmented shell line would help.
- s069: the Icefin light cone floats free of the robot's nose. Attach it.
- s120/s121: Doug overlaps the bottom-right microbe.
- s135/s136/s188/s252: the HUD sits on the REC frame / world-map border. Inset those frames by about 40 px.
- s159: the thought bubble's tail points between Doug and the microscope. Aim it at Doug.

Re-check scope for round 2: fixes 1–12 only.

## Round 2: pre-render re-check (fixes 1–12 + regression scan), 2026-10-12

Inputs: `shotlist.json` (274 shots), all 274 keyframes in `build/keyframes/` (all rendered after the last
shotlist save), `build/contact/sheet_01..23.png`, full-size keyframes for s138, s146, s182, s187, s194 and s261,
simulated end-of-move frames for all 38 shots that have a camera move (keyframes show the uncropped canvas, so I
cropped each one with `camera_rect(..., u=1.0)`), and `build/thumbnail*.png`, `thumb_compare_168.png` and
`thumb_compare_small.png`.

Note on tooling: when I started, `build/contact/` held only `sheet_01.png` with a single tile (s001).
`keyframes --shots s001` wipes every contact sheet and rebuilds only from the shots it rendered
(`studio/assemble.py` `keyframes()` → `contact_sheets()` unlinks `*.png` first). I rebuilt all 23 sheets from the
existing, current keyframes without re-rendering. Whoever runs a partial keyframe pass next should rebuild the
full sheet set, or the engine should only regenerate sheets on full runs.

### Fix re-check

| # | Shot(s) | Result |
|---|---|---|
| 1 | s012 | PASS. "PERFECTLY CLEAR" sits fully on the light-blue side. At the end of the zoom its right edge is about 105 px from the frame edge. |
| 2 | s025 | PASS. "JOINED THE PHOTO" is at the top left, above the ice chunk, with a safe margin through the shake. |
| 3 | s254 | PASS. The "DENMAN" label sits inside the canyon floor. |
| 4 | s090 | PASS. The whole water band is dark, the robot is on one tone, and the seabed line is intact. |
| 5 | s162 | PASS. The tardigrade drawing appears with a red arrow, and "WATER BEAR" is readable. |
| 6 | s187 | PASS. Doug stands on the green ground between Fuji and the buried panel, clear of the HUD and of "COMPLETELY BURIED". |
| 7 | s178 / s181 / s182 | PASS. "RADAR MAPS" clears the screen border, s181 is a close-up with clear text, and in s182 "UNDER THE ICE" sits under "138" above the scientist's hair, with a tight gap but no overlap. |
| 8 | s146 | PASS. The bubble is above the scientist, its tail points at his head, and it is clear of both the dashed line and the km label. |
| 9 | s004 s005 s045 s107 s138 s142 s205 s213 s253 s272 | PASS on every listed wordart move. The stray dashed fragment in s138 is gone. A new overlap in s138 is listed as fix R2-3. |
| 10 | s115 | PASS. The tubes are pale blue and clear with green microbes, so they no longer read as blood vials. |
| 11 | variety runs | PASS on every run: s073 close-up and s076/s077 bar graphic; s179/s181 close-ups; s237/s238 close-ups and s239 zoom; s259/s260 canyon close-ups; and alternate-shot zooms on s054–057, s112/s114, s127/s129 and s161/s162. Two of the new moves introduced clipping, listed as fixes R2-1 and R2-2. |
| 12 | thumbnail A | PASS. See the thumbnail section below. |

Regression scan of all 23 sheets: no off-model Doug, no new text crops, no spelling errors, death counter
130→139 intact, no gore. The only new problems are the three below, two of which come from the new camera moves.

### VERDICT: FAIL

There are three small director fixes, all in camera values or label positions. Re-check scope for round 3:
s193, s194, s261 and s138 only.

#### Required fixes

R2-1. **s193 / s194, director.** The new zoom_in moves end with the crop top at y≈110 full-size. Doug's cap starts at
   y≈102, so at the end of both moves the cap is clipped and his head touches the top edge. Change both cameras to
   `{"move": "zoom_in", "x": 1180, "y": 520, "zoom": 1.15}`, which puts the crop top at y≈50. Also, in s194
   "COULD INCREASE" (x≈380–1140, baseline y≈500) runs its last letters into the orange heat glow and onto the
   top edge of the melt lens. Move it to y≈400 (higher in the clear ice band) or end it by x≈980.
R2-2. **s261, director.** The new push-in `to: [1050, 590, 1.15]` ends with a crop of x 215–1885 and y 120–1060. That cuts Doug's head
   off (he stands at y 60–240, so only his legs remain), and "SEA LEVEL" (x 118–323) is cut to "EVEL". Change it to
   `"to": [960, 500, 1.1]` (crop x 87–1833, y 9–991), which keeps Doug, SEA LEVEL and the HUD in frame and still
   pushes into the warning sign. Alternatively, drop Doug from this shot.
R2-3. **s138, director.** The "260 KM TO OPEN SEA" box (x≈1075–1525, y≈770–830) sits on the top-right of the sponge
   boulder and touches the rightmost sponge stalk. Move the box right and down to x≈1230, y≈800 so it stays fully right of the
   boulder (boulder right edge ≈1170) and above the dashed line, or shrink it to "260 KM".

#### Thumbnail verdict

- **A (`thumbnail.png`): PASS, keep as primary.** Fix 12 is done. The labels are bold and noticeably larger,
  Doug is about 1.6× scale with his red cap and white head clear, and "See-Through Fish" now starts at x≈28 (above
  the 24 px minimum). At 168 px all six labels can now be read, Doug reads as a red-capped figure on the rope, and
  every band subject is distinguishable. It matches the title "What Dying at Every Depth Under Antarctica Would Be
  Like" without repeating it and isn't misleading. Advisory only: a few red glow speckles from the Denman band
  drift up into the Lake Vostok band (around x 650–700, y 600–620 at 1280 px), and a few ash dots sit just under the
  volcano band line. Clipping the glow and ash sprays to their own bands would tidy it up.
- **B (`thumbnail_b.png`, "4 KM DOWN"): PASS as the A/B alternate.** The round-1 optional note was taken up: the
  red speckle is now a smooth red radial gradient on the canyon floor, which reads as heat or danger instead of
  noise at 168 px. The text is large and clean, and Doug is big and obvious. The threat is still implied
  rather than shown, which suits a test variant.

#### Advisory carried over (not blocking)

- s036: the ice chimney is still small next to the wordart.
- s120: Doug still sits close to the bottom-right microbe.
- s075: the bottom of "FAST" nearly touches Doug's cap. A 20–30 px raise would give it air.

## Round 3: pre-render re-check (R2-1 to R2-3, plus art-review fixes on s034/s035/s202/s265), 2026-10-12

Inputs: `shotlist.json` (274 shots; only s034, s035, s138, s193, s194, s202, s261 and s265 changed compared with the round-2
snapshot, and nothing in `studio/` or `assets/` changed). All 274 keyframes and all 23 contact sheets were rendered after the
last shotlist save. I viewed full-size keyframes for all 8 changed shots. For the three camera moves I rendered the true
end-of-move frame (u = 1.0): `render_still` → `camera_rect` → `fit_frame` → `with_topbar`, the same order `ShotRenderer`
uses, so the caption bar is drawn on top after the crop. I also re-cropped all 38 camera shots and scanned contact
sheets 03, 12, 17, 22 and 23, which hold every changed shot and its neighbours.

Correction to my round-2 method: I cropped keyframes that already had the caption bar baked in, so those crops showed
the caption bar cut off. In the real render the bar is composited after the crop and is never cut. None of the round-2
findings depended on this.

### Fix re-check

| # | Shot | Result |
|---|---|---|
| R2-1 | s193 | PASS. Camera is now `zoom_in x1180 y520 z1.15`, so the crop runs y 50–990. At the end frame Doug (cap, head and feet) is fully in frame, about 55 px below the top edge. He is clear of the caption bar horizontally. MELT, the melt lens, the arrow and the HUD are all in frame. |
| R2-1 | s194 | PASS. Same camera as s193. "COULD INCREASE" was moved to x 640, y 400 and now spans x≈315–965 in the pale band. It is clear of the thin-ice line (y 506) and of the orange glow, which starts at x≈980. At the end frame the text runs x≈75–820, so nothing is clipped. |
| R2-2 | s261 | PASS. The move is now `to [960,500,1.1]`. At the end frame Doug is whole, "SEA LEVEL" is complete (x≈115–325), the HUD is inside the right edge, and the push still lands on the warning sign. |
| R2-3 | s138 | PASS. "260 KM TO OPEN SEA" now spans x≈1215–1665, y≈770–830. It is clear of the sponge boulder and its stalks (right edge ≈1150) and above the dashed line (y 870). |
| art | s034 / s035 | PASS. CRACKS and FROM BELOW sit at y 330 in the sky and are clear of the ice-slope outline and the HUD. |
| art | s202 | PASS. "7 EMPIRE STATES" spans x≈110–670 and is clear of the borehole and the building stack. Doug in the borehole is on-model. |
| art | s265 | PASS. The baked 1.25× group zoom breaks the s262–s266 run of five identical diagrams. The EASIER arrows fill the frame, and the 1996, 2018 and 5+ KM labels can all be read. |

Regression scan: Doug is on-model everywhere I checked. There are no new text crops, overlaps or spelling errors. The death
counter still runs 130→139 in order, and there is no gore. The other 37 camera moves end cleanly. No run of 4 or more
near-identical compositions remains.

### VERDICT: PASS

The keyframes are cleared for the render. No required fixes.

#### Advisory (not blocking)
- s138: the right edge of the "260 KM" box (x≈1665) touches the shelf-front colour edge at x 1660. Moving it to x 1420 would leave a gap.
- s265: the ocean-surface line from the group (white, x≈1560–1920, y≈340) floats inside the dark ice. It is also visible in s262–s264, so it is consistent, but stopping it at the ice front would look cleaner.
- Carried over: s036 ice chimney is small; Doug sits close to the microbe in s120; "FAST" is tight above Doug's cap in s075.
- Post-render screening (samples, qc.json, final thumbnail and Shorts) is still to do after `render --final`.

## Round 4: post-render screening (final.mp4, thumbnail, Shorts), 2026-10-12

Inputs: `build/final.mp4` (1920x1080, 914.5 s, rendered 18:24 after the last shotlist save at 18:13), `build/qc.json`
(`problems: []`), all 30 samples in `build/samples` (taken at t = 15 + 30k s). I re-grabbed each sample time at full
1080p and mapped it to a shot id through `captions.srt`. I also checked `build/thumbnail.png` and `thumbnail_small.png`
against `metadata.json`, and `build/shorts/short01-03` (previews, 5 frames each, plus a contact sheet every 3 s). I ran a
scan over all 274 scenes for overlapping label, text and wordart boxes. The only hit that wasn't the intended death-counter
swap was s248. Nothing was rendered.

### Main video
- No black or blank frames, glitches or frozen frames in the samples. Topbar chapter captions match the chapter list. The death
  counter rises 130 to 138 in order across the samples. Doug is on-model in every sample he appears in. No gore: the Blood
  Falls outflow is a brown iron stain, and deaths are cartoon only.
- **Defect, s248 (sample f_028, t≈825 s):** the "DENMAN GLACIER" label (x 600, y 330, size 40, appears at 0.143) is drawn
  over the right end of the "SEA LEVEL" label (x 330, y 330). On screen it reads **"SEA LEVE"** for about 3.5 s. The same
  scene recurs in s249–s261, but there the DENMAN label is absent, so they are clean. Pre-render rounds missed this.
- Mid-shot samples that only look sparse because their reveals had not fired yet (s027 microbe panel, s144 sponge distance
  shot): fine at full length.

### Thumbnail
PASS. Archetype B cross-section. Bands darken from top to bottom with one subject per band, and Doug is on the rope at the
top. Labels are outside the stack, alternate sides and use no title words. At 168 px the bands, Doug's red cap and the labels
can all still be read. The bottom-right corner, where the timestamp sits, is empty white. It complements "What Dying at Every Depth Under
Antarctica Would Be Like" and is not misleading: every pictured stop is a chapter.

### Shorts
PASS. All three are 1080x1920 (42.6 / 49.5 / 47.8 s). The red title is readable at the top and the subtitles are big and
high-contrast. The full 16:9 frame is letterboxed, so no main drawing is cut at the sides. On every end card the red arrow
points straight down and Doug points at it. The Doug death in short01 (137 to 138) is a cartoon death (water geyser).
- Advisory: short03 fish close-up (around 24–36 s), where the ROV's left thrusters touch the left frame edge. This comes from the
  main-video shot and is not a crop introduced by the Short.
- Advisory: short01 at about 30 s has a subtitle wrap orphan ("frozen samples could / be").

### VERDICT (main): FAIL
### VERDICT (shorts): PASS

#### Required fixes
1. **s248 (director, composition):** move the "DENMAN GLACIER" label from x 600 to **x 720** (keep y 330, size 40, appear
   0.143). It will then span about x 525–915, clear of "SEA LEVEL" (right edge about 430), the rope (x 1032) and "A CANYON" (top
   about 425). Then re-render: `keyframes --shots s248` to confirm, and after that `render --final`. The Shorts do not use s248
   (short01 is the Vostok section, which ends at the s244 counter tick), so they do not need re-rendering.
