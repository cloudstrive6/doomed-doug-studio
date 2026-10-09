# Asset requests: 011 Every Animal Doug Could Beat in a Fight, Until He Dies

From the director, for the illustrator (the art director approves). The house style follows `assets/library/anglerfish.json` and
`channel/art_bible.md`:
- **Detailed tier** for creatures and props: outlines 4-6, flat fills plus `spray` shading, a darker back and a lighter belly,
  white eyes with black pupils. Everything faces **right** unless a note says otherwise. Local coordinates are centred on the anchor.
- **Anchors and sizes.** I laid out all 285 shots with placeholder boxes at exactly the sizes and anchors below, then checked the
  contact sheets for the counter zone, caption bar, crops and guide inset. `bc` means the anchor is at the bottom-centre: the lowest point
  sits on y=0 and the drawing spans y -h..0. `c` means the anchor is at the centre. Sizes are local units at scale 1, width x height.
  Where a note gives a local point (a tail tip, a claw, a saddle, an eye), I aimed arrows or gaze lines at it, so please keep it close.
- **Facing.** The shotlist flips creatures so they face Doug. Draw them facing right, and keep the silhouette readable when mirrored.
- **Tone.** This is adult-coded nature horror and the kid-appeal risk is high (brief, section 7). The animals must look dangerous and not
  cuddly: no smiles, no blush, no big sparkly eyes, no pastel nursery colours. **No blood, wounds or injuries on any drawing.** The goose
  is mid-hiss, the cat has its ears flat back, and the elephant has its ears out.
- **SIL** marks an asset that is also used with `"silhouette": true` (a black shape with a red glow). Its outer outline must stay clean
  and recognisable when filled black.
- **Priority:** A = hero (8+ shots), B = supporting (3-7), C = one-off.

**Reused from the library (no work needed):** `cat` (the calm tabby on the wall), `rat`, `grey_wolf` (also SIL), `polar_bear`,
`saltwater_crocodile`, `platypus` (the 010 bandage callback), `cape_fur_seal` (seal blubber), `front_door`, `small_car` (family car),
`suitcase` (20 kg), `baby_grand_piano` ("concert grand"), `binoculars`, `clock`, `house`, `red_barn`, `research_hut`, `body_outline`
(the "two grown men" outlines), `scientist`, `rainforest_tree`, `australia_map`, `water_splash`, `doug_cap`, `field_guide`,
`field_guide_open`, and the annotation set (`question_mark`, `exclamation_mark`, `warning_triangle`, `red_x`).

**Drawn inline in the shotlist (no asset needed):** the DOUG DEATHS counter, the poll boards and bars, the "WIN?" row and its tick on
the field guide (overlay, same zone rules as FRIEND?), Doug's red boxing gloves and the hand bandage, the people icons, the TV, the nest
and eggs, the muscle-fibre bars, the bite gauge, the wolf eyes in the dark, the PNAS paper, the chalkboard, the cardboard box, the
sound waves, the sea-ice floes and the gorilla's "death drawn already" sheet.

**Notes for the art director (not illustrator work):**
1. **Capless upright Doug, s021-s024 (goose).** The script has the goose walk off wearing Doug's cap ("took the cap"). Doug sits
   dazed with `gear: ["cap_off"]` (upright pose, so no cap is drawn) while `canada_goose_cap` wears it. The cap is back on in s025.
   The art bible lists this as an approved one-off only, so please log it in `decisions.md`.
2. **No chest-beat pose.** For s177-s178 (Doug beats his chest) I loop `["hands_hips", "think"]`, which is the closest match. If you
   want to add a `chest_beat` pose (both forearms bent across the chest), I'll swap it in. It's optional.
3. **Glyph check (CD condition).** In the bundled Arimo, `≈` and `→` render correctly: I used them in "≈ 1 CAR" (s195) and
   "1 in 3 → HOSPITAL" (s043/s044). `✓` does **not** render (it draws a tofu box), so every tick in the episode is a drawn green
   polyline, as on the field guide.
4. **The gorilla leaves after looking at Doug, not because of his chest beat (CD condition).** s177-s178 show the chest beat and the
   gorilla standing still. s179 shows the long look: a dotted gaze line and a 0.8 s hold. Only s180 has it walking away
   (`silverback_walking`, facing away). s183-s184 show it already far off.
