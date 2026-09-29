# Asset requests: 001 Every Layer of the Ocean

From the director, for the illustrator (art director approves). House style per `assets/library/anglerfish.json` and
`channel/art_bible.md`: detailed creature tier (outlines 4-6, flat fills plus `spray` shading, darker back, lighter belly,
white eyes with black pupils), **facing right**, local coordinates centred on the anchor. Sizes are in local units at
scale 1. Creatures that appear on dark zone backgrounds (twilight `#1b4f86` down to hadal `#020308`) need mid-tone
fills and a light rim or highlight so they don't vanish. Several are also shown as `"silhouette": true` (marked
**SIL**), so the outer outline must be a clean, recognisable shape. **Anchors matter**: I placed every drawing
by the anchor described below.

Shots listed are from `shotlist.json`. Priority A = hero or recurring, B = supporting, C = one-off prop.

## Creatures

### portuguese_man_o_war (A)
- **What:** Portuguese man o' war (siphonophore colony), item 1.
- **Look:** a translucent blue-to-purple gas float (`#a35bd6` / `#b48be8`, lighter top highlight) shaped like an
  inflated, slightly lopsided balloon or sandwich bag, with a pink-purple crinkled crest along the top. Under it,
  a clump of short blue-purple polyps, then 5 to 7 long, wavy, thin tentacles (`#6a5acd`) with little bead dots.
- **Anchor:** (0,0) = the waterline at the centre of the float. The float sits above y<0 (about 300 wide, 130 tall),
  and the tentacles hang down to about y=+420.
- **Facing:** crest runs left-right; any direction works. **Shots:** s005, s007, s008, s009, s010, s011, s013, s014, s015, s017, s018, s019, s020, s021, s022, s023, s120, s230
- **DONE:** `assets/library/portuguese_man_o_war.json`, preview `assets/previews/001-assets-illustrator1-a.png`

### cone_snail (A)
- **What:** geography cone snail (*Conus geographus*), item 2.
- **Look:** a cone-shaped shell, wide shoulder tapering to a point, with a low spire. The pattern is brown and white
  ("map-like" tented blotches, rust-brown bands on cream). A small pink-grey soft body and a short siphon tube poke
  out at the narrow front.
- **Anchor:** bottom-centre on the sand at (0,0). About 320 long, 150 tall. **Facing:** narrow front end to the right.
- **Shots:** s024, s026, s027, s028, s030, s031, s033, s035, s039, s040, s041, s042, s043, s044. Also used 10 times small in a grid (s044), so it must read at scale 0.5.
- **DONE:** `assets/library/cone_snail.json`, preview `assets/previews/001-assets-illustrator1-a.png`

### cone_snail_engulf (B)
- **What:** the same snail spreading its stretchy false mouth (rostrum) like a pink cape or funnel over a stunned fish.
- **Look:** same shell as `cone_snail`. From the front, a wide translucent pink (`#e79aa0`) funnel or bell opens to the
  right, about 260 across, with a small yellow fish (`small_fish` colours) visible inside it.
- **Anchor:** bottom-centre, same as `cone_snail`. About 480 wide. **Facing:** right. **Shots:** s037, s038
- **DONE:** `assets/library/cone_snail_engulf.json`, preview `assets/previews/001-assets-illustrator1-a.png`

### small_fish (A)
- **What:** generic small reef fish (prey, recurring).
- **Look:** a yellow-orange body with a white belly, one dark stripe, a round eye and a forked tail. Simple and cute-ish,
  but not babyish.
- **Anchor:** centre. About 200 long. **Facing:** right. **Shots:** s028, s030, s031, s034, s036, s037, s053, s054, s119, s120, s151, s202, s206
- **DONE:** `assets/library/small_fish.json`, preview `assets/previews/001-assets-illustrator1-a.png`

### fish_halves (C)
- **What:** `small_fish` cleanly cut in two by the bobbit worm (cartoon, **no gore**).
- **Look:** two halves with a gap of about 40 between them. The cut faces are flat pale pink with a tiny bone line.
  No blood. Add two small motion "whoosh" lines.
- **Anchor:** centre. About 260 wide. **Facing:** right. **Shots:** s055
- **DONE:** `assets/library/fish_halves.json`, preview `assets/previews/001-assets-illustrator1-a.png`

