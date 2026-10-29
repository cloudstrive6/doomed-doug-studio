# 031-polar-bear-on-purpose: asset requests (director)

House style: detailed tier for creatures, places and props (dark outlines, flat fills, interior shading), crude tier only for the sprinter. Facing right unless noted. Sizes are local units at scale 1; the shotlist is laid out against these extents and anchors, so please keep them. **Priority:** `paw_print_icon` (every shot, it sits in the BEAR readout), then `ringed_seal`, `polar_bear_thin`, `holding_cell` + `cell_bars`, `bearded_seal`, `polar_bear_running`, `arctic_town_block`.
CD notes (brief 7, decisions.md): every bear predatory and heavy, never cute or plush; **no cubs anywhere**; no claws in Doug, no blood on snow, no seal kills drawn (seals escape or stay off-screen); no real people (the sprinter is generic); the map has no text. A placeholder preview of the layout is in `episodes/031-polar-bear-on-purpose/build/preview/` (pink boxes = these requests).

Reused from the library (no request): `basketball`, `bathroom_scale`, `big_water_bottle`, `binoculars`, `bucket`, `bush_plane`, `calendar`, `campfire`, `clipboard`, `dinner_plate`, `doug_cap`, `empire_state_building`, `exclamation_mark`, `field_guide_open`, `fossil_bone`, `front_door`, `grass_tuft`, `helicopter`, `house`, `journal_paper`, `kitchen_timer`, `loudspeaker`, `magnifying_glass`, `narrator_hand`, `picnic_basket`, `placard`, `plastic_bag`, `podium`, `polar_bear`, `polar_bear_lying`, `polar_bear_standing`, `printed_card`, `question_mark`, `red_x`, `research_hut`, `rosette_badge`, `ruler`, `scientist`, `seal_costume`, `signboard`, `songbird`, `speedometer`, `stew_bowl`, `tape_measure`, `tent`, `thermometer`, `tin_can`, `wait_stopwatch`, `warning_triangle`, `water_splash`, `water_splash_small`, `wildlife_official`.

## `arctic_map`
**Map (episode locations).**

- Look: Simple MS Paint map card of the Arctic, polar-ish view: pale-blue `#bfe6ff` Arctic Ocean, land in pale grey-tan `#d9d2b8` (not green, so labels and dots read), black outline, black frame. Must show Alaska (left), Hudson Bay (lower left), Greenland (centre), Svalbard (islands right of centre) and Novaya Zemlya (long double island, right). No text.
- Facing / anchor / size: Centre anchor, 1400 x 800 (x -700..700, y -400..400). **Put these exactly at these local points** (the shot draws red dots there): Churchill on the west shore of Hudson Bay (-430,+170); Hudson Bay water centre (-380,+110); Svalbard (+170,-150); Novaya Zemlya, middle of the west coast (+400,-30).
- Notes: Used at 0.75 (centred 960,580) and 0.35-0.5 as an inset.
- Shots: s060, s133, s134, s139, s160, s205 (6 shots)

## `arctic_town_block`
**Place (The Town).**

- Look: A plain two-storey Arctic apartment block on short piles: faded pale blue-grey `#c9d3dc` walls, small square windows (a few lit yellow), snow on the flat roof, an entrance door to the stairwell at the left (lit doorway). No signs, no text, no flags.
- Facing / anchor / size: Bottom-centre anchor: x -400..400, y -360..0; stairwell door at local x -295..-205, y -170..0.
- Notes: Two copies (one flipped) on a dusk street `#3b4a6b`. Keep the walls light so Doug and the bears read in front.
- Shots: s130, s131, s132, s135, s136, s137, s138, s140, s149 (9 shots)

## `bearded_seal`
**Creature (The Swim, the three seals on the floe edge).**

