# 017 asset requests (director to illustrator)

There are 55 new drawings. Everything else in the shotlist already exists in `assets/library/`. Reused there: frog, songbird, scientist, caver, paperclip, bank_card, calendar/clock, microscope, magnifying_glass, petri_dish, thermometer, hot_tub, house, usa_map, world_map, north_america_map, australia_map, pine_tree, large_dog, cat, horse, bread_loaf, fair_booth, finish_banner, highspeed_camera, grass_blade, ant_costume, fungus_stalk, bullet_ant, stone_bat, lab_mouse, kitchen_chair, door_ajar, heart_icon, doug_cap, and the annotation set.

**House rules for this episode.** These come from the brief and the art bible.
- Spores and fungus are soft cartoon dust and fuzz (off-white `#f6f6f0`, light grey speckle). Never wounds, rot or skin disease. No fruiting bodies bursting out of drawn bodies.
- Creatures are drawn at the detailed creature tier (layered fills, interior shading, outlines 3 to 5). Nothing cute: no big shiny eyes, no smiles.
- No text inside an asset unless this file asks for it. Several assets get rotated or flipped.
- **Costumes** are worn props, like `cricket_costume` and `sheep_costume`:
  - Anchor = Doug's hips at Doug scale 1, drawn for the `stand` pose, facing right.
  - Doug's head, face and red cap must stay fully visible. Hood features (eyes, ears) sit *beside* the cap, never over it.
  - The shotlist places each costume at Doug's exact x/y/scale, after Doug.
  - `spider_costume` and `bat_costume` are also drawn upside down: Doug and the costume share a group with `rotate: 180` for ceiling and hanging shots. So these two need no text and no gravity-dependent details (no dangling tassels).
- **`*_flat` costumes** are the empty suit after a death, lying flat on the ground. Anchor at the centre, about 470x150, like `crab_costume_flat`. No Doug inside, no tears. Ghost Doug floats above them in the shot.
- **Fly mating beat (s047-s050, s057).** Only the dead female (`fly_death_pose_banded`) is drawn on the glass. The males are separate `house_fly` assets kept 150+ px away from her. Nothing in any asset shows two flies touching.

## Insects (items 1-3)

