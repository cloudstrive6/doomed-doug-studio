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