- Look: Bearded seal lying on ice, facing right: long heavy grey-brown `#8a7a6a` body, small head, and a big bushy white moustache of whiskers (its defining feature), square front flippers. Calm, not cute.
- Facing / anchor / size: Facing right. Bottom-centre anchor (belly on y=0): about 480 x 180 (x -240..240, y -180..0).
- Notes: Three of them at 0.33-0.4 on the floe edge.
- Shots: s082, s083, s084, s085, s086, s087, s088, s090 (8 shots)

## `berry_bowl`
**Prop (Doug's offering, death 252 aftermath).**

- Look: A small wooden bowl heaped with dark blue berries. The cap rests on the berries in the aftermath shots.
- Facing / anchor / size: Centre anchor: about 180 x 90 (x -90..90, y -45..45); top of the berry heap at (0,-45).
- Notes: Held at Doug's front hand in the `crouch` pose, then on the ground with `doug_cap`.
- Shots: s197, s198, s199, s200, s201, s202 (6 shots)

## `berry_bush`
**Plant (The Thin Bear).**

- Look: Low autumn tundra berry shrub (crowberry/blueberry): woody red-brown stems, small leaves turning red and orange, clusters of dark blue-black berries. Not green-dominant (it sits on brown tundra).
- Facing / anchor / size: Bottom-centre anchor: about 300 x 160 (x -150..150, y -160..0).
- Shots: s178, s179, s180, s183, s185 (5 shots)

## `caribou_antler`
**Prop (Pagano 2024 diet list).**

- Look: A single shed caribou antler: pale bone-brown `#d9c49a`, long curved main beam with a few tines and the flattened palm-shaped brow tine at the base. No skull.
- Facing / anchor / size: Centre anchor: about 300 x 260.
- Shots: s183 (1 shot)

## `cell_bars`
**Overlay for `holding_cell` (front grille).**

- Look: A heavy steel cell door frame with vertical bars every 60 units (dark grey `#3a3f46`, 8-10 units thick) and one horizontal bar, **transparent between the bars**, plus a small blank metal tag plate at the top centre (0,-500), about 170 x 50, for overlaid text ("NO FOOD", "DETAINED").
- Facing / anchor / size: Same anchor and bbox as `holding_cell`.
- Notes: Always drawn after the cell contents.
- Shots: s142, s145, s147, s148, s152, s153, s154, s155, s228, s229, s230, s231 (12 shots)

## `holding_cell`
**Place (holding facility cell, back layer).**

- Look: Front view into one concrete cell: grey `#a3a8ae` back wall with a small high vent, side walls in perspective, grey floor strip (y -120..0). Empty: the contents (bear, Doug, bowl, cap) are drawn by the shot, then `cell_bars` on top.
- Facing / anchor / size: Bottom-centre anchor: 600 x 560 (x -300..300, y -560..0).
- Notes: Rows of three at scale 1.0 and one at 1.2 (closing image).
- Shots: s142, s145, s147, s148, s152, s153, s154, s155, s228, s229, s230, s231 (12 shots)

## `holding_facility`
**Place (Churchill polar bear holding facility, exterior).**

- Look: Long low grey corrugated-metal building (quonset/hangar shape) with a few vents, a roller door, snow drifts at the base, and a blank cream sign board on the front.
- Facing / anchor / size: Bottom-centre anchor: x -600..600, y -320..0. **Sign board blank**, centred at (0,-250), clear area 520 x 70 (the shot writes POLAR BEAR HOLDING FACILITY on it).
- Shots: s141 (1 shot)

## `paw_print_icon`
**Episode device (BEAR readout icon, also used for footprint tracks).**

- Look: A single black `#1a1a1a` polar bear paw print: one wide bean-shaped palm pad and five small oval toe pads in an arc above it, tiny claw dots above the toes. Flat fill, no outline colour change. Must read at 30 px (scale 0.3) next to the readout label.
- Facing / anchor / size: Centre anchor, 100 x 100 (x -50..50, y -50..50). Toes point up.
- Notes: Replaces 013's ruler icon so the readout does not look like DISTANCE TO HIPPO (brief section 2). Used at 0.3 beside the counter on every shot, and at 0.45-0.6 as footprint tracks.
- Shots: s003, s004, s005, s006, s007, s008, s009, s010, s011, s012, s013, s014, s015, s016, s017, s018, s019, s020, s021, s022, s023, s024, s025, s026, s027, s028, s029, s030, s031, s032, s033, s034, s035, s036, s037, s038, s039, s040, s041, s042, s043, s044, s045, s046, s047, s048, s049, s050, s051, s052, s053, s054, s055, s056, s057, s058, s059, s060, s061, s062, s063, s064, s065, s066, s067, s068, s069, s070, s071, s072, s073, s074, s075, s076, s077, s078, s079, s080, s081, s082, s083, s084, s085, s086, s087, s088, s089, s090, s091, s092, s093, s094, s095, s096, s097, s098, s099, s100, s101, s102, s103, s104, s105, s106, s107, s108, s109, s110, s111, s112, s113, s114, s115, s116, s117, s118, s119, s120, s121, s122, s123, s124, s125, s126, s127, s128, s129, s130, s131, s132, s133, s134, s135, s136, s137, s138, s139, s140, s141, s142, s143, s144, s145, s146, s147, s148, s149, s150, s151, s152, s153, s154, s155, s156, s157, s158, s159, s160, s161, s162, s163, s164, s165, s166, s167, s168, s169, s170, s171, s172, s173, s174, s175, s176, s177, s178, s179, s180, s181, s182, s183, s184, s185, s186, s187, s188, s189, s190, s191, s192, s193, s194, s195, s196, s197, s198, s199, s200, s201, s202, s203, s204, s213, s214, s215, s216, s217, s218, s219, s220, s221, s222, s223, s224, s225, s226, s227, s228, s229, s230, s231 (221 shots)

## `polar_bear_black_skin`
**Creature diagram (The Fur: the skin under the fur).**

- Look: Exactly the `polar_bear` silhouette and pose, but with the fur removed: the whole body solid charcoal-black skin `#2a2a2e` with a slightly lighter `#4a4a52` shading, a thin dashed pale-grey line just outside the body where the fur outline was, black nose, small dark eye with a tiny white highlight so the head reads. Diagram look, not gory, no muscles or anatomy.
- Facing / anchor / size: Facing right. Same anchor and bbox as `polar_bear` (x -302..320, y -345..0) so the two sit side by side at the same scale.
- Notes: Split-panel beside `polar_bear` at 0.85.
- Shots: s030, s031 (2 shots)

## `polar_bear_lunge`
**Creature (bursting out of the water onto the floe).**

- Look: Same design family as `polar_bear` / `polar_bear_standing` (creamy-white `#f4f1e4` coat, grey-blue `#c9d6e2` shading underneath and on the far legs, thick dark outline, long neck, small low head, black nose, small dark eye, heavy hindquarters). **Predatory, never cute:** no big eyes, no smile, no blush, no rounded plush look (brief 7, kid appeal HIGH). Exploding up out of the water onto an ice edge: forequarters and head up and forward, front paws reaching onto the ice, mouth slightly open (no fangs needed), water streaming off the fur in pale-blue drips; hindquarters still in the water below.
- Facing / anchor / size: Facing right. Anchor (0,0) = the ice-edge corner where its chest meets the floe: forequarters above and right of it (x 0..+300, y -420..0), hind body and legs below the waterline to the left (x -320..0, y 0..+140; draw that part a little bluer as submerged).
- Notes: Used flipped at a floe edge with a `water_splash` in front.
- Shots: s092, s101, s221 (3 shots)

## `polar_bear_paw`
**Creature close-up (The Charge).**

- Look: One huge front paw seen from above, pressed flat on ice: thick creamy-white fur on top, the toes spread, five **thick, dark, curved claws** pointing forward (right), and the rough black pads showing at the front edge with a few texture dots. No blood, no prey.
- Facing / anchor / size: Claws toward the right. Centre anchor: **460 wide** (x -230..230, y -170..170), so at the same scale it is exactly as wide as the library `ruler` (30 cm). That is the fact being shown (Parks Canada: up to 30 cm).
- Notes: Used at 1.4 next to `ruler` at 1.4.
- Shots: s116, s117, s118, s119, s120 (5 shots)

## `polar_bear_rearing`
**Creature (item 1 roof slam, tent death, boss).**

- Look: Same design family as `polar_bear` / `polar_bear_standing` (creamy-white `#f4f1e4` coat, grey-blue `#c9d6e2` shading underneath and on the far legs, thick dark outline, long neck, small low head, black nose, small dark eye, heavy hindquarters). **Predatory, never cute:** no big eyes, no smile, no blush, no rounded plush look (brief 7, kid appeal HIGH). Reared up on its hind legs, body tilted forward about 20 degrees, both forelegs raised high and forward with the big front paws turned down ready to slam (the roof-breaking pounce). Mouth closed or slightly open, no teeth, no claws in anything.
- Facing / anchor / size: Facing right. Bottom-centre anchor at the hind feet: about 560 x 700 (x -260..300, y -700..0); front paws around (+200,-620).
- Notes: Used at 0.5-0.75, flipped, beside the snow lair and over Doug's snow shelter.
- Shots: s007, s012, s013, s026, s174 (5 shots)

## `polar_bear_running`
**Creature (the charge).**

- Look: Same design family as `polar_bear` / `polar_bear_standing` (creamy-white `#f4f1e4` coat, grey-blue `#c9d6e2` shading underneath and on the far legs, thick dark outline, long neck, small low head, black nose, small dark eye, heavy hindquarters). **Predatory, never cute:** no big eyes, no smile, no blush, no rounded plush look (brief 7, kid appeal HIGH). Full gallop: front legs reaching forward, hind legs pushed back, body long and low, head forward and level, ears back. A couple of snow puffs under the feet are welcome; speed lines are drawn in the shot.
- Facing / anchor / size: Facing right. Bottom-centre anchor (lowest paw on y=0): about 700 x 340 (x -350..350, y -340..0).
- Notes: Used from 0.18 (icon row) to 0.9 (hero), often flipped. Must read at 35 px tall in the 10-icon row.
- Shots: s064, s065, s066, s079, s098, s108, s114, s115, s123, s124, s128, s222 (12 shots)

## `polar_bear_sling`
**Creature + prop (Churchill relocation).**

- Look: A sleeping (tranquillised) polar bear curled up inside a cargo net sling: net in dark rope lines over the white body, eyes closed, relaxed; four rope lines rising to a single hook at the top. Calm, not distressed.
- Facing / anchor / size: Anchor (0,0) = the top hook. Net bag hangs below: x -220..220, y 0..360.
- Notes: Hung from `helicopter` by a line drawn in the shot.
- Shots: s143 (1 shot)

## `polar_bear_sniffing`
**Creature (detection beats).**

- Look: Same design family as `polar_bear` / `polar_bear_standing` (creamy-white `#f4f1e4` coat, grey-blue `#c9d6e2` shading underneath and on the far legs, thick dark outline, long neck, small low head, black nose, small dark eye, heavy hindquarters). **Predatory, never cute:** no big eyes, no smile, no blush, no rounded plush look (brief 7, kid appeal HIGH). Standing on all fours, neck stretched up and head lifted high with the nose pointing to the sky, sniffing the wind; two short wavy scent lines are NOT part of the asset (drawn in the shot).
- Facing / anchor / size: Facing right. Bottom-centre anchor (feet on y=0): about 630 x 420 (x -300..330, y -420..0); nose tip near (+300,-400).
- Notes: Used small on horizons (0.16-0.45), flipped.
- Shots: s004, s005, s006, s011, s022, s164, s218 (7 shots)

## `polar_bear_swimming`
**Creature (aquatic stalk, underwater).**

- Look: Same design family as `polar_bear` / `polar_bear_standing` (creamy-white `#f4f1e4` coat, grey-blue `#c9d6e2` shading underneath and on the far legs, thick dark outline, long neck, small low head, black nose, small dark eye, heavy hindquarters). **Predatory, never cute:** no big eyes, no smile, no blush, no rounded plush look (brief 7, kid appeal HIGH). Fully submerged, swimming flat and long just below the surface: neck and head stretched forward, front paws paddling, hind legs trailing. Slightly blue-tinted shading (`#bcd3e3`) so it reads as underwater on `#3a9ad9`, outline stays dark.
- Facing / anchor / size: Facing right. Centre anchor: about 700 x 220 (x -350..350, y -110..110).
- Notes: Also used as a first-reveal silhouette under water (shot adds a dark `#1b4f86` glow + red rim), and with its top half above a water rect in s104 (head at the surface), so keep the head and back on the top edge.
- Shots: s082, s085, s086, s087, s088, s090, s091, s104 (8 shots)

## `polar_bear_thin`
**Creature (item 8 hero, also the emaciated bear in The Swim and icon grids).**

- Look: Same design family as `polar_bear` / `polar_bear_standing` (creamy-white `#f4f1e4` coat, grey-blue `#c9d6e2` shading underneath and on the far legs, thick dark outline, long neck, small low head, black nose, small dark eye, heavy hindquarters). **Predatory, never cute:** no big eyes, no smile, no blush, no rounded plush look (brief 7, kid appeal HIGH). A visibly lean adult on land: narrow waist, long legs, a slight dip behind the shoulders, hip bones shown as **two simple short curved lines** on the hindquarters. **Not sick-looking or gross:** no ribs, no sores, no sad face; lean and hungry, head low, looking ahead.
- Facing / anchor / size: Facing right. Bottom-centre anchor (feet on y=0): about 600 x 330 (x -300..300, y -330..0).
- Notes: Used at 0.18 in a 10x2 icon grid (must still read as a polar bear at ~110 px wide), 0.45-0.9 as hero, and as a silhouette.
- Shots: s093, s094, s095, s177, s178, s179, s180, s181, s182, s183, s184, s185, s186, s187, s190, s193, s194, s197, s198, s199, s200, s203, s212 (23 shots)

## `polar_bear_thin_collar`
**Overlay for `polar_bear_thin` (Pagano 2024 collar camera).**

- Look: Only a dark grey `#2b2b2b` GPS collar around the neck of `polar_bear_thin` with a small black camera box (blue lens dot) hanging under the throat. Nothing else (transparent elsewhere).
- Facing / anchor / size: Same anchor, facing and scale as `polar_bear_thin` (it is drawn at the same x/y/scale on top of it).
- Notes: s182 only.
- Shots: s182 (1 shot)

## `ringed_seal`
**Creature (prey, items 1, 3, 8).**

- Look: Ringed seal lying on the ice, head raised and alert, facing right: plump grey `#8a8f96` body with darker back, pale ring markings, pale belly, small round head, big dark eyes, short whiskers, small front flipper, hind flippers together. Not a cuddly pup.
- Facing / anchor / size: Facing right. Bottom-centre anchor (belly on y=0): about 420 x 170 (x -210..210, y -170..0).
- Notes: Used from 0.14 (inside lair icons) to 1.0 (close-up). Sits inside `snow_lair_cutaway` at local (-40,+140) scale 0.45, and is rotated 60 deg as it slides down the hole in s013.
- Shots: s003, s006, s007, s008, s009, s011, s012, s013, s021, s022, s057, s058, s059, s062, s063, s064, s065, s066, s072, s073, s074, s097, s193, s195, s196 (25 shots)

## `rubbish_bag`
**Prop (The Town).**

- Look: A black bin bag `#2b2b2b` tied at the top with a knot, lumpy, grey highlight.
- Facing / anchor / size: Anchor (0,0) = the knot (Doug's hand); bag hangs below: x -60..60, y 0..140.
- Notes: Held in Doug's front hand (point pose) and lying torn open by the bin.
- Shots: s136, s150 (2 shots)

## `rubbish_bin`
**Prop (The Town).**

- Look: A communal wheeled rubbish bin / small dumpster with the lid propped open, dark blue-grey `#4a5568`, a couple of bags poking out. Not green.
- Facing / anchor / size: Bottom-centre anchor: about 260 x 200 (x -130..130, y -200..0).
- Shots: s131, s132, s136 (3 shots)

## `snow_lair_broken`
**Place (item 1, the roof comes in).**

- Look: Same as `snow_lair_cutaway` (identical footprint, layers and hole) but the roof has caved in: a jagged hole in the top of the drift, broken snow chunks fallen into the cave, a puff of snow, the cave empty.
- Facing / anchor / size: Same anchor and bbox as `snow_lair_cutaway`.
- Notes: s013.
- Shots: s013 (1 shot)

## `snow_lair_cutaway`
**Place (item 1 hero diagram).**

- Look: Cross-section of a ringed-seal birth lair: a snowdrift mound rising above the flat snow surface (top at y -160), the cut face of the drift and of the snow layer below the surface in `#e6eef5` with faint layer lines, a hollow cave inside (pale blue `#cfe2ee`, x -220..260, y -60..+140, floor = the sea-ice top) and a dark breathing hole through the sea-ice band at x +120..+200 (from y +140 down to +260, open to the water). Sea-ice band y +140..+260 in `#bcd3e3`. Leave the cave interior empty (the seal is a separate asset).
- Facing / anchor / size: Anchor (0,0) = the snow surface level at the centre. Total about 840 x 420 (x -420..420, y -160..260). The shot's background bands match exactly: surface at y 0, sea ice +140..+260, water `#3a9ad9` below.
- Notes: Placed at the snow surface (y 560 or 600) at scale 1.
- Shots: s006, s007, s008, s009, s010, s011, s012, s021, s022 (9 shots)

## `snow_shelter`
**Prop (Doug's neat little snow shelter, item 1 + montage).**

- Look: A small neat snow-block dome (igloo-like, block lines in `#c9d6e2`) shown as a **cutaway**: the front half removed so the pale-blue hollow inside is visible, with a flat floor at y=0. Doug sits inside (drawn after the asset, `sit` pose at scale 0.4-0.5).
- Facing / anchor / size: Bottom-centre anchor: dome x -260..260, y -330..0; interior hollow about x -210..210, y -290..0.
- Notes: Doug sits at x -20. Keep the interior a light value so Doug's black lines read.
- Shots: s024, s025, s026, s218 (4 shots)

## `snow_shelter_broken`
**Prop (death 247 aftermath).**

- Look: The snow shelter collapsed into a low heap of broken snow blocks, a few blocks tumbled to the sides. No body. Flat top area at (0,-140) where the cap sits.
- Facing / anchor / size: Bottom-centre anchor: x -300..300, y -140..0.
- Notes: With `doug_cap` on top.
- Shots: s026, s027, s028 (3 shots)

## `stairwell`
**Place (The Town, the bear in the stairwell).**

- Look: Full-frame cross-section of a bare concrete stairwell: grey `#9aa3ab` walls, an upper landing at the left, a straight flight of stairs with a handrail descending to a lower landing at the right, a bare bulb, a door on the lower landing.
- Facing / anchor / size: Centre anchor, 1920 x 1080 at scale 1 (x -960..960, y -540..540). Upper landing floor at y -60 from x -960 to -560; flight down to the lower landing floor at y +380 from x +160 to +960; door at x +540..+700, y +100..+380.
- Notes: Doug stands on the upper landing (frame y 480), `polar_bear_standing` on the lower landing (frame y 920).
- Shots: s150, s151 (2 shots)

## `stick_sprinter`
**Crude-tier human (100 m world-record comparison).**

- Look: Crude-tier stick-man sprinter (scientist tier: 5 px lines, big round white head with grey crescent, short hair, **no red cap**, focused face), mid-stride, wearing a plain white running vest with a blank race bib. Generic: **no likeness of any real athlete**, no flag colours, no logos. `auto_ink`.
- Facing / anchor / size: Facing right. Bottom-centre anchor (feet on y=0): about 300 x 460.
- Shots: s112, s113, s114 (3 shots)

## `tent_collapsed`
**Prop (death 251 aftermath).**

- Look: The same green tent lying flat: fabric heap, two bent orange poles sticking out, guy lines slack, a small bump at the top centre (0,-80) where the cap sits. No body, no blood.
- Facing / anchor / size: Bottom-centre anchor: x -230..230, y -80..0.
- Notes: With `doug_cap` on the peak.
- Shots: s174, s175, s176 (3 shots)

## `tent_dented`
**Prop (The Tent).**

- Look: Exactly the library `tent` (green dome, orange trim) with a big round dent pushed into its right side, and a black bear nose with a bit of white muzzle poking into the dent from outside at the right. Only the nose and muzzle, no teeth.
- Facing / anchor / size: Same anchor and scale as `tent` (bottom-centre, x -190..190, y -238..0) plus the muzzle out to x +260.
- Notes: Drawn over `tent` at the same x/y/scale.
- Shots: s173, s174 (2 shots)

## `thermal_bear_face`
**Creature (thermal image of a polar bear).**

- Look: Only what a thermal camera sees of a polar bear: a floating front-facing face made of thermal glow. Bright yellow-white nose with orange, red and magenta halo rings; two smaller glowing eyes; a glowing mouth line; faint purple hints of the ears. Nothing else of the body. Eerie, not cute.
- Facing / anchor / size: Centre anchor: about 300 x 220 (x -150..150, y -110..110); nose at about (0,+30).
- Notes: On `thermal_screen`, from 0.25 (distant) to 1.0 (close).
- Shots: s046, s047, s048, s050, s051, s122, s219 (7 shots)

## `thermal_camera`
**Prop (Doug's handheld thermal camera).**

- Look: Handheld thermal imager: dark grey pistol-grip body, lens at the front (right), a small screen on the back facing the viewer showing purple with one tiny yellow glow.
- Facing / anchor / size: Anchor (0,0) = the grip (Doug's front hand, `point` pose); body about x -40..110, y -110..40.
- Notes: Held at scale 0.6.
- Shots: s042, s049, s050, s051 (4 shots)

## `thermal_screen`
**Prop (The Fur, the thermal display).**

- Look: A thermal camera display: thick dark-grey bezel with rounded corners, a few small buttons, a tiny 'IR' mark in a corner; the screen itself is dark purple-black `#1a0f2e` with faint blue-purple noise and a thin crosshair. Nothing glowing on it (the face and cap are separate).
- Facing / anchor / size: Centre anchor: 720 x 480 (x -360..360, y -240..240); screen area x -320..320, y -200..200.
- Notes: Used at 0.6-1.2.
- Shots: s044, s046, s047, s048, s049, s050, s051, s052, s053, s122, s219 (11 shots)

## `whale_carcass`
**Prop (the one bear that gained weight).**

- Look: Cartoon beached dead marine mammal (small whale): grey `#8a8f96` hump lying on its side, a few pale rib arcs showing on one patch, tail fluke on the ground. Clean and simple, **no red, no gore, no flesh**.
- Facing / anchor / size: Bottom-centre anchor: about 420 x 160.
- Notes: Small (0.5) on the cream data card.
- Shots: s187 (1 shot)
