# Asset requests: 008 Every Step of the Ocean Food Chain

From the director, for the illustrator (the art director approves). House style follows `assets/library/anglerfish.json`
and `channel/art_bible.md`:
- Creatures, places and props are drawn in the **detailed tier**: outlines 4-6, flat fills plus `spray` shading, darker back and
  lighter belly, white eyes with black pupils. Everything faces **right** unless stated otherwise. Local coordinates are
  centred on the anchor.
- **Anchors and sizes matter.** I laid out all 321 shots with outline placeholder boxes at exactly the sizes and anchors below and
  checked the contact sheets (counter zone, caption bar, crops). `bc` = anchor at the bottom-centre (the lowest point sits on y=0,
  so the drawing spans y -h..0). `c` = anchor at the centre. Sizes are local units at scale 1, width x height.
- **Tone (brief risk list):** nature horror for adults. Predators stay at the detailed cartoon tier: no cute faces, no smiles, no
  pastel nursery colours, no big sparkly eyes. No blood, no bite wounds, no carcasses. Doug's costumes are cheap and homemade
  (cardboard, felt, tape), played straight, never mascot-cute.
- SIL = also used with `"silhouette": true`, so the outer outline must be clean and recognisable as a black shape.
- Priority: A = hero or recurring (8+ shots), B = supporting, C = one-off.

**Rig reference for worn costumes** (same as 002/004): anchor (0,0) = **Doug's hips** at Doug scale 1. Head centre (0,-218) r72,
cap top about y=-300, cap brim points right to x=+126, shoulders (0,-122), feet at y=+150 (stand feet at x about +-32). Costumes
must leave the **head, face and red cap fully visible** (art bible), and must read on poses `stand`, `float`, `walk1/2`,
`arms_up`, `panic1/2`, `cower`, `hands_hips`, `wave` (arms move, so do not draw sleeves past the elbows). Scale used in shots:
0.25-0.65.

**Flat costumes** (`*_flat`): the empty costume after the death beat, lying flat (no Doug inside), with the costume's own
drawn/marker eyes crossed out as X eyes, like `squid_costume_flat`. No bite marks, no tears that read as wounds.

Reused from the library (no work needed): `snail_costume`, `squid_costume`, `squid_costume_flat`, `sperm_whale`, `giant_squid`,
`blue_whale`, `shark` (spiny dogfish / blacktip / bull shark stand-in, always labelled), `humboldt_squid`, `small_fish`, `crab`,
`amber_snail`, `dolphin`, `salmon`, `coral_reef`, `aquarium`, `bed`, `small_car`, `school_bus`, `eiffel_tower`, `fishing_boat`,
`rubber_ring`, `doug_cap`, `scientist`, `calendar`, `clock`, `kitchen_timer`, `phone`, `satellite`, `soda_bottle`, `clam`,
`dinner_plate`, `heart_icon`, `dryas_flower` (the "daisy" of the marguerite), `gravestone`, `world_map`, `pacific_map`,
`north_america_map`, and the annotation set (`question_mark`, `exclamation_mark`, `warning_triangle`, `red_x`, `thermometer`).

---

## Engine request (art director, not the illustrator)

### Upright Doug without the cap: `gear: ["cap_off"]` on standing poses
- **Why:** the approved one-off exception in `decisions.md`: in the closing LIVE feed Doug is capless, tiny and far off, waving,
  while an orca wears his cap. Today `doug.py` only honours `cap_off` for `on_back` (and then draws the cap on the ground).
- **Ask:** when `cap_off` is set on a non-flat pose, simply skip `_cap()` (draw nothing on the ground). Head, face and everything
  else unchanged.
- **Shots:** s313, s314 (`stand`), s318, s319 (`wave`), Doug at scale 0.12 inside the monitor. Until this lands those four shots
  render with the cap on, which contradicts the narration, so this blocks art approval of the close.

---

