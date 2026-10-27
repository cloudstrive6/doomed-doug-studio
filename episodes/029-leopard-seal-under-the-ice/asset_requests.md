# 029-leopard-seal-under-the-ice: asset requests (director)

House style: detailed tier for creatures, places and props (thick dark outlines, flat fills, interior shading); crude tier
(`auto_ink`, `keep_ink` faces) for the humans, who are generic stand-ins, never likenesses. Facing right unless noted. Sizes
are local units at scale 1 and match the layout the shotlist was built against (the director checked every shot with
placeholder boxes of exactly these extents), so please keep the anchors and extents. **The leopard seal family is the
priority and needs the art director's sign-off on the design (brief section 7): reptile head, menacing, no cute eyes.**
All `leopard_seal*` drawings must be the same animal (same palette, spots, head shape).

**Status (illustrator, 2026-10-27): all 37 drawn and previewed. The leopard seal family still needs the art director's sign-off.**

Reused from the library (no request): `antarctica_map`, `baby_grand_piano`, `binoculars`, `calendar`, `camper`, `canoe_paddle`, `cape_fur_seal`, `car_trailer`, `cat_yawn`, `city_skyline_night`, `city_skyline_small`, `clipboard`, `clock`, `deck_chair`, `dinner_plate`, `dollar_bill`, `doug_cap`, `exclamation_mark`, `field_guide_open`, `grizzly_bear`, `guitar`, `heart_icon`, `highspeed_camera`, `hot_water_drill`, `humpback_whale`, `journal_paper`, `large_dog`, `lizard`, `magnifying_glass`, `old_book`, `phone`, `placard`, `platform_scale`, `question_mark`, `red_x`, `research_hut`, `sailboat`, `scientist`, `seal_costume`, `seal_costume_flat`, `signboard`, `silver_fish`, `small_car`, `stew_bowl`, `us_quarter`, `wait_stopwatch`, `warning_triangle`, `water_splash`, `water_splash_small`.

## `leopard_seal`
**Creature (hero).** Leopard seal swimming, side view, the episode's hero predator.

- Look: Long, slim, almost snake-like body (much slimmer than `weddell_seal`), dark slate-grey back `#5f6670` fading to a pale silver-grey belly `#c9ced4`, dark grey-black spots densest on the throat, shoulders and flanks. The head is the key feature: huge, long, flat and **reptile-like** (about a quarter of the body length), wide jaw line that runs back past the eye in a permanent 'grin', small dark eye under a heavy brow, no visible ear flaps, a few whiskers. Very long front flippers held back along the body, two hind flippers trailing at the left. **Menacing, never cute**: no big round eyes, no smile highlights (CD note). Detailed tier with soft interior shading.
- Facing / anchor / size: Facing right, centre anchor, about 800 x 220 (x -400..400, y -110..110), head x +200..+400.
- Notes: Real length is 3-3.5 m: the size card uses it at scale 0.7 next to `small_car` at 1.37 (Mini, 3.05 m), so keep the body length close to 800 units.
- Shots: s003, s004, s015, s016, s017, s019, s020, s023, s024, s025, s029, s042, s043, s044, s045, s053, s055, s058, s059, s063, s064, s084, s085, s088, s090, s091, s129, s130, s133, s134, s136, s137, s138, s139, s142, s143, s144, s148, s149, s150, s151, s152, s156, s157, s166, s174, s175, s179, s180, s189, s194, s195, s197, s198, s200, s203, s205, s211, s226, s227, s228, s231, s232, s233, s241, s246, s247, s248, s249, s250, s251, s252, s253, s254, s255, s256, s259, s260, s261, s263 (80 shots)
- **DONE** (illustrator, 2026-10-27): `assets/library/leopard_seal.json`, preview `assets/previews/029-leopard-seal-under-the-ice-assets-seal.png`. actual extents x -404..414, y -72..110; head x +160..+414. One shared head/palette/spot set across the whole family.

## `adelie_penguin`
**Creature.** Adelie penguin standing.

