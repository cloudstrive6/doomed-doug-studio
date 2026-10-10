# Asset requests: 014 What Dying From Every Brain Parasite Would Feel Like

From the director, for the illustrator (the art director approves). House style: `assets/library/anglerfish.json` and
`channel/art_bible.md`.
- **Detailed tier** for every creature and prop: outlines 4-6, flat fills plus `spray` shading, darker back, lighter belly.
  Everything faces **right** unless noted. Local coordinates are centred on the anchor.
- **Anchors and sizes.** I laid out all 256 shots with placeholder boxes at exactly the bboxes below and checked the layouts for the
  counter/meter zone, caption bar, crops and overlaps. `bc` = anchor at bottom-centre (the lowest point sits on y=0, drawing spans
  y -h..0). `c` = anchor at the centre. Sizes are local units at scale 1 (width x height). Please stay inside the bbox. Where I give a
  local point (eye, muzzle, blade tip), arrows, dotted paths or overlays in the shotlist aim at it, so please put that feature there.
- **Backgrounds by band (brief):** "Steers you" pale pond green / cream / grass gold; "Lives in you" flesh pink `#f4c6c4` and lab
  cream `#f6ecd2`; "Eats you" deep maroon `#5a1a24` / `#7a2232` and near-black `#120a0c` (boss). Assets used in band 3 (horse,
  compost heap, worm icon, mandrill, amoeba, flowerpot) must read on maroon and near-black: mid-tone fills, no near-black bodies.
- **Tone (brief section 7).** No anatomical brains, no tissue, no wounds, no blood. Parasites are **diagram icons, no faces**.
  Animals are documentary-cartoon, never cute (no eyelashes, no blush, no smiles); the horse, sheep and killifish are never shown suffering.
- **Priority:** A = hero (8+ shots), B = supporting (3-7), C = one-off.

**Reused from the library (no work needed):** `ant_costume`, `carpenter_ant`, `fungus_stalk` (002 callback), `amber_snail` (land snail),
`cercaria` (fluke larvae), `seagrass`, `water_splash_small`, `head_outline` (+ `doug_cap` on top = "Doug's head"), `body_outline`, `rat`,
`lettuce`, `leaf`, `crab`, `amphipod` (freshwater shrimp stand-in), `silver_fish`, `cat`, `black_mamba` (snake), `grey_wolf`, `golf_ball`,
`ruler`, `fingertip`, `calendar`, `clock`, `thermometer`, `angry_sun`, `magnifying_glass`, `scientist`, `test_tube_rack`, `glass_jar`,
`printed_card`, `library_book`, `dinner_plate`, `water_bottle`, `hand_outline`, `kitchen_chair`, `bed`, `house`, `compact_camera`,
`airplane`, `world_map`, `usa_map`, `heart_icon`, `small_plant`, `naegleria_amoeba` (002 callback), `gravestone`, `doug_cap`, and the
annotation set (`question_mark`, `exclamation_mark`, `warning_triangle`, `red_x`).

**Drawn inline in the shotlist (no asset needed):** the DOUG DEATHS counter and the episode meter "BRAIN: STEERED / OCCUPIED / EATEN"
(size-28 label under the counter at (1590, 238)), all backgrounds (salt marsh, marsh cross-section, mudflat, dusk/night/morning/day grass
field, sheep field, garden fence, bedroom, cafe, paddock, boss garden), cysts and eggs (small cream circles), the ice pack, the grape, the
grain of rice, the bistro table, the cardboard "vegetarian" sign (hand-lettered, small, on a string: deliberately not 013's big
VEGETARIAN title text), the front-view head for the Spirometra scans, the DNA helix, bar charts, the blown-up first millimetre of a ruler,
the hair strand, dust puffs, the lake inset, dotted paths, ripples and zigzag pain lines.

---

## Steers you (band 1)