## Item 1: Mantis Shrimp

### mantis_shrimp (A)
- **What:** peacock mantis shrimp (*Odontodactylus scyllarus*), side view facing right, resting.
- **Look:** segmented body in bright green `#3fae5a` with darker green back, orange-red legs and swimmerets, a blue-and-red tail
  fan with a few leopard spots, two stalked eyes on top of the head (each a banded ball), antennae. The two **raptorial clubs
  folded tight under the head** like a closed fist (pale blue-white club, red rim). Detailed tier, no smile, no cute eyes.
- **Size/anchor:** 520x240, `c`. Also used tiny (scale 0.15-0.18) on the food-chain staircase, so keep the silhouette simple.
- **Shots:** s005-s011, s014, s028, s032-s033, s084, s284-s285, s311 (often `flip: true` so it faces left out of its burrow).

### mantis_shrimp_strike (A)
- **What:** the same shrimp mid-strike.
- **Look:** identical body; one club **swung fully forward and down** to about x +330, y +40 (the hitting surface faces right).
  No motion lines (I add them).
- **Size/anchor:** 640x240, `c`, same body position as `mantis_shrimp` so the two swap cleanly.
- **Shots:** s012-s013, s015-s019, s024, s029-s031.

### mantis_arm_spring (B)
- **What:** cutaway diagram of the shrimp's raptorial arm showing the **saddle-shaped spring** (the "catapult").
- **Look:** a pale pink-orange arm segment drawn as a cutaway with a grey dashed outline. Inside it is a curved blue saddle shape
  (like a Pringle seen side-on) with a small latch, and a coiled-spring hint behind it. The club is at the right end. Diagram style
  on a transparent background.
- **Size/anchor:** 640x320, `c`. **Shots:** s026-s027.

### snail_shell_cracked (B)
- **What:** Doug's snail-costume shell after the bubble pops, lying on the sand beside dead Doug.
- **Look:** the honey-amber spiral shell from `snail_costume`, **split cleanly in two halves** with a zigzag crack, the two halves
  slightly apart, a few small shell chips. Cartoon only.
- **Size/anchor:** 300x200, `c`. **Shots:** s032-s033 (Doug is `on_back` beside it).

### highspeed_camera (C)
- **What:** a lab high-speed camera on a tripod.
- **Look:** black boxy camera body with a big lens pointing right, a small red REC light, grey tripod legs.
- **Size/anchor:** 200x340, `bc`. **Shots:** s011, s045.

### speedometer (B)
- **What:** a gauge dial (speedometer / bite-force meter).
- **Look:** a semicircle dial with a thick black rim, white face, tick marks, a green-yellow-red arc, and a red needle **pinned in
  the red zone**. Leave the lower centre (around 0,+60) blank, because I put a label under it.
- **Size/anchor:** 320x220, `c`. **Shots:** s013 (80 km/h), s171, s173 (BITE FORCE).

## Item 2: Giant Moray

### giant_moray (A, SIL)
- **What:** giant moray eel (*Gymnothorax javanicus*), side view facing right.
- **Look:** very long, thick, muscular body tapering to the tail, with a continuous dorsal fin. Pale yellow-brown with **dark
  brown leopard spots** that get denser toward the head. A blunt head with a small eye and the mouth slightly open, showing a
  few needle teeth (no blood). It must read when only the front third pokes out of a rock crack (I draw rock over the body).
- **Size/anchor:** 900x180, `c`; head occupies about x +300..+450. Used with `flip: true` (head left) a lot.
- **Shots:** s034-s036, s038, s040-s041, s045-s047, s049-s051, s054, s058 (SIL, peeking from the crack), s059, s084, s284-s285, s311.

