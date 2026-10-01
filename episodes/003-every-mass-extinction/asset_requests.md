# Asset requests: 003 Every Mass Extinction

From the director, for the illustrator (art director approves, and owns `time_machine` and the `sunburn` gear).
House style per `assets/library/anglerfish.json` and `channel/art_bible.md`: creatures, places and props are the
detailed tier (outlines 4-6, flat fills plus `spray` shading, darker back, lighter belly, white eyes with black
pupils), **facing right** unless stated, local coordinates centred on the anchor. Sizes are local units at scale 1.
**Anchors matter.** Every drawing is placed in `shotlist.json` by the anchor described below. I laid the shots out with
placeholder boxes, so a wrong anchor will put things in the sky.

Tone: deadpan nature-documentary cartoon. Prehistoric animals are **not cute**: no big shiny eyes, no smiles, no
pastel palette (the brief flags dinosaurs and a time machine as kid magnets). Deaths stay on Doug's rig (X eyes, `lie`
rotated, ghost); creatures that die get a red X from me, or the one `dunkleosteus_dead` variant. No blood.

Priority: A = hero or recurring, B = supporting, C = one-off prop. SIL = also shown with `"silhouette": true`, so the
outer outline must be a clean, recognisable shape.

Rig reference for worn props (`snorkel_gear`, `head_towel`, `ammonite_costume*`): anchor (0,0) = **Doug's hips** at
Doug scale 1. Head centre (0,-218) r72, cap top about y=-300, cap brim points right to x=+126, shoulders (0,-122),
feet at y=+150 (stand: feet at x about +-32). Props leave the **head, face and red cap fully visible**.

---

## Art director: series lore and engine

### time_machine (A, art director owns the drawing; series lore for the whole `prehistoric` playlist)
- **What:** Doug's time machine. Per the series bible and the creative director: a **crude MS Paint phone booth**, our
  own design (not a TARDIS: no police-box blue, no "POLICE" sign, no lamp).