- Look: Black back and head, white front, the distinctive **white eye ring**, short black beak with a little feathered base, short flippers, pink feet. Plain realistic-cartoon, not a cute mascot (no blush, no big eyes), per the CD's kid-appeal note.
- Facing / anchor / size: Facing right, anchor bottom-centre, about 140 x 300.
- Notes: Used in rows of up to 18 at scale 0.34-0.44, so it must read tiny.
- Shots: s037, s038, s039, s040, s041, s042, s043, s044, s045, s046, s047, s048, s051, s052, s053, s054, s055, s056, s057, s058, s059, s063, s064, s065, s066, s067, s158 (27 shots)
- **DONE** (illustrator, 2026-10-27): `assets/library/adelie_penguin.json`, preview `assets/previews/029-leopard-seal-under-the-ice-assets-2.png`. x -76..84, y -290..0.

## `leopard_seal_head_rising`
**Creature.** Leopard seal head and neck rising vertically out of water (at a dinghy side, a crack, a pool).

- Look: Same reptilian head as `leopard_seal`, seen in profile, snout pointing right and slightly up, mouth closed with the long grin line, spotted throat. The neck goes straight down into the water: draw a small water ripple ring (pale `#bfe6ff` ellipse arcs) at the base so it reads as emerging, never as a cut-off neck.
- Facing / anchor / size: Facing right, anchor = waterline centre of the neck (0,0); about 380 x 440 (x -150..+230, y -420..+20); snout tip about (+220, -330).
- Notes: Used from scale 0.32 (in the sepia card) up to 1.6 (The Head close-up, waterline at the bottom of frame).
- Shots: s007, s018, s082, s092, s096, s099, s103, s104, s108, s110, s112, s146, s147, s167, s168, s182, s183, s184, s196, s208, s233 (21 shots)
- **DONE** (illustrator, 2026-10-27): `assets/library/leopard_seal_head_rising.json`, preview `assets/previews/029-leopard-seal-under-the-ice-assets-seal.png`. x -180..224, y -366..+36 (head top a little lower than -420); snout tip (+222,-330).

## `leopard_seal_hauled_out`
**Creature.** Leopard seal lying on ice (or on a marina pontoon), resting.

- Look: Same design as `leopard_seal` (slate back, pale spotted belly, long reptile head) lying flat on its belly, head slightly raised and turned toward the viewer's right, mouth closed, front flippers flat on the ground. No sleepy/cute face.
- Facing / anchor / size: Facing right, anchor bottom-centre (belly contact line y=0), about 760 x 190 (x -380..380, y -190..0).
- Notes: Also stands in for sleeping males (s239-s240, with dye marks and 'z' drawn by the director) and the 1916 seal chasing across the floe (sepia scenes).
- Shots: s002, s012, s036, s071, s072, s073, s074, s075, s076, s077, s078, s081, s083, s100, s114, s238, s239 (17 shots)
- **DONE** (illustrator, 2026-10-27): `assets/library/leopard_seal_hauled_out.json`, preview `assets/previews/029-leopard-seal-under-the-ice-assets-seal.png`. x -381..382, y -185..0.

## `zodiac_boat`
**Prop / boat.** Antarctic expedition inflatable boat (Zodiac type).

- Look: Larger than the dinghy: orange-red `#e0571b` and grey tubes, black rubber floor, an outboard motor at the stern (left), a small grab line along the tubes.
- Facing / anchor / size: Facing right, anchor = waterline centre, about 620 x 160 (x -320..300, y -110..+50); inner floor/seat at y -70 (Doug sits or stands in it, drawn before the boat).
- Shots: s099, s100, s108, s109, s110, s111, s112, s113, s114, s121, s122, s124, s125, s126, s248 (15 shots)
- **DONE** (illustrator, 2026-10-27): `assets/library/zodiac_boat.json`, preview `assets/previews/029-leopard-seal-under-the-ice-assets-2.png`. x -344..302 (outboard), y -148 (bow tip)..+34.

## `explorer_1916_skis`
**Human (crude tier).** Thomas Orde-Lees skiing.

- Look: The same 1916 man on long wooden skis, leaning forward mid-stride with one ski pole in each hand.
- Facing / anchor / size: Facing right, anchor hips, skis at y +150..+166 (x -220..+280). Flipped to face left in most shots.
- Shots: s002, s007, s008, s011, s012, s013, s014, s015, s016, s017, s018, s019, s020 (13 shots)
- **DONE** (illustrator, 2026-10-27): `assets/library/explorer_1916_skis.json`, preview `assets/previews/029-leopard-seal-under-the-ice-assets-3.png`. skis y +150..+168, x -222..+286.