### moray_xray and moray_xray_jaws_forward (B)
- **What:** an X-ray cutaway of the moray's head showing the **second (pharyngeal) jaws** in the throat.
- **Look:** a dark-navy background is not included (transparent). The head outline is drawn in pale cyan `#bff6ff` lines with a
  faint fill, with the skull and main jaw in white. A second, smaller white jaw sits in the throat at about x -120. In
  `moray_xray_jaws_forward` the identical head has the throat jaws shot forward into the mouth at about x +150, with faint
  "ghost" lines where they were. Teeth are simple white points.
- **Size/anchor:** 760x300 each, `c`, identical head geometry so they overlay. **Shots:** s042-s044 (xray), s043 (forward).

### tape_measure (C)
- **What:** an analogy prop, a tape measure snapping back.
- **Look:** a yellow tape-measure case on the left and a metal tape extended to the right with tick marks, plus a curved
  "snap" kink near the case.
- **Size/anchor:** 420x160, `c`. **Shots:** s044.

### roving_coral_grouper (A, SIL)
- **What:** roving coral grouper (*Plectropomus pessuliferus*), the moray's hunting partner.
- **Look:** a long-bodied grouper, **red-orange with small bright blue spots** and a darker back, a big mouth, and a square tail.
  The friendly behaviour comes from the story, not the drawing: it gets a neutral fish face.
- **Size/anchor:** 420x170, `c`. Also rotated 80 degrees (head down) for the "headstand" signal, so keep the anchor central.
- **Shots:** s047 (SIL), s048-s056, s058-s060.

### reef_fish_costume (A) / reef_fish_costume_flat (B)
- **What:** Doug's homemade small-reef-fish costume.
- **Look:** a felt suit in yellow-orange with one dark vertical stripe (echoing `small_fish`), a forked felt tail sticking out
  behind the hips to about (-170,+40), a small dorsal fin on the back of the suit (behind the shoulders, not on the head), and
  a round button eye sewn on the chest. Zipper.
- **Anchor/bbox:** hips, about x -120..+120, y -200..+100. **Shots:** s034-s035, s037-s039, s041-s043, s046-s050, s055-s058.
- **Flat:** 460x170, `c`, the empty suit lying flat with the button eye crossed out. **Shots:** s059-s060.

## Item 3: Giant Pacific Octopus

### giant_pacific_octopus (A)
- **What:** giant Pacific octopus, seen from slightly above, **arms spread wide**.
- **Look:** a deep red-orange `#c8452f` body with a paler mottled underside and white suckers on the arm undersides. The mantle is
  in the upper centre at about (0,-150), with a horizontal-slit eye. Eight arms curl outward, and the **two outer arms reach the
  full width** (tip to tip, for the 5 m dotted line). The beak area is hidden at about (0,+20); I circle it in red. Detailed,
  textured skin, no face beyond the eye.
- **Size/anchor:** 1000x560 (please keep it at or under 620 tall), `c`. **Shots:** s061-s064, s067-s073, s079-s083, s284-s285, s311.

### octopus_arm (B)
- **What:** a single octopus arm, for pouring through the hole, wrapping the jar and grabbing the dogfish.
- **Look:** the same red-orange arm, thick at the left end and tapering to a curled tip at the right, with a row of white
  suckers on the underside.
- **Size/anchor:** 520x200, anchor at the **thick base, left end middle** (x 0..520). **Shots:** s068, s070, s074, s076, s083.

### glass_jar (B) and jar_lid (B)
- **What:** a big glass jar Doug locks himself in, and its screw lid.
- **Look (jar):** **outline only** (no fill, like `ice_block`), so Doug shows through it. A thick pale-blue glass outline with a
  rounded shoulder, a threaded neck at the top (y -480..-440), two white glints and a faint blue tint line at the base.
- **Look (lid):** a grey metal screw lid with ridges on the side, 340 wide.
- **Size/anchor:** jar 360x480 `bc`. Doug at scale 0.55 stands inside with feet 30 above the base. Lid 340x60 `c`, placed on the
  neck at (0,-490) relative to the jar at scale 1.1, and lying on the rocks after the death.
