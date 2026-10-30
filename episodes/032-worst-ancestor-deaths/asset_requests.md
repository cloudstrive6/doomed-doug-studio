# 032-worst-ancestor-deaths: asset requests (director)

House style: detailed tier for creatures, fossils, places and props (dark outlines, flat fills, interior shading); crude tier only for worn props on Doug. Facing right unless noted. Sizes are local units at scale 1, and **the shotlist is laid out against these anchors, extents and key points**, so please keep them (a pink-box layout preview was checked against them). Requests are listed in priority order: the CASE FILE pair and the boss/creature drawings first (they are on screen most), then the fossils, then the one-shot props.

CD notes (brief section 7, decisions.md 2026-10-30): **bones and outlines only for every real individual** (Lucy, MH1/MH2, Shanidar 1, Taung, SK 54, OH 8, KNM-ER 1808, Peking Man): no hominin is ever drawn alive, dying, falling or being carried, and no juvenile is ever drawn at all except as a skull or bone on a white card. Damage is shown **on the fossil only** (clean bone, red crack lines or small dark holes), never wounds in flesh and never blood. No cartoon ape faces or 'caveman' look (the costume has no mask). Predators are predatory and heavy, never cute. Maps have no text. No real people.

Reused from the library (no request): `africa_map`, `bathroom_scale`, `beehive`, `boulder`, `calendar`, `cat`, `cave_lion`, `chimpanzee`, `croc_eyes_water`, `crocodile_skull`, `dinner_plate`, `doug_cap`, `exclamation_mark`, `explorer_1916`, `grass_tuft`, `hard_hat`, `heart_icon`, `honeybee`, `journal_paper`, `kitchen_chair`, `kitchen_counter`, `magnifying_glass`, `monkey`, `narrator_hand_pencil`, `old_book`, `question_mark`, `rainforest_tree`, `red_x`, `saltwater_crocodile`, `savanna_bush`, `scientist`, `shovel`, `small_car`, `south_africa_map`, `spotted_hyena`, `stone_tool`, `time_machine`, `warning_triangle`, `water_glass`, `water_splash_small`.

## `case_file`
**Episode device icon (CASE FILE meter, every shot).**

- Look: A crude MS Paint manila folder, closed, front view: flat buff-yellow `#e8c87a` with a darker `#c9a24a` tab on the top-left and a thin black outline; one white paper corner peeking out at the top right. No text (it must read at 66 px wide).
- Facing / anchor / size: Centre anchor, 300 x 220 (x -150..150, y -110..110). Used at scale 0.22 at (1384, 238), left of the `CASE FILE: n/8` label under the death counter.
- Notes: Bold, simple shapes only: at 0.22 a fine line disappears.
- Shots: 212 shots (s002-s213; every shot for the meter)
- **Done** (illustrator, 2026-10-30): `assets/library/case_file.json`, preview `assets/previews/032-worst-ancestor-deaths-assets-a.png`.

## `case_file_open`
**Episode device (the CASE FILE beats, 9 shots).**

- Look: A big crude manila folder lying open toward us with a white lined paper sheet paper-clipped on the front (silver clip top-centre). Folder buff `#e8c87a`, tab and edges `#c9a24a`, black outline 5-6. The folder tab on the top-left carries the printed words `CASE FILE` in black block capitals. The sheet itself is BLANK (very faint pale-blue rule lines are fine): the shotlist writes the lines on it.
- Facing / anchor / size: Centre anchor, 940 x 680 (x -470..470, y -340..340). **Blank text zone on the sheet: x -380..380, y -230..300.** The shotlist writes up to 9 centred lines starting at local y -170, 58 units apart (last at y +294), up to ~700 units wide, so keep that whole area white and free of clips, stains or rules darker than `#d8e4f0`. Used at scale 0.95 at (960, 600).
- Notes: Episode-only device (brief section 2). Not a tray, no slots (030). Lines are handwritten red (new) and dark grey (old) Comic Neue on top.
- Shots: s025, s047, s074, s098, s125, s152, s178, s201, s206 (9 shots)
- **Done** (illustrator, 2026-10-30): `assets/library/case_file_open.json`, preview `assets/previews/032-worst-ancestor-deaths-assets-a.png`.