| name | what / real-world look | facing, anchor, size | shots |
|---|---|---|---|
| `cicada` | Periodical cicada (Magicicada), side view. Black body, bright red-orange eyes, clear wings with orange veins folded tent-like over the abdomen, orange legs. | Facing right, anchor centre, about 400x170 (wings included). | s005, s008, s011-s013, s016, s020, s023, s025-s028, s083 |
| `cicada_infected` | The same cicada geometry with the rear third of the abdomen gone. A chalky white rounded plug of spores sits where the last segments were (soft off-white, a few grey speckles). Wings intact. | Same as `cicada`. | s006, s014-s022, s030, s265-s266 |
| `cicada_nymph` | Brown cicada nymph underground: hunched, big digging front legs, pale brown shell, small dark eyes, angled as if digging up. | Facing up-right, anchor centre, about 300x200. | s008-s010, s030 |
| `tree_branch` | Long horizontal tree branch: brown bark `#7a4f2c` with darker underside and a few twig stubs, small leaf clusters near both ends. Cicadas, a songbird and the cap sit on it. | Anchor centre, about 1700x120. Branch centre line at local y 0, top surface at about y -25. Leaves stay within +-100 of the line. | s016, s019-s020, s025-s029 |
| `cicada_costume` | Doug's cicada onesie (worn): black felt suit over the torso, a tapering segmented black abdomen sticking out behind (to the left, x about -260..-100), clear plastic wings with orange marker veins as a cape, two big red pom-pom eyes on a headband beside the cap. | Worn prop, anchor = hips. | s002-s022, s024-s025 |
| `cicada_costume_half` | The same costume with the back end of the abdomen gone. A chalky white round plug shows at the cut. | Worn prop, anchor = hips. | s026-s028 |
| `cicada_costume_rear` | The popped-off back end of the costume: a black segmented felt cone with a white plug face, like a cork. | Anchor centre, about 200x140. Rotated in shots. | s026-s027 |
| `cicada_costume_flat` | The half costume lying empty and flat (rear missing), pom-pom eyes drooping, wings crumpled. | Anchor centre, about 470x150. | s029, s135 |
| `house_fly` | House fly, side view: grey striped thorax, grey-buff abdomen with darker patches, big dark-red eyes, clear wings folded flat over the back, bristly legs. | Facing right, anchor centre, about 350x200. Also rotated -90 to climb glass. | s005, s032-s033, s035, s037-s038, s041, s043, s048-s050, s057, s083 |
| `fly_death_pose` | Entomophthora "death pose": a dead house fly, side view. Body tilted head-down toward the surface, proboscis pressed down, legs braced out stiff, both wings raised high up and away from the body in a V (about 60 degrees above the back). Matte, slightly swollen abdomen. No bands. | Facing right, anchor centre, about 380x360. | s031, s034, s039-s041, s044, s265-s266 |
| `fly_death_pose_banded` | The same geometry. Pale cream `#f3ecd0` fuzzy bands run across the abdomen between the dark segments, with 3-4 tiny soft white spore puffs around the body. Cartoon, never a wound. This is the dead female. Draw her alone. | Same as above. | s044, s047-s050, s057 |
| `fly_costume` | Doug's house-fly onesie (worn): grey felt suit with black thorax stripes, big dark-red mesh goggle eyes on a headband beside the cap, clear plastic wings folded flat behind the back. | Worn prop, anchor = hips. | s031-s052 |
| `fly_costume_wings_up` | The same costume with both wings raised high in a V above and behind the shoulders, like the death pose. Must work with `pose: arms_up`: the wings sit behind the arms. | Worn prop, anchor = hips. | s053-s054 |
| `fly_costume_banded` | `fly_costume_wings_up` plus pale cream fuzzy bands across the suit's belly and 2-3 small white puffs. | Worn prop, anchor = hips. | s055 |
| `fly_costume_flat` | The empty fly suit lying flat, wings still up but crumpled, goggles askew. | Anchor centre, about 470x150. | s056, s135 |
| `alarm_clock` | Classic twin-bell wind-up alarm clock: red body, two silver bells and a hammer, white face, black hands at about 6:00, small feet. | Anchor centre, about 220x260. | s043, s121, s127-s132 |
| `ireland_map` | The island of Ireland plus the west of Great Britain (Wales and northern England), world_map style: flat green land, dark green outline, light blue sea, black frame, faint NI border, no labels. Projection `x = (lon + 6.5) * 70`, `y = -(lat - 53.5) * 115`. Frame lon -11..-1, lat 50.5..56 (x -315..385, y -288..345). | Anchor (0,0) = lon -6.5 / lat 53.5. | s059, s073-s074 |
| `gunpowder_store` | Victorian red-brick gunpowder storeroom (Castle Espie style): small single-storey building, slate roof, heavy arched wooden door, one tiny barred vent, ivy on one corner. A painted sign over the door reads **GUNPOWDER STORE** (the only text). | Anchor bottom-centre, about 700x500. | s060, s063 |
| `cave_spider` | Orb-weaving cave spider (Meta menardi / Metellina merianae), top-down: glossy chestnut-brown body, darker banding, long banded legs (front pair longest), small cephalothorax, eight tiny eye dots. Creepy, not cute. | Head facing right, anchor centre, legspan about 400x360. | s005, s065-s072, s076-s078, s083 |
| `cave_spider_fuzz` | Gibellula-infected cave spider. Same top-down geometry, entirely coated in soft white cotton-wool fuzz. The legs read as stiff fuzzy white sticks, with a little pale spray halo. No gore. | Same as `cave_spider`. | s058, s061-s062, s064, s069-s070, s080, s265-s266 |
| `spider_costume` | Doug's spider onesie (worn): dark brown felt suit, four extra stuffed felt legs (two each side) sticking out from the torso and bending down at the knee, a row of small black bead eyes on a headband beside the cap. Also drawn upside down (group rotate 180). | Worn prop, anchor = hips. | s058-s078 |
| `spider_costume_fuzz` | The empty spider costume stuck flat to a cave ceiling, top-down, legs splayed, entirely covered in white fuzz. | Anchor centre, about 500x400. | s079, s135 |

## Whole species (items 4-5)

