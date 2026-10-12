# Asset requests: 015 The Deeper Doug Digs, the Scarier the Fossils Get

From the director, for the illustrator (the art director approves). House style: `assets/library/anglerfish.json` and `channel/art_bible.md`.
- Detailed tier for creatures and props (outlines 4-6, flat fills plus spray shading). Face **right** unless noted. `bc` = anchor bottom-centre, `c` = centre. Sizes are local units at scale 1; the shotlist is laid out to these bboxes.
- Tone (brief section 7): dinosaurs and animals look dangerous and documentary-cartoon, never cute. No baby animals, no wounds, no severed parts, no emergence. Parasites are diagram icons with no faces.
- Several assets appear on dark scenes (x-ray `#0d1b2a`, near-black rock): mid-tone fills.
- Priority: A = hero (8+ shots), B = 3-7, C = one-off.

**For the art director:** the episode strata ramp (inline in the shotlist, layer 1 to 11): `#d9b77a`, `#d4a04a`, `#c07a3a`, `#a65a32` (+ boundary clay stripe `#efe6d0`), `#8e4a2c`, `#7a6656`, `#6b7280`, `#4f5560`, `#4a3a34` (grey bands `#5f5f5f`), `#2a2a2e`, `#15181a` (green glow `#2f5a3a`). Shaft interior `#f1e4c6`. DEPTH meter = size-28 label at (1590, 238) with the `shovel` asset at scale 0.16 to its left.

**Reused from the library:** time_machine, doug_cap, usa_map, world_map, india_map, switzerland_map, volcano, basketball_hoop, ruler, picnic_blanket, sandwich, horse, songbird, hippo, clock, scientist, jewel_wasp (parasitoid wasp), sofa, crt_tv, lizard, bank_card, shark, frog, small_fish, dinosaur_skeleton, t_rex, golf_ball, magnifying_glass, pigeon, dinner_plate, gravestone, calendar, storm_cloud, rat, fern, feathered_dinosaur, large_dog, fighting_dinosaurs_fossil (005 callback), fishing_rod, rock_lump, water_splash(_small), snorkel, ichthyosaur_fossil, ammonite, humboldt_squid, tapeworm, worm_icon, komodo_dragon, compact_camera, printed_card, croc_jaws_open, trilobite, dunkleosteus, and the annotation set.

**Drawn inline (no asset):** all backgrounds and strata, the shaft, rice grains, synchrotron ring, ash layers, microscope circle and eggs, coprolite slices, grinder, spiral-valve diagram, paper cups, Ediacaran soft discs, the neighbour shell tube, baseball bat, breath mint, GUARD flag, human hair.

### `shovel` (A)
- Doug's garden spade (the episode's hero prop and the DEPTH meter icon). Pale wooden shaft #c08a4a with dark edge, wooden T-grip at the top, grey steel blade #9aa3ab with a darker shaded half, a few dirt specks on the blade. Upright, blade down.
- Anchor = the grip point where Doug's front hand holds it (stand pose hand = hip + (50,-14) x scale). Shaft vertical; T-grip top at (0,-110), blade bottom tip at (0,+166) so it rests on the ground when Doug stands. ~70x280 (x -35..35, y -125..+166). Must read at scale 0.16 as a tiny meter icon, so keep the blade shape bold. Closing shot: planted upright, two caps stacked on the T-grip at (0,-110).
- Shots: s002-s289
- **DONE** (illustrator): `assets/library/shovel.json`, preview assets/previews/015-assets-a.png (checks: assets/previews/015-assets-checks.png, 015-assets-fix.png)

### `teleoceras` (A)
- Teleoceras, Miocene barrel-bodied rhino: very short stubby legs, long round barrel body like a hippo, one small conical nose horn, grey-brown #8a7a6a with darker back, lighter belly, small ears, small eye under a heavy lid. Not cute.
- `bc` (feet on y=0), ~520x260 (x -260..260, y -260..0), facing right.
- Shots: s008-s013, s017, s021, s024-s025, s027-s030, s281
- **DONE** (illustrator): `assets/library/teleoceras.json`, preview assets/previews/015-assets-a.png (checks: assets/previews/015-assets-checks.png, 015-assets-fix.png)

