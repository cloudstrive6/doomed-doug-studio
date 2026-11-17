# 050 asset requests (director, 2026-11-17)

53 new drawings. The shotlist already places them using the anchors, sizes and local coordinates below. Please keep
them, or tell me what changed and I'll re-place them. Creatures and places are the detailed tier (layered fills,
interior shading, outlines 3-5). Costumes are deadpan felt suits worn over Doug: anchor = Doug's hips (0,0), same
x/y/scale as the `doug` element, listed after him, and they leave his head, face and red cap fully visible.

**Kid-appeal risk is higher than usual on an octopus episode (brief section 7, decisions.md):** no octopus gets a smile,
blush, sparkles or big round cartoon eyes. Octopus eyes are smallish with a **horizontal bar-shaped pupil** under a
heavy lid, and they look calm and alien. The dumbo octopus is a pale deep-sea animal, not a mascot. **No gore:** the
man-of-war tentacles the blanket octopus carries are clean blue beaded strands (never torn ends), the seven-arm octopus
eats nothing on screen, no ink clouds, no severed arms anywhere.

Size budget: the HUD (DOUG DEATHS / DEPTH / ARMS) fills x 1300-1860, y 110-300 on every shot, so keep each drawing
within the sizes below. Large creatures are placed so that their tops stay at y ≥ 300 near the right side.

Reused from the library (no work needed): `yellow_submarine`, `rov`, `baited_camera_lander`, `research_ship`,
`portuguese_man_o_war`, `roving_coral_grouper`, `small_fish`, `crab`, `amphipod`, `coral_reef`, `seagrass`, `seashell`,
`world_map`, `pacific_map`, `australia_map`, `indonesia_map`, `ruler`, `fingertip`, `umbrella_open`, `bed`, `front_door`,
`walnut`, `balance_scale`, `magnifying_glass`, `diver`, `scientist`, `large_man`, `glass_jar`, `moon_jellyfish`,
`yellowfin_tuna`, `silver_fish`, `water_glass`, `calendar`, `trophy_cup`, `kitchen_timer`, `dinner_plate`, `thermometer`,
`heart_icon`, `the_target` (049, used here as a plain archery target), `brown_dog_sitting`, `sperm_whale`, `crt_tv`,
`pressure_gauge`, `old_book`, `cinema_seat`, `narrator_hand_pencil`, `depth_icon`, `doug_cap`, annotation set.
The ARMS tally is a plain size-28 `label` "ARMS: 8" under the DEPTH meter (no icon), so the art director has nothing to
draw for it unless they want one.

---

## 1. The Punch (Red Sea reef, about 5 m)

### `day_octopus` (s004, s006-s007, s011, s013-s014, s016, s019) **DONE** (`assets/previews/050-punch-assets.png`)
- Day octopus (*Octopus cyanea*) resting on sand, arms spread low and wide: mottled red-brown and cream skin with a
  darker reticulated pattern, a bag-shaped mantle raised behind the head, two raised eye bumps, a pale dark-ringed false
  eyespot (ocellus) on the web under each eye, eight thick arms curling at the tips with pale sucker rows showing on the
  curled tips. Facing right (eyes looking right).
- Anchor bottom-centre (where the arms touch the sand). About 700 x 420 (x -350..350, y -420..0). Used at 0.5-0.8.

### `day_octopus_punch` (s005, s010, s015, s023) **DONE** (`assets/previews/050-punch-assets.png`)
- Same animal and footprint as `day_octopus`, but one front arm shot straight out to the right like a jab, nearly
  straight, ending in a tight curled tip about local (+520, -150), with 2-3 short white motion lines behind the arm. The
  other arms stay planted. No fist-shaped fingers: it's still an arm. The thumbnail direction (curled-fist arm) is the
  graphic designer's call; this is the side-on punch.
- Anchor bottom-centre, about 900 x 420 (x -350..+560). Used at 0.8-0.85 with the anchor at x 560-1150.

### `day_octopus_crack` (s008-s009, s022) **DONE** (`assets/previews/050-punch-assets.png`)
- A grey-brown reef rock (pink coralline patches, like `live_rock` but about 600 x 360) with a dark diagonal crack, and
  the day octopus half-poured into it: mantle and head already inside the crack (just the top of the mantle visible),
  four arms trailing out over the rock and sand. Shows "pours itself into cracks".