## `tall_savanna_tree`
**Place (Lucy's Fall; reused at The Leopard).**

- Look: A tall, climbable East African savanna tree (a fig or tall acacia, NOT the flat-topped sunset `acacia_tree`): thick brown trunk `#7a4f2c` with bark strokes, a few sturdy horizontal limbs, an open medium-green crown `#4f8a3a` with darker clumps (`#3a6a2a`) so branches show through. Daylight look.
- Facing / anchor / size: Bottom-centre anchor, 600 x 900 (x -300..300, y -900..0). **Two flat standing branches (Doug stands on them):** the top branch runs right from the trunk, its top surface from (+60,-725) to (+290,-730), stand point **(+180,-725)**; a low branch runs left, top surface around **(-150,-420)** (x -260..-60). Both clearly thick enough to stand on. Keep the area above the top branch (x +100..+260, y -900..-735) free of dense leaves so Doug (scale 0.34) reads. A leopard (`leopard_lying`) also lies on the top branch at The Leopard.
- Notes: Used at scale 0.75 (trunk at x 760 or 900). Crown top must stay below y -900. Tree must read on a light sky `#8fd3ff` and on a dusk sky `#f6c45a`.
- Shots: s002, s005, s008, s014, s017, s018, s019, s020, s021, s026 ... (24 shots)
- **Done** (illustrator, 2026-10-30): `assets/library/tall_savanna_tree.json`, preview `assets/previews/032-worst-ancestor-deaths-assets-a.png`. Clear air kept above both standing branches.

## `pachycrocuta`
**Creature (the boss: giant hyena).**

- Look: Pachycrocuta brevirostris standing, side view facing right: a heavy, low, bear-bulky hyena, sloping back from high shoulders, short thick legs, **a huge broad head with massive jaws**, dark muzzle, round ears, shaggy sandy-brown `#9a7a4a` coat with faint darker spots. Mean small eye under a heavy brow. Clearly bigger and heavier than `spotted_hyena`, but about the same height.
- Facing / anchor / size: Bottom-centre anchor (feet on y=0), 760 x 330 (x -360..400, y -330..0). **Shoulder top at (+150,-300); jaw at (+360,-230).**
- Notes: Used at 0.55-1.1, often as a black silhouette with a red glow on night backgrounds (`#2b2f36`): give it a mid-tone fill so it reads at night, and a clean silhouette.
- Shots: s003, s183, s185, s186, s191, s192, s193, s194, s195, s204 (10 shots)
- **Done** (illustrator, 2026-10-30): `assets/library/pachycrocuta.json`, preview `assets/previews/032-worst-ancestor-deaths-assets-a.png`.

## `crowned_eagle`
**Creature (The Eagle).**

- Look: African crowned eagle perched, side/3/4 view facing right: dark slate-grey back and wings, pale cream chest heavily barred and blotched black-brown, a raised double crest on the head, hooked dark beak with yellow cere, fierce pale eye under a heavy brow, thick barred legs and **huge yellow feet with long black talons** gripping the perch. Predatory, not cute.
- Facing / anchor / size: Bottom-centre anchor = talons on the perch line (y=0), 300 x 420 (x -150..150, y -420..0).
- Notes: Used at 0.6-1.0, also as a silhouette with a red glow (keep a clean outline: crest and talons must read in silhouette). Stands on a bathroom scale in one beat.
- Shots: s079, s081, s083, s093, s094, s095, s099, s100, s105 (9 shots)
- **Done** (illustrator, 2026-10-30): `assets/library/crowned_eagle.json`, preview `assets/previews/032-worst-ancestor-deaths-assets-a.png`.

## `horned_crocodile`
**Creature (Crocodylus anthropophagus).**

- Look: A big crocodile, side view facing right, standing low: olive-grey `#6b7a4a` with darker back blotches, pale yellowish belly, bony scute rows, long broad snout with interlocking teeth on the closed jaw line, yellow slit-pupil eye, and **two small raised horns (bony bosses) just behind and above the eyes**, its defining feature.
- Facing / anchor / size: Bottom-centre anchor (feet on y=0), 1000 x 220 (x -500..500, y -220..0). **Horns at (+300,-170).**
- Notes: Used at 0.4-0.9, also as a silhouette with a thin red rim in water and as a dark shape under the water (death 258). Must read longer than `small_car` at 1.67.
- Shots: s133, s134, s137, s138, s139, s140, s141, s150, s151, s157 (10 shots)
- **Done** (illustrator, 2026-10-30): `assets/library/horned_crocodile.json`, preview `assets/previews/032-worst-ancestor-deaths-assets-a.png`.

## `leopard_lying`
**Creature (The Leopard on its branch).**

- Look: The same leopard lying along a tree branch, facing LEFT, front legs dangling over each side, tail hanging down, head turned to look down at the ground. No prey drawn, nothing in its paws.
- Facing / anchor / size: Anchor (0,0) = belly on the branch line at the body centre; 520 x 200 (x -260..260, y -170..+30, legs and tail may hang lower to about +110).
- Notes: Placed on the top branch of `tall_savanna_tree` at 0.55; also a silhouette with a red glow once (keep legs and tail clear).
- Shots: s106, s107, s120, s121, s122, s124, s130 (7 shots)
- **Done** (illustrator, 2026-10-30): `assets/library/leopard_lying.json`, preview `assets/previews/032-worst-ancestor-deaths-assets-a.png`. Checked in place on `tall_savanna_tree` at 0.55: belly sits on the branch line, the branch shows under it. Note: at 0.55 the cat (286 px) is longer than the top branch (about 172 px at 0.75), so the tail end overhangs the branch tip.

## `leopard`
**Creature (The Leopard).**

- Look: Adult leopard standing, side view facing right: golden `#d9a441` coat with black rosettes, pale belly, long tail with a dark tip, small ears, pale green eye under a heavy brow, calm stare. Heavy shoulders. Predatory, not cute.
- Facing / anchor / size: Bottom-centre anchor (paws on y=0), 600 x 330 (x -300..300, y -330..0).
- Notes: Usually flipped to face Doug. Also used as a black silhouette (purple glow) at The Bad Liver.
- Shots: s126, s127, s128, s129, s179 (5 shots)
- **Done** (illustrator, 2026-10-30): `assets/library/leopard.json`, preview `assets/previews/032-worst-ancestor-deaths-assets-a.png`.

## `sk54_skull_cap`
**Fossil (SK 54).**

- Look: The back of a young skull cap (calvaria) seen from behind: a cream-tan rounded dome `#e8d6a8` with a broken lower edge, and **two neat round holes** in the lower back, side by side. Clean bone, no blood, nothing else.
- Facing / anchor / size: Centre anchor, 420 x 300 (x -210..210, y -150..150). **Hole centres at (-55,+40) and (+55,+40), radius about 14** (110 units apart).
- Notes: Used at 1.0 on a white card. Sensitivity: young individual, bone only.
- Shots: s108, s109, s112, s113, s114, s115, s116, s117, s118 (9 shots)
- **Done** (illustrator, 2026-10-30): `assets/library/sk54_skull_cap.json`, preview `assets/previews/032-worst-ancestor-deaths-assets-a.png`.

## `leopard_jaw`
**Fossil (SK 349 leopard lower jaw).**

- Look: A leopard's lower jaw held **upside-down above the skull**, as in Brain's famous demonstration: cream-grey fossil jaw bone with two long lower canines pointing **down**, a few smaller teeth between them.
- Facing / anchor / size: Centre anchor, 380 x 200 (x -190..190, y -100..100), jaw body x -190..190, y -100..+40. **Canine tips at (-55,+95) and (+55,+95)** (same 110 spacing as the SK 54 holes, so the fangs slot into them at the same scale).
- Notes: Used at 1.0 hovering 250 above the cap, then dropped into place (canine tips on the holes).
- Shots: s108, s109, s117, s118 (4 shots)
- **Done** (illustrator, 2026-10-30): `assets/library/leopard_jaw.json`, preview `assets/previews/032-worst-ancestor-deaths-assets-a.png`. Checked dropped onto `sk54_skull_cap` at the same scale: canine tips land on the hole centres.

## `lucy_skeleton`
**Fossil (Lucy, AL 288-1).**

- Look: Lucy's partial skeleton laid out flat as in the famous museum layout: about 40 percent of a small skeleton, cream-to-tan bone `#e8d6a8` with a brown outline, darker `#b89a6a` shading, missing pieces simply absent (gaps, not drawn as dashed). Skull fragments at the top, jaw, both upper arm bones, a forearm, ribs pieces, pelvis, a thigh bone and lower leg pieces. Bones only, clean, no damage marks, no blood.
- Facing / anchor / size: Centre anchor, 420 x 700 (x -210..210, y -350..350). **The upper arm bone on the viewer's LEFT (her right humerus) has its top end at (-95,-205)**: the red arrow points there.
- Notes: Used at scale 0.8 on a white card. Sensitivity: real individual, keep it dignified, no face.
- Shots: s006, s007, s022, s023, s024 (5 shots)
- **Done** (illustrator): `assets/library/lucy_skeleton.json`, preview `assets/previews/032-worst-ancestor-deaths-assets-b1.png`

## `fossil_bone_pale`
**Generic hominin bone (many beats).**

- Look: Same shape as `fossil_bone` (a generic long bone with knobbly ends) but clean pale cream `#efe6d0`, tan outline `#8a6a3a`, soft `#d8c8a0` shading, one faint crack line. No tar, no brown stains.
- Facing / anchor / size: Centre anchor, 220 x 60 (x -110..110, y -30..30).
- Notes: Used at 0.33-1.4, often rotated; 40 copies make the 'as many as forty individuals' grid. Stands for the two Malapa victims, the leg bone OH 35, and the Peking Man remains: it must read as 'a bone', never as a body.
- Shots: s033, s037, s042, s043, s045, s046, s048, s060, s141, s146, s148, s149, s187, s190 (14 shots)
- **Done** (illustrator): `assets/library/fossil_bone_pale.json`, preview `assets/previews/032-worst-ancestor-deaths-assets-b1.png`

## `humerus_cracked`
**Fossil detail (Lucy's broken upper arms).**

- Look: A single upper arm bone (humerus), vertical, head (ball end) at the top: cream `#efe2c0` bone, brown outline, light shading. A short web of bright red `#e0201b` crack lines across the top end (the head and neck), 3-4 jagged lines, nothing else red. Cartoon, clean.
- Facing / anchor / size: Centre anchor, 100 x 420 (x -50..50, y -210..210). Top of the head at (0,-200).
- Notes: Used at 0.6-1.2, sometimes two side by side.
- Shots: s010, s011, s012, s013, s015, s016 (6 shots)
- **Done** (illustrator): `assets/library/humerus_cracked.json`, preview `assets/previews/032-worst-ancestor-deaths-assets-b1.png`

## `skeleton_diagram`
**Diagram (Shanidar 1's injuries).**

- Look: A simple front-view adult human skeleton diagram, standing, arms slightly away from the body: cream bones `#efe2c0`, brown outline, plain and clinical (like a school chart), skull with two eye sockets and small ear bumps. No damage drawn, no blood, no face expression.
- Facing / anchor / size: Centre anchor, 360 x 900 (x -180..180, y -450..450). **Key points (arrows aim here):** his left eye socket (viewer's right) at (+28,-385); ear bump on the viewer's left at (-62,-375); his right upper arm (viewer's left) mid-shaft at (-120,-200); the same forearm at (-140,-60).
- Notes: Used at 0.62 on a white card.
- Shots: s055, s063, s064, s065, s066, s068, s069 (7 shots)
- **Done** (illustrator): `assets/library/skeleton_diagram.json`, preview `assets/previews/032-worst-ancestor-deaths-assets-b1.png`

## `taung_skull`
**Fossil (the Taung skull).**

- Look: Front view of a small fossil skull (Taung 1): cream-tan bone `#e8d6a8` with a darker natural-cast brain part behind, two big round eye sockets, short face, small jaw with teeth. Bone only, no skin, no expression, not cute. A small dark hole at the bottom of each eye socket.
- Facing / anchor / size: Centre anchor, 300 x 340 (x -150..150, y -170..170). Eye socket centres (+/-60,-30); **socket floors (holes) at (+/-60,-8)** (arrow targets).
- Notes: Sensitivity HIGH: a real young individual. Clinical, dignified. Used at 0.95-1.1 on a white card.
- Shots: s082, s085, s087, s091, s092, s097 (6 shots)
- **Done** (illustrator): `assets/library/taung_skull.json`, preview `assets/previews/032-worst-ancestor-deaths-assets-b1.png`

## `foot_skeleton`
**Fossil (OH 8 foot).**

- Look: Side view of a human-relative foot skeleton: ankle bones (heel, talus) on the left, five metatarsals fanning to the right, cream `#efe2c0` bone, brown outline. A few small round dark pits (tooth marks) on the ankle bones. No toes needed (OH 8 has none). Clean, no blood.
- Facing / anchor / size: Centre anchor, 460 x 220 (x -230..230, y -110..110). **Ankle bones at (-150,-40); foot bones at (+60,0)** (arrow targets).
- Notes: Used at 1.2 on a white card.
- Shots: s141, s142, s143, s144, s148, s149 (6 shots)
- **Done** (illustrator): `assets/library/foot_skeleton.json`, preview `assets/previews/032-worst-ancestor-deaths-assets-b1.png`

## `small_table`
**Prop (Doug's dinner table).**

- Look: A small plain wooden table, side view: tabletop `#a0522d` with a darker edge, two straight legs, and a white tablecloth hanging a little over the front edge.
- Facing / anchor / size: Bottom-centre anchor, 520 x 300 (x -260..260, y -300..0). **Tabletop surface at y -300.**
- Notes: Used at 0.8-0.9 next to `kitchen_chair` (seat at -195).
- Shots: s160, s173, s179, s180, s181, s182 (6 shots)
- **Done** (illustrator): `assets/library/small_table.json`, preview `assets/previews/032-worst-ancestor-deaths-assets-b2.png`

## `liver_plate`
**Prop (The Bad Liver).**

- Look: A white dinner plate (same as `dinner_plate`: low 3/4 view, blue rim line) with a glossy dark-red-brown cartoon liver `#7a2a22` (smooth lobed shape, white highlight) on it. Food, not anatomy: no veins, no blood pool.
- Facing / anchor / size: Centre anchor, 300 x 105 (x -150..150, y -60..45); plate bottom at y +45.
- Notes: On `small_table`.
- Shots: s162, s170, s173, s176, s180 (5 shots)
- **Done** (illustrator): `assets/library/liver_plate.json`, preview `assets/previews/032-worst-ancestor-deaths-assets-b2.png`

## `liver_plate_flag`
**Prop (Doug's dinner).**

- Look: `liver_plate` plus a cocktail-stick flag stuck in the liver: a small white paper flag that reads **LEOPARD** in black block capitals (the only text).
- Facing / anchor / size: Centre anchor, 300 x 245 (x -150..150, y -200..45); plate bottom at y +45; flag text must read at scale 0.8.
- Shots: s160, s179 (2 shots)
- **Done** (illustrator): `assets/library/liver_plate_flag.json`, preview `assets/previews/032-worst-ancestor-deaths-assets-b2.png`

## `napkin_bib`
**Worn prop (napkin tucked in).**

- Look: A white napkin tucked in at Doug's neck, hanging over his chest as a triangle, with two small corner points at the collar. Thin grey outline, faint fold line.
- Facing / anchor / size: Anchor = Doug's hips at scale 1 **in the `sit` pose** (the sit pose drops the hips 70 units; check the neck point against the rig): napkin from just under the neck down to mid-chest, about 120 wide. Drawn after Doug at the same x/y/scale.
- Notes: Used at scale 0.55 in four shots, including `sit_thumbs_up`. Must never cover the face.
- Shots: s179, s180, s181, s182 (4 shots)
- **Done** (illustrator): `assets/library/napkin_bib.json`, preview `assets/previews/032-worst-ancestor-deaths-assets-b2.png`

## `early_human_costume`
**Worn prop (costume gag, once).**

- Look: An adult-sized costume of a small upright early-human relative worn over Doug's `stand` pose: a shaggy brown fur bodysuit `#7a5a3a` (darker `#5a3e22` strokes) covering torso, arms and legs, short fur mitts and bare-looking fur feet. **No mask, no ape face, no hood**: Doug's head, face and red cap stay fully visible above the collar (brief: adult-coded, no cartoon ape faces).
- Facing / anchor / size: Anchor = Doug's hips at scale 1, `stand` pose, facing right: collar at about y -150 (neck), suit to the feet at y +152, arms following the stand pose. Drawn after Doug at the same x/y/scale.
- Notes: Shots use Doug scale 0.55. Check it against the rig with `art` before handing over.
- Shots: s127, s128, s129 (3 shots)
- **Done** (illustrator): `assets/library/early_human_costume.json`, preview `assets/previews/032-worst-ancestor-deaths-assets-b2.png`

## `crowned_eagle_flying_cap`
**Creature (The Eagle steals the cap).**

- Look: The same crowned eagle in flight, wings spread wide, flying up and to the right, legs down, holding **Doug's red cap** (`doug_cap` exact shape and colour `#e0201b`) in its talons. Nothing else carried.
- Facing / anchor / size: Centre anchor, 600 x 400 (x -300..300, y -200..200); cap at about (0,+150).
- Notes: Used at 0.75, 0.45 and 0.25 as it flies away. Only cap in the frame (Doug is `cap_off`).
- Shots: s101, s102, s103 (3 shots)
- **Done** (illustrator): `assets/library/crowned_eagle_flying_cap.json`, preview `assets/previews/032-worst-ancestor-deaths-assets-b2.png`

## `hyena_cub`
**Creature ("hi friend?").**

- Look: A giant-hyena cub sitting, facing right: dark brown fluffy coat (spotted hyena cubs are dark), round ears, big head, small dark eye under a brow, neutral wary look (not kawaii, no shine, no smile). Like `cave_lion_cub` in tone.
- Facing / anchor / size: Bottom-centre anchor, 220 x 200 (x -110..110, y -200..0).
- Notes: Flipped to face Doug; on night ground, so keep the outline readable on `#3a2e28`.
- Shots: s199, s200, s202, s203, s204 (5 shots)
- **Done** (illustrator): `assets/library/hyena_cub.json`, preview `assets/previews/032-worst-ancestor-deaths-assets-b2.png`

## `pachycrocuta_sleeping`
**Creature (den cross-section).**

- Look: The same giant hyena lying curled asleep on its side, head on its paws, eyes shut. Not cute.
- Facing / anchor / size: Bottom-centre anchor, 600 x 200 (x -300..300, y -200..0).
- Notes: In a dark den cross-section (`#120a0c`): mid-tone fill.
- Shots: s199, s200 (2 shots)
- **Done** (illustrator): `assets/library/pachycrocuta_sleeping.json`, preview `assets/previews/032-worst-ancestor-deaths-assets-b2.png`

## `small_bone_heap`
**Prop (bones under nests, in dens, in the trap).**

- Look: A low heap of small cream animal bones: little ribs, small limb bones, a couple of tiny rodent/hare skulls, scattered vertebrae, in two tones of cream with brown outlines. No human skull, no monkey face, nothing that reads as a child.
- Facing / anchor / size: Bottom-centre anchor, 420 x 160 (x -210..210, y -160..0).
- Notes: Used at 0.4-1.1 on dark and light grounds.
- Shots: s048, s088, s090, s121, s198, s199, s200 (7 shots)
- **Done** (illustrator): `assets/library/small_bone_heap.json`, preview `assets/previews/032-worst-ancestor-deaths-assets-b2.png`

## `cave_mouth_large`
**Place (Shanidar Cave).**

- Look: A wide limestone cave mouth in a grey-brown mountainside: rock face `#7a6a58` with lighter `#9a8a76` ledges and cracks, a big dark arch opening `#2e241c` (darker toward the inside), a few loose blocks on the floor at the entrance. The roof of the arch is rough and blocky (the shotlist hangs small loose rocks just under it).
- Facing / anchor / size: Bottom-centre anchor, 1200 x 600 (x -600..600, y -600..0). **Dark arch opening: x -380..380, arch top at y -480.** Keep the inside of the arch plain dark so Doug and rocks read.
- Notes: Used at 0.75 on the Shanidar mountain backdrop (sky `#b9cde0`).
- Shots: s054, s056, s057, s059 (4 shots)
- **Done** (illustrator, 2026-10-30): `assets/library/cave_mouth_large.json`, preview `assets/previews/032-worst-ancestor-deaths-assets-c.png` (fitted sheet `032-worst-ancestor-deaths-assets-c-fit.png`).

## `femur_extra_bone`
**Fossil (KNM-ER 1808).**

- Look: A horizontal thigh bone: cream ends `#efe2c0`, and along the whole shaft (x -220..220) a thick, lumpy, uneven grey-brown `#9a8a76` outer layer, like bumpy plaster, shaded so it clearly sits ON the bone.
- Facing / anchor / size: Centre anchor, 700 x 160 (x -350..350, y -80..80).
- Notes: Used at 0.9-1.25 on a white card. Clinical, not gross.
- Shots: s161, s165, s166, s169 (4 shots)
- **Done** (illustrator, 2026-10-30): `assets/library/femur_extra_bone.json`, preview `assets/previews/032-worst-ancestor-deaths-assets-c.png` (fitted sheet `032-worst-ancestor-deaths-assets-c-fit.png`).

## `bone_cross_section`
**Diagram (1808 bone layers).**

- Look: A bone cross-section disc: dark-cream marrow centre, a clean cream ring of normal bone, and around it a rough, lumpy grey `#9a8a76` outer ring. Black outline.
- Facing / anchor / size: Centre anchor, 360 x 360 (x -180..180, y -180..180).
- Shots: s166, s175 (2 shots)
- **Done** (illustrator, 2026-10-30): `assets/library/bone_cross_section.json`, preview `assets/previews/032-worst-ancestor-deaths-assets-c.png` (fitted sheet `032-worst-ancestor-deaths-assets-c-fit.png`).

## `monkey_skull`
**Fossil/comparison (eagle-prey monkey skull).**

- Look: Front view of a monkey skull, same drawing language as `taung_skull` but clearly a monkey (narrower, more muzzle, smaller braincase), cream bone. A small dark puncture at the bottom of each eye socket.
- Facing / anchor / size: Centre anchor, 260 x 300 (x -130..130, y -150..150). **Socket floors at (+/-50,-10).**
- Notes: Used side by side with `taung_skull`.
- Shots: s089, s092 (2 shots)
- **Done** (illustrator, 2026-10-30): `assets/library/monkey_skull.json`, preview `assets/previews/032-worst-ancestor-deaths-assets-c.png` (fitted sheet `032-worst-ancestor-deaths-assets-c-fit.png`). Punctures at (+/-50,-16), just above the socket floor line (y -10).

## `eagle_nest_tree`
**Place (crowned eagle nests, Ivory Coast).**

- Look: A tall forest tree with a huge stick platform nest in the top fork: grey-brown trunk, dark green crown `#2e5a2a` around and above the nest, the nest a wide flat heap of sticks with a few green leaves on top.
- Facing / anchor / size: Bottom-centre anchor, 700 x 950 (x -350..350, y -950..0). Nest top surface at (0,-800).
- Notes: Used at 0.65 with `small_bone_heap` at its foot.
- Shots: s088, s090 (2 shots)
- **Done** (illustrator, 2026-10-30): `assets/library/eagle_nest_tree.json`, preview `assets/previews/032-worst-ancestor-deaths-assets-c.png` (fitted sheet `032-worst-ancestor-deaths-assets-c-fit.png`).

## `rock_with_collarbone`
**Fossil find (Malapa, 2008).**

- Look: A grey-brown breccia rock `#8a7a6a` (lumpy, pebbly texture, darker underside) with a pale cream collarbone `#efe2c0` (slim S-shaped bone) partly embedded and sticking out of the top right. No hands, no person.
- Facing / anchor / size: Centre anchor, 400 x 260 (x -200..200, y -130..130). Collarbone tip at **(+150,-60)** (arrow target).
- Notes: Used at 1.0 on a white card.
- Shots: s034, s035 (2 shots)
- **Done** (illustrator, 2026-10-30): `assets/library/rock_with_collarbone.json`, preview `assets/previews/032-worst-ancestor-deaths-assets-c.png` (fitted sheet `032-worst-ancestor-deaths-assets-c-fit.png`).

## `telephone_pole`
**Scale prop (12 m fall).**

- Look: A plain wooden telephone pole: brown `#7a5a3a` pole with grain lines, one crossbar near the top with three small glass insulators, a short wire stub on each side. No signs.
- Facing / anchor / size: Bottom-centre anchor, 240 x 900 (x -120..120, y -900..0), **exactly as tall as `tall_savanna_tree`** (same 900 units).
- Notes: Stands next to the tree at the same scale 0.75.
- Shots: s020, s021 (2 shots)
- **Done** (illustrator, 2026-10-30): `assets/library/telephone_pole.json`, preview `assets/previews/032-worst-ancestor-deaths-assets-c.png` (fitted sheet `032-worst-ancestor-deaths-assets-c-fit.png`).

## `tall_savanna_tree_snapped`
**Place (death 254).**

- Look: Same tree as `tall_savanna_tree` (same trunk, crown, low branch, same footprint), but the top branch has snapped near the trunk at (+60,-725): the broken limb hangs down at a steep angle, a pale splintered break showing, and its tip ends near **(+170,-700)** where the cap hangs (the shotlist puts `doug_cap` 20 units below that point).
- Facing / anchor / size: Bottom-centre anchor, 600 x 900, identical to `tall_savanna_tree`.
- Notes: Shown on a near-black background (cut to black): keep the trunk mid-brown and the leaves mid-green so it reads on `#0b0b0b`.
- Shots: s029 (1 shot)
- **Done** (illustrator, 2026-10-30): `assets/library/tall_savanna_tree_snapped.json`, preview `assets/previews/032-worst-ancestor-deaths-assets-c.png` (fitted sheet `032-worst-ancestor-deaths-assets-c-fit.png`). Built from a copy of `tall_savanna_tree` (crown, trunk, low branch identical); only the top branch is replaced. The droop is shallow (about 13 degrees), not steep, because the fixed break (+60,-725) and tip (~+178,-700) points allow only that; checked with `doug_cap` 20 below the tip on `#0b0b0b`.

## `plaster_skull_cast`
**Prop (Peking Man cast).**

- Look: A white plaster cast of a skull cap (low, long, heavy-browed fossil skull cap, no jaw) on a small square wooden plinth with a tiny blank paper label. Chalky white `#f2efe6`, grey shading.
- Facing / anchor / size: Bottom-centre anchor (plinth on y=0), 300 x 200 (x -150..150, y -200..0).
- Notes: On a shelf on a sober dark card `#1a1d22`.
- Shots: s207, s209 (2 shots)
- **Done** (illustrator, 2026-10-30): `assets/library/plaster_skull_cast.json`, preview `assets/previews/032-worst-ancestor-deaths-assets-c.png` (fitted sheet `032-worst-ancestor-deaths-assets-c-fit.png`).

## `coat_hook`
**Prop (closing image).**

- Look: A simple wooden coat-hook board on a wall: a short `#a0522d` plank with two black metal hooks. The cap hangs on the right hook.
- Facing / anchor / size: Centre anchor, 200 x 160 (x -100..100, y -80..80). **Cap hang point (+40,+30)** (`doug_cap` at 0.5 placed there).
- Notes: On a cream home wall `#f4f1dc`.
- Shots: s212, s213 (2 shots)
- **Done** (illustrator, 2026-10-30): `assets/library/coat_hook.json`, preview `assets/previews/032-worst-ancestor-deaths-assets-c.png` (fitted sheet `032-worst-ancestor-deaths-assets-c-fit.png`).

## `iraq_map`
**Map (Shanidar).**

- Look: Map of Iraq and its neighbours in the `world_map` style: flat green land, dark green outline, light-blue sea (the Persian Gulf corner), white wave ticks, black frame, no labels. Faint dashed borders; the Zagros mountains as a few darker green bumps in the north-east (Iraqi Kurdistan).
- Facing / anchor / size: Centre anchor, 1100 x 900. **Projection: lon 38..49 E, lat 29..38 N, 100 px per degree, centre lon 43.5 / lat 33.5: x = (lon - 43.5) x 100, y = -(lat - 33.5) x 100.** Shanidar Cave (44.22 E, 36.83 N) = (+72,-333): the shotlist draws a red ring there, keep it clear of the frame.
- Notes: Used at 0.6 centred (900, 600).
- Shots: s058 (1 shot)
- **Done** (illustrator, 2026-10-30): `assets/library/iraq_map.json`, preview `assets/previews/032-worst-ancestor-deaths-assets-c.png` (fitted sheet `032-worst-ancestor-deaths-assets-c-fit.png`). Also has thin blue Tigris/Euphrates and Lake Urmia; Shanidar point is clear of the Zagros ticks.

## `china_map`
**Map (Zhoukoudian).**

- Look: Map of China and its neighbours in the `world_map` style (flat green land, dark green outline, light-blue sea with white wave ticks, black frame, no labels), including the Korean peninsula, the Bohai Sea and Taiwan.
- Facing / anchor / size: Centre anchor, 1240 x 720. **Projection: lon 73..135 E, lat 18..54 N, 20 px per degree, centre lon 104 / lat 36: x = (lon - 104) x 20, y = -(lat - 36) x 20.** Zhoukoudian near Beijing (115.93 E, 39.69 N) = (+239,-74): red ring there.
- Notes: Used at 0.9 centred (860, 620). Map is about the fossils only (brief risk: no modern politics).
- Shots: s189 (1 shot)
- **Done** (illustrator, 2026-10-30): `assets/library/china_map.json`, preview `assets/previews/032-worst-ancestor-deaths-assets-c.png` (fitted sheet `032-worst-ancestor-deaths-assets-c-fit.png`). No political borders drawn (brief: no modern politics); land, coast, Yellow River, Yangtze, Himalaya ticks, Lake Baikal only. Zhoukoudian point is clear.

## `sabretooth_skull`
**Fossil (Malapa death trap).**

- Look: Sabre-toothed cat skull, side view facing right: cream bone, big eye socket, long curved upper sabre fangs reaching below the lower jaw. Clean, no blood.
- Facing / anchor / size: Centre anchor, 340 x 220 (x -170..170, y -110..110).
- Notes: On a dark cave floor `#2a1d10`: give it a dark outline and a lighter fill so it reads.
- Shots: s048 (1 shot)
- **Done** (illustrator, 2026-10-30): `assets/library/sabretooth_skull.json`, preview `assets/previews/032-worst-ancestor-deaths-assets-c.png` (fitted sheet `032-worst-ancestor-deaths-assets-c-fit.png`). Checked on `#2a1d10`.

## `antelope_skull`
**Fossil (Malapa death trap).**

- Look: Antelope skull, side or 3/4 view facing left: long narrow cream skull with two ridged curved horns sweeping back. Clean.
- Facing / anchor / size: Centre anchor, 300 x 260 (x -150..150, y -130..130).
- Notes: Dark cave floor; same readable treatment as `sabretooth_skull`.
- Shots: s048 (1 shot)
- **Done** (illustrator, 2026-10-30): `assets/library/antelope_skull.json`, preview `assets/previews/032-worst-ancestor-deaths-assets-c.png` (fitted sheet `032-worst-ancestor-deaths-assets-c-fit.png`). Checked on `#2a1d10`.

## `seesaw`
**Prop (eagle weight gag).**

- Look: A plain playground seesaw: grey metal triangle pivot in the middle, long wooden plank `#a0522d` **tilted down on the LEFT** (the light cat's side stays down, that's the joke).
- Facing / anchor / size: Bottom-centre anchor, 960 x 290 (x -480..480, y -290..0). Plank top surface at the left end **(-330,-140)** (the cat sits there) and the right (raised) end **(+330,-260)** (the backpack sits there).
- Notes: Used at 1.0 with `cat` (0.55) and `hiking_backpack`.
- Shots: s096 (1 shot)
- **Done** (illustrator, 2026-10-30): `assets/library/seesaw.json`, preview `assets/previews/032-worst-ancestor-deaths-assets-c.png` (fitted sheet `032-worst-ancestor-deaths-assets-c-fit.png`). A rubber bumper sits under the low left end so it rests on something.

## `hiking_backpack`
**Prop (20 kg).**

- Look: A big stuffed blue hiking backpack with straps, side pockets and a rolled sleeping mat on top. Plain, no logos, no text.
- Facing / anchor / size: Bottom-centre anchor, 240 x 300 (x -120..120, y -300..0).
- Shots: s096 (1 shot)
- **Done** (illustrator, 2026-10-30): `assets/library/hiking_backpack.json`, preview `assets/previews/032-worst-ancestor-deaths-assets-c.png` (fitted sheet `032-worst-ancestor-deaths-assets-c-fit.png`).

## `two_fingers`
**Scale prop (33 mm).**

- Look: Two human fingers (index and middle) held together, pointing up, seen from the back with the nails showing: skin `#f2c9a5`, darker `#d9a27f` side, cut off flat at the bottom by a sleeve cuff (no hand or arm). Same tier as `fingertip`.
- Facing / anchor / size: Centre anchor, 160 x 340 (x -80..80, y -170..170). **The two fingers together are exactly 110 units wide** (matches the hole spacing on `sk54_skull_cap`).
- Shots: s115 (1 shot)
- **Done** (illustrator, 2026-10-30): `assets/library/two_fingers.json`, preview `assets/previews/032-worst-ancestor-deaths-assets-c.png` (fitted sheet `032-worst-ancestor-deaths-assets-c-fit.png`).

## `lumpy_paint_pipe`
**Analogy prop ("a lumpy second coat of paint on a pipe").**

- Look: A horizontal grey metal pipe `#8d9096` with flanged ends, covered along the middle by a thick, lumpy, drippy second coat of cream paint `#efe6d0` with a few drips hanging down.
- Facing / anchor / size: Centre anchor, 700 x 120 (x -350..350, y -60..60).
- Shots: s167 (1 shot)
- **Done** (illustrator, 2026-10-30): `assets/library/lumpy_paint_pipe.json`, preview `assets/previews/032-worst-ancestor-deaths-assets-c.png` (fitted sheet `032-worst-ancestor-deaths-assets-c-fit.png`).

## `four_story_building`
**Scale prop (14 m trench).**

- Look: Plain four-storey concrete block, same family as `six_story_building`: exactly four rows of four blue windows, flat roof with parapet.
- Facing / anchor / size: Bottom-centre anchor, 312 x 400 (x -156..156, y -400..0).
- Notes: Used at 1.3 inside a dark trench; keep the walls light.
- Shots: s062 (1 shot)
- **Done** (illustrator, 2026-10-30): `assets/library/four_story_building.json`, preview `assets/previews/032-worst-ancestor-deaths-assets-c.png` (fitted sheet `032-worst-ancestor-deaths-assets-c-fit.png`).

## `ten_story_building`
**Scale prop (30-50 m shaft).**

- Look: Plain ten-storey concrete block, same family as `six_story_building` / `eight_story_building`: light concrete, flat roof with parapet, exactly ten rows of four blue windows, floor lines.
- Facing / anchor / size: Bottom-centre anchor, 312 x 1000 (x -156..156, y -1000..0), 100 units per floor like the family.
- Notes: Used at 0.63 next to the cave shaft cross-section.
- Shots: s041 (1 shot)
- **Done** (illustrator, 2026-10-30): `assets/library/ten_story_building.json`, preview `assets/previews/032-worst-ancestor-deaths-assets-c.png` (fitted sheet `032-worst-ancestor-deaths-assets-c-fit.png`).

## `shipping_crate`
**Prop (December 1941).**

- Look: A plain closed wooden shipping crate, nailed shut: planks, corner posts, a diagonal brace, nail heads, a little straw poking out of one seam. No text, no stencils, nothing peeking out (the library `fossil_crate` shows a dinosaur skull, wrong here).
- Facing / anchor / size: Bottom-centre anchor, 400 x 260 (x -200..200, y -260..0).
- Notes: Sober card, no jokes.
- Shots: s208 (1 shot)
- **Done** (illustrator, 2026-10-30): `assets/library/shipping_crate.json`, preview `assets/previews/032-worst-ancestor-deaths-assets-c.png` (fitted sheet `032-worst-ancestor-deaths-assets-c-fit.png`).
