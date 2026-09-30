# Asset requests: 002 Every Parasite

From the director, for the illustrator (art director approves). House style per `assets/library/anglerfish.json` and
`channel/art_bible.md`: creatures and props are the detailed tier (outlines 4-6, flat fills plus `spray` shading,
darker back, lighter belly, white eyes with black pupils), **facing right**, local coordinates centred on the anchor.
Sizes are local units at scale 1. **Anchors matter**: every drawing was placed in `shotlist.json` by the anchor
described below (I previewed the layout with placeholder boxes, so wrong anchors will put things in the sky).

## Gore watch (brief section 8): read this first
Parasites are body horror by nature. Everything here is cartoon or **textbook-diagram** level:
- **Never** draw anything entering, leaving or growing inside a body: no emerging worms, no larva on or in a host,
  no cysts, no organs, no brains, no blood. "Inside the host" beats are drawn by me as a dotted line on a plain
  silhouette (`body_outline`, `head_outline`, or a creature asset with `"silhouette": true`).
- The four watch items are **diagram-simple**: the jewel wasp larva (I draw it inline as a plain cream bean with 3
  segment ticks, no request), `horsehair_worm` (a loose tangle on its own, never next to or coming out of a cricket),
  the raccoon roundworm (no worm drawing at all: eggs are plain ovals, drawn inline), `naegleria_amoeba` (a textbook
  cell, no face, no teeth).
- Single-celled parasites (`toxoplasma_cell`, `trypanosome`, `naegleria_amoeba`, `red_blood_cell`) and `cercaria`,
  `blood_flukes`: microscope-diagram look (pale translucent fills, a nucleus dot, thin outlines 3-4), not monsters.
- Kid-appeal: no big cute eyes or smiles on creatures, no pastel nursery palette. Deadpan nature-documentary cartoon.

Priority A = hero or recurring, B = supporting, C = one-off prop. SIL = also shown as `"silhouette": true`, so the
outer outline must be a clean recognisable shape.