- Anchor bottom-centre (sand line), about 640 x 380 (y -380..0). The crack mouth is about local (0, -200). Used at 0.7-0.85.

### `goatfish` (s007-s008, s013-s014, s016, s019, s021, s023, s028) **DONE** (`assets/previews/050-punch-assets.png`)
- Red Sea goatfish (yellowsaddle / forsskal type): long slim body, pale pink-white with a yellow back saddle and a dark
  lengthwise stripe from snout to tail, forked tail, and **two long chin barbels** (whiskers) under the mouth, which is
  the defining feature. Neutral fish eye.
- Facing right, anchor centre, about 300 x 110. Used at 0.4-0.7, sometimes flipped.

### `blacktip_grouper` (s015-s016) **DONE** (`assets/previews/050-punch-assets.png`)
- Blacktip grouper (*Epinephelus fasciatus*): stocky reef grouper, pale orange-red with 5-6 darker red vertical bars,
  **black triangular tips on each dorsal fin spine** (the name), big mouth, rounded tail. Neutral fish face.
- Facing right, anchor centre, about 360 x 160. Used at 0.55-0.6.

### `roving_coral_grouper_open` (s024) **DONE** (`assets/previews/050-punch-assets.png`)
- The library `roving_coral_grouper` with its mouth wide open (big dark `#7a0d0d` mouth interior, no teeth detail, no
  red fluid), same colours and proportions, so it reads as "the grouper was waiting".
- Facing right, anchor centre, same size as `roving_coral_grouper`. Used at 0.95, flipped (facing Doug on the left).

### `goatfish_costume` (s019-s024) **DONE** (`assets/previews/050-punch-assets.png`)
- Doug's homemade felt goatfish suit (worn prop): pale pink felt body tube from shoulders to knees with the yellow back
  saddle and dark side stripe, felt forked tail behind the hips to about (-180, +40), and **two floppy felt chin barbels**
  hanging from the chest under his chin. Head, face and cap fully visible (the suit opening is at the neck).
- Anchor = Doug's hips. Must fit `float`, `swim1`/`swim2`, `point`, and `fall` rotated -30 (s023). Used at 0.45-0.75.

### `goatfish_costume_flat` (s025) **DONE** (`assets/previews/050-punch-assets.png`)
- The goatfish costume after death 375: empty, lying flat on the sand, limp tail at the left, neck opening at the right,
  flopped barbels, and a printed felt eye **crossed out with an X** (death grammar, like `reef_fish_costume_flat`).
- Anchor centre, about 440 x 140. Used at 0.6 at (960, 850); I put `doug_cap` on top at (980, 790), so leave a flat
  top around local (+30, -100).

### `octopus_outline_diagram` (s017-s018, s160) **DONE** (`assets/previews/050-punch-assets.png`)
- Plain science diagram of an octopus seen from above, grey outline style like `head_outline`: grey `#8a8a8a` fill
  outline, white body, mantle at the top, eight arms spreading down and out, and a small pink cartoon brain (like
  `cartoon_brain`, about 110 x 80) inside the head at **local (0, -200)**. No face.
- Anchor centre, about 700 x 700. Used at 0.9-1.0. s160 (sober card on `#15181a`) circles the brain area at local
  (0,-200) for "the optic gland", so the outline must read on near-black (thick light-grey outline).

### `octopus_outline_arms_red` (s018) **DONE** (`assets/previews/050-punch-assets.png`)
- Exactly the same drawing and geometry as `octopus_outline_diagram`, but the arms and body are filled cartoon red
  `#e0201b` with darker red shading (the neurons), and only the small brain stays pink. It pops in on top of the plain
  one for "two thirds of them sit in their arms and body". Same anchor and size.

## 2. The Mimic (Indonesia, open sand, about 10 m)

### `mimic_octopus` (s026-s028, s030-s033, s038-s039, s044) **DONE** (`assets/previews/050-mimic-assets.png`)
- Mimic octopus (*Thaumoctopus mimicus*) at rest on sand: small body and **very long thin arms**, all banded
  cream-white and chocolate brown, spread long across the sand. Small raised eyes with bar pupils.