- **Shots:** s074-s078.

### crab_costume (A) / crab_costume_flat (B)
- **What:** Doug's crab costume.
- **Look:** a red-brown cardboard carapace worn like a sandwich board on the torso, with two big felt claws on the sides of the
  suit at hip height (not on the hands), four pairs of floppy felt legs hanging from the sides, and two eye stalks on a headband
  **beside** the cap (not covering it). Tape on the seams.
- **Anchor/bbox:** hips, about x -150..+150, y -200..+80. **Shots:** s061-s069, s071-s073, s075-s076, s084.
- **Flat:** 460x170 `c`, the empty carapace flat with the claws limp and the eye stalks drooping, eyes crossed out.
  **Shots:** s077-s078, s169 (crossed out with a red X: "no costume this time").

### tennis_ball (C)
- Yellow-green tennis ball with the white curved seam, 120 `c`. **Shots:** s070.

### bathroom_scale (B)
- **What:** a flat bathroom scale.
- **Look:** a white/grey square scale in low 3/4 view with a small blank display window at (0,-45) (I put the "80 KG" or "22 KG"
  label there).
- **Size/anchor:** 260x70, `bc`. **Shots:** s069, s088.

## Item 4: Giant Trevally

### giant_trevally (A, SIL)
- **What:** giant trevally (*Caranx ignobilis*).
- **Look:** a deep-bodied, powerful silver fish with a **steep blunt forehead** and a dark grey-silver back, a slightly
  scowling brow line over a gold eye, a sickle tail and dark fin edges. Not cute.
- **Size/anchor:** 620x320, `c`. Rotated -35 to -55 degrees for the leaps, so the anchor must be central.
- **Shots:** s086-s090, s096 (SIL), s098 (SIL), s100-s102, s104-s106, s109-s110, s112, s284-s285, s311.

### sooty_tern (A)
- **What:** sooty tern in flight.
- **Look:** black back and wings, white underside and forehead, a black cap and eye-stripe, a thin black bill, a deeply **forked
  tail**, and long narrow wings spread.
- **Size/anchor:** 320x150, `c`. Used small (0.28-0.5), so keep it bold. **Shots:** s092, s094-s096, s098, s100-s102, s106, s108-s109.

### tern_costume (A)
- **What:** Doug's lumpy, badly made sooty tern costume, with **wings too big**.
- **Look:** a black felt body suit with a white front panel and two **huge stiff black wings** sewn onto the back of the suit,
  sticking out and up to about x +-260, y -320 (they are part of the suit, not attached to his arms). A forked felt tail behind
  the hips, and a long black bill on a headband poking forward **under the cap brim** (face visible). Uneven stitching.
- **Anchor/bbox:** hips, about x -260..+260, y -330..+60. Poses: `stand`, `float`, `panic1/2`, `arms_up`.
- **Shots:** s086-s101, s103-s104, s106-s112.

## Item 5: Goliath Grouper

### goliath_grouper (A, SIL)
- **What:** goliath grouper (*Epinephelus itajara*).
- **Look:** a massive, heavy, rounded fish with a mottled brown-yellow-olive pattern and darker bars, a broad flat head, **tiny
  eyes** and a **huge wide mouth** at the right, slightly open, with small teeth (teeth visible but not scary-sharp). Rounded fins
  and tail.
- **Size/anchor:** 820x440, `c`; the mouth is at about (+400,+20). **Shots:** s113-s116, s119-s122, s124-s127, s131 (SIL),
  s136 (SIL), s284-s285, s311.

### goliath_grouper_full (B)
- **What:** the grouper right after one gulp.
- **Look:** the same fish with **cheeks bulging** and the mouth closed, and the tip of a grey shark tail fin (the shark costume's
  tail, grey felt) sticking out of the mouth corner. No blood.