### `killifish` (A): California killifish, side view
- **DONE** (illustrator): `assets/library/killifish.json`; preview `assets/previews/014-assets-a.png` + backgrounds/bbox check `assets/previews/014-killifish-bg.png`.
s004-s007, s009-s013, s015-s020, s022 (as small as 0.8, as big as 3.0 for the cyst diagram)
- `c`, **260 x 100** (x -130..+130, y -50..+50), facing right. Eye at about (+95, -10).
- Real look (*Fundulus parvipinnis*): small, slim, slightly flattened killifish; olive-grey back `#6f7a5a`, **bright silver flanks**
  with faint dark vertical bars, white belly, rounded tail fin (not forked), small rounded dorsal fin set far back, blunt head, small upturned mouth.
- **Keep the top of the head plain** (a light silver area centred at about (+80, -5), radius ~40): in s011-s013 I scatter up to 70 tiny
  cream cyst dots there at scale 3.0 and 1.8. No interior anatomy.
- Used rotated -25..+25 (the "dance") and flipped. Must read on pond green `#7fae8e` water and on cream.

### `killifish_costume` (B): Doug's killifish onesie (worn prop)
- **DONE** (illustrator): `assets/library/killifish_costume.json`; preview `assets/previews/014-assets-a.png` + backgrounds/bbox check `assets/previews/014-killifish_costume-bg.png`.
s024-s027, s086 (falling, rotated 80), s088 (in the costume pile, rotated 80)
- Anchor = **Doug's hips (0,0)**, same scale as Doug; bbox x -200..+120, y -170..+70. Drawn after Doug.
- Homemade silver felt fish suit over the torso (y -150..+60) with faint dark bars, white belly panel, a front zipper, a rounded felt tail
  fin behind the hips to about (-200, +20), a small dorsal fin on the back of the suit. **Head, face and red cap fully visible** (no hood).
- s025-s027 Doug floats chest-deep at the water line: water covers everything below the hips, so the torso part must read on its own.
- In the pile shots it lies on the floor rotated ~80 degrees, so give it a clear silhouette as an object.

### `horn_snail` (C): California horn snail
- **DONE** (illustrator): `assets/library/horn_snail.json`; preview `assets/previews/014-assets-a.png` + backgrounds/bbox check `assets/previews/014-horn_snail-bg.png`.
s008 (three on the mudflat), s009, s022
- `bc`, **110 x 200** (x -55..+55, y -200..0). Tall, narrow, many-whorled conical spire pointing up and slightly back, dark brown-grey
  shell `#5a4a3a` with paler spiral ribs, small dark body and foot at the base. Reads on mud `#8a7a5a` (give the shell a pale rim line).

### `heron` (A): great blue heron, standing
- **DONE** (illustrator): `assets/library/heron.json`; preview `assets/previews/014-assets-b.png` + backgrounds/bbox check `assets/previews/014-heron-bg.png`.
s018 (silhouette), s019-s023, s027 (silhouette), s028, s029
- `bc`, **360 x 640** (x -180..+180, y -640..0), facing right (I flip nothing). Beak tip at about (+170, -560).
- Real look: tall blue-grey wading bird, long S-curved neck, dagger-shaped yellow-orange bill, white face with a black stripe over the eye
  running into a black crest plume, rusty thighs, very long thin dark legs, shaggy breast plumes.
- Silhouette shots use `glow_r: 0` and my own red spray at the body, so the silhouette shape alone has to read (long legs + S-neck + bill).
- Standing in the shallows at (1520, 900): the counter zone (x 1300-1860, y 110-260) stays clear because the head top sits at y ~324.

### `royal_albert_hall` (C): London concert hall icon
- **DONE** (illustrator): `assets/library/royal_albert_hall.json`; preview `assets/previews/014-assets-a.png` + backgrounds/bbox check `assets/previews/014-royal_albert_hall-bg.png`.
s013 (beside the infected fish, label "5,272 SEATS")
- `bc`, **600 x 320**. Round/oval red-brick hall `#b5533c`, pale terracotta frieze band, low glass-and-iron dome on top, arched
  entrance porch at the front. Simple and recognisable at 510 px wide.

### `grass_blade` (A): one tall blade of grass (the lancet ant's perch)
- **DONE** (illustrator): `assets/library/grass_blade.json`; preview `assets/previews/014-assets-b.png` + backgrounds/bbox check `assets/previews/014-grass_blade-bg.png`.
s030, s041-s043, s045, s047-s049, s055-s060
- `bc`, **80 x 720** (x -40..+40, y -720..0). **Tip at (+20, -720)**: the ant clamps there, Doug hangs there (s055-s058) and the cap sits
  on it (s059-s060 at tip y -18).