### bobbit_antennae (A)
- **What:** only the five antennae of a buried bobbit worm, poking out of the sand.
- **Look:** five thin, slightly curved, striped stalks (white and brown bands) of different heights (about 60 to 150),
  growing from a small dark oval hole.
- **Anchor:** (0,0) = the sand surface at the hole; stalks go up (y<0). About 120 wide. **Shots:** s045, s046, s047, s048, s051, s052, s053, s056, s058
- **DONE:** `assets/library/bobbit_antennae.json`, preview `assets/previews/001-assets-illustrator1-a.png`

### bobbit_worm (A, SIL)
- **What:** *Eunice aphroditois*, full body (used buried in the sand, and as Barry in the aquarium).
- **Look:** a very long, segmented body with an iridescent purple-bronze sheen (`#7a4a6a` with a lighter
  `#b58aa8` highlight stripe) and tiny bristles on the sides. The head is at the right end, with five striped antennae
  and a pair of closed scissor-like jaws.
- **Anchor:** centre. **About 900 wide by 120 tall** (long on purpose). **Facing:** head to the right. **Shots:** s048, s049, s050, s061, s062
- **DONE:** `assets/library/bobbit_worm.json`, preview `assets/previews/001-assets-illustrator1-b.png`

### bobbit_worm_strike (A)
- **What:** the front of the bobbit worm bursting up out of the sand mid-strike.
- **Look:** the same colours as `bobbit_worm`. The body rises vertically, slightly S-curved, with wide-open
  scissor jaws (two hooked mandibles, dark red inside, no blood) at the top and the antennae flung back.
  Add a small burst of sand at the base.
- **Anchor:** (0,0) = the sand surface where the body leaves the ground. It extends up to about y=-420 and is about
  200 wide. **Shots:** s053, s063
- **DONE:** `assets/library/bobbit_worm_strike.json`, preview `assets/previews/001-assets-illustrator1-b.png`

### humboldt_squid (A, SIL)
- **What:** Humboldt squid (*Dosidicus gigas*), "diablo rojo".
- **Look:** a torpedo-shaped mantle with a diamond fin at the back (left end), a big eye, and eight arms plus two
  tentacles trailing to the right. Brick red `#b8322a` with darker red chromatophore dots.
- **Anchor:** centre. About 500 long. **Facing:** arms and eye to the right. Used a lot, down to scale 0.28, so the
  silhouette must stay clear. **Shots:** s067, s068, s069, s070, s071, s072, s073, s074, s075, s076, s077, s078, s079, s080, s081, s082, s083, s084, s090, s128, s135, s136, s137, s230
- **DONE:** `assets/library/humboldt_squid.json`, preview `assets/previews/001-assets-illustrator1-b.png`

### humboldt_squid_white (B)
- **What:** the same drawing, flashed pale (for the red and white flashing beat).
- **Look:** identical shape to `humboldt_squid`, with a near-white `#f3e9e4` body and faint pink dots. Keep the geometry
  exactly the same so the two swap cleanly. **Shots:** s074, s075
- **DONE:** `assets/library/humboldt_squid_white.json`, preview `assets/previews/001-assets-illustrator1-b.png`

### giant_squid (A, SIL)
- **What:** giant squid (*Architeuthis*).
- **Look:** a long, slim mantle with small fins at the left end and a head with one **huge** eye. Eight arms and two
  very long feeding tentacles with club tips trail right. Orange-red `#c8553d` with a lighter underside.
- **Anchor:** centre. About 700 long. **Facing:** tentacles to the right. **Shots:** s085, s086, s087, s091, s092, s093, s096, s097, s098, s099, s100, s103, s230
- **DONE:** `assets/library/giant_squid.json`, preview `assets/previews/001-assets-illustrator1-b.png`

### giant_squid_eye (A)
- **What:** an extreme close-up of the giant squid's eye (fills much of the frame).
- **Look:** a big round eye about 700 across with a silvery-grey iris ring, a large black pupil (about 45% of the
  width) with a white highlight, and reddish-orange squid skin with chromatophore dots around it.
- **Anchor:** centre. About 800 wide. **Shots:** s094, s095, s101
- **DONE:** `assets/library/giant_squid_eye.json`, preview `assets/previews/001-assets-illustrator1-b.png`