- **Size/anchor:** 860x460, `c`. **Shots:** s132, s137-s138.

### shark_costume (A)
- **What:** Doug's cheap grey shark costume ("fear me").
- **Look:** a grey felt body suit with a white belly panel and three drawn-on gill lines. A **big triangular dorsal fin rises
  from the back of the suit behind his head** to about (-60,-330). (The stage note says "cap tucked under the fin", but the art
  bible wins: the fin stands behind the head and the cap stays fully visible.) A felt shark tail behind the hips, and a row of
  felt teeth printed across the chest.
- **Anchor/bbox:** hips, about x -160..+160, y -340..+80. Poses: `float`, `hands_hips`.
- **Shots:** s113, s115, s117-s118, s120, s123-s124, s127-s129, s135-s136.

### baby_grand_piano (C)
- Black baby grand piano, side view, lid propped open, with white keys showing. 560x360 `bc`. **Shots:** s116.

### shipwreck (A)
- **What:** a sunken wooden wreck on the sea floor, where the grouper lives.
- **Look:** a broken, tilted wooden hull (brown `#6b4a2e`) half buried in sand, a snapped mast, portholes, and green-brown algae
  patches. It should read as background (mid values, no strong contrast).
- **Size/anchor:** 1000x360, `bc`. **Shots:** s113-s128, s135-s138.

## Item 6: Tiger Shark

### tiger_shark (A, SIL)
- **What:** tiger shark (*Galeocerdo cuvier*).
- **Look:** a big grey-brown shark with **dark vertical tiger stripes** on the back and sides, a very **blunt square snout**,
  a white belly and a long upper tail lobe.
- **Size/anchor:** 820x260, `c`. **Shots:** s139-s142, s144, s148-s150, s153 (SIL), s154, s157, s161-s162 (SIL), s284-s285, s311.

### tiger_shark_xray (B)
- **What:** an X-ray view of a tiger shark with an **empty stomach outline**.
- **Look:** a pale cyan line drawing of the shark outline and a simple cartilage skeleton in white. A large empty oval stomach
  centred at about (+40,+20), about 340x150 (I place the cans, bottle, sacks, squid and fish inside it). Transparent background
  (I use a dark navy panel).
- **Size/anchor:** 900x300, `c`. **Shots:** s158-s160.

### tin_can (C) and burlap_sack (C)
- **tin_can:** a plain empty food can, grey metal with a blank faded label and an open jagged top. 60x90 `c`.
- **burlap_sack:** a crumpled tan burlap sack with a woven texture and a tied neck. 120x140 `c`.
- **Shots:** s158-s160.

### sea_turtle_costume (A) / sea_turtle_costume_flat (B)
- **What:** Doug's sea turtle costume.
- **Look:** a domed green-brown **turtle shell backpack** with hexagonal scute lines on his back (like the snail shell backpack,
  centred at about (-80,-60)), a pale yellow plastron panel on the front of the suit, and two felt flipper mitts at the suit's
  sides at hip height.
- **Anchor/bbox:** hips, about x -170..+130, y -200..+90. Poses: `float`, `wave`.
- **Shots:** s139, s141, s143-s149, s151-s153, s155-s156, s160-s162.
- **Flat:** 460x170 `c`, the empty shell and suit flattened, sinking, with the shell's painted eyes crossed out. **Shots:** s163-s164.

### seagrass (A)
- **What:** a seagrass meadow clump for the sea floor.
- **Look:** long ribbon blades in mid green and olive, swaying, some darker blades behind. Mid values so it stays in the
  background. I tile 5 copies across the floor.
- **Size/anchor:** 600x220, `bc`. **Shots:** s139-s146, s148-s150, s156-s157, s161-s162.

### albatross_chick (B)
- **What:** a Laysan albatross fledgling.
- **Look:** a big fluffy grey-brown chick with patches of white adult feathers coming through, a dark hooked bill and a clumsy
  stance. It also floats on the water (so the bottom of the body is flat).