### `camel` (C)
- Miocene camel (generic modern-looking one-hump-free camelid, i.e. a llama-like long-necked camel without hump), sandy tan.
- `bc`, ~360x330, facing right.
- Shots: s012, s023-s024
- **DONE** (illustrator): `assets/library/camel.json`, preview assets/previews/015-assets-a.png (checks: assets/previews/015-assets-checks.png, 015-assets-fix.png)

### `teleoceras_skeleton` (B)
- Teleoceras skeleton lying on its side in grey ash (Ashfall in-situ style): cream #efe6d0 bones, skull with nose horn right, ribs, short leg bones. One leg bone near local (+60,+60) shows a lumpy knobbly bone growth (the lung-failure marker; red ring aims there).
- `c`, ~520x220.
- Shots: s026, s032-s033
- **DONE** (illustrator): `assets/library/teleoceras_skeleton.json`, preview assets/previews/015-assets-a.png (checks: assets/previews/015-assets-checks.png, 015-assets-fix.png)

### `ash_man` (C)
- A small snowman made of grey volcanic ash: two stacked grey balls #9a9a9a with darker spray shading, pebble eyes and mouth, twig arms. No face expression beyond the pebbles.
- `bc`, ~160x260; flat top at (0,-260) where a doug_cap sits at scale 0.4.
- Shots: s029-s031
- **DONE** (illustrator): `assets/library/ash_man.json`, preview assets/previews/015-assets-a.png (checks: assets/previews/015-assets-checks.png, 015-assets-fix.png)

### `fly_pupa` (A)
- Fossil fly pupa (puparium): small brown barrel capsule #8a5a2a, rounded ends, 8-10 faint segment rings, slightly glossy highlight. Mineralised look (a bit stony).
- `c`, ~200x90, long axis horizontal. Used from scale 0.45 (pile) to 3.0 (hero); also as a black silhouette with blue glow.
- Shots: s036-s044, s046, s052-s054, s281
- **DONE** (illustrator): `assets/library/fly_pupa.json`, preview assets/previews/015-assets-a.png (checks: assets/previews/015-assets-checks.png, 015-assets-fix.png)

### `fly_pupa_xray` (B)
- X-ray view of a fly pupa on a dark background: pale cyan #9fe6ff glowing outline of the case, and inside it the pale white silhouette of an adult parasitoid wasp folded up (antennae and wings tucked). Diagram, no gore, no emergence.
- `c`, ~600x280. Must read on #0d1b2a.
- Shots: s045, s047-s048, s051
- **DONE** (illustrator): `assets/library/fly_pupa_xray.json`, preview assets/previews/015-assets-b.png (checks: assets/previews/015-assets-checks.png, 015-assets-fix.png)

### `fly_pupa_costume` (B)
- Doug's fly-pupa costume (worn prop, like squid_costume): brown segmented barrel suit from neck to shins, arms hidden or poking out stubby; head, face and red cap fully visible above.
- Anchor = Doug's hips at Doug scale 1 (x,y,scale same as Doug). Fits stand pose.
- Shots: s053-s055
- **DONE** (illustrator): `assets/library/fly_pupa_costume.json`, preview assets/previews/015-assets-b.png (checks: assets/previews/015-assets-checks.png, 015-assets-fix.png)

### `fly_pupa_costume_flat` (C)
- The fly-pupa costume gone flat and empty on the ground, with two X eyes printed on its front. No body inside shown. The cap is added separately beside it.
- `bc`, ~360x140.
- Shots: s056
- **DONE** (illustrator): `assets/library/fly_pupa_costume_flat.json`, preview assets/previews/015-assets-b.png (checks: assets/previews/015-assets-checks.png, 015-assets-fix.png)

### `palaeopython` (B)
- Young Palaeopython (Eocene python relative): brown-olive snake with darker saddle blotches, loosely coiled on the ground, head raised slightly at the right (~(+190,-40)), visible lizard-sized bulge mid-body. Unimpressed eye. Not cute.
- `c`, ~420x200, facing right.
- Shots: s059, s062, s071, s074-s078, s281
- **DONE** (illustrator): `assets/library/palaeopython.json`, preview assets/previews/015-assets-b.png (checks: assets/previews/015-assets-checks.png, 015-assets-fix.png)

