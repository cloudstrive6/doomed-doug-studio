# 024-moose-deadlier-than-bears: asset requests (director to illustrator / art director)

Library assets I reuse as they are: `moose` (the standing bull in most shots), `grizzly_bear` (the bear reference figure; it never attacks anything), `grey_wolf`, `grey_wolf_sitting`, `deer`, `cat_angry`, `moose_costume` (021 callback only, s021), `small_car`, `field_guide_open`, `chalkboard` (tiny meter icon at 0.07), `narrator_hand`, `pine_tree`, `snowy_fir`, `fallen_log`, `doormat`, `seagrass`, `front_door`, `kitchen_counter`, `bed`, `dollar_bill`, `ruler`, `basketball_hoop`, `tape_measure`, `library_book`, `journal_paper`, `wait_stopwatch` (50-second dive timer), `calendar`, `clock`, `thermometer`, `speedometer`, `finish_banner`, `bathroom_scale`, `travel_suitcase`, `platform_scale`, `house`, `camper` (neighbours, volunteers, 'four average men'), `scientist`, `wildlife_official`, `magnifying_glass`, `binoculars`, `airplane`, `fishing_boat`, `bucket`, `dinner_plate`, `large_dog`, `rabbit`, `moss_patch`, `water_splash_small`, `snow_dust_cloud`, `north_america_map`, `gravestone`, `doug_cap`, `question_mark`, `exclamation_mark`, `warning_triangle`, `red_x`.

