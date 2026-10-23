# 026 Why the Deep Sea Turns Animals Into Terrifying Giants: asset requests (director, 2026-10-23)

All placements in `shotlist.json` assume the **anchor, size and facing given here** (layout was checked with placeholder
boxes of exactly these bboxes). Please keep them, or tell me and I will move the shots. House style as `anglerfish.json`:
thick black outlines (5-6), flat fills, interior shading, simple silhouettes that read at thumbnail size. Creatures are
the detailed tier. **Every creature lives on dark water** (twilight `#1b4f86` down to hadal `#020308`): use mid-tone
fills, never near-black, and keep a clean outer outline because most of them also appear as `silhouette` + red `rim`.
Brief risk notes: no smiling or cute faces (kid-appeal risk), no gore, nothing that reads as blood.

Reused from the library (no work needed): research_ship, narrator_hand, japanese_spider_crab, giant_squid, giant_squid_eye,
sperm_whale, calendar, dinner_plate, small_fish, sandwich, ruler, giraffe, small_car, baby_grand_piano, bicycle_wheel,
cat, flowerpot, aquarium, museum_building, scientist, black_smoker, submersible, rov, crt_tv, hadal_snailfish, amphipod,
world_map, pacific_map, antarctica_map, meganeura, scale_tree, sea_sponge, red_blood_cell, microscope, thumbs_up_hand,
speedometer, stew_bowl, cupcake_candle, wait_stopwatch, heart_icon, placard, rope_hook, doug_cap, worm_icon,
freshwater_snail, anglerfish, barreleye_fish, garden_spider, carpenter_ant, crab, fishing_boat, clipboard, annotations.

## Episode device / recurring props

### cable_harness
- What: Doug's winch-cable harness (worn prop, like `hard_hat`): anchor = Doug's hips (0,0), list **after** Doug at the
  same x/y/scale; `flip: true` when Doug faces left. Used on almost every shot.
- Look: grey webbing hip belt (y -12..+12, x -42..+42) with two short thigh loops; one orange `#e07b00` webbing strop from
  the back of the belt (-30,-5) running up and left to a steel shackle ring centred at **(-170,-400)** (ring r ~14,
  grey `#a9adb3`, dark outline). The strop must clear the head circle (centre (0,-218), r 72) by at least 25 units and must
  not cross the face or the cap brim (brim points right). A small yellow cable lamp clamped on the strop at about
  (-120,-300), its pale `#fff7a0` face pointing right/down. No shoulder straps (arms move a lot: float, wave, point,
  arms_up, panic, swim, crouch, thumbs_up).
- The scene draws the steel cable as a line straight up from the ring, so the ring position is load-bearing.
- Bbox about x -200..+45, y -430..+30. Auto-ink not needed (mid-grey/orange read on navy and black).
- Shots: s002-s276 (215 shots).
- DONE (illustrator): `assets/library/cable_harness.json`, preview `assets/previews/026-deep-sea-giants-assets-device-oarfish-japan-crab.png` (on Doug, white + navy: `assets/previews/026-deep-sea-giants-harness-on-doug.png`).

### cable_counter_icon
- What: icon for the episode's **CABLE OUT** meter (sits left of the size-28 label at (1590, 238), like 016's ice cube).
- Look: small winch drum seen side-on, grey drum wound with dark cable, red crank handle, very thick outline. Must read at
  32 px. Anchor centre, about 180x180. Used at scale 0.16 on every shot (s002-s281).
- Note for the art director: the brief asks that this meter reads as a cable counter, not 006's depth gauge.
- DONE (illustrator): `assets/library/cable_counter_icon.json`, preview `assets/previews/026-deep-sea-giants-assets-device-oarfish-japan-crab.png`.

### why_clipboard
- What: the episode device **WHY SO BIG?** clipboard; the narrator's hand writes one reason per item on it.
- Look: big brown `#a0522d` board, silver clip at the top, **blank** white sheet (no scribbles, no tick: text is
  overlaid by the scene). Sheet zone x -180..+180, y -240..+260; the scene writes the title at local y -185 and lines at
  y -110, -50, 10, 70, 130, 190 (centred at x 0), so keep that area empty and flat white. Anchor centre, 420x580.