## `music_note`
**Annotation.** A single black eighth-note music note.

- Look: Bold black note head and stem with one flag, thick outline so it reads at 30 px on blue water.
- Facing / anchor / size: Centre anchor, about 80 x 120.
- Notes: Used in drifting lines of 2-5 for the seal's song and Doug humming.
- Shots: s004, s226, s227, s228, s232, s239, s246, s251, s252, s253, s254, s255, s256 (13 shots)
- **DONE** (illustrator, 2026-10-27): `assets/library/music_note.json`, preview `assets/previews/029-leopard-seal-under-the-ice-assets-2.png`. about 100 x 125 with a white halo.

## `photographer_diver`
**Human (crude tier).** Underwater wildlife photographer (Paul Nicklen stand-in, not a likeness).

- Look: Same tier as `diver`: dark drysuit, mask, tank, fins, **no red cap**, holding a big boxy underwater camera housing forward in both hands with two strobe arms. `auto_ink: true`.
- Facing / anchor / size: Facing right, anchor hips, camera front at about (+240, -120).
- Notes: The seal's open mouth closes around the camera end in s135, so keep the camera clearly separate from the head.
- Shots: s129, s130, s131, s132, s133, s135, s136, s137, s138, s139, s143, s144, s145 (13 shots)
- **DONE** (illustrator, 2026-10-27): `assets/library/photographer_diver.json`, preview `assets/previews/029-leopard-seal-under-the-ice-assets-3.png`. dome port at about (+248,-120), strobes up to y -258, clear of the head.

## `adelie_penguin_swimming`
**Creature.** Adelie penguin swimming fast underwater, horizontal.

- Look: Same colours as `adelie_penguin`, streamlined horizontal body, flippers swept back, a couple of small bubbles. Alive and darting, never caught or limp.
- Facing / anchor / size: Facing right, centre anchor, about 300 x 110.
- Shots: s041, s059, s128, s130, s138, s139, s144, s145, s149, s150, s156, s211 (12 shots)
- **DONE** (illustrator, 2026-10-27): `assets/library/adelie_penguin_swimming.json`, preview `assets/previews/029-leopard-seal-under-the-ice-assets-2.png`. body x -140..180, y -42..38; bubbles/speed lines out to x -217.

## `fur_seal_pup`
**Creature.** Antarctic fur seal pup sitting up on its front flippers.

- Look: Small dark brown-black pup with a slightly paler muzzle, pointed snout, small ear flaps, small dark eyes (not big cute eyes).
- Facing / anchor / size: Facing right, anchor bottom-centre, about 140 x 160.
- Notes: Used in groups of 10 and sitting in cinema seats (scale 0.42).
- Shots: s182, s183, s184, s185, s187, s188, s191, s192, s193, s194, s195, s197 (12 shots)
- **DONE** (illustrator, 2026-10-27): `assets/library/fur_seal_pup.json`, preview `assets/previews/029-leopard-seal-under-the-ice-assets-2.png`. x -68..98, y -160..0.

## `crabeater_seal`
**Creature.** Crabeater seal hauled out on pack ice, with leopard seal scars.

- Look: Slim, pale cream-silver to light tan seal `#d8cdb4` (darker back), long dog-like snout, small dark eye. On its side: **three long pale lines in a parallel group** (two of them close together as a pair) drawn as simple lighter `#f3eee2` stripes with a thin grey edge. Never red, never wounds.
- Facing / anchor / size: Facing right, anchor bottom-centre, about 560 x 150.
- Notes: Also needed big (scale 1.3) for the scar close-up.
- Shots: s199, s200, s201, s202, s203, s204, s205, s206, s207, s208, s209, s210 (12 shots)
- **DONE** (illustrator, 2026-10-27): `assets/library/crabeater_seal.json`, preview `assets/previews/029-leopard-seal-under-the-ice-assets-2.png`. x -286..287, y -106..0 (slim body, so lower than 150).

## `marina_pontoon`
**Place / prop.** Floating marina pontoon (Westhaven).

