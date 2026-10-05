# Asset requests: 007 Every Time Earth Froze

Director, 2026-10-05. There are 30 new drawings. House style is in `assets/library/anglerfish.json`: detailed-tier creatures and places, 4-6 px outlines, flat fills, no faces on non-human things. Unless a request says otherwise, everything faces **right**.
**Anchors and sizes are load-bearing.** The shotlist already places these assets by the numbers below (generator: `episodes/007-.../build/gen_shotlist.py`), so please match them exactly. If you have to change a number, tell the director.

Reused from the library, no work needed: `time_machine`, `ice_block`, `doug_cap`, `sunscreen`, `world_map`, `usa_map`, `volcano`, `house`, `library_book`, `calendar`, `fishing_boat`, `apartment_block`, `campfire`, `heart_icon`, `scientist`, `fishing_rod`, `iceberg`, `fingertip`, `research_hut`, `sticker_antarctica`, `doug_sunglasses`, `empire_state_building`, `pangaea_map`, `gondwana`, `magnifying_glass`, `fern`, `t_rex`, `asteroid`, `angry_sun`, `black_smoker`, `microbe`, `petri_dish`, `small_plant`, `cat`, `kitchen_timer`, `gravestone`, plus the annotation set.

---

## Props (Year Without a Summer, Frost Fairs)

