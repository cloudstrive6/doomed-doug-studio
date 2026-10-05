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

## Keyframes round 1

Reviewer: art-director · Date: 2026-10-05

**Verdict: FAIL.** There are 35 numbered fixes covering 48 distinct shots, plus two pond shots to recompose (fix 35). All of them go to the **director** (composition). None of them needs an illustrator change.

The style itself is in good shape and needs no rework:
- Doug is on-model in every shot: cap, crescent, oval eyes and thin lines. The parka, ice block, ghost, sunglasses and `on_back` death beats all follow the bible.
- The ice and snow family (`#dff4ff` and its tints), sky, sea and the orange greenhouse palette are consistent within each item.
- The death counter runs from 56 to 65 with no gaps. 65 matches the series bible (006 ended at 56, and there are 9 deaths).
- There is no gore anywhere.
- Each item opens with a red title card, and maps, diagrams and scenes alternate well.

What fails is placement: Doug turns invisible, Doug floats in the air, wordart sits on map frames, props intrude on the death-counter zone, and there is one stray paint patch.

I skipped s001 (the thumbnail does not exist yet). Coordinates below are 1080p scene units from `shotlist.json`.

### A. Blocking: Doug invisible or broken
1. **s036, s037, s038, s050, s051:** Doug auto-inks **white**. His auto-ink point lands on the dark `old_london_bridge`, so his legs vanish white-on-white against the ice and only his head and cap read (I checked the single frames).
   - **Fix:** add `"ink": "#000000"` to the `doug` element in all five shots. Black reads fine against the mid-brown arches.
2. **s238:** the `rect` (250,500,300x330) that hides the walking Doug runs past the ground line. It paints a light notch into the horizon at about x 250-550, y 800-830.
   - **Fix:** make it `"y": 500, "h": 290` so it stops at y 790 above the ground line. The walking Doug's feet are at 781, so he stays covered.

### B. Blocking: the death-counter zone (x 1300-1860, y 110-230, plus the globe at 1795,165) must stay clear
3. **s147:** the second `beech_tree` (1750,470, scale 0.7) has its crown behind the globe and FROZEN tag.
   - **Fix:** move it to about (1130,600) at scale 0.6, or drop it from this title card.
4. **s172:** the `scale_tree` (1600,830, scale 0.8) has its crown on the globe and counter.
   - **Fix:** use (1250,830) at scale 0.7. The crown top is then about y 290.
5. **s195:** the right `scale_tree` (1650,790, scale 1.0) has its crown on the globe.
   - **Fix:** drop that tree, or bring it forward to (1700,1040). Its base then sits low in the ground band as a nearer tree, and the crown top is about y 250.
6. **s273:** the red arrow starts at (1350,200), inside the counter zone, touching the "DOUG DEATHS: 65" box.
   - **Fix:** point at the cap from the left: `from [650,180] to [890,250]`.

### C. Blocking: Doug floating in the air when there is a surface (feet must be at y + 152 x scale)
7. **s107, s108, s110:** Doug (1250,210, scale 0.4) hangs about 90 px above the dam top, which is at y 360. In s110 his head nearly touches the chapter bar.
   - **Fix:** set `"y": 299` in all three shots so he stands on the dam (the same as the s121 fishing set).
8. **s042:** Doug (300,480) floats in the grey sky.
   - **Fix:** put him on the ice at (300,760) at scale 0.4.
9. **s048:** Doug (1820,330) floats at the right frame edge, outside the safe area.
   - **Fix:** stand him on the left bank at (120,464) facing right. The bank top is at about y 525.
10. **s069, s070:** Doug (1480,360, scale 0.4) floats about 100 px above the coast.
    - **Fix:** set `"y": 465` in both shots. In s070, move the `MORE?` label to (1650,300) so it clears his arm.
11. **s089:** swimming Doug (1300,250) swims in the sky above the sea line at y 300.
    - **Fix:** set `"y": 330` so he swims in the FRESH layer.
12. **s214:** swimming Doug (1650,200) swims in the orange sky.
    - **Fix:** set `"y": 300` so he is at the sea surface.
13. **s114:** Doug (640,450) floats, and the wordart "CHANNELED SCABLANDS" sits on his head.
    - **Fix:** set Doug to `"y": 510` so his feet are on the ground at 600. That also clears the wordart.

### D. Blocking: wordart crossing a map frame or a drawing (art bible, Text)
The pattern for maps is to **shrink the map and raise it so the wordart sits in clear sea or sky.** When you rescale a map, move everything drawn on it (labels, circles, the small Doug) with this formula: `new = centre + (old - old_centre) x (new_scale / old_scale)`.

14. **s019 and s090** (`world_map` 0.9 at y 560; the frame bottom is at about 915; the wordart at y 900 sits on the frame and the ice):
    - **Fix:** use the map at 0.8 at (1020,500), so the frame bottom is about 820, and the wordart at y 930.
15. **s059, s062, s073** (`doggerland_*` 0.95 at y 560; the frame bottom is at about 990):
    - **Fix:** use the map at 0.8 at (960,500) and the wordart at y 950.
    - s059: you may instead move "HILLS, RIVERS" to size 60 at (1720,330) in the right margin.
16. **s134:**
    - **Fix:** move "DRY" to size 100 at (1730,330) in the right margin. It is short enough to fit there.
