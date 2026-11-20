# 053 asset requests (director, 2026-11-20)

43 new drawings. The shotlist already places them using the anchors and footprints below (local units, scale 1). Please keep
those, or tell me what changed and I'll re-place them. I checked every shot with grey placeholder boxes of exactly these
footprints (`build/preview.py`), so a drawing that grows much past its box will hit the HUD, the caption bar or a neighbour.

**Tiers.** Plants, places and diagrams use the detailed tier: layered fills, interior shading, texture strokes 2-3, outlines 3-5.
Humans use the crude tier: Doug's line weight, `auto_ink`, and `keep_ink` on white face and hand fills. Everything faces RIGHT
unless noted; the shotlist flips them.

**Safety and tone (brief section 7) come first:**
- No blisters, rashes, burns, wounds, vomit or drips of anything that reads as a body fluid. Sap is clean white beads, venom is
  one tiny pale-yellow droplet.
- Plants stay botanical and plain. No faces, no smiles, no googly eyes on any plant, vegetable or fruit (flowers and berries
  already pull toward a kids' nature show; the channel is not made for kids).
- Nothing in these drawings should work as an identification key. Draw each plant recognisably but simply; no labelled
  "how to tell it apart" details.

**HUD.** Every shot carries the death counter (size-44 label at 1590,162) and the CONTACT meter under it: the `contact_dial`
icon at scale 0.36 with its pivot at about (1257, 252), and a fixed-width size-28 label "CONTACT: ..." centred at (1590, 238).
Together they fill about x 1205-1860, y 110-275. Tall drawings are placed so they stay below y 290 on that side.

**Reused from the library (no work needed):** `field_guide` (closed, item 1 title), `narrator_hand_pencil`, `cartoon_brain`,
`north_america_map`, `britain_map`, `europe_map`, `usa_map`, `pnw_map_states`, `australia_map`, `picnic_basket`, `picnic_blanket`,
`campfire`, `steam_wisps`, `wooden_spoon`, `stew_bowl`, `dinner_plate`, `shovel`, `plastic_bag`, `case_file`, `gravestone`,
`watering_can`, `magnifying_glass`, `heart_icon`, `heart_monitor`, `cow`, `dairy_cow`, `scientist`, `scientist_woman`,
`victorian_woman` (1810s settler), `deer_fence`, `vial`, `nerve_doorbell_diagram` (atropine "tape over a doorbell"), `eye_icon`,
`thermometer`, `chalkboard`, `rabbit` (the hare), `bat_hanging`, `cartoon_bone`, `compact_camera`, `front_door`, `clock`,
`small_car`, `small_car_driving` (Doug shows through its open window), `minivan`, `pickup_truck`, `city_bus`, `angry_sun`,
`medicine_bottle_plain`, `teaspoon`, `upright_piano`, `tent`, `small_table`, `honeybee`, `honey_jar`, `wild_honeycomb`, `calendar`,
`journal_paper`, `bp_cuff_arm`, `bucket`, `folding_stool`, `sun_hat` (Doug the settler), `microscope`, `doug_cap`, `fingertip`,
`basketball_hoop`, `oak_tree`, `the_target`, `umbrella_open`, `rainforest_tree`, `tree_fern`, `beanbag_chair`, `ruler`,
`garden_spider`, `cone_snail`, `specimen_tray`, `alarm_clock`, `record_book`, `beach_towel`, `old_book`, `street_sign_blank`,
`storm_cloud`, and the annotation set (`question_mark`, `exclamation_mark`, `warning_triangle`, `red_x`).

**Art director, two approvals** (both episode-only devices from the brief):
1. `field_guide_open_plants`: the plant edition of the field guide, an EDIBLE? relabel of `field_guide_open` (same geometry).
2. `contact_dial`: the CONTACT meter icon. The shotlist draws the black pointer itself (pivot to a wedge centre, length 100 x
   scale) and steps it one way: MOUTH (items 1-4), SECONDHAND at death 394, SKIN at death 395, NONE at "No touch." (s163), where
   the label turns red-on-pink `#ffd2cc` / `#e0201b`. The label is padded to a fixed width so a later state fully covers the
   earlier one on the switch shots (s079, s122, s163).

Doug's gear: survivals and the boss use the existing `sunburn` gear for "flat cartoon pink" (Nightshade s057-s060 flat red face,
Hogweed s138/s142/s143, Manchineel s183-s188), `sweat`, and `bandage` (Gympie). No new Doug gear.