- **Size/anchor:** 150x170, `bc`. **Shots:** s152-s154.

### australia_map (B)
- **What:** a map of Australia with the south coast of New Guinea, in the `world_map` style (flat green land, dark outline, light
  blue sea `#bfe6ff`, black frame, no labels).
- **Projection (I place pins with it):** equirectangular, lon 110..155 E, lat 6..40 S, **28 px per degree**, 1260x952, `c` anchor
  at lon 132.5 / lat -23: `x = (lon - 132.5) * 28`, `y = -(lat + 23) * 28`. It must include Cape York, the Torres Strait (the gap
  to New Guinea at about lat -10.3), the Kennedy River mouth / Princess Charlotte Bay (144.1, -14.5), Shark Bay's double
  peninsula (113.6, -25.8) and Bremer Bay (119.4, -34.4).
- **Shots:** s147, s178, s183, s186, s291 (always at 960,600 scale 0.75).

## Item 7: Saltwater Crocodile

### saltwater_crocodile (A, SIL)
- **What:** saltwater crocodile (*Crocodylus porosus*), side view facing right, standing low.
- **Look:** a huge, long, heavy olive-grey to dark brown body with lighter yellowish flanks and belly, rows of bony scutes along
  the back and tail, a long broad snout with a few teeth showing along the closed jaw line, and a high eye bump. Legs are low and
  splayed, feet flat on the ground line.
- **Size/anchor:** 1000x230, `bc`. It also swims and surfs (rotated about -10 degrees) and is used small in a row of "relatives".
- **Shots:** s166-s168, s170-s172, s174, s176-s177, s179-s183, s185, s187, s189, s192 (SIL), s193-s194, s284-s285, s311.

### tide_table (C)
- **What:** a small printed tide-table booklet Doug holds.
- **Look:** a white booklet with a blue cover band, a tiny wave icon and two columns of tiny tick lines (no readable text).
- **Size/anchor:** 110x150, `c`. **Shots:** s191-s194.

## Item 8: Polar Bear

### polar_bear (A)
- **What:** a polar bear walking on the ice, side view facing right.
- **Look:** a creamy white `#f4f1e4` coat with pale grey-blue shading underneath (so it reads on white ice: **give it a clear
  dark outline**), a long neck, a small head with a black nose and a small dark eye, and big paws. Not cuddly: a heavy predator
  build.
- **Size/anchor:** 620x380, `bc`. **Shots:** s195-s198, s200, s206-s208, s210, s213-s215, s220, s284-s285, s311.

### polar_bear_lying (B)
- **What:** the bear still-hunting: **lying flat on its belly**, chin on the ice, front paws forward, motionless.
- **Look:** same colours and outline as `polar_bear`. It should read as "a large white shape, very still".
- **Size/anchor:** 660x190, `bc`; the head is at the left end (it lies beside a hole on its left). **Shots:** s202-s205, s217-s218.

### seal_costume (A) / seal_costume_patched (A) / seal_costume_flat (B)
- **What:** Doug's seal costume (polar bear), and the same costume patched up (great white).
- **Look:** a grey `#8a8f96` seal body suit with darker speckles and a pale belly panel, two flipper mitts at the suit sides,
  tail flippers at the feet, and **whiskers**: three short black lines on each side poking out sideways from behind the cheeks,
  not over the face. Zipper. **Patched:** identical, plus 4-5 mismatched fabric patches (one tartan, one bright blue) and silver
  duct-tape crosses. The patched version is also used with Doug in the `fall` pose, rotated -20, for the breach.
- **Anchor/bbox:** hips, about x -130..+130, y -220..+170. Poses: `float`, `stand`, `wave`, `fall`.
- **Shots (seal):** s195, s198-s202, s205-s207, s209, s211-s213, s215-s218. **Shots (patched):** s221, s224-s226, s228-s229,
  s233-s235, s238, s241-s243, s245-s247.