- Shots: s042, s043, s090, s150, s177, s238, s254, s272 (at scale 0.9-1.0, centre about (1350, 750)).
- DONE (illustrator): `assets/library/why_clipboard.json`, preview `assets/previews/026-deep-sea-giants-assets-device-oarfish-japan-crab.png`.

### drop_camera
- What: the 2011 Scripps / National Geographic free-fall lander ("dropcam").
- Look: yellow tubular frame, two orange glass float spheres at the top, a camera housing and one lamp at the bottom,
  lifting ring on top. Anchor bottom-centre (feet on y=0), about 260x380 (y -380..0). Faces right.
- Shots: s263 (hanging under the ship, 0.55), s265 (on the trench mud, 0.6).
- DONE (illustrator): `assets/library/drop_camera.json`, preview `assets/previews/026-deep-sea-giants-assets-device-oarfish-japan-crab.png`.

## Creatures (item order)

### giant_oarfish
- Real look: *Regalecus glesne*, longest bony fish. Long ribbon-like silver body (`#c9d3dc`, faint grey speckles, bluish
  shading on one side), a tall red `#e0302a` crest of long fin rays on top of the head, one red dorsal fin running the
  whole length of the back, small mouth, round eye, body tapering to a thin tail. No pelvic "oars" needed beyond two thin red streamers.
- **Drawn vertical, head at the TOP** (it is always shown hovering upright), dorsal fin along the right edge.
  Anchor centre, about 160x1000 (x -80..80, y -500..500).
- Shots: s003 (silhouette), s006, s008 (silhouette), s009-s029; s010 and s020 use `rotate: 90` to lay it horizontal; s274.
- DONE (illustrator): `assets/library/giant_oarfish.json`, preview `assets/previews/026-deep-sea-giants-assets-device-oarfish-japan-crab.png` (navy + silhouette/rim + rotated: `assets/previews/026-deep-sea-giants-oarfish-crab-detail.png`).

### giant_oarfish_beached
- Same fish lying on its side on a beach, head right, limp crest, dull silver, eye a simple cartoon X (no wounds).
  Anchor bottom-centre (resting on y=0), about 1000x150. Shots: s020, s021.
- DONE (illustrator): `assets/library/giant_oarfish_beached.json`, preview `assets/previews/026-deep-sea-giants-assets-device-oarfish-japan-crab.png`.

### japan_map / japan_map_cracked
- world_map style (flat green `#6cbf5a` land, dark green outline, light-blue sea, black frame, no labels): Japan's four
  main islands, Pacific coast facing right/east. Anchor centre, about 640x720 frame.
- `japan_map_cracked`: identical, plus a black zigzag crack across Honshu with a few small chips. Same anchor.
- Shots: japan_map s013, s014, s016, s017, s031 (inset), s038; cracked s018 (red X stamped over it).
- DONE (illustrator): `assets/library/japan_map.json` + `assets/library/japan_map_cracked.json`, preview `assets/previews/026-deep-sea-giants-assets-device-oarfish-japan-crab.png`.

### spider_crab_folded
- A resting Japanese spider crab with its long legs folded up and over into a tent shape, so from a distance it looks like
  a closed broken umbrella. Pale orange/beige (`#e8b48a`) with the library crab's white spots. Anchor bottom-centre
  (leg tips on y=0), about 300x260. Shots: s031-s033.
- DONE (illustrator): `assets/library/spider_crab_folded.json`, preview `assets/previews/026-deep-sea-giants-assets-device-oarfish-japan-crab.png`.

### japanese_spider_crab_cap
- Exactly `japanese_spider_crab` (front view, anchor centre, ~700x420) with Doug's red cap (`doug_cap` geometry) held up
  in its right claw, claw raised to about (+250,-260). Shots: s052-s055.
- DONE (illustrator): `assets/library/japanese_spider_crab_cap.json`, preview `assets/previews/026-deep-sea-giants-assets-device-oarfish-japan-crab.png`.

### giant_phantom_jelly
- Real look: *Stygiomedusa gigantea*. Dark red-maroon bell (`#8a1a2a`, lighter rim `#b8344a`, mid-tone so it reads on navy),
  about 300 wide, and **four** long wavy ribbon-like arms (curtains) hanging down, no stinging tentacles.
  Anchor = bell centre (0,0); bell x -150..150, y -110..60; arms down to y ~+880, spread x -220..220.