### `messel_snake_slab` (B)
- Messel oil-shale slab: dark grey-brown stone #4a4038 with a coiled fossil snake skeleton (cream vertebrae and ribs) and, inside its belly area at local (+40,+20), a small lizard skeleton.
- `c`, ~640x420.
- Shots: s060-s061, s063, s066
- **DONE** (illustrator): `assets/library/messel_snake_slab.json`, preview assets/previews/015-assets-b.png (checks: assets/previews/015-assets-checks.png, 015-assets-fix.png)

### `nested_scan` (B)
- CT/X-ray scan diagram on dark: snake outline in pale cyan with its body loop, a lizard outline inside it centred at (+40,+20), and a tiny insect blob inside the lizard at (+70,+22). Three nested outlines, diagram only.
- `c`, ~700x420. Labels/arrows aim at the points given.
- Shots: s067-s069, s079
- **DONE** (illustrator): `assets/library/nested_scan.json`, preview assets/previews/015-assets-b.png (checks: assets/previews/015-assets-checks.png, 015-assets-fix.png)

### `nesting_dolls` (C)
- Three Russian nesting dolls in a row, big to small, plain red/yellow painted, simple faces.
- `bc`, ~520x300.
- Shots: s070
- **DONE** (illustrator): `assets/library/nesting_dolls.json`, preview assets/previews/015-assets-c.png (checks: assets/previews/015-assets-checks.png, 015-assets-fix.png)

### `doug_cap_fossil` (B)
- Doug's cap turned to stone (003 callback): exactly the doug_cap shape, but grey stone #9a958c with faint red tint, cracks and a chip.
- `c`, ~200x80, same geometry as doug_cap.
- Shots: s086-s087, s287-s288
- **DONE** (illustrator): `assets/library/doug_cap_fossil.json`, preview assets/previews/015-assets-c.png (checks: assets/previews/015-assets-checks.png, 015-assets-fix.png)

### `sue_skull_case` (B)
- Sue's T. rex skull (facing right, dark brown-black fossil bone, big teeth) on a low plinth inside a glass display case (pale blue glass, white glint lines).
- `bc`, ~520x420; skull ~400 wide inside.
- Shots: s088-s089, s108
- **DONE** (illustrator): `assets/library/sue_skull_case.json`, preview assets/previews/015-assets-c.png (checks: assets/previews/015-assets-checks.png, 015-assets-fix.png)

### `sue_jaw` (B)
- Close-up of a T. rex lower jaw (left side, facing right), dark brown fossil bone, teeth row at the front (right). Three smooth-edged round holes on the back half at local (+120,-10), (+200,0), (+250,+20), radius ~25 each. No wounds, just bone.
- `c`, ~800x300. Red rings aim at the hole points.
- Shots: s090-s091, s093, s099, s101-s102
- **DONE** (illustrator): `assets/library/sue_jaw.json`, preview assets/previews/015-assets-c.png (checks: assets/previews/015-assets-checks.png, 015-assets-fix.png). Note: drawn as a true LEFT-side view, so the snout/tooth row is at the LEFT and the holes sit on the back half at the requested points (narration: "back half").

### `trichomonas` (C)
- Single-celled Trichomonas, diagram cartoon: pale green pear-shaped cell, 4 front flagella, wavy membrane along one side, a nucleus. No face.
- `c`, ~220x140.
- Shots: s094-s095, s100
- **DONE** (illustrator): `assets/library/trichomonas.json`, preview assets/previews/015-assets-c.png (checks: assets/previews/015-assets-checks.png, 015-assets-fix.png)

### `falcon` (C)
- Perched falcon (peregrine type): slate-grey back, barred pale chest, dark moustache stripe, yellow feet and cere. Not cute.
- `bc`, ~260x260, facing right (used flipped).
- Shots: s096
- DONE: `assets/library/falcon.json`; preview `assets/previews/015-deeper-fossils-dig-assets-b.png` (worn check `015-worn.png`, dark check `015-dark.png`).

### `vet_coat` (B)
- White vet/lab coat worn by Doug, with a grey stethoscope hanging round the neck (cord apex at the neck point, never across the face).
- Anchor = Doug's hips at scale 1. Head and cap fully visible.
- Shots: s104-s106
- DONE: `assets/library/vet_coat.json`; preview `assets/previews/015-deeper-fossils-dig-assets-b.png` (worn check `015-worn.png`, dark check `015-dark.png`).

