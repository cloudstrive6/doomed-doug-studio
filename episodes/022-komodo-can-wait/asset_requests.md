# 022-komodo-can-wait: asset requests (director to illustrator / art director)

Library assets I reuse as they are: `komodo_dragon` (the adult in every walking, standing, chasing and stacked shot), `deer`,
`lizard` (the "ordinary lizard" in The Last Giant), `saltwater_crocodile`, `great_white_shark`, `horse`, `african_bush_elephant`,
`elephant_tusked` (stands in for Stegodon, small and labelled), `baby_grand_piano` (the "concert grand"), `bathroom_scale`,
`dinner_plate` (Doug's tiny paper plate and the 1,095 meals), `sandwich`, `picnic_blanket` (its green flask is the thermos),
`fallen_log`, `rainforest_tree`, `tree_branch`, `savanna_bush`, `palm_tree`, `deck_chair` (the folding chair), `rubber_ring`,
`flag_doug_was_here`, `field_guide`, `field_guide_open`, `mouthwash_bottle` (010 callback), `scientist`, `clipboard`, `binoculars`,
`magnifying_glass`, `journal_paper`, `vial`, `calendar`, `clock`, `thermometer`, `tennis_ball`, `soccer_ball`, `insect`, `stew_bowl`,
`thumbs_up_hand`, `fossil_bone`, `dust_cloud` (death 179 only), `dust_plume`, `narrator_hand`, `australia_map`, `paper_crown`,
`doug_cap`, `gravestone`, `question_mark`, `exclamation_mark`, `warning_triangle`, `red_x`.

Drawn from primitives in the shotlist (no asset needed): the pie chart, the running track, the DNA helix, the wall-calendar grids,
the timeline bar, the coin, the islands and the tide strips, the sun, moon and music notes.

House rules for everything below (brief section 7 and the CD's notes in `decisions.md`): detailed cartoon tier, thick black outline
(5-6), flat fills with soft interior shading, read at thumbnail size. **No blood, no wounds, no red on teeth or mouths beyond the
usual dark `#7a0d0d` mouth interior, no carcasses, no feeding on screen.** Dragons are **heavy, low and menacing**: small hard eye
under a heavy brow, no smile curve, no big round eyes, nothing that reads as a fantasy dragon (no wings, horns, fire or spikes).
Young dragons are **lean and hard-eyed, never cute**. Komodo palette: match `komodo_dragon.json` exactly (grey-brown pebbly body,
darker back, dusty lighter belly, pale curved claws, forked yellow tongue) so every pose reads as the same animal. Everything faces
right unless noted; the shotlist flips as needed.

## THE WAIT clock (episode device, art director owns the look)

### wait_stopwatch
- What: THE WAIT, the episode's crude MS Paint stopwatch. Used tiny as the meter icon beside the label under the death counter in every
  shot (scale 0.16, like 013's DISTANCE meter and 020's `depth_icon`), and big as a prop (narrator presses its button, "17 MIN",
  "1 MIN", the section-header cards, the closing "clock is still running").
- Look: chunky round silver-grey stopwatch: thick black outline, grey `#a9adb3` case with a darker rim, a top crown button on a short
  stem, a small side button at about 1 o'clock, and a **plain white face with only 12 short tick marks and no hands** (the shotlist
  prints the time value in black on the face). Base it on `clock.json` / `alarm_clock.json` for line weight. Must read as a stopwatch
  at 0.16 (about 40 px tall): keep the crown button bold.
- Size/anchor: centre anchor, about 260 wide x 300 tall (x -130..130, y -160..140). Crown button top at (0,-160), button press point at
  (0,-140). **Face centre (0,+20), clear radius 100** for the overlay text.
- Shots: every shot s002-s288 (meter icon at 0.16 next to the label at (1600, 238)); big at s004, s052-s054, s100, s131, s163, s174,
  s176, s190, s213, s235, s280-s281 (on Doug's lap, 0.32), s284, s287.

## Komodo dragon poses (all must match `komodo_dragon` exactly)

### komodo_log
- What: an adult dragon lying perfectly flat and still beside a game trail, eyes **closed**, so that at a glance it passes for a dusty
  fallen log (the "NOT A LOG" gag). The thumbnail hero pose.
- Look: `komodo_dragon` with the legs tucked flat under the body, belly on the ground, tail straight out behind, head resting low on the
  ground facing right, closed eye as a single heavy lid line, mouth shut, tongue in. Same colours, slightly dustier (`#b8a882` dust
  speckle on the back).
- Facing right. Anchor bottom-centre (belly on y=0). About 940 x 150 (x -470..470, y -150..0).
- Shots (20): s002-s003, s005, s013-s021, s023-s024, s028, s056, s077, s122, s237, s284.

- **DONE (illustrator):** `assets/library/komodo_log.json`, preview `assets/previews/022-komodo-can-wait-assets.png`. wobble/boil 0; eye at local (+362,-84); bbox x -470..470, y -142..0.
### komodo_log_eye
- What: exactly `komodo_log` (same geometry, `wobble`/`boil` identical so the swap is seamless) with **one eye open**: small amber eye,
  black slit-ish pupil, heavy brow. Like `croc_log` / `croc_log_eye`.
- Facing right. Same bbox and anchor as `komodo_log`.
- Shots (11): s025-s026, s162-s163, s229-s230, s279-s283.

- **DONE (illustrator):** `assets/library/komodo_log_eye.json`, preview `assets/previews/022-komodo-can-wait-assets.png`. same geometry as komodo_log (wobble/boil 0), swap at the same x/y/scale/flip.
### komodo_head
- What: head and neck of an adult in profile with the **long forked yellow tongue flicked out** (tongue tips clearly spread). Used
  big for The Tongue (scale 1.4-1.6), small (0.4-0.5) in crowds of heads around an off-frame meal, peeking over a ridge, and
  round the side of a boulder (flipped).
- Look: heavy head, small hard amber eye under a heavy brow, closed mouth with the jaw line visible, neck cut off softly at the left
  (fade the neck into a darker scaly edge, no cut or stump look). Tongue: long, yellow `#e8c43a` with a dark outline, deeply forked,
  the two tips about 60 units apart at the right end.
- Facing right. Anchor centre. About 560 x 220 (x -280..280, y -110..110), tongue tips at about x +280.
- Shots (33): s053, s055, s057-s066, s069-s070, s076-s077, s123, s125-s130, s132-s133, s139-s141, s143, s158-s160, s165.

- **DONE (illustrator):** `assets/library/komodo_head.json`, preview `assets/previews/022-komodo-can-wait-assets.png`. tongue tips at (+282,-12) and (+282,+48); eye (+30,-62); bbox x -280..282, y -106..108.
### komodo_mouth_teeth
- What: close-up of the dragon's mouth slightly open, showing a row of **curved, flattened, serrated teeth** along the jaws.
- Look: the front half of the head, very large, jaws open about 20 degrees, dark `#7a0d0d` mouth interior (no red on the teeth),
  teeth cream-white, backward-curved blades with tiny serration notches, partly sheathed by grey-pink gum. Hard eye.
- Facing right. Anchor centre. About 900 x 500.
- Shots (4): s029, s033-s034, s040.

- **DONE (illustrator):** `assets/library/komodo_mouth_teeth.json`, preview `assets/previews/022-komodo-can-wait-assets.png`. bbox x -450..446, y -250..252; head continues off the left edge.
### komodo_tooth
- What: one tooth, enlarged, for the 2024 iron-coating fact.
- Look: a flattened backward-curved blade, cream `#f1ead6`, point down, serrated back edge, with a **clear orange `#e07b2a` stripe
  along the cutting edge and the tip** (the iron). No red, no gum.
- Point down. Anchor centre. About 260 x 420.
- Shots (5): s035-s039.

- **DONE (illustrator):** `assets/library/komodo_tooth.json`, preview `assets/previews/022-komodo-can-wait-assets-b.png`. bbox x -118..118, y -206..206.
### komodo_skull
- What: textbook-style side view of a Komodo dragon skull (Fry et al. 2009 model). **Not** the 010 `komodo_head_scan` venom diagram.
- Look: long, fairly light cream bone `#efe6d0` skull with grey shading, large eye socket, long narrow snout, row of small curved teeth.
- Facing right. Anchor centre. About 600 x 260 (same length as `crocodile_skull` so the two read as "same size").
- Shots (3): s041-s043.

- **DONE (illustrator):** `assets/library/komodo_skull.json`, preview `assets/previews/022-komodo-can-wait-assets-b.png`. about 600x220 (x -300..300, y -118..102), kept lower than the croc on purpose.
### crocodile_skull
- What: saltwater crocodile skull, side view, for the 6.5x bite comparison.
- Look: same cream bone palette, much deeper, heavier and broader jaw, big conical teeth, thick jaw muscle attachment area.
- Facing right. Anchor centre. About 600 x 220.
- Shots (2): s042-s043.

- **DONE (illustrator):** `assets/library/crocodile_skull.json`, preview `assets/previews/022-komodo-can-wait-assets-b.png`. about 610x240 (x -306..302, y -116..122).
### komodo_swim
- What: a dragon swimming at the surface: only the head and a low line of back and tail above the waterline.
- Look: `komodo_dragon` colours; head up, nostrils clear, a few ripple lines and a small white wake at the head. Draws on `#3a9ad9`.
- Facing right. Anchor = waterline centre (y=0 is the water surface). About 700 wide, up to 110 above and 20 below the line.
- Shots (5): s101, s104-s105, s110-s111.

- **DONE (illustrator):** `assets/library/komodo_swim.json`, preview `assets/previews/022-komodo-can-wait-assets.png`. drawn for #3a9ad9; wake reaches x +432; y -70..20.
### komodo_rearing_pair
- What: two large males in **ritual combat**: reared up on their hind legs and tails, chest to chest, forelimbs gripping each other.
- Look: both match `komodo_dragon`; mouths closed, no wounds, no bites. Dust puffs at their feet.
- Facing: the pair faces each other (left one faces right). Anchor bottom-centre (feet on y=0). About 700 x 560.
- Shots (1): s138.

- **DONE (illustrator):** `assets/library/komodo_rearing_pair.json`, preview `assets/previews/022-komodo-can-wait-assets.png`. bbox about x -352..352, y -560..0; left one holds its head higher.
### komodo_bloated
- What: a heavy, bloated, full dragon basking flat on a warm rock after a meal (The Meal, The Fast, the closing).
- Look: `komodo_dragon` with a visibly rounder, sagging belly that spreads on the rock, legs splayed out flat, chin down, eyes
  **half-closed** (heavy lid over half the eye, still hard, not sleepy-cute). No food or prey shapes visible inside.
- Facing right. Anchor bottom-centre. About 960 x 200.
- Shots (25): s168, s177-s182, s191, s193, s196-s197, s201-s212, s277-s278.

- **DONE (illustrator):** `assets/library/komodo_bloated.json`, preview `assets/previews/022-komodo-can-wait-assets.png`. bbox x -480..482, y -200..0.
### komodo_young
- What: a young dragon (hatchling to juvenile). Used on the ground, rotated about -80 degrees climbing a trunk, sitting on a branch, and
  as the "four healthy young".
- Look: **lean, long and wiry**, longer tail relative to body, banded pattern of yellow-orange speckles on dark grey-green (real
  juvenile colouring), hard narrow eye, tongue in. **Never big-eyed, never round-headed, never cute.**
- Facing right. Anchor bottom-centre (feet on y=0). About 420 x 100 (x -210..210). Keep the silhouette bold at scale 0.25.
- Shots (24): s114, s137, s214-s217, s220-s230, s232, s234, s242, s245, s249-s250, s255.

- **DONE (illustrator):** `assets/library/komodo_young.json`, preview `assets/previews/022-komodo-can-wait-assets.png`. bbox x -212..214, y -72..0; 6-unit outline holds at 0.25.
### megalania
- What: Megalania (*Varanus priscus*), the giant extinct Australian monitor. First shown as a silhouette (red glow, then full).
- Look: same body plan as `komodo_dragon` but **drawn at the same unit scale and about 1.8x as long and much bulkier**: deeper head,
  thicker neck and limbs, heavier tail; darker olive-brown `#6a5f45` with lighter belly; small hard eye. Monitor lizard, not a dinosaur.
- Facing right. Anchor bottom-centre. About 1700 x 380 (x -850..850, y -380..0). SIL-safe outline (one closed shape).
- Shots (4): s263-s266 (s263-s264 as `silhouette`).

- **DONE (illustrator):** `assets/library/megalania.json`, preview `assets/previews/022-komodo-can-wait-assets-megalania.png`. bbox x -817..868, y -376..0; SIL-safe; use glow_r ~1200 for the silhouette.
### megalania_grey
- What: exactly `megalania` (same geometry) in flat greys `#9a9a9a` / `#7d7d7d`, outline `#5a5a5a`, for "gone" / extinct.
- Same bbox and anchor.
- Shots (3): s267-s268, s277.

- **DONE (illustrator):** `assets/library/megalania_grey.json`, preview `assets/previews/022-komodo-can-wait-assets-megalania.png`. same geometry as megalania.
## Other creatures

### water_buffalo
- What: an adult domestic water buffalo (introduced to the islands).
- Look: big, dark slate-grey `#4a4a4a` with lighter grey muzzle and lower legs, wide swept-back crescent horns, heavy shoulders, calm
  confident eye (half-lidded, unbothered). Side view. No wounds, no blood, never lying down.
- Facing right. Anchor bottom-centre. About 700 x 460.
- Shots (18): s002, s144-s149, s152-s157, s161, s164-s167.

- **DONE (illustrator):** `assets/library/water_buffalo.json`, preview `assets/previews/022-komodo-can-wait-assets-b.png`. bbox about x -342..356, y -462..0.
### wild_boar
- What: a wild boar (Sunda/Flores type).
- Look: bristly dark grey-brown body, crest of longer bristles along the spine, long snout with small tusks, short legs, thin tail.
- Facing right. Anchor bottom-centre. About 420 x 240.
- Shots (5): s002, s016, s151, s174, s195.

- **DONE (illustrator):** `assets/library/wild_boar.json`, preview `assets/previews/022-komodo-can-wait-assets-b.png`. bbox about x -220..223, y -272..0.
### smilodon
- What: a sabre-toothed cat (head and shoulders is fine), for "compared the method to sharks and sabre-toothed cats".
- Look: tawny `#c9944a` big cat, darker back, long curved upper canines showing past the closed lower jaw. No blood.
- Facing left (toward the shark on the left). Anchor centre. About 600 x 520.
- Shots (2): s045-s046.

- **DONE (illustrator):** `assets/library/smilodon.json`, preview `assets/previews/022-komodo-can-wait-assets-b.png`. faces left; bbox about x -336..256, y -266..258 (ear tip slightly above the spec box).
## Nests and eggs

### nest_mound
- **DONE** (illustrator): `assets/library/nest_mound.json`, preview `assets/previews/022-komodo-can-wait-props.png (+ on scene backgrounds: 022-komodo-can-wait-props-onbg.png)`.
- What: a Komodo nest mound of scraped earth (also used empty as the **decoy nest**).
- Look: low domed heap of brown earth `#8a6a4a` with darker shading, a few twigs and dry leaves, one dug opening at the front.
- Anchor bottom-centre. About 520 x 170.
- Shots (8): s114, s218-s219, s236, s252-s255.

### komodo_eggs
- **DONE** (illustrator): `assets/library/komodo_eggs.json`, preview `assets/previews/022-komodo-can-wait-props.png (+ on scene backgrounds: 022-komodo-can-wait-props-onbg.png)`.
- What: a clutch of Komodo eggs placed in front of the nest mound.
- Look: about 8 visible **leathery white elongated eggs** (`#f4f1e8`, grey shading), in a shallow scrape, slightly dented and matte.
- Anchor bottom-centre. About 260 x 90.
- Shots (8): s218-s219, s236, s240, s245, s247-s248, s252.

### komodo_eggs_hatching
- **DONE** (illustrator): `assets/library/komodo_eggs_hatching.json`, preview `assets/previews/022-komodo-can-wait-props.png (+ on scene backgrounds: 022-komodo-can-wait-props-onbg.png)`.
- What: the same clutch hatching: torn leathery shells, three young dragon heads and forelimbs pushing out.
- Look: same footprint as `komodo_eggs`; the young are the `komodo_young` design (lean, hard narrow eyes, no cute faces).
- Anchor bottom-centre. About 260 x 110.
- Shots (2): s253-s254.

## Props and places

### placard
- **DONE** (illustrator): `assets/library/placard.json`, preview `assets/previews/022-komodo-can-wait-props.png (+ on scene backgrounds: 022-komodo-can-wait-props-onbg.png)`.
- What: Doug's handheld protest sign for "MORAL SUPPORT".
- Look: plain white card board with a black outline on a light wooden stick. **Leave the card blank**: the shotlist prints the text.
- Anchor = grip point at the bottom of the stick (0,0); card x -150..150, y -360..-200 (text centre at (0,-280)).
- Shots (4): s164-s167 (lying on the grass, rotated, in s166-s167).

### signboard
- **DONE** (illustrator): `assets/library/signboard.json`, preview `assets/previews/022-komodo-can-wait-props.png (+ on scene backgrounds: 022-komodo-can-wait-props-onbg.png)`.
- What: a zoo entrance sign on two wooden posts (CHESTER ZOO, LONDON ZOO).
- Look: cream `#e8dcc0` board with a dark frame on two brown posts. **Leave the board blank** (text centre at (0,-265)).
- Anchor bottom-centre. About 440 x 330.
- Shots (4): s239-s242.

### big_water_bottle
- **DONE** (illustrator): `assets/library/big_water_bottle.json`, preview `assets/previews/022-komodo-can-wait-props.png (+ on scene backgrounds: 022-komodo-can-wait-props-onbg.png)`.
- What: a big two-litre plastic bottle of water (15 in a row = 31 kg).
- Look: clear pale-blue plastic, blue cap, water to the shoulder, plain white label band (no brand).
- Anchor bottom-centre. About 110 x 330.
- Shots (1): s175 (fifteen copies).

### stick_cyclist
- **DONE** (illustrator): `assets/library/stick_cyclist.json`, preview `assets/previews/022-komodo-can-wait-props.png (+ on scene backgrounds: 022-komodo-can-wait-props-onbg.png)`.
- What: a city commuter cycling at an easy pace (Copenhagen comparison).
- Look: crude tier like `scientist` (5 px lines, big round head, grey crescent, no red cap), `auto_ink`; plain upright city bike with a
  basket, relaxed face.
- Facing right. Anchor bottom-centre (wheels on y=0). About 420 x 420.
- Shots (1): s011.

### picnic_basket
- **DONE** (illustrator): `assets/library/picnic_basket.json`, preview `assets/previews/022-komodo-can-wait-props.png (+ on scene backgrounds: 022-komodo-can-wait-props-onbg.png)`.
- What: a wicker picnic basket for Doug's peace-treaty picnic.
- Look: tan woven basket `#c9944a` with crosshatch weave, two hinged lids, a red-and-white gingham cloth poking out, arched handle.
- Anchor bottom-centre. About 220 x 180.
- Shots (2): s184-s185.

### flower_bouquet
- **DONE** (illustrator): `assets/library/flower_bouquet.json`, preview `assets/previews/022-komodo-can-wait-props.png (+ on scene backgrounds: 022-komodo-can-wait-props-onbg.png)`.
- What: the bunch of flowers Doug brings to the nest.
- Look: 5-6 simple flowers (pink, yellow, white) on green stems tied with a red ribbon.
- Anchor = grip point at the bottom of the stems (0,0); flowers up to y -200, about 120 wide.
- Shots (4): s252-s255.

### boulder
- **DONE** (illustrator): `assets/library/boulder.json`, preview `assets/previews/022-komodo-can-wait-props.png (+ on scene backgrounds: 022-komodo-can-wait-props-onbg.png)`.
- What: the big rock Doug hides behind (The Tongue); the cap sits on top after death 180.
- Look: grey-brown `#7a6a58` volcanic boulder, lit upper-left, darker lower-right, a few cracks, dusty base. No face, no body shapes.
- Anchor bottom-centre. About 420 x 330, with a **flat spot on top at (0,-330)** for the cap.
- Shots (5): s073-s077.

### flat_rock
- **DONE** (illustrator): `assets/library/flat_rock.json`, preview `assets/previews/022-komodo-can-wait-props.png (+ on scene backgrounds: 022-komodo-can-wait-props-onbg.png)`.
- What: the low warm rock slab dragons bask on, and the rock Doug sets his folding chair on in the boss.
- Look: wide, low grey-tan `#8a7a6a` slab with a sun-lit flat top and darker front face, a few cracks.
- Anchor bottom-centre. About 900 x 120, **flat top surface at y -110** (dragons and the chair stand there).
- Shots (25): s177-s181, s191, s193, s196-s197, s201, s203, s205-s212, s279-s283, s288.

### komodo_np_map
- **DONE** (illustrator): `assets/library/komodo_np_map.json`, preview `assets/previews/022-komodo-can-wait-map.png`.
- What: map of Komodo National Park in the `world_map` style (flat green `#6cbf5a` land, dark green outline, light-blue sea, black frame,
  no labels): Komodo Island, Rinca, the small islands between (Padar, Gili Motang, Nusa Kode) and the west end of Flores, with the east tip
  of Sumbawa at the far left edge.
- Projection: equirectangular, lon 118.7..121.3 E, lat 7.74..9.26 S at 500 px per degree: about 1300 x 760 including the frame, anchor
  centre at lon 120.0 / lat -8.5, so x = (lon - 120) * 500, y = -(lat + 8.5) * 500. The shotlist rings Komodo at about (-275, 40),
  Rinca at (-140, 90) and west Flores at (+260, 0), and puts ten site dots on land, so please keep those three positions on land.
- Anchor centre. Used at scale 0.82 centred at (900, 600).
- Shots (9): s006-s007, s106-s109, s274-s276.

### bread_knife
- **DONE** (illustrator): `assets/library/bread_knife.json`, preview `assets/previews/022-komodo-can-wait-props.png (+ on scene backgrounds: 022-komodo-can-wait-props-onbg.png)`.
- What: a serrated bread knife for "serrated along the edges like a bread knife".
- Look: long steel blade `#c9ced4` with a clearly scalloped serrated edge, black handle with rivets, lying horizontally, blade to the
  right. No blood.
- Anchor centre. About 520 x 60.
- Shots (1): s034.

## Doug gear (art director, not the illustrator)

### `bandage` gear
- What: Doug's small **white** ankle bandage (series bible: survival marker for a bite he walks away from; never red, never a wound).
- Look: a short white wrap of 3 turns with a thin grey outline around the **front ankle**, just above the foot, for the `stand`, `point`,
  `thumbs_up`, `walk1`/`walk2` poses (it must follow the leg in the walk loop, which is why it is gear and not a prop).
- Shots (6): s047, s049-s052, s054. The thumbnail uses it too. Until it exists the shotlist references `"gear": ["bandage"]` on those
  Doug elements, and the engine ignores it.

## Notes for the art director / graphic designer
- The thumbnail (`thumbnail.json`, s001) is not drawn yet. Brief proposal A: `komodo_log_eye` big, tongue out, tiny Doug walking away
  whistling with the bandage, "IT CAN WAIT".
- THE WAIT meter: size-28 `label` "THE WAIT: <value>" centred at (1600, 238) with `wait_stopwatch` at 0.16 to its left, under the
  counter. Values used, monotonic: (blank) "THE WAIT", 0 S, 1 S, 50 MIN, 4 HR, 1 DAY, SEVERAL DAYS (Crowd and Buffalo), 5 DAYS, 1 MONTH,
  MONTHS, 2+ YEARS, ABOUT 4,000,000 YR.
- Background ramp by THE WAIT band (time of day, luminance falls band by band): Seconds sky `#8fd3ff` / ground `#e2c97e`; Hours
  `#a9cfe4` / `#d8bd6e`; Days `#ecc27a` / `#c9a24a`; Weeks `#f2a24a` / `#b8913a`; Months `#e0844a` / `#9c8452`; Years `#8a6a8a` /
  `#93806a`; the boss is night `#1b2f5a` / `#2b3d33` (Doug auto-inks white) with sea `#2f6f9f`. The Swim keeps surface water `#3a9ad9`.
