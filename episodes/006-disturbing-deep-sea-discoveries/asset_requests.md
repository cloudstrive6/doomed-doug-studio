# Asset requests: 006 Disturbing Deep Sea Discoveries

From the director, for the illustrator (the art director approves). House style follows `assets/library/anglerfish.json`
and `channel/art_bible.md`:
- Creatures, places and props are drawn in the detailed tier: outlines 4-6, flat fills plus `spray` shading, darker back and
  lighter belly, white eyes with black pupils. Everything faces **right** unless stated otherwise. Local coordinates are
  centred on the anchor.
- **Anchors and sizes matter.** I laid out all 278 shots with placeholder boxes at exactly the sizes and anchors below and
  checked the contact sheets. `bc` = anchor at the bottom-centre (the lowest point sits on y=0, so the drawing spans y -h..0).
  `c` = anchor at the centre. Sizes are local units at scale 1, given as width x height.
- **Most of this episode is dark** (navy `#0b2447`, abyss `#050a1f`, hadal `#020308`). Deep-sea things need mid-tone fills and
  a light rim/glint so the silhouette reads on near-black. Keep black outlines (the scenes are not auto-inked for creatures).
- **Tone:** deadpan documentary for adults. No cute faces on animals, no smiles, no pastel nursery colours. No gore.
- SIL = also used with `"silhouette": true`, so the outer outline must be clean and recognisable as a silhouette.
- Priority: A = hero or recurring (8+ shots), B = supporting, C = one-off.

Reused from the library (no work needed): `snorkel_gear`, `canoe`, `shark` (silky shark), `fishing_boat`, `baited_camera_lander`,
`satellite`, `school_bus`, `heart_icon`, `diver`, `scientist`, `bed`, `phone`, `calendar`, `world_map`, `usa_map`, `volcano`,
`rotten_egg`, `empire_state_building`, `small_fish`, `submersible`, `rov`, `magnifying_glass`, `clock`, `giant_squid` (SIL, the
Bloop "monster"), `freshwater_snail`, `crab`, `hot_tub`, `head_towel`, `doug_cap`, `test_tube_rack`, `petri_dish`, `podium`,
`dinner_plate`, `small_plant`, `gravestone`, `plastic_bag` (001 callback), `small_car`, `mount_everest`, and the annotation set.

---

## Shared

### pacific_map (A)
- **DONE** (illustrator): `assets/library/pacific_map.json`, preview `assets/previews/006-disturbing-deep-sea-discoveries-assets-a.png`. Exact projection from the request; land re-projected from `world_map`, plus Aleutian, Solomon, Vanuatu, Fiji, Samoa, Tonga and Micronesia dots.
- **What:** the same MS Paint map style as `world_map` (flat green land, dark outline, light-blue ocean, black frame, no labels)
  but **centred on 180° longitude** so the whole Pacific is in one piece: East Asia, Japan, the Philippines, Indonesia and
  Australia/New Zealand on the left, the Americas on the right, Alaska and the Aleutians at the top, Antarctica as a white strip
  along the bottom. Include Hawaii (small dots) and the Mariana / Solomon island dots.
- **Projection (important, I place pins with it):** exactly 1600x800, equirectangular, `c` anchor at lon 180 / lat 0:
  `x = ((lon mod 360) - 180) / 180 * 800`, `y = -lat / 90 * 400` (the same scale as `world_map`, just shifted 180°).
- **Shots:** s094, s095, s106, s111, s142, s154, s208, s226, s227, s250, s253 (always at 960,560 scale 1.0).

### microbe (B)
- **DONE** (illustrator): `assets/library/microbe.json`, preview `assets/previews/006-disturbing-deep-sea-discoveries-assets-b.png`.
- **What:** a tiny cartoon bacterium: pale lime-green `#9be07a` rounded rod with a darker outline, a few inner dots and one
  short wiggly tail. **No face.** Mid-tone so it reads on dark rock and on cream.
- **Size/anchor:** 90x50, `c`. **Shots:** s018, s083, s086, s088, s157, s199, s200, s201, s261, s263 (scale 0.4-1.0).