- **Look:** an upright booth about 360 wide x 640 tall. Suggestion: red or teal frame with a small panel at the top
  reading `TIME` (one word, so it doesn't add on-screen text). Big doorway with the **door swung open to the right**,
  hinged on the right edge. The open door panel sits at about x +180..+330 with a window grid. The interior back wall
  is visible through the doorway: dark grey, with a crude dial or lever on the side wall so it reads as a machine.
  Optional: one small spray of sparks or glow at the base. Keep it clean so it stays readable at 0.85 scale.
- **Anchor:** bottom-centre = floor of the booth on the ground line. **Flat roof at exactly y=-640** from x=-170..+170.
  At s248-s249 a pigeon stands on it, placed at ground-640.
- **Doug inside:** I draw Doug **on top of** the booth, standing in the doorway, at the booth's x, with his feet at ground-8.
  Booth scale 1.0 gets Doug 0.75, and booth 0.85 gets Doug 0.62. The doorway opening should be at least x -120..+120 and
  y -560..-10 so Doug (cap included) fits inside the frame.
- **Shots:** s002, s003 (white void, opener), s004, s048, s092, s153, s199 (era title cards, scale 0.85), s005-s009
  (Ordovician rock: Doug steps out), s248, s249 (final frame: pigeon on the roof, empty doorway).

### Doug gear `sunburn` (A, engine change in `studio/doug.py`, art director)
- **Shots:** s089, s090, s091 (Ozone Hole survival, pose `sit`). The shotlist already passes `"gear": ["sunburn"]`.
  Unknown gear is currently ignored, so these shots render as plain Doug until it exists.
- **Creative director's note (A6, binding):** the sunburn is a **colour fill on the head plus flakes on the nose only**.
  The design stays locked: same head shape, crescent, eyes and red cap. Suggestion: head fill `#ff8a7a` instead of
  the skin white, arm lines drawn in `#e0201b` ("his arms turn bright red"), and 2-3 tiny white peel flakes on the
  nose or front of the face. Nothing else changes.
- Nice-to-have, not required: a wide `straddle` leg pose for s174 (one foot on each side of the crack). I use `arms_up`
  over a narrow crack for now.

---

## Ordovician (Killer Moss, Gondwana Ice)

### moss_patch (A)
- **What:** one of the first land plants, a liverwort-like early plant (item 1, "Killer Moss"). The hero of the item.
- **Look:** a **low, flat smear** of green, under a thumbnail high. Lobed, ribbon-like flat green thallus (mid green
  `#4c9a3a`, lighter top edges, darker undersides), a few tiny pale stalks with dot capsules, a faint darker texture.
  No flowers, no stems, no roots visible. It must look harmless.
- **Anchor:** bottom-centre, on the rock surface. About 240 x 50 (very wide and low).
- **Scales:** 0.8-1.6 on the landscape. **3.0 in the close-ups (s010-s012)**, so add enough lobes and texture to hold up
  at 720 px wide.
- **Shots:** s005, s009-s017, s019, s023-s025.
- **Done:** `assets/library/moss_patch.json`, preview `assets/previews/003-ord-dev-a.png`; at 1.4 and 3.0 on the ice background: assets/previews/003-ord-dev-in-scene.png.

### trilobite (B)
- **What:** Ordovician trilobite, the "species in the sea" icon for items 1, 2 and 5.
- **Look:** top-down view, head end facing right. Grey-brown segmented oval with a three-lobed body (central axis
  ridge), a semicircular head shield with two crescent eyes, a short tail shield. Outline 5.
- **Anchor:** centre. About 300 x 200. Used at 0.15-0.45, flipped, and once rotated 180 (stranded).
- **Shots:** s007, s022, s037-s040, s095, s096, s123.
- **Done:** `assets/library/trilobite.json`, preview `assets/previews/003-ord-dev-a.png`; at 0.38/0.15 on dark: assets/previews/003-ord-dev-dark.png.

### brachiopod (B)
- **What:** lamp shell, the most common shellfish of the era (stranded shells, casualty list).
- **Look:** two-valved shell seen from above, like a fan-shaped clam with a small beak (hinge) at the bottom and strong
  radiating ribs. Cream-tan `#e3cfa0` with brown growth lines.
- **Anchor:** centre. About 260 x 220. Used at 0.15-1.2. At 1.2 (s182-s184) it's the hero shell, and I punch holes in
  it with pale circles, so keep the centre area simple.
- **Shots:** s022, s037, s038, s040, s045, s095, s096, s123, s182-s184, s188-s190.
- **Done:** `assets/library/brachiopod.json`, preview `assets/previews/003-ord-dev-a.png`; centre kept plain (ribs only on the outer third); on dark: assets/previews/003-ord-dev-dark.png.

### doormat (C)
- **What:** the "doormat causing a blizzard" analogy (s021).
- **Look:** a brown coir doormat in low 3/4 view, bristle texture, darker border. **No text.**
- **Anchor:** centre. About 420 x 180.
- **Done:** `assets/library/doormat.json`, preview `assets/previews/003-ord-dev-a.png`.

### ice_block (C)
- **What:** Doug frozen solid mid-pat (s025, death 19).
- **Look:** **outline only, no fill**, so Doug shows through: an irregular block of ice with a thick pale-blue outline
  (`#9fd4f0`, width 8), white highlight streaks and corner glints, and frost spray along the bottom and edges.
- **Anchor:** bottom-centre on the ground. About 420 wide x 560 tall at scale 1. It is used at 0.85 over a sitting
  Doug (Doug scale 0.8) at the same ground line.
- **Done:** `assets/library/ice_block.json`, preview `assets/previews/003-ord-dev-a.png` (the tile crops its top; see it over a sitting Doug at 0.85 on #c9dbe8 in `assets/previews/003-ord-dev-in-scene.png`). It has a darker blue rim under the pale-blue outline so it stays visible on the pale-blue background.

### gondwana (A)
- **What:** the supercontinent Gondwana as a flat map landmass (Gondwana Ice). It slides across a globe and fills the
  screen in the close-ups.
- **Look:** one flat green landmass (`#6cbf5a`, dark green outline) with faint thin internal lines marking the future
  pieces. No labels. Place the pieces as follows so my labels land:
  - Africa: upper-right lobe, x 0..+250, y -200..+50.
  - South America: west lobe, x -280..-60, y -100..+150.
  - Antarctica: bottom, y +120..+250.
  - India and Australia: east and southeast, x +150..+300, y +50..+220.
- **Anchor:** centre. About 600 x 500. Used at 0.55-0.7 on a globe (r 360) and at 1.4 for the close-up. In the
  close-up I draw a white ice-cap ellipse centred at local (0,+30), over Africa and eastern South America.
- **Shots:** s026-s031.
- **Done:** `assets/library/gondwana.json`, preview `assets/previews/003-ord-dev-a.png`; on #3d5f5a: assets/previews/003-ord-dev-dark.png.

### snorkel_gear (B)
- **What:** Doug's snorkel and flippers for the "this beach was a reef" beat (Gondwana Ice). It's worn with the rig's
  `mask` gear.
- **Look:** a J-shaped snorkel tube (blue `#3a6ea5` with a yellow tip) rising behind the head on the left (back) side:
  from the mask strap at about (-55,-215) up to about (-40,-330). Two big blue flippers on the feet at about (+-32,+150),
  pointing forward (right).
- **Anchor:** Doug's hips (rig reference above). Used on `stand` and `hands_hips`, and **rotated -90 with `lie`** for
  the death (s047), so it must read sideways.
- **Shots:** s045, s046, s047.
- **Done:** `assets/library/snorkel_gear.json`, preview `assets/previews/003-ord-dev-a.png`; on Doug upright and rotated -90 with lie: assets/previews/003-ord-dev-in-scene.png. The tube sits just outside the head edge (x about -84..-58) rather than at x -55..-40, so it does not cover the left of the red cap.

## Devonian (Dead Reefs, Ozone Hole)

### stromatoporoid (A)
- **What:** an extinct reef-building sponge, the Devonian reef builder next to corals.
- **Look:** a lumpy, layered dome mound with stacked wavy growth layers visible in a cut face. The surface has low bumps
  (mamelons) and tiny star-shaped pore marks. Cream-tan `#d8c49a` with brown layer lines. No face.
- **Anchor:** bottom-centre (seabed). About 380 x 260. Sits between two `coral_reef` clusters at the same baseline.
- **Shots:** s049-s054, s056, s066, s067, s069, s070, s189, s190.
- **Done:** `assets/library/stromatoporoid.json`, preview `assets/previews/003-ord-dev-a.png`; on #3d5f5a: assets/previews/003-ord-dev-dark.png.

### angry_sun (B)
- **What:** the sun with an angry face (Ozone Hole: UV "from above").
- **Look:** a yellow-orange disc with short triangular rays, an angry V brow and a gritted-teeth mouth. Adult-coded
  annoyed, not a cute kids' sun.
- **Anchor:** centre. About 400 across including rays. Used at 0.6-0.8, never inside the death-counter zone.
- **Shots:** s072-s074, s077, s089-s091.
- **Done:** `assets/library/angry_sun.json`, preview `assets/previews/003-ord-dev-a.png`.

### spore and spore_malformed (B, a pair)
- **What:** fossil plant spores under the microscope, normal vs UV-damaged (Hangenberg evidence).
- **Look:** `spore` is a round pale amber spore with a Y-shaped (trilete) mark and a neat even fringe of short
  spines. `spore_malformed` is the same size and colour, but lumpy and lopsided, with long, uneven, **twisted** spines.
  Microscope-diagram style.
- **Anchor:** centre. About 300 across. Used at 0.6-0.7 side by side in a microscope circle.
- **Shots:** s075, s076.
- **Done:** `assets/library/spore.json`, `assets/library/spore_malformed.json`, preview `assets/previews/003-ord-dev-b.png`.

### supernova (B, SIL)
- **What:** a nearby exploding star (one proposed cause of the ozone loss).
- **Look:** a white-yellow core, a jagged orange-red shock ring, a few long spikes, and a spray glow. Its silhouette
  must read as a spiky starburst.
- **Anchor:** centre. About 500 across. It's shown as a silhouette first, then revealed (s080).
- **Done:** `assets/library/supernova.json`, preview `assets/previews/003-ord-dev-b.png`; silhouette: assets/previews/003-ord-dev-dark.png.

### campfire (C)
- **What:** "a campfire in the next town" (s081).
- **Look:** crossed logs, a ring of stones and orange-yellow flames.
- **Anchor:** bottom-centre. About 200 x 200. Used small (0.4) next to `house`.
- **Done:** `assets/library/campfire.json`, preview `assets/previews/003-ord-dev-b.png`.

### dunkleosteus (A, SIL) and dunkleosteus_dead (B)
- **What:** Dunkleosteus, the armoured placoderm fish.
- **Look:** a massive armoured head and neck shield made of grey-brown bony plates with visible plate seams and a
  small eye. The jaw is made of **sharp bony blade plates, not teeth** (two self-sharpening points at the front,
  slightly open). Behind the armour, a dark blue-grey shark-like body tapers to a shark-style (heterocercal) tail.
  Pale belly.
- **Layout:** facing right. The head and armour cover about x +100..+300, y -110..+40, and the jaw blades are at
  about (+290,+60). I point arrows there.
- **Anchor:** centre. About 600 x 260. Used at 1.4 (hero) and 1.1, and as a silhouette at s085.
- **`dunkleosteus_dead`:** the same fish **belly-up**, sinking, with an X eye, slightly tilted. Same anchor. Used at
  0.55 (s091).
- **Shots:** s085-s088, and s091 (dead).
- **Done:** `assets/library/dunkleosteus.json`, `assets/library/dunkleosteus_dead.json`, preview `assets/previews/003-ord-dev-b.png`; colour, silhouette and dead on #3d5f5a: assets/previews/003-ord-dev-dark.png.

## The Great Dying (Siberian Traps, Hot Tub Ocean, Purple Oceans)

### marshmallow_stick (B)
- **What:** Doug's marshmallow toasting stick (s108-s110, callback at s219).
- **Look:** a long thin brown stick with a white marshmallow on the tip. The marshmallow is toasted golden-brown on
  the lava side.
- **Layout:** handle end at about (-170,-60) where Doug's pointing hand is, and the marshmallow tip at about
  (+200,+60), angled down toward the lava.
- **Anchor:** centre. Used at 0.6-0.9, also lying on the ground (s110).
- **Done:** `assets/library/marshmallow_stick.json`, preview `assets/previews/003-great-dying-assets.png`; with Doug pointing at 0.75: `assets/previews/003-gd-a2.png`.

### conodont (B)
- **What:** the eel-like conodont animal whose tiny teeth record past temperatures (Hot Tub Ocean).
- **Look:** a slender pale pink-grey eel-like body, two **large round eyes** at the head end (its known defining
  feature), a fin fold with fin rays along the tail, and faint V-shaped muscle blocks along the body. Textbook look.
- **Anchor:** centre. About 500 x 120. I draw the teeth inline.
- **Shot:** s113.
- **Done:** `assets/library/conodont.json`, preview `assets/previews/003-great-dying-assets.png`; on dark: `assets/previews/003-gd-a2.png`.

### hot_tub (B)
- **What:** the "top setting on a hot tub" analogy (s119).
- **Look:** a square white-and-wood hot tub in low 3/4 view, turquoise water with bubbles, and a few steam wisps rising
  **off the water surface only**. No people.
- **Anchor:** bottom-centre. About 600 x 300.
- **Done:** `assets/library/hot_tub.json`, preview `assets/previews/003-great-dying-assets.png` (bottom-centre anchor, so the tile crops the steam).

### rubber_ring (B)
- **What:** Doug's swim ring (Hot Tub Ocean title card and Doug beat).
- **Look:** a red-and-white striped inflatable ring in low 3/4 view (an ellipse) with a small valve.
- **Anchor:** centre of the ring. About 420 x 150. It's drawn **behind** Doug: at ring scale = 1.25 x Doug scale, with
  Doug (pose `float`) 30 px above the anchor, it should sit around his waist.
- **Shots:** s111, s120, s125, s130-s132.
- **Done:** `assets/library/rubber_ring.json`, preview `assets/previews/003-great-dying-assets.png`; with a floating Doug + head_towel: `assets/previews/003-gd-a2.png`.

### head_towel (C)
- **What:** "a little towel on his head" (s130-s132).
- **Look:** a small folded white towel with a blue stripe, **resting on top of the cap dome** (cap top at y=-300). The
  brim and the red of the cap stay visible.
- **Anchor:** Doug's hips (rig reference). Used with pose `float`.
- **Done:** `assets/library/head_towel.json`, preview `assets/previews/003-great-dying-assets.png` (alone it sits high in the tile, it's hip-anchored); on Doug: `assets/previews/003-gd-a2.png`.

### rotten_egg (C)
- **What:** the "smells like rotten eggs" beat (hydrogen sulfide).
- **Look:** a cracked egg in its half-shell with a greyish-green yolk. I draw the stink lines inline.
- **Anchor:** centre. About 260 x 300.
- **Shots:** s136, s137.
- **Done:** `assets/library/rotten_egg.json`, preview `assets/previews/003-great-dying-assets.png`.

### lystrosaurus (A, SIL)
- **What:** Lystrosaurus, the survivor of the Great Dying that Doug befriends and that ignores him.
- **Look:** a stocky, barrel-bodied plant-eater with short sprawling legs, a short tail, and a boxy short-snouted head
  with a **horny beak** and **two tusks** pointing down. Grey-olive/brown skin, a lighter belly, a heavy-lidded,
  bored eye (it stares past Doug).
- **Layout:** facing right. The beak is at about (+280,-150) and the tusks at about (+260,-80) (my arrows point there).
- **Anchor:** bottom-centre (feet). About 520 x 260. Used at 1.2-1.4. It's also used tiny (0.22) as a map icon on
  `pangaea_map`, so keep the silhouette blocky.
- **Shots:** s146-s152 (silhouette at s146).
- **Done:** `assets/library/lystrosaurus.json`, preview `assets/previews/003-great-dying-assets.png`; silhouette and 0.22 map icon: `assets/previews/003-gd-b.png`.

## End-Triassic (Pangaea Splits, Acid Seas)

### pangaea_map (A)
- **What:** the supercontinent Pangaea as a flat map. It's used for the rift and also for the Lystrosaurus range and
  the reef map.
- **Look:** one flat green landmass (`#6cbf5a`, dark outline, faint internal lines for the future continents). No
  ocean fill (my background is the sea). No labels. Place it as follows so my labels and crack land:
  - The whole map spans about x -560..+560, y -380..+360.
  - North America: upper-left, x -480..-60, y -360..-60.
  - Eurasia: across the top right, x 0..+560, y -380..-120.
  - Africa: centre-right, x 0..+380, y -120..+250.
  - South America: lower left, x -300..0, y -40..+240.
  - Antarctica, India and Australia: along the bottom, y +240..+360.
  - The **seam between North America and Africa** runs along about x -40..-10, from y -300 to y +80. Leave it as a
    thin dark line. I draw the glowing red crack on top.
- **Anchor:** centre. Used at scale 1.0 centred on screen.
- **Shots:** s149, s154-s156, s158, s159, s192, s193.
- **Done:** `assets/library/pangaea_map.json`, full view at 0.6: `assets/previews/003-pangaea-map.png` (it's 1120 wide, so `assets/previews/003-end-triassic-assets.png` crops it).

### coelophysis (B)
- **What:** an early Triassic dinosaur (rival of the phytosaurs, then "dominates").
- **Look:** a slender, small bipedal theropod with a long neck and tail and a narrow head. Tan with darker back stripes.
  Not cute.
- **Anchor:** bottom-centre (feet). About 450 x 300. It also stands on the `podium` (feet on the top slab).
- **Shots:** s171-s173.
- **Done:** `assets/library/coelophysis.json`, preview `assets/previews/003-end-triassic-assets.png`.

### phytosaur (B)
- **What:** a crocodile-like Triassic hunter.
- **Look:** a low, armoured, crocodile-shaped body with back scutes and a very long, narrow snout. Defining feature:
  the **nostrils sit on a raised bump near the eyes**, not at the snout tip. Olive-brown.
- **Anchor:** bottom-centre. About 650 x 200.
- **Shots:** s171, s172.
- **Done:** `assets/library/phytosaur.json`, preview `assets/previews/003-end-triassic-assets.png`. Nostril mound sits at about (+124,-133), just in front of the eye at (+98,-108).

### volcano (A)
- **What:** a generic volcano (CAMP CO2, Acid Seas, Deccan Traps, the arguing scientists).
- **Look:** a grey-brown cone with a crater, two or three orange lava streams down the flanks, and a small smoke puff
  at the top. I add extra gas clouds myself.
- **Anchor:** bottom-centre. About 600 x 400. Used at 0.6-1.2.
- **Shots:** s164, s181, s200-s220 (most Deccan shots).
- **Done:** `assets/library/volcano.json`, preview `assets/previews/003-end-triassic-assets.png`. Crater rim at y=-326, smoke to about y=-440.

### ammonite (A)
- **What:** a coiled ammonite, the "shelled relatives of the octopus" and the locals Doug blends in with.
- **Look:** a planispiral coiled shell with strong ribs, cream with brown bands. The opening faces right, with a few
  short tentacles and one eye. Not cute.
- **Anchor:** centre. About 300 x 300. Used at 0.25-0.6, flipped.
- **Shots:** s188-s190, s196-s198.
- **Done:** `assets/library/ammonite.json`, preview `assets/previews/003-end-triassic-assets.png`; at 0.25-0.6 on dark/flipped: `assets/previews/003-gd-c.png`.

### ammonite_costume and ammonite_costume_flat (A, the episode's single costume callback)
- **What:** Doug's ammonite costume ("zipped in to blend in with the locals"), and its collapsed state for the death.
- **`ammonite_costume` look:** a coiled ammonite shell worn like a backpack and shell suit around the torso. Cream
  with brown ribs, **a visible front zipper** (the 002 onesie language), and a short fringe of fabric tentacles
  hanging around the waist. The head, face and cap stay fully visible. Pose `stand`.
- **`ammonite_costume_flat` look:** the same costume gone soft and flat, as a deflated, slumped shell. It's used
  **rotated -90** on top of a `lie` Doug at the same anchor (s198).
- **Anchor:** Doug's hips (rig reference). Used at Doug scale 0.85.
- **Shots:** s196, s197; flat: s198.
- **Done:** `assets/library/ammonite_costume.json` and `assets/library/ammonite_costume_flat.json`, preview `assets/previews/003-end-triassic-assets.png`; on Doug (stand, and lie rotated -90 with the flat one at 0.85): `assets/previews/003-gd-c.png`.

## End-Cretaceous (Deccan Traps, Chicxulub)

### india_map (B)
- **What:** the Indian subcontinent as a flat map (Deccan Traps).
- **Look:** a flat green outline (`#6cbf5a`, dark outline), no labels. The Deccan plateau is west-central, at about
  local (-50,-20) (I spray the red lava stain there).
- **Anchor:** centre. About 500 x 600. Used at 1.2.
- **Shots:** s201-s203.
- **Done:** `assets/library/india_map.json`, preview `assets/previews/003-every-mass-extinction-end-cretaceous-full.png` (contact sheet at 0.5: `assets/previews/003-every-mass-extinction-end-cretaceous.png`). Projected so the Deccan Traps (75.5E 20N) land exactly at local (-50,-20); extent x -175..+325, y -315..+260, so the centre of the bbox is right of and above the anchor (at 1.2 the map spans about x 550-1150, y 200-890 in s201-s203).

### empire_state_building (B)
- **What:** the scale unit for "five Empire State Buildings piled on top of each other".
- **Look:** a slim Art Deco tower with setbacks and a spire, in grey stone and blue windows.
- **Anchor:** bottom-centre. **Exactly 512 tall** (y -512..0) and about 160 wide. I stack five at scale 0.25 with
  128 px steps, so they must touch end to end.
- **Shot:** s205.
- **Done:** `assets/library/empire_state_building.json`, preview `assets/previews/003-every-mass-extinction-end-cretaceous-full.png` (contact sheet at 0.5: `assets/previews/003-every-mass-extinction-end-cretaceous.png`). Base y=0, spire tip y=-512, 160 wide.

### fire_extinguisher (B)
- **What:** Doug's fire extinguisher for his third volcanic extinction.
- **Look:** a red cylinder with a black hose and nozzle, a pressure gauge and a white label (no readable text).
- **Anchor:** centre. About 150 x 330. Used at 0.6 held at Doug's pointing hand, and rotated 80 lying on the ground in
  the death (s220).
- **Shots:** s218-s220.
- **Done:** `assets/library/fire_extinguisher.json`, preview `assets/previews/003-every-mass-extinction-end-cretaceous-full.png` (contact sheet at 0.5: `assets/previews/003-every-mass-extinction-end-cretaceous.png`). Extent y -170..+160.

### asteroid (A, SIL)
- **What:** the Chicxulub impactor.
- **Look:** a lumpy grey-brown rock with craters and a lighter lit side. Plain rock, no fire trail (the art can sit in
  daylight next to Everest).
- **Anchor:** centre. About 400 across. Used tiny (0.25) as a timeline icon, at 1.3 next to `mount_everest` at 0.6
  (true relative size: 10 km wide vs 8.8 km tall), and at 1.6 as a silhouette with red glow (s224).
- **Shots:** s201, s207, s208, s210, s211, s214-s217, s224-s226, s241.
- **Done:** `assets/library/asteroid.json`, preview `assets/previews/003-every-mass-extinction-end-cretaceous-full.png` (contact sheet at 0.5: `assets/previews/003-every-mass-extinction-end-cretaceous.png`); silhouette checked (clean lumpy outline), and on a dark background.

### sauropod (A)
- **What:** a long-necked late Cretaceous plant-eater (titanosaur).
- **Look:** grey-green, a long neck and tail, a small head, pillar legs and a lighter belly.
- **Anchor:** bottom-centre. About 700 x 450. Used at 0.5-1.0.
- **Shots:** s221-s223, s233, s234, s236, s243-s245.
- **Done:** `assets/library/sauropod.json`, preview `assets/previews/003-every-mass-extinction-end-cretaceous-full.png` (contact sheet at 0.5: `assets/previews/003-every-mass-extinction-end-cretaceous.png`). Extent x -400..+352, y -472..0 (head up-right).

### t_rex (A)
- **What:** Tyrannosaurus, the meat-eater of the food chain and the "every dinosaur that wasn't a bird" line-up.
- **Look:** brown-olive, a big head, tiny arms, a horizontal body and a lighter belly. Mouth closed or slightly open.
  Not cute.
- **Anchor:** bottom-centre. About 600 x 420. Used at 0.45-0.9, flipped.
- **Shots:** s223, s236, s243, s248.
- **Done:** `assets/library/t_rex.json`, preview `assets/previews/003-every-mass-extinction-end-cretaceous-full.png` (contact sheet at 0.5: `assets/previews/003-every-mass-extinction-end-cretaceous.png`). Extent x -345..+338, y -412..0.

### fern (B)
- **What:** a fern clump for the peaceful Cretaceous morning.
- **Look:** five or six arching green fronds with leaflets.
- **Anchor:** bottom-centre. About 300 x 300.
- **Shots:** s221-s223, s233, s234, s244, s245.
- **Done:** `assets/library/fern.json`, preview `assets/previews/003-every-mass-extinction-end-cretaceous-full.png` (contact sheet at 0.5: `assets/previews/003-every-mass-extinction-end-cretaceous.png`). Extent about 380 x 300.

### feathered_dinosaur (B)
- **What:** a small feathered theropod, the "ones that made it had feathers" beat.
- **Look:** a raptor-like body with brown feathers, wing-like feathered arms and a feathered tail. Not cute.
- **Anchor:** bottom-centre. About 400 x 300.
- **Shot:** s247.
- **Done:** `assets/library/feathered_dinosaur.json`, preview `assets/previews/003-every-mass-extinction-end-cretaceous-full.png` (contact sheet at 0.5: `assets/previews/003-every-mass-extinction-end-cretaceous.png`). Note: the feathered tail makes it wider than asked, x -395..+232 (y -297..0); at 0.8 from x=520 the tail reaches x about 205.

### pigeon (A)
- **What:** the final-frame pigeon on the time machine roof ("it still won't share its bench").
- **Look:** a grey feral pigeon with an iridescent green-purple neck, an orange eye and two dark wing bars. Head tilted
  down, staring at the doorway below. Unimpressed.
- **Anchor:** bottom-centre (feet). About 220 x 200. Placed at the time machine roof (booth ground - 640 x scale).
- **Shots:** s248, s249.
- **Done:** `assets/library/pigeon.json`, preview `assets/previews/003-every-mass-extinction-end-cretaceous-full.png` (contact sheet at 0.5: `assets/previews/003-every-mass-extinction-end-cretaceous.png`). Feet on y=0; extent about x -138..+134, y -165..0.

---

### Reused from the library (no request)
`usa_map` (three different scales for the three "size of the United States" lines, per the CD: s032 three small maps in
one ice blob, s099 one map under a 1 km lava slab, s160 a "CAMP = USA" equation), `world_map` (world view and zoomed
x2.4 on Siberia and x3 on the Yucatan), `coral_reef`, `small_fish`, `scientist`, `thermometer`, `calendar`, `clock`,
`thumbs_up_hand`, `house`, `swimming_pool`, `burrow`, `small_plant`, `leaf`, `podium`, `mount_everest`, `songbird`,
`suitcase`, `doug_cap`, `heart_icon`, and the annotation set (`red_x`, `question_mark`, `exclamation_mark`,
`warning_triangle`).
