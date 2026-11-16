# 049 asset requests (director, 2026-11-16)

32 new drawings. The shotlist already places them using the anchors, sizes and local coordinates below, so please
keep those (or tell me what changed and I'll re-place them). Creatures and places are the detailed tier (layered
fills, interior shading, outlines 3-5); humans are crude tier with `auto_ink`. **No gore anywhere**: dead bees are
whole round cartoon bees with X eyes, the meat ball is a plain bundle with no legs, wings or heads visible, and no red
fluids (brief, thumbnail direction). Nothing cute: no smiles or blush on bees, hornets or larvae. Costumes are
deadpan felt suits, no bouncing antennae (brief, running gags).

Reused from the library (no work needed): `asian_giant_hornet`, `honeybee`, `beehive`, `hot_tub`, `thermometer`,
`field_guide_open`, `narrator_hand`, `narrator_hand_pencil`, `hollow_tree`, `pine_tree`, `fallen_log`, `nest_mound`,
`japan_map`, `china_map`, `pacific_map`, `bc_map`, `north_america_map`, `usa_map`, `container_ship`, `airplane`,
`vacuum_cleaner`, `basketball`, `glass_jar`, `bug_net`, `big_water_bottle` (blank label, overlaid "SPORTS DRINK", no
brand), `sap_cup`, `calendar`, `alarm_clock`, `old_book`, `phone`, `placard`, `wildlife_official`, `parasitic_wasp`,
`fly_swatter`, `trophy_cup`, `doug_cap`, `gravestone`, annotation set.

## HUD

### `the_target` (198 shots, every shot from s002)
- **DONE** (illustrator, 2026-11-16): `assets/library/the_target.json`, preview `assets/previews/049-giant-hornet-slaughter-assets.png`.
- What: THE TARGET, the episode-only HUD device (brief section 2; art director owns the look). A crude MS Paint
  archery target: 3 rings red `#e0201b` / white / red with a black bullseye dot, thick black outline, a small wooden
  easel leg or two behind it, one arrow stuck slightly off-centre. **Must not look like 041's price tag or 043's
  fingerpost.**
- Anchor centre, about 200x200 (x -100..100, y -100..100). Used at scale 0.2 (40 px) left of the size-28 label
  "TARGET: BEE / HIVE / DOUG / NORTH AMERICA" at y 238, so it must read at 40 px: thick rings, no fine detail.
- At the boss (s193 on) the label turns red-on-pink ("stamped"); the icon stays as is.

## Hornets, bees and nest contents

### `honeybee_dead` (11 shots: s002, s049, s052, s054, s059-s062, s068, s069, s108; also the thumbnail pile)
- **DONE** (illustrator, 2026-11-16): `assets/library/honeybee_dead.json`, preview `assets/previews/049-giant-hornet-slaughter-assets.png`. ~260x190; ground contact about y +60 local.
- Whole cartoon western honeybee lying on its back: same colours as `honeybee` (golden abdomen with dark bands,
  fuzzy brown thorax), round and chunky, six thin legs folded up in the air, wings crumpled flat, **X eyes** (black X
  on the head). Whole and clean: no missing parts, no fluid.
- Anchor centre, about 220x150 (like `honeybee`). Used at 0.26-0.32 in rows on the ground, so keep the X eyes big.

### `asian_giant_hornet_front` (5 shots: s070, s072, s077, s125, s133)
- **DONE** (illustrator, 2026-11-16): `assets/library/asian_giant_hornet_front.json`, preview `assets/previews/049-giant-hornet-slaughter-assets.png`. ~480x430; feet at about y +215 local.
- The `asian_giant_hornet` seen from the front, facing the camera: big orange-yellow head with dark kidney-shaped
  eyes on both sides, three small ocelli, **black toothed mandibles open**, dark brown thorax shoulders, wings raised
  behind like a V, front legs planted. Menacing, not cute (no pupils, no smile).
- Anchor centre, about 500x420. Used at 0.4 (standing guard at a hive entrance) to 0.9 (hero close-up).

### `meat_ball_bundle` (6 shots: s014-s016, s022-s024)
- **DONE** (illustrator, 2026-11-16): `assets/library/meat_ball_bundle.json`, preview `assets/previews/049-giant-hornet-slaughter-assets.png`.
- The hornet's "meat ball": a round, slightly lumpy brown `#8a5a2a` bundle with darker `#5e3a1a` creases and a
  soft highlight, like a rolled-up ball of chewed material. **No legs, wings or heads visible on it.** No red.