- Shots: s057 and s059 (silhouette), s060-s077, s066 tiny (0.13), s067 tiny on the map; s274.
- DONE (illustrator): `assets/library/giant_phantom_jelly.json`, preview `assets/previews/026-deep-sea-giants-assets-b-jelly.png` (white / navy / silhouette+rim / 168px tile), contact sheet `assets/previews/026-deep-sea-giants-assets-b.png`. Bbox x -265..250, y -112..900.

### pelagic_brotula
- Small fish that lives with the jelly: elongated eel-like body, dull pinkish-tan `#c9a38a`, continuous dorsal/anal fin
  fringe, small eye. Facing right, anchor centre, about 200x70. Shots: s071 (silhouette)-s075, s077.
- DONE (illustrator): `assets/library/pelagic_brotula.json`, preview `assets/previews/026-deep-sea-giants-assets-b-jelly.png` (white / navy / silhouette+rim / 168px tile), contact sheet `assets/previews/026-deep-sea-giants-assets-b.png`.

### tennis_court_top
- Half a tennis court seen from directly above, its **width (10.97 m doubles) running left-right**: 550 units wide
  (50 u/m), showing the baseline at the bottom, service boxes, and the net at the top, about 600 units tall. Green-blue
  court, white lines. Anchor bottom-centre (baseline centre), bbox x -290..290, y -620..10. Shot: s062.
- DONE (illustrator): `assets/library/tennis_court_top.json`, preview `assets/previews/026-deep-sea-giants-assets-b-jelly.png` (white / navy / silhouette+rim / 168px tile), contact sheet `assets/previews/026-deep-sea-giants-assets-b.png`.

### giant_isopod
- Real look: *Bathynomus giganteus*. Side view facing right: pale lilac-grey `#a9a3b8` armoured, segmented pill-bug body,
  big dark compound eyes, two pairs of antennae, seven pairs of legs, tail fan. Unbothered, not cute.
  Anchor bottom-centre (legs on y=0), about 500x220. Shots: s079-s106, s178, s274 (some flipped, s099 `rotate: 180`).
- DONE (illustrator): `assets/library/giant_isopod.json`, preview `assets/previews/026-deep-sea-giants-assets-b-isopod.png` (white / navy / silhouette+rim / 168px tile), contact sheet `assets/previews/026-deep-sea-giants-assets-b.png`. Antennae reach x +300 (bbox x -285..300).

### giant_isopod_rolled
- The same isopod curled into a tight armoured ball (pill bug defence). Anchor bottom-centre, about 230x230.
  Shots: s083 (tile), s084, s085.
- DONE (illustrator): `assets/library/giant_isopod_rolled.json`, preview `assets/previews/026-deep-sea-giants-assets-b-isopod.png` (white / navy / silhouette+rim / 168px tile), contact sheet `assets/previews/026-deep-sea-giants-assets-b.png`.

### giant_isopod_full
- The same isopod after a huge meal: bloated round belly bulging between the plates, legs barely touching the ground,
  one sweat drop. Anchor bottom-centre, about 520x260. Shot: s089 (beside the library `whale_skeleton`).
- DONE (illustrator): `assets/library/giant_isopod_full.json`, preview `assets/previews/026-deep-sea-giants-assets-b-isopod.png` (white / navy / silhouette+rim / 168px tile), contact sheet `assets/previews/026-deep-sea-giants-assets-b.png`.

### colossal_squid
- Real look: *Mesonychoteuthis hamiltoni*. Side view, mantle at the left, arms to the right: very wide heavy red-maroon
  mantle (`#b33a3a`) with fins at the tip, one huge pale silver-blue eye, eight short thick arms and two tentacles with
  visible rows of small pale hooks. Anchor centre, about 900x400. Shots: s003, s107, s110 (silhouette), s111-s125, s274.
- DONE (illustrator): `assets/library/colossal_squid.json`, preview `assets/previews/026-deep-sea-giants-assets-b-squid.png` (white / navy / silhouette+rim / 168px tile), contact sheet `assets/previews/026-deep-sea-giants-assets-b.png`. Bbox x -462..472, y -165..165.

### colossal_squid_juvenile
- The 2025 juvenile: small, glassy translucent body (pale `#e8e2e6` with pink-brown chromatophore dots), big eyes, short
  arms. Facing right, anchor centre, about 260x120. Shots: s129, s130 (next to the 30 cm `ruler`).