### `dinosaur_nest` (B)
- Sauropod nest: low sandy-brown mound with 4 big round cream eggs #efe6d0 with faint speckles, one partly sunk. No hatchlings.
- `bc`, ~520x200; eggs r ~45.
- Shots: s109, s119, s121-s129
- DONE: `assets/library/dinosaur_nest.json`; preview `assets/previews/015-deeper-fossils-dig-assets-b.png` (worn check `015-worn.png`, dark check `015-dark.png`).

### `sanajeh_slab` (B)
- Sanajeh fossil slab: red-brown stone, a coiled snake skeleton wrapped around a crushed egg at (0,0), two whole round eggs at (-200,+80) and (+200,+90), and a small cluster of loose little bones at (+230,-120) (the hatchling remains, just bones, no body shape).
- `c`, ~640x420.
- Shots: s111-s116, s120
- DONE: `assets/library/sanajeh_slab.json`; preview `assets/previews/015-deeper-fossils-dig-assets-b.png` (worn check `015-worn.png`, dark check `015-dark.png`).

### `sanajeh` (A)
- Sanajeh indicus, living: long brown snake with darker blotches, stretched in a loose S, head at the right (~(+330,-20)), slightly open mouth. Not cute.
- `c`, ~700x200, facing right.
- Shots: s117-s119, s121-s129, s281
- DONE: `assets/library/sanajeh.json`; preview `assets/previews/015-deeper-fossils-dig-assets-b.png` (worn check `015-worn.png`, dark check `015-dark.png`).

### `mud_wave` (B)
- Cartoon brown wave of mud and sand rolling to the right: curling crest, darker inner swirl, pebbles, spray of mud dots. No bodies.
- `bc`, ~900x420.
- Shots: s124, s126, s129
- DONE: `assets/library/mud_wave.json`; preview `assets/previews/015-deeper-fossils-dig-assets-b.png` (worn check `015-worn.png`, dark check `015-dark.png`).

### `volcanic_mudflow` (B)
- Same idea as mud_wave in grey volcanic mud #8a8a8a with darker swirls and ash puffs.
- `bc`, ~900x420.
- Shots: s135, s151, s155
- DONE: `assets/library/volcanic_mudflow.json`; preview `assets/previews/015-deeper-fossils-dig-assets-b.png` (worn check `015-worn.png`, dark check `015-dark.png`).

### `psittacosaurus` (B)
- Adult Psittacosaurus: bipedal-ish beaked dinosaur, parrot beak, small cheek horns, row of bristle quills on the tail, tan-olive. Not cute.
- `bc`, ~420x260, facing right.
- Shots: s135, s148
- DONE: `assets/library/psittacosaurus.json`; preview `assets/previews/015-deeper-fossils-dig-assets-b.png` (worn check `015-worn.png`, dark check `015-dark.png`).

### `repenomamus` (B)
- Repenomamus robustus: badger-sized stocky mammal, dark brown fur, short legs, small ears, visible front teeth. Not cute.
- `bc`, ~300x150, facing right.
- Shots: s137, s281
- DONE: `assets/library/repenomamus.json`; preview `assets/previews/015-deeper-fossils-dig-assets-b.png` (worn check `015-worn.png`, dark check `015-dark.png`).

### `repenomamus_stomach_slab` (C)
- Fossil slab with a Repenomamus skeleton and a small cluster of tiny dinosaur bones in its ribcage at (+20,0).
- `c`, ~600x360.
- Shots: s138-s139
- DONE: `assets/library/repenomamus_stomach_slab.json`; preview `assets/previews/015-deeper-fossils-dig-assets-b.png` (worn check `015-worn.png`, dark check `015-dark.png`).

### `repenomamus_fight_slab` (B)
- The 2023 Lujiatun fossil: pale volcanic slab with two skeletons, the mammal lying on top of the larger dinosaur. Points: mammal paw on the dinosaur's lower jaw at (+300,-40), mammal back foot on its hind leg at (-120,+60), mammal teeth on the ribs at (+80,-20).
- `c`, ~760x420.
- Shots: s140-s141, s144-s146
- DONE: `assets/library/repenomamus_fight_slab.json`; preview `assets/previews/015-deeper-fossils-dig-assets-b.png` (worn check `015-worn.png`, dark check `015-dark.png`).

