# 048 asset requests (director, 2026-11-15)

15 new drawings. The shotlist already places them using the anchors and local coordinates below, so please keep
the anchors, sizes and facing as specified (or tell me what changed and I'll re-place them). All creatures are
detailed tier (layered fills, interior shading, outlines 3-5). Nothing cute: no smiles, no blush, no hearts, no
baby animals. No blood or wounds anywhere (CD notes, decisions.md 2026-11-15).

## Creatures

### `false_killer_whale` (84 shots: the episode's star)
- What: false killer whale (*Pseudorca crassidens*), a large all-dark dolphin. Side view, **facing right**.
- Real look: slender, torpedo body, **almost black** (use charcoal `#2e3138` with a lighter `#4a4f58` back highlight and
  shading so it reads on every water colour, down to the boss navy `#14365e`); **rounded, beakless, overhanging melon
  head** (no orca-style white patches); subtle pale grey W/anchor blaze on the throat/chest; tall **falcate (back-curved)
  dorsal fin mid-back**; distinctive narrow flippers with a bend ("elbow") on the leading edge; slim tail stock, dark flukes.
  Small dark eye with a white glint, mouth line closed, a hint of conical teeth only if it reads as neutral (no grin).
- Size/anchor: anchor centre, body x -320..+320, y -80..+80; dorsal tip about (-10, -150); snout tip at about (+320, +5).
  The shotlist puts fish "in the mouth" at the snout, so keep the mouth line around (+250..+320, +10).
- Must not read as an orca (no white eye patch, no saddle) or as a shark (no gills, rounded head).
- Used in: s002, s006-s007, s009, s011-s012, s015-s016, s024-s025, s027-s028, s031, s034-s037 (s037 as `silhouette`),
  s039-s041, s043, s047-s049, s051, s053-s054, s058-s061, s064, s069-s070, s072, s076, s081 (silhouette), s083-s085,
  s089-s096, s099-s107, s112, s116-s118, s122, s136, s139-s141, s144-s153, s157, s159, s175-s178, s183-s184, and more
  (flip and rotate are used; rotate up to about +-30, and -60 in s116).

### `false_killer_whale_open` (9 shots)
- What: same whale, same anchor/size/facing, **mouth open** (jaws parted about 30 degrees) and empty, for "let the fish go".
- Look: rows of simple white conical teeth on both jaws, mouth interior dark maroon `#5a2a2a` (not red, no tongue detail).
  Calm eye, no aggression lines.
- Mouth point (between the jaws) at about (+290, +10).
- Used in: s154, s155, s158, s171-s174, s179, s180.

### `false_killer_whale_tuna` (6 shots + thumbnail direction)
- What: same whale and anchor, carrying **most of a yellowfin tuna** crosswise in its jaws (the boss image).
- Look: the tuna (see `yellowfin_tuna`) held by its middle, its front half sticking forward out of the mouth to about
  x +560, tail end tucked into the jaw near x +250; tuna y range about -40..+60. Clean, intact fish: no bite marks, no red.
- Used in: s003, s077, s162 (as `silhouette` with red rim), s165, s170, s178.

### `false_killer_whale_fin` (182 shots: HUD icon + surface fins)
- What: the whale's dorsal fin and a short strip of back breaking the surface.
- Look: dark charcoal falcate fin (back-curved tip), mid-grey leading-edge highlight so it reads at tiny size,
  a little white waterline ripple at the base. Clearly lower and more curved than `orca_fin`.
- Anchor: bottom-centre ON the waterline (0,0); back strip x -150..+150, y -30..0; fin tip about (+20, -170).
- Used at scale 0.16 as the TO DOUG meter icon at (1418, 256) on every shot, and at 0.2-0.5 as surfacing fins
  (s004, s019-s021, s029, s044-s046, s048, s067-s068, s088-s089, s105, s110-s111, s113, s115, s123-s127, s160, s166,
  s181, ...). Photo-ID board (s110-s111) uses it inside small photo frames.

### `false_killer_whale_skull` (4 shots)
- What: false killer whale skull, side view facing right (the 1846 Stamford subfossil and the "skull looks like a
  killer whale's" beat).
- Look: aged bone `#e6dcc4` with `#b8a888` shading, long low cranium with a short broad rostrum, large rounded orbit,
  lower jaw attached, 8-11 conical teeth per jaw row. Subtle brown staining (it came out of a fen). Nothing broken-looking
  or gory.
- Anchor centre, about 420 x 180 (x -210..+210, y -90..+90).
- Used in: s008, s134, s135 (on a mud rect), s136.

### `yellowfin_tuna` (27 shots)
- What: yellowfin tuna, side view facing right.
- Look: dark metallic blue back `#1f3f7a`, silver-white belly, a **golden-yellow lateral stripe**, long **yellow
  sickle-shaped second dorsal and anal fins**, row of small yellow finlets to the tail, deep crescent tail, big round eye.
- Anchor centre, about 520 x 180 (fins to about +-120).
- Used in: s047-s048, s055, s058, s060-s063, s069-s070, s076-s077, s166-s175, s179-s182, HUD plate from s182 on
  (scale 0.3), and lying on top of dead Doug (s181, rotate -4).

### `mahi_mahi` (17 shots)
- What: mahi-mahi (dolphinfish), side view facing right.
- Look: vivid green-gold back fading to yellow sides with small blue spots, **steep blunt forehead** (bull), one long
  dorsal fin running the full back, deeply forked tail.
- Anchor centre, about 460 x 170.
- Used in: s048, s055, s062-s063, s089-s094, s100-s103, s122, s145, s152 (held at the whale's snout at scale ~0.25-0.45).

### `golden_retriever` (1 shot)
- What: adult golden retriever standing, side view facing left or right (we flip as needed), calm.
- Look: golden coat `#d9a04a` with feathered tail and legs, floppy ears, dark nose. Adult only.
- Anchor bottom-centre (feet on y=0), about 320 x 240.
- Used in: s169 (tuna "as heavy as a golden retriever").

### `sperm_whale_fluke` (1 shot)
- What: a sperm whale's tail flukes raised high out of the water (the defensive circle, death 363).
- Look: same dark grey as `sperm_whale`, broad triangular flukes with a notch and wrinkled trailing edge, tail stock
  rising from the water, pale-blue `#bfe6ff` water streaming off the edges (no white zigzags).
- Anchor bottom-centre ON the waterline; about 520 wide, 440 tall (x -260..+260, y -440..0).
- Used in: s021 (scale 0.6, cut before any contact).

## Doug props (worn; art director to approve)

### `mahi_mahi_costume` (4 shots)
- What: Doug's felt mahi-mahi suit for the upright `float` pose, same construction as `dolphin_costume`: anchor = Doug's
  hips, listed after Doug at the same x/y/scale.
- Look: green-gold felt body with blue spot patches and visible stitching/zipper, the blunt mahi forehead as a hood over
  the cap dome with the **cap, brim, face and eyes fully visible**, a long felt dorsal fin running down the back, forked
  felt tail out of the lower back, fin mitts. Deadpan, not cute.
- Used in: s104-s107 (float pose, scale 0.55 and 0.3).

### `mahi_mahi_costume_flat` (2 shots)
- What: the mahi suit gone flat with Doug in it (death 367). Same convention as `reindeer_costume_flat` (047): listed
  after an `on_back` Doug at the same x/y/scale, **no rotate**; suit over torso and legs (about x -140..+186, y -58..+74),
  tail flopped at the feet end, face, X eyes and cap (head centre (-218, 0)) left clear.
- Used in: s108, s109 (Doug floating on the water surface, scale 0.55).

### `dolphin_costume_flat` (1 shot)
- What: `dolphin_costume` gone flat with Doug in it (death 364). Same convention as `reindeer_costume_flat`: after an
  `on_back` Doug, same x/y/scale, no rotate; grey felt suit over torso/legs, flukes flopped past the feet, the felt dorsal
  fin folded over; face, X eyes and cap clear.
- Used in: s046.

## Props

### `dougs_plate` (181 shots: episode HUD device)
- What: DOUG'S PLATE, the episode-only device from the brief: an **empty** white dinner plate with a **fork on the left
  and a knife on the right**, seen in the same low 3/4 view as `dinner_plate`. Must not look like 021's MENU card.
- Look: white plate with a thin blue rim line and shallow well; plain steel fork and table knife (grey `#c9ced4`, black
  outline). No food, no crumbs.
- Anchor centre, about 460 x 110 (plate 300 x 90 at the centre, cutlery out to x +-230).
- Used as a HUD icon at (1180, 166), scale 0.42, left of the counter on every shot; big in s182 (scale 1.6, centre
  (900, 700)) with `yellowfin_tuna` landing on it and a red SERVED stamp. From s182 on the HUD plate carries a small tuna.

### `tuna_head_hook` (1 shot)
- What: a longline branch line's hook with only a tuna head left on it (depredation beat, cartoon only).
- Look: grey steel J hook, the tuna head (dark blue top, silver cheek, big eye) hanging from it; the back edge is a clean
  **scalloped bite outline in the same body colours**, no pink or red flesh, no bones, no drips. Reads as a cartoon
  "only the head came up".
- Anchor = line tie point at the top of the hook (0,0); hook to about y +70; head x -90..+90, y +60..+220.
- Used in: s080 (scale 0.6).

### `hawaii_map` (8 shots)
- What: main Hawaiian Islands map in the `world_map` style (flat green islands, dark green outline, light-blue sea
  `#bfe6ff`, white wave ticks, black frame, no labels): Niihau, Kauai, Oahu, Molokai, Lanai, Maui, Kahoolawe, Hawaii (Big Island).
- Projection: x = (lon + 157.5) x 160, y = -(lat - 20.6) x 160; frame x -500..+500, y -320..+320 (lon -160.6..-154.4,
  lat 18.6..22.6), anchor centre. Check points: **Lanai (-156.93, 20.83) -> (+91, -37)**, **Kona coast (-155.99, 19.64)
  -> (+242, +154)**; the shotlist rings these two spots.
- Used in: s038, s050, s054, s072 (0.3 inset), s085, s114, s152 (0.32 inset), s164.

## Reused library drawings (no work needed)
sperm_whale, sperm_whale_top, orca, dolphin, dolphin_costume, dolphin_costume_swim, swordfish, salmon, silver_fish,
humboldt_squid, shark_fin, seagull, rowboat, inflatable_dinghy, fishing_boat, sailboat, snorkel, minivan, city_bus,
ping_pong_table, pizza_box, pizza_table_twelve, small_table, baby_grand_piano, tape_measure, finish_banner, calendar,
compact_camera, dtag, price_tag, signboard, wait_stopwatch, new_zealand_map, pacific_map, world_map, bc_map,
south_america_full_map, britain_map, europe_map, scientist, stick_man_plain, photographer_diver, field_guide_open,
narrator_hand_pencil, doug_cap, gravestone, water_splash, question_mark, exclamation_mark, warning_triangle, red_x, thermometer.