- Look: Long low grey timber/concrete deck on black float blocks, a couple of cleats, two short piles with white caps rising behind.
- Facing / anchor / size: Side view, anchor = waterline centre, about 960 wide; deck top at y -40; piles up to y -160.
- Notes: Owha lies on it at scale 1.6 (deck top at canvas y 696).
- Shots: s071, s072, s073, s074, s077, s078, s079, s081, s082, s083, s092 (11 shots)
- **DONE** (illustrator, 2026-10-27): `assets/library/marina_pontoon.json`, preview `assets/previews/029-leopard-seal-under-the-ice-assets-3.png`. x -492..492; deck top y -44; piles to -164.

## `canvas_tent`
**Prop.** Old canvas ridge tent (1916 camp).

- Look: Off-white `#ece3cf` canvas ridge tent with slightly sagging sides, a darker door flap, two guy ropes to pegs.
- Facing / anchor / size: Anchor bottom-centre, about 280 x 170.
- Shots: s002, s007, s008, s010, s011, s012, s013, s014, s021, s022 (10 shots)
- **DONE** (illustrator, 2026-10-27): `assets/library/canvas_tent.json`, preview `assets/previews/029-leopard-seal-under-the-ice-assets-3.png`. about 300 x 185.

## `new_zealand_map`
**Map.** Flat map of New Zealand (world_map style).

- Look: Flat green North and South Islands (and Stewart Island) with dark outline, light-blue `#bfe6ff` sea, black frame, no labels.
- Facing / anchor / size: Centre anchor, frame 600 x 700. Projection so the director's dots land: x = (lon - 172.5) x 46, y = (lat S - 41.25) x 48 (Auckland about (+104,-211), Whangarei (+84,-265), Tauranga/Bay of Plenty (+169,-171), Dunedin (-92,+222)).
- Shots: s084, s085, s086, s087, s088, s089, s090, s091, s098 (9 shots)
- **DONE** (illustrator, 2026-10-27): `assets/library/new_zealand_map.json`, preview `assets/previews/029-leopard-seal-under-the-ice-assets-3.png`. frame 600 x 700 with the requested projection; director dots all land on land.

## `leopard_seal_gape`
**Creature.** Leopard seal on ice doing the open-mouth threat display (looks like a huge grin or yawn).

- Look: Hauled-out leopard seal with head and chest raised and the mouth gaping very wide toward the viewer's right: dark `#7a0d0d` mouth, pale pink tongue, a row of pale teeth with the two canines visible (simple, not bloody). It should read as a tourist's 'smiling seal' photo AND as a warning. Menacing, reptilian, no cute eyes.
- Facing / anchor / size: Facing right, anchor bottom-centre, about 760 x 380 (x -380..380, y -380..0); open mouth around (+260, -280).
- Notes: Used big (scale 1.1-1.3) as the tourist photo and the selfie partner.
- Shots: s101, s102, s105, s119, s120, s121, s122, s124 (8 shots)
- **DONE** (illustrator, 2026-10-27): `assets/library/leopard_seal_gape.json`, preview `assets/previews/029-leopard-seal-under-the-ice-assets-seal.png`. x -381..345, y -387..0; mouth centre about (+260,-280).
- **FIXED round 2** (illustrator, 2026-10-27, art review fix 1): both jaws closed with their own black outlines and rounded snout/chin tips; the mouth interior is set back behind the tips with a concave black front edge (background shows through at the front); the tongue is raised so it reads; `#7a0d0d` and tooth count unchanged. Anchor and bbox unchanged (x -379..346, y -384..0); mouth centre still about (+260,-280). Preview `assets/previews/029-leopard-seal-under-the-ice-assets-fixes.png` (cell crops at default scale, so it was rendered at 0.5) plus `assets/previews/029-leopard-seal-under-the-ice-seal-mouths.png` (at 1.3 on ice/water).

## `leopard_seal_jaw_diagram`
**Diagram.** Side-on diagram of the leopard seal's closed jaws showing the krill sieve.