## Illustrator status (2026-11-20): all done

All 44 drawings are in `assets/library/`. The 43 in the header counts carrot/parsnip/celery/parsley as one. Previews (git-ignored): `assets/previews/053-deadly-harmless-plants-assets.png`
(`asset-preview` at 0.4) and `assets/previews/053-deadly-harmless-plants-fitted-1.png` / `-fitted-2.png` (each fitted, with a small copy).
Generators: `episodes/053-deadly-harmless-plants/build/art/gen_a.py` to `gen_d.py`.

Deviations from the footprints (director, please check placement):
- `soup_pot`: the body stays inside the box, but the upright bail handle rises to **y -312** (box -230). This affects s015-s018, s123 and s161. Ask if you want it folded down.
- `caribbean_map`: Florida tip at (-230,-220) as asked. At a true aspect ratio the Lesser Antilles sit right of (+60,+40): **Tobago (+133,+58)**,
  Trinidad (+122,+73), Grenada (+115,+41), Martinique (+128,-10), Puerto Rico (+29,-81). A ring at about (+90,-20) r 130 covers PR to Trinidad.
- `hot_dog_stick`: sausage centred at (+140,0), not +150, to stay inside x ±200.
- `top_hat`: charcoal `#2a2a2e`, not pure black, so it reads on dark grounds.
- `nerve_switch_diagram`: ON at y -62 and OFF at y +61, both inside the tape strip zone, so the tape will cover them partly.
- Small overruns of 10 units or less: `yew_tree` x -386..382 / y -762, `manchineel_tree` x -416..409 / y -630 (spray glow only to -645),
  `water_hemlock` ±161, `celery` x -77..75 / y +192, `parsley` x -82..90, `beetroot` y +112, `oleander_shrub` ±234 / y -396,
  `yew_berry_closeup` needle tips y -251, `stone_church` x -366, `greek_soldier` y -348 / x +178, `greek_soldier_lying` crest y -122,
  `fibreglass_glove` fibres x -134 / y -167, `gympie_leaf_closeup` stalk x -328, `gympie_gympie` leaves up to y +18 below ground,
  `manchineel_branch_sap` a leaf tip at y +165.
- Kept points: yew seed (0,-50) / cup (+105,+55); nightshade cluster (+140,-330); manchineel cap hang (+260,-330) on bare branch;
  red band y -110..-80; sap beads at the 4 points; Trabzon (+250,+130); helmet rim y -294 (tested on Doug stand/point/thumbs_up).

---

## Episode devices

### `field_guide_open_plants` (s014-s018, s038-s040, s058-s059, s078-s079, s101-s102, s121-s122, s140-s142, s153-s154, s158-s160, s182-s188, s195) DONE
- Exactly `field_guide_open` (cover, pages, spine at x=0, dog-ears, coffee ring, red ribbon), anchor centre, x -280..280,
  y -180..202. Do not move any zone: the shotlist overlays the name, tick, YES/NO and the TOUCH? note at fixed local points.
- Right page prints **EDIBLE?** at (+90,-115) in the same lettering as FRIEND?, with the empty 44x44 tick box at (+205,-115).
- Left page: one small pressed flower (a flattened dried brown-green sprig, three leaves and one pale flower, held by two paper
  tape strips) inside x -250..-40, y +10..+150. Generic: not any of this episode's plants.
- Keep clear: name zone around (-140,-110) about 230x60, stamp zone around (+140,+50) about 220x120, and (+140,+140) for the red
  "TOUCH?" note (Hogweed).
- Used at 0.5-0.55 in the bottom corner and at 1.1-1.15 as a close-up.

### `contact_dial` (every shot from s002) DONE
- A crude MS Paint gauge: a half disc, flat side down. Pivot / anchor (0,0) at the centre of the flat base, radius 120.
- Four equal 45-degree wedges from left to right: MOUTH `#7cc25a`, SECONDHAND `#ffe24a`, SKIN `#f2a24a`, NONE `#e0201b`, each
  with a 6 px black outline, plus a black hub circle (r 12) at the pivot. Opaque fills (a later dial is drawn on top of an
  earlier one and must hide its pointer).
- No text and no pointer. Footprint x -130..130, y -130..10. It has to read at scale 0.36 (about 94 px wide).

## Item 1: Water Hemlock