### sperm_whale (B, SIL)
- **What:** sperm whale.
- **Look:** dark grey `#5b6470`, a huge boxy head (about 1/3 of its length), a small eye near the mouth corner, a narrow
  underslung jaw with a few teeth, a wrinkled back, and a tail fluke. **Round white sucker-scar rings** on the head.
- **Anchor:** centre. About 800 long. **Facing:** head to the right. Also shown upside down (rotate 180) as a
  whale fall. **Shots:** s097, s098, s099, s128, s182
- **DONE:** `assets/library/sperm_whale.json`, preview `assets/previews/001-assets-illustrator1-c.png`

### barreleye_fish (A)
- **What:** barreleye (*Macropinna microstoma*), with its eyes pointing up.
- **Look:** a dark brown-black body (`#3a2e2a`, with a lighter `#6b5a50` rim on the fins) and big wing-like pectoral fins.
  The top of the head is a **transparent dome shield** (thin light-blue outline, very pale fill `#dff4ff`) with two
  **green tube-shaped eyes** inside it pointing straight up (bright green `#39d353` lenses on top). Two small dark
  nostril dots sit above the small mouth at the front, like fake eyes.
- **Anchor:** centre. About 420 long. **Facing:** mouth to the right. **Shots:** s104, s105, s106, s107, s108, s109, s110, s111, s112, s113, s114, s116, s117, s118, s119, s121
- **DONE:** `assets/library/barreleye_fish.json`, preview `assets/previews/001-assets-illustrator1-c.png`

### barreleye_fish_eyes_forward (A)
- **What:** the same fish with both tubular eyes rotated forward (pointing right) inside the shield.
- **Look:** identical geometry to `barreleye_fish`; only the eyes change. They swap in with a pop-in.
  **Shots:** s117, s119, s120, s121, s122, s123
- **DONE:** `assets/library/barreleye_fish_eyes_forward.json`, preview `assets/previews/001-assets-illustrator1-c.png`

### vampire_squid (A, SIL)
- **What:** vampire squid (*Vampyroteuthis infernalis*).
- **Look:** a dark reddish-brown `#6b1f2a` body, with webbing between the eight arms forming a cape (the web edge has
  small soft spines), two ear-like fins on the mantle, and big round blue eyes (`#5ad1ff` irises). The arm tips
  are slightly lighter.
- **Anchor:** centre. About 350 wide. **Facing:** eyes and arms to the right, or head-up; either is fine.
  **Shots:** s124, s125, s126, s127, s128, s129, s130, s131, s132, s133, s134, s135, s136, s138, s139, s140, s141
- **DONE:** `assets/library/vampire_squid.json`, preview `assets/previews/001-assets-illustrator1-c.png`

### vampire_squid_pineapple (B)
- **What:** the vampire squid's defensive "pineapple" posture, with its arms flipped inside out over its body.
- **Look:** a spiky ball or pineapple shape. The dark inner web with rows of soft spines faces outward and the fins
  stick out at the bottom. Same palette as `vampire_squid`.
- **Anchor:** centre. About 320 wide. **Shots:** s136, s137
- **DONE:** `assets/library/vampire_squid_pineapple.json`, preview `assets/previews/001-assets-illustrator1-c.png`

### anglerfish_male (B)
- **What:** the tiny male deep-sea anglerfish (no lure).
- **Look:** a small, slim brown-grey fish (`#6b6b7f`, lighter than the female) with a pointy snout, small hook-like teeth
  at the jaw tip, a big nostril, and **no rod or lure**.
- **Anchor:** centre. About 120 long. **Facing:** right. **Shots:** s153, s154, s155, s156, s157, s158
- **DONE:** `assets/library/anglerfish_male.json`, preview `assets/previews/001-assets-illustrator1-c.png`

### black_swallower (A)
- **What:** black swallower (*Chiasmodon niger*), normal.
- **Look:** a slim dark brown-black fish (`#3a3530`, lighter `#6e655c` belly) with a long, big-jawed head, a
  slightly open mouth showing hooked teeth, a long body and a small tail. It should look harmless and small.
- **Anchor:** centre. About 300 long. **Facing:** right. **Shots:** s162, s163, s164, s165, s166, s167, s169, s171, s174, s177, s178, s230
- **DONE:** `assets/library/black_swallower.json`, preview `assets/previews/001-assets-illustrator1-c.png`