- **Flat:** 460x170 `c`, the empty grey suit lying flat on the ice, eyes crossed out. **Shots:** s219-s220.

### cape_fur_seal (A)
- **What:** a real seal, swimming, side view facing right (it stands in for Cape fur seals, and for ringed/bearded seals in the
  polar shots).
- **Look:** a sleek brown-grey body, a darker back, a pointed snout with whiskers, small ear flaps, and fore-flippers. Not cute:
  small dark eyes.
- **Size/anchor:** 300x130, `c`. It is rotated -80 (head up, breathing at a hole), 80 (headstand) and 180 (flipped onto the ice).
- **Shots:** s197, s200-s201, s205-s206, s227-s233, s239-s240.

### beaufort_map (B)
- **What:** a regional map of the Beaufort Sea north of Alaska, in the `world_map` style (flat green land, dark outline,
  light-blue sea, black frame, no labels).
- **Projection:** lon 165..125 W, lat 66..77 N, `c` anchor at lon -145 / lat 71.5: `x = (lon + 145) * 24`,
  `y = -(lat - 71.5) * 75` (960x825). Draw the Alaska north coast (Point Barrow at about -156.8/71.3) and the Yukon coast
  (about -139/69.5), and show the **pack ice as a white region with a wavy edge north of about lat 73.5**.
- **Shots:** s209, s211-s213 (always at 900,640 scale 0.9).

### finish_banner (C)
- **What:** a tiny marathon finish arch.
- **Look:** two thin poles with a red-and-white checkered banner on top.
- **Size/anchor:** 120x110, `bc`. I place 16 copies along the swim route at scale 0.3. **Shots:** s212.

## Item 9: Great White Shark

### great_white_shark (A, SIL)
- **What:** great white shark (*Carcharodon carcharias*), side view facing right.
- **Look:** a heavy torpedo body, slate-grey back with a **sharp countershading line** to the white belly, a conical snout, a
  black eye, a big triangular dorsal fin and a crescent tail. The mouth is closed with a few teeth visible. No blood.
- **Size/anchor:** 850x320, `c`. It is rotated -45 to -80 for the breaches (head up), so keep the anchor central.
- **Shots:** s221-s223, s227 (SIL), s229-s230 (SIL), s231-s233, s235-s236 (SIL), s237, s239-s240, s246 (SIL), s247, s249-s250,
  s284-s285, s289, s305, s311.

### seal_island (B)
- **What:** Seal Island, False Bay: a low, flat, rocky island crowded with seals.
- **Look:** a low grey-brown granite outcrop with flat top, and 15-20 small brown seal shapes lying on it.
- **Size/anchor:** 900x220, `bc` (bottom = waterline). **Shots:** s227-s228.

### seal_decoy (C)
- **What:** a seal-shaped decoy: a flat grey cut-out of a seal (carpet/rubber), floating, with a tow-rope loop at the nose.
- **Size/anchor:** 260x70, `c`. **Shots:** s244.

### six_story_building (C)
- **What:** a plain six-storey building for the 20 m scale.
- **Look:** a light concrete block with **exactly six rows of windows** and a flat roof.
- **Size/anchor:** 300x600, `bc` (used at scale 1.067 so it is exactly 640 px = 20 m). **Shots:** s230.

### south_africa_map (B)
- **What:** a map of South Africa in the `world_map` style.
- **Projection:** lon 15..34 E, lat 22..36 S, 70 px per degree, 1330x980, `c` at lon 24.5 / lat -29:
  `x = (lon - 24.5) * 70`, `y = -(lat + 29) * 70`. False Bay must be a clear notch (Seal Island at 18.59, -34.14), and Gansbaai
  (19.35, -34.58) just east of it. Lesotho may be a faint inner line.
- **Shots:** s226, s288-s290 (always at 960,610 scale 0.72).