| name | what / real-world look | facing, anchor, size | shots |
|---|---|---|---|
| `frog_costume` | Doug's frog onesie (worn): green `#5f9a3a` suit with a cream belly panel, dark green spots, webbed green mitts and flipper feet. The hood has two bulging gold frog eyes on top, either side of the cap (not covering it). Must also work waist-deep: the shotlist hides the legs under a water rect at hip height. | Worn prop, anchor = hips. | s081-s098, s100-s105 |
| `frog_costume_flat` | The empty frog suit floating flat on the water, flippers splayed, hood eyes drooping. | Anchor centre, about 470x150 (the water line passes through the middle). | s106, s135 |
| `lily_pad` | Round green lily pad with a V notch, 3/4 low view, lighter veins, a little water ring. The cap sits on top at local y about -30. | Anchor centre, about 360x100. | s106-s107 |
| `bat_hanging` | Hibernating little brown bat hanging upside down: brown fur, wings wrapped round the body, small ears, eyes closed, toes gripping. | Anchor = the feet grip point at the top (0,0); the body hangs down to y about +320, about 160 wide. | s115-s116, s123, s125 |
| `bat_white_nose` | `bat_hanging` geometry with soft white fuzz on the muzzle, the ear tips and the wing edges (white-nose syndrome). Cartoon fuzz, nothing raw. | Same as `bat_hanging`. | s108, s110-s114, s117, s120-s121, s265-s266 |
| `bat_costume` | Doug's bat costume (worn): brown-grey felt suit, scalloped felt wings from wrists to hips like a cape, two pointed ears on the hood beside the cap. Also drawn upside down (group rotate 180). | Worn prop, anchor = hips. | s108-s130 |
| `bat_costume_flat` | The empty bat suit lying flat on the cave floor, wings splayed, with a round white fuzzy cartoon nose patch on the hood. | Anchor centre, about 470x150. | s131-s133, s135 |
| `thermostat_dial` | Round wall thermostat: beige ring, white dial face with tick marks, a red pointer turned to the far right (max), red-to-blue arc. No numbers (the shotlist puts a label under it). | Anchor centre, about 240x240. | s119, s258-s263 |
| `fuel_gauge` | Car fuel gauge: half-circle dial, E and F at the ends, white face, red needle at about 1/4 (low), small fuel-pump icon. | Anchor centre, about 300x170. | s119 |

## People (items 6-10)

| name | what / real-world look | facing, anchor, size | shots |
|---|---|---|---|
| `dust_plume` | Billowing tan dust cloud (`#e2d3b0`, shaded `#c8b58a`), rolling lobes, a few drifting wisps at the edges. No stars, no limbs, no faces (unlike `dust_cloud`). | Anchor centre, about 700x460. | s145, s149, s151, s153-s154, s157, s265-s266 |
| `hard_hat` | Yellow construction hard hat as a worn prop. It perches *on top of* Doug's cap: the cap dome and brim stay visible below its rim. | Worn prop, anchor = hips (sits at about y -330..-420 at scale 1). | s153-s157 |
| `rye_stalk` | One rye stalk: thin golden stem with a long narrow seed head and long bristly awns. | Anchor bottom-centre, about 60x420. | s158-s160 |
| `rye_ergot` | The same stalk. One long curved dark purple-black ergot spur sticks out of the head where a grain should be, about 3x the length of a grain. | Anchor bottom-centre, about 80x440 (head at the top 160). | s158-s159, s161, s265-s266 |
| `grain_sack` | Burlap sack of rye grain, tied open, golden grain heaped at the mouth. | Anchor bottom-centre, about 360x420. Open top at local y about -250. | s163 |
| `medieval_cottage` | Medieval timber-framed cottage: whitewashed wattle walls, dark beams, thick straw thatch, small wooden door, one shuttered window. | Anchor bottom-centre, about 520x420. | s158-s160, s163-s167, s169, s175-s178 |
| `stone_hospital_medieval` | Small medieval stone hospital (Antonine order): grey stone hall, steep roof, arched door with a blue tau (T-shaped) cross over it, small bell gable. | Anchor bottom-centre, about 600x480. | s166-s167 |
| `medicine_bottle_plain` | Plain brown glass medicine bottle, white screw cap, blank white label (no text, no brand). | Anchor bottom-centre, about 140x260. | s173-s174, s238 |
| `wawel_cathedral` | Wawel Cathedral, Kraków, at night: grey-stone Gothic cathedral with the gold Sigismund Chapel dome and the clock and bell towers, lit windows warm yellow. Keep the tallest tower on the left half; the right third stays under about 500 px tall. | Anchor bottom-centre, about 1000x620. | s183 |
| `stone_tomb` | Sealed royal stone sarcophagus: pale grey-tan stone chest on a plinth, a flat lid with a simple carved crown, a cobweb on one corner. | Anchor bottom-centre, about 700x380. | s180-s181, s184-s185, s265-s266 |
| `stone_tomb_open` | The same tomb with the lid slid diagonally, a dark gap showing, a faint soft dust haze rising. Nothing inside visible. | Same as above. | s185-s186, s201-s204 |
| `newspaper_curse` | 1970s newspaper front page: generic masthead "THE DAILY NEWS", a giant headline **CURSE**, grey column lines, a small photo box with a tomb outline. No real paper names. | Anchor centre, about 520x640. | s187, s205 |
| `peanuts_and_corn` | A small pile of peanuts in shells next to a husked ear of corn, each with a few small yellow-green powdery mould spots. | Anchor centre, about 700x400. | s190-s191 |
| `petri_dish_mould` | `petri_dish` geometry with yellow-green powdery Aspergillus colonies inside. | Same as `petri_dish` (200x72, bottom-centre). | s188-s189, s193-s195 |
| `vial` | Small glass lab vial: white cap, clear pale liquid, a blank white label band (the shotlist puts the name in a label above). | Anchor bottom-centre, about 80x220. | s194, s196 |
| `paper_crown` | Gold paper party crown (zigzag points, a couple of stuck-on paper jewels), worn perched on top of the cap so the cap stays visible below. | Worn prop, anchor = hips (sits at about y -330..-430 at scale 1). | s201-s205 |
| `bc_map` | Southwest British Columbia, Vancouver Island, Washington and Oregon, world_map style: flat green land, dark outline, light blue Pacific and Salish Sea, faint state and border lines, black frame, no labels. Projection `x = (lon + 122.5) * 70`, `y = -(lat - 46.75) * 80`. Frame lon -129..-116, lat 42..51.5 (x -455..455, y -380..380). | Anchor (0,0) = lon -122.5 / lat 46.75. | s209, s216, s220, s224-s225 |
| `porpoise` | Harbour porpoise, side view: dark grey back, paler belly, small triangular dorsal fin, short blunt snout, no beak. | Facing right, anchor bottom-centre (belly line), about 420x160. | s210-s211 |
| `llama` | Llama standing: cream-and-brown wool, long neck, banana ears, calm half-lidded eye. | Facing right, anchor bottom-centre, about 300x420. | s210-s211 |
| `hospital_building` | Plain modern hospital seen only from outside: pale concrete block, a grid of blue windows, a glass entrance, a small red cross sign on the roof edge. No people, no beds, nothing visible through the windows. | Anchor bottom-centre, about 900x620. | s240-s242 |
| `petri_dish_auris` | `petri_dish` geometry with smooth creamy-white yeast colonies (Candida auris) inside. | Same as `petri_dish`. | s231, s233, s250, s265-s266 |
| `spore_puff_walk` | A fuzzy off-white spore clump (soft cloud-like lobes, light grey shading and speckle) walking on two tiny stick legs. No face, no arms. Dry, not cute. | Anchor bottom-centre (feet), about 200x220. | s246, s249, s256-s257 |
| `spore_puff_sit` | The same spore clump sitting, stick legs out in front. | Anchor bottom-centre, about 220x180. | s260-s261 |
| `doug_fuzz_silhouette` | **New death variant (art director approves once, as a reusable `parasites` death).** Doug's `stand` silhouette at scale 1, filled with soft white fuzz (off-white with grey speckle and a fuzzy edge), no face. Doug's red cap (exact `doug_cap` geometry) sits on the head. | Anchor = hips, the same as Doug. | s261 |

