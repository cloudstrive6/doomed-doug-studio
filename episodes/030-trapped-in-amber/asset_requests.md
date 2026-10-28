# 030-trapped-in-amber: asset requests (director)

House style: detailed tier for creatures, specimens and props (dark outlines, flat fills, interior shading), crude tier only for the
narrator's hand. Facing right unless noted. Sizes are local units at scale 1; the shotlist was laid out against these extents, so please
keep the anchors and footprints. **Priority: `amber_bead` + `amber_bead_glint` (114 shots each) and the eight specimens that sit in them.**
CD notes (decisions.md): every creature menacing, never cute (no big eyes, no blush); the Jurassic Park card stays generic (no title, logo or
poster likeness); only the cap is ever sealed in amber, never Doug (the closing bead uses `doug_cap`, no new asset).

Reused from the library (no request): `ammonite`, `ancient_conifer_trunk`, `bank_card`, `carpenter_ant`, `cockroach`, `cockroach_costume`, `coin_generic`, `doug_cap`, `doug_sunglasses`, `eggshell_fragments`, `exclamation_mark`, `fallen_log`, `feathered_dinosaur`, `fern`, `fossil_bone`, `gall_mite`, `garden_spider`, `giant_isopod`, `golden_lancehead`, `gravestone`, `house_fly`, `insect`, `journal_paper`, `kitchen_timer`, `leaf`, `lizard`, `magnifying_glass`, `meltwater_wave`, `microscope`, `mosquito`, `new_zealand_map`, `old_drawing_card`, `palaeopython`, `question_mark`, `red_x`, `resin_drop`, `scientist`, `scientist_woman`, `seashell`, `shovel`, `songbird`, `time_machine`, `torch`, `tree_branch`, `warning_triangle`.

## `amber_bead`
**Prop (episode device, top priority).**

- Look: The polished amber piece every specimen sits in: a rounded, slightly irregular oval bead (not a perfect ellipse, one flatter side lower right), glossy golden `#e8a33a` with a lighter honey core `#ffd36b` (soft radial spray, brightest upper-left of centre), darker `#b07020` band along the lower-right rim, outline `#6b3a10` width 6. A few tiny pale bubbles near the rim only. **The core region x -230..230, y -155..155 must stay plain** (no streaks, bubbles or texture), because specimens are drawn on top of it.
- Facing / anchor / size: Centre anchor, 600 x 420 (x -300..300, y -210..210).
- Notes: Used as a sandwich: `amber_bead`, then the specimen asset(s) at bead-local coords, then `amber_bead_glint`, all inside one group (scale 0.22 in the tray, 0.42-1.15 on cards). Must read as amber at 130 px wide (tray). Amber-forest resin palette from the art bible.
- Shots: s002, s005, s006, s007, s008, s009, s010, s011, s012, s013, s014, s020, s021, s030, s032, s033, s034, s035, s036, s037, s040, s041, s042, s045, s046, s047, s049, s054, s055, s056, s057, s058, s059, s060, s061, s062, s066, s067, s068, s069, s070, s071, s076, s077, s078, s079, s080, s081, s082, s083, s084, s087, s088, s089, s090, s096, s097, s098, s099, s100, s104, s105, s106, s107, s108, s109, s110, s111, s112, s113, s114, s117, s118, s119, s120, s121, s122, s123, s130, s131, s132, s133, s135, s141, s142, s143, s144, s149, s155, s156, s157, s158, s159, s160, s161, s162, s163, s164, s181, s182, s183, s184, s185, s186, s187, s189, s191, s192, s195, s200, s201, s211, s212, s213 (114 shots)

## `amber_bead_glint`
**Overlay for `amber_bead`.**