5. **The cat-bite statistic is a plain bar (CD condition).** s043/s044 show a 3-segment bar with one red third and
   "1 in 3 → HOSPITAL". There is no hand drawing, wound, hospital or medical imagery.

---

## A. Hero creatures

### `cassowary` (A, SIL)
- **What:** Southern cassowary, the item 5 star and one of the 10 icons in the closing.
- **Look:** Tall, heavy flightless bird standing upright. Shaggy, coarse **black** body plumage that hangs like hair (a mid-tone
  near-black `#2a2a2e` with grey strand strokes, so it reads on the dark rainforest), a long bare **bright blue neck** (`#3a7bd5` to
  turquoise), two dangling **red wattles** at the throat, and a tall brown-horn **casque** on top of the head. Thick scaly grey legs, with a
  visibly long inner claw on each foot. Hard amber eye. Not friendly: it should look like it would kick.
- **Facing / anchor / size:** right, `bc`, about 320x600 (casque top at y -600, feet on y=0).
- **Shots:** s100-s106, s109, s110, s112, s113, s114 (4 small at 0.3), s116, s117, s118, s120, s121-s125, s281.

### `red_kangaroo` (A)
- **What:** A big male red kangaroo standing upright, chest out.
- **Look:** Rusty red-brown coat (`#b5502e`) with a paler cream belly and chest, long upright ears, a long muzzle with a dark nose,
  and **muscular forearms** held a bit forward. Huge hind feet. A long thick tail **planted on the ground behind it like a fifth leg**.
- **Facing / anchor / size:** right, `bc`, about 420x600. **Keypoint: the tail tip touches the ground at about local (-260, 0),**
  and the tail base is around (-90, -170). The arrows in s059/s060 land on the tail tip.
- **Shots:** s050, s052-s056, s058-s062, s066, s070, s073, s281.

### `red_kangaroo_kick` (B)
- **What:** The same kangaroo in its fighting move: **leaning right back, balanced on its tail**, with both hind feet swung up and
  forward together to kick. Forearms up.
- **Look:** Same colours and head as `red_kangaroo`, so the two can cut between each other.
- **Facing / anchor / size:** right, `bc`, about 560x520. **Keypoints:** the tail tip on the ground at about local (-200, 0), and both
  hind feet out to the right at about (+260, -180..-260).
- **Shots:** s057 (sparring with a mirrored `red_kangaroo`), s063, s064, s065, s066, s071.

### `silverback_gorilla` (A, used for scale)
- **What:** An adult male western lowland gorilla standing upright, arms hanging, calm but enormous. In s179 he is "looking at Doug for
  a long moment".
- **Look:** Near-black charcoal coat (`#2f2f33` with grey strokes so it reads on the grey-misty jungle), a dark leathery face and
  chest, a heavy brow and a high crested head. The pale **silver saddle** shows on the back and flank. Big hands. A steady, unreadable stare
  (not angry, not friendly).
- **Facing / anchor / size:** right, three-quarter view, `bc`, about 440x640. The eye sits around local (+60, -560).
- **Shots:** s156-s162, s165, s169, s176-s179, s281.

### `silverback_chest_beat` (B)
- **What:** The same gorilla mid chest-beat: **upright, both cupped hands on the chest**, mouth open in a roar, with a couple of short
  motion ticks at the hands.
- **Facing / anchor / size:** right, `bc`, about 440x640, the same footprint as `silverback_gorilla` so the two can swap.
- **Shots:** s166, s171, s172 (big and small copies), s173, s174, s175.

### `silverback_walking` (B)
- **What:** The same gorilla on all fours, knuckle-walking. It is used for the charge (s167-s170) and for **walking away** (s180, s183, s184).
- **Look:** Side view. The **silver saddle across the back is clearly visible**, since the arrow in s164 points at it at about local
  (-100..+60, -400..-340). Knuckles down, heavy shoulders.
- **Facing / anchor / size:** right, `bc`, about 640x420.
- **Shots:** s163, s164, s167, s168, s170, s175, s180, s183, s184.