### `repenomamus_fight` (A)
- Living reconstruction: adult Psittacosaurus lying on its belly, Repenomamus on top of it, jaws on the ribs, paw on the jaw. Tense, documentary-cartoon, no blood.
- `bc`, ~560x300, dinosaur facing right.
- Shots: s142-s143, s149, s151-s154
- DONE: `assets/library/repenomamus_fight.json`; preview `assets/previews/015-deeper-fossils-dig-assets-b.png` (worn check `015-worn.png`, dark check `015-dark.png`).
- REDRAWN after art review: preview `assets/previews/015-fight-v2.png`, in-shot check `assets/previews/015-fight-shot.png`. New hold points (local): bite on ribs (+34,-64), paw on lower jaw (+274,-46), hind foot on thigh (-180,-74).

### `referee_shirt` (B)
- Black-and-white striped referee shirt worn by Doug, with a silver whistle on a cord at the mouth area (~(+50,-195) at scale 1, not covering the eyes).
- Anchor = Doug's hips at scale 1.
- Shots: s152-s154
- DONE: `assets/library/referee_shirt.json`; preview `assets/previews/015-deeper-fossils-dig-assets-b.png` (worn check `015-worn.png`, dark check `015-dark.png`).

### `whistle` (C)
- Silver referee whistle on its own.
- `c`, ~90x50.
- Shots: s155-s156
- DONE: `assets/library/whistle.json`; preview `assets/previews/015-deeper-fossils-dig-assets-b.png` (worn check `015-worn.png`, dark check `015-dark.png`).

### `rhamphorhynchus` (A)
- Rhamphorhynchus: pterosaur with long narrow wings spread, long tail ending in a diamond vane, long toothy beak (tip ~(+280,-20), throat ~(+220,0)), brown-grey body. Not cute.
- `c`, ~600x300, facing right.
- Shots: s163-s166, s168, s172-s175, s180-s181
- DONE: `assets/library/rhamphorhynchus.json`; preview `assets/previews/015-deeper-fossils-dig-assets-b.png` (worn check `015-worn.png`, dark check `015-dark.png`).

### `aspidorhynchus` (A)
- Aspidorhynchus: long slender silver-grey fish with a sharp sword-like snout and rows of small teeth, shiny scales, forked tail.
- `c`, ~600x160, facing right. Also used as black silhouette.
- Shots: s166-s168, s172-s175, s180-s181, s281
- DONE: `assets/library/aspidorhynchus.json`; preview `assets/previews/015-deeper-fossils-dig-assets-b.png` (worn check `015-worn.png`, dark check `015-dark.png`).

### `wing_teeth_closeup` (C)
- Close-up: the fish's jaw rows of teeth tangled in a thin brown wing membrane (fibres drawn as fine lines). Wing bone visible separately above. No blood.
- `c`, ~900x500.
- Shots: s169-s171
- DONE: `assets/library/wing_teeth_closeup.json`, preview `assets/previews/015-assets-wide.png` (dark-bg check `015-assets-darktest.png`)

### `aspidorhynchus_slab` (B)
- Solnhofen cream limestone slab: fish skeleton and a pterosaur skeleton lying right at its snout, wing outline clearly visible at upper right (~(+280,-70)).
- `c`, ~800x360.
- Shots: s161-s162, s176-s177
- DONE: `assets/library/aspidorhynchus_slab.json`, preview `assets/previews/015-assets-wide.png` (dark-bg check `015-assets-darktest.png`)

### `tanystropheus` (A)
- Tanystropheus: neck about three times the body length. Tail x -500..-170, body -170..0, neck 0..+470, small head +470..+500 with nostrils on top of the snout and long curved teeth. Olive-grey with a lighter belly, paddle-ish limbs.
- `c`, ~1000x240, facing right.
- Shots: s186, s189-s193, s199, s201-s204, s281
- DONE: `assets/library/tanystropheus.json`, preview `assets/previews/015-assets-wide.png` (dark-bg check `015-assets-darktest.png`)

### `tanystropheus_slab` (B)
- Grey rock slab with only a skull and a long line of 13 long neck vertebrae; the neck ends abruptly at (-400,0) with a few tooth-mark notches. Bones only, never a severed neck in flesh.
- `c`, ~900x260.
- Shots: s194-s198, s201
- DONE: `assets/library/tanystropheus_slab.json`, preview `assets/previews/015-assets-wide.png` (dark-bg check `015-assets-darktest.png`)