- DONE (illustrator): `assets/library/colossal_squid_juvenile.json`, preview `assets/previews/026-deep-sea-giants-assets-b-squid.png` (white / navy / silhouette+rim / 168px tile), contact sheet `assets/previews/026-deep-sea-giants-assets-b.png`.

### colossal_squid_hook_arm
- Close-up of one tentacle club curling up from the bottom of frame: thick red tentacle with a row of pale swivelling hooks.
  The top hook curls open so `doug_cap` can hang from it at about **(0,-580)**. Anchor bottom-centre, about 240x620.
  Shots: s119, s120, s126-s127 (small, rotated 90), s132-s135 (cap hanging on it).
- DONE (illustrator): `assets/library/colossal_squid_hook_arm.json`, preview `assets/previews/026-deep-sea-giants-assets-b-squid.png` (white / navy / silhouette+rim / 168px tile), contact sheet `assets/previews/026-deep-sea-giants-assets-b.png`. Top hook spans x -22..40, y -630..-540; its tip dips into the cap at the s132 placement (checked).

### greenland_shark
- Real look: *Somniosus microcephalus*. Side view facing right: heavy cigar body, grey-brown `#6e6a64` with darker back,
  small rounded dorsal fins set far back, short blunt snout, tiny pale eye (no eye parasite), small pectorals. Slow, old.
  Anchor centre, about 900x260. Shots: s136-s160 (s142 at 1.8 as a head close-up, s149 tiny), s274.
- DONE (illustrator): `assets/library/greenland_shark.json`, preview `assets/previews/026-deep-sea-giants-shark-ship-tubes-dark.png` (white / twilight / hadal / silhouette+rim / 168px tile), contact sheet `assets/previews/026-deep-sea-giants-assets-shark-spider.png`. Bbox x -470..446, y -146..128 (tail tip and dorsal a little past the 900x260 box). Head close-up at 1.8 checked: tiny pale eye, flat (not smiling) underslung mouth.

### mayflower_ship
- 17th-century three-masted merchant ship under sail, brown hull, cream sails, small red pennant, facing right.
  Anchor waterline centre, about 600x620 (mast tops at y -560). Shot: s149.
- DONE (illustrator): `assets/library/mayflower_ship.json`, preview `assets/previews/026-deep-sea-giants-shark-ship-tubes-dark.png`, contact sheet `assets/previews/026-deep-sea-giants-assets-shark-spider.png`. Bbox x -300..322 (bowsprit), y -560..+10; hull dips 10 units below the waterline, with a white ripple on y 0.

### giant_tube_worms
- Real look: *Riftia pachyptila*. A thicket of about seven thick white tubes (`#f2efe6`, faint ring lines) of different
  heights up to 600 units, each topped with a bright red `#e0302a` feathery plume; dark rubble base. Not the library's thin
  `tubeworm_cluster`. Anchor bottom-centre, about 520x640. Shots: s161-s183, s274.
- DONE (illustrator): `assets/library/giant_tube_worms.json`, 8 tubes, preview `assets/previews/026-deep-sea-giants-shark-ship-tubes-dark.png`, contact sheet `assets/previews/026-deep-sea-giants-assets-shark-spider.png`. Bbox x -272..269, y -652..0.

### bigfin_squid
- Real look: *Magnapinna*. Pale whitish-pink `#e8dcdc` small mantle pointing **up** with two big round fins at the top,
  arms held straight out to the sides then bent sharply down at the "elbows" into very long thin filaments hanging down.
  Anchor = the elbow-level centre (0,0): mantle up to y -220, elbows at about x +-250, y 0, filaments down to y +800.
  Bbox about x -260..260, y -220..800. Shots: s185-s206 (s196/s200 tiny), s274.
- DONE (illustrator): `assets/library/bigfin_squid.json`, 10 arms, preview `assets/previews/026-deep-sea-giants-bigfin-dark.png` (white / twilight / hadal / silhouette+rim / 168px tile), contact sheet `assets/previews/026-deep-sea-giants-assets-shark-spider.png`. Bbox x -274..260, y -228..800.

### giant_sea_spider (+ _xray, _cap)
- Real look: *Colossendeis colossea*. Front/side view: eight very long thin jointed pale cream-orange `#e8c8a0` legs arched
  like a tall spider, a tiny body (thumb-length) at the top centre about y -330, leg tips on the ground at x +-420.
  Anchor bottom-centre (leg tips on y=0), about 860x420.