- A single long blade, slightly curved, tapering to a point, grass-gold green `#9aa83a` with a darker `#5f6b2a` midrib line, base in a
  small tuft. Must read on dusk orange, night navy `#2b2f4a` and pale yellow day sky.

### `fluke_icon` (C): lancet fluke / adult fluke diagram icon
- **DONE** (illustrator): `assets/library/fluke_icon.json`; preview `assets/previews/014-assets-a.png` + backgrounds/bbox check `assets/previews/014-fluke_icon-bg.png`.
s021 (adult fluke inside the heron), s035 ("6-10 mm, about the length of a grain of rice")
- `c`, **200 x 70**. Lancet-shaped flatworm, pointed at both ends, pale translucent cream-pink `#f2d6c8`, two small sucker dots, faint
  branching gut lines. Microscope-diagram style, no face.

### `cow` (B): grazing cow, standing
- **DONE** (illustrator): `assets/library/cow.json`; preview `assets/previews/014-assets-b.png` + backgrounds/bbox check `assets/previews/014-cow-bg.png`.
s033, s034, s043 (silhouette at the frame edge), s054, s058 (silhouette), s059-s060 (flipped, small)
- `bc`, **640 x 420** (x -320..+320, y -420..0), facing right, head up, muzzle at about (+300, -250).
- Real look: brown-and-white (Hereford-style) cow, broad body, short horns or polled, pink-grey muzzle, tail with a tuft.
  The night silhouette (s058) must read as "cow" from shape alone: blocky body, four legs, head and ears.

### `sheep` (A): sheep, side view
s033, s036 (big, with fluke speckle), s061-s063, s066, s074 (tilted -10), s075, s076 (ten in a row at 0.32), s077, s079, s080
- `bc`, **420 x 300** (x -210..+210, y -300..0), facing right. Muzzle at about (+205, -190) (the s066 arrow ends there).
- Real look: cream woolly fleece `#f2ead8` with grey shading lumps, dark face and legs (Suffolk-style), drooping ears. Calm, not cute.
- Rotations of up to +-12 degrees are used for "head at an unusual angle / stumbling"; no distress pose, no lying down.
- **DONE** (illustrator): `assets/library/sheep.json`; preview `assets/previews/014-illustrator-b-assets.png`.

### `sheep_head_outline` (B): sheep head diagram for the gid cyst
s067-s070, s072, s073 (scale 1.4, centred at (820, 560))
- `c`, **520 x 440**. Side-profile sheep head facing right in the `head_outline` diagram style: plain grey fill `#d9d9d9`, dark grey outline,
  ear, eye dot, muzzle at the right. **No brain, no interior.**
- **Keep the skull area plain**: I draw the cyst as a pale blue circle centred at local **(-40, -60)** growing to radius **110**, plus
  red "pressure" arrows from it. Nothing else may be drawn there.
- **DONE** (illustrator): `assets/library/sheep_head_outline.json`; preview `assets/previews/014-illustrator-b-assets.png`.

### `sheep_costume` (A): Doug's sheep onesie (worn prop)
s061-s063, s066-s075, s077, s078, s081-s083, s086 (falling, rotated 85), s088 (pile)
- Anchor = **Doug's hips (0,0)**; bbox x -150..+150, y -190..+170. Drawn after Doug, works with `stand`, `walk1/2`, `wave`, `think`.
- Lumpy cream woolly onesie (cloud-bump outline) over torso, arms and legs, dark hoof mittens and boots, a woolly hood **behind** the head
  with two dark drooping ears beside the cap. **Face and red cap fully visible.**
- **DONE** (illustrator): `assets/library/sheep_costume.json`; preview `assets/previews/014-illustrator-b-assets.png`. Note: the hood and ears beside the cap must reach the cap (top about y -292), so the drawing goes above the y -190 bbox top; fitted to `stand` (in `walk1/2` the feet poke out past the boots).