### `deck_chair`
- **What:** an unfolded seaside deck chair. Doug sits in it in the June 1816 snow.
- **Look:** a pale wooden frame (`#c89a5a`) with a slung canvas seat in **red/white vertical stripes** (`#e0201b` / `#ffffff`). The canvas sags. The back leans back to the LEFT.
- **Geometry:** side view. **Anchor: bottom-centre, with the feet on the ground.** The seat surface (where Doug's hip rests) is at **y = -50**, from x -60 to +120. The back rest rises from (-60, -50) up-left to about (-150, -300). Total size about 330 x 330.
- **Shots:** s025, s026, s027. Doug is drawn after it with `sit` at the chair's x + 10.
- **DONE (deck_chair):** `assets/library/deck_chair.json`. Preview: `assets/previews/007-every-time-earth-froze-assets.png` (also `007-props.png`, `007-maps.png`, `007-nature.png`, `007-doug-test.png`). Checked with Doug sit at chair x+10 / y-108 at scale 0.85: his hip sits on the canvas.

### `deck_chair_folded`
- **What:** the same deck chair folded flat and carried under Doug's arm.
- **Look:** the same wood and striped canvas, folded into a long flat bundle with the stripes still visible.
- **Geometry:** **anchor: centre** (the grip). About 140 x 460, long axis vertical. It is shown rotated -10.
- **Shots:** s002, s003, s006, s007, s022, s024.
- **DONE (deck_chair_folded):** `assets/library/deck_chair_folded.json`. Preview: `assets/previews/007-every-time-earth-froze-assets.png` (also `007-props.png`, `007-maps.png`, `007-nature.png`, `007-doug-test.png`).

### `red_barn`
- **What:** a New England farm barn in June 1816.
- **Look:** red board walls (`#b0302a`), a white X-braced double door, white trim, a grey gambrel roof and a small hayloft window.
- **Geometry:** **anchor: bottom-centre.** About 500 x 420. Snow gets sprayed over the roof in some shots, so keep the roof shape simple.
- **Shots:** s006, s007, s011.
- **DONE (red_barn):** `assets/library/red_barn.json`. Preview: `assets/previews/007-every-time-earth-froze-assets.png` (also `007-props.png`, `007-maps.png`, `007-nature.png`, `007-doug-test.png`).

### `kitchen_chair`
- **What:** a plain kitchen chair, used as the scale reference for 18 inches of snow.
- **Look:** a wooden chair (`#a0522d`), side view, with four legs, a flat seat and a slatted back.
- **Geometry:** **anchor: bottom-centre.** The **top of the seat is at y = -195 exactly.** The back rises to about y = -420. About 220 wide.
- **Shots:** s010, at scale 0.62. The seat must line up with the snow surface line.
- **DONE (kitchen_chair):** `assets/library/kitchen_chair.json`. Preview: `assets/previews/007-every-time-earth-froze-assets.png` (also `007-props.png`, `007-maps.png`, `007-nature.png`, `007-doug-test.png`).

### `old_london_bridge`
- **What:** Old London Bridge, before 1831.
- **Look:** a long stone bridge (`#a59a8c`, with darker `#7d7468` shading) standing on **19 small, closely spaced arches**. Each arch has a pointed starling (boat-shaped pier base) at the waterline. A crude row of small timber houses with brown roofs runs along the deck.
- **Geometry:** front view. **Anchor: bottom-centre, at the waterline** (the pier feet are at y = 0). The deck is at about y = -150 and the house tops at about y = -260. About **760 wide** (x -380..+380). The arches must stay visibly distinct at scale 0.7.
- **Shots:** s029-s031, s034-s039, s041-s046, s049-s051. It is used at scale 0.7-0.8 and in close-up at scale 2.0 (s044, s045, s046).
- **DONE (old_london_bridge):** `assets/library/old_london_bridge.json`. Preview: `assets/previews/007-every-time-earth-froze-assets.png` (also `007-props.png`, `007-maps.png`, `007-nature.png`, `007-doug-test.png`). 19 round-headed arches on piers every 40 units; the abutments make it 768 wide (x -384..+384).

### `fair_booth`
- **What:** a frost fair stall on the frozen Thames.
- **Look:** a wooden stall frame with a peaked canvas tent roof in **blue/cream or red/cream stripes**, a small pennant on top, a counter board and a crude hanging sign with no text.
- **Geometry:** **anchor: bottom-centre, on the ice.** About 300 x 360.
- **Shots:** s034-s039, s041, s049-s051.
- **DONE (fair_booth):** `assets/library/fair_booth.json`. Preview: `assets/previews/007-every-time-earth-froze-assets.png` (also `007-props.png`, `007-maps.png`, `007-nature.png`, `007-doug-test.png`). One variant: blue/cream stripes.

### `printing_press`
- **What:** a 1680s wooden hand printing press set up on the ice.
- **Look:** a dark wood frame (`#6b4423`) with two uprights and a crossbeam. A big screw in the middle has a long side bar handle. Below are a flat bed (platen) and a stack of paper.
- **Geometry:** **anchor: bottom-centre.** About 300 x 380.
- **Shots:** s037, s038, s039, s050, s051.
- **DONE (printing_press):** `assets/library/printing_press.json`. Preview: `assets/previews/007-every-time-earth-froze-assets.png` (also `007-props.png`, `007-maps.png`, `007-nature.png`, `007-doug-test.png`).

### `printed_card`
- **What:** the souvenir card "printed on the Thames". It is the episode's visual kicker.
- **Look:** a cream card (`#f6ecd2`) with an ornate black and red printed border, small corner flourishes and a slight curl at one corner.
- **Geometry:** **anchor: centre.** About 420 x 280. **Leave the centre (x -170..+170, y -90..+60) completely blank.** The shotlist overlays text such as "DOUG," and "PRINTED ON THE THAMES" there.
- **Shots:** s039, s040, s050-s055. Sizes range from scale 0.25 (in Doug's hand) to 1.6 (close-up).
- **DONE (printed_card):** `assets/library/printed_card.json`. Preview: `assets/previews/007-every-time-earth-froze-assets.png` (also `007-props.png`, `007-maps.png`, `007-nature.png`, `007-doug-test.png`).

### `elephant`
- **What:** the elephant led across the frozen Thames in 1814.
- **Look:** an Asian elephant in grey (`#8a8a8a`) with darker shading on the belly. It has small ears, a curled trunk and a calm, plodding pose. It wears a small red harness blanket.
- **Geometry:** side view facing right. **Anchor: bottom-centre, with the feet on the ice.** About 520 x 400.
- **Shots:** s043.
- **DONE (elephant):** `assets/library/elephant.json`. Preview: `assets/previews/007-every-time-earth-froze-assets.png` (also `007-props.png`, `007-maps.png`, `007-nature.png`, `007-doug-test.png`).

## Maps (Doggerland, Missoula, Last Glacial Maximum, First Snowball)

All maps follow the `world_map` style: flat green land `#6cbf5a` with a dark green outline, light-blue sea `#bfe6ff`, a black frame and **no labels** (the shotlist adds them). **Each map uses the projection given below**, because the shotlist computes label, arrow and lake positions from it.

### `north_sea_today`, `doggerland_map`, `doggerland_islands`, `doggerland_island` (one shared frame)
- **Frame:** 1190 x 900, anchor centre, black frame. The projection is equirectangular: **x = (lon - 3) x 66, y = -(lat - 57) x 64**. It covers lon -6..12 and lat 50..64 (Britain on the left, Norway top right, the Netherlands, Belgium and Denmark at the bottom and right).
- `north_sea_today`: modern coastlines with the North Sea open.
- `doggerland_map`: the ice-age version. The whole southern North Sea is **dry green land** joining Britain to the continent, from about 51N up to about 56.5N. Add a few light-blue river lines and darker marsh dots. Open sea stays north of about 56.5N and along the Norwegian Trench.
- `doggerland_islands`: the same frame with the sea back in. Only **3-5 low islands** remain, around the Dogger Bank (lon 0.5..5, lat 54..55.8).
- `doggerland_island`: **one island** at about lon 1.5..4, lat 54.3..55.2. Everything else is sea.
- **Must stay inside the frame:** the Norwegian coast near the Storegga slide at about (lon 5.5, lat 62.6), which is local (165, -358). The shotlist draws tsunami arcs from that point.
- **Shots:** `north_sea_today` s058. `doggerland_map` s059, s062, s063, s134. `doggerland_islands` s063, s064. `doggerland_island` s064, s065, s068, s072, s073. All are placed at (960, 560), scale 0.95, and overlaid on each other in s063 and s064, so **the frame must be identical across the four**.
- **DONE (north_sea_today):** `assets/library/north_sea_today.json`. Preview: `assets/previews/007-every-time-earth-froze-assets.png` (also `007-props.png`, `007-maps.png`, `007-nature.png`, `007-doug-test.png`).
- **DONE (doggerland_map):** `assets/library/doggerland_map.json`. Preview: `assets/previews/007-every-time-earth-froze-assets.png` (also `007-props.png`, `007-maps.png`, `007-nature.png`, `007-doug-test.png`).
- **DONE (doggerland_islands):** `assets/library/doggerland_islands.json`. Preview: `assets/previews/007-every-time-earth-froze-assets.png` (also `007-props.png`, `007-maps.png`, `007-nature.png`, `007-doug-test.png`).
- **DONE (doggerland_island):** `assets/library/doggerland_island.json`. Preview: `assets/previews/007-every-time-earth-froze-assets.png` (also `007-props.png`, `007-maps.png`, `007-nature.png`, `007-doug-test.png`).

### `pnw_map`
- **What:** the Pacific Northwest, used for the Missoula Floods.
- **Projection:** **x = (lon + 117) x 100, y = -(lat - 47) x 100.** It covers lon -124..-110 and lat 44.5..49.8, so the frame is about 1400 x 530. **Anchor: centre.**
- **Content:** the Pacific in the blue sea colour west of the coast (about lon -124). Land is green. The Canada border at lat 49 (y = -200) is a dashed dark line. Faint state lines separate Washington, Oregon, Idaho and Montana. The Columbia River is a blue line running to the coast at about (-124, 46.2). The Clark Fork river valley in Idaho and Montana is a thin blue line through Lake Pend Oreille at (-116.4, 48.1), which is local (60, -110).
- **Do not draw** ice, the lake or flood channels. The shotlist adds those as overlays.
- **Shots:** s104, s105, s106, placed at (960, 560), scale 1.2.
- **DONE (pnw_map):** `assets/library/pnw_map.json`. Preview: `assets/previews/007-every-time-earth-froze-assets.png` (also `007-props.png`, `007-maps.png`, `007-nature.png`, `007-doug-test.png`).

### `north_america_map` and `north_america_ice_map`
- **Projection (both):** **x = (lon + 110) x 12, y = -(lat - 45) x 12.** It covers lon -170..-50 and lat 10..80, so the frame is 1440 x 840. **Anchor: centre.** The frame must be identical for both maps.
- **Content:** Alaska, Canada with Hudson Bay (centre about local (300, -180)), the Canadian Arctic islands, the edge of Greenland at the top right, the contiguous US, Mexico and Cuba. The Great Lakes are drawn in blue: Lake Huron is at about local (331, 2) and Lake Michigan's south tip (Chicago) at about local (269, 37). The Mississippi is a thin blue line to its mouth at about local (250, 186). The Gulf of St Lawrence is at about local (576, -36).
- `north_america_ice_map`: the same map at the Last Glacial Maximum. The **Laurentide and Cordilleran ice sheets** are white `#ffffff` with a pale-blue `#6a9cc0` outline and a little `#d4e6f2` shading. They cover all of Canada including Hudson Bay, Alaska's southern coast range and the Great Lakes. The southern edge dips to about **40N in the Midwest**, so Chicago is under ice. The ice edge should be wavy and lobed.
- **Shots:** `north_america_ice_map` s088, s127, s129, s130 (s130 zooms 1.1x on Chicago). `north_america_map` s138, s258 (s258 zooms on Lake Huron). Both are placed at (900, 540), scale 1.0.
- **DONE (north_america_map):** `assets/library/north_america_map.json`. Preview: `assets/previews/007-every-time-earth-froze-assets.png` (also `007-props.png`, `007-maps.png`, `007-nature.png`, `007-doug-test.png`).
- **DONE (north_america_ice_map):** `assets/library/north_america_ice_map.json`. Preview: `assets/previews/007-every-time-earth-froze-assets.png` (also `007-props.png`, `007-maps.png`, `007-nature.png`, `007-doug-test.png`).

### `antarctica_map`
- **What:** top-down Antarctica.
- **Look:** a white ice continent with pale-blue `#d4e6f2` shading toward the coasts and a dark outline. The Antarctic Peninsula points toward the upper left, and the Ross and Weddell ice shelves are slightly bluer. **No ocean fill:** the background shows through.
- **Geometry:** **anchor: centre.** About 900 x 800.
- **Shots:** s148 (with a red X over it), s158 (with a dashed circumpolar current around it).
- **DONE (antarctica_map):** `assets/library/antarctica_map.json`. Preview: `assets/previews/007-every-time-earth-froze-assets.png` (also `007-props.png`, `007-maps.png`, `007-nature.png`, `007-doug-test.png`). About 900x750 (x -450..450, y -375..375).

## Living things and places

### `dryas_flower`
- **What:** mountain avens, *Dryas octopetala*, the Younger Dryas namesake. It is Doug's friend in item 4.
- **Look:** **8 white rounded petals** around a **yellow centre** with stamens, on a short stem. Small, dark green, crinkly oak-like leaves with toothed edges sit at the base. No face.
- **Geometry:** **anchor: bottom-centre** (the stem base on the ground). About 160 wide x 220 tall. It must read clearly at scale 0.6.
- **Shots:** s085, s086, s098-s102, s269. It is shown slightly rotated (±6) in s100 and s101 for the happy-sway beat.
- **DONE (dryas_flower):** `assets/library/dryas_flower.json`. Preview: `assets/previews/007-every-time-earth-froze-assets.png` (also `007-props.png`, `007-maps.png`, `007-nature.png`, `007-doug-test.png`).

### `cn_tower`
- **What:** Toronto's CN Tower, the scale reference for the 610 m deep Lake Missoula.
- **Look:** a slim grey concrete shaft tapering upward, a pod with a darker window band about 2/3 of the way up, a small upper pod and a thin red-and-white antenna spire.
- **Geometry:** **anchor: bottom-centre. Exactly 600 tall** (y -600..0) and about 110 wide at the base.
- **Shots:** s108, at scale 0.68.
- **DONE (cn_tower):** `assets/library/cn_tower.json`. Preview: `assets/previews/007-every-time-earth-froze-assets.png` (also `007-props.png`, `007-maps.png`, `007-nature.png`, `007-doug-test.png`).

### `eiffel_tower`
- **What:** the Eiffel Tower, stacked 9 high to show 3 km of ice.
- **Look:** a brown-bronze iron lattice (`#8a5a3a`) with an open arch between the four legs, two platforms and a spire.
- **Geometry:** **anchor: bottom-centre. Exactly 512 tall** (spire tip at y = -512) and about 300 wide at the base, so copies stack end to end like `empire_state_building`. It is used at scale 0.155, so keep the lattice crude and bold so it doesn't turn to mush.
- **Shots:** s132.
- **DONE (eiffel_tower):** `assets/library/eiffel_tower.json`. Preview: `assets/previews/007-every-time-earth-froze-assets.png` (also `007-props.png`, `007-maps.png`, `007-nature.png`, `007-doug-test.png`).

### `puffy_parka` (worn prop, Doug's tier rules apply)
- **What:** Doug's huge puffy winter parka for the Last Glacial Maximum flag beat and the Marinoan Snowball.
- **Look:** a bright orange `#ff8a1f` quilted puffer body with horizontal puff bands and darker `#d06a10` seams, a white fur-trimmed collar ring at the neck and a zip line. **No sleeves and no hood.** Doug's own arm lines stay visible so the prop works with every pose (point, hands_hips, panic1/2). **It must leave Doug's head, face and red cap completely clear.**
- **Geometry:** **anchor = Doug's hip (0, 0) at Doug scale 1.** The neck is at (0, -150) and the collar sits just below it. The body runs from y -150 to about +15 and is about 170 wide (x -85..+85), with puffy shoulder caps.
- **Shots:** s142, s143, s217, s218, at the same x, y and scale as Doug.
- **DONE (puffy_parka):** `assets/library/puffy_parka.json`. Preview: `assets/previews/007-every-time-earth-froze-assets.png` (also `007-props.png`, `007-maps.png`, `007-nature.png`, `007-doug-test.png`). Collar ring y about -147..-124 (clear of the head); checked on stand, point, panic1 and hands_hips.

### `puffy_parka_flat`
- **What:** the same parka on Doug lying dead on his back after the greenhouse thaw.
- **Geometry:** follow the `ammonite_costume_flat` convention. It is drawn in the upright frame and placed with **rotate -90 at Doug's x + 30 x scale**, the same y and the same scale, listed after the `on_back` Doug. Draw it slightly squashed and sweaty, with 2-3 small sweat drops.
- **Shots:** s219, s220 (Doug x 700, y 762, scale 0.85; parka at x 725).
- **DONE (puffy_parka_flat):** `assets/library/puffy_parka_flat.json`. Preview: `assets/previews/007-every-time-earth-froze-assets.png` (also `007-props.png`, `007-maps.png`, `007-nature.png`, `007-doug-test.png`). Checked at the s219 numbers (Doug 700/762/0.85 on_back, parka 725/763 rotate -90): sweat drops face the sky.

### `palm_tree`
- **What:** a palm tree on the Eocene Antarctic coast, and on the Costa Rica beach in s202.
- **Look:** a curved trunk with ring segments (`#a0522d` / `#7a3e1e`), a crown of 6-7 drooping green fronds (`#2e8b3a` with lighter `#4caf50` leaflets) and a couple of brown coconuts.
- **Geometry:** **anchor: bottom-centre.** About 350 x 700, with the trunk leaning slightly right.
- **Shots:** s147, s149, s150, s202.
- **DONE (palm_tree):** `assets/library/palm_tree.json`. Preview: `assets/previews/007-every-time-earth-froze-assets.png` (also `007-props.png`, `007-maps.png`, `007-nature.png`, `007-doug-test.png`).

### `beech_tree`
- **What:** a southern beech (*Nothofagus*) tree on the warm Eocene Antarctic hills.
- **Look:** a broad, rounded, layered canopy of small dark-green leaves (`#3f7a35`, with `#5e9c48` highlights in clumps), a grey-brown trunk and spreading branches.
- **Geometry:** **anchor: bottom-centre.** About 450 x 650.
- **Shots:** s147, s149-s152, s159, s168, s169.
- **DONE (beech_tree):** `assets/library/beech_tree.json`. Preview: `assets/previews/007-every-time-earth-froze-assets.png` (also `007-props.png`, `007-maps.png`, `007-nature.png`, `007-doug-test.png`).

### `picnic_blanket`
- **What:** Doug's picnic under the beech trees.
- **Look:** a red/white gingham blanket in a low 3/4 view, flat on the grass. Two triangle sandwiches and a green metal flask sit at the right end.
- **Geometry:** **anchor: centre of the blanket surface.** About 520 x 140. Doug sits on it at local (0, -40) (sit pose).
- **Shots:** s168, s169.
- **DONE (picnic_blanket):** `assets/library/picnic_blanket.json`. Preview: `assets/previews/007-every-time-earth-froze-assets.png` (also `007-props.png`, `007-maps.png`, `007-nature.png`, `007-doug-test.png`).

### `meganeura`
- **What:** the giant Carboniferous griffinfly, Doug's friend in item 8.
- **Look:** a long segmented abdomen in metallic blue-green (`#2a7f8a`, with darker `#1b5560` bands), big dark compound eyes and **two pairs of long clear wings** (pale `#e8f6ff` fill with dark vein lines). It is a dragonfly silhouette, not a bee. No face.
- **Geometry:** **anchor: centre** (the thorax). The **wingspan is 500** (x -250..+250) and the body is about 420 long. Side and top view as for a pinned dragonfly, facing right.
- **Shots:** s181 (as a silhouette, `glow_r` 0, plus a body spray), s182 (scale 1.2, with a dotted wingspan line from x -250 to +250), s183, s192, s193, s194 (flipped), s269.
- **DONE (meganeura):** `assets/library/meganeura.json`. Preview: `assets/previews/007-every-time-earth-froze-assets.png` (also `007-props.png`, `007-maps.png`, `007-nature.png`, `007-doug-test.png`). Drawn top-down like a pinned dragonfly, wings spread horizontally (tips x about -250..+258), body tilted 22 degrees so the head points up-right; `flip` makes it fly up-left (s194). Abdomen runs down-left to about (-120, 320), so the s182 dotted line at local y +117 crosses the abdomen, under the wings.

### `front_door`
- **What:** an ordinary front door, the scale reference (the 70 cm wingspan is almost as wide as the door).
- **Look:** a red-brown panelled wooden door in its white frame, with a brass knob, a small window and a doormat line at the bottom.
- **Geometry:** **anchor: bottom-centre.** About 300 x 640.
- **Shots:** s183, at scale 1.1 beside the Meganeura at scale 0.6.
- **DONE (front_door):** `assets/library/front_door.json`. Preview: `assets/previews/007-every-time-earth-froze-assets.png` (also `007-props.png`, `007-maps.png`, `007-nature.png`, `007-doug-test.png`).

### `scale_tree`
- **What:** a Carboniferous swamp scale tree (*Lepidodendron*).
- **Look:** a tall straight trunk (`#6b5a3a`) covered in a **diamond leaf-scar pattern**. At the top, a few forked branches end in tufts of grassy green leaves (`#4f8a3a`). The base has spreading root lobes.
- **Geometry:** **anchor: bottom-centre.** About 300 x 780. It is also used rotated 80-85 as a fallen trunk.
- **Shots:** s172, s179-s187, s192, s195.
- **DONE (scale_tree):** `assets/library/scale_tree.json`. Preview: `assets/previews/007-every-time-earth-froze-assets.png` (also `007-props.png`, `007-maps.png`, `007-nature.png`, `007-doug-test.png`). Crown tufts reach about y -800.

### `stromatolites`
- **What:** cyanobacterial mounds in the shallows, 2.4 billion years ago.
- **Look:** a cluster of 4-5 domed, cabbage-like rock mounds in brown-grey (`#8a7a6a`) with visible **thin wavy stacked layers**. A green-blue film (`#3faa7a`) covers the tops, with a few tiny bubbles above.
- **Geometry:** **anchor: bottom-centre.** About 600 x 260.
- **Shots:** s245, s247, s248, s251-s253, s257, s264, s266, s270-s272.
- **DONE (stromatolites):** `assets/library/stromatolites.json`. Preview: `assets/previews/007-every-time-earth-froze-assets.png` (also `007-props.png`, `007-maps.png`, `007-nature.png`, `007-doug-test.png`).

### `algae_patch`
- **What:** Doug's algae friend in the Sturtian meltwater pond.
- **Look:** a bright green (`#3faa4a`) clump of filamentous algae with lighter `#9be07a` strands and a few small bubbles. It should look friendly but have **no face**.
- **Geometry:** **anchor: centre.** About 260 x 160.
- **Shots:** s239-s244, s267 (scale 1.6), s269.
- **DONE (algae_patch):** `assets/library/algae_patch.json`. Preview: `assets/previews/007-every-time-earth-froze-assets.png` (also `007-props.png`, `007-maps.png`, `007-nature.png`, `007-doug-test.png`).