- Look: Exactly the `amber_bead` outline (same points, same `#6b3a10` width 6) with **no fill**, plus two curved white `#fff3c0` glint streaks at upper-left (around (-200,-140) and (-150,-170)), one small white star glint at (+190,-120) and 3-4 tiny pale bubbles near the rim. Nothing inside x -200..200, y -120..150 except those near-rim marks, so the specimen stays readable, but the glints overlapping the specimen edge are what make it look sealed inside.
- Facing / anchor / size: Centre anchor, same 600 x 420 footprint, transparent interior.
- Notes: Always drawn after the specimen; never used alone.
- Shots: s002, s005, s006, s007, s008, s009, s010, s011, s012, s013, s014, s020, s021, s030, s032, s033, s034, s035, s036, s037, s040, s041, s042, s045, s046, s047, s049, s054, s055, s056, s057, s058, s059, s060, s061, s062, s066, s067, s068, s069, s070, s071, s076, s077, s078, s079, s080, s081, s082, s083, s084, s087, s088, s089, s090, s096, s097, s098, s099, s100, s104, s105, s106, s107, s108, s109, s110, s111, s112, s113, s114, s117, s118, s119, s120, s121, s122, s123, s130, s131, s132, s133, s135, s141, s142, s143, s144, s149, s155, s156, s157, s158, s159, s160, s161, s162, s163, s164, s181, s182, s183, s184, s185, s186, s187, s189, s191, s192, s195, s200, s201, s211, s212, s213 (114 shots)

## `feather_tick`
**Specimen (item 1 hero, cold open).**

- Look: A short broken length of a primitive feather: pale cream-brown `#d9c49a` shaft running diagonally from lower-left to upper-right, loose separate barbs (not a modern zipped vane) fanning off both sides. A **tick nymph** (tiny, flat, oval, dark red-brown `#5a2a1a`, 6 legs since it is a nymph, small mouthparts) clinging to the barbs at about (+40,-10), one leg wrapped around a barb. Tick about 70 x 50, clearly visible (cartoon enlarged).
- Facing / anchor / size: Centre anchor, fits the bead core: about 440 x 230 (x -220..220, y -115..115).
- Notes: Also used alone on the family-tree card at 0.35.
- Shots: s002, s005, s006, s011, s012, s020, s023, s024, s030, s032, s054, s076, s077, s078, s104, s105, s130, s155, s156, s181, s212, s213 (22 shots)

## `dracula_tick`
**Specimen.**

- Look: Deinocroton draculi engorged: a round, balloon-swollen soft tick body (grey-brown `#7a5a4a` with lighter stretched sheen and fine wrinkle lines), tiny head/mouthparts and 8 short legs sticking out at the front, looking almost too small for the body. Creepy, not cute: no eyes, no face.
- Facing / anchor / size: Centre anchor, about 260 x 220 (x -130..130, y -110..110).
- Notes: Shown in the bead at scale 1, on a nest at 0.15-0.18 (keep it readable as a blob with legs).
- Shots: s007, s008, s009, s010, s021, s022 (6 shots)

## `tick_unfed`
**Specimen (comparison).**

- Look: The same tick unfed: small flat teardrop body, same colours as `dracula_tick`, 8 legs, mouthparts forward. Top view.
- Facing / anchor / size: Centre anchor, about 160 x 130.
- Notes: Before/after beside the swollen one.
- Shots: s008 (1 shot)

## `coin_edge`
**Prop.**

- Look: A generic copper coin standing on its edge, seen three-quarter: narrow copper `#b8733a` ellipse face (about 110 wide x 300 tall) with a thick visible rim band on the right showing its thickness (about 24 wide, darker `#8a4a20`, fine vertical edge lines). No currency text, no portrait.
- Facing / anchor / size: Bottom-centre anchor (resting edge on y=0), about 140 x 300.
- Notes: "Shorter than a penny is thick": a dotted line runs from the rim band to the tick.
- Shots: s012 (1 shot)

## `film_poster_generic`
**Prop card.**

- Look: A crude generic movie-poster frame: tall portrait card with a black border, dark night-jungle gradient (`#1b2f1a` to `#0b0f0b`), a ring of jagged palm/fern silhouettes along the bottom, two searchlight beams fanning from the bottom corners, a blank rectangle at the bottom where credits would go (just grey lines). **No title, no logo, no lettering, no dinosaur skeleton badge, nothing that resembles any real film's poster** (CD decision 5). The centre (x -200..200, y -230..170) stays dark and empty for an amber bead to sit on.
- Facing / anchor / size: Centre anchor, about 600 x 860 (x -300..300, y -430..430).
- Notes: Used at scale 1.0 on a dark `#1a1d22` card, with a `mosquito` in a bead in the centre and a red `?` beside.
- Shots: s013, s014 (2 shots)

## `dna_strand`
**Diagram prop.**