- `giant_sea_spider_xray`: identical geometry, legs semi-pale with orange gut branches drawn inside each leg and small
  gonad bulges, a tiny red heart in the body. Shots: s221, s222, s224, s225.
- `giant_sea_spider_cap`: identical, with `doug_cap` hooked on the tip of the front-right leg, that leg lifted a little
  (bbox top about y -460). Shot: s230.
- Shots (plain): s207-s229 (s213 at 0.04 on Doug's hand), s274.
- DONE (illustrator): `assets/library/giant_sea_spider.json`, `giant_sea_spider_xray.json`, `giant_sea_spider_cap.json`, preview `assets/previews/026-deep-sea-giants-sea-spider-dark.png` (white / twilight / hadal / silhouette+rim / 168px tile), contact sheet `assets/previews/026-deep-sea-giants-assets-shark-spider.png`. Bbox x -427..427, y -418..0 (proboscis hangs from the body to y -250). Cap variant: lifted front-right leg tip at (392,-428), cap top about y -485, right edge about x +460.

### stethoscope_crouch
- Worn prop for Doug's `crouch` pose, facing right: anchor = Doug's hips, list after Doug at the same x/y/scale.
  Earpieces at the sides of the head (crouch has drop 61 and lean 15), grey tubing hanging down to the front hand
  (held out at chest height), the chest piece held in that hand. Keep the face and cap clear. Please tell me the chest-piece
  local point so I can put the spider's leg on it. Shot: s227 (Doug at (700, 870), scale 0.6).
- DONE (illustrator): `assets/library/stethoscope_crouch.json`, preview `assets/previews/026-deep-sea-giants-stethoscope-on-doug.png`, s227 layout check `assets/previews/026-deep-sea-giants-s227-check.png`, contact sheet `assets/previews/026-deep-sea-giants-assets-amphipod-xeno.png`. **Chest-piece centre = local (172, -48)**, so in s227 it is at canvas (803, 841). Earpieces at local (-22,-142) and (134,-142). Note for s227: the spider at (1150, 935) x1.4 has its left legs at x 560-890, so they cross Doug (see the check PNG); move the spider right by ~120 or accept the legs framing him.

### supergiant_amphipod
- Real look: *Alicella gigantea*. Pale white with a faint pink-orange tint `#f2e6e0`, long segmented shrimp-like body
  (less curled than the library `amphipod`), side plates, many legs, long antennae, small dark eye. Facing right, anchor
  centre, about 500x200. Used as a swarm of 8-18 copies (s250-s252) at 0.28-0.38, some flipped and rotated up to 25 deg.
  Shots: s231-s252, s274.
- DONE (illustrator): `assets/library/supergiant_amphipod.json`, preview `assets/previews/026-deep-sea-giants-amphipod-xeno-foram-dark.png` (white / twilight / hadal / silhouette+rim / 168px tile), contact sheet `assets/previews/026-deep-sea-giants-assets-amphipod-xeno.png`. Bbox x -226..276, y -80..90.

### xenophyophore
- Real look: a giant single-celled foram: a lumpy, fragile, honeycombed grey-brown `#8a8274` mud-grain "sponge" with a
  few open pores (homes for tenants), flat bottom resting on mud. No face. Anchor bottom-centre, about 260x200
  (y -200..0). Shots: s003, s253 (silhouette), s256-s281 (s257-s275 at 1.6-2.2 close-ups, s278-s281 small on the monitor).
- DONE (illustrator): `assets/library/xenophyophore.json`, preview `assets/previews/026-deep-sea-giants-amphipod-xeno-foram-dark.png`, contact sheet `assets/previews/026-deep-sea-giants-assets-amphipod-xeno.png`. Bbox x -132..132, y -196..0. Six open pores.

### foram_shell
- Classic tiny chambered spiral foram shell, cream `#efe6d0`, seen in a microscope view. Anchor centre, about 120x120.
  Shot: s259.
- DONE (illustrator): `assets/library/foram_shell.json`, preview `assets/previews/026-deep-sea-giants-amphipod-xeno-foram-dark.png`, contact sheet `assets/previews/026-deep-sea-giants-assets-amphipod-xeno.png`. Bbox x -50..51, y -45..44.
