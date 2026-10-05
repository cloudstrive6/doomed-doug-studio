# Art review: 007 Every Time Earth Froze

Reviewer: art-director · Date: 2026-10-05

**Assets verdict: PASS.** 30 of 30 assets are APPROVED. I fixed 3 maps myself (stray marks outside the frame). Two composition notes go to the director. They do not block the assets.

## How I checked
- I read the illustrator previews: `assets/previews/007-every-time-earth-froze-assets.png`, `007-props.png`, `007-maps.png`, `007-nature.png` and `007-doug-test.png`.
- I rendered the assets in context with `python -m studio keyframes 007-every-time-earth-froze --shots` on s010, s025, s044, s050, s063, s100, s106, s127, s130, s132, s138, s142, s148, s182, s183, s218, s219, s242 and s258.
- I rendered extra test boards to /tmp:
  - `puffy_parka` on point, hands_hips, panic1 and stand;
  - `antarctica_map` at 1.15 on ocean blue;
  - `printed_card` at 1.6 with the reserved text box drawn on top;
  - `pnw_map`.
- I checked the geometry against the numbers in `asset_requests.md`:
  - the four Doggerland frames are identical: rect (-595,-450,1190,900), and the Norway polygon is the same in all four;
  - the two North America frames are identical: (-720,-420,1440,840);
  - `cn_tower` is exactly 600 tall and `eiffel_tower` exactly 512 tall;
  - the `kitchen_chair` seat lines up with the snow line in s010;
  - the Storegga point (165,-358) is inside the frame, about 45 units off the Norwegian coast. That is correct for a slope slide.

## Fixes made by me
1. **`north_america_map`, `north_america_ice_map` and `pnw_map`:** I removed the white wave squiggles that sat **outside** the map frame:
   - one squiggle at x 816..864 on each North America map;
   - three squiggles at x -880..-780 on `pnw_map`.

   They were invisible on white previews, but on the light-blue sky backgrounds used in s106, s127 and s138 they would show as stray marks outside the frame. Nothing else changed, and the frames and coordinates are untouched. I re-rendered s106, s127, s138 and s258 and they are clean.

## Assets (30)