17. **s068:** "TSUNAMI" (560,300) crosses the left frame edge, and the wave arcs run above the frame top (y about 90-135).
    - **Fix:** use size 72 at (1725,330) in the right margin, and start each arc at or below y 140 so the waves stay inside the frame.
18. **s127:** "PEAK" (1500,900) sits on the frame and on Cuba.
    - **Fix:** use size 80 at (1775,330) in the right margin, above Doug.
19. **s258:** "HURONIAN" (960,960) sits on the frame bottom.
    - **Fix:** use the map at 0.9 at (860,500) and keep the wordart at y 960.
20. **s014:** "LARGEST ERUPTION" (960,560) sits over the volcano and its lava.
    - **Fix:** use size 80 at (500,180) in the sky to the left of the plume.
21. **s016:** "CUBE" (1020,240) crosses the cube's top edge.
    - **Fix:** move it to (420,330) in the clear sky.
22. **s044 and s046:** the wordart (y about 230-250) sits on the bridge's house row.
    - **Fix:** move it down to the river or ice band: s044 at (1100,990), s046 at (700,1000).
    - s044: also move the red `?` (500,260) off the houses, for example to (300,500).
23. **s101:** "FAVORITE WEATHER" (960,330) crosses the ice block's top edge.
    - **Fix:** move it to (700,200). That keeps it clear of the counter zone too.
24. **s110:** "NOT BUILT TO LAST" (700,200) runs into the warning triangle (800,300).
    - **Fix:** move the triangle to (300,330).

### E. Blocking: text, safe area and overlaps
25. **s088:** the "NORTH ATLANTIC" label (1736,424) runs off the right edge of the frame.
    - **Fix:** set x to 1620 and end the arrow at x 1460.
26. **s076:** the red arrow runs through the "NETHERLANDS" label.
    - **Fix:** end the arrow at (1480,520), or move the label up to y 400.
27. **s118:** the "FLOOD!" bubble covers the "J" of "J HARLEN BRETZ".
    - **Fix:** move the label to x 1420.
28. **s120 and s125:** the medal and ribbon cover Bretz's face (circle at y 340, ribbon top at y 220).
    - **Fix:** hang the medal on his chest. In s120 use ribbon `[[1105,325],[1125,385],[1135,385],[1155,325]]` and circle (1130,410) r 34. In s125 use the same shape shifted to x 700.
29. **s121 and s122:** the `fishing_rod` tip goes up through the chapter bar.
    - **Fix:** reduce the rod to scale 0.45 and lay it flatter over the lake, so the tip ends below y 100.
30. **s185:** the `scale_tree` (960,870, scale 1.2) crown runs into the chapter bar.
    - **Fix:** use scale 1.0 at y 900.
31. **s223:** there are three date labels (14 words, over the 8-word limit), and the two above the booth touch each other.
    - **Fix:** delete "660 MILLION YEARS AGO" (1500,230) and the booth tag "717 MILLION YEARS AGO". Doug is not arriving here, so the booth tag is not needed. Keep "717 TO 660 MILLION YEARS AGO".
32. **s102:** the ghost Doug (700,480) touches the "1,200 YEARS" label.
    - **Fix:** move the ghost to y 560.
33. **s104, s105, s106:** Doug (1700,900) straddles the `pnw_map` frame line, with his head inside the frame and his legs outside.
    - **Fix:** use the map at 1.1 at x 880, so the right frame edge is about 1650, and Doug at (1790,700) facing left, fully outside the frame.
34. **s150:** the sun (1500,330) is painted over the beech canopy.
    - **Fix:** move the sun to (1050,140) in clear sky.

### F. Blocking: layout variety
35. **s238-s244:** the same pond composition appears **7 times in a row**: the same ellipse, camera and Doug size. The ticking date labels in s240 help, but this breaks the "not the same composition 5 times in a row" rule.
    - **Fix:** recompose at least two of the shots. For example:
      - s243 as a close-up: Doug and the algae at about 1.4x, with the three labels in a row across the top;
      - s241 as a wide pull-back: the pond small in a white world, with the booth.

### Recommended (non-blocking; fix if you are in the shot anyway)
- **s057, s147, s245:** the red title text straddles two ground colours, which the bible's rule against crossing land masses covers. It is still legible because of the black outline.
  - s057: move the title up into the sky at (1200,420).
  - s147: use size 100 at x 1290 so it sits fully on the green.
  - s245: leave it as is.
- **s245:** change "2,400,000,000 YEARS AGO" to "2.4 BILLION YEARS AGO" to match s246 and read faster.
- **s034-s039:** six near-identical ice, booths and bridge frames. Consider making s038 a close-up on the press.
- **s250:** "METHANE" nearly touches the chapter bar. Lower it to y 120.
- **s264:** "WHO DID IT" sits right on Doug's cap. Raise it to y 100.
- **s013:** the "MOUNT TAMBORA" label sits on the smoke puff. Move it to y 60.
- **s274:** the thumbs-up hand lands on the booth's red door handle and reads muddy. Shift Doug to x -30.

### Re-check plan
After the director's pass, I re-render every shot listed above plus s057 and s245 with `python -m studio keyframes 007-every-time-earth-froze --shots ...` and review them as round 2.