- Look: A short horizontal DNA double helix: two twisting backbones (blue `#3a7ad9` and red `#e0201b`) with coloured rungs (yellow, green), thick black outline, cartoon. Clean ends (it is shown broken into pieces at smaller scales).
- Facing / anchor / size: Centre anchor, about 640 x 170.
- Notes: Used at 0.1-1.1.
- Shots: s014, s015, s018, s019, s020 (5 shots)

## `moa`
**Creature.**

- Look: Giant moa (Dinornis), standing, facing right: huge flightless bird with no visible wings, long neck held forward-up, small head with a short broad bill, shaggy hair-like brown feathers `#7a5a3a` with darker streaks, very thick scaly grey legs with three big toes. Realistic-cartoon, not cute.
- Facing / anchor / size: Bottom-centre anchor (feet on y=0); about 450 wide x 900 tall at scale 1 = true size against Doug at scale 1 (3.6 m bird vs 1.8 m Doug).
- Notes: Used once at 0.62 next to Doug at 0.31.
- Shots: s017 (1 shot)

## `feather_nest`
**Prop.**

- Look: A rough cup nest of twigs and bark strips, lined with soft pale downy feathers sticking up over the rim, empty. Brown `#7a4f2c` twigs, cream `#efe6d0` feathers.
- Facing / anchor / size: Bottom-centre anchor, about 360 x 150 (x -180..180, y -150..0).
- Notes: On the ground (item 1), in a tree fork on a branch (item 7), and in the death beat with the cap sitting in it.
- Shots: s021, s022, s173, s176, s177, s178, s179, s180 (8 shots)

## `enantiornithine`
**Creature (item 7 parent, also on the family tree).**

- Look: An adult enantiornithine bird, perched/standing facing right, wings half-raised: brown-grey feathers `#6a5a4a`, paler belly, a **long toothed snout** with a row of small sharp white teeth clearly visible, a **clawed finger on the front edge of each wing**, long legs with hooked talons, small hard yellow eye under a heavy brow, short fan tail. Menacing, never cute (CD note): no round eyes, no blush.
- Facing / anchor / size: Bottom-centre anchor (feet on y=0), about 420 x 300.
- Notes: Used plain, flipped, and as a silhouette (`silhouette: true`, purple glow spray behind) for the reveal; the teeth and wing claws must be readable in the silhouette's outline.
- Shots: s024, s156, s169, s170, s171, s172, s173, s174, s175, s178, s180 (11 shots)

## `feathered_dino_looming`
**Creature (item 1 kit beat and the boss: the adult).**

- Look: The head and neck of a big feathered theropod leaning into frame **from the right edge, facing left**: long toothy snout slightly open with sharp teeth, hard yellow eye under a heavy brow, shaggy brown feathers `#6a4a2a` with darker back and pale throat, the neck thick and running off the right edge. Same family look as the library `feathered_dinosaur`, but enormous. The neck's cut edge must sit at x=0 so it is always off-frame (art bible open-jaw rule: never show a cut neck).
- Facing / anchor / size: Anchor (0,0) = neck base on the right edge; extents about x -900..0, y -360..+260.
- Notes: Placed at x 1940 (just past the frame edge), y 620-650, scale 1.0-1.05. Silhouette version first (purple glow), then full colour 1 beat later. Head must stay below y 260 at those placements (counter zone).
- Shots: s028, s029, s030, s208, s209 (5 shots)