- Anchor bottom-centre, about 800 x 260 (arms span most of the width). Used at 0.35-1.0. Also drawn as a silhouette (s026).

### `mimic_octopus_flatfish` (s034) **DONE** (`assets/previews/050-mimic-assets.png`)
- The mimic octopus pretending to be a banded sole: arms pulled back into a flat leaf-shaped striped oval gliding over
  the sand, brown and white bands, eyes on top. Should look like `banded_sole` at a glance.
- Facing right, anchor bottom-centre, about 500 x 160. Used at 0.8.

### `mimic_octopus_lionfish` (s035-s036, s041) **DONE** (`assets/previews/050-mimic-assets.png`)
- The mimic octopus hovering above the sand with its banded arms flared out in a spiky fan around the body, imitating a
  lionfish's spines. Same banding.
- Anchor centre, about 520 x 420. Used at 0.45-0.95, hovering (the scene's sand is ~200 px below it).

### `mimic_octopus_seasnake` (s039, s041, s045-s047) **DONE** (`assets/previews/050-mimic-assets.png`)
- A small round burrow hole in the sand (dark opening with a sand rim) with **two banded arms rising out of it** in
  opposite S-curves (one up-left, one up-right), black-and-white banded like a sea snake. The rest of the octopus is
  hidden in the burrow.
- Anchor = the burrow mouth on the sand line, arms rise to about y -500, span about x -280..280. Used at 0.5-1.0.

### `banded_sole` (s034) **DONE** (`assets/previews/050-mimic-assets.png`)
- Zebra sole (banded flatfish): flat oval body with bold dark-brown and cream vertical bands, both eyes on top, fringe
  fins all round. Facing right, anchor centre, about 420 x 160. Used at 0.8.

### `lionfish` (s035) **DONE** (`assets/previews/050-mimic-assets.png`)
- Red lionfish: red-and-white vertical stripes, a big fan of long spiny dorsal fins and wing-like pectoral fins,
  feathery tentacles over the eyes. Neutral, not cute. Facing right, anchor centre, about 420 x 320. Used at 0.8.

### `banded_sea_snake` (s039-s040) **DONE** (`assets/previews/050-mimic-assets.png`)
- Banded sea krait / sea snake in an S-curve: bold black and silvery-blue-white bands, small head, **flat paddle-shaped
  tail**. Facing right, anchor centre, about 600 x 160. Used at 0.7-0.9.

### `damselfish` (s039-s041) **DONE** (`assets/previews/050-mimic-assets.png`)
- Small damselfish (humbug type): white body with three black vertical bars, round deep body, small mouth.
  Facing right, anchor centre, about 200 x 150. Used at 0.4-0.5.

### `damselfish_costume` (s044-s049) **DONE** (`assets/previews/050-mimic-assets.png`)
- Doug's felt damselfish suit (worn prop): white felt body tube with three black felt bars, small felt tail behind the
  hips, little felt fins at the sides. Head, face, cap visible.
- Anchor = Doug's hips. Must fit `swim1`/`swim2`, `float`, `cower`; used flipped once (s047). Used at 0.45-0.6.

### `octopus_eye` (s042-s043) **DONE** (`assets/previews/050-mimic-assets.png`)
- Close-up of an octopus eye on mottled red-brown skin: golden-brown iris with a **horizontal rectangular (bar) pupil**,
  heavy fleshy lid above it, skin texture bumps around. Calm, alien, not cute (no lashes, no shine stars).
- Anchor centre, about 600 x 420. Used at 1.0.

### `raincoat` (s037) **DONE** (`assets/previews/050-mimic-assets.png`)
- Yellow hooded rain jacket hanging on a wire hanger, front view, toggles, two pockets. Anchor centre, about 400 x 500.
  Used at 0.9 next to the library `umbrella_open` ("a raincoat doing an umbrella").

## 3. The Thrower (Jervis Bay, about 15 m)

### `shell_midden` (s049-s052, s054-s072) **DONE** (`assets/previews/050-thrower-blanket-assets.png`)
- A wide low bed of old broken pale shells on the sand (scallop and clam halves, cream/white/grey, some tan), built up
  into a gentle mound, with two small dark den openings among the shells. This is the octopus "town" floor.
- Anchor bottom-centre, about 1300 x 140 (y -100..+40). **Flat top at about local y -60**: at scale 1.25 placed at
  y 905 its top sits near y 830, where Doug sits (s066-s072) and the octopuses rest.

### `gloomy_octopus` (s051, s053-s054, s058, s061-s064, s066, s072) **DONE** (`assets/previews/050-thrower-blanket-assets.png`)
- Gloomy octopus (*Octopus tetricus*): grey-brown body with fine pale speckle, a **white ring around each eye**, eight
  medium arms spread on the bottom, mantle raised behind. Facing right.
- Anchor bottom-centre, about 700 x 380. Used at 0.17-0.9 (tiny copies make a row of ten in s058).

### `gloomy_octopus_throw` (s050-s052, s055-s057, s059-s060, s062, s067-s069) **DONE** (`assets/previews/050-thrower-blanket-assets.png`)
- The gloomy octopus mid-throw: front arms gathered under the body holding a bundle of silt and shells, the funnel-shaped
  **siphon visible under the body pointing forward at about local (+100, -120)** (the arrow in s056 points there), a short
  burst of tan silt leaving forward-right. Facing right.
- Anchor bottom-centre, same footprint as `gloomy_octopus`. Used at 0.45-1.0, sometimes flipped.

### `gloomy_octopus_dark` (s063-s065) **DONE** (`assets/previews/050-thrower-blanket-assets.png`)
- Same as `gloomy_octopus` but darkened and worked-up: deep brown-purple `#4a2e2a` body with almost black mottling
  (still a mid-tone, readable on blue), arms raised higher, tense. Same anchor and size.

### `gloomy_octopus_duck` (s052, s060, s065) **DONE** (`assets/previews/050-thrower-blanket-assets.png`)
- A gloomy octopus that just got hit: body pressed low, two front arms raised up and forward as a shield toward the left.
  Facing left (the thrower is on the left). Anchor bottom-centre, about 600 x 420. I flip it in places, so draw it facing
  right and I'll flip.

## 4. The Blanket (open water, about 20 m)

### `blanket_octopus` (s073, s076-s080, s083, s087-s088, s090, s092-s094) **DONE** (`assets/previews/050-thrower-blanket-assets.png`)
- Female blanket octopus (*Tremoctopus*) in midwater: long body, **long webbing hanging between the top arms like a
  half-open cloak**, iridescent deep purple-blue to magenta with pale highlights, small eyes. Two arms hold **clean blue
  beaded man-of-war tentacle strands** (same colour as the library `portuguese_man_o_war` tentacles), never torn ends.
- Facing right, anchor centre, about 800 x 650. Used at 0.6-0.95, silhouette in s073.

### `blanket_octopus_cape` (s075, s081) **DONE** (`assets/previews/050-thrower-blanket-assets.png`)
- The same female with the web **fully spread into a huge rippling cape** around her (threat display), purple-magenta
  with darker bands and eye-like spots along the web edge.
- Anchor centre, about 1100 x 800. Used at 0.75-0.85.

### `blanket_octopus_male` (s084-s088) **DONE** (`assets/previews/050-thrower-blanket-assets.png`)
- The tiny male: a small, pale translucent pinkish-white octopus with a short rounded body and short arms, no web.
  Drawn as a creature (it's shown at 0.25-0.9 next to a walnut and on a balance pan).
- Anchor centre, about 200 x 140.

### `man_o_war_costume` (s089-s093) **DONE** (`assets/previews/050-thrower-blanket-assets.png`)
- Doug's man-of-war costume (worn prop): an inflated blue-purple felt **gas-float vest** around his torso with a pink
  crinkled crest along the top of the back (not over his head), and 5-6 beaded blue felt tentacles hanging from the waist
  to about y +420. Head, face, cap visible.
- Anchor = Doug's hips. Used with `float` at 0.5-0.6, hips at y 330 just under the surface line at y 150.

### `man_o_war_costume_flat` (s094) **DONE** (`assets/previews/050-thrower-blanket-assets.png`)
- The costume after death 376: deflated float lying flat on the surface, limp tentacles hanging down, and a printed
  felt X eye. Anchor centre, about 460 x 200 (float part y -40..+20, tentacles down to +180). Used at 0.65 at (960, 160),
  `doug_cap` on top at (960, 112).

## 5. The Glass Octopus (twilight, about 500 m)

### `glass_octopus` (s096-s100, s104-s105, s107-s115) **DONE** (`assets/previews/050-glass-sevenarm-assets.png`)
- Glass octopus (*Vitreledonella richardi*): almost invisible. Only a **faint thin pale outline** of the body and arms
  (white `#d6e6f0` at width 2-3, about 40% visual weight) and a very faint pale fill, with three solid parts drawn
  clearly: two **long cylindrical (rectangular) eyes** side by side centred near **local (0, -120)** spanning about
  x -150..150, a thin **optic nerve** line from the eyes, and a small reddish-brown **gut** spindle at about (0, +20).
  It must read on `#1b4f86` but look like glass.
- Anchor centre, about 600 x 700. Used at 0.5-1.4 (zoom on the eyes in s105).

### `dishwasher_open` (s102) **DONE** (`assets/previews/050-glass-sevenarm-assets.png`)
- Kitchen dishwasher with the door folded down and the racks pulled out, **filled to the brim with water** (pale blue
  with ripple lines), several glasses in the top rack. Anchor centre, about 700 x 600. Used at 1.0; a `water_glass` pops
  in at local (0, -80).

## 6. The Seven Arms (about 1,000 m)

### `seven_arm_octopus` (s116, s118-s119, s123-s125, s128, s133-s135, s138) **DONE** (`assets/previews/050-glass-sevenarm-assets.png`)
- *Haliphron atlanticus*: a huge, soft, gelatinous midwater octopus, translucent ruby/wine red with darker red arms and
  a broad web, soft saggy mantle, small eyes. Looks heavy and jelly-like.
- Anchor centre, about 800 x 700. Used at 0.35-1.0, silhouette in s116.

### `seven_arm_octopus_male` (s121-s122) **DONE** (`assets/previews/050-glass-sevenarm-assets.png`); **REDRAWN 2026-11-17 per art_review item 1** (`assets/previews/050-sac-fix.png`, in context `assets/previews/050-s121-sac-fix.png`): closed bulging lilac sac `#e9dcef` centred (+114,-100) bulging past the outline, white highlight arc, 4 px black outline, wine-red coiled tube arm (~1.5 turns, dark edge, 4 sucker dots); no rings, no red centre
- Same animal (smaller and slimmer), with the **eighth arm coiled tight inside a pale sac under the right eye**, clearly
  visible as a little spiral in a bulge. Seven arms hang free. Sac at about **local (+100, -100)** (the arrow in s121
  points there). Anchor centre, about 800 x 700. Used at 1.0.

### `seven_arm_octopus_holding` and `seven_arm_octopus_holding_front` (s129-s130, s136-s137) **DONE** (`assets/previews/050-glass-sevenarm-assets.png`)
- A pair for layering. `seven_arm_octopus_holding` = the animal with its arms curled forward into an **open cradle**
  (like holding a fruit bowl) whose centre is at **local (+220, +40)**, cradle about 300 wide. `..._front` = only the
  two front arm tips that curl over the front of the cradle, same anchor and scale, everything else transparent.
  I draw the jelly or jelly-costumed Doug between the two layers.
- Anchor centre, about 900 x 800. Used at 0.85 at (950, 620), so the cradle centre lands at (1137, 654).

### `egg_yolk_jelly` (s128-s130, s134) **DONE** (`assets/previews/050-glass-sevenarm-assets.png`)
- Egg-yolk jelly (*Phacellophora camtschatica*): broad translucent white bell with a **bright yolk-yellow centre** and
  many long thin pale tentacle clusters hanging from the rim. Anchor centre of the bell, about 400 x 600 (bell
  y -100..+40, tentacles down to +500). Used at 0.4-0.6.

### `jelly_costume` (s135-s137) **DONE** (`assets/previews/050-glass-sevenarm-assets.png`)
- Doug's jelly costume (worn prop): a translucent pale-blue felt jelly bell **worn like a cape over his shoulders and
  back**, rim at chest height, with ribbon tentacles hanging below his hips. Head, face and cap must stay visible (the
  bell sits behind and below the head, not over it). Anchor = Doug's hips. Used with `float` at 0.34-0.5.

### `jelly_costume_flat` (s138) **DONE** (`assets/previews/050-glass-sevenarm-assets.png`)
- The jelly costume collapsed flat after death 377: a limp disc with tentacles splayed and a printed X eye. Anchor
  centre, about 420 x 150; `doug_cap` sits on top at local (0, -100).

## 7. The Brooder (1,397 m, Monterey Canyon)

### `brooding_octopus` (s139-s142, s145-s157) **DONE** (`assets/previews/050-deep-assets.png`)
- *Graneledone boreopacifica*: pale purplish-grey octopus with warty bumps, **draped over a cluster of white teardrop
  eggs** attached to a rock ledge, arms wrapped around the cluster, eyes open, motionless. Thin and tired, not sickly.
- Anchor bottom-centre (ledge top), about 600 x 380. Used at 0.6-1.2.

### `octopus_egg_cases_empty` (s159, s162) **DONE** (`assets/previews/050-deep-assets.png`)
- The same egg cluster after hatching: empty translucent egg cases, open at the tips, on the rock ledge. No octopus.
  Must read on near-black `#15181a` (pale outlines). Anchor bottom-centre, about 500 x 220. Used at 0.7-0.75.

### `octopus_hatchling` (s154, s182) **DONE** (`assets/previews/050-deep-assets.png`)
- A large, well-developed octopus hatchling: a complete small octopus (pale, few chromatophore dots), proportionally
  big eyes are fine here but keep them dark and simple, no smile. Anchor centre, about 300 x 300.

### `folding_stool` (s155-s157) **DONE** (`assets/previews/050-deep-assets.png`)
- Small camping stool: two crossed tubular legs, a canvas seat strip. Anchor bottom-centre, **seat top exactly at
  local y -100**, about 200 wide. At 0.6 on floor y 780 the seat is at y 720; Doug sits at hips 685 (seat = hips + 70 x 0.5).
  Used tipped over (`rotate` 80) in s157.

### `doug_beard` (s156) and `doug_beard_lying` (s157) **DONE** (`assets/previews/050-deep-assets.png`)
- Worn props: a long, scruffy grey-white cartoon beard growing from Doug's chin, reaching his hips. `doug_beard` fits
  the `sit` pose facing right; `doug_beard_lying` fits the `on_back` pose (head on the left, so the beard runs from the
  chin along his chest toward the hips). Anchor = Doug's hips, same scale as Doug. Must not cover his eyes or cap.
  Art director: this is a prop, not a design change.

## 8. The Garden (about 3,200 m, Davidson Seamount)

### `pearl_octopus` (s163, s165, s167-s168, s171-s173, s175-s177, s181-s187, s189-s190) **DONE** (`assets/previews/050-deep-assets.png`)
- Pearl octopus (*Muusoctopus robustus*) brooding: a small **pale purple-pink** octopus turned upside-down on the rock,
  arms curled up over its eggs so it looks like a pearl-coloured dome with arm tips showing, small eye visible on the
  side. Many copies form the garden.
- Anchor bottom-centre, about 240 x 160. Used at 0.25-1.0 (lots of copies, so keep the element count moderate).

### `grapefruit` (s168) **DONE** (`assets/previews/050-deep-assets.png`)
- A grapefruit: pinkish-yellow round fruit with dimpled skin and a small stem nub. Anchor centre, about 240 x 240.

### `diving_suit` (s185-s188) **DONE** (`assets/previews/050-deep-assets.png`)
- Doug's cartoon deep-sea suit (worn prop), used with `gear: ["helmet"]` (the bubble helmet keeps his face and cap
  visible): chunky grey padded torso with a brass collar ring, bolts, a small chest gauge, thick padded sleeves to the
  elbows. Legs stay Doug's own lines (it must fit `walk1`/`walk2` and `sit`).
- Anchor = Doug's hips. Used at 0.42-0.48.

### `diving_suit_flat` (s189) **DONE** (`assets/previews/050-deep-assets.png`)
- The suit after death 379: crumpled flat on the rock like an empty sack, collar ring and gauge visible, a painted X on
  the chest plate. Anchor centre, about 460 x 160; `doug_cap` sits on top at local (0, -100).

## 9. The Deepest (6,957 m, Java Trench)

### `dumbo_octopus` (s003, s190, s193-s196, s202-s212) **DONE** (`assets/previews/050-deep-assets.png`)
- Dumbo octopus (*Grimpoteuthis*) as a **pale deep-sea animal**: translucent off-white to pale pink umbrella-shaped body,
  **two ear-like fins above the eyes**, short arms joined by a web almost to the tips, a fringe of fine cirri along the
  arms, small dark eyes (no highlights, no smile). Calm and strange, not a mascot (brief section 7).
- Facing right, anchor centre, about 500 x 450. Used at 0.4-1.0, and as a red-rimmed silhouette in s003, s190 and s193.

### `yellow_submarine_crumpled` (s209-s210) **DONE** (`assets/previews/050-deep-assets.png`)
- Doug's `yellow_submarine` crushed inward like a stepped-on can: hull folded with zigzag crush lines and dents,
  porthole cracked and dark, propeller bent, conning tower squashed. **No Doug visible** (decisions.md). Cartoon only.
- Same anchor as `yellow_submarine`, about 480 x 260 (sits on the floor at about local y +130). Used at 1.2 at (760, 760).

---

## Illustrator notes (2026-11-17): all requests drawn

Every request is in `assets/library/`. The sheets are in `assets/previews/`: `050-punch-assets.png`, `050-mimic-assets.png`,
`050-thrower-blanket-assets.png`, `050-glass-sevenarm-assets.png` and `050-deep-assets.png`. `050-all-assets.png` shows everything at 0.5.
Those sheets centre each asset on its anchor, so the tops of bottom-anchored drawings can look clipped there. The drawings themselves are not clipped.

**Re-placement needed**
- **s019 (`swim1`/`swim2`):** use **`goatfish_costume_swim`** (new). It is the same suit turned for the 70-degree swim lean, with the barbels hanging down.
  Use the same x/y/scale as the `doug` element. `goatfish_costume` fits `float`, `point` and `fall` (with `rotate` matching Doug, as in s023).
- **s187-s188 (`sit`):** use **`diving_suit_sit`** (new). It is the same suit dropped 70 for the sit pose, with the same anchor, x/y and scale as Doug.
  `diving_suit` stays for walk1/walk2 (s185-s186). The suit has no padded sleeves: the walk loop swings the upper arms, so Doug's arm lines come out of a narrower torso instead.

**Size and anchor notes (no change needed)**
- Anchors are as requested. Key local points as requested:
  - shell_midden: flat top at y -60
  - gloomy_octopus_throw: siphon at (+100,-120)
  - glass_octopus: eyes around (0,-120), gut at (0,+20)
  - seven_arm_octopus_male: sac at (+100,-100)
  - holding pair: cradle centre at (+220,+40)
  - folding_stool: seat top at y -100
  - octopus_outline_*: brain at (0,-200)
- Wider or taller than asked:
  - octopus_outline_diagram/_arms_red: ~800x625
  - goatfish_costume_flat: ~500x140; barbels flop out to x +272, flat top ~y -50 under the cap at (+30,-100)
  - mimic_octopus_flatfish: arm tips trail to x -315
  - mimic_octopus_lionfish: ~500x455
  - raincoat: hook rises to y -292
  - jelly_costume_flat: tentacles splay to ~600 wide
  - man_o_war_costume_flat: ~455x265
  - gloomy_octopus_throw: rears to y -415
- Smaller than asked: seven_arm_octopus_male ~550x560 (it is the smaller, slimmer male).
- glass_octopus: the tubular eyes stand upright and tilt outward (x -150..150, y -190..-65), as in the real animal. Side by side horizontally they read as sunglasses.
- damselfish_costume: a round humbug body, so one drawing fits swim1/swim2, float, cower and flipped.
- egg_yolk_jelly at 0.4 in the cradle: the long tentacles hang below the cradle, so a smaller scale may sit better.
- Kid-appeal check: no smiles, blush or shine anywhere. Octopus eyes are small, with bar pupils under heavy lids or plain dark eyes.
  The dumbo and the hatchling each show one dark profile eye and no mouth. The man-of-war strands end in round beads (no torn ends), and there is no ink.

