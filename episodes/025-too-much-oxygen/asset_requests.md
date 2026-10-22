# 025-too-much-oxygen: asset requests (director to illustrator / art director)

Library assets reused as they are (checked first, per the brief): `meganeura` (all griffinfly shots; also the 19 cm modern relative at 0.27),
`arthropleura` (boss, thumbnail creature, cap rides on its back in s254), `scale_tree` (coal-forest backdrop, fallen trunks rotated 78-85,
the treetop drop in s143 at 1.6), `fern`, `tape_measure` (HUD icon at 0.16, and the tape beside Doug in s193), `time_machine`,
`time_machine_closed`, `fallen_log`, `bowling_pin`, `cat`, `travel_suitcase` (the carry-on), `front_door`, `small_car`, `water_glass_empty`
(the household spider glass, upturned with `rotate: 180`), `water_splash`, `campfire`, `matchbox`, `doug_cap`, `insect`, `hynerpeton`
(East Kirkton's early four-legged animals), `crocodile_skull`, `croc_eyes_water`, `giant_moray`, `small_fish`, `falcon`, `songbird` /
`bat_hanging` / `rhamphorhynchus` (as black silhouettes, "no birds, no bats, no flying reptiles"), `scientist`, `classic_museum`
(Prague and the NHM), `journal_paper`, `crt_tv` (the scan screen), `magnifying_glass`, `glass_jar`, `library_book`, `calendar`,
`thermometer`, `microbe`, `worm_icon` (small invertebrates in the mud), `leaf`, `moss_patch`, `boulder`, `dorset_cliff` (stand-in
sandstone cliff at Howick Bay), `paper_crown` (on Arthropleura: "the biggest bug"), `heart_icon`, `dust_plume`, `narrator_hand`,
`world_map`, `pangaea_map`, `britain_map`, `usa_map`, `question_mark`, `exclamation_mark`, `warning_triangle`, `red_x`.
`jaekelopterus` is **not** reused: Megarachne and Hibbertopterus must not look like it (brief section 7).

Drawn from primitives in the shotlist (no asset needed): the AIR TODAY / AIR THEN pie charts, the oxygen and biggest-insect line chart,
coal-seam and peat cutaways, the Kentucky coal-bed stack, the fire/charcoal/buried loop, the drinking straw, the fern-stem cross-section
with beak holes and scar rings, the gills-to-book-lungs diagram, the fanning book plates, the garden rake, garden-pond tadpoles, the
1980 museum card, the MENU card, the flight-muscle block, the DOUG FOR SCALE panel (vertical 0-3 m tape, red reading line, dashed
"2 TO 3 M?" bracket) and the HUD reading label.

House rules (brief section 7, art bible): detailed cartoon tier, thick black outline (5-6), flat fills with interior spray shading,
readable at phone size. **Bugs must read as real and heavy, never cute or mascot-like**: no smiles, no big shiny eyes, no bright toy
colours. Everything faces right unless noted (the shotlist flips). No gore anywhere: no stings, bites or piercings shown on contact.
Several creatures are used as black silhouettes (with red glow, or a red `rim` underwater), so each outline alone must read as that
animal. Please keep to the anchor and bbox given: the shotlist was laid out against them.

## Creatures

### bojophlebia
- **DONE** (illustrator, 2026-10-22): `assets/library/bojophlebia.json`, preview `assets/previews/025-too-much-oxygen-assets.png`
- What: Bojophlebia prokopi, a giant Carboniferous winged insect (an early relative of mayflies and dragonflies, NOT a modern mayfly).
- Look: Top view in flight, like a pinned specimen: **four broad, rounded, fairly equal wings** (pale smoky grey-brown #d8d0bc with
  darker cross-veins, a little darker at the bases), a stout dark brown segmented body, short head with two small dark eyes and short
  antennae, **two long thin tail filaments** (cerci). Must read clearly different from `meganeura` (broader, rounder wings, browner,
  tail filaments, no metallic blue). Used greyed (`ink: #4a4a4a`) as a fossil on a rock slab too.
- Facing/anchor: Head up-right like `meganeura` (body tilted about 20 degrees). Centre anchor (thorax). bbox about x -210..210,
  y -150..170 (420 wingspan).
- Shots (17): s032, s033, s036, s038, s039, s040, s041, s042, s044, s046, s047, s049, s050, s051, s060, s061, s064.

### megarachne_spider_1980
- **DONE** (illustrator, 2026-10-22): `assets/library/megarachne_spider_1980.json`, preview `assets/previews/025-too-much-oxygen-assets.png`
- What: The 1980 interpretation of Megarachne: a huge hairy spider (museum model / old reconstruction). Shown, then stamped with a red X.
- Look: Top-down, tarantula-like: big round dark brown abdomen at the back, broad cephalothorax, two prominent fangs at the front,
  eight thick hairy banded legs (dark brown #4a3424 with lighter bands), hair strokes. Heavy and creepy, not cute. Also drawn in
  pale cyan ink as an "X-ray" (`ink: #9fe6ff`), so keep the outline clean.
- Facing/anchor: Head to the right. Centre anchor, bbox about x -250..250, y -230..230.
- Shots (12): s067-s076, s078, s079.

### megarachne
- **DONE** (illustrator, 2026-10-22): `assets/library/megarachne.json`, preview `assets/previews/025-too-much-oxygen-assets.png`
- What: Megarachne servinei as it really was: a **short, broad freshwater sea scorpion** (eurypterid).
- Look: Top view: a wide, rounded, almost circular head shield with two small eyes near the front, a short broad body of a few wide
  segments, **no long tail spike** (stubby), front limbs carrying **comb-like blades** (rakes) held forward, a couple of walking legs.
  Dull mud brown #6b5235 with darker back. Clearly not `jaekelopterus` (no long body, no pincers, no paddles). Also used as a fossil
  (`ink: #4a4a4a`) and as a black silhouette in the shallows.
- Facing/anchor: Head to the right. Centre anchor, bbox about x -260..240, y -190..190.
- Shots (12): s065, s077, s078, s080-s086, s088, s089.

### giant_tarantula
- **DONE** (illustrator, 2026-10-22): `assets/library/giant_tarantula.json`, preview `assets/previews/025-too-much-oxygen-assets.png`
- What: The largest living spider, the South American giant tarantula (Theraphosa), for the "about thirty" comparison.
- Look: Top-down, hairy brown-pink tarantula, rounded abdomen, eight thick legs. Same top-down style as `megarachne_spider_1980` but
  smaller and lighter (#8a6650), so the two read side by side.
- Facing/anchor: Head to the right. Centre anchor, bbox about x -300..300, y -280..280 (drawn at 0.42 next to the 1980 spider at 0.7).
- Shots (1): s073.

### mazothairos
- **DONE** (illustrator, 2026-10-22): `assets/library/mazothairos.json`, preview `assets/previews/025-too-much-oxygen-assets.png`
- What: Mazothairos enormis, a palaeodictyopteran ("The Beak"): a big Carboniferous insect with a piercing beak.
- Look: Side-top 3/4 view, wings spread flat: **long, straight, narrow wings** with bold dark bands/spots (palaeodictyopteran wing
  pattern, browns and cream), heavy body, small head with a **long, stiff, pointed beak angled down and forward under the head** (the
  key feature; it is pointed at with a red arrow in a 1.3x close-up), short antennae. **No extra winglets** on this one (the script
  doesn't give them to Mazothairos). It perches on Doug's leaf hat in s112-s113, so the legs should hang down to about y +60.
- Facing/anchor: Facing right. Centre anchor, bbox about x -300..300, y -140..80 (beak tip around (+250,+50)).
- Shots (12): s090, s092, s093, s096, s097, s099, s102, s103, s111, s112, s113, s114.

### six_winged_insect
- **DONE** (illustrator, 2026-10-22): `assets/library/six_winged_insect.json`, preview `assets/previews/025-too-much-oxygen-assets.png`
- What: Diagram of a generic palaeodictyopteran showing the **small extra flaps (prothoracic winglets)** in front of the wings.
- Look: Top view, head pointing **up**: thorax centre at (0,-60), head at (0,-160) with a short beak, abdomen down to y +260. Forewings
  out to the upper left/right (tips about (±330,-150)), hindwings below them (tips about (±330,+20)), and two **small rounded flaps** right
  behind the head at about (±85,-90). The shotlist pops red numbers 1-6 at about (±236,-164), (±309,0), (±91,-82), so keep those spots on
  the wings/flaps. Same banded wing style as `mazothairos`.
- Facing/anchor: Head up. Centre anchor, bbox about x -340..340, y -200..270.
- Shots (2): s094, s095.

### pulmonoscorpius
- **DONE** (illustrator, 2026-10-22): `assets/library/pulmonoscorpius.json`, preview `assets/previews/025-too-much-oxygen-assets.png`
- What: Pulmonoscorpius kirktonensis, a giant land scorpion about 70 cm long ("the size of a house cat").
- Look: Side view, walking right: dark brown-black #3a2e24 armoured body with lighter segment edges, **fairly small pincers** (the
  script says so; they are pointed at), eight walking legs touching y +80, the tail arched up over the back ending in a bulbous
  stinger. Heavy and real. Used as a silhouette with red glow (s147) and must match the length of `fallen_log` at similar scale (s170:
  log 0.9, scorpion 0.95, "about as long as the log").
- Facing/anchor: Facing right. Centre anchor, legs touch y = +80 (like `arthropleura`). bbox about x -360..340, y -230..80.
- Shots (15): s032, s033, s147, s148, s149, s154, s155, s157, s158, s159, s163, s166, s167, s168, s170.

### pulmonoscorpius_underside
- **DONE** (illustrator, 2026-10-22): `assets/library/pulmonoscorpius_underside.json`, preview `assets/previews/025-too-much-oxygen-assets.png`
- What: The same scorpion seen **from below**, for "four pairs of book lungs on their underside".
- Look: Ventral view, head right: pale tan underside plates, legs radiating, and **four pairs of small dark slits** (book-lung openings)
  in two rows on the middle segments, clearly visible. Tail straight out to the left.
- Facing/anchor: Head right. Centre anchor, bbox about x -360..340, y -160..160.
- Shots (1): s161.

### hibbertopterus
- **DONE** (illustrator, 2026-10-22): `assets/library/hibbertopterus.json`, preview `assets/previews/025-too-much-oxygen-assets.png`
- What: Hibbertopterus, a giant sweep-feeding sea scorpion about 1.6 m long and 1 m wide, the trackway maker.
- Look: Top 3/4 view, walking right: **very broad, rounded, flattened head shield** (much wider than `jaekelopterus`), wide armoured
  body tapering to a short pointed tail, front limbs carrying long **spiny blades** (rakes) held forward, sturdy walking legs. Mud brown
  #6f5a3e, spray texture. Heavy, slow-looking, not menacing-fast. Used as a silhouette (s178) and walking over a lying Doug (s194).
- Facing/anchor: Facing right. Centre anchor, bbox about x -330..330, y -220..220.
- Shots (11): s178-s183, s186, s188, s189, s190, s194.

### hibbertopterus_trackway
- **DONE** (illustrator, 2026-10-22): `assets/library/hibbertopterus_trackway.json`, preview `assets/previews/025-too-much-oxygen-assets.png, assets/previews/025-assets-B-trackway.png`
- What: The 6 m Fife trackway: **two parallel bands of footprints with a dragged-tail groove down the middle**.
- Look: Top view on transparent ground (it sits on sand `#c9a87a` and on a rock outcrop `#b08f62`): two rows of crescent/oval
  footprint clusters in darker sand #8a6f4a with lighter rims, a continuous wavy groove between them. Long and horizontal.
- Facing/anchor: Running left to right. Centre anchor, bbox about x -650..650, y -110..110. Doug lies inside it (s193), so leave the middle
  band readable.
- Shots (14): s174, s176, s177, s178, s184, s185, s187, s191-s197.

### crassigyrinus
- **DONE** (illustrator, 2026-10-22): `assets/library/crassigyrinus.json`, preview `assets/previews/025-too-much-oxygen-assets.png`
- What: Crassigyrinus scoticus, "the tadpole from hell": an early four-limbed water predator, 2-3 m long. Not a bug.
- Look: Side view: long, **flat, eel-like body** with a finned tail, **very tiny limbs**, and the 2023 reconstruction's **low, wide,
  crocodile-like head** with big jaws, many large teeth and large eyes. Dark olive-brown #4a4a30 with lighter belly and mottling.
  Used underwater as a black silhouette with a red rim (s199) and as a crushed fossil (`ink: #4a4a4a`).
- Facing/anchor: Facing right. Centre anchor, bbox about x -420..420, y -120..110.
- Shots (9): s033, s199, s201, s203, s204, s205, s206, s210, s230.

### crassigyrinus_eyes
- **DONE** (illustrator, 2026-10-22): `assets/library/crassigyrinus_eyes.json`, preview `assets/previews/025-too-much-oxygen-assets.png`
- What: Crassigyrinus waiting just below the surface: **only two large eyes and the top of the flat head** show above the water.
- Look: Two big eyes with dark pupils on bumps, the low snout ridge, a dark shape faintly under the surface, pale ripple lines.
  Murky pool water #2f3a2a around it (like `croc_eyes_water`, but no scutes and no crocodile eye; this must not read as a crocodile).
- Facing/anchor: Facing right. Anchor (0,0) on the waterline; bbox about x -200..200, y -70..60.
- Shots (5): s198, s215, s216, s217, s219.

### crassigyrinus_skull
- **DONE** (illustrator, 2026-10-22): `assets/library/crassigyrinus_skull.json`, preview `assets/previews/025-too-much-oxygen-assets.png`
- What: The 2023 digital skull reconstruction: **low and wide**, full of huge teeth, with ridges and large eye sockets.
- Look: Side view in the cream bone palette of `crocodile_skull` (they appear side by side), lower and flatter than a croc's, large
  orbit at (+40,-40), a row of big conical teeth, a few raised ridges along the top. No flesh, no red.
- Facing/anchor: Facing right. Centre anchor, bbox about x -300..300, y -100..100 (also drawn at 0.75 inside the `crt_tv` screen).
- Shots (6): s208, s209, s211, s212, s213, s214.

### crassigyrinus_old_head
- **DONE** (illustrator, 2026-10-22): `assets/library/crassigyrinus_old_head.json`, preview `assets/previews/025-too-much-oxygen-assets.png`
- What: The old (pre-2023) reconstruction: a **tall, narrow head, a bit like a moray eel**.
- Look: Brown-ink engraving plate style like `old_hallucigenia_1977`: a deep, narrow, slab-sided head in side view with a high skull and
  a long jaw line, on a yellowed plate background (#efe2b8, brown border).
- Facing/anchor: Facing right. Centre anchor, bbox about x -200..200, y -230..230.
- Shots (1): s207.

### arthropleura_fossil_boulder
- **DONE** (illustrator, 2026-10-22): `assets/library/arthropleura_fossil_boulder.json`, preview `assets/previews/025-too-much-oxygen-assets.png`
- What: The Howick Bay find: a fallen **sandstone block split open** with a section of Arthropleura's segmented shell inside.
- Look: Buff sandstone #d9b77a block cracked into two halves, the inside face showing a long dark segmented fossil strip (about 12
  plates with side lobes, matching `arthropleura`). Grainy spray texture.
- Facing/anchor: Bottom-centre anchor (sits on the beach). bbox about x -300..300, y -380..0.
- Shots (5): s224, s225, s227, s241, s242.

### arthropleura_head
- **DONE** (illustrator, 2026-10-22): `assets/library/arthropleura_head.json`, preview `assets/previews/025-too-much-oxygen-assets.png`
- What: The 2024 juvenile head reveal: a millipede body but some centipede-like head features.
- Look: Front 3/4 view of the head and first segments: two antennae, **eyes on short stalks**, mouthparts, in the same dark brown-grey
  plate palette as `arthropleura`.
- Facing/anchor: Facing the viewer/right. Centre anchor, bbox about x -220..220, y -170..170 (also at 0.6 inside the `crt_tv` screen).
- Shots (2): s235, s236.

### tree_fern
- **DONE** (illustrator, 2026-10-22): `assets/library/tree_fern.json`, preview `assets/previews/025-too-much-oxygen-assets.png`
- What: Carboniferous tree fern (Psaronius-type) for The Beak's forest.
- Look: Straight, shaggy trunk (#5a4a30 with matted root texture) topped by a crown of long, arching, finely divided fronds (#4f8a3a /
  darker #3a6a2a). Different silhouette from `scale_tree` (crown of fronds, no forked branches).
- Facing/anchor: Bottom-centre anchor (trunk base y=0). bbox about x -220..220, y -620..0 (keep it no taller: at 0.95 it must stay under
  the death-counter zone).
- Shots (13): s090, s092, s102, s103, s105, s110-s117.

## Props

### doug_silhouette
- **DONE** (illustrator, 2026-10-22): `assets/library/doug_silhouette.json`, preview `assets/previews/025-too-much-oxygen-assets.png, assets/previews/025C-dougtest.png`
- What: The DOUG FOR SCALE figure: Doug standing, as a **flat silhouette** (episode device beside the vertical tape).
- Look: Doug's `stand` pose filled flat mid-grey #8a8a8a with a 5 px black outline, the cap shape included (outline only, no red), no
  face. Must read as "Doug" from the outline alone.
- Facing/anchor: Facing right. Bottom-centre anchor (feet on y=0); height exactly 450 (cap top at y -450), width about 200.
- Shots (10): s039, s056, s082, s099, s122, s149, s173, s179, s210, s229.

### cupcake_candle
- **DONE** (illustrator, 2026-10-22): `assets/library/cupcake_candle.json`, preview `assets/previews/025-too-much-oxygen-assets.png`
- What: Doug's celebration cupcake with **one birthday candle**, small normal flame.
- Look: Pink-frosted cupcake in a striped paper case, a single thin striped candle, a small yellow-orange flame.
- Facing/anchor: Centre anchor, bbox about x -90..90, y -130..130 (wick tip at about (0,-110)).
- Shots (7): s024-s030 (it survives the flare).

### candle_flare
- **DONE** (illustrator, 2026-10-22): `assets/library/candle_flare.json`, preview `assets/previews/025-too-much-oxygen-assets.png, assets/previews/025D-stack.png`
- What: The candle flame "jumping far too high" in high-oxygen air.
- Look: A tall, roaring column of cartoon flame (yellow core, orange, red edges) with a few sparks. Cartoon, no smoke cloud over faces.
- Facing/anchor: Bottom-centre anchor at the wick. bbox about x -150..150, y -650..0.
- Shots (1): s027.

### fire_flames
- **DONE** (illustrator, 2026-10-22): `assets/library/fire_flames.json`, preview `assets/previews/025-too-much-oxygen-assets.png`
- What: A cluster of cartoon flames for "even the plants in a wet swamp could catch fire" (no logs, no stones, unlike `campfire`).
- Look: Layered red-orange-yellow flame tongues, a few sparks, a faint glow at the base.
- Facing/anchor: Bottom-centre anchor. bbox about x -200..200, y -420..0.
- Shots (1): s019.

### leaf_hat
- **DONE** (illustrator, 2026-10-22): `assets/library/leaf_hat.json`, preview `assets/previews/025-too-much-oxygen-assets.png, assets/previews/025C-dougtest.png`
- What: Doug's camouflage hat made of overlapping leaves (worn prop, not a costume).
- Look: A dome of overlapping green leaves (#4f8a3a / #6fae4a, a few lighter) sitting on top of the cap, **the red cap brim and the top of
  the cap dome still visible** (the script: "the red cap poking through the top"). No face.
- Facing/anchor: Worn prop like `paper_crown`: anchor = Doug's hips at scale 1 (stand pose); rim bottom at about y -293, leaves up to
  about y -420. Used at scale 0.55 with stand / hands_hips / thumbs_up.
- Shots (8): s110-s117.

### bug_net
- **DONE** (illustrator, 2026-10-22): `assets/library/bug_net.json`, preview `assets/previews/025-too-much-oxygen-assets.png, assets/previews/025C-dougtest.png`
- What: Doug's insect net.
- Look: Light wooden handle, a wire hoop and a white mesh bag hanging below the hoop.
- Facing/anchor: Anchor = the handle grip end (0,0); the handle runs straight up to the hoop centred at (0,-400), hoop radius about 100,
  bag hanging to about y -260. Used rotated a little.
- Shots (3): s140, s141, s142 (in s141/s142 Meganeura holds the hoop and Doug hangs from the grip).

### fern_saddle
- **DONE** (illustrator, 2026-10-22): `assets/library/fern_saddle.json`, preview `assets/previews/025-too-much-oxygen-assets.png`
- What: A saddle made out of a fern, for riding Arthropleura.
- Look: A saddle shape woven from green fern fronds, two dangling stirrups made of twisted stems.
- Facing/anchor: Centre anchor, bbox about x -160..160, y -90..90.
- Shots (4): s250, s251, s253, s254.

### bathtub
- **DONE** (illustrator, 2026-10-22): `assets/library/bathtub.json`, preview `assets/previews/025-too-much-oxygen-assets.png`
- What: A standard bathtub (1.6 m scale reference).
- Look: White enamel tub, side view, rounded rim, claw feet, a tap and plug chain.
- Facing/anchor: Centre anchor, bbox about x -330..330, y -130..130.
- Shots (1): s179.

### bicycle_wheel
- **DONE** (illustrator, 2026-10-22): `assets/library/bicycle_wheel.json`, preview `assets/previews/025-too-much-oxygen-assets.png`
- What: A road bike wheel (about 70 cm), scale reference for Meganeura's wingspan.
- Look: Thin black tyre, silver rim, many straight spokes, small hub with a cassette.
- Facing/anchor: Centre anchor, diameter about 500.
- Shots (1): s122.

### ukulele
- **DONE** (illustrator, 2026-10-22): `assets/library/ukulele.json`, preview `assets/previews/025-too-much-oxygen-assets.png`
- What: A soprano ukulele (about 53 cm), scale reference for Megarachne.
- Look: Small light-wood guitar shape, sound hole, four strings, dark fretboard, headstock with four pegs. Not `guitar`.
- Facing/anchor: Horizontal, neck to the right. Centre anchor, bbox about x -210..210, y -75..75.
- Shots (1): s082.