### `water_hemlock` (s003-s005, s009-s012, s015-s019, s080, s194) DONE
- Water hemlock (*Cicuta maculata*), a tall wetland plant about 2 m: hollow green stems streaked and mottled purple, compound
  leaves with narrow toothed leaflets, and 3-5 flat-topped white umbrella clusters (compound umbels) at the top (y -720..-560).
- Anchor bottom-centre (ground), x -160..160, y -720..0. Used from 0.35 (icon row) to 0.85, and inside the s011 soup bag at 0.4.
- Must also read in the vegetable "family photo" (s010, s012) standing in the back row at 0.62.

### `water_hemlock_roots` (s005, s013, s019) DONE
- The underground part: a cluster of 4-6 thick, pale tan, finger-like tuberous roots fanning down from the stem base, and the
  stem base itself cut lengthwise showing the hollow chambers (horizontal cross-walls). No liquid, no drips.
- Anchor top-centre (0,0) = where the stem meets the soil; x -170..170, y 0..300. In s005 it sits under `water_hemlock` (0.62)
  at 1.1 in a soil cross-section; in s019 it lies on the marsh bank rotated 20 degrees.

### `nerve_brake_diagram` (s007, s008) DONE
- Crude biology card, transparent background, same family as `nerve_doorbell_diagram`: a lilac nerve cell body at left
  (about -480,0), a yellow axon wire running right, ending at a car brake pedal (black ribbed rubber pad on a grey arm, on a small
  grey floor plate) with the pad centred at about (+260,-40).
- No printed text (the shotlist puts GO and STOP labels above). Keep a clear gap under the pedal at (+250,+80), radius 55, for
  the cicutoxin blob that wedges under it, and keep x -520..-300, y -130..+70 simple: three green GO arrows are drawn there.
- Anchor centre; x -600..600, y -220..220.

### `carrot`, `parsnip`, `celery`, `parsley` (s010-s013) DONE
- Four plain supermarket vegetables standing upright like a portrait row. No faces.
- `carrot`: orange root (tip down) with a green feathery top; x -60..60, y -200..180.
- `parsnip`: cream root with a green leafy top, same size and pose as the carrot; x -60..60, y -200..180. Also used alone at 1.3
  in s013 beside the hemlock roots.
- `celery`: a bunch of pale green ribbed stalks with leaves at the top; x -70..70, y -220..180.
- `parsley`: a flat-leaf parsley bunch; x -80..80, y -150..120.
- Anchor centre for all four.

### `soup_pot` (s015-s018, s123, s161) DONE
- A steel camping pot with the wire bail handle up, sitting on the fire. Pale beige soup surface as an ellipse centred (0,-200),
  rx 140, ry 26, with a few orange vegetable chunks only near the rim. Keep the middle of the surface clear: Doug's cap floats
  there at the death (s018). No steam (the shotlist adds `steam_wisps`).
- Anchor bottom-centre; x -170..170, y -230..0. Placed at 1.0 on top of `campfire` at 1.3.

## Item 2: The Yew

### `yew_tree` (s020 silhouette, s022-s025, s031-s033, s038-s041, s194) DONE
- English yew: a dark, dense evergreen with a broad dome crown (base `#1f4a2a`, lighter `#2f6a3a` clumps, darker underside),
  a short thick reddish-brown flaky, fluted trunk visible below the crown (y -200..0), and a light sprinkle of small red berries.
- Anchor bottom-centre; x -380..380, y -760..0. Used at 0.25-0.85. Also a black silhouette with a purple glow in s020, so the
  outline alone has to say "tree".

### `stone_church` (s020, s022-s024, s038-s041) DONE
- A small grey stone village church: square tower on the left (crenellated top at y -600), nave with a slate roof to y -380,
  arched windows, a wooden door. Stones `#a8acb2`, roof `#5a6470`.
- Anchor bottom-centre; x -360..360, y -600..0. Used at 0.5-0.8.

### `yew_berry_closeup` (s034-s036, s080, s123, s161) DONE
- One berry, hero size: a bright red, glossy, fleshy cup (aril) open at the top, with an olive-brown/dark seed visibly sitting
  inside it. A short green twig with 3-4 flat dark needles at the upper left.
- The seed must show at about (0,-50) and the red cup body at about (+105,+55): the shotlist points a red arrow and "NOT SAFE"
  at the seed and a green arrow and "SAFE" at the cup.
- Anchor centre; x -220..220, y -220..220. Used at 1.6, and at 0.25-0.35 inside icon discs.

