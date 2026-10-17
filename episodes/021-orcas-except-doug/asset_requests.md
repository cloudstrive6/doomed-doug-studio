# 021-orcas-except-doug: asset requests (director to illustrator)

Library assets I reuse as they are: `orca`, `orca_bent_fin` (Port/Starboard), `salmon`, `seal_costume` (the 008 suit, same
costume), `shark_costume` (the 008 suit, same costume), `dolphin`, `porpoise` (stands in for Dall's porpoise), `moose`,
`great_white_shark`, `blue_whale`, `cape_fur_seal` (sea lion icon), `canoe`, `fishing_boat`, `sailboat_no_rudder` + `rudder`
(008 callback), `field_guide`, `field_guide_open`, `bathroom_scale`, `balance_scale`, `bowling_ball`, `small_car`, `front_door`,
`bc_map`, `north_america_map` (also zoomed inside `tile` frames for Farallon, Unimak and Monterey), `south_africa_map`,
`australia_map`, `world_map`, `water_splash`, `water_splash_small`, `doug_cap`, `scientist`, `scientist_woman`, `clipboard`,
`journal_paper`, `library_book`, `calendar`, `clock`, `kitchen_timer`, `compact_camera`, `binoculars`, `loudspeaker`,
`magnifying_glass`, `water_plants_bunch`, `house`, `pencil`, `small_fish`, `clam`, the flat costumes from earlier episodes
(outro), and the annotation set.

THE MENU card is drawn from primitives in the shotlist (no asset needed).

House rules for everything below: detailed cartoon tier, thick black outline, flat fills with soft interior shading. **No blood,
no wounds, no teeth marks with red, no carcasses.** Orcas must look powerful, never cute: hard small eye, no smile curve, no
babies drawn as babies. Costumes are props worn over Doug: anchor = Doug's hips at Doug scale 1, listed after Doug at the same
x/y/scale, and Doug's head, face and red cap stay fully visible. Each costume should work on `stand`, `float`, `wave` and the
`swim1`/`swim2` loop unless noted.

## Creatures

### orca_fin
- What: the top of a surfacing orca: tall black dorsal fin plus a short strip of black back, sitting on the waterline.
- Look: jet black `#111`-ish with a mid-grey highlight edge so it reads on dark water; tall, straight, slightly back-swept
  male fin; a white ripple ring at its base. Not grey (that is `shark_fin`).
- Facing: right (the fin's trailing edge on the left). Size: ~220 wide x 300 tall. Anchor: bottom-centre on the waterline (y=0).
- Shots (29): s003, s027-s029, s049-s050, s059, s075-s076, s103, s124, s130, s132, s137-s140, s167, s172, s202-s203, s205-s206,
  s213-s214, s232, s255-s256, s258. Used tiny (0.12-0.2) as map icons and up to 0.8, so keep the shape bold.

### orca_female
- What: adult female orca (mother, "females leading", Moctezuma's companion).
- Look: identical to `orca` but the dorsal fin is shorter (about half the height) and curved back (falcate). Same black/white
  pattern, grey saddle patch.
- Facing: right. Size/anchor: same bbox and anchor as `orca` (x -460..445, centre anchor) so they swap 1:1.
- Shots: s196, s231, s239-s240, s242-s243.

### harbor_seal
- What: harbor seal (the Bigg's orcas' main prey; also the Doug-sized scale gag).
- Look: plump spotted seal, grey-silver with many small dark spots and rings, pale belly, round dog-like head with a short
  muzzle, big dark eyes, whiskers, no ear flaps, short front flippers, hind flippers together at the back.
- Facing: right. Size: ~420 x 170. Anchor: centre. Reads both lying on a rock and swimming.
- Shots (19): s012-s015, s044-s045, s054-s063, s072, s095, s105.

### sea_otter
- What: sea otter floating on its back (item 2).
- Look: dark brown body, pale cream-grey head and face, small round ears, whiskers, small paws holding a grey stone on its
  chest, hind feet poking up at the tail end, short flat tail. Floating on its back, head to the right, looking content.
- Facing: head right. Size: ~420 x 160. Anchor: centre; the bottom (its back) at about y +45 so it sits on a waterline placed
  just under the anchor.
- Shots (15): s031-s039, s042, s045-s047, s051, s095. Also used tiny (0.13) as map icons.

### pacific_white_sided_dolphin
- What: Pacific white-sided dolphin.
- Look: sleek, short beak, dark grey back, light grey flank patch, white belly, and the pale grey "suspender" stripes curving
  along the flank; bicoloured dorsal fin (dark front, pale back).
- Facing: right. Size: ~600 x 220. Anchor: centre (same footprint as `dolphin`).
- Shots: s083-s085, s094-s095.

### short_tail_stingray
- What: short-tail stingray, one of the largest stingrays (item 5).
- Look: huge flat diamond-round disc seen from slightly above, dark grey-brown back, paler rim, small eyes and spiracles near
  the front, short thick tail with a visible barbed spine (serrated, pale) about half-way along it.
- Facing: head right, tail pointing left. Size: disc ~600 wide x 320 deep, tail to x -520. Anchor: disc centre. Barb at about
  (-380, 0) (I point arrows and a warning triangle at it in s111).
- Shots (11): s101-s102, s104, s107-s111, s115, s118, s121.

### deer
- What: Sitka black-tailed deer (two of them huddled on a rock in s137).
- Look: brown-grey coat, pale throat, big ears, black tail top, slim legs, no antlers.
- Facing: right. Size: ~300 x 300. Anchor: bottom-centre (hooves at y=0).
- Shots: s137.

### whale_shark
- What: whale shark, the biggest fish (item 9).
- Look: long broad body, dark blue-grey with white spots and pale checkerboard lines, white belly, very wide flat mouth at the
  very front, small eye, ridges along the back, tall crescent tail, big first dorsal fin. Calm.
- Facing: right. Size: ~1000 x 300. Anchor: centre.
- Shots (11): s182-s187, s191-s193, s198, s201.

### gray_whale
- What: gray whale (mother; also scaled down for the calf and for map icons).
- Look: mottled slate grey with white/pale barnacle and scar patches, no dorsal fin but a row of small knuckles on the back
  near the tail, slightly arched narrow head, short paddle flippers, flukes at the left.
- Facing: right. Size: ~900 x 260. Anchor: centre. Also used with `silhouette: true` (glow off) in s206 as the herded
  "baleen whale".
- Shots (16): s095, s161-s164, s166, s168-s173, s177-s179, s206.

### humpback_whale
- What: humpback whale (the strangers who break up attacks).
- Look: dark grey-black back with knobbly bumps on the head, very long white pectoral flippers (the key feature, keep them
  big), small hump-backed dorsal fin, pale throat grooves.
- Facing: right. Size: ~900 x 320 (flippers included). Anchor: centre. Used down to 0.08 as icons.
- Shots: s171, s173-s175, s178, s180.

### orca_skeleton
- What: Old Tom's skeleton as displayed in the Eden Killer Whale Museum.
- Look: off-white orca skeleton mounted on a low dark wooden plinth with two steel posts: big skull with a row of conical
  teeth (a few with worn grooves, drawn as small notches, no colour), long spine, flipper bones. Clean museum bone, nothing else.
- Facing: right. Size: ~900 x 380. Anchor: bottom-centre (plinth on the floor).
- Shots: s216, s223.

## Costumes (worn over Doug, anchor = Doug's hips)

### salmon_costume
- Homemade Chinook costume: silver felt body suit with a pink stripe, dark blue-green spotted back panel, white belly, a hooked
  "kype" snout hood framing the face from above, a forked felt tail behind the legs, small fin mitts. Played straight.
- Poses: float, wave, stand. Shots: s026-s028 (and in the outro lineup via the existing flats only).

### sea_otter_costume
- Brown furry onesie with a cream face-ring hood (small round ears on the hood), tail flap, paw mitts. Used on the alive
  `on_back` Doug the 003 way (`rotate: -90` at Doug's x + 18, same y/scale), so check it lines up with `on_back` at scale 0.6.
- Shots: s048-s049.

### otter_rock
- Small flat grey stone (~130 x 60) with a flat top where `doug_cap` sits (cap at about (0, -38) x scale). Anchor centre.
- Shots: s048-s050 (on Doug's chest, then floating alone with the cap on it: the death image for 172).

### dolphin_costume
- Grey felt dolphin suit: curved dorsal fin rising behind the head (clear of the cap), beak hood above the face, pale belly
  panel, flipper mitts, flukes behind the legs. Poses: swim1/swim2, float. Shots: s097-s098.

### stingray_costume
- A big flat brown felt ray disc with a pale rim and a limp felt tail with a stitched spine, worn like a blanket over an
  **`on_back`** Doug (no rotate): it covers the torso and legs, leaving the head, eyes and cap clear on the left. Anchor = Doug's
  hips on the `on_back` pose. Shots: s119 (I add sand spray on top of it).

### moose_costume
- Brown felt moose suit with a hood carrying two broad pale palmate antlers that rise to both sides of the cap (cap stays
  visible between them), a dangling felt dewlap under the chin, hoof mitts. Pose: stand (swimming upright at the waterline,
  chin up). Shots: s139.

### moose_costume_flat
- The moose hood's antlers floating alone on the water (empty, slightly tilted), with the deflated brown suit sagging just
  under the waterline. A clear gap between the antlers at about (0, -20) for `doug_cap`. Anchor = waterline centre. Shots: s140.
  Also the Short #2 end-card silhouette, so the antler outline must read on its own.

### shark_costume_flat
- The 008 `shark_costume`, empty-looking and upside down: grey felt suit lying belly-up with the felt dorsal fin pointing down,
  drawn horizontally to sit over an **`on_back`** Doug at the same x/y/scale (no rotate), head, X eyes and cap clear on the
  left. Shots: s159-s160 (in s160 it drifts alone with `doug_cap` beside it).

### whale_shark_costume
- Polka-dot whale shark suit: dark blue-grey felt with white spots, a wide open-mouth hood framing Doug's face (his mouth open
  too), tall crescent tail behind the legs, dorsal fin behind the head. Poses: swim1/swim2. Shots: s199.

### whale_shark_costume_flat
- The same suit rolled belly-up (white belly on top, spots underneath), horizontal, sitting over an **`on_back`** Doug (no
  rotate), head/X eyes/cap clear. Shots: s200.

### gray_whale_calf_costume
- Mottled grey felt whale suit with pale barnacle patches, a blunt whale-head hood above the face, flipper mitts, flukes
  behind the legs. Pose: float. Shots: s177-s179.

### blue_whale_costume
- An enormous homemade blue whale suit, Doug fully inside and invisible: slate-blue felt with pale mottling, throat grooves,
  zip seam, small dorsal fin far back, flukes at the left; a round blowhole opening on top of the head at **(+300, -200)**
  where `doug_cap` pokes out (I place the cap there). Facing right. Size ~1400 x 420. Anchor centre. Shots: s244-s245.

## Props and people

### surfboard / surfboard_bitten
- `surfboard`: plain white-and-red stripe surfboard, side view, ~560 x 60, top surface at y -14, anchor centre.
- `surfboard_bitten`: the same board with a neat curved half-moon notch missing from the right end (clean cartoon outline,
  no tooth marks, no red). Shots: s073-s074 / s075-s076.

### whaleboat
- 1900s wooden open whaleboat, side view facing right: brown planks, pale gunwale, pointed both ends, two oars resting, a coil
  of rope at the bow with the rope end at the bow tip (+340, -40). Size ~700 x 200. Anchor = waterline centre; Doug's feet
  stand on a floor at y -60 (sitting Doug's seat at y -60 too). **No harpoon, no whaling gear beyond rope and oars.**
- Shots (10): s202-s203, s208, s210, s214, s217-s219, s221-s222.

### rowboat
- Doug's tiny wooden rowboat (the thumbnail boat; graphic designer may reuse it): short pale-wood hull, one seat, two oars.
  Facing right. Size ~420 x 120. Anchor = waterline centre; seat top at y -40. Shots: s247-s250, s254, s258.

### whaler / whaler_old
- Crude-tier stick men (Doug's tier, `auto_ink`, no red cap): 1900s shore whaler with a flat cap, waistcoat, rolled
  sleeves and a dark beard; `whaler_old` the same with a grey beard and slight stoop. Anchor hips, facing right.
- Shots: whaler s205, s207, s214-s215, s218-s219; whaler_old s215.

### wildlife_official
- Crude-tier stick-man spokesman (no red cap): peaked official cap, mustache, khaki shirt with a badge. Anchor hips, facing right.
- Shots: s135-s136.

## Maps (world_map style: flat green land, dark outline, light-blue sea, black frame, no labels)

### aleutian_map
- The Aleutian chain and the Alaska Peninsula, about 1400 x 600, anchor centre. The chain runs as a line of islands from
  lower-left (-650, 80) to upper-right (600, -60), with mainland Alaska filling the top-right corner. Adak Island at about
  (-250, 40), Unimak at about (450, -40). Shots: s036-s037, s052 (I place otter icons along the chain at roughly
  (-510, 60), (-290, 30), (-70, 0), (150, -30), (370, -60) x 0.9 from the centre).

### se_alaska_map
- Southeast Alaska: islands and narrow channels, about 1300 x 800, anchor centre; **Icy Strait runs left-right through the
  centre (0, 0)**. Shots: s128, s131-s133 (ring, moose icons and fins are placed around the centre).

### gulf_of_california_map
- Baja California on the left, mainland Mexico on the right, the Gulf of California between them, about 1100 x 900, anchor
  centre; **the southern Gulf at about (60, 150)**. Shots: s188-s189, s197.

### eden_bay_map
- Old sepia-style map of the far south coast of New South Wales: cream/yellowed paper `#efe2b8`, brown ink coast, hatched sea,
  a compass rose; Twofold Bay as a clear bite in the coast at **(120, 40)**, the Kiah River mouth just south of it at
  (100, 90). About 1100 x 800, anchor centre. Shots: s204-s205, s234 (small inset).