### `african_bush_elephant` (A)
- **What:** An African bush elephant in side view: a matriarch, a family member and the scale shot.
- **Look:** Grey (`#8a8a8a`) with a darker belly and wrinkle strokes. **Very large ears shaped like Africa** (this is not the small-eared
  Asian `elephant` in the library), a single-domed head, a hollow back, a long trunk and curved ivory tusks. Dusty red tint at the feet is fine.
- **Facing / anchor / size:** right, `bc`, about 720x540 (the shoulder top at about y -480 for the "3-3.7 M" dotted line).
- **Shots:** s246, s247, s250-s252, s255, s256, s260-s264, s265, s269, s270, s273 (tiny), s281.

### `african_bush_elephant_front` (A)
- **What:** The boss: an African bush elephant facing the camera with its **ears fully spread out**, trunk down, tusks forward. Still and
  attentive (it's listening), and enormous.
- **Look:** Same colours as the side view. The spread ears make a big wide silhouette. Small dark eyes and a heavy forehead. Not cute.
- **Facing / anchor / size:** front view, `bc`, about 900x760.
- **Shots:** s245, s249, s253, s267, s268, s271, s274-s278.

### `chimpanzee` (A, SIL)
- **What:** An adult male chimpanzee knuckle-walking on all fours. It is also the black silhouette in the "8 vs 1" and "9 in 10" diagrams.
- **Look:** Black-brown coat, a bare grey-tan face with big ears, a heavy brow and long arms. Expression flat and alert.
- **Facing / anchor / size:** right, `bc`, about 420x300.
- **Shots:** s128, s129, s130, s132, s135, s137, s139, s141-s143, s145-s149 (silhouettes), s150, s281.

### `chimpanzee_sitting` (B)
- **What:** The same male chimp sitting on a log, arms resting on its knees, staring flatly at Doug.
- **Facing / anchor / size:** right, `bc` (the bottom sits on the log top), about 320x380.
- **Shots:** s126, s151, s152.

## B. Goose and cat

### `canada_goose` (A)
- **What:** A Canada goose standing alert on the grass.
- **Look:** A black head and long black neck with the **white chinstrap** patch, a brown-grey body with pale scalloped feather edges,
  a white under-tail, black legs and feet. Big for a bird.
- **Facing / anchor / size:** right, `bc`, about 360x420.
- **Shots:** s005, s006, s007, s011, s018, s025, s026, s281.

### `canada_goose_hiss` (B)
- **What:** The same goose in its threat display: **neck stretched low and forward**, beak open with the pink tongue showing, wings
  half lifted.
- **Facing / anchor / size:** right, `bc`, about 460x300.
- **Shots:** s007 (small), s008, s009, s010, s012, s017.

### `canada_goose_attack` (B)
- **What:** The goose mid-charge: **wings fully out**, running forward with the beak open. The "weapon is the wing" shot (s014) points a red
  arrow at the bend of the wing (the wrist), so keep it obvious on the near wing, around the upper-left of the drawing.
- **Facing / anchor / size:** right, `bc`, about 620x380.
- **Shots:** s013, s014, s015, s019.

### `canada_goose_cap` (B)
- **What:** The goose waddling off, smug, **wearing Doug's red cap** (the same dome and brim as `doug_cap`, sitting a bit crooked on its
  head).
- **Facing / anchor / size:** right (it walks away from Doug toward the pond), `bc`, about 360x460.
- **Shots:** s021, s022, s023, s024.

### `cat_angry` (C)
- **What:** The library `cat` (the same orange tabby) **crouched on the wall with its ears flat back** and its tail lashing in an S-curve.
- **Facing / anchor / size:** right, `bc`, about 420x300. Match `cat`'s colours exactly.
- **Shots:** s032, s033, s034.

### `cat_yawn` (C)
- **What:** The library `cat`, identical pose and footprint, mid-**yawn**: mouth wide open (pink, with small fangs) and eyes squeezed shut.
  This is the "decided he was boring" beat.
- **Facing / anchor / size:** right, `bc`, same as `cat` (about 330x390).
- **Shots:** s037.

## C. Wolf, crocodile, bears

### `grey_wolf_sitting` (C)
- **What:** The library `grey_wolf`, sitting on its haunches and watching (the four extra wolves revealed when "the camera pulled back").
- **Facing / anchor / size:** right, `bc`, about 300x340. The same coat as `grey_wolf`, with amber eyes.
- **Shots:** s097 (4 copies, 2 mirrored, among the pine trees).