Drawn from primitives in the shotlist (no asset needed): the BEAR / MOOSE tally marks, the field-guide stamps, the evidence and sober cards, the newspaper, the 55% bar, the den hillside, the railway between snow walls, the night road and headlight beam, the 100 m track, the RAN / STOOD columns, the moon, gates, boxing gloves (red circles at Doug's hands).

House rules (brief section 7): detailed cartoon tier, thick black outline (5-6), flat fills with soft interior shading, readable at phone size. **Moose are heavy, long-legged and menacing**: small hard eye under a heavy brow, long drooping overhanging muzzle, high shoulder hump, hanging bell, never cute or mascot-like, nothing from cartoons. Match `moose.json`'s palette (dark brown body, darker back, long pale grey-brown legs, pale tan palmate antlers) on every moose pose so they read as the same animal. Bears match `grizzly_bear.json`. **No blood, no wounds, no carcasses, no dead moose anywhere** (train, road and locked antlers are numbers or antlers only). Everything faces right unless noted; the shotlist flips as needed. The bbox for each asset is what the shotlist was laid out against: please keep to it (anchor at (0,0)).

### bear_moose_scoreboard
- What: The episode's BEAR / MOOSE scoreboard (art director owns the look; brief section 2).
- Look: Base it on `chalkboard.json` (same frame, ledge, chalk and eraser, same dark green #2f5a3a board). Chalk-white #f4f4ec hand-lettered header row: **BEAR** centred at (-165,-150) and **MOOSE** centred at (+165,-150), bold, about 60 units tall. A chalk vertical divider at x=0 from y -190 to +160 and a chalk underline under the headers at y -100. **Leave both columns empty below the header**: the shotlist chalks the tally marks itself (BEAR marks in x -300..-40, MOOSE marks in x +30..+300, y -60..+150; groups of five with a diagonal). No numbers, no animals drawn on it. Must read as 'a crude scoreboard' at scale 0.38 too (closing shot).
- Facing/anchor: Centre anchor. bbox x -390..390, y -238..238 (about 780 x 476).
- Shots (15): s018, s019, s020, s047, s065, s096, s118, s141, s167, s191, s214, s238, s269, s275, s276.

### moose_warning
- What: The library bull `moose` in its warning posture (item 1 'ears back, hump hair up'; reused for every 'aggressive moose' beat).
- Look: Same geometry, colours, antlers and footprint as `moose.json` so it swaps in place, but: **ears pinned flat back** along the neck, the long hairs on the shoulder hump **standing straight up** as a bristly dark crest (clear spiky silhouette), head held a little lower, small hard eye with a lowered brow, a hint of white of the eye. Heavy and menacing, never cartoon-cute.
- Facing/anchor: Facing right, bottom-centre anchor (hooves on y=0), same as `moose`. bbox x -280..350, y -566..0 (about 630 x 566).
- Shots (7): s022, s023, s024, s063, s162, s186, s243.

### moose_head_on
- What: Bull moose head and shoulders, **head-on** (the thumbnail hero; also s014 'Here's the problem.').
- Look: Detailed tier. Huge broad palmate antlers spreading to both sides (pale tan like `moose.json`), ears pinned back, hump hair raised behind the head, long drooping overhanging muzzle, hanging bell (dewlap) under the chin, two small hard eyes under heavy brows. Dark brown. Menacing, not cute: no smile, no big round eyes.
- Facing/anchor: Front view, centre anchor. bbox x -350..350, y -350..350 (about 700 x 700).
- Shots (1): s014.

### moose_cow
- What: Adult cow moose (no antlers): the mother in The Calf, the 360 kg cow in The Apples, the antlerless winter moose.
- Look: Same palette and build as `moose.json` (dark brown body, high shoulder hump, long pale grey-brown legs, long drooping muzzle, small bell) but **no antlers**, slightly lighter build, ears up and alert-back. Heavy, long-legged, unmistakably a moose.
- Facing/anchor: Facing right, bottom-centre anchor (hooves y=0). bbox x -280..280, y -480..0 (about 560 x 480).
- Shots (18): s060, s061, s062, s066, s067, s068, s070, s072, s084, s085, s089, s090, s091, s092, s093, s136, s178, s237.

### moose_cow_rearing
- What: Cow moose **rearing on her hind legs, front hooves raised and striking** (The Hooves: the kick, defending the calf, standing up at boxing Doug).
- Look: No antlers (cow, or a bull after shedding). Body tilted up about 50 degrees, hind legs planted, both front legs raised and bent forward with the dark hooves clearly visible at the front top, ears pinned back, mane up. Also used as a black silhouette with a red rim (s128), so the outline alone must read as 'a moose rearing'. No contact, no victim drawn.
- Facing/anchor: Facing right, bottom-centre anchor at the hind hooves (y=0). bbox x -240..240, y -640..0 (about 480 x 640).
- Shots (4): s128, s129, s137, s143.

### moose_calf
- What: Newborn moose calf ('assembled from spare legs').
- Look: Reddish-brown #8a5a3a (lighter than the adult), absurdly long knobbly legs with big knees, short body, big ears, long-ish snout, no hump, no antlers. Wobbly stance. It must look awkward and gangly, **not** cute-baby (no big shiny eyes, no smile): adult-coded, nature-documentary.
- Facing/anchor: Facing right, bottom-centre anchor. bbox x -150..150, y -300..0 (about 300 x 300).
- Shots (22): s053, s054, s055, s056, s057, s058, s059, s060, s061, s062, s063, s066, s067, s068, s069, s070, s071, s072, s136, s137, s237, s247.

### moose_charging
- What: Bull moose **charging head-down at a gallop** (The Run at 56 km/h, rut sparring as a facing pair, the bull charging cardboard-antlered Doug, wolves chasing).
- Look: Same palette and antlers as `moose.json`. Head lowered and thrust forward with the antlers aimed ahead, ears back, legs mid-gallop (front pair reaching forward, hind pair pushing back), a few speed strokes behind the rump. Two of them are placed face to face (one flipped) for 'lock antlers and shove', so keep the antler tips at the front-top.
- Facing/anchor: Facing right, bottom-centre anchor (lowest hoof on y=0). bbox x -325..325, y -420..0 (about 650 x 420).
- Shots (21): s028, s104, s105, s106, s107, s108, s109, s110, s111, s130, s131, s163, s184, s185, s192, s194, s232, s234, s235, s236, s239.

### moose_velvet
- What: Bull moose with **half-grown antlers in velvet** (The Rut: 'a brand-new set every summer', 'fastest-growing tissue').
- Look: `moose.json` body, but the antlers are about half size, rounded, soft-looking and covered in fuzzy grey-brown velvet (no pale bone), with a few blood-vessel-free texture strokes. Summer coat a bit glossier.
- Facing/anchor: Facing right, bottom-centre anchor. bbox x -280..350, y -500..0 (about 630 x 500).
- Shots (3): s176, s177, s179.

### moose_antler_rack
- What: A **shed pair of bull moose antlers** joined as a rack (127 cm span; laid across a double bed; ~one of three 'not antlers, hooves or calves' icons).
- Look: Pale tan bone #d9c49a with darker shading, broad palmate paddles with tines along the rims, the two paddles spreading wide left and right from a small skull-plate stub in the middle (no skull, no blood). Seen from the front so the full span reads. Span = the full asset width.
- Facing/anchor: Centre anchor. bbox x -300..300, y -130..130 (about 600 x 260).
- Shots (5): s178, s180, s181, s182, s247.

### moose_head_surfacing
- What: A moose head and neck **rising out of a lake, draped in pondweed and chewing** (The Dive, beside Doug's paddleboard).
- Look: Wet dark-brown head and upper neck emerging from the water up to the jaw/neck, antlers optional (antlerless reads better at small size, your call), long muzzle mid-chew, pondweed strands hanging from the muzzle and draped over the ears (match `water_weed_draped` greens), drips, a ring of ripples at the waterline. Eye looking straight ahead, **not** at Doug.
- Facing/anchor: Facing right, anchor (0,0) = waterline under the neck. bbox x -180..180, y -300..20 (about 360 x 320).
- Shots (3): s050, s051, s052.

### moose_submerged
- What: A whole moose **completely underwater**, feeding on the lake bed (lake cross-section shots in The Dive).
- Look: Side view, legs standing on the lake bed, body fully below the surface, head lowered to the plants with water weed in its mouth, nostrils drawn pinched shut, a few bubbles rising from the back, colours slightly blue-tinted (#5b4a40 body) so it reads as underwater on #3a9ad9.
- Facing/anchor: Facing right, bottom-centre anchor on the lake bed (hooves y=0). bbox x -310..310, y -560..0 (about 620 x 560).
- Shots (8): s033, s036, s042, s043, s044, s045, s046, s048.

### moose_nose_cutaway
- What: Cross-section diagram of a **moose nose with the nostril valves** (Witmer's dissection, 'AUTOMATIC VALVE').
- Look: Detailed-tier side view of the front of a moose muzzle (big drooping overhanging nose) cut away to show the nasal passage in pale pink #f4c6c4 (cartoon, not realistic) with two flap-like valves. The **nostril openings are at about (+120,+120) and (+220,+120)** on the lower front so the shotlist's blue arrows can press them shut. Diagram style, no blood, no gore.
- Facing/anchor: Facing right, centre anchor. bbox x -400..400, y -250..250 (about 800 x 500).
- Shots (4): s038, s039, s040, s041.

### moose_in_apple_tree
- What: A **moose stuck in an apple tree** (Gothenburg 2011, The Apples hero image; also shown as a silhouette and tilted -14 degrees for the rescue).
- Look: One drawing: an apple tree (same tree as `apple_tree`) with a cow moose (no antlers) wedged belly-down across the branches in the crown, long legs dangling down on both sides, head drooping over a branch looking uncomfortable, a few red apples in the leaves and a couple falling. Dry and absurd, **no** cartoon-drunk cues (no hiccups, no swirly eyes, no bubbles).
- Facing/anchor: Bottom-centre anchor (trunk base on y=0). bbox x -380..380, y -700..0 (about 760 x 700).
- Shots (12): s077, s080, s081, s082, s083, s086, s087, s097, s098, s099, s100, s101.

### locked_antlers_ice
- What: **Two sets of bull moose antlers locked together, sticking up through ice** (Unalakleet 2016).
- Look: Only the antlers above a flat ice surface: two big pale palmate racks interlocked in the middle, tines tangled, a little snow on top, a short ice-crack ring where they come out of the ice. **No heads, no bodies, no eyes**, nothing below the ice line.
- Facing/anchor: Anchor (0,0) = ice surface at the centre. bbox x -350..350, y -260..0 (about 700 x 260).
- Shots (2): s189, s190.

### moose_track
- What: A **moose front hoof print in snow** (7 in / 18 cm; compared with a dollar bill).
- Look: Two long pointed teardrop halves of a split hoof (cloven), toes pointing up, with two small dewclaw dots behind, pressed into white snow: blue-grey #9fb3c6 inside shading, a crisp dark outline. Its length (vertical) must be about 1.15x the length of `dollar_bill` at the same scale-to-size ratio: at scale 1.4 the print is ~380 px long next to the bill at 0.75 (~330 px).
- Facing/anchor: Toes up, centre anchor. bbox x -85..85, y -135..135 (about 170 x 270).
- Shots (3): s132, s133, s247.

### moose_icon
- What: Tiny flat **moose map icon** (map counts: 2 at Gander Bay, 4 at Howley, the island filling up, 19 hit by one train, the 385 calendar, Anchorage numbers).
- Look: Simple dark-brown #5a3a24 moose silhouette in side view with a pale antler hint and a thin black outline; no face detail. Must stay a readable moose at scale 0.16 (about 26 px wide).
- Facing/anchor: Facing right, centre anchor. bbox x -80..80, y -60..60 (about 160 x 120).
- Shots (13): s157, s158, s204, s205, s206, s224, s225, s251, s252, s253, s254, s255, s261.

### grizzly_running
- What: Grizzly **sprinting** (The Run: 'you cannot outrun a bear', 64 km/h).
- Look: Match `grizzly_bear.json` exactly (colours, hump, claws) in a full gallop: front legs reaching, back legs bunched, ears back, mouth closed. Not attacking anything.
- Facing/anchor: Facing right, bottom-centre anchor. bbox x -300..300, y -330..0 (about 600 x 330).
- Shots (5): s103, s109, s110, s111, s119.

### grizzly_sleeping
- What: Grizzly **curled up asleep** (in the den cross-section, The Snow).
- Look: Same palette as `grizzly_bear`, curled in a ball, nose tucked to the paws, eyes closed (single lid lines), relaxed. The shotlist draws the den, the hillside and the 'Z's around it.
- Facing/anchor: Bottom-centre anchor. bbox x -230..230, y -220..0 (about 460 x 220).
- Shots (4): s150, s152, s153, s165.

### grizzly_cub
- What: Grizzly cub (The Calf: 'furiously protective of their cubs').
- Look: Same palette as `grizzly_bear`, small and round but not cartoon-cute (no big shiny eyes, no smile). Standing on all fours.
- Facing/anchor: Facing right, bottom-centre anchor. bbox x -130..130, y -180..0 (about 260 x 180).
- Shots (1): s064.

### brown_bear_swimming
- What: A **brown bear swimming**, head and hump above the water (The Dive: 'excellent swimmers').
- Look: `grizzly_bear` palette; only the head, ears and the top of the shoulder hump show above a waterline with a V-shaped wake and ripples; dark underwater body faintly visible below. Calm, not attacking.
- Facing/anchor: Facing right, anchor (0,0) = waterline at the body centre. bbox x -250..250, y -140..20 (about 500 x 160).
- Shots (2): s030, s031.

### black_bear
- What: American **black bear** (Ashton, Idaho apple trees; the calf-predator chart; Newfoundland's largest land carnivore).
- Look: Detailed tier: glossy black #1f1f22 coat with grey-blue highlights so it reads on night navy, brown muzzle, no shoulder hump, straight face profile, rounder ears than the grizzly, short claws. Standing on all fours, calm.
- Facing/anchor: Facing right, bottom-centre anchor. bbox x -240..260, y -300..0 (about 500 x 300).
- Shots (4): s068, s094, s096, s254.

### apple
- What: A single red apple (Doug holds it out at s022-s024; Doug's cap sits on it at death 196; fermented apples on the lawn).
- Look: Shiny red #d6262b apple with a darker side, white highlight, short brown stalk and one green leaf. Reads at scale 0.25.
- Facing/anchor: Centre anchor; top of the apple at about y -80 (the cap rests there). bbox x -80..80, y -85..85 (about 160 x 170).
- Shots (6): s022, s023, s024, s026, s081, s089.

### apple_tree
- What: Backyard **apple tree** (Swedish garden, Ashton Idaho).
- Look: Short thick brown trunk, broad round leafy crown in dark green with red apples dotted through it. Reads on the night navy (#1b2f5a) background: give the leaves a mid-green #3f7a35 with lighter clumps.
- Facing/anchor: Bottom-centre anchor. bbox x -360..360, y -700..0 (about 720 x 700).
- Shots (4): s075, s079, s094, s095.

### willow_bush
- What: Clump of **boreal willow shrubs** (the calf hides in them; the cow steps out of them; Doug's cap hangs on a branch at death 197).
- Look: Dense clump of thin upright reddish-brown willow stems with narrow yellow-green leaves (#9aa84a / #6f8a3a), taller in the middle. Opaque enough to hide a cow moose's body (to about y -300). Not a pine.
- Facing/anchor: Bottom-centre anchor. bbox x -210..210, y -360..0 (about 420 x 360).
- Shots (22): s002, s003, s012, s013, s022, s023, s024, s026, s053, s055, s056, s059, s061, s062, s063, s065, s069, s070, s071, s072, s074, s154.

### paddleboard
- What: Doug's **stand-up paddleboard** (The Dive; Doug stands on it and lies back on it).
- Look: Long flat board, side view, pale yellow #f2d36b deck with a thin red stripe, rounded nose to the right, a tiny fin under the tail. Deck (top surface) at y -10. Plain, no text.
- Facing/anchor: Centre anchor. bbox x -300..300, y -25..25 (about 600 x 50).
- Shots (15): s027, s029, s030, s031, s032, s033, s035, s036, s042, s043, s046, s049, s050, s051, s052.

### snow_shovel
- What: Doug's **snow shovel** (The Snow; held in his front hand, then lying on the path with his cap on it).
- Look: Wide square plastic blade in blue #3a6ea5 with a black rim, straight wooden handle with a D-grip. **Anchor (0,0) = the grip** in Doug's front hand (stand pose); the handle runs down-forward and the blade's bottom edge sits at about (+70,+165) so it rests on the ground when Doug holds it at scale 0.55.
- Facing/anchor: Blade to the right (forward). bbox x -30..110, y -20..175 (about 140 x 195).
- Shots (5): s168, s169, s170, s172, s173.

### cardboard_antlers
- What: Doug's **cardboard antler hat** (The Rut: 'purely to blend in'; a hat, **not** a costume).
- Look: Two flat brown-cardboard #c8a06a antler cut-outs with corrugated edge lines and visible tape, stapled to a cardboard headband, tied under the chin with string. Worn prop like `hard_hat`: anchor = Doug's hips, listed after Doug at the same x/y/scale; the band sits on the cap dome at about y -294 so the red cap brim, face and eyes stay fully visible; the antlers spread to about x -170..+170, y -430.
- Facing/anchor: Facing right. bbox x -170..170, y -430..-290 (about 340 x 140).
- Shots (2): s193, s194.

### cardboard_antlers_flat
- What: The cardboard antlers **lying crumpled on the moss** after death 201 (Doug's cap is drawn beside them).
- Look: Same cardboard antlers, flat on the ground, one bent, string loose.
- Facing/anchor: Bottom-centre anchor (ground y=0). bbox x -170..170, y -90..0 (about 340 x 90).
- Shots (1): s196.

### locomotive
- What: A **diesel locomotive in winter**, side view (The Train).
- Look: Generic North-American diesel freight locomotive (no real railway logos): navy #1f3a6b body with a yellow #f2c21b stripe, cab at the front right with windows, big headlight on the nose at about (+470,-250), snow on the roof and plow. **A small whistle/horn on the nose at about (+400,-340)** (the shotlist hangs an icicle from it and points an arrow at it). Wheels on rails at y=0.
- Facing/anchor: Facing right, bottom-centre anchor (rails y=0). bbox x -500..500, y -420..0 (about 1000 x 420).
- Shots (6): s198, s204, s207, s208, s209, s210.

### moose_crossing_sign
- What: Yellow **moose-crossing warning sign** on a post (The Highway; Doug's cap hangs on its right corner the next morning).
- Look: Yellow #ffd21f diamond with a black border and a black moose silhouette, on a grey metal post planted in the ground. Diamond centre at (0,-470), half-diagonal about 150 so the right corner is at (+150,-470). No text.
- Facing/anchor: Bottom-centre anchor (post foot y=0). bbox x -150..150, y -620..0 (about 300 x 620).
- Shots (4): s246, s267, s268, s274.

### small_car_driving
- What: The library `small_car` **driving at night with its window open** (The Highway: Doug singing at the wheel).
- Look: Same footprint, colours and anchor as `small_car` (red hatchback, 360x180, facing right) but: the **side window is an empty opening** (no glass fill, so Doug drawn *behind* the car shows through it; window about x -20..+90, y -150..-95), headlight lit yellow, tail light red, two short motion lines behind. The shotlist adds the headlight beam.
- Facing/anchor: Facing right, bottom-centre anchor (wheel bottoms). bbox x -178..178, y -178..0 (about 356 x 178).
- Shots (2): s271, s272.

### fire_engine
- What: Swedish **fire engine** (firefighters bent the tree down).
- Look: Generic red #d6262b fire truck, side view, ladder on the roof, blue lights, white stripe, no text or real logos.
- Facing/anchor: Facing right (flipped in use), bottom-centre anchor. bbox x -400..400, y -380..0 (about 800 x 380).
- Shots (1): s083.

### hand_saw
- What: A **hand saw** (the neighbours sawed off branches).
- Look: Grey toothed steel blade with a wooden handle, horizontal.
- Facing/anchor: Centre anchor, teeth down. bbox x -150..150, y -55..55 (about 300 x 110).
- Shots (1): s082.

### lake_superior_map
- What: Map of **Lake Superior with Isle Royale highlighted** (The Dive and The Wolves).
- Look: Flat map style like `usa_map`/`north_america_map`: lake in #3a9ad9, land in flat green with a dark outline; Canada along the top/north shore, the US to the south. **Isle Royale** (the long thin island in the north-west of the lake) at about local (-300,-280), filled in a highlight colour (yellow #ffe24a) so it pops. No labels. A clean frame line round the map.
- Facing/anchor: Centre anchor; keep everything inside the bbox. bbox x -600..600, y -400..400 (about 1200 x 800).
- Shots (3): s034, s224, s225.

### newfoundland_map
- What: Map of the **island of Newfoundland** (The Highway).
- Look: Flat green island on ocean #3a9ad9 with its ragged coastline (big north-west peninsula, bays), dark outline, no labels. Gander Bay (north-east coast) at about local (+235,-306) and Howley (west-central interior, by Grand Lake) at about local (-110,0): add a tiny dark dot at each so the shotlist's icons line up. The island should leave room for a 9x6 grid of moose icons over its middle. A clean frame line.
- Facing/anchor: Centre anchor. bbox x -500..500, y -450..450 (about 1000 x 900).
- Shots (7): s249, s250, s251, s252, s253, s254, s255.

### anchorage_map
- What: Map of **Anchorage and the Chugach Mountains** (The Snow: snow pushes moose down the valleys into the city).
- Look: Flat map: Cook Inlet water #3a9ad9 on the left, the city as a grey grid patch in the lower-middle, white-capped Chugach Mountains filling the top and right third with 3 valleys opening down toward the city (the shotlist draws red arrows down them at about local (-140,-350) to (-200,0), (+100,-360) to (0,+100) and (+340,-330) to (+170,+120)). No labels. Frame line.
- Facing/anchor: Centre anchor. bbox x -600..600, y -400..400 (about 1200 x 800).
- Shots (4): s155, s156, s157, s158.

### stadium
- What: A **giant open-air stadium** (enough seats for every Newfoundland moose; 107,601 seats).
- Look: Huge oval bowl seen from a high three-quarter view, grey concrete stands packed with tiny seat dots, green field in the middle, no logos, no team names.
- Facing/anchor: Centre anchor. bbox x -500..500, y -280..280 (about 1000 x 560).
- Shots (1): s256.

## For the graphic designer (thumbnail, s001)
`thumbnail.json` does not exist yet; s001 is `scene_ref: thumbnail` and carries the first 7 words. Proposal A (brief section 3): use `moose_head_on` above as the hero (it is requested at the detailed tier for exactly this), the library `grizzly_bear` small beside it, tiny Doug, "WRONG ANIMAL". If the bear needs a nervous sideways glance, ask the illustrator for a `grizzly_bear` variant; the shotlist doesn't need one.
