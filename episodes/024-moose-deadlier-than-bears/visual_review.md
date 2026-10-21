# 024-moose-deadlier-than-bears: visual review

## Round 1: keyframes (2026-10-21)

**VERDICT: FAIL**

I checked all 24 contact sheets (s001 to s279 plus the endslate) and opened full frames for s007, s010, s033, s035, s038, s047, s050, s056, s071, s074, s084, s100, s110, s129, s143, s180, s189, s196, s236 and s272.

**What passes**
- Doug is on-model in every shot (red cap, white head, crude stick body) and readable on every background, including the navy Apples nights and the snow.
- The death counter runs 195 to 203 with exactly 8 deaths: s026, s074, s123, s145, s172, s196, s245, s274. Each one follows a black beat and shows the cap and the field guide "NO". The BEAR/MOOSE scoreboard ticks match the script: ties up to 5-5 at s118, then moose only, ending 5-11.
- **Sober cards pass.** Anchorage, 1995 (s146-s148) and the Newfoundland/Maine cards (s258-s263) are plain slate with white text. They have no Doug, no counter, no scoreboard, no names and no jokes. The text is legible and not cropped.
- No gore anywhere. Deaths are the cartoon ghost and cap. Calf mortality (s067/s068) is a sober bar chart. The frozen bulls (s189/s190) show only antlers above the ice. Nothing is in a kids'-show tone. Chapter titles, labels and the endslate are legible and spelled correctly.
- The locked_antlers_ice redraw (art review fix 1) now reads as interlocked palmate racks. The Newfoundland icons now sit on land at Gander Bay and Howley (art review fix 2).

**Required fixes**

1. **s071, s072, s074: remove the grizzly from the calf scene (director).** A small `grizzly_bear` (x 1770, scale 0.2) stands beside the willows, and it is still in frame at Doug's death in s074. A viewer can read it as the bear killing Doug. That breaks the episode's punchline ("He has never even met a bear", BEAR deaths 0). Delete the asset from all three shots. The black-bear silhouette at s070 already makes the "shaped like a bear" point.
2. **s143: the bull turns into a cow (illustrator + director).** In s142 the moose is an antlered bull. In s143 it becomes `moose_cow_rearing`, which has no antlers and a mane, so it reads as a rearing horse. Have the illustrator add a `moose_bull_rearing` variant (the same pose with the `moose_antler_rack` attached, keeping the bulbous nose and bell) and use it in s143. Optionally use it in s129 too, which is a generic charge where the horse read is also strong. s137 (cow defending her calf) stays as it is.
3. **s035: the plants are invisible and the water has two surfaces (director).** The five `seagrass` assets sit under the water rect, so the "PLANTS" arrow points at an empty lake bed. The paddleboard floats at y≈470 while the waterline is at y=380, which cuts the moose's legs off at a second line. Draw the seagrass after the water fill. Put the paddleboard on the y=380 waterline. Have the moose wade with its legs going below the single surface line.
4. **s047: Doug stands on open water (director).** He has no paddleboard here, although he is on the board in s046 and s049. Put him back on the `paddleboard` at the waterline, or stand him on the shore strip.
5. **s180: the map label is on the wrong side of the continent (director).** "ALASKA + NW CANADA" sits at x 1500 / y 640, next to Quebec and the Atlantic coast, while the red circle is on Alaska. Move the label next to the circle (about x 420, y 580, below the circled area) and put the shed antler rack beside it.
6. **s056: the calendar text overflows the page (director).** "MAY - JUNE" at size default is wider than the calendar page, so the M and E hang off both edges. Either cut the calendar text (the "MID-MAY TO EARLY JUNE" label already says it) or shrink it to fit inside the page with a margin of at least 10 px.
7. **s236: the red circle cuts through the text (director).** The circle (r≈70) crosses the "0" of "KILLED: 0" and clips "STOOD STILL". Enlarge it to an ellipse of about 220×70 centred on "KILLED: 0", so it surrounds the whole line without touching any glyph.
8. **s100: the crossed-out gravestone floats in the tree (director).** The `gravestone` and `red_x` at (700, 600) hang mid-trunk, overlap the moose's dangling legs, and make "RIP DOUG" unreadable. Move both to the ground at about (560, 880), clear of the trunk and the field guide, so the narrator's "prepared" grave reads.

**Should fix (not blocking alone; do them in the same pass)**

9. **s229/s230: wrong aircraft (illustrator/director).** The `airplane` is a modern passenger jet. Mech tracked the pack from a small ski plane. Use a small high-wing bush plane (illustrator, new `bush_plane` asset) or drop the plane.
10. **s114, s119: the split-screen divider runs through the chapter tag (director).** The vertical line crosses the "THE RUN" box. Start the divider below the tag (y ≥ 60).
11. **s037: "NO OTHER DEER" is drawn behind the pines (director).** Tree tips poke through the letters. Draw the label after the trees, or move it to y≈100 above the treeline.
12. **s044: "18 FT? UNMEASURED" appears too early (director).** The narration here only says "reported dives of more than eighteen feet". Show "18 FT+" here and keep "UNMEASURED" for s046, where the narration lands it.
13. **s216: the moose never "turns to face the train" (director).** It is the same side view as s215. Flip it, or swap to a rear/three-quarter view toward the headlight, so the beat shows on screen.
14. **s109, s110: the moose and the bear overlap (director).** The bear's head sits inside the moose's front legs, so the two silhouettes merge. Space them about 150 px apart. In s110, drop the "ABOUT 56 KM/H" label or put it directly over the moose, and put "UP TO 64 KM/H" directly over the bear.
15. **Variety (director).** There are a few runs of 4 or more near-identical frames:
    - s249-s255 has seven Newfoundland map frames in a row. Push in on the island, or cut s253/s254 to the black bear on a plain coastline.
    - s258-s263 has six dark text cards. Keep them sober, but make the moose-vs-deer icons in s261 large (about 200 px; they are about 30 px now) and keep them on s262-s263 so the Maine card looks different from the Newfoundland card.
    - s042-s046 has five near-identical underwater-moose frames. Vary the scale or crop once, for example a close-up on the nose for s042.
16. **s200, s266: the newspaper/article pictures read as a fish or lizard (illustrator).** Put a small moose silhouette in the article picture box.
17. **s050-s052: the surfacing head reads as a horse at small size (illustrator).** This is the optional polish from the art review. Make the ears broader, leaf-shaped and angled outward.

**Dependency (graphic designer, before the render)**
- **s001** still shows "(thumbnail pending)". It is the thumbnail scene_ref and must be in place before `render --final`. I will screen it in the post-render round.

**Routing:** director: 1, 2 (shot swap), 3-8, 10-15; illustrator: 2 (new rearing bull asset), 9, 16, 17; graphic designer: s001 thumbnail. After the fixes, re-run `keyframes` for s035, s037, s044, s047, s050-s052, s056, s071-s074, s100, s109, s110, s114, s119, s129, s143, s180, s200, s216, s229, s230, s236, s249-s263 and s266, and send them back for round 2.