- Look: Clean textbook-style head outline (pale grey fill, black outline), mouth closed, lips cut away to show the teeth: two canines at the front and, further back, the cheek teeth, each with **three sharp points**, interlocking upper and lower so the gaps form a grid/sieve. No eye detail needed beyond a small dot.
- Facing / anchor / size: Facing right, centre anchor, about 900 x 500; the interlocking back teeth centred at local (+80, +40), canines at about (+330, +30).
- Notes: The director draws arrows and a red ring on the interlock zone, so keep that area clear of other detail.
- Shots: s155, s161, s162, s163, s164, s169, s172, s173 (8 shots)
- **DONE** (illustrator, 2026-10-27): `assets/library/leopard_seal_jaw_diagram.json`, preview `assets/previews/029-leopard-seal-under-the-ice-assets-seal.png`. about 905 x 430 (y -248..183); sieve centred ~(+80,+40), canines ~(+310..+378, +2..+92); interlock zone kept clear.
- **FIXED round 2** (illustrator, 2026-10-27, art review fix 2): the dashed flat cut edge is gone. The head ends in a closed, rounded back of skull/neck curve (x -452..456, about 910 wide, unchanged). The canines are now the longest teeth: about 130 tall versus 80 for the cheek teeth (1.6x), curved and sharp. The upper canine is at x +270..+324 with its tip at (+278,+100); the lower canine sits in front at x +330..+384 with its tip at (+346,-58). Both roots are tucked into pink gum bulges. The canines moved about 30 units back from +310..+378. The interlock zone at (+80,+40) is untouched, the whisker dots moved up 40 to clear the lower canine tip, and there is no wordart or red ring on the canines. Preview `assets/previews/029-leopard-seal-under-the-ice-assets-fixes.png` plus `assets/previews/029-leopard-seal-under-the-ice-jaw-diagram-s161.png`, which shows it at the s161 placement (860,520,1.1) and at 0.4.

## `krill_cloud`
**Creature swarm.** A dense swarm of Antarctic krill.

- Look: Dozens of tiny pink-orange `#f08a7a` curved shrimp shapes (some with a black eye dot) over a soft pink spray cloud; denser in the middle, loose at the edges, translucent enough that Doug drawn inside it still reads.
- Facing / anchor / size: Centre anchor, about 700 x 420.
- Shots: s154, s159, s160, s176, s177, s178, s181 (7 shots)
- **DONE** (illustrator, 2026-10-27): `assets/library/krill_cloud.json`, preview `assets/previews/029-leopard-seal-under-the-ice-assets-2.png`. 700 x 400.

## `doug_skis`
**Worn prop (Doug).** Doug's cross-country skis.

- Look: Two long pale-wood skis with turned-up tips at the right, side by side under his feet. No poles (his arms stay free for wave/thumbs up).
- Facing / anchor / size: Anchor = Doug's hips at scale 1; skis lie at y +150..+166 under the feet, x -220..+280. Listed after Doug at the same x/y/scale.
- Shots: s006, s026, s027, s028, s029, s248 (6 shots)
- **DONE** (illustrator, 2026-10-27): `assets/library/doug_skis.json`, preview `assets/previews/029-leopard-seal-under-the-ice-assets-3.png`. checked on Doug stand pose.

## `penguin_costume`
**Worn prop (Doug).** Doug's homemade penguin costume.

- Look: Same construction as `seal_costume`: black felt sack suit with a lumpy white belly panel, two floppy black felt flipper mitts sewn on the sides, orange felt feet over his shoes, a black hood ring bunched at the neck. Head, face and red cap fully visible (art bible worn-prop rule).
- Facing / anchor / size: Anchor = Doug's hips at scale 1, bbox like `seal_costume` (x -136..136, y -226..186).
- Shots: s062, s063, s064, s065, s248 (5 shots)
- **DONE** (illustrator, 2026-10-27): `assets/library/penguin_costume.json`, preview `assets/previews/029-leopard-seal-under-the-ice-assets-3.png`. x -142..142, y -194..182; checked on stand/wave/float.

## `inflatable_dinghy`
**Prop / boat.** Small inflatable tender dinghy (marina type).

- Look: Grey `#8a9096` round tubes with a darker rub strip, pointed bow at the right, flat transom at the left, one wooden seat inside, two short oars resting in it.
- Facing / anchor / size: Facing right, anchor = waterline centre; about 440 x 130 (x -220..220, y -90..+40); seat top at y -60 (Doug sits there with `sit`).
- Notes: Also lies upside down (rotate 150) for 'capsized', and sits on `car_trailer`.
- Shots: s068, s069, s070, s082, s092 (5 shots)
- **DONE** (illustrator, 2026-10-27): `assets/library/inflatable_dinghy.json`, preview `assets/previews/029-leopard-seal-under-the-ice-assets-2.png`. x -228..222, y -128 (oar handles)..+16; seat at y -60 hidden behind the tube.