## `dna_kit`
**Prop (Doug's gadget).**

- Look: A small handheld grey plastic box with rounded corners, a stubby antenna, two round buttons, a blank pale-green screen (rectangle x -70..70, y -60..0, left empty for overlay text), printed black caps "DNA KIT" under the screen.
- Facing / anchor / size: Centre anchor, about 200 x 160.
- Notes: Held near Doug's thumbs-up hand at 0.55; close-up at 1.4 with "ERROR" overlaid on the screen.
- Shots: s026, s027, s028 (3 shots)

## `test_tube_dino`
**Prop.**

- Look: A single empty glass test tube with a cork, slight blue glass tint, white label printed "DINO".
- Facing / anchor / size: Centre anchor, about 60 x 220.
- Notes: One shot, on the ground by Doug.
- Shots: s026 (1 shot)

## `amber_spider`
**Creature (in amber, item 2).**

- Look: A young spider in side view facing right, frozen mid-lunge: rounded orange-brown abdomen, smaller head-body, 8 thin jointed legs (front pair raised forward), **fangs (chelicerae) open and pointing forward** at the front. Clean silhouette.
- Facing / anchor / size: Centre anchor, about 260 x 160.
- Notes: In the bead at 0.75 (young) and 1.05 (the adult male), and outside the bead in the web.
- Shots: s005, s033, s034, s035, s036, s037, s040, s041, s042, s043, s044, s045, s046, s047, s049, s054, s076, s077, s078, s104, s105, s130, s155, s156, s181, s212, s213 (27 shots)

## `parasitic_wasp`
**Creature (in amber).**

- Look: A small dark parasitic wasp, side view facing right: black-brown body with a narrow waist, clear veined wings, long antennae, legs splayed as if stuck. Not the emerald `jewel_wasp`.
- Facing / anchor / size: Centre anchor, about 220 x 120.
- Notes: Always flipped to face the spider.
- Shots: s005, s033, s034, s035, s036, s037, s040, s041, s042, s043, s044, s045, s046, s047, s048, s049, s054, s076, s077, s078, s104, s105, s130, s155, s156, s181, s212, s213 (28 shots)

## `hell_ant_grip`
**Creature (item 3 hero).**

- Look: Ceratomyrmex hell ant in side view facing right: dark red-brown body, a **long horn/paddle sticking forward-up from the forehead**, long scythe jaws **swung upward** so the prey is pinned between jaws and horn; the prey is a small pale cockroach-relative nymph (tan, segmented, little legs). Menacing.
- Facing / anchor / size: Centre anchor, about 440 x 240, fits the bead core.
- Notes: Jaws at about (+120..+200, -40..+40) so arrows can point at them.
- Shots: s005, s055, s056, s057, s058, s059, s060, s061, s062, s076, s077, s078, s104, s105, s130, s155, s156, s181, s212, s213 (20 shots)

## `hell_ant`
**Creature.**

- Look: The same hell ant alone, jaws open and raised upward, horn visible, no prey.
- Facing / anchor / size: Centre anchor, about 380 x 200.
- Notes: Diagram cards, the forest floor beside costumed Doug (0.55), the death beat, and a silhouette tease.
- Shots: s053, s063, s065, s072, s073, s074, s075 (7 shots)

## `vampire_ant`
**Creature (in amber).**

- Look: Linguamyrmex vampire ant, side view facing right: dark brown hell ant with a **flat paddle-shaped plate on its face** (slightly metallic grey sheen `#8d9096`), long upward-curved jaws, a few tiny trigger hairs near the mouth.
- Facing / anchor / size: Centre anchor, about 420 x 220.
- Notes: Arrows point at the paddle (upper right) and the hairs (lower right).
- Shots: s066, s067, s068, s069, s070, s071 (6 shots)

## `rice_grain`
**Prop.**

- Look: One long grain of white rice, horizontal, cream-white with a faint grey outline and soft shading.
- Facing / anchor / size: Centre anchor, 300 x 80.
- Notes: Size comparison with `hell_ant`.
- Shots: s065 (1 shot)

## `cockroach_costume_empty`
**Death prop (item 3).**

- Look: Doug's `cockroach_costume` lying flat and empty on the ground (deflated): the same glossy reddish-brown shell, tan collar, zipper and spiny legs, splayed, antennae flopped. No Doug inside.
- Facing / anchor / size: Bottom-centre anchor, about 420 x 100.
- Notes: The death beat: `doug_cap` sits on top of it at about (0,-60) x scale; a ghost Doug floats above.
- Shots: s075 (1 shot)

## `ammonite_shell_empty`
**Specimen (item 4 hero).**

- Look: A small juvenile ammonite shell, planispiral and ribbed (cream with brown bands, like the library `ammonite` but **no body, no head, no arms**). The opening faces lower right and is **packed with sand** (`#e8c07a` with darker grains).
- Facing / anchor / size: Centre anchor, about 300 x 300.
- Notes: Also used with `ink: "#9fe6ff"` on a navy scan panel, so keep the outline black (it is recoloured).
- Shots: s079, s080, s081, s082, s083, s084, s085, s086, s087, s088, s089, s090, s091, s092, s093, s094, s095, s096, s097, s098, s099, s100, s104, s105, s130, s155, s156, s181, s212, s213 (30 shots)

## `beach_towel`
**Prop.**

- Look: A striped beach towel lying flat on sand, in perspective: red/white stripes, frayed short ends.
- Facing / anchor / size: Centre anchor, about 460 x 90.
- Notes: Doug sits on it (sit pose).
- Shots: s101, s102 (2 shots)

## `xiaophis_skeleton`
**Specimen (item 5 hero).**

- Look: Xiaophis, the headless baby snake: a tiny loosely coiled (S-bend) chain of cream-white vertebrae with fine curved ribs, **no skull** (the front end just stops), the tail tapering. Delicate, readable as a backbone.
- Facing / anchor / size: Centre anchor, about 360 x 220.
- Notes: Arrows point at the vertebrae; a label says "97".
- Shots: s079, s106, s107, s108, s109, s110, s111, s112, s113, s114, s116, s117, s118, s119, s122, s123, s130, s155, s156, s181, s212, s213 (22 shots)

## `shed_snake_skin`
**Specimen / prop.**

- Look: A long translucent papery shed snake skin fragment: pale grey-cream `#e6e0cc` with a clear diamond scale pattern drawn in fine grey lines, ragged torn ends, slightly twisted.
- Facing / anchor / size: Centre anchor, about 500 x 120 (horizontal).
- Notes: In a bead at 0.85, and huge (1.5, `rotate` 80) hanging from a branch in the night reveal. No text, so rotation is fine.
- Shots: s120, s121, s122, s123, s128 (5 shots)

## `big_cretaceous_snake`
**Creature (silhouette only).**

- Look: A big primitive snake draped along a horizontal branch, head raised to the right with the mouth closed, thick body hanging in a loop below the branch. Generic (no pit-viper heat pits, no rattles, no hood), olive-brown. The outline must read clearly as a snake when blacked out.
- Facing / anchor / size: Anchor = branch-top centre, about 900 x 320.
- Notes: Only ever shown as `silhouette: true` (night reveal and the bigger-snake beat).
- Shots: s121, s128 (2 shots)

## `oculudentavis_skull`
**Specimen (item 6 hero).**

- Look: The tiny Oculudentavis skull in side view facing right: bird-like domed skull, **very large round eye socket** with a ring of bony plates, long narrow snout with a **row of small sharp teeth** along the jaw. Cream bone `#efe6d0` with grey shading.
- Facing / anchor / size: Centre anchor, about 320 x 200.
- Notes: Bead, diagram cards (up to 1.6), family-tree card.
- Shots: s106, s131, s132, s133, s134, s135, s136, s140, s141, s145, s146, s148, s149, s155, s156, s181, s212, s213 (18 shots)

## `oculudentavis_specimen`
**Specimen.**

- Look: The second specimen: a partial lizard skeleton with a complete skull (same skull shape as above but the snout less beak-like), the front of the body with visible scales (small brown scale texture) and soft tissue patches, front legs.
- Facing / anchor / size: Centre anchor, about 440 x 220.
- Notes: Bead and the squashed-skulls card.
- Shots: s141, s142, s143, s144, s145, s149 (6 shots)

## `tiny_saddle`
**Prop.**

- Look: A tiny brown leather riding saddle with stirrups and a blank cream tag hanging from it.
- Facing / anchor / size: Bottom-centre anchor, about 220 x 140.
- Notes: Held near Doug's hand, then on the ground and on the log. A label "SMALLEST DINOSAUR" is overlaid separately.
- Shots: s150, s151, s152 (3 shots)

## `retracted_stamp`
**Annotation.**

- Look: Red rubber-stamp mark "RETRACTED": rough `#e0201b` rectangle outline (double rule), bold caps letters as strokes, slightly broken ink (same family as `again_stamp`). Upright.
- Facing / anchor / size: Centre anchor, about 520 x 150.
- Notes: Stamped over `journal_paper` at scale 1.0.
- Shots: s139 (1 shot)

## `bee_hummingbird`
**Creature.**

- Look: Bee hummingbird, hovering, facing right: tiny body, iridescent blue-green back, grey-white belly, long thin bill, blurred wings.
- Facing / anchor / size: Centre anchor, about 160 x 110.
- Notes: Comparison card at 1.3.
- Shots: s136 (1 shot)

## `belone_fossil`
**Specimen (item 7 hero).**

- Look: The hatchling's remains as seen in amber: a small bird head with a toothed beak, one wing with flight feathers spread, patches of skin, and a clawed foot, laid out flat (fossil, flat museum look, no blood, nothing gory). Brown `#6a4a2a` feathers, cream bone, dark skin patches.
- Facing / anchor / size: Centre anchor, about 440 x 260.
- Notes: Arrows point at head (upper right), wing (upper left) and foot (lower right).
- Shots: s106, s157, s158, s159, s160, s161, s162, s163, s164, s181, s212, s213 (12 shots)

## `amber_lump_claw`
**Prop.**

- Look: A raw, rough, unpolished amber lump (darker `#c07a24` with a crusty matte surface) with a **tiny clawed foot** poking out of one end.
- Facing / anchor / size: Centre anchor, about 320 x 220.
- Notes: On the museum director's desk.
- Shots: s165, s166, s167 (3 shots)

## `belone_scan`
**Diagram (x-ray family).**

- Look: CT/x-ray of the hatchling for a dark navy `#0d1b2a` panel (transparent background, same family as `tiger_shark_xray` / `cassowary_wing_xray`): faint blue soft-tissue outline of the little bird, pale-cyan `#9fe6ff` bones with white edges (skull with teeth, wing bones, leg and claws).
- Facing / anchor / size: Centre anchor, about 440 x 260.
- Notes: One shot at 1.4.
- Shots: s168 (1 shot)

## `eva_tail`
**Specimen (boss).**

- Look: Eva, the dinosaur tail section: a short slightly curved tail segment lying diagonally, covered in fine brown-and-white feathers, with **8 small vertebrae visible** as a row of cream bones through a translucent patch, a darker soft-tissue band along the bones.
- Facing / anchor / size: Centre anchor, about 440 x 200.
- Notes: Bead at 1.15, alone at 1.1-1.3 beside two coins.
- Shots: s182, s183, s184, s185, s186, s187, s188, s189, s191, s192, s194, s195, s200, s201 (14 shots)

## `amber_market_stall`
**Place prop.**

- Look: A crude market stall: wooden table with a striped awning, three or four flat trays of polished amber pieces (golden blobs), a hand-written blank sign board. No people.
- Facing / anchor / size: Bottom-centre anchor, about 900 x 560.
- Notes: Item 8 market beat; a `price_tag` sits on one bead at about (+120,-290).
- Shots: s197, s198, s199 (3 shots)

## `price_tag`
**Prop.**

- Look: Small white paper price tag with a punched hole and a loop of string, blank.
- Facing / anchor / size: Centre anchor, about 120 x 70.
- Notes: One shot.
- Shots: s198 (1 shot)

## `kachin_map`
**Sober-card map.**

- Look: Northern Myanmar in the sober-card style of `myanmar_coast_map`: muted plain land `#4a5a48`, neighbouring countries a shade darker, thin pale outline, **Kachin State highlighted** with a lighter fill `#6a7a62` and a thin white border, a small white dot for Myitkyina, a small dot for the Hukawng Valley amber mines area. No labels (they are overlaid).
- Facing / anchor / size: Centre anchor, about 700 x 900.
- Notes: Sober Kachin/SVP card (no Doug, no counter, no wordart) and the snake's "northern Myanmar" beat.
- Shots: s115, s202, s203, s204, s205 (5 shots)

## `specimen_tray`
**Prop (episode device).**

- Look: A shallow wooden museum specimen tray (warm `#8a5a2a` wood, darker inner rim) with **8 round recessed slots in one row**, each a dark velvet-lined dip. A small blank brass label plate on the front edge. Slots must be exactly at x = -700, -500, ..., +700 (200 apart), y = 0, inner radius 82.
- Facing / anchor / size: Centre anchor, 1600 x 260 (x -800..800, y -130..130).
- Notes: Used at 0.8 on the end-of-item tray shots (beads drop into slots at scale 0.22), and tiny (0.24) in the cold open.
- Shots: s002, s032, s054, s076, s077, s078, s104, s105, s130, s155, s156, s181, s212, s213 (14 shots)

## `narrator_hand_pencil`
**Narrator prop.**

- Look: The narrator's crude-tier arm and hand (same style as `narrator_hand`, `auto_ink`) entering **horizontally from the right edge**, holding a yellow pencil pointing left/up toward the death counter.
- Facing / anchor / size: Anchor (0,0) = pencil tip; the sleeve runs right to about (+700,+40), off-frame.
- Notes: s052: tip at (1420, 330) then lowered to (1420, 440). Nothing may reach above y 260 (counter zone).
- Shots: s052 (1 shot)