- Anchor centre, about 200x180 (x -100..100, y -90..90). The shotlist sits `doug_cap` on top at about (0, -85)
  local for Doug's death (s022-s024), so keep the top roundish.

### `brood_bundle` (2 shots: s075, s079)
- **DONE** (illustrator, 2026-11-16): `assets/library/brood_bundle.json`, preview `assets/previews/049-giant-hornet-slaughter-assets.png`.
- Same shape and anchor as `meat_ball_bundle`, but pale cream `#f2e6c8` with light-grey creases: the honeybee
  brood chewed into paste, carried home.

### `hornet_larva_cell` (16 shots: s015-s019, s023, s024, s079, s080, s083-s085, s087-s090)
- **DONE** (illustrator, 2026-11-16): `assets/library/hornet_larva_cell.json`, preview `assets/previews/049-giant-hornet-slaughter-assets.png`.
- One cell of a hornet nest comb seen from the front: grey-tan paper hexagon `#cfc6b4` with darker paper rim and
  faint paper-layer stripes, and a fat white `#fbf6e6` grub filling it, its head capsule poking out at the top:
  small brown head with tiny mandibles, **no eyes, no face**. Soft cream shading on the body segments.
- Anchor centre, about 260x320. Mouth at about (+40, -90) local: the shotlist puts pale yellow drool drops there.
  Used from 0.7 (rows of three on a `#d8cfbd` nest background) to 1.3 (close-up).

### `bee_heat_ball` (9 shots: s091 silhouette, s097-s099, s101-s104, s110)
- **DONE** (illustrator, 2026-11-16): `assets/library/bee_heat_ball.json`, preview `assets/previews/049-giant-hornet-slaughter-assets.png`.
- The Japanese honeybee "heat ball": a tight round ball of 60-80 overlapping bees (Japanese honeybees, a bit darker
  than `honeybee`: dark grey-brown with thin pale bands), all facing inward, wings sticking out at angles; one smoky
  hornet wing tip and a sliver of orange hornet head peek out near the centre. A few faint heat-shimmer lines.
- Anchor centre, roughly round, radius about 280 (560x560). Must be opaque: in s110 it is placed over Doug (scale 0.6)
  at scale 0.7 to hide him completely, and `doug_cap` sits on top at about (0, -340) local. Bold silhouette (s091 uses
  `silhouette: true`).

### `hornet_radio_tagged` (2 shots: s176, s177)
- **DONE** (illustrator, 2026-11-16): `assets/library/hornet_radio_tagged.json`, preview `assets/previews/049-giant-hornet-slaughter-assets.png`.
- Exactly `asian_giant_hornet` (same anchor, size, pose, facing right) with a tiny black radio tag (a small dark box
  with a thin trailing antenna wire, about 40x24 local) tied at the narrow waist between thorax and abdomen with a few
  loops of **white dental floss**. Used at 1.0 (close-up) and 0.3 (in flight).

### `hornet_stinger` (5 shots: s114 silhouette, s115-s118)
- **DONE** (illustrator, 2026-11-16): `assets/library/hornet_stinger.json`, preview `assets/previews/049-giant-hornet-slaughter-assets.png`.
- Diagram close-up: the last two banded segments of a hornet abdomen (dark brown and yellow-orange, like the hornet)
  at the left, x -350..+40, and a long, straight, dark brown, sharply pointed stinger coming out of it to the right,
  from x +40 to the tip at **(+400, 0)**. Faint highlight along the stinger. No venom drop, no red.
- Anchor centre, about 750x260 (y -130..130). The shotlist draws a dotted measuring line under the stinger from
  x +40 to +400 at scale 1.1, and passes the stinger through a white "suit fabric" strip at local x +230..+340.

### `capped_cells` (1 shot: s186)
- **DONE** (illustrator, 2026-11-16): `assets/library/capped_cells.json`, preview `assets/previews/049-giant-hornet-slaughter-assets.png`.
- Close-up of a piece of hornet nest comb: grey paper hexagonal cells, most of them **capped with domed white silk
  caps** (queen pupae), a couple open and empty. Anchor centre, about 520x400.

