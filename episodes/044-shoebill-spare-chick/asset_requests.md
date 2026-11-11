# 044-shoebill-spare-chick: asset requests (director, 2026-11-11)

The shotlist already places these by name, so please keep the **anchor, bounding box and key points** given here:
the generator (`episodes/044-shoebill-spare-chick/build/gen_shotlist.py`) puts other things on those points
(prey in the bill, a cap on the head, Doug's hips on a shell rim). All facing right unless noted. Use the house style:
detailed tier, thick black outlines, flat fills with interior shading. **Never cute**: no big eyes, no smiles, no
nursery pastels (art bible "Never"). Shoebill palette everywhere: slate blue-grey body `#7d8a96` with darker
`#5f6b76` wings/back, paler `#a9b3bb` chest; huge bill pale horn/yellowish `#d8c79a` with grey-brown blotches
and a dark hooked tip; small round **pale yellow-white eye** with a black dot pupil (the stare is the whole joke);
small tuft at the back of the head; long dark grey legs with big feet.

Reused from the library (no request): `croc_egg` (as the shoebill egg, rotated 90), `croc_hatchling` (Nile hatchling),
`boa_constrictor_coiled` (stands in for the African rock python at night), `reeds`, `lilo`, `cat`, `upright_piano`,
`africa_map`, `wait_stopwatch` (used as the clock), `calendar`, `ruler`, `boot` (a man's shoe), `balance_scale`,
`athletics_track`, `case_file_open`, `field_guide_open`, `doug_cap`, `water_splash`, `hippo_underwater`, `small_fish`,
`silver_fish`, `frog`, `turtle_hatchling`, `rat`, `white_duck`, `scientist`, `scientist_woman`, `wildlife_official`,
`stick_man_plain`, `small_table`, `flat_rock`, `bathroom_scale`, `narrator_hand_pencil`, `cardboard_box_open`,
`fire_flames`, `eye_icon`, `dna_strand`, `compact_camera`, `music_note`, `water_weed_draped`, `leaf`, `storm_cloud`.

---

## Shoebill (the star; 7 drawings, all the same bird)

### `shoebill_statue`  (THE STATUE, ~80 shots: the most important drawing in the episode)
Adult shoebill standing dead still, body in 3/4 view, **head turned to face the viewer**, the huge bill pointing
**down onto its chest**, both pale eyes staring straight into the camera. Wings folded, legs straight, feet flat.
It must read as the same unblinking bird in every item, from 0.28 to 1.05 scale.
- Anchor bottom-centre (feet on y = 0). Bbox x -170..170, y -640..0 (head top about -640, bill tip about (0,-430)).
- Shots: every item (s005-s194), full frame in s028-s047.

### `shoebill_side`
Same bird in profile facing right, standing upright, neck in a gentle S, bill held forward and slightly down.
- Anchor bottom-centre (feet). Bbox x -200..+260, y -640..0. Bill tip about (+250,-470).
- **Grip point (+200,-470)**: prey (catfish, croc hatchling, fish + weeds) is drawn on top here, crosswise, so leave
  the bill closed and plain there. **Head-top point (+60,-600)**.
- Also used flipped (facing left) and walking away. Shots: s002, s013-s014, s032, s054-s057, s078-s081, s089,
  s101-s103, s114, s132-s134, s141, s158, s174-s177, s186, s190, s193.

### `shoebill_collapse`
The strike: whole bird pitching forward and down, **wings flung open above the body**, neck straight, bill first into
the water at the right. Legs trailing up-left. Comic, sudden, no prey visible, no blood.
- Anchor (0,0) = waterline under the body centre. Bbox x -380..+380, y -300..+60; bill tip enters the water about (+330,+40).
- Shots: s015-s018, s025, s040, s065, s084, s123.

### `shoebill_looking_down`
Profile facing right, neck bent so the head and **bill point down-forward at the ground/nest** just in front of it,
bill very slightly open. The eye looks down along the bill (never at the viewer: director's note, Water Bucket).
- Anchor bottom-centre (feet). Bbox x -200..+320, y -520..0. **Bill tip (+300,-180)** (water is poured from here),
  **head top (+200,-430)** (a cap is balanced here in s160).
- Shots: s127-s137, s140, s149-s153, s156, s160, s192.

### `shoebill_gulp`
Profile facing right, head tipped straight up, bill pointing at the sky, throat with a cartoon bulge, a small grey
**tilapia tail fin** poking out of the bill tip. Swallowed whole, no blood.
- Anchor bottom-centre (feet). Bbox x -200..+200, y -700..0.
- Shots: s115, s151, s159.

### `shoebill_head_profile`
Big close-up of the head and the whole bill in profile for the size shots. The bill is the hero: shoe-shaped, broad,
with a sharp edge line and a clear **hook at the tip**, blotchy horn colour; small pale eye.
- **Anchor (0,0) = where the top of the bill meets the face.** The bill runs right to the hooked tip at **(+460,+40)**
  and is about 90 units deep (y 0..+90): a 30 cm ruler at scale 1.204 lines up 0-24 cm with it.
- The head sits left of the anchor (x -220..0, y -200..+120); the neck runs down and **ends in a rounded fluffy chest at
  about y +520** (no cut edge, so it can sit mid-frame).
- Shots: s048-s051, s053, s061 (small), s050 (small, podium).

### `shoebill_chick_big`
The older chick: a **big, scruffy, grey downy shape**, sitting in the nest, short bill up and slightly open, begging.
Shoebill-chick-ugly, not cute: lumpy grey fluff `#8f8f8f`/`#a8a8a8`, dark bill, no shine in the eye. (CD: "the older
chick is only a big grey shape".) No pecking, no injury, no second chick in the drawing.
- Anchor bottom-centre. Bbox x -150..150, y -300..0; bill tip about (+30,-300).
- Shots: s146-s163, s164-s194 (many), tally icons at scale 0.16.

### `shoebill_nest`
Flattened platform of trampled reeds and grass at water level, seen low 3/4: wide flat oval top, stems sticking out of
the rim, dark wet underside meeting the water. Must read on hot-day, dusk, night and cream backgrounds.
- Anchor = centre of the top surface. Bbox x -420..420, y -60..+80; eggs and chicks sit on y about -10.
- Shots: ~65 (s002, s003, s056, Water Bucket, First Egg, Spare, tally icons at 0.2).

### `shoebill_egg_hatched`
Bottom half of a chalky white egg (matching `croc_egg`, lightly stained) with a zigzag broken rim, plus the top shell
piece lying beside it to the right.
- Anchor centre. Bottom half x -80..80, **rim at y -60**, base y +110; loose top piece about (+130,+80).
- Doug (in the chick costume) is drawn first with his hips on the rim, the shell in front hides his legs.
- Shots: s188-s190.

## Prey and other animals

### `lungfish`
Marbled lungfish: long eel-like body, olive-brown with darker **marbled blotches**, pale belly, small eye, and the
**thin thread-like paired fins** (two pairs) that make it a lungfish; tail tapers to a point.
- Anchor centre, ~460x110 (x -230..230, y -55..55). Shots: s004, s006, s009-s015, s027, s076, s109, s112-s113.

### `lungfish_cocoon`
Cross-section cutaway of dry cracked mud with a **lungfish curled in a U inside a brown mud cocoon** (oval chamber,
slightly darker lining, a small breathing tube to the top). For the "waiting for rain" beat.
- Anchor centre, ~360x200. Shots: s005-s008.

### `catfish`
Large African sharptooth catfish: long, dark grey-olive back, paler grey sides, **broad flat head with long whisker
barbels**, long dorsal fin, rounded tail.
- Anchor centre, ~520x170 (x -260..260, y -85..85); hold point about (-60,0). Shots: s004, s063, s076, s079-s081.

### `nile_monitor`
Nile monitor lizard, side view on the ground: long and heavy, **dark olive-black with yellow spotted bands**, long
forked tongue optional, strong claws, very long keeled tail to the left. Calm adult.
- Anchor bottom-centre (ground y 0). Bbox x -360..360 (tail to the left), y -150..0. Also used as a black silhouette.
- Shots: s067, s069-s074, s084, s109.

### `water_snake`
Small slim water snake swimming in an S curve, olive-brown with a dark stripe, pale belly, small head facing right.
- Anchor centre, ~380x80. Shots: s072-s076, s109, s112-s113.

### `hamerkop`
Hamerkop: small dull brown wading bird, **hammer-shaped head** (long crest backward balancing a stout dark bill),
medium legs. About 0.4 of the shoebill's height in the shots.
- Anchor bottom-centre, ~260x300. Shots: s061-s062.

## Doug's costumes (worn props: anchor = Doug's hips, listed after Doug at the same x/y/scale; head, face and cap stay visible)

### `lungfish_costume` (stand pose)
Homemade felt lungfish onesie: olive-brown with sewn darker marbling, two pairs of floppy thread fins on the sides, long
tapering felt tail out of the lower back to about (-200,+60). Bbox about x -200..+110, y -180..+90. Shots: s022-s025.

### `catfish_costume` (stand pose, also arms_up)
Grey-olive felt catfish suit, flat felt head-flap over the chest with **long drooping whisker barbels** hanging down,
felt dorsal fin on the back, tail to the left. Bbox about x -200..+110, y -180..+90. Shots: s063-s065.

### `monitor_costume` (stand pose)
Dark olive felt lizard suit with yellow sewn spots, claw mitts, a long felt tail out of the back to about (-300,+100).
Bbox about x -300..+110, y -180..+100. Shots: s082-s084.

### `monitor_costume_empty`
The same lizard suit lying flat and empty on the bank (death beat). Anchor bottom-centre, ~520x90 (x -260..260, y -90..0).
**Tail tip at (-250,-20)**: the cap sits there in s085.

### `croc_hatchling_costume` (sit pose)
Small green felt crocodile-hatchling suit (green `#5f8a3a`, darker sewn scute bands, felt snout visor on the chest,
stubby legs, tail out to the left to about (-300,+80)). Not white (that is the 2025 white alligator suit).
Bbox about x -300..+110, y -180..+80. Shots: s121-s123.

### `croc_hatchling_costume_empty`
The same suit lying empty on the bank. Anchor bottom-centre, ~420x110 (x -210..210, y -110..0); **cap point (0,-110)**. Shot: s124.

### `tilapia_costume` (stand pose)
Grey-silver felt tilapia (a deep-bodied perch-like fish) suit with faint vertical bars, spiny felt dorsal fin on the
back, fan tail to the left. Bbox about x -200..+110, y -180..+90. Shot: s158.

### `shoebill_chick_costume` (stand pose)
Doug's grey, scruffy, **deadpan** shoebill-chick suit: lumpy grey felt fluff body, a short felt chick bill on the chest
(not over the face), no cute features. Bbox about x -120..+100, y -180..+100. Shots: s188-s190.

## Props

### `floating_mat`
Floating mat of tangled grass, papyrus stems and weed in open water, flat-topped, ragged edges, a few drips and
ripples round it. Must look like it could hold a 5 kg bird and not an 80 kg man.
- **Anchor = centre of the top surface on the waterline (0,0).** Bbox x -330..330, y -40..+30; standing surface y -20.
- Shots: s066, s086-s105 (19 shots).

### `wooden_spoon`
Plain wooden kitchen spoon, horizontal, bowl to the right. Anchor centre, ~220x50. Shots: s064, s066.

### `garden_hose_claws`
A coiled green garden hose lying on a lawn with **small lizard claws** along it and one end turned up as a head with
an **annoyed face** (heavy lid, flat mouth). Anchor bottom-centre, ~520x200. Shot: s077.

### `wooden_clog`
A big wooden shoe (Dutch clog), pale wood, side view, toe right. Anchor bottom-centre, ~360x160. Shot: s051.

### `watering_can`
Classic metal garden watering can, side view, spout to the right with a rose. Anchor bottom-centre, ~300x220. Shots: s135-s136.

### `spare_tyre_boot`
Rear view of a small car with the boot open, a **spare tyre** lying in the boot well. Leave clear space at the
lower right of the tyre for a grey "IN CASE" tag (we overlay it at about (+250,+160)). Anchor centre, ~640x420.
Shots: s169-s170.

## Exact shot usage (generated from shotlist.json; this list wins over the shot numbers above)
- `catfish`: s004, s063, s076, s079, s080, s081
- `catfish_costume`: s063, s064, s065
- `croc_hatchling_costume`: s121, s122, s123
- `croc_hatchling_costume_empty`: s124
- `floating_mat`: s066, s086, s087, s088, s089, s091, s096, s097, s098, s099, s100, s101, s102, s103, s104, s105, s106
- `garden_hose_claws`: s077
- `hamerkop`: s061, s062
- `lungfish`: s004, s006, s009, s010, s011, s012, s014, s015, s027, s076, s109, s112, s113
- `lungfish_cocoon`: s005, s006, s007, s008
- `lungfish_costume`: s022, s023, s024, s025
- `monitor_costume`: s082, s083, s084
- `monitor_costume_empty`: s085
- `nile_monitor`: s067, s069, s070, s071, s073, s074, s084, s109
- `shoebill_chick_big`: s147, s148, s149, s150, s152, s153, s155, s156, s157, s160, s161, s162, s163, s164, s165, s166, s171, s172, s173, s174, s176, s177, s178, s179, s184, s185, s188, s189, s190, s192, s193, s195
- `shoebill_chick_costume`: s188, s189, s190
- `shoebill_collapse`: s015, s016, s017, s018, s025, s040, s065, s084, s123
- `shoebill_egg_hatched`: s188, s189, s190
- `shoebill_gulp`: s115, s151, s159
- `shoebill_head_profile`: s048, s049, s050, s051, s053, s060
- `shoebill_looking_down`: s127, s128, s129, s130, s135, s136, s140, s149, s150, s152, s156, s160, s192
- `shoebill_nest`: s002, s003, s056, s117, s118, s119, s125, s126, s127, s128, s129, s130, s131, s132, s133, s134, s135, s136, s137, s138, s139, s140, s141, s142, s143, s144, s145, s146, s147, s148, s149, s150, s152, s154, s155, s156, s157, s160, s161, s162, s163, s164, s165, s166, s171, s172, s173, s174, s176, s177, s178, s179, s187, s188, s189, s190, s192, s193
- `shoebill_side`: s002, s013, s014, s019, s032, s054, s055, s056, s079, s080, s081, s089, s101, s102, s103, s114, s132, s133, s134, s141, s158, s174, s176, s177, s186, s190, s193
- `shoebill_statue`: s005, s006, s007, s008, s009, s010, s011, s012, s020, s021, s022, s023, s024, s027, s028, s029, s030, s031, s033, s034, s035, s037, s038, s040, s041, s042, s043, s044, s045, s046, s047, s061, s062, s063, s064, s067, s069, s070, s071, s075, s076, s078, s082, s083, s086, s087, s088, s090, s091, s094, s095, s096, s097, s098, s099, s100, s106, s107, s108, s113, s120, s123, s125, s132, s144, s145, s146, s164, s165, s166, s181, s182
- `spare_tyre_boot`: s169, s170
- `tilapia_costume`: s158
- `water_snake`: s072, s073, s075, s076, s109, s112, s113
- `watering_can`: s135, s136
- `wooden_clog`: s051
- `wooden_spoon`: s064, s066
