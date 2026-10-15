# Visual review: 019-drawn-completely-wrong

## Round 1: pre-render keyframes + thumbnail (2026-10-15)

Scope: contact sheets `build/contact/sheet_01..25.png` (s001-s293, all 293 shots). Spot-checked these full keyframes:
s017, s018, s083, s186, s205, s215, s216, s235, s275, s288. Also checked `build/thumbnail.png`,
`build/thumbnail_small.png` and `thumbnail.json`. The shotlist was read only; I did not edit it.

VERDICT: FAIL

Overall the episode reads well. The OLD DRAWING card device is clear and consistent. Chapter bars match the items.
The death counter steps 154 -> 161 on the right beats: s032, s085, s109, s185, s208, s237, s289. That matches the
script plan (deaths on Brontosaurus, Elasmosaurus, Stegosaurus, Hallucigenia, Dimetrodon, Therizinosaurus and
Spinosaurus; survivals on Iguanodon, Megalosaurus, Deinocheirus and Homo diluvii). Doug is on-model in every shot.
There is no gore, and the deaths are cartoon (dust clouds, splashes, caps, ghosts). Nothing has a kids'-show tone. On
screen, "Öhningen" (s242) renders correctly.

The fixes below are mostly text overlapping drawings, one contradictory stamp, two "rivers" that read as grass, one
gore-adjacent detail, and one run of identical frames.

### Required fixes

1. **s017 (director): the APATOSAURUS label covers Elmer Riggs's body.** The scientist is at (1180, 860) and the label
   at (1260, 900), so the label box sits on his torso and legs. Move the scientist to x 1460, scale 0.5, and Doug to
   x 1760, so the scientist stands clear between the label and Doug. Or move the scientist up and left to (960, 700),
   above the "=".
2. **s018 and s026 (director): the wordart overlaps the old drawing card.** "OLDER NAME WON" (s018) and "THE NAME IS
   BACK" (s026) are centred at x 1120, and their left ends run over the card's top-right corner (card right edge is
   about x 860). Move both wordarts to x 1220 (same y 360). They still clear the DOUG DEATHS box vertically.
3. **s205 (director): "RELATIVES" reads as crossed out, which is the opposite of the line "It's family."** The
   `red_x` (scale 0.5 at 820, 799) is about 150 px tall. The cream patch rect is only 48 px tall, so the X's four
   arms stick out around "RELATIVES". Remove `red_x` from s205. Put the X in **s190** instead ("It is not a dinosaur"),
   over the DINOSAURS plate at (820, 799) with appear 0.3. Then s205's patch-and-relabel reads as a correction, not a
   rejection.
4. **s215 (director): the "4.5 m" dimension line and label run through the card header.** The line is at y 330 and
   the label at y 300, right through "OLD DRAWING" and the "1954" box. Move the dashed line to
   `[[420, 955], [1220, 955]]` and the label to (820, 955), under the card on the floor strip. Doug at x 1600 is clear.
5. **s054 (director): the DEFENSE warning triangle sits on the Iguanodon's face.** The triangle at (1180, 420) covers
   the head and eye. Move the triangle to (1520, 420) and the "DEFENSE" label to (1520, 300). The head ends around
   x 1370.
6. **s275 (director): the middle giraffe's head pokes through the "ABOUT 15 m" label.** The giraffe tops out at the
   line y 730. Raise the dashed line and label to y 685, and drop the giraffes to scale 0.34 so the heads end below
   about y 760. Optional: lay the three giraffes nose to tail horizontally to match "laid nose to tail".
7. **s157-s160 and s287-s291 (director): the "river" reads as a grass slope.** The polygon fill `#6f8a6e`
   (Deinocheirus) and `#6b7a4a` (Spinosaurus) is a dull green on green or tan ground. So "dips its bill into the
   river", "checking the river after each one" and the s289 splash all land on what looks like a hill. Recolour the
   poly to water: fill `#3a9ad9`, outline `#1f5f8f` (the s075 sea colours). Add 3-4 short white wave ticks. In s289 the
   splash will then read as Doug going into the water.