### black_swallower_full (A)
- **What:** the same fish with its stomach hugely distended.
- **Look:** the same head and tail, but the belly is a huge balloon about 3 times the body depth. The skin is stretched
  **see-through** (a pale translucent `#e8d8c8` fill with a thin outline), with the outline of a coiled long fish
  (snake mackerel, silver) visible inside. No gore.
- **Anchor:** centre. About 420 wide. **Facing:** right. Also used rotated 180 (floating belly-up) and with a
  Doug-shaped belly (I add an outline over it). **Shots:** s166, s171, s173, s175, s176, s179
- **DONE:** `assets/library/black_swallower_full.json`, preview `assets/previews/001-assets-illustrator1-c.png`

### snake_mackerel (B)
- **What:** snake mackerel (*Gempylus serpens*), the prey.
- **Look:** a very long, thin, silvery-steel body (`#aab4c0`) with a darker back, a pointed head with a jutting lower jaw
  and fangs, and a small forked tail.
- **Anchor:** centre. About 700 long, 80 tall. **Facing:** right. **Shots:** s167, s171, s174
- **Done:** `assets/library/snake_mackerel.json`, preview `assets/previews/001-ill2-creatures.png`

### zombie_worms (A, SIL)
- **What:** a cluster of *Osedax* bone-eating worms.
- **Look:** a patch of 8 to 12 tiny pink tubes (`#ff8fa3`) standing up from a small bone surface, each topped with
  a feathery red plume (`#e0201b`). It should read as "pink shag carpet".
- **Anchor:** bottom-centre (the bone surface). About 200 wide, 120 tall. It is scaled up to 3x in a close-up (s186),
  so give it clean shapes. **Shots:** s181, s184, s186, s187, s188, s189, s190, s191, s193, s194, s197, s198, s230
- **Done:** `assets/library/zombie_worms.json`, preview `assets/previews/001-ill2-creatures.png`

### hadal_snailfish (A, SIL)
- **What:** hadal snailfish (*Pseudoliparis*), the deepest fish.
- **Look:** a pale, translucent pinkish-white (`#f3d6d6`) tadpole shape: a big soft rounded head, a tapering
  gelatinous body, a long soft fin fringe to the tail, small dark eyes, and faint visible pink insides for the
  "jelly" look. It should look calm.
- **Anchor:** centre. About 300 long. **Facing:** right. **Shots:** s200, s207, s208, s209, s210, s211, s212, s214, s215, s217, s218, s219, s230
- **Done:** `assets/library/hadal_snailfish.json`, preview `assets/previews/001-ill2-creatures.png`

### amphipod (B)
- **What:** a deep-trench amphipod (small shrimp-like scavenger).
- **Look:** a curled, segmented, shrimp-like body, pale orange-pink `#f2b8a0`, with many little legs, two pairs of
  antennae and a small dark eye.
- **Anchor:** centre. About 220 long. **Facing:** right. **Shots:** s236, s237, s238
- **Done:** `assets/library/amphipod.json`, preview `assets/previews/001-ill2-creatures.png`

### crab (C)
- **What:** a rice-paddy crab (freshwater crab).
- **Look:** a muddy brown-green shell, two claws up, and eye stalks.
- **Anchor:** centre. About 220 wide. **Shots:** s238
- **Done:** `assets/library/crab.json`, preview `assets/previews/001-ill2-creatures.png`

### swordfish (C)
- **What:** swordfish (for the "its eye fits in the pupil" comparison).
- **Look:** a dark blue-grey back, silver belly, long flat bill, crescent tail, tall dorsal fin, and a clear round eye.
- **Anchor:** centre. About 500 long. **Facing:** right. **Shots:** s095
- **Done:** `assets/library/swordfish.json`, preview `assets/previews/001-ill2-creatures.png`

## Places and big props

### coral_reef (A)
- **What:** a coral cluster for the sunlit reef scenes (used in 23 shots).
- **Look:** pink branching coral, an orange brain coral, a purple sea fan and some green seaweed, on a small rock base.
- **Anchor:** bottom-centre (sits on the sand line). About 600 wide, 350 tall. **Shots:** s024, s026, s027, s028, s030, s031, s032, s033, s035, s036, s037, s038, s039, s040, s041, s042, s043, s045, s046, s047, s052, s053, s056
- **Done:** `assets/library/coral_reef.json`, preview `assets/previews/001-ill2-places-a.png`