### tubeworm_cluster (A)
- **DONE** (illustrator): `assets/library/tubeworm_cluster.json`, preview `assets/previews/006-disturbing-deep-sea-discoveries-assets-b.png`. Tallest plume tip at about y=-316.
- **What:** a clump of about 8 thin chemosynthetic tubeworms of different heights: off-white/cream tubes with faint ring lines,
  each topped with a small red `#d6332a` feathery plume, rooted in a little dark rubble base. Must read on near-black (cream
  tubes do the work). Not the giant Riftia; thinner trench worms.
- **Size/anchor:** 300x320, `bc`. Also used with `"silhouette": true` (s251), so keep the outer outline clean (SIL).
- **Shots:** s195, s197, s201, s205, s206, s246, s251, s252, s255-s278 (the whole trench + LIVE feed ending).

### clam (A)
- **DONE** (illustrator): `assets/library/clam.json`, preview `assets/previews/006-disturbing-deep-sea-discoveries-assets-b.png`. Opening (dark gap with a sliver of red flesh) faces right.
- **What:** an elongated pale vesicomyid clam, slightly open: off-white `#e9e4d6` shell with growth lines, a dark gap showing
  between the valves, lying on its side. Mid-grey shadow underneath.
- **Size/anchor:** 170x90, `bc`. **Shots:** s195, s197, s201, s246, s252, s257, s260-s278.

### clam_with_cap (B)
- **DONE** (illustrator): `assets/library/clam_with_cap.json`, preview `assets/previews/006-disturbing-deep-sea-discoveries-assets-b.png`. The clam covers x -92..+96, and the red dome sticks out of the right end to about x +125, so the drawing is about 225 wide. The brim is pinched in the seam.
- **What:** the same clam **closed**, with Doug's red cap clamped in it: the brim and part of the red dome `#e0201b` (5px
  outline, like `doug_cap`) sticking out of the shut valves. This is the closing image of the episode.
- **Size/anchor:** 190x100, `bc`, slightly bigger than `clam` so it fully covers an open clam + cap drawn underneath.
- **Shots:** s275-s278.

### fingertip (B)
- **DONE** (illustrator): `assets/library/fingertip.json`, preview `assets/previews/006-disturbing-deep-sea-discoveries-assets-a.png`. Nail top flat at y=-560, x -150..+150; finger is 460 wide.
- **What:** a big cartoon human index finger pointing straight up, seen from the back so the **fingernail faces the viewer**
  and its top edge is a flat platform. Skin `#f2c9a5` with a darker `#d9a27f` side shade, pale pink nail with a white tip, a
  couple of knuckle crease lines at the bottom, cut off flat at the bottom edge.
- **Size/anchor:** 500x800, `bc`. **The nail's flat top must sit at y = -560**, spanning x -150..+150: tiny figures and a car stand on it.
- **Shots:** s149 (Doug and a scientist standing on the nail, "two grown men on every fingernail"), s259 (a `small_car` on
  the nail, the same composition as a visual callback). Cream background `#f4ecd8`.

### seabed_mining_vehicle (B, SIL)
- **DONE** (illustrator): `assets/library/seabed_mining_vehicle.json`, preview `assets/previews/006-disturbing-deep-sea-discoveries-assets-a.png`. Hose ends at the top-left corner (-350,-320).
- **What:** a deep-sea mining collector: low tracked vehicle, yellow-orange `#e3a21a` body with dark grey tracks, a wide
  front intake/collector head at the right, two headlights, a black umbilical hose rising from the top-left. Neutral industrial
  look, no logos.
- **Size/anchor:** 700x320, `bc`. Also SIL (s174: black silhouette threat reveal before the colour version in s175).
- **Shots:** s174, s175, s179, s230.

---

## 1. The Sharkcano