### `brood_comb` (5 shots: s066, s067, s073-s075)
- **DONE** (illustrator, 2026-11-16): `assets/library/brood_comb.json`, preview `assets/previews/049-giant-hornet-slaughter-assets.png`.
- Inside a honeybee hive: one honeycomb panel in a wooden frame (top bar visible), wax-yellow hexagon cells, most
  capped tan/white (brood), a few open showing pearly white C-shaped larvae. Flat, front view.
- Anchor centre, **about 900x500** (x -450..450, y -250..250). Used at 1.2-1.25 centred at (960, 560-600) on an
  amber `#e9b64a` background, so at 1.25 its top lands at y 288 (clear of the counter zone). Doug stands in front of it.

## Doug costumes (worn props; anchor = Doug's hips, list after Doug at the same x/y/scale)

### `bee_costume` (65 shots, items 1-4; e.g. s002, s004-s006, s008-s010, s021, s041-s046, s064-s067, s071-s091)
- **DONE** (illustrator, 2026-11-16): `assets/library/bee_costume.json`, preview `assets/previews/049-giant-hornet-slaughter-assets.png`. Torso-only suit (house convention), fits stand/hands_hips/panic/thumbs_up/arms_up/walk and flips. **For s088 `crouch` use `bee_costume_crouch`** (same x/y/scale; pre-leaned 15 deg and dropped 61 like the rig).
- Doug's homemade honeybee onesie: golden-yellow `#f2b632` felt with three wide black `#2a2a2a` stripes across the
  torso, fuzzy brown felt yoke at the shoulders, zipper, a short round striped abdomen bulb behind the hips at about
  (-140, 0) with a small soft felt stinger tip, two small clear plastic wings on the back pointing up-left.
  **Head, face and red cap fully visible; no antennae** (or at most two short stiff ones on a headband beside the cap,
  never over it, never bouncy).
- Must fit poses: `stand`, `hands_hips` (s021: "arms folded"), `panic1`/`panic2`, `crouch` (s088, holding a cup),
  `thumbs_up` (s089), `arms_up` (s090), `walk`. Facing right and flipped for facing left.

### `bee_costume_flat` (2 shots: s068 death 370, s131)
- **DONE** (illustrator, 2026-11-16): `assets/library/bee_costume_flat.json`, preview `assets/previews/049-giant-hornet-slaughter-assets.png`.
- The bee costume lying empty and flat on the ground (family of `fly_pupa_costume_flat`): squashed yellow/black felt
  suit, collapsed collar hole on the right, crumpled wings, abdomen bulb sagging, and **two printed X eyes** (white
  discs with black X) on the front of the collar. No Doug inside.
- Anchor bottom-centre on the ground, about 470x150. The shotlist puts `doug_cap` on it at about (+115, -70) local.

### `hornet_costume` (2 shots: s109, s110)
- **DONE** (illustrator, 2026-11-16): `assets/library/hornet_costume.json`, preview `assets/previews/049-giant-hornet-slaughter-assets.png`.
- Doug's giant-hornet onesie (the costume swap at The Heat Ball): orange-yellow felt hood ring around his face with
  two big dark felt kidney eyes on a headband beside the cap (never over it), dark brown felt thorax suit with two
  orange spots, a banded dark brown / yellow-orange abdomen bulb behind the hips at (-150, 0) ending in a blunt felt
  stinger, smoky plastic wings on the back. Face and red cap fully visible. Pose `stand`, facing right.

### `hornet_costume_flat` (2 shots: s111 death 371, s112)
- **DONE** (illustrator, 2026-11-16): `assets/library/hornet_costume_flat.json`, preview `assets/previews/049-giant-hornet-slaughter-assets.png`.
- The hornet costume empty and flat on the ground, same family as `bee_costume_flat`: squashed brown/orange suit,
  felt eyes drooping on the bent headband, printed X eyes on the collar. **Two or three soft white steam wisps**
  rising off it are fine (cooked joke), nothing red.
- Anchor bottom-centre, about 470x150; `doug_cap` sits on it at about (+120, -73) local.

### `beekeeper_suit` (2 shots: s132, s133)
- **DONE** (illustrator, 2026-11-16): `assets/library/beekeeper_suit.json`, preview `assets/previews/049-giant-hornet-slaughter-assets.png`. Sleeves are fitted to `thumbs_up` (s132, s133). For a `stand` Doug use `beekeeper_suit_stand`.
- A standard white cotton beekeeping suit worn over Doug: white `#f7f7f2` suit with light grey shading, front zipper,
  elastic cuffs and ankles, a round hood with a black mesh veil ring that **frames his face (face fully visible)**, and
  the red cap sitting on top of the hood (the rig draws the cap; the hood stays below it). Poses `thumbs_up` and
  `stand`, facing right.