8. **s286 and s288 (illustrator / art director): the Spinosaurus silhouette appears to drip blood.** In silhouette +
   red-rim mode, the "water dripping" shapes under the jaw of `spinosaurus_mystery` render as black drops with red
   rims hanging from the snout. That reads as blood dripping from the mouth, which is close to our no-gore line, and
   this silhouette is also the likely Shorts end-card tease. Remove the drip shapes from the asset, or keep them out of
   the silhouette pass (for example draw them after the silhouette as light-blue `#cfe9ff` drops). Then re-key s286 and
   s288 and re-check the silhouette.
9. **s215-s218 (director): run of 4 near-identical frames.** It is the same 1954 turtle card at (820, 590), scale
   1.2, with Doug at right; only the caption changes. s211 is the same frame too. Keep s215 and s216 (after fix 4) and
   change two:
   - s217 "He even named the species for it": add a custom camera push from `[960, 540, 1.0]` to `[820, 820, 1.35]`
     so the shot lands on the CHELONIFORMIS label (keep the label inside the central 80%).
   - s218 "Cheloniformis means turtle-shaped": shrink the card to the s016 layout (scale 0.75 at x 560), and put Doug
     in `sea_turtle_costume` at right (x 1350) with "TURTLE-SHAPED" wordart above him. This gives a new frame and a
     joke.

### Advisory (not blocking)

- **s083**: the silhouette-then-reveal is by design (decisions.md). At scale 0.45, though, the black neck reads as a
  pillar and the line is "The long end has a mouth". Consider scale 0.6 so the head and jaw profile reads in
  silhouette.
- **s268 (tone)**: the April 1944 bombing uses the same slapstick dust cloud with stars and spirals as Doug's deaths.
  Real people died in that raid. Use the dust cloud without the stars and spirals (or smoke only) so it doesn't read
  as a gag.