### `moose` (C)
- **What:** A bull moose: the "animal far bigger than any single wolf".
- **Look:** Dark brown, with a long face and drooping muzzle, a dewlap, a shoulder hump, long legs and broad palmate antlers.
- **Facing / anchor / size:** right, `bc`, about 640x560.
- **Shots:** s082, s083.

### `croc_eyes_water` (B)
- **What:** Only the **eyes, brow bumps and nostrils** of a saltwater crocodile, plus a short row of back scutes, poking out of
  muddy brown water. This is the ambush.
- **Look:** Olive-grey bumps with yellow slit-pupil eyes. The anchor sits on the water line, so the bumps rise above y=0. Add a couple of
  short pale ripple lines on the water around them.
- **Facing / anchor / size:** right, `c` (on the waterline), about 600x80.
- **Shots:** s185, s187, s188, s197, s198, s203, s206.

### `croc_jaws_open` (B)
- **What:** A saltwater crocodile's head in side view with the **jaws wide open**: the bite-force diagrams (a gauge beside it, a car
  "weighed" above it, the walnut brain).
- **Look:** Olive-grey with a yellowish underside, interlocking pointed teeth, a pale pink-yellow inner mouth (no blood), a yellow eye.
- **Facing / anchor / size:** right, `bc`, about 620x420. The brain spot used in s201 is about local (-60, -300).
- **Shots:** s192, s193, s194, s195, s201.

### `croc_log` (B)
- **What:** A saltwater crocodile lying perfectly still and flat on the riverbank, **looking like a muddy log**: dull brown-olive with dried
  mud patches, no legs showing, eye closed. In s211 Doug sits down next to it.
- **Facing / anchor / size:** right (it gets mirrored to face Doug), `bc`, about 900x150. The eye is near the head end, about
  local (+330, -110).
- **Shots:** s204, s205, s211.

### `croc_log_eye` (C)
- **What:** **Exactly** `croc_log` (same geometry), with **one yellow eye open**. It is overlaid on top of `croc_log` at the end of s211
  for the reveal, so every line must match.
- **Shots:** s211, s212.

### `polar_bear_standing` (B, SIL)
- **What:** A polar bear **standing up on its hind legs** at full height (3 m, above a ceiling line).
- **Look:** Same palette as the library `polar_bear`: creamy white `#f4f1e4`, grey-blue shading, a clear thick outline so it reads on white
  ice, a black nose, big paws with dark claws. Predator, not cuddly.
- **Facing / anchor / size:** right (three-quarter view is fine), `bc`, about 380x860.
- **Shots:** s217 (silhouette reveal), s218, s221.

### `grizzly_bear` (C)
- **What:** A grizzly bear on all fours: the poll's "least beatable" animal.
- **Look:** Brown, with a pale-tipped grizzled back, the **shoulder hump**, a dished face, long pale claws.
- **Facing / anchor / size:** right, `bc`, about 560x340.
- **Shots:** s215, s216.

## D. Props and places

### `dust_cloud` (B)
- **What:** A classic cartoon **fight cloud**: billowing tan-beige dust (`#e2d3b0`, shaded `#c8b58a`) with a few motion lines and 2-3
  small stars, plus the odd limb blur. No body parts or blood. This is how every death happens off-screen.
- **Facing / anchor / size:** `c`, about 700x460.
- **Shots:** s020 (goose), s071 (kangaroo), s098 (wolf), s124 (cassowary), s153 (chimp, rising from behind the log).

### `snow_dust_cloud` (C)
- **What:** The same fight cloud in snow colours (white `#ffffff` billows shaded pale blue `#cfe6f5`) for the polar bear.
- **Facing / anchor / size:** `c`, about 700x460.
- **Shots:** s242.

### `pine_tree` (A)
- **What:** A dark conifer for the dusk forest (wolf): a tall layered triangular crown and a short brown trunk.
- **Look:** Use a mid-dark blue-green (`#2f5a48`, shaded `#1f3f33`) with a pale edge highlight so it reads on the navy dusk sky `#2c3e66`.
- **Facing / anchor / size:** `bc`, about 300x760 (at scale 0.8 the tip stays below the caption bar).
- **Shots:** s074, s078-s081, s085, s088, s093-s099.