### `beekeeper_suit_on_back` (2 shots: s134 death 372, s135)
- **DONE** (illustrator, 2026-11-16): `assets/library/beekeeper_suit_on_back.json`, preview `assets/previews/049-giant-hornet-slaughter-assets.png`.
- The same suit fitted to Doug's `on_back` death pose (hips at x,y, head to the left, body horizontal out to about
  x +150 x scale), following the art bible "costume on his back" rules: hood and veil around the head at the left
  without covering the X eyes or the cap. Listed after Doug at the same x/y/scale, no rotate.

## People (crude tier, `auto_ink`, anchor hips, feet +150, faces right)

### `hiker` (4 shots: s078, s127, s128, s195)
- **DONE** (illustrator, 2026-11-16): `assets/library/hiker.json`, preview `assets/previews/049-giant-hornet-slaughter-assets.png`. The front hand (pole grip) is at (+148,-158), so the s195 `phone` at (+150,-167) lands in it.
- Stick-man hiker: bucket hat (khaki, not red), small backpack, walking pole in the front hand. Used at 0.6.
  In s195 the shotlist puts `phone` in his front hand at about (+150, -167) x scale.

### `hornet_crew_member` (7 shots: s119, s120, s179-s182, s198)
- **DONE** (illustrator, 2026-11-16): `assets/library/hornet_crew_member.json`, preview `assets/previews/049-giant-hornet-slaughter-assets.png`.
- Stick man in a bulky, thick white protective suit (two puffy layers, visible seams), a full clear face shield over
  a hood (face visible behind it), thick white gloves and boots. The WSDA eradication crew. Used at 0.6-0.8, flipped
  in some shots.

### `gloved_hand` (1 shot: s176)
- **DONE** (illustrator, 2026-11-16): `assets/library/gloved_hand.json`, preview `assets/previews/049-giant-hornet-slaughter-assets.png`.
- A crude-tier forearm and hand in a **purple nitrile glove** entering horizontally from the right edge, fingertips
  pinching a loop of white dental floss. Anchor (0,0) = fingertips; the sleeve runs right to about (+760, 0..90),
  off-frame at scale 1 when placed at x 1200.

## Places and props

### `nest_tree` (9 shots: s173 silhouette, s174, s177-s179, s188-s190, s194)
- **DONE** (illustrator, 2026-11-16): `assets/library/nest_tree.json`, preview `assets/previews/049-giant-hornet-slaughter-places.png`.
- The Blaine nest tree: a thick alder trunk, grey-brown bark `#7a7268` with pale lichen patches and vertical bark
  strokes, two cut stub branches and a short leafy top (keep it short), flared roots. A small dark oval **entrance
  hole centred at (-20, -390)**, rx 35 ry 45, interior `#1a120c`.
- Anchor bottom-centre, **x -160..160, y -620..0** (top must stay below the caption bar at scale 1.0 on ground y 930).
  Reads on the pre-dawn `#0b1020` sky (use a mid-tone bark, not near-black). Bold silhouette for s173.

### `nest_tree_wrapped` (3 shots: s180-s182)
- **DONE** (illustrator, 2026-11-16): `assets/library/nest_tree_wrapped.json`, preview `assets/previews/049-giant-hornet-slaughter-places.png`.
- `nest_tree` (same anchor and size) wrapped in clear plastic stretch film: pale blue tint, white crinkle highlights,
  three bands of grey tape; the entrance hole at (-20, -390) left open (the vacuum hose goes in there).

### `nest_tree_open` (7 shots: s003, s183-s186, s191, s192)
- **DONE** (illustrator, 2026-11-16): `assets/library/nest_tree_open.json`, preview `assets/previews/049-giant-hornet-slaughter-places.png`. Right half inner edge runs (+90,-40) to (+230,-600); its pale cut face reaches about +262 at shoulder height, so Doug at x +280 `point` facing left (s003, s191, s192) has his hand on it. The hollow now has a dark back wall so the nest sits inside the trunk.
- The trunk section **cut open lengthwise and pulled apart like an open book**: left half (x -380..-80) and right
  half (x +80..+380) leaning outward, pale cut wood faces, and in the hollow between them a basketball-sized grey paper
  nest (layered combs, rows of white capped cells, and 4-5 big hornet queens peeking out).