## Doug's costumes (act 1). Props worn over the rig, like `squid_costume`
Anchor (0,0) = **Doug's hips** at Doug scale 1 (rig: head centre (0,-218) r72, cap top about y=-300, cap brim points
right to x=+126, shoulders (0,-122), feet at y=+150). The costume covers the torso roughly y=-140..+70 and x=-80..+80,
leaves the **head, face and red cap fully visible** and the lower legs visible. Headband extras (antennae, ears, eye
stalks) sit **behind** the cap and poke out above/around it without covering the face. Premium-onesie look (fabric
suit with a visible front zipper), not cardboard, so it differs from the squid gag. Each one is also used
**rotated -90 lying flat** for a death (and the rat one lying empty on the floor), so it must still read sideways.
Used on poses stand, walk1/2, arms_up, point, wave, shrug, cower, sit, lie (the rig lowers the body for sit/cower;
I offset the costume, you don't need to).

### cockroach_costume (A)
- **What:** Doug's cockroach onesie (item 1, Jewel Wasp; also the opener costume fitting).
- **Look:** glossy reddish-brown (`#7a3b1a`, highlight `#a8582b`) oval body shell with a centre wing-seam line and a
  zipper; paler tan pronotum collar around the neck; 4 thin spiny brown extra legs sticking out of the sides (2 per
  side); 2 very long thin antennae from a headband behind the cap, curving up and back to about y=-420.
- **Shots:** s003 (held by the scientist, rotated), s004, s005, s006, s007, s009, s012-s025. s025 lying dead (rotated -90).

### ant_costume (A)
- **What:** carpenter-ant onesie (item 2, Zombie Ant Fungus).
- **Look:** near-black (`#2a1f1a`, sheen `#4a3a30`) three-part body: slim thorax over the torso, a big round gaster
  (abdomen) bulb sticking out behind the hips to the left (x -150, y 0), 4 thin jointed extra legs, 2 elbowed antennae
  from a headband, zipper. Must read on the jungle greens (`#2e8b3a`, `#cfe9a8`).
- **Shots:** s005, s026-s044.

### cricket_costume (A)
- **What:** field-cricket onesie (item 3, Horsehair Worm).
- **Look:** glossy black-brown (`#2b2118`, highlight `#5a4632`), long folded wings down the back like a cape, two big
  bent jumping hind legs at the sides (the cricket giveaway), 2 very long thin antennae swept back from a headband,
  zipper. Must read on night navy (`#1b2a4a`) too: add a lighter rim highlight.
- **Shots:** s005, s046, s048, s050-s058, s060, s062-s065 (s064/s065 sitting on a sun lounger).

### snail_costume (A)
- **What:** amber-snail costume with the parasite's eye stalks (item 4, Green-Banded Broodsac).
- **Look:** honey-amber spiral shell worn like a backpack behind the torso (centre about (-90,-40), ~170 across),
  pale yellow-grey body suit, and **two fat eye stalks** rising from a headband behind the cap to about y=-400, each
  striped in bright green / white / dark green bands (`#6fdc3a`, `#ffffff`, `#1f6b1a`) like the real broodsac. No
  eyes on the stalk tips. I add the disco glow with spray.
- **Shots:** s005, s067, s069-s071, s073, s074, s076, s078, s081, s083-s087 (s087 lying dead on a leaf).

### rat_costume (A)
- **What:** brown-rat onesie (item 5, Toxoplasma; the bridge item).
- **Look:** grey-brown fur suit (`#8a7a6a`, lighter belly `#c9b9a6`) with a hood around the face (face stays visible),
  two round pink-lined ears on the hood beside the cap, pink paws, a long pink segmented tail from the back curling to
  about (-220,+120), zipper.
- **Shots:** s005, s088, s089, s093-s095, s097, s099, s100, s103-s108, s109 and s111 (empty costume lying on the
  floor, rotated -90).

### doug_sunglasses (C)
- **What:** black cartoon sunglasses for Doug at the lake (item 6 stage direction).
- **Look:** two dark lenses (fill `#111`, small white glint) centred on Doug's eyes at **(6,-220) and (38,-220)**,
  lens ~34x28 each, thin bridge between, one arm running back to the head edge at x=-70. Nothing else.
- **Anchor:** Doug's hips (standing rig); I shift it for the sit pose. **Shots:** s126.

## Creatures: act 1

### jewel_wasp (A)
- **What:** emerald cockroach wasp (*Ampulex compressa*), item 1 hero. SIL-friendly.
- **Look:** metallic blue-green body (`#1f9e7a` / sheen `#6fe0c0`, darker `#0e5c49`), slim; the **middle and hind
  thighs bright red-orange** (`#d9451f`), thin wasp waist, clear wings folded over the back, long curved antennae,
  small stinger at the back end.
- **Anchor:** centre, ~380 long x 170 tall, facing right. **Shots:** s006-s011, s015-s017, s019, s024, s025, s217, s229.

### cockroach (A)
- **What:** a real American cockroach, side view (the explanation diagrams in item 1).
- **Look:** reddish-brown glossy body, ~420 long x 160 tall, **head at the right end x +170..+210** (small, tucked
  under the shield), **pronotum shield (thorax) x +60..+160** with a paler rim, wings/abdomen x -210..+60, 6 spiny
  legs (front legs attached near (+110,+40)), and **2 very long antennae** rising up and forward from the head to
  about (+260,-230) (they get "clipped" by a red dotted line in s016).
- **Anchor:** centre, facing right. **Shots:** s008, s010, s011, s016 (at scale 1.9-2.2, so keep detail clean).

### burrow (B)
- **What:** the wasp's burrow entrance on the ground.
- **Look:** low mound of brown earth (`#8a5a2b`) with a dark round entrance hole on its right side, a few pebbles
  and a twig. ~500 x 220. **Anchor:** bottom-centre (ground line). **Shots:** s015, s017.

### carpenter_ant (A)
- **What:** carpenter ant (*Camponotus*), item 2. Also shown SIL (with my yellow dotted fungus network on top).
- **Look:** black with a red-brown tint (`#2a1f1a` / `#5a2e1e` highlights), big head with visible mandibles at the
  right, elbowed antennae, narrow waist, big rounded gaster at the left, 6 thin legs. **Diagram-clean silhouette.**
- **Anchor:** centre, ~360 x 180, facing right. **Shots:** s026, s027, s029, s030, s034, s036, s038-s040, s045, s217.

### leaf (A)
- **What:** a big rainforest leaf seen from below, horizontal (the ant's "death grip" leaf; also broodsac and cricket food).
- **Look:** mid-green (`#3f9b3a`, lighter underside `#6cc15a`), pointed tip at the right, short stem at the left,
  a **thick pale main vein** along the centre and side veins.
- **Anchor:** centre, ~600 x 220. **Shots:** s033, s036, s042-s045, s049, s070, s077, s079 (often `flip`).

### small_plant (A)
- **What:** a small plant/seedling that ants and snails climb.
- **Look:** thin green stem with 4-5 alternating leaves, the **top leaf flat and horizontal at about y=-540** (Doug
  the snail sits on it). ~220 x 560. **Anchor:** bottom-centre (ground).
- **Shots:** s032, s034, s035, s041, s042, s080, s081, s085-s087.

### rainforest_tree (B)
- **What:** framing tree for the Thai rainforest scenes (placed at the left and right edges, one flipped).
- **Look:** tall grey-brown trunk with buttress roots, a dark green crown (`#1d5e27` / `#2e8b3a`) at the top
  (y -900..-600), two hanging lianas. ~420 x 900. **Anchor:** bottom-centre. **Shots:** s026-s045 (every jungle shot).

### fungus_stalk (B)
- **What:** the Ophiocordyceps fruiting stalk, drawn **on its own**, standing on the leaf. No ant body attached (gore
  rule: nothing growing out of a body).
- **Look:** thin wiry tan-brown stalk (`#a0703a`), slightly curved, with a small swollen orange-brown capsule near the
  top. ~60 x 260. **Anchor:** bottom-centre (base). **Shots:** s045.

### clock (B)
- **What:** round analogue wall clock showing **12 o'clock** (noon and midnight).
- **Look:** white face, red rim, black numbers 12/3/6/9 only, both hands straight up. ~220 diameter.
- **Anchor:** centre. **Shots:** s032, s042, s141, s145, s195, s204, s208, s210.

### horsehair_worm (A)
- **What:** a free-living adult horsehair (Gordian) worm in water, item 3. **Diagram-simple, on its own.**
- **Look:** one long thin (6-8 px) dark brown worm (`#5a3e26`) in loose loops with one clear knot, both blunt ends
  visible, no face, no segments or interior. ~420 x 300.
- **Anchor:** centre. **Shots:** s046-s048, s052, s061, s217.

### field_cricket (A)
- **What:** a real field cricket, side view. Also SIL (s050).
- **Look:** glossy black-brown, round head, very long antennae, wings folded flat on the back, **big jumping hind
  legs**, two cerci at the tail. ~300 x 150. **Anchor:** centre, facing right. **Shots:** s049, s050, s053, s059.

### matchbox_charger (C)
- **What:** the scale analogy: 30 cm of phone-charger cable coiled inside a matchbox.
- **Look:** an open matchbox (drawer pulled out, red/yellow label) stuffed with neat white coils of charger cable, a
  USB plug end hanging over the edge. ~360 x 240. **Anchor:** centre. **Shots:** s055.

### swimming_pool (B)
- **What:** hotel swimming pool (night scene), also small in the "where it turns up" montage.
- **Look:** rectangular pool in a low 3/4 view: pale tiled coping, glowing turquoise water with light ripples, a chrome
  ladder at one end. ~700 x 220. **Anchor:** centre. **Shots:** s047, s064-s066.

### sun_lounger (B)
- **What:** white hotel sun lounger, side view.
- **Look:** white slatted plastic, back rest raised at the left, short legs. ~380 x 160, **seat surface at about
  y=-50**. **Anchor:** bottom-centre (legs on the ground). **Shots:** s064-s066.

### amber_snail (B)
- **What:** a healthy amber snail (*Succinea*), item 4.
- **Look:** elongated translucent honey-amber shell (`#d9a441`, highlight `#f2cf7a`), pale yellow-grey body, two
  short thin eye tentacles. ~260 x 160. **Anchor:** bottom-centre (foot on ground), facing right.
- **Shots:** s068, s070, s077, s079.

### broodsac_snail (A)
- **What:** the same snail infected with Leucochloridium (the famous look), item 4.
- **Look:** as `amber_snail`, but the two eye tentacles are **swollen fat and thumb-shaped**, striped in bright green /
  white / dark green bands (`#6fdc3a`, `#ffffff`, `#1f6b1a`), tips at about (+110..+150, -150..-220). Cartoon, clean,
  no gore. ~280 x 230. **Anchor:** bottom-centre. **Shots:** s067, s069, s071-s073, s075, s080-s082.

### songbird (A)
- **What:** a small songbird (the broodsac's next host; also "birds" in the Toxoplasma host list). SIL (s076, s087).
- **Look:** robin-like: brown back and wings, rusty-orange breast, short pointed beak, perched pose. ~300 x 220.
- **Anchor:** centre, facing right. **Shots:** s068, s075-s077, s086, s087, s091, s092.

### caterpillar (C)
- **What:** plump green caterpillar (what the bird thinks it sees).
- **Look:** chubby green body with lighter bands, small dark head, stubby legs. Not cute, no smile. ~300 x 110.
- **Anchor:** bottom-centre. **Shots:** s069.

### toxoplasma_cell (A)
- **What:** *Toxoplasma gondii* tachyzoite, microscope-diagram style, item 5.
- **Look:** crescent/banana-shaped single cell, pale lilac translucent (`#d9c3f0`, outline `#6a3aa8`), one darker
  round nucleus, a slightly pointed "cap" at one end. ~360 x 180. **Anchor:** centre.
- **Shots:** s088, s089, s094, s097, s217.

### rat (A)
- **What:** a brown rat (the Berdoy experiment animal).
- **Look:** grey-brown fur, paler belly, pink ears, nose and feet, long pink tail. ~380 long (with tail) x 150.
- **Anchor:** bottom-centre, facing right. **Shots:** s091, s092, s096, s098-s102 (small, inside a pen diagram too).

### cat (A)
- **What:** large orange tabby cat, sitting (Toxoplasma's only sexual host; also "pets").
- **Look:** orange with darker tabby stripes, white chest, green eyes, tail wrapped round the front paws. Calm,
  unimpressed, a real predator (not cute). ~300 x 380. **Anchor:** bottom-centre, **facing right** (I flip it).
- **Shots:** s061, s093-s095, s104, s105, s107, s108, s229.

## Creatures and diagrams: act 2 (Doug as himself, darker redder backgrounds `#e9a48c` to `#3d0f18`)

### blood_flukes (A)
- **What:** adult *Schistosoma* pair, textbook diagram, item 6.
- **Look:** a thicker pale cream-pink male worm curved into a C, with a groove along his body holding a thinner, darker
  (`#7a4a5a`) female lying inside it. Smooth, simple, two small suckers at the male's front end. ~420 x 180.
- **Anchor:** centre. **Shots:** s110, s115, s118-s121.

### freshwater_snail (C)
- **What:** freshwater snail host (ramshorn / *Biomphalaria* type).
- **Look:** flat disc-coiled dark brown shell, grey body, 2 thin tentacles. ~220 x 150. **Anchor:** centre, facing right.
- **Shots:** s113 (underwater, on `#4a86a8`).

### cercaria (B)
- **What:** the free-swimming larva of the blood fluke, diagram.
- **Look:** small oval pale translucent body with a long tail that **forks into a Y** at the end. ~200 x 90.
- **Anchor:** centre, facing right. **Shots:** s113 (8 small copies), s114.

### body_outline (A)
- **What:** generic front-view human outline for all "inside the body" beats (dotted paths are mine).
- **Look:** medical-diagram silhouette: light grey fill (`#e6e6e6`), 4 px dark grey outline, arms slightly away
  from the body, **no face, no organs, no features**. ~300 x 760, navel at (0,0), head top at y=-380, feet at +380.
- **Anchor:** centre. **Shots:** s112, s115, s123, s124, s139, s159, s182, s183, s197, s198.

### head_outline (A)
- **What:** side-profile head diagram facing right (malaria brain, raccoon roundworm eyes, amoeba smell nerve).
- **Look:** grey fill, dark grey outline, a small ear, **nose tip at about (+230,+20)**, a small eye dot at about
  (+150,-40), skull top at y=-260, short neck at the bottom. **No brain, no interior.** ~460 x 520.
- **Anchor:** centre. **Shots:** s166, s184, s186, s225, s227.

### kissing_bug (A)
- **What:** triatomine "kissing bug", item 7. SIL-friendly.
- **Look:** dark brown-black elongated body, **orange-red stripes along the flattened abdomen edges**, long narrow
  cone-shaped head with a thin beak folded under, thin legs, antennae. ~340 x 160.
- **Anchor:** centre, facing right. **Shots:** s130-s135, s147.

### trypanosome (A)
- **What:** trypanosome single cell (used for both *T. cruzi* and *T. brucei*), microscope diagram. SIL (s148).
- **Look:** long wavy leaf-shaped cell, pale purple (`#cdb3ec`, outline `#6a3aa8`), an undulating fin along one side,
  one whip-like flagellum at the front, a nucleus dot. ~360 x 120. **Anchor:** centre.
- **Shots:** s135, s139, s148, s195, s196, s209.

### bed (B)
- **What:** Doug's bed, side view.
- **Look:** wooden frame, **mattress top at y=-150**, white pillow at the left end, a blue blanket. ~600 x 300.
- **Anchor:** bottom-centre (floor). **Shots:** s133, s136, s146.

### calendar (A)
- **What:** tear-off page calendar (time passing; I overlay labels like "3 MONTHS", "APRIL 14").
- **Look:** red top binding with 2 rings, a big **blank white page** (keep the centre y -40..+80 empty for my label),
  a curled page corner. ~260 x 300. **Anchor:** centre. **Shots:** s051, s120, s138, s140, s146 (5 flying pages), s180,
  s204, s238.

### heart_icon (B)
- **What:** simple red cartoon heart (valentine) symbol.
- **Look:** bright red, one white shine, thick outline. ~200 x 180. **Anchor:** centre.
- **Shots:** s063, s065, s100, s107, s131, s143.

### library_book (C)
- **What:** overdue library book (the Chagas "library fine" analogy).
- **Look:** dusty hardback, a "LIB" spine sticker, a due-date card sticking out of the top. ~300 x 360.
- **Anchor:** centre. **Shots:** s144.

### mosquito (A)
- **What:** female *Anopheles* mosquito, item 8.
- **Look:** slender dark grey-brown body, **spotted wings**, long thin legs, long straight proboscis, the typical
  Anopheles resting posture with the abdomen tilted up. ~340 x 240. **Anchor:** centre, facing right. Also used tiny
  (scale 0.2) on Doug's arm, so the shape must survive at 70 px.
- **Shots:** s151-s157, s159, s168, s169, s217, s229.

### fly_swatter (C)
- **What:** red plastic fly swatter. ~120 x 420 (mesh head at the top). **Anchor:** centre. **Shots:** s153.

### red_blood_cell (A)
- **What:** red blood cell, diagram.
- **Look:** red disc (`#d9322b`) with a darker centre dimple, 3/4 view, simple highlight. ~240 across.
- **Anchor:** centre. **Shots:** s160, s161, s164, s165.

### hammock (B)
- **What:** hammock strung between two palm trunks (Doug's malaria nap).
- **Look:** striped canvas hammock sagging in the middle, ropes to two short palm trunks at x=±360. **Anchor:** centre
  of the hammock bed (Doug lies on it at about (0,-30)). ~800 x 400. **Shots:** s168, s169.

### raccoon (A)
- **What:** raccoon ("Buddy"), item 9.
- **Look:** grey fur, black eye mask, pale muzzle, ringed black/grey tail, on all fours, side view. **Top of the head
  at about (+150,-200)** (Buddy wears Doug's cap there in s191). ~420 x 260. **Anchor:** bottom-centre (feet), facing
  right. **Shots:** s173-s176, s178, s179, s181, s189-s192, s229.

### house (B)
- **What:** small suburban house (raccoons live "right next to houses").
- **Look:** white walls, red roof, door, one window, a trash can beside it. ~500 x 420.
- **Anchor:** bottom-centre. **Shots:** s173, s174, s179.

### tsetse_fly (A)
- **What:** tsetse fly, item 10.
- **Look:** brown-grey fly, wings folded flat over the back like **closed scissors**, long forward-pointing proboscis,
  striped abdomen. ~320 x 180. **Anchor:** centre, facing right. **Shots:** s193-s195.

### lab_mouse (C)
- **What:** white lab mouse (the body-clock study). Pink ears, nose and tail. ~260 x 120.
- **Anchor:** bottom-centre, facing right. **Shots:** s208.

### podium (B)
- **What:** wooden lectern with a microphone (Doug's speech).
- **Look:** brown wood, slanted top, mic on a gooseneck. **~300 x 260** (short: Doug stands behind it and must show
  from the chest up). **Anchor:** bottom-centre. **Shots:** s211, s212.

### airplane (C)
- **What:** small passenger jet, side view (jet lag). ~500 x 180. **Anchor:** centre, facing right. **Shots:** s201.

### naegleria_amoeba (A)
- **What:** *Naegleria fowleri*, item 11 (the boss). Diagram-style single cell. SIL (s216, s218, then full reveal).
- **Look:** irregular blob with 2-3 rounded lobes (pseudopods), pale lilac-grey translucent (`#d9c9e6`, outline
  `#5a3a7a`), one dark nucleus with a central dot, a few granules. **No face, no teeth.** The silhouette must still
  read as a lumpy cell. ~360 x 280. **Anchor:** centre. **Shots:** s216, s218, s219, s221, s222, s230.

### jetty (B)
- **What:** wooden lake jetty, side view (Doug's cannonball).
- **Look:** plank deck spanning x -250..+250, **deck top surface at y=-30**, posts down to y=+130 into the water.
- **Anchor:** centre. **Shots:** s240-s243.

### usa_map (B)
- **What:** simple contiguous-US map (Toxoplasma carriers, Naegleria cases, "southern states").
- **Look:** flat green fill, dark outline, faint state lines, no labels. ~1000 x 600. **Anchor:** centre.
- **Shots:** s090, s233, s237 (I draw a red ellipse over the southern band at about y=+170).

### toddler (C)
- **What:** crude-tier stick toddler (the "toddler walking a sofa" analogy), Doug's tier, `"auto_ink": true`, no cap.
- **Look:** big round head, short body, tiny t-shirt, one arm forward holding the end of a leash (I draw the leash from
  about (-60,-180) at scale 1). ~260 tall. **Anchor:** bottom-centre (feet), facing **left** toward the sofa.
- **Shots:** s018.

## Reused from the library (no request)
`scientist`, `sofa`, `phone`, `gravestone`, `doug_cap`, `world_map`, `thermometer`, `thumbs_up_hand`, `tv_remote`,
`suitcase`, `question_mark`, `exclamation_mark`, `warning_triangle`, `red_x`. Drawn inline in the shotlist: eggs,
the diagram larva, paperclip, burrow interior, ruler, pet bowl, petri dish, pen diagram, charts.