### `fallen_log` (B)
- **What:** A thick mossy fallen log lying horizontally (the chimp's bench and Doug's arm-wrestle table).
- **Look:** Brown bark with grooves, moss patches and a pale cut end with rings on the left. **The top surface is at about local y -130**,
  so the chimp, Doug and the paper sit on it.
- **Facing / anchor / size:** `bc`, about 700x140.
- **Shots:** s126, s151, s152, s153, s154.

### `birdseed_bag` (B)
- **What:** A brown paper bag with a white label reading **BIRDSEED**, top rolled over, and a few seeds spilling.
- **Facing / anchor / size:** `c`, about 180x240. It is also used upside down (`rotate: 180`, "then he ran out"), and in s125 the
  `doug_cap` sits on top of it, at local about (0, -125) at scale 0.55.
- **Shots:** s121, s122, s123, s125.

### `sandwich` (B)
- **What:** A triangle sandwich: white bread with lettuce, tomato and cheese layers. It stands for "food from people".
- **Facing / anchor / size:** `c`, about 200x150.
- **Shots:** s114, s115, s116, s117, s118.

### `cassowary_foot` (C)
- **What:** A close-up of one cassowary foot: thick grey scaly toes, with the **inner toe carrying a long dagger-like claw** (dark horn,
  slightly curved, about 12 cm). It is the "CLAW" shot, with a ballpoint pen above it for scale.
- **Facing / anchor / size:** right, `bc`, about 520x300. The claw tip is around local (+230, -130). I'll re-aim the s107 arrow once the
  drawing exists.
- **Shots:** s107, s108.

### `ballpoint_pen` (C)
- **What:** An ordinary clear-barrel ballpoint pen with a blue cap and a blue ink tube inside, lying horizontally.
- **Facing / anchor / size:** `c`, about 460x40.
- **Shots:** s108.

### `bowling_ball` (C)
- **What:** A dark blue-black bowling ball with three finger holes and a white shine.
- **Facing / anchor / size:** `c`, about 200x200.
- **Shots:** s009.

### `house_brick` (C)
- **What:** A plain red house brick in 3/4 view, with a darker side face.
- **Facing / anchor / size:** `c`, about 220x110.
- **Shots:** s033 (2 stacked).

### `cement_bag` (C)
- **What:** A grey paper sack of cement with a plain **CEMENT** label and a folded top.
- **Facing / anchor / size:** `bc`, about 180x240.
- **Shots:** s080 (3, stacked).

### `walnut` (C)
- **What:** A whole walnut in its shell: tan, wrinkled, with a seam line. This is the size of the crocodile's brain.
- **Facing / anchor / size:** `c`, about 140x120.
- **Shots:** s201, s202.

### `silver_fish` (B)
- **What:** A generic silvery Arctic fish (char-like) with a darker back, a silver belly and a few pale spots: Doug's peace offering.
  It is held in Doug's hand by the tail, and later lies untouched on the ice next to the cap.
- **Facing / anchor / size:** right, `c`, about 240x90.
- **Shots:** s239-s244.

### `loudspeaker` (B)
- **What:** A field loudspeaker: a black box with a big round grey cone, standing on the ground (the Amboseli playback speaker).
- **Facing / anchor / size:** front view, `bc`, about 180x240.
- **Shots:** s254-s257, s259-s262, s264.

### `savanna_bush` (B)
- **What:** A low, dry savanna shrub with olive-brown leaves and twiggy branches. The loudspeaker hides behind it, and so does Doug in s269.
- **Look:** Olive-brown `#7a6a3a`, not bright green, so it sits on the red-dust ground.
- **Facing / anchor / size:** `bc`, about 360x200.
- **Shots:** s254, s255, s256, s269, s270.

### `acacia_tree` (C)
- **What:** A flat-topped umbrella acacia with a dark trunk and a wide flat crown. It should read as a near-silhouette on the dark red sunset.
- **Facing / anchor / size:** `bc`, about 620x520.
- **Shots:** s254.

### `crumpled_paper` (C)
- **What:** A crumpled ball of white paper, with a hint of a pencil sketch line visible in the folds. It is the "narrator had the death
  drawn already" drawing, crumpled and dropped at the frame edge.
- **Facing / anchor / size:** `c`, about 140x140.
- **Shots:** s182.