- Anchor bottom-centre, about 760x620 (y -620..0). Doug stands at x +280 (facing left, `point`) with his hand on the
  right half's inner edge (s191, s192, s003).

### `nest_tree_open_empty` (2 shots: s193 death 374, s199 closing)
- **DONE** (illustrator, 2026-11-16): `assets/library/nest_tree_open_empty.json`, preview `assets/previews/049-giant-hornet-slaughter-places.png`. A grey paper stalk ledge with its top at y -270 holds `doug_cap_radio_tag` at (0,-290).
- Same as `nest_tree_open` but the hollow is **empty** (vacuumed): bare paper scraps only, no hornets, no nest.
  In s199 the shotlist sets `doug_cap_radio_tag` inside the hollow at about (0, -290) local.

### `doug_cap_radio_tag` (2 shots: s199, s202)
- **DONE** (illustrator, 2026-11-16): `assets/library/doug_cap_radio_tag.json`, preview `assets/previews/049-giant-hornet-slaughter-assets.png`.
- `doug_cap` geometry (red cap, right brim) with the same tiny black radio tag as `hornet_radio_tagged` tied to the
  cap's button / brim with a few loops of white dental floss, short antenna wire. Anchor centre, about 220x110.

### `border_booth` (3 shots: s170-s172)
- **DONE** (illustrator, 2026-11-16): `assets/library/border_booth.json`, preview `assets/previews/049-giant-hornet-slaughter-places.png`. x -280..+520 (the roof overhangs 20 each side).
- A small border-control booth: white kiosk with a flat roof, a big sliding window at the front, a blank
  sign panel over the window, and a red-and-white striped boom barrier sticking out to the **right** (Doug and his
  sign stand on the left). Anchor bottom-centre, about 520x560 (x -260..+260 plus the barrier to about +520,
  y -560..0).

### `passport` (2 shots: s171, s172)
- **DONE** (illustrator, 2026-11-16): `assets/library/passport.json`, preview `assets/previews/049-giant-hornet-slaughter-assets.png`.
- A small generic passport booklet: navy cover, a gold round emblem and gold lines (no country, no words). Anchor
  centre, about 160x220. Held in Doug's front hand at 0.5, lying on the ground at 0.4.

### `newspaper_blank` (3 shots: s167-s169)
- **DONE** (illustrator, 2026-11-16): `assets/library/newspaper_blank.json`, preview `assets/previews/049-giant-hornet-slaughter-assets.png`. Headline rule removed, so the blank area runs y -215..-55.
- Same layout as `newspaper_curse` (masthead THE DAILY NEWS over a double rule, grey photo box, grey column lines,
  dog-eared corner) but with the **headline area blank**: the shotlist overlays "MURDER HORNET" centred at
  (0, -100) local, up to 480 wide, and strikes it out with a red line. Anchor centre, about 520x640.

### `shipping_container` (1 shot: s166)
- **DONE** (illustrator, 2026-11-16): `assets/library/shipping_container.json`, preview `assets/previews/049-giant-hornet-slaughter-places.png`.
- A standard 40-ft shipping container, side view: red-orange `#c8452f` corrugated steel (vertical ridges), darker
  corner posts and rails, door end with locking bars at the right. Real proportion about 12.2 x 2.6 m.
  Anchor bottom-centre, about 1200x260.

### `aa_battery` (1 shot: s007)
- **DONE** (illustrator, 2026-11-16): `assets/library/aa_battery.json`, preview `assets/previews/049-giant-hornet-slaughter-assets.png`.
- A plain AA battery lying horizontally: copper-orange / black body with a silver positive nub at the right, no
  brand. Anchor centre, **400x100** (so at 1.24 it matches the hornet's length at 0.95).

### `steam_wisps` (4 shots: s099, s101, s110, s111)
- **DONE** (illustrator, 2026-11-16): `assets/library/steam_wisps.json`, preview `assets/previews/049-giant-hornet-slaughter-assets.png`.
- Three soft white wavy steam ribbons rising, pale blue-grey outline (family of the `hot_tub` steam). Transparent
  between ribbons. Anchor centre, about 240x300.