### kavachi_volcano (A)
- **DONE** (illustrator): `assets/library/kavachi_volcano.json`, preview `assets/previews/006-disturbing-deep-sea-discoveries-assets-a.png`. Rim tops at (+-160..174, -558), bowl bottom at y=-472.
- **What:** an underwater volcano cross-section as a broad cone of grey-brown rock `#7a6a58` (lit left flank, shaded right flank
  `#5e5045`, a few rock texture strokes), with an **open crater at the summit**: the rim top at y=-560 at about x ±170, the bowl
  dipping to about y=-470. Faint yellow-brown sulfur stains around the crater. **No lava streams** (it sits underwater).
- **Size/anchor:** 1100x560, `bc`. **Shots:** s005, s007-s013 (scale 1.2 at (960,1080), summit ~y 408), s008 (scale 1.6),
  s022-s025 (scale 1.6, only the summit visible at the bottom).

### hammerhead_shark (A, SIL)
- **DONE** (illustrator): `assets/library/hammerhead_shark.json`, preview `assets/previews/006-disturbing-deep-sea-discoveries-assets-b.png`. Cephalofoil drawn as a slanted bar at x +215..+290.
- **What:** scalloped hammerhead, side/three-quarter view so the **hammer head** reads: wide T-shaped cephalofoil with an eye at
  each tip, bronze-grey back `#8a8f96`, white belly, tall first dorsal, crescent tail. No grin.
- **Size/anchor:** 620x260, `c`. SIL in s014 (`glow_r` 440). **Shots:** s014-s019, s022-s025 (flipped to face left in some).

### sixgill_stingray (B)
- **DONE** (illustrator): `assets/library/sixgill_stingray.json`, preview `assets/previews/006-disturbing-deep-sea-discoveries-assets-b.png`. Includes the long translucent snout that Hexatrygon really has.
- **What:** a sixgill stingray seen from slightly above: a flat rounded-diamond disc in mottled brown-grey `#7d6e5e`, paler edge,
  small eyes on top, long whip tail to the left.
- **Size/anchor:** 440x200, `c`. **Shots:** s015, s016, s017, s019.

## 2. The Underwater Crop Circles

### puffer_sand_circle (A)
- **DONE** (illustrator): `assets/library/puffer_sand_circle.json`, preview `assets/previews/006-disturbing-deep-sea-discoveries-assets-a.png`. The outer outline is black, so `ink` greys it for the old nest.
- **What:** top-down view of the pufferfish "crop circle" nest: a perfect round structure in pale sand `#e8c07a`, about 24 sharp
  radial ridges (lighter) and valleys (darker `#c99a52`) running out from the centre like wheel spokes, a soft ring of fine pale
  sand in the middle, a few tiny shell bits on the ridge tops. It must read as a perfect geometric circle at small sizes.
- **Size/anchor:** 700 diameter, `c` (I used a 700x700 box). **Shots:** s028-s030, s035-s037, s039, s040, s042-s047. In s043
  one copy is drawn with `"ink": "#9a8a6a"` (the old, abandoned nest).

### lopsided_sand_circle (B)
- **DONE** (illustrator): `assets/library/lopsided_sand_circle.json`, preview `assets/previews/006-disturbing-deep-sea-discoveries-assets-a.png`. The square side has a straight edge at x=+200 with 90-degree corners at y=+-166.
- **What:** Doug's attempt, same top-down sand style: a wonky circle with only 6-8 uneven ridges, the left half roughly round,
  the right side **clearly a square corner** (two straight edges at 90°). Scrappy and obviously human-made.
- **Size/anchor:** 420x360, `c`. **Shots:** s045, s046, s047 (an arrow points at the square side at about x +150).

### pufferfish (A, SIL)
- **DONE** (illustrator): `assets/library/pufferfish.json`, preview `assets/previews/006-disturbing-deep-sea-discoveries-assets-b.png`.
- **What:** the white-spotted pufferfish (Torquigener albomaculosus), side view, **not inflated**: small slim puffer, pale
  brownish-grey back with white spots, white belly, big round eye, small beak mouth, small fins. Neutral expression.
