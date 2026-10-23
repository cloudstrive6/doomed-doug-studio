# Visual review: 026-deep-sea-giants

## Round 1: pre-render keyframes + thumbnails (2026-10-23)

Screened: all 24 contact sheets (s001-s281 + endslate, 281 shots), `build/thumbnail.png`, `thumbnail_b.png`,
`thumbnail_c.png`, their `_small` files, and my own 168x94 feed-size downscales of all three (the `_small` files on
disk are 320x180, not 168x94).

VERDICT: FAIL

### What passes
- Doug is on-model in every shot: red cap, white head, readable on the navy and black backgrounds. The capless
  shots (s052-s056, s133-s135, s230) are on purpose because the story takes the cap.
- Deaths are cartoon only (X eyes, ghost Doug, frost ball, squashed under a leg) and the counter runs 210 to 218 in
  order. No blood, no organs, no dismemberment. The whale "pieces of arms" in s127 is a small hooked arm, not a
  wound. Labels like the s170 blood cell and s222 REPRODUCTIVE ORGANS are diagrammatic and fine.
- Tone is adult deadpan ("roommates?", "hi friend?", RENT FREE, the BUS sign). Nothing reads as a nursery show.
- The creatures are recognisable: oarfish, spider crab, phantom jelly, isopod, colossal squid, Greenland shark,
  tube worms, bigfin squid, sea spider, amphipod, xenophyophore. The s274 recap column reads well.
- I found no spelling errors in the on-screen text.

### Required fixes
1. **s213** (director): the key subject is invisible. `giant_sea_spider` at scale 0.04 sits at (828,776), right on
   Doug's cap brim, so the A FEW MM arrow seems to point at Doug's cap. Move the tiny spider onto the mud in front
   of Doug (about x 900, y 915) at scale about 0.08-0.10. Add a white circle or magnifier ring around it and aim the
   arrow at the ring.
2. **s177, s238, s254, s272** (director): on the WHY SO BIG? clipboard, "BRING YOUR OWN FOOD" runs into both edges
   of the paper. In s177 and s238 the narrator's glove also covers "FOOD" and "MORE OXYGEN". Shrink every clipboard
   line one step, or wrap that line to "BRING YOUR / OWN FOOD", and move the hand down below the last line (or onto
   the board's right rim) so it covers no text.
3. **s161** (director): the red "GIANT TUBE WORM" title sits on top of the red worm plumes ("WORM" is red on red).
   Raise the title to about y 250, or drop the worm clump about 120 px, so the title sits on clear water.
4. **s023** (director): the ROBOT SUBMARINE wordart (560,820) is drawn over Doug (260,830). Move the text to about
   (600,330) above the ROV, or move Doug further left/up out of the text band.
5. **s018** (director): "PREDICTS NOTHING" (1400,800) runs into the right edge of the Japan map. Move it to about
   x 1560 / y 860, or shrink it to 64, so it clears the map frame.
6. **s262** (director): the small red dot under the white arrow (`red_blood_cell` at scale 0.12) has no label and
   reads as a stray mark. Add a "BLOOD CELL" label next to it and scale it up to about 0.25, or cut it.
7. **s165** (director): Doug (250,560, scale 0.3) is drawn on top of the left black smoker and vanishes into it.
   Move Doug and his cable to clear water (about x 380) or scale him to 0.4.
8. **s203** (director / art director): the narration says Doug hangs "with his arms bent at the elbows", but he is
   in pose `arms_up` with straight arms. Use an existing bent-arm pose if one exists. If not, the art director needs
   to add an "elbows out" pose (arms out sideways, forearms down, like the squid). The gag only works if the pose
   copies the squid. Also move BLEND IN (760,960) off the squid's filaments and the mud line, for example to y 300.
9. **Variety runs** (director): these stretches repeat the same staging (creature centre or right, Doug small on
   his cable at left, same background) for 4 or more shots in a row:
   - s069-s075 (phantom jelly, 7 shots)
   - s163-s166 (tube worm clump between two smokers)
   - s203-s206 (bigfin squid)
   - s220-s226 (sea spider centred, 7 shots)

   Break each run with at least one different framing: a tight crop on one detail (the jelly bell with the brotula,
   a single worm plume, one squid elbow), a cutaway, or a camera push or zoom. Good spots are s072-s073, s164, s204
   and s222-s224. Reuse existing assets only.
10. **Thumbnail C** (graphic designer): at 168x94, "Colossal Squid" and "Greenland Shark" are set much smaller than
    the other labels (about 6 px tall) and cannot be read. Use one label size for all six tiles; let the two long
    labels wrap to two lines, or trim the tile art height to make room. The YouTube duration badge will also sit on
    the "One Cell" tile's bottom-right corner, so move that tile's label or keep its key content clear of the bottom
    right.
11. **Thumbnail B** (graphic designer): at feed size Doug is a tiny face inside the tentacles, and the left half of
    the frame is empty apart from the text.
    - Scale the jelly and Doug up about 20% and shift them left so Doug's face lands near the frame's centre third.
    - Remove the stray thin tentacle stub sticking out to the right at about (1050-1100, 470).
    - The winch cable now ends on the bell rather than at Doug's harness. Run it to his hand, or remove it.

### Minor fixes (should fix, not blocking on their own)
12. **s012** (director): the red ripple curve (1360-1395, from y 160) floats free of the fish and starts right
    under the CABLE OUT box, so it reads as a stray line. Lay it along the oarfish's dorsal fin, or start it below
    y 300.
13. **s027, s065, s190, s206** (director): wordart touches the creature (NOTHING HAPPENS on the oarfish's tail,
    ABOUT 100 TIMES on the jelly bell, 20 TIMES on the squid's filaments, ISN'T DOUG on the filaments). Nudge each
    one 60-100 px into clear water.
14. **s057, s185, s253** (director): the red item titles overlap the reveal silhouette (s057, s185) or Doug's cable
    (s253). They are still readable, but raising each title about 80 px would clean it up.
15. **s071** (illustrator / director): the brotula silhouette (scale 0.6) on top of the bell reads as a black hole
    in the jelly. Scale it to about 0.9, or lift it 30 px above the bell so its fish outline reads.
16. **s013, s014, s018** (director): Doug stands in open water at 250 m with no cable or harness. Either add the
    harness and cable, or set these map cutaways on the beige "explainer" background like s016/s017.
17. **s136-s141, s145-s147, s153, s159** (art director): the frosted cable (the white dashed width-13 overlay)
    reads as a zipper or ladder at 1080p, and it vanishes in s142-s143 then comes back. Keep it, but make it
    consistent across the whole Greenland chapter and lower its contrast (for example #c9d6e6 and a thinner
    dash).

### Thumbnails at 168x94
- **A (HOOKS, squid eye + hook arm + Doug): best of the three.** One focal point (the eye), with Doug and the hook
  visible next to it and big readable text. It fits the title and is not misleading, because Doug dies to these hooks
  at s133-s134. No changes required.
- **B (10 METERS, jelly wrap):** readable text and a clear threat, but Doug is too small. See fix 11.
- **C (6-tile grid):** clean list-format control, but two labels are unreadable. See fix 10.
- **Pipeline note:** the `*_small.png` files are 320x180. If the gate expects 168x94 previews, regenerate them at
  that size.