- **s099**: the Far Side beat is a blank blackboard plus a pencil. Draw an original chalk doodle of a spiked tail on
  the board (not a copy of Larson's panel) so the shot shows something.
- **s193 "long gone before the first dinosaurs appeared"**: Dimetrodon and the dinosaur stand side by side, as if they
  met. Add a gap with a red time arrow between them, or grey out the Dimetrodon.
- **s237 "Doug has died. Again."**: the Therizinosaurus has left the frame, so only a cap, plants and leaves remain.
  Keep the animal (or its claws) at the right edge so the cause is obvious. s238 brings it back anyway.
- **s071**: Marsh's paper covers half of his face. Lower it to chest height.
- **s172**: the "1991" label overlaps the card's left edge. Move it to x 80.
- **s186**: the upside-down cap fossil reads as a cap at full size but weakly in the sheet. A bit more red in the cap
  fossil would help.
- **Editor (subtitles)**: the contact-sheet caption font has no "ö" ("Ramsk?ld", "?hningen" in the s172, s174 and
  s242 captions). The on-screen label is fine. If the Shorts or YouTube burned-in subtitles use the same font, swap it
  for one that covers Latin-1.

### Thumbnail (`build/thumbnail.png`, `build/thumbnail_small.png`): PASS

- Archetype A, 11 tiles, white canvas, black rounded frames, chapter-name labels, no title words, no Doug (allowed
  for A). At 320x180 every tile still reads: boxy Brontosaurus, nose-horn Iguanodon, the backwards plesiosaur, the
  plate-roof Stegosaurus, the arms with a "?", the 1977 Hallucigenia, the turtle and the slab. Red X stamps are crisp.
  It fits the title "...Scientists Drew All Wrong" and is not misleading. s001 matches the thumbnail.
- Advisory (graphic designer): the **Dimetrodon** tile is the only one showing the modern, correct animal, and it is
  stamped with an X, which implies the real animal is wrong. Consider a sepia "toy dinosaur" redraw (the
  `gift_shop_shelf` plate) or a sepia Dimetrodon in the old-card style, to match the other ten tiles.
- Advisory: "Homo Diluvii Testis" is set at label_size 32 (the others are 36), so it looks like a different weight.
  It fits at 34. Also, the slab tile reads more as a "seed with a tail" than a skeleton at feed size; a white
  "man-shaped" dashed outline around the fossil would make the joke readable.

### Routing summary

- Director: fixes 1-7 and 9 (s017, s018, s026, s054, s157-s160, s190, s205, s215, s217, s218, s275, s287-s291).
- Illustrator / art director: fix 8 (`spinosaurus_mystery` drips in silhouette mode; re-key s286 and s288).
- Graphic designer: thumbnail advisories only.

Re-key the changed shots and send the new sheets back for round 2.

## Round 2: re-rendered keyframes (2026-10-15)

Scope: all 25 contact sheets (s001-s293) re-viewed for regressions. Full 1080p keyframes opened for s017, s018, s026,
s054, s158, s190, s205, s215, s217, s218, s275, s286, s288 and s289. Camera blocks checked in `shotlist.json`.

VERDICT: PASS

### Round-1 required fixes

1. **s017**: FIXED. The scientist now stands at x 1540, clear of the APATOSAURUS label and next to Doug.
2. **s018 / s026**: FIXED. "OLDER NAME WON" and "THE NAME IS BACK" start at about x 960, well clear of the card's
   right edge (x 860).
3. **s205 / s190**: FIXED. s205 has no X; the cream patch with red "RELATIVES" reads as a correction. s190 now has the
   red X over the DINOSAURS plate, which matches "It is not a dinosaur".
4. **s215**: FIXED, with a different placement from the one I suggested. The dashed line and "4.5 m" now sit above the
   card (y about 210-230) and clear the OLD DRAWING header and the 1954 box. That works.
5. **s054**: FIXED. The warning triangle (1520, 420) and DEFENSE label (1520, 300) are clear of the Iguanodon's head.
6. **s275**: FIXED. The line and "ABOUT 15 m" are at y 685, and the giraffe heads end around y 760, below the label.
7. **s157-s160 / s287-s291**: FIXED. The river is now blue water with an outline and white wave ticks. "Dips its bill
   into the river" (s158) and the s289 splash now clearly happen in water.
8. **`spinosaurus_mystery` (s286, s288)**: FIXED. The drip shapes are gone from the asset. The silhouette has a clean
   red rim and nothing hangs from the jaw. No gore reading on navy-teal or orange.
9. **s215-s218 run**: FIXED. s217 adds the CHELONIFORMIS label plus a push to [1150, 560, 1.15], which is lighter than
   the push I suggested but keeps the label in frame. s218 is a new frame: a small card on the left, Doug in the turtle
   costume, and "TURTLE-SHAPED" wordart. The run is broken.

Round-1 advisories that were also taken up: s099 (the blackboard now has a chalk spiked-tail doodle), s268 (plain smoke
cloud with no gag stars or spirals), s172 (the 1991 label no longer overlaps the card). Still open and not blocking:
s237 (no Therizinosaurus in the death frame), s193 (the two animals still stand side by side), s071 and s083.

### Regression scan
No new problems. Every shot has Doug on-model. The counter still steps 154->161 at s032, s085, s109, s185, s208, s237
and s289. No text is cropped or covers a drawing. There is no gore and nothing reads as a kids' show.

### Advisory (not blocking)
- **`spinosaurus_mystery` silhouette for the Shorts end card (director / illustrator)**: in the keyframe the silhouette
  works as "something is under the water". On its own as a tease, though, the raised snout reads a bit like a raised
  arm or mitten, and the double-hump sail like two boulders. If this becomes a Short's `tease_asset`, consider showing
  more of the jaw profile (open jaw or a visible tooth row notch) so it reads as "croc-snouted dinosaur" at phone size.
  I will check this again at the Shorts end-card stage.
- Caption font still lacks "ö" in the contact sheets (s172, s174, s242). This is editor-side only, and the on-screen
  label is correct.

### Routing
None required. Ready for art_approved from a visual-screening standpoint.

## Post-render, 2026-10-15
Full report: `reviews/visual_review_postrender.md`.

1. **s092, s098, s108, s139, s143, s250 (director):** the zoom-in (1.08) crops the last digit of the death counter. Set `camera.x` to 960.
2. **s007, s015, s043 (director, same pass):** the zoom (1.06) shaves the counter's right border. Set `camera.x` to 960.
3. **short03 (illustrator + director):** the `spinosaurus_mystery` end-card silhouette isn't recognisable as a Spinosaurus. Add a tease-only `spinosaurus_mystery_tease` with a croc-snout profile and one continuous sail, and set it as short03 `tease_asset`.

Thumbnail: PASS (unchanged). short01 and short02 cliffhangers: PASS.

VERDICT (main): FAIL
VERDICT (shorts): FAIL (short03 silhouette)