- **Size/anchor:** 300x170, `c`. SIL in s032. **Shots:** s032-s039, s041-s043, s046, s047 (also flipped for females).

### alien_head (C, SIL only)
- **DONE** (illustrator): `assets/library/alien_head.json`, preview `assets/previews/006-disturbing-deep-sea-discoveries-assets-b.png`. The silhouette is a light-bulb cranium on a thin neck.
- **What:** a classic grey alien head (big skull, large black almond eyes, small chin). Only ever shown as a black silhouette
  with no glow, so the outline matters most.
- **Size/anchor:** 220x280, `c`. **Shots:** s038 (crossed out with a red X), s213.

## 3. The Bottomless Blue Hole

### ctd_instrument (B)
- **DONE** (illustrator): `assets/library/ctd_instrument.json`, preview `assets/previews/006-disturbing-deep-sea-discoveries-assets-b.png`. Lifting eye at (0,-124), top of the ring at about y=-132.
- **What:** an oceanographic CTD profiler on a cable: a short grey metal frame cage `#c9ccd2` around a white sensor cylinder,
  two small sensor nozzles at the bottom, a lifting eye at the top centre at about (0,-130) where I attach the cable line.
- **Size/anchor:** 160x260, `c`. **Shots:** s059-s063, s065 (light parts so it reads on dark blue water).

## 4. The Lost City

### lost_city_chimney (A)
- **What:** a Lost City carbonate tower: a tall knobbly **white/cream** spire `#f2efe6` with irregular flanges (little ledges)
  sticking out of its sides, grey-cream shading `#cfc8b5` on the right, a few small feathery white tips at the top. Ghostly and
  pale so it glows against twilight navy `#1b4f86`.
- **Size/anchor:** 200x900, `bc`. Used at many scales (0.15-0.8) for the whole field; "Poseidon" is the same drawing at 0.6-0.8.
- **Shots:** s072, s074, s076-s085, s088-s092 (s091/s092: a small copy rotated 40-80° is the snapped-off top).
- **DONE** (illustrator): `assets/library/lost_city_chimney.json`, preview `assets/previews/006-assets-s4-8-tall.png`. Spire x ±75 at the base, feathery tips reach y≈-900; flanges stick out to about ±110.

### apartment_block (C)
- **What:** a plain 20-storey concrete apartment block: flat roof, light grey `#a8a8a8` walls, 20 rows of small blue windows,
  door at the bottom.
- **Size/anchor:** 260x900, `bc` (same height as the chimney so they compare 1:1). **Shots:** s080.
- **DONE** (illustrator): `assets/library/apartment_block.json`, preview `assets/previews/006-assets-s4-8-tall.png`. Roof slab at y=-900 (small roof vent box to -930).

## 5. The Bloop

### blue_whale (C)
- **What:** blue whale side view: very long slate-blue `#5d7a99` body with paler mottling, tiny dorsal fin far back, throat
  grooves under the head, small eye, flukes at the left. Calm, not cute.
- **Size/anchor:** 900x230, `c`. **Shots:** s099 (scale 0.6), s100 (scale 1.4).
- **DONE** (illustrator): `assets/library/blue_whale.json`, preview `assets/previews/006-assets-s4-8.png`.

### iceberg (A)
- **What:** an Antarctic tabular iceberg in cross-section: above the waterline a **flat-topped** white-blue slab
  (`#dff4ff`, white highlights, pale blue shadow), below the waterline a bigger submerged part drawn paler and bluer.
- **Size/anchor:** 700 wide x 780 tall. **Anchor = the waterline centre (0,0)**: the flat top is at y=-260 spanning x -260..+260
  (Doug sits/stands on it), the underwater part goes down to y=+520.
- **Shots:** s103-s106, s113-s116 (in s105/s115 a second, smaller copy is rotated 14-25° as the broken-off slab; I draw the crack
  as a black line on top).
- **DONE** (illustrator): `assets/library/iceberg.json`, preview `assets/previews/006-assets-s4-8.png`. Flat top exactly y=-260, x -260..+260; waterline width ±292; submerged part ±350, down to +520.