### `heart_wiring_diagram` (s028, s029) DONE
- Crude card, transparent background: a flat cartoon heart (pink-red `#e0556a`, not anatomical) with a yellow `#ffd21a` wire
  (black outline) looping through it, and a little yellow spark at the top.
- Keep three clear spots on the wire for the purple taxine blobs at (-120,-60), (0,+40) and (+120,-20).
- Anchor centre; x -300..300, y -260..260. Used at 1.15.

## Item 3: Deadly Nightshade

### `deadly_nightshade` (s042 silhouette, s043-s045, s056-s057, s080, s194) DONE
- *Atropa belladonna*, a leafy shrub about 1.2 m: dull green oval pointed leaves, a few dull purple-brown bell flowers, and glossy
  black berries, each sitting on a green star of five sepals, with a white highlight.
- Put a visible berry cluster around (+140,-330): the s044 arrow lands there.
- Anchor bottom-centre; x -280..280, y -560..0. Used at 0.3-1.0.

### `beetroot` (s051) DONE
- A deep red-purple round beet with a thin root tail, and red-veined green leaves up. Anchor centre; x -80..80, y -150..110.

### `top_hat` (s051, s052) DONE
- A plain tall black top hat with a grey band and a small blank paper card tucked in the band. Anchor centre; x -90..90, y -80..80.