## `blubber_stove_pot`
**Prop.** 1916 blubber stove with a cooking pot.

- Look: A crude stove made from an old tin drum with a small stove pipe, a dented metal pot on top, a small orange flame and a little grey smoke. No meat visible.
- Facing / anchor / size: Anchor bottom-centre, about 200 x 220.
- Shots: s032, s033, s034, s035 (4 shots)
- **DONE** (illustrator, 2026-10-27): `assets/library/blubber_stove_pot.json`, preview `assets/previews/029-leopard-seal-under-the-ice-assets-3.png`. stove 170 x 190, smoke to y -304.

## `explorer_1916`
**Human (crude tier).** Generic Shackleton-expedition man, standing.

- Look: Doug's crude tier (5 px lines, round head with grey crescent), **no red cap**: knitted balaclava or woollen cap, bushy beard, thick woollen jumper, heavy trousers and boots. Neutral face. `auto_ink: true`.
- Facing / anchor / size: Facing right, anchor hips (0,0), feet +150.
- Notes: Used in the sepia 1916 scenes, never a likeness of a real person.
- Shots: s032, s033, s034, s035 (4 shots)
- **DONE** (illustrator, 2026-10-27): `assets/library/explorer_1916.json`, preview `assets/previews/029-leopard-seal-under-the-ice-assets-3.png`. auto_ink; built on Doug rig proportions (feet +150).

## `bowling_lane`
**Prop / diagram.** A bowling lane seen from above.

- Look: Long pale-wood strip with grain lines, gutters on both sides, a foul line at the left end, the target arrows, and ten white pins in their triangle at the right end.
- Facing / anchor / size: Horizontal, centre anchor, about 1000 x 120; foul line at x -470, head pin at about x +440 (foul line to head pin = 18 m).
- Shots: s040, s048, s049, s050 (4 shots)
- **DONE** (illustrator, 2026-10-27): `assets/library/bowling_lane.json`, preview `assets/previews/029-leopard-seal-under-the-ice-assets-3.png`. 1000 x 124; foul line x -470, head pin x +440.

## `inflatable_dinghy_swamped`
**Prop / boat.** The same dinghy punctured and swamped.

- Look: Front tube sagging and wrinkled flat, the hull half under water and tilted, water inside, a little puncture tear (no teeth).
- Facing / anchor / size: Anchor = waterline centre (or the sea floor), about 440 x 100.
- Shots: s073, s079, s080, s093 (4 shots)
- **DONE** (illustrator, 2026-10-27): `assets/library/inflatable_dinghy_swamped.json`, preview `assets/previews/029-leopard-seal-under-the-ice-assets-2.png`. x -242..242, y -68..+42.

## `leopard_seal_canine`
**Prop / diagram.** One leopard seal canine tooth on its own.

- Look: Long, curved, sharply pointed ivory tooth `#f4ecd8` with grey shading on one side and a duller root half at the bottom (diagram style, no gum, no blood).
- Facing / anchor / size: Pointing up, centre anchor, about 110 x 300 (tip at y -150).
- Notes: Shown at scale 1.4-1.6 beside `us_quarter`.
- Shots: s106, s107, s174 (3 shots)
- **DONE** (illustrator, 2026-10-27): `assets/library/leopard_seal_canine.json`, preview `assets/previews/029-leopard-seal-under-the-ice-assets-seal.png`. x -40..54, y -152..150, tip at y -150.
- **FIXED round 2** (illustrator, 2026-10-27, art review fix 3): redrawn as a slim, sabre-curved fang. The tip at (-54,-150) bends to the left, the crown is `#f4ecd8` with grey on the inside (concave) curve, and the root is smooth, duller tan, tapering, with no bands. There is one faint gum line at y 0. Centre anchor, x -54..40, y -150..148 (about 95 x 300). Preview `assets/previews/029-leopard-seal-under-the-ice-assets-fixes.png`.

## `boat_fender_bitten`
**Prop.** Boat fender with bite holes.