### whale_skeleton (A)
- **What:** a whale fall: a whale skeleton lying on the sea floor.
- **Look:** off-white bones `#efe6cf` with grey shading. A big skull at the left, a curved row of ribs, and a tapering
  spine to the tail on the right. It should read at abyss darkness.
- **Anchor:** bottom-centre (on the floor). **About 1200 wide by 300 tall.** **Shots:** s181, s183, s184, s189, s194, s195, s196, s197, s198
- **Done:** `assets/library/whale_skeleton.json`, preview `assets/previews/001-ill2-places-b.png`

### world_map (A)
- **What:** a simple MS Paint world map for location beats.
- **Look:** flat green continents (`#6bbf59`, dark outline), a transparent or light-blue ocean, no labels, and a crude
  but recognisable shape. Japan, the Mariana area, California, the UK and Indonesia must be where they really are.
- **Anchor:** centre. **Size exactly 1600 x 800, equirectangular:** x = lon / 180 * 800, y = -lat / 90 * 400. I place
  red circles by this formula (Indo-Pacific, Ogasawara 27N 142E, Tokyo, Monterey 36.8N 122W, Mariana 11.3N 142.2E).
  **Shots:** s025, s088, s089, s185, s221
- **Done:** `assets/library/world_map.json`, preview `assets/previews/001-ill2-places-b.png`

### aquarium (B)
- **What:** a public aquarium display tank (the Cornwall "Barry" story).
- **Look:** a glass tank with a black frame, light-blue water, some rocks and coral at the bottom, and 2 or 3 small
  fish. Keep the middle fairly clear.
- **Anchor:** bottom-centre. About 560 wide, 360 tall. **Shots:** s057, s058, s059, s060
- **Done:** `assets/library/aquarium.json`, preview `assets/previews/001-ill2-places-a.png`

### live_rock (C)
- **What:** aquarium "live rock".
- **Look:** a lumpy grey-purple porous rock with pink coralline patches and a small dark hole.
- **Anchor:** bottom-centre. About 260 wide. **Shots:** s058, s061
- **Done:** `assets/library/live_rock.json`, preview `assets/previews/001-ill2-places-a.png`

### mount_everest (C)
- **What:** Mount Everest, for the "peak still 2 km underwater" comparison.
- **Look:** a grey-brown pyramid peak with snow caps and a tiny flag at the summit.
- **Anchor:** bottom-centre. **About 800 wide by 750 tall** (the summit is at about y=-750 above the anchor).
  **Shots:** s223
- **Done:** `assets/library/mount_everest.json`, preview `assets/previews/001-ill2-places-b.png`

## Vehicles

### yellow_submarine (A)
- **DONE** (`assets/library/yellow_submarine.json`, preview `assets/previews/001-vehicles.png`)
- **What:** Doug's tiny yellow submarine (final item, the outro frame).
- **Look:** a rounded yellow hull `#ffd21f` with a black outline, a small conning tower, a propeller at the left, and
  two headlights at the front (right). There is **one big round porthole at local (60, -20), radius about 55, with
  pale-blue glass `#bfe6ff`**. I draw a tiny Doug (scale 0.22 to 0.3) on top of the porthole, so keep it clear of
  details.
- **Anchor:** centre. About 420 wide. **Facing:** right. **Shots:** s230, s231, s232, s233, s235, s239, s240, s241, s242, s243, s244, s245