### `giraffe` (C)
- Giraffe standing, side view, neck up.
- `bc`, ~360x700.
- Shots: s191
- DONE: `assets/library/giraffe.json`, preview `assets/previews/015-assets-giraffe.png` (dark-bg check `015-assets-darktest.png`)

### `nothosaurus` (B)
- Nothosaurus: marine reptile with long narrow snout and interlocking fang teeth, long neck (shorter than Tanystropheus), paddle limbs, dark olive back.
- `c`, ~700x220, facing right. Also used large as a black silhouette.
- Shots: s199-s200, s204
- DONE: `assets/library/nothosaurus.json`, preview `assets/previews/015-assets-wide.png` (dark-bg check `015-assets-darktest.png`)

### `xenacanth` (B)
- Permian freshwater xenacanth shark: eel-like body, long dorsal fin running down the back, a single spine sticking back from the head, grey-brown.
- `c`, ~560x180, facing right.
- Shots: s208-s209, s212, s225-s226, s281
- DONE: `assets/library/xenacanth.json`, preview `assets/previews/015-assets-wide.png` (dark-bg check `015-assets-darktest.png`)

### `coprolite` (B)
- Shark coprolite: stone, grey-brown, ~5 cm, tightly spiral-twisted like a drill bit. Read as a fossil stone, never comic.
- `c`, ~260x120.
- Shots: s210-s215, s221
- DONE: `assets/library/coprolite.json`, preview `assets/previews/015-assets-small.png` (dark-bg check `015-assets-darktest.png`)

### `shark_fin` (B)
- Dorsal fin above the waterline with a small ripple ring.
- `bc` on the waterline, ~160x150.
- Shots: s227-s229
- DONE: `assets/library/shark_fin.json`, preview `assets/previews/015-assets-small.png` (dark-bg check `015-assets-darktest.png`)

### `herefordshire_nodule` (B)
- Herefordshire nodule cracked into two halves, pale grey stone, with a tiny dark shape inside.
- `c`, ~300x220.
- Shots: s234, s245
- DONE: `assets/library/herefordshire_nodule.json`, preview `assets/previews/015-assets-small.png` (dark-bg check `015-assets-darktest.png`)

### `ostracod` (B)
- Ostracod: tiny crustacean in a bean-shaped two-part shell, pale tan, a few legs/antennae poking out.
- `c`, ~300x200.
- Shots: s235, s250-s251, s281
- DONE: `assets/library/ostracod.json`, preview `assets/previews/015-assets-small.png` (dark-bg check `015-assets-darktest.png`)

### `ostracod_tongue_worms` (A)
- Magnified ostracod (as above) with two slender pale worm shapes clinging to it: one on the outside of the shell at (+230,-60), one tucked inside at (-40,+30) next to small round eggs. Diagram, no faces.
- `c`, ~600x400.
- Shots: s236-s242, s249, s255
- DONE: `assets/library/ostracod_tongue_worms.json`, preview `assets/previews/015-assets-small.png` (dark-bg check `015-assets-darktest.png`)

### `cloudina_tube` (A)
- Cloudina: upright tube of stacked cones nested inside each other, like a pile of paper cups, cream-white with grey shading, top cone open.
- `bc`, ~80x260.
- Shots: s261-s265, s267-s268, s270, s272-s274, s277, s282-s286
- DONE: `assets/library/cloudina_tube.json`, preview `assets/previews/015-assets-cloudina.png` (dark-bg check `015-assets-darktest.png`)

### `cloudina_bored` (B)
- Close-up of a Cloudina cone stack with one neat small round hole drilled through the shell at (0,-40).
- `c`, ~300x400.
- Shots: s269, s271, s276, s279-s281
- DONE: `assets/library/cloudina_bored.json`, preview `assets/previews/015-assets-cloudina.png` (dark-bg check `015-assets-darktest.png`)

### `cloudina_costume` (B)
- Doug's Cloudina costume: stacked-cone suit from shoulders to feet, cream-white; head, face and cap visible on top.
- Anchor = Doug's hips at scale 1; stand pose.
- Shots: s283-s286
- DONE: `assets/library/cloudina_costume.json`, preview `assets/previews/015-assets-cloudina.png` (dark-bg check `015-assets-darktest.png`)