## Notes for the art director
- **Background ramp (proposed, please confirm or adjust):**
  - Opener and Massospora: cream `#f4f1dc` sky over mould-green `#c9d6a3`.
  - Fly fungus: forest-green wall `#2f5a3a`, dusk glass `#f2a24a`, night `#1b2f5a`.
  - Cave spider: cave forest `#26402e`.
  - Chytrid: overcast `#b9c4a8` over swamp olive `#5d6b45`.
  - White-nose: cave grey `#5a5f66`.
  - Valley Fever: dry hills `#f6dcae` / `#f2c77a`.
  - Ergot: parchment `#e8dcc0` and rye `#d9b45a`.
  - Tomb: crypt `#3a3a44`.
  - C. gattii: deep forest `#1f3a2a`.
  - C. auris: sterile `#f3f1d6`.
- **WordArt on green or olive grounds** (cave, pond, forest) uses `top #ffffff`, `bottom #ffe24a`, `outline #1a1a1a`, so it is never lime on green.
- **Upside-down Doug** (spider ceiling walk s076-s078, bat hanging s127-s130) is a `group` with `rotate: 180` holding Doug plus the costume. The cap then hangs below the head, which reads as funny rather than broken in a test render. Please confirm it.
- **No `cap_off` anywhere.**
  - Deaths 140-144 show the empty `*_flat` costume, the `doug_cap` placed where the script puts it (branch, glass, thread, lily pad, cave floor) and ghost Doug with X eyes.
  - 145 and 146 are `on_back` + `dead` with the cap on.
  - 147 is `doug_fuzz_silhouette`.
- **Sober cards** have no Doug, no counter and no joke, in white text: s099 (chytrid), s152 (Northridge), s168 (ergot), s192 (tomb), s223 (C. gattii). The C. auris card is s243, in dark text on a pale card. The two tomb-death narration shots (s186, s189) carry no joke either.