### `sheepdog` (B): border collie
s064 (big, a tapeworm icon is overlaid on its belly), s077, s078, s079 (small), s083-s085 (flipped, facing left toward Doug)
- `bc`, **400 x 270**, facing right. Black-and-white border collie, white blaze, collar ruff and chest, alert half-pricked ears, long
  feathered tail held low. Working dog, not a puppy. Keep the belly area (about (-20, -120)) plain for the overlay in s064.
- **DONE** (illustrator): `assets/library/sheepdog.json`; preview `assets/previews/014-illustrator-b-assets.png`.

## Lives in you (band 2)

### `slug` (B): garden slug
s091, s092, s094 (on a leaf), s095, s109-s110 (tiny, 0.3, on Doug's lettuce)
- `bc`, **260 x 90**, facing right. Leopard-slug-like: grey-brown body `#8a7a6a` with darker spots, mantle saddle, two long eye
  tentacles and two short ones, glossy highlight line. Not slimy-gross, no face.
- **DONE** (illustrator): `assets/library/slug.json`; preview `assets/previews/014-illustrator-b-assets.png`.

### `worm_icon` (A): the generic parasite worm icon (episode-wide)
s087-s091, s100-s103, s105, s106, s108, s113, s124, s145, s156, s157, s174, s176, s195, s196, s200-s203, s209, s210, s212 (up to 15 at
once), s245
- `c`, **200 x 70**. A plain pale pink `#f2b8b8` nematode squiggle (gentle S), darker outline `#a05050`, rounded head end on the right,
  tapered tail, one faint highlight. **No face, no mouth, no segments.** Must read at 0.1-0.25 scale (20-50 px) and on maroon.
- Used `rotate: 180` as "dead / belly up" (s102, s103, s108, s113).
- **DONE** (illustrator): `assets/library/worm_icon.json`; preview `assets/previews/014-illustrator-b-assets.png`.

### `worm_suitcase` (B): the Spirometra traveller (worm icon + tiny suitcase)
s143, s153 (silhouette, glow_r 200), s154, s155, s164-s166, s170
- `c`, **240 x 120**. The same `worm_icon` worm (same colours) standing in an upright S with a **tiny brown hard-shell suitcase**
  (`travel_suitcase` look: `#a0522d` face, dark handle) held by its front end. The brief allows this one-off nod to the places prop.
- **DONE** (illustrator): `assets/library/worm_suitcase.json`; preview `assets/previews/014-illustrator-b-assets.png`.

### `worm_boots` (B): the Gnathostoma wanderer (worm icon + walking boots)
s169, s171, s172, s175, s177, s182, s190-s193 (s193: next to `compact_camera`)
- `c`, **230 x 110**. The same worm wearing **two tiny brown hiking boots** under its body, mid-stride. Same colours as `worm_icon`.
- **DONE** (illustrator): `assets/library/worm_boots.json`; preview `assets/previews/014-illustrator-b-assets.png`.

### `tapeworm` (B): adult tapeworm, cartoon
s064, s065 (big, "up to a meter"), s114, s116-s119, s122, s123, s137, s138 (small, overlaid on the `body_outline` belly)
- `c`, **460 x 220**. Long flat cream-white `#f3ecd6` ribbon in loose S loops with segment lines that get wider toward the tail end,
  a tiny knob head at the right. Diagram style, no gore, no gut.
- **DONE** (illustrator): `assets/library/tapeworm.json`; preview `assets/previews/014-illustrator-b-assets.png`.

### `pork_chop` (B): raw pork chop icon
s114, s116, s117, s118 (small cream cysts drawn on it), s137
- `c`, **260 x 180**. Pale pink meat `#f2b8b0`, white fat rim, small bone at one side. Clean grocery-icon look, nothing bloody.
- **DONE** (illustrator): `assets/library/pork_chop.json`; preview `assets/previews/014-assets-illustrator-b-small.png` + backgrounds/bbox check `assets/previews/014-pork_chop-bg.png`.

### `salad_bowl` (C): Doug's salad
s140-s142 (on the bistro table, top at y 660)
- `c`, **220 x 120**. Low white bowl with mixed green leaves, a couple of cherry tomatoes and cucumber slices. Please make it read as a
  *salad*, not as the `lettuce` head (013's look).
- **DONE** (illustrator): `assets/library/salad_bowl.json`; preview `assets/previews/014-assets-illustrator-b-small.png` + backgrounds/bbox check `assets/previews/014-salad_bowl-bg.png`.

### `frog` (C): frog
s096, s160, s173
- `bc`, **240 x 180**, facing right. Sitting green frog (`#5f9a3a`, darker spots, cream belly, gold eye). Documentary, no smile.
- **DONE** (illustrator): `assets/library/frog.json`; preview `assets/previews/014-assets-illustrator-b-small.png` + backgrounds/bbox check `assets/previews/014-frog-bg.png`.

## Eats you (band 3)

### `compost_heap` (C): compost / manure heap
s195, s197, s206
- `bc`, **640 x 280**. Brown mound `#6b4a2a` with straw strands `#c9a04a`, a few peelings and leaves, darker spray shading. Mid tones so
  it reads on maroon and on dark paddock ground `#3a2a1e`.
- **DONE** (illustrator): `assets/library/compost_heap.json`; preview `assets/previews/014-assets-illustrator-b-large.png` + backgrounds/bbox check `assets/previews/014-compost_heap-bg.png`.

### `horse` (A): chestnut horse, standing calmly
s197 (silhouette at the frame edge), s198, s199, s203-s206, s211 (small), s213 (four at 0.4), s218-s221 (flipped to face Doug; s220-s221
also `rotate: 6` to look down at the cap)
- `bc`, **680 x 560** (x -340..+340, y -560..0), facing right. Eye at about (+250, -470), muzzle/mouth at about (+330, -360)
  (s198 and s206 arrows end there).
- Real look: chestnut coat `#a0522d`, darker mane and tail, white blaze, dark hooves. **Calm, healthy, gentle eye with a soft brow** (the
  script says it looks at Doug "with something very close to sympathy"). No sores, no lumps drawn, no distress.
- **DONE** (illustrator): `assets/library/horse.json`; preview `assets/previews/014-assets-illustrator-b-large.png` + backgrounds/bbox check `assets/previews/014-horse-bg.png`.

### `mandrill` (C): mandrill, sitting
s223 (silhouette with my own red spray glow), s227 (full colour)
- `bc`, **420 x 440**, facing right (3/4 view is fine). Olive-brown fur, **red nose stripe with blue ridged cheeks**, yellow-orange beard,
  small dark eyes. Must read on near-black `#120a0c`. Silhouette shape: hunched sitting primate with a long muzzle.
- **DONE** (illustrator): `assets/library/mandrill.json`; preview `assets/previews/014-assets-illustrator-b-large.png` + backgrounds/bbox check `assets/previews/014-mandrill-bg.png`.

### `balamuthia_amoeba` (B): the boss reveal, a plain small amoeba icon
s224, s225, s230 (tiny, 0.12, on a hair), s231 (inside the head outline), s238 (in soil), s248 (above the flowerpot)
- `c`, **260 x 210**. Microscope-diagram amoeba: irregular rounded blob with a few short branching pseudopods, **pale tan-grey `#d8cbb0`**
  (deliberately *not* lilac, so it never reads as `naegleria_amoeba`), darker inner cytoplasm, one nucleus with a dark nucleolus. No
  face. The script wants it "plain" and small: the horror is that it looks like nothing. Must read on near-black.
- **DONE** (illustrator): `assets/library/balamuthia_amoeba.json`; preview `assets/previews/014-assets-illustrator-b-small.png` + backgrounds/bbox check `assets/previews/014-balamuthia_amoeba-bg.png`.

### `flowerpot` (A): terracotta pot of soil (closing image)
s222, s228, s238, s248-s254 (s253-s254: Doug's red cap sits on top of it, the final shot)
- `bc`, **240 x 230**. Plain terracotta pot `#c8643a`, darker rim band, a dark soil top `#3a2418` with a few crumbs; **soil top centre at
  (0, -215)** (the `doug_cap` sits at y -245). Must read on near-black.
- **DONE** (illustrator): `assets/library/flowerpot.json`; preview `assets/previews/014-assets-illustrator-b-small.png` + backgrounds/bbox check `assets/previews/014-flowerpot-bg.png`.