### submersible (B)
- **DONE** (`assets/library/submersible.json`, preview `assets/previews/001-vehicles.png`)
- **What:** a generic modern research submersible (Kubodera's team, Cameron, Vescovo).
- **Look:** a white and orange body, a front viewport sphere, thrusters, two lights, and a small manipulator arm.
- **Anchor:** centre. About 450 wide. **Facing:** right. **Shots:** s088, s090, s091, s092, s228, s229

### trieste (B)
- **DONE** (`assets/library/trieste.json`, preview `assets/previews/001-vehicles.png`)
- **What:** the bathyscaphe *Trieste* (1960).
- **Look:** a long grey cigar-shaped float with a small rail deck on top and a small round crew sphere hanging underneath
  with one tiny window. Its look is simple and historic.
- **Anchor:** centre. About 600 wide. **Facing:** right. **Shots:** s225, s226, s227

### rov (C)
- **DONE** (`assets/library/rov.json`, preview `assets/previews/001-vehicles.png`)
- **What:** an MBARI-style underwater robot (ROV).
- **Look:** a yellow boxy frame, a white float block on top, blue thrusters, a camera and two lights at the front, and a
  tether cable going up.
- **Anchor:** centre. About 400 wide. **Facing:** right. **Shots:** s116

### fishing_boat (C)
- **DONE** (`assets/library/fishing_boat.json`, preview `assets/previews/001-vehicles.png`)
- **What:** a small fishing boat (Baja fishermen, sailors' stories).
- **Look:** a white hull with a red stripe, a small cabin and a fishing pole or boom.
- **Anchor:** (0,0) = the waterline centre (the hull sits on the water). About 500 wide. **Facing:** right.
  **Shots:** s068, s086

### baited_camera_lander (B)
- **DONE** (`assets/library/baited_camera_lander.json`, preview `assets/previews/001-vehicles.png`)
- **What:** a deep-sea baited camera lander (the 2022 snailfish footage).
- **Look:** a metal tripod frame (grey) with an orange float, a camera plus light on top, and a mesh bait bag hanging in
  the middle.
- **Anchor:** bottom-centre (feet on the floor). About 350 tall. **Shots:** s208

### school_bus (B)
- **DONE** (`assets/library/school_bus.json`, preview `assets/previews/001-vehicles.png`)
- **What:** a yellow school bus in side view (the man o' war tentacles and the whale-skeleton length).
- **Look:** yellow `#ffc61a`, a black stripe, a row of windows and black wheels.
- **Anchor:** bottom-centre. About 600 wide. **Facing:** right. **Shots:** s011, s189

### small_car (C)
- **DONE** (`assets/library/small_car.json`, preview `assets/previews/001-vehicles.png`)
- **What:** a small hatchback car (the "car parked on your thumbnail" analogy).
- **Look:** a red or blue compact car in side view.
- **Anchor:** bottom-centre (the wheels' bottom). About 350 wide. **Shots:** s213

## Scale-comparison and everyday props (C unless noted)

- **plastic_bag (A, SIL):** **DONE** (preview `assets/previews/001-props.png`) a crumpled white-grey single-use plastic shopping bag with two handles and faint wrinkle lines.
  About 260 wide, centred. It must read on near-black (light grey fill `#dcdcdc`). It is also the "sandwich bag" in s011.
  **Shots:** s011, s232, s233, s234, s235, s240, s242, s243
- **tv_remote:** **DONE** (preview `assets/previews/001-props.png`) a black TV remote with coloured buttons, lying horizontally. About 250 long, bottom-centre. **Shots:** s027
- **suitcase:** **DONE** (preview `assets/previews/001-props.png`) a fat, over-packed suitcase with bulging straps and a luggage tag reading "HEAVY". About 300 wide,
  centred. **Shots:** s071
- **traffic_light:** **DONE** (preview `assets/previews/001-props.png`) a traffic light on a short pole; the red light is lit and the others are dim. About 300 tall,
  centred. **Shots:** s075
- **basketball:** **DONE** (preview `assets/previews/001-props.png`) an orange ball with black seams. About 120 across, centred. **Shots:** s094
- **american_football:** **DONE** (preview `assets/previews/001-props.png`) a brown American football with white laces. About 180 long, centred. **Shots:** s129
- **banana:** **DONE** (preview `assets/previews/001-props.png`) a yellow banana. About 250 long, centred. **Shots:** s163
- **canoe:** **DONE** (preview `assets/previews/001-props.png`) a red-brown wooden canoe in side view. About 600 long, centred. **Shots:** s168
- **sofa:** **DONE** (preview `assets/previews/001-props.png`) a three-seat sofa, red or brown. About 420 wide, bottom-centre. **Shots:** s050
- **phone:** **DONE** (preview `assets/previews/001-props.png`) a smartphone standing upright with a glowing pale-blue screen (spray glow). About 150 tall, centred. **Shots:** s109, s150
- **chemical_barrel:** **DONE** (preview `assets/previews/001-props.png`) an industrial steel drum, green or grey, with a yellow hazard label. About 200 wide by 280 tall,
  centred. **Shots:** s237, s238
- **harpoon_tooth (B):** **DONE** (preview `assets/previews/001-props.png`) a diagram close-up of the cone snail's hollow, barbed radular tooth: a long, slim, pale ivory
  harpoon with a hollow channel line, backward barbs near the tip, and a pointed tip to the right. About 500 long,
  centred. **Shots:** s029
- **thumbs_up_hand (visual-review fix):** **DONE** (preview `assets/previews/001-every-layer-of-the-ocean-thumbs-up.png`) a crude cartoon
  thumbs-up: fist with four stacked curled fingers, thumb straight up with a pale thumbnail on top, blue sleeve cuff.
  About 250 wide by 490 tall, centred; the top of the thumbnail is at local y=-245. Replaces the skin-coloured
  ellipse and rect in s213. Suggested: asset at x 960, y 790, scale 1.2, with `small_car` at x 935, y 500 (the car's wheels rest on the thumbnail). **Shots:** s213

## Characters and Doug props

### squid_costume (A)
- **DONE** (`assets/library/squid_costume.json`, preview `assets/previews/001-characters.png`)
- **What:** Doug's homemade squid costume (the Humboldt death beat). It is worn **over Doug**.
- **Look:** a brown cardboard tube or cone mantle (`#c89b62`, visible tape strips and a scribbled marker eye), with
  6 to 8 floppy cardboard tentacles hanging from the bottom and an open top so Doug's head and red cap stick out
  above it.
- **Anchor:** matches the Doug rig at the same x, y and scale: (0,0) = Doug's hips. The tube spans about
  y=-150 (neck) to y=+60 and is about 180 wide; the tentacles hang to y≈+200. I draw it right after the Doug element.
  It is also shown empty and floating away (rotated 25 degrees).
- **Shots:** s082, s083, s084. Art director: please check it doesn't count as changing Doug's design (it's a prop).

### doug_cap (A)
- **DONE** (`assets/library/doug_cap.json`, preview `assets/previews/001-characters.png`)
- **What:** Doug's red cap on its own (taken by the bobbit worm, and the only thing that floats up from the black
  swallower).
- **Look:** **Exactly the rig cap** from `studio/doug.py` `_cap()`: a `#e0201b` dome plus a brim pointing right, with a
  5 px black outline. Scale it so that at scale 1 it matches Doug at scale 1 (about 150 wide).
- **Anchor:** centre. **Shots:** s063, s064, s179, s180

### scientist (B)
- **DONE** (`assets/library/scientist.json`, preview `assets/previews/001-characters.png`)
- **What:** the recurring presenter or researcher: a crude stick man in **Doug's tier, not the creature tier**.
- **Look:** the same crude line style as Doug (5 px lines, big round head with a grey crescent, oval eyes) but **no red
  cap**. Round glasses, a white lab coat (a simple trapezoid over the torso) and messy hair strokes. Neutral face.
- **Anchor:** hips at (0,0); feet at +150, top of head at about -300 (the Doug rig's proportions). **Facing:** right.
  **Shots:** s033, s060, s061, s080, s111, s158, s206

### diver (C)
- **DONE** (`assets/library/diver.json`, preview `assets/previews/001-characters.png`)
- **What:** a researcher-diver (the Humboldt "timid" story), in the crude stick-man tier.
- **Look:** a stick man like the scientist, but with a dive mask, a yellow tank, fins, and a dive light held forward
  in the right hand (at about local (110, -60)). **No red cap**.
- **Anchor:** hips at (0,0). **Facing:** right. **Shots:** s077, s078

## Notes for the art director
- Existing assets reused: `anglerfish`, `gravestone`, `question_mark`, `exclamation_mark`, `warning_triangle`,
  `red_x`, `thermometer`.
- The bobbit cap-theft beat is staged so the **cap is never missing from Doug's head** on screen (the rig always draws
  it). Instead the cap is shown in the worm's jaws (s063), then only Doug's legs stick out of the burrow (s064), and
  Doug climbs out wearing the cap (s065).
- The flattened "pancake" Doug (s218) and the ice-cube Doug (s197, s198) are built inline from ellipses and rects in
  the shotlist, so the rig is untouched.