- Look: White-and-blue cylindrical inflatable boat fender with a rope through the top eye and two crescent-shaped puncture holes (dark, no red).
- Facing / anchor / size: Vertical, centre anchor, about 120 x 280.
- Shots: s079, s080 (2 shots)
- **DONE** (illustrator, 2026-10-27): `assets/library/boat_fender_bitten.json`, preview `assets/previews/029-leopard-seal-under-the-ice-assets-2.png`. x -62..62, y -212 (rope)..126.
- **FIXED round 2** (illustrator, 2026-10-27, art review fix 4): the stacked chevrons are replaced by two dark crescent-slit punctures side by side on a diagonal, at (-20,-14) and (+20,+14). Each one has a jagged pale rim and short wrinkle lines, plus two dent lines across the vinyl. No red. Anchor and bbox unchanged. Preview `assets/previews/029-leopard-seal-under-the-ice-assets-fixes.png` (checked at 0.6 and 1.6).

## `leopard_seal_open`
**Creature.** The same swimming leopard seal with the mouth wide open (lunge / gulp).

- Look: Identical body, bbox and anchor to `leopard_seal`; the lower jaw drops to show a dark `#7a0d0d` mouth interior. Teeth are a few small simple pale nubs only, no detailed fangs (it closes over a photographer's camera in s135, which must stay non-graphic; also used for the krill gulp).
- Facing / anchor / size: Facing right, centre anchor, same 800 x 220 bbox; mouth gap at about x +300..+400, y -40..+40.
- Shots: s135, s178 (2 shots)
- **DONE** (illustrator, 2026-10-27): `assets/library/leopard_seal_open.json`, preview `assets/previews/029-leopard-seal-under-the-ice-assets-seal.png`. same body/bbox; mouth gap x ~+300..+410, y -45..+45; small nub teeth only.
- **FIXED round 2** (illustrator, 2026-10-27, art review fix 1): same jaw outline, rounded tips and set-back concave mouth edge as `_gape`; teeth unchanged. Body, anchor and bbox unchanged; gap still x +300..+410, y -45..+45. Preview `assets/previews/029-leopard-seal-under-the-ice-assets-fixes.png` plus `assets/previews/029-leopard-seal-under-the-ice-seal-mouths.png` (at 1.4 on surface water).

## `cinema_seat`
**Prop.** One cinema seat, front view.

- Look: Red velvet seat and back with dark armrests and a seat cushion folded down; seat cushion top at about y -90.
- Facing / anchor / size: Anchor bottom-centre, about 140 x 180.
- Notes: A row of ten; fur seal pups sit in them (s191-s192).
- Shots: s192, s193 (2 shots)
- **DONE** (illustrator, 2026-10-27): `assets/library/cinema_seat.json`, preview `assets/previews/029-leopard-seal-under-the-ice-assets-3.png`. about 168 x 182; cushion top y -90.

## `quad_bike_rider`
**Vehicle + human.** Biologist on a quad bike crossing the ice (Tracey Rogers stand-in, not a likeness).

- Look: Red ATV quad bike, side view, chunky tyres, rear rack with a small box; a crude-tier stick woman (no cap, dark hair, warm jacket) seated on it, hands on the bars. Rider `auto_ink`.
- Facing / anchor / size: Facing right, anchor bottom-centre (tyre bottoms), about 440 x 430.
- Shots: s236, s237 (2 shots)
- **DONE** (illustrator, 2026-10-27): `assets/library/quad_bike_rider.json`, preview `assets/previews/029-leopard-seal-under-the-ice-assets-3.png`. x -226..238, y -453..0.

## `endurance_wreck`
**Place / prop.** Shackleton's ship Endurance crushed in the pack ice.

- Look: Dark wooden three-masted barquentine hull tilted steeply, half buried in jumbled pack-ice blocks, masts snapped and leaning, loose rigging lines. Plain colours (the card is sepia-framed).
- Facing / anchor / size: Anchor bottom-centre on the ice line, about 700 x 550.
- Shots: s010 (1 shots)
- **DONE** (illustrator, 2026-10-27): `assets/library/endurance_wreck.json`, preview `assets/previews/029-leopard-seal-under-the-ice-assets-3.png`. x -362..362, y -522..0 (ice strip to +40).

## `explorer_1916_rifle`
**Human (crude tier).** Frank Wild running out with a rifle.

- Look: The same 1916 man running, holding a rifle diagonally across his chest, muzzle pointing UP (not aimed, no shot, no muzzle flash).
- Facing / anchor / size: Facing right, anchor hips.
- Notes: One shot only (s021); the next shot cuts away before anything happens (brief policy note).
- Shots: s021 (1 shots)
- **DONE** (illustrator, 2026-10-27): `assets/library/explorer_1916_rifle.json`, preview `assets/previews/029-leopard-seal-under-the-ice-assets-3.png`. muzzle points up-right, no flash.
- **FIXED round 2** (illustrator, 2026-10-27, art review fix 5): the rifle is carried across the chest at about 72 degrees, with the butt at the front hip (+40,+10) and the muzzle beside the back shoulder above head height (-68,-314). Both mittens are on it (grip at the chest, fore-end by the back shoulder) and there is no flash. Anchor unchanged (hips). Extents changed from x -104..183, y -307..93 to x -104..156, y -314..93, because the muzzle no longer sticks out to the right. Preview `assets/previews/029-leopard-seal-under-the-ice-assets-fixes.png`.

## `penguin_costume_flat`
**Prop (death beat).** The empty penguin costume floating flat on the water after death 236.

- Look: Deflated black-and-white felt sack lying horizontally, flipper mitts flopped, orange feet at the left, hood end at the right. Waterline across its middle (it floats).
- Facing / anchor / size: Centre anchor, about 480 x 180.
- Notes: The red cap (`doug_cap`) is placed on top of it by the director.
- Shots: s067 (1 shots)
- **DONE** (illustrator, 2026-10-27): `assets/library/penguin_costume_flat.json`, preview `assets/previews/029-leopard-seal-under-the-ice-assets-3.png`. about 510 x 200, waterline at y 0.

## `zodiac_boat_wrapped`
**Prop / boat.** The Zodiac with Palmer Station's extra protective layer.

- Look: Same boat, but every tube wrapped in a thick extra black rubber skin with visible seams/straps, so it reads as 'armoured'.
- Facing / anchor / size: Same anchor and bbox as `zodiac_boat`.
- Shots: s111 (1 shots)
- **DONE** (illustrator, 2026-10-27): `assets/library/zodiac_boat_wrapped.json`, preview `assets/previews/029-leopard-seal-under-the-ice-assets-2.png`. same bbox as zodiac_boat.

## `zodiac_boat_wrecked`
**Prop / boat.** The Zodiac bitten through and destroyed (2015 Palmer Station).

- Look: Tubes collapsed and wrinkled, bow sunk, outboard tilted up, mostly under the waterline. No teeth or bite marks shown, just wreckage.
- Facing / anchor / size: Same anchor, about 620 x 110.
- Shots: s113 (1 shots)
- **DONE** (illustrator, 2026-10-27): `assets/library/zodiac_boat_wrecked.json`, preview `assets/previews/029-leopard-seal-under-the-ice-assets-2.png`. x -369..322, y -99..+58.

## `selfie_stick_phone`
**Prop.** Phone on an extended selfie stick.

- Look: Black telescopic stick with a small grip, phone clamped at the far end, screen facing back toward Doug.
- Facing / anchor / size: Anchor = grip (0,0), stick running up and right to the phone at about (+230,-230).
- Shots: s122 (1 shots)
- **DONE** (illustrator, 2026-10-27): `assets/library/selfie_stick_phone.json`, preview `assets/previews/029-leopard-seal-under-the-ice-assets-3.png`. phone centre (+236,-236).

## `pasta_strainer`
**Prop.** Kitchen pasta strainer / colander.

- Look: Silver metal bowl, side view, with rows of round holes, two side handles and a ring foot.
- Facing / anchor / size: Centre anchor, about 360 x 220.
- Shots: s164 (1 shots)
- **DONE** (illustrator, 2026-10-27): `assets/library/pasta_strainer.json`, preview `assets/previews/029-leopard-seal-under-the-ice-assets-3.png`. about 370 x 195.

## `vacuum_cleaner`
**Prop.** Household canister vacuum cleaner.

- Look: Red canister body on small wheels, grey hose curling up and over to a wand and floor head on the right.
- Facing / anchor / size: Anchor bottom-centre, about 420 x 300.
- Notes: The 'quietly, a vacuum cleaner' gag (s175).
- Shots: s175 (1 shots)
- **DONE** (illustrator, 2026-10-27): `assets/library/vacuum_cleaner.json`, preview `assets/previews/029-leopard-seal-under-the-ice-assets-3.png`. about 434 x 284.