## 6. The Jacuzzi of Despair

### brine_pool (A)
- **What:** the "Jacuzzi of Despair" brine pool in a low 3/4 view: an elliptical lake on the seafloor with a **dark mirror-like
  surface** `#3b4a63`, white glints and a faint shimmer line along the far shore, a raised lip of sediment, and a **ring of dark
  blue-black mussels** with light highlights around the rim. A few tiny bubble streams at the edge.
- **Size/anchor:** 760x200, `c` = centre of the pool surface. Used at scale 1.2 at (960,860) on navy `#0b2447`; props float on it
  at about y=838. **Shots:** s117, s119-s125, s128-s139.
- **DONE** (illustrator): `assets/library/brine_pool.json`, preview `assets/previews/006-assets-s4-8.png`. Pool surface ellipse rx 318 / ry 58 around (0,0); sediment lip + mussel ring to ±380 x ±100.

### double_decker_bus (C)
- **What:** a red London-style double-decker bus, side view facing right, two rows of windows, black wheels.
- **Size/anchor:** 520x360, `bc`. **Shots:** s127 (standing in the pool cross-section, roof level with the brine surface).
- **DONE** (illustrator): `assets/library/double_decker_bus.json`, preview `assets/previews/006-assets-s4-8.png`. Roof at y=-356.

## 7. The Champagne Vent

### champagne_glass (B)
- **What:** a champagne flute: clear pale glass with a white outline-glint, gold liquid `#f3e6a0` in the bowl with tiny
  bubbles, thin stem and round foot.