### `venetian_lady` (s054, s055) DONE
- Crude tier like `victorian_woman` (Doug's line weight, big round head with grey crescent, `auto_ink`, `keep_ink` face):
  a 1500s Venetian court lady with her hair up in braids, a deep red `#9e2a2a` gown with a square neckline, gold trim and puffed
  sleeves. Her front hand is raised beside her eye holding a tiny glass dropper at about (+120,-200). Neutral face, normal eyes.
- Anchor hips (feet at +150); x -160..180, y -330..152. Used at 1.0 on sepia `#e9dcc0`.

### `hat_stand` (s058-s060) DONE
- A wooden hat stand: round base, turned pole, four curved hooks at the top (y -560), a plain grey bowler hat on top and a long
  scarf hanging from one hook. No face (Doug thinks it is the narrator; it must not look like a person).
- Anchor bottom-centre; x -110..110, y -620..0. Used at 0.85.

## Item 4: Oleander

### `oleander_shrub` (s061 silhouette, s062-s065, s078-s079, s194) DONE
- A dense rounded shrub of narrow, leathery, dark-green willow-like leaves, with many clusters of pink flowers and a few white.
- Anchor bottom-centre; x -220..220, y -380..0. Repeated along the freeway median at 0.42 (it must read that small), and at
  1.1-1.3 as a hero.

### `oleander_branch` (s066, s076-s078, s080, s123, s161) DONE
- A single branch: anchor (0,0) at the cut base on the left, extending right to x +420 (y -80..80), narrow dark leaves in threes
  and a pink flower cluster at the tip (+380,0). Used at 0.3-1.4, once rotated -20 through Doug's car window.

### `heart_pump_door_diagram` (s068, s070) DONE
- Crude heart-cell card, transparent background: a horizontal pink cell membrane band (`#f4c6c4`, darker edges) across y -40..+40,
  with a small grey revolving door (two crossed panels in a round frame, about 110 wide) set into the membrane at (0,0). Pale
  "outside" above, pale pink "inside" below. No printed text (the shotlist adds a PUMP label).
- Keep the door centre (0,0) clear for the jam blob, and keep the salt dots out of the drawing (the shotlist adds them).
- Anchor centre; x -380..380, y -220..220. Used at 1.2.

### `metronome` (s071) DONE
- A classic wooden pyramid metronome, front view, pendulum arm straight up (tip at (0,-230)) with a small sliding weight.
- Anchor bottom-centre; x -90..90, y -260..0. It stands on top of `upright_piano` (0.7) at 0.7; the narrator's pencil nudges the
  arm tip.

### `hot_dog_stick` (s072-s075, s077) DONE
- A long thin, fresh green-brown stick (an oleander twig, 2-3 narrow leaves near the handle end at left) with one plain
  sausage skewered near the right tip (+150,0). No bun.
- Anchor centre; x -200..200, y -70..70. Used at 0.7-2.0, flipped and rotated ±10 over the campfire.

## Item 5: Mad Honey

### `greek_soldier` (s084, s086, s087, s091) DONE
- Crude tier, `auto_ink`: an ancient Greek hoplite stick man with a bronze crested helmet (open face, neutral, face visible), a
  short red tunic and cloak, a round bronze shield on the back arm, and the front hand at (+148,-165) holding a small chunk of
  honeycomb. Also stands in for the general Xenophon (s086).
- Anchor hips (feet at +152); x -150..170, y -340..152. Used at 0.5-0.75, sometimes rotated ±12-18 degrees (dizzy).

### `greek_soldier_lying` (s085, s088, s090, s101, s102) DONE
- The same soldier flat on his back, eyes closed as simple curved lines (NOT X eyes: they all got up again), helmet tipped,
  shield flat beside him. Same convention as Doug's `on_back`: anchor hips, lowest points at +70, head to the left.
- x -330..180, y -110..70. Used at 0.45-0.5, eight at once across a hillside, some flipped.

### `greek_helmet_hat` (s101, s102) DONE
- Worn prop on the `hard_hat` convention: a crude bronze Greek helmet with a red crest perched on top of Doug's cap. Anchor =
  Doug's hips at scale 1, bottom rim at y -294 so the cap dome and brim stay visible below; x -110..110, y -400..-270.
- s101: worn on a standing Doug tilted 8 degrees. s102: lying on the ground beside him (rotate 80).

### `black_sea_map` (s084) DONE
- `world_map` style (flat green land, dark green outline, light-blue sea, white wave ticks, black frame, no labels): the Black
  Sea with Turkey's north coast, Crimea and the Caucasus coast.
- Anchor centre; x -480..480, y -300..300. Put the eastern Turkish Black Sea coast (Trabzon, about 39.7E 41.0N) at (+250,+130):
  the red dot goes there. Keep the sea around (0,-20) clear for a "BLACK SEA" label.

### `rhododendron_bush` (s092 silhouette, s093, s094) DONE
- A big rounded shrub with leathery dark-green leaves and large trusses of pink-purple flowers (*R. ponticum*) plus a few yellow
  trusses (*R. luteum*). Anchor bottom-centre; x -320..320, y -460..0. Used at 0.6-1.0, and as a silhouette in s092.

### `nerve_switch_diagram` (s095, s096) DONE
- Same family as `nerve_doorbell_diagram`: a lilac nerve cell at left, a yellow axon wire to a cream wall light-switch plate
  (100x160) at (+400,0) with the toggle UP, small printed "ON" above and "OFF" below the toggle.
- Keep the toggle readable under a beige tape strip the shotlist draws over x +360..+440, y -70..+70 (tape holding it ON).
- Anchor centre; x -560..560, y -200..200. Used at 1.0.

## Item 6: White Snakeroot

### `white_snakeroot` (s104, s108, s109, s114, s119, s194) DONE
- *Ageratina altissima*, a knee-to-waist-high woodland plant: opposite, toothed, heart-shaped leaves and flat-topped clusters of
  small fuzzy bright-white flowers on top. It must read on dusk orange `#e88a4a` and on cream.
- Anchor bottom-centre; x -200..200, y -420..0. Used at 0.42-0.8.

### `frontier_cabin` (s104, s105, s112, s117-s118, s120-s122) DONE
- An 1810s Indiana log cabin in summer, no snow: round logs with pale cut ends, a shake roof, a stone chimney with a wisp of
  smoke, a closed plank door and one small window.
- Anchor bottom-centre; x -340..340, y -520..0. Used at 0.35-0.75 (reads small on the sober Nancy Hanks Lincoln card).

### `milk_glass` (s105, s107, s109, s112, s116, s121, s123, s161) DONE
- The `water_glass` tumbler filled with opaque white milk (`#fbfbf5`, pale grey shading, a meniscus). Anchor centre;
  x -55..55, y -92..90. Used at 0.3 (in hands) to 2.0.

## Item 7: Giant Hogweed

### `giant_hogweed` (s124 silhouette, s126-s129, s131, s133, s139-s141, s161, s194) DONE
- A towering plant about 5 m: a thick green stem blotched with purple-red spots and coarse bristly hairs, huge jagged, deeply cut
  leaves at the base (out to ±380), and one giant flat-topped white umbrella flower head on top (y -1250..-1100, about 600 wide)
  with two smaller side heads.
- Anchor bottom-centre; x -380..380, y -1250..0. At 0.6 it is 750 px tall next to Doug at 0.25 (true scale: 5 m vs 1.8 m) and
  a 0.78 basketball hoop (3 m). Also a silhouette in s124.

## Item 8: Gympie-Gympie

### `gympie_gympie` (s143 silhouette, s144-s146, s148, s153, s154, s194) DONE
- *Dendrocnide moroides*, a rainforest shrub about 1.5 m: big, soft-looking, heart-shaped, serrated bright-green leaves with a pale
  fuzzy sheen (fine short hair strokes), and clusters of small mulberry-like purple-pink fruit.
- It stands on a dark green `#1d5e27` forest: use lighter greens (`#7cc25a` / `#9cd36a`) with a dark outline so it reads.
- Anchor bottom-centre; x -300..300, y -560..0. Used at 0.3-0.95.

### `gympie_leaf_closeup` (s147, s161) DONE
- One heart-shaped leaf filling the frame: serrated edge, midrib and veins, the surface covered in fine pale needle-like hairs
  (short white strokes). Anchor centre; x -320..320, y -260..260. Used at 1.4 on pale green `#cfe9c0`.

### `gympie_hair_closeup` (s149) DONE
- One magnified hair: a tall, glassy, pale silica needle (white / pale blue with a highlight line) rising from a bulbous base set
  in a green leaf-surface band at the bottom (y +220..+300), with a tiny pale-yellow venom droplet at the tip (0,-300). Do not draw
  it as a hollow tube (no source says hollow).
- Anchor centre; x -90..90, y -300..300. Used at 1.1.

### `fibreglass_glove` (s150) DONE
- A knitted glove made of pink fibreglass insulation fluff (`#f4a6b0`, darker `#e07c8c`), fingers spread, ribbed cuff, a few
  stiff prickly fibres sticking out. Empty glove, no hand. Anchor centre; x -130..130, y -150..150. Used at 1.4.

### `herbarium_sheet` (s156, s157) DONE
- An old museum herbarium sheet: a yellowed cream card with a pressed, flattened, dried brown-green heart-shaped leaf held down
  by small paper tape strips, a tiny blank label box at bottom right, faint age spots. It must read on dark brown `#3b2a17`.
- Anchor centre; x -150..150, y -210..210. Used at 1.2.

## Item 9: The Manchineel (boss)

### `manchineel_tree` (s002, s162 silhouette, s164-s166, s168, s170, s172, s176-s180, s182-s188, s190-s192, s194) DONE
- A friendly, round beach tree: a short, thick grey-brown trunk with a bright red painted band at about y -110..-80, a broad round
  crown of glossy bright-green oval leaves, and small yellow-green apples dotted in the crown. It has to look like a lovely place
  to sit.
- A low branch on the right, with the cap hang point at (+260,-330): the closing shots hang `doug_cap` there (s190-s192).
- Anchor bottom-centre; x -420..420, y -620..0, crown inside y -620. Used at 0.55-0.8 (at 0.8 the crown top lands at y 304, just
  under the HUD), on sunny, overcast, rainy and night beaches, and as a silhouette with a red glow in s162.

### `manchineel_apple` (s167, s173) DONE
- A small round green-yellow crab-apple-like fruit with a short stalk and one small leaf. Anchor centre; x -70..70, y -70..70.
  Used at 2.2 as a hero.

### `manchineel_apple_bitten` (s174, s175, s184, s185, s187) DONE
- The same fruit with one bite out of it (pale flesh). No drips or juice. Same anchor and footprint. Used at 0.3-0.7 (in a hand).

### `caribbean_map` (s166) DONE
- `world_map` style, no labels: Florida, the Gulf, Cuba, the Caribbean island arc, the Central American coast and the north coast
  of South America with Trinidad and Tobago.
- Anchor centre; x -500..500, y -320..320. Florida's southern tip at (-230,-220) (red dot) and the island arc around (+60,+40)
  (red ring). Please note Tobago's position in the description for later use.

### `manchineel_branch_sap` (s169) DONE
- A horizontal branch cutaway: bark texture, leaves at the left, a few twigs, two small green apples at the right, and clean white
  milky sap beads oozing at a leaf stalk (-300,-40), a twig tip (0,-60), a bark nick (+180,0) and a fruit stalk (+330,+60).
- Keep y -200..-170 clear across the top (LEAVES / TWIGS / BARK labels at x -290, 0, +260) and (+350,+145) clear for FRUIT.
- Anchor centre; x -420..420, y -160..160. Used at 1.4.