## Item 10: Sperm Whale

### sperm_whale_top (A)
- **What:** a sperm whale seen **from above**, for the marguerite (daisy) defence ring.
- **Look:** the same dark grey as `sperm_whale`, with a long, wide, **blunt box head** (the top third), a narrowing body with
  knuckles along the back, and tail flukes spread at the left end. Small white scar circles on the head.
- **Size/anchor:** 600x170, `c`, head pointing right (I rotate seven copies so the heads meet in the middle and add a calf at
  scale x0.45). **Shots:** s270-s273, s278-s279, s305.

## Item 11: Orca (boss)

### orca (A, SIL)
- **What:** a big male orca, side view facing right.
- **Look:** jet black with crisp white eye patch, white chin/belly, grey saddle patch behind a **very tall straight dorsal fin**
  (male), paddle flippers, and flukes. The mouth is closed. It must look powerful, not plush.
- **Size/anchor:** 900x330, `c`. It is also used at very small scale (0.07) in a 40-icon grid, rotated about +-20 for surfacing,
  and as a silhouette with red glow before the boss card.
- **Shots:** s250-s251, s270 (SIL), s279 (SIL), s281-s285, s292, s297, s299-s301, s303, s305, s308-s309, s314-s319.
- **The cap on the orca:** I place `doug_cap` on the orca's head (x +210 x scale, y -120 x scale). Please keep the top of the
  head at about (+210,-110) so the cap sits on it (s314, s318-s319).

### orca_bent_fin (B)
- **What:** Port and Starboard: the same orca with a **collapsed dorsal fin bent over** to one side.
- **Size/anchor:** 900x300, `c`. **Shots:** s288-s289.

### sailboat (A) / sailboat_no_rudder (A)
- **What:** Doug's tiny sailboat.
- **Look:** a small white single-mast sailing boat in side view facing right, with a short hull (blue stripe), **one triangular
  white sail** on a mast that rises to about y -480, and a ship's **wheel on a post** at about (+60,-150) where Doug stands at
  the helm. Below the stern (left) there is a visible **rudder blade** at about (-250,+20..+120) under the waterline. The
  `_no_rudder` version is identical, with just a broken stub where the rudder was.
- **Anchor/size:** waterline centre (0,0): hull bottom about +110, mast top -480; about 560 wide. Doug (scale 0.5 x boat scale)
  stands at local (-20,-110) with his hips there, and his legs are hidden by the hull (I draw Doug first). He grips the wheel.
- **Shots (sailboat):** s287, s298 (tiny map icon), s300, s302 (rotated 25, sinking), s304, s308.
  **Shots (no rudder):** s301, s309-s310, s312-s314, s318-s319.

### rudder (B)
- **What:** the loose rudder the orcas take.
- **Look:** a white fibreglass blade with a grey stock on top and a snapped edge.
- **Size/anchor:** 90x160, `c`. **Shots:** s301, s303, s309.

### life_jacket (A)
- **What:** an orange life jacket worn over Doug's stick body (worn prop).
- **Look:** a bright orange `#ff7a1a` vest from the shoulders (y -130) to the hips (y -10), with two puffy front panels, black
  straps and a buckle. Arms and legs free.
- **Anchor/bbox:** hips, about x -100..+100, y -140..0. Poses: `stand`, `wave`, `thumbs_up`.
- **Shots:** s287, s299-s301, s304, s308-s314, s318-s319.

### iberia_map (C)
- **What:** a map of Spain and Portugal in the `world_map` style.
- **Projection:** lon 10 W..4 E, lat 35.5..44 N, 80 px per degree, 1120x680, `c` at lon -3 / lat 39.75:
  `x = (lon + 3) * 80`, `y = -(lat - 39.75) * 80`. Include the tip of North Africa and the Strait of Gibraltar.
- **Shots:** s298 (at 960,560 scale 0.85).