- **Size/anchor:** 70x200, `c` (Doug's hand grip at the stem). **Shots:** s145, s146, s158-s161 (rotated 80° when dropped in s161).
- **DONE** (illustrator): `assets/library/champagne_glass.json`, preview `assets/previews/006-assets-s4-8.png`. Liquid line at y=-72; stem y +12..+84 (grip about (0,+40)); foot at y=+90.

## 8. The Scaly-Foot Snail

### scaly_foot_snail (A)
- **What:** the scaly-foot snail, side view: a **dark metallic iron shell** `#3a3d44` with grey/silver highlights and a low coil,
  and a big foot covered in **overlapping black scales like chain mail** along its side; soft reddish-orange snout with two short
  tentacles. Must read on navy (silver highlights).
- **Size/anchor:** 460x300, `c`. **Shots:** s163, s165, s167-s175, s178-s183 (s165/s167 at scale 1.5: the scales are the hero detail).
- **DONE** (illustrator): `assets/library/scaly_foot_snail.json`, preview `assets/previews/006-assets-s4-8.png`. Reads on navy; scales are five staggered rows on the foot side.

### black_smoker (A)
- **What:** a hydrothermal black-smoker chimney: rugged dark grey-black column `#3a3632` with orange-brown mineral crust
  patches and grey highlights so it reads on navy, slightly wider at the base, billowing **black-grey smoke plume** from the top
  (drawn with grey shading so it shows on the dark background).
- **Size/anchor:** 300 wide x 1000 tall incl. plume (chimney ~700, plume ~300), `bc`.
- **Shots:** s073, s074 (with a red X), s163, s171-s173, s178-s182.
- **DONE** (illustrator): `assets/library/black_smoker.json`, preview `assets/previews/006-assets-s4-8-tall.png`. Vent mouth at y=-700, plume to y≈-1000.

### saucepan_armor (B)
- **What:** a worn prop (art bible: props worn over Doug): a steel-grey saucepan `#b8bcc4` taped flat to Doug's chest, base
  facing out, handle sticking out to the left/back, two strips of silver duct tape in an X. Leave the head, face and cap clear.
- **Size/anchor:** about 220x200; **anchor = Doug's hips at Doug scale 1** (pan disc centred about (0,-90) on the torso).
  Also drawn loose, `rotate: 90`, lying on the vent floor (s182, s183). **Shots:** s180-s183 (Doug pose `cower`, scale 0.6).
- **DONE** (illustrator): `assets/library/saucepan_armor.json`, preview `assets/previews/006-assets-s4-8.png`. Drawn for the `cower` pose: pan centred on the lower torso at (9,-22), r 52, so his folded arms, chin and cap stay visible; list it **after** Doug at the same x/y/scale. Loose: `rotate: 90`.

## 9. The Asphalt Volcano

### asphalt_mound (A)
- **DONE** (illustrator): `assets/library/asphalt_mound.json`, preview `assets/previews/006-s9-12-assets-a.png`, dark-bg check `assets/previews/006-s9-12-dark.png`
- **What:** the Chapopote asphalt volcano: a broad low mound of **glossy black-grey hardened asphalt** `#2d2c33` with ropy,
  wrinkled lava-like flows `#55545e` running down the sides and bright white glints. It must read on abyss `#050a1f`: use the
  lighter wrinkle strokes and glints generously.
- **Size/anchor:** 1200x420, `bc`. **Shots:** s185, s187-s191, s194, s195, s197, s201, s203-s206 (small in the background).

## 10. The Golden Orb

### golden_orb (A)
- **DONE** (illustrator): `assets/library/golden_orb.json`, preview `assets/previews/006-s9-12-assets-a.png`, dark-bg check `assets/previews/006-s9-12-dark.png`
- **What:** the golden orb as found: a smooth shiny **gold dome** `#e8b030` with a bright highlight and a darker underside,
  stuck to rock, with a **torn ragged hole on the right side** showing a dark interior.
- **Size/anchor:** 200x120, `bc` (sits on a rock top). **Shots:** s207, s209-s211, s213, s215, s217-s222 (an arrow points at the
  hole at about x +80).

### sea_sponge (C, SIL only)
- **DONE** (illustrator): `assets/library/sea_sponge.json`, preview `assets/previews/006-s9-12-assets-a.png`, dark-bg check `assets/previews/006-s9-12-dark.png`
- **What:** a vase/tube-shaped deep-sea sponge. Only shown as a black silhouette (no glow).
- **Size/anchor:** 200x260, `bc`. **Shots:** s213.

### giant_anemone (B)
- **DONE** (illustrator): `assets/library/giant_anemone.json`, preview `assets/previews/006-s9-12-assets-b.png`, dark-bg check `assets/previews/006-s9-12-dark.png`
- **What:** Relicanthus, the giant deep-sea anemone: a pale whitish-pink column `#f1d9d2` with very long, thin tentacles spreading
  wide to both sides (the widest point about 540 across), on a broad golden-tan basal disc gripping the rock.
- **Size/anchor:** 560x520, `bc`. **Shots:** s217, s218 (a half-size `golden_orb` sits at its base).

## 11. Dark Oxygen

### manganese_nodule (A)
- **DONE** (illustrator): `assets/library/manganese_nodule.json`, preview `assets/previews/006-s9-12-assets-b.png`, dark-bg check `assets/previews/006-s9-12-dark.png`
- **What:** a polymetallic nodule: a lumpy, cauliflower-knobbly potato-sized rock, dark brown-black `#4a3f36` with lighter
  `#6b5e50` highlights on the bumps. Must read on near-black.
- **Size/anchor:** 140x100, `c`. Scattered as a field of 12 (scale 0.55) and shown as a close-up at scale 2.0.
- **Shots:** s223, s225, s228-s236, s241-s245.

## 12. The Deepest Ecosystem Ever Found

### research_ship (C)
- **DONE** (illustrator): `assets/library/research_ship.json`, preview `assets/previews/006-s9-12-assets-b.png`, dark-bg check `assets/previews/006-s9-12-dark.png`
- **What:** a white oceanographic research vessel at night, side view facing right: white hull with a dark waterline stripe,
  superstructure with **lit yellow windows**, an A-frame crane at the stern (left), a mast with a red light. Reads on a night sky.
- **Size/anchor:** 900x360; **anchor = waterline centre**, so the hull bottom sits about 60 below the anchor.
- **Shots:** s272 (the start of the LIVE-feed ending).