| # | Asset | Verdict | Notes |
|---|---|---|---|
| 1 | deck_chair | APPROVE | Red and white canvas sags, the back leans left, and the wood is on spec. Doug's hip sits on the canvas in s025. Bold and readable. |
| 2 | deck_chair_folded | APPROVE | The stripes still read when folded. The cross strap sells "folded". |
| 3 | red_barn | APPROVE | Gambrel roof, X-braced white doors, hayloft. The roof shape is simple enough for the snow spray. Strongest prop in the batch. |
| 4 | kitchen_chair | APPROVE | The seat top sits on the snow line exactly (s010). The slatted back reads as a ladder-back, which is fine. |
| 5 | old_london_bridge | APPROVE | 19 arches with starlings stay distinct at 0.7, and the house row is crude and charming. At 2.0 (s044) the arches are the hero. The 768 width was already flagged to the director and is fine. |
| 6 | fair_booth | APPROVE | Blue and cream tent, pennant, blank sign. Reads at about 0.5 (s050). |
| 7 | printing_press | APPROVE | Screw, bar handle, platen and paper stack are all legible, and the dark wood is on spec. |
| 8 | printed_card | APPROVE | Verified: the reserved centre (x -170..+170, y -90..+60) is completely blank. The border, flourishes and curl stay outside it. Works with "DOUG" in s050. |
| 9 | elephant | APPROVE | Calm, plodding, small ears, curled trunk, red harness blanket. A dot eye is fine for an animal (no cartoon face). |
| 10 | north_sea_today | APPROVE | world_map style, no labels, Norway coast inside the frame. |
| 11 | doggerland_map | APPROVE | The land bridge is unmistakable. Rivers and marsh dots add detail without clutter. |
| 12 | doggerland_islands | APPROVE | Four low islands at the Dogger Bank. Overlays cleanly in s063. |
| 13 | doggerland_island | APPROVE | One island, sea everywhere else. |
| 14 | pnw_map | APPROVE (fixed 1) | Dashed 49N border, faint state lines, Columbia reaches the coast, the Wyoming corner is correct. The Pacific is only a sliver because of the projection, as specified. |
| 15 | north_america_map | APPROVE (fixed 1) | Hudson Bay, the Great Lakes, the Mississippi, Cuba and the Greenland edge are all present. Huron and Hudson Bay circles land correctly (s138, s258). |
| 16 | north_america_ice_map | APPROVE (fixed 1) | Lobed white ice with a pale-blue edge, Chicago under ice, Cordilleran ribbon on the Alaska coast. Same frame as `north_america_map`. |
| 17 | antarctica_map | APPROVE | The Peninsula points upper-left, the Ross and Weddell shelves are bluer, no ocean fill. Two tiny non-blocking nits are listed below. |
| 18 | dryas_flower | APPROVE | 8 white petals, yellow centre, toothed dark leaves, no face. Clear at 0.6 and inside the ice block (s100). |
| 19 | cn_tower | APPROVE | Exactly 600 tall, window-band pod, red and white spire. |
| 20 | eiffel_tower | APPROVE | Exactly 512 tall. At 0.155 it holds as a bold brown A-shape and stacks cleanly (s132). |
| 21 | puffy_parka | APPROVE | Head, face and cap are fully clear. Quilted bands and the fur collar are on palette. See director note 1 about the `point` pose. |
| 22 | puffy_parka_flat | APPROVE | Squashed, sweat drops face the sky, the cap stays visible (s219). |
| 23 | palm_tree | APPROVE | Ringed curved trunk, drooping fronds, coconuts. |
| 24 | beech_tree | APPROVE | Layered canopy with highlight clumps. The flat tiers lean a little "acacia", but Nothofagus is tiered and it reads as a temperate tree beside the palms. Non-blocking. |
| 25 | picnic_blanket | APPROVE | Gingham in 3/4 view, sandwiches and a green flask at the right. A seated Doug sits on it. |
| 26 | meganeura | APPROVE | Dragonfly silhouette, two pairs of veined clear wings, compound eyes, no face. The 500 wingspan line works in s182. |
| 27 | front_door | APPROVE | Panelled red-brown door, white frame, brass knob, transom window. |
| 28 | scale_tree | APPROVE | The diamond leaf-scar pattern is the hero detail. Forked tufts and root flare are there. |
| 29 | stromatolites | APPROVE | Stacked wavy layers, green-blue film, bubbles. Reads as living rock, not as a face or a cake. |
| 30 | algae_patch | APPROVE | Friendly lime clump with strands and bubbles, no face. Reads in the pond in s242. |

Style check (style bible section 7):
- **Two tier:** every creature, place and prop is in the detailed tier with interior shading and layered fills, against the crude Doug.
- **Gore:** none.
- **Palette:** hexes match the requests and the art bible (ice `#dff4ff` family, wood `#a0522d`, cap red `#e0201b` kept for Doug only).
- **Silhouettes:** bold enough for the s181 silhouette beat (meganeura).

## Notes for the director (composition, non-blocking for asset approval)
1. **s142 "Doug plants a flag":** the parka covers most of the `point` arm, because the arm reaches x +120 and the parka shoulder reaches +99. Only a short stub of hand shows. The flag pole is at x 980, but the hand is at about x 800, y 592. **Fix:** move the pole and sign so the pole is at x about 800 (the hand), with the sign to its right. Keep the parka listed *after* Doug. I tested drawing it first, and the stick body showing through the jacket looks like an X-ray.
2. **s183:** the `front_door` at scale 1.1 overlaps the right-hand `scale_tree` trunk, and the door frame cuts into it. Nudge the door left by about 60 px or the tree right by about 60 px so each has its own outline.

## Nits for the illustrator (optional, next pass only)
- `antarctica_map`:
  - near the Ross shelf (local about (40..60, 270..340)) the coastline outline has a gap with a thin sliver of background showing;
  - the Peninsula tip has a few small unoutlined white shards.

  Neither reads at shot size (s148, s158).
