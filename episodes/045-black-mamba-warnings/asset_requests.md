# 045-black-mamba-warnings: asset requests (director, 2026-11-12)

The shotlist already places these by name, so please keep the **anchor, bounding box and key points** given here.
The generator (`episodes/045-black-mamba-warnings/build/gen_shotlist.py`) puts other things on those points: a coiled
mamba on the mound top, a cap on the eagle head, Doug's hips in a saddle. Everything faces right unless noted. Use the
house style: detailed tier, thick black outlines (5-6), flat fills with interior shading. **Never cute**: no big eyes,
no smiles, no nursery pastels.

**Mamba palette, same as the library `black_mamba` / `black_mamba_gape`:** olive-grey body `#7f8865` (not black),
darker back, pale cream belly with scute lines, a long coffin-shaped head with a heavy brow, a small dark eye, and a
mouth that is a straight line when closed. The only black is the inky blue-black mouth lining `#0b0f2a`, shown when
the mouth is open. No drool, no venom drops, no blood. The three reared drawings (`black_mamba_reared`,
`black_mamba_hood`, `black_mamba_hood_gape`) must be **one pose, one geometry**, with only the neck and the mouth
changing, because they cut against each other in item 4-7 strips.

Reused from the library (no request): `black_mamba`, `black_mamba_gape`, `field_guide_open`, `doug_cap`, `speedometer`,
`stick_cyclist`, `scientist`, `stick_man_plain`, `journal_paper`, `old_book`, `record_book_open`, `calendar`, `clock`,
`alarm_clock`, `wait_stopwatch`, `chalkboard`, `fallen_log`, `wooden_shed`, `house`, `rubbish_bin`, `rubbish_bag`, `rat`,
`cat`, `tent`, `flour_bag`, `bed`, `nile_monitor`, `jackal`, `savanna_bush`, `acacia_tree`, `tree_branch`,
`kitchen_counter`, `bucket`, `phone`, `eye_icon`, `vial`, `lab_mouse`, `medicine_bottle_plain`, `pill_bottle`,
`small_table`, `door_flung_open`, `narrator_hand`, `hospital_building`, `antivenom_box`, `banknote`, `round_hut`,
`africa_map`, `bicycle_wheel`, plus the annotation set.

---

## Places and props

### `termite_mound` (35 shots: the episode's home base, the most important drawing)
**DONE (illustrator, 2026-11-12):** preview `assets/previews/045-black-mamba-warnings-assets-props.png` (+ `assets/previews/045-black-mamba-warnings-assets-thumbs.png` at 168x94).
An African termite mound with the mamba's front door: a squat, lumpy red-brown clay dome (`#b5653a`, darker `#8a4a2a`
shading, a lighter sunlit side) with two or three short rounded turrets. Its **rounded top platform** (about 160 wide,
nearly flat) sits at local y -480, so a coiled snake (`black_mamba_coiled`) or Doug's cap (`doug_cap` at y -510) can
rest on it. A **dark hole at the base**, centred (0,-70), about 120 wide x 90 tall, near-black `#1a0f0a` inside a
clay lip. It must read as a doorway. Anchor bottom-centre (ground y 0), about 440 x 520 (x -220..220, y -520..0). Mid
tones only, so it still reads on the near-black death cards (`#0b0f14`). It is used at 0.6-1.25.
Shots: s002-s003, s005, s014-s015, s018-s021, s023-s025, s027-s032, s034-s039, s045-s049, s066-s069,
s203-s204 (dawn coda).

### `house_cross_section`
**DONE (illustrator, 2026-11-12):** preview `assets/previews/045-black-mamba-warnings-assets-props.png` (+ `assets/previews/045-black-mamba-warnings-assets-thumbs.png` at 168x94).
A cutaway of a small single-storey house: the kitchen is on the ground floor (counter, kettle, window) and the roof space
above it is an empty, dim triangle (`#8a7050` with yellow insulation strokes), its floor at about local y -470,
x -250..250, where the shotlist puts a coiled mamba. Red roof, white walls, cut edges drawn as thick black lines.
Anchor bottom-centre, about 800 x 700. Shot: s041.

### `bicycle_flat_tyre`
**DONE (illustrator, 2026-11-12):** preview `assets/previews/045-black-mamba-warnings-assets-props.png` (+ `assets/previews/045-black-mamba-warnings-assets-thumbs.png` at 168x94).
An old black steel upright bicycle, side view facing right, with its **front tyre flat**: squashed, the rim almost on
the ground, the rubber bulging out. A brown saddle with its top at about (-90,-320), handlebars at about (+200,-330), a
chain, and a dusty rear tyre. No brand. Anchor bottom-centre (wheels on y 0), about 620 x 360. It also has to read
tiny (0.12) on a paper map. Shots: s004, s181, s200-s201.

### `nerve_doorbell_diagram` (14 shots)
**DONE (illustrator, 2026-11-12):** preview `assets/previews/045-black-mamba-warnings-assets-props.png` (+ `assets/previews/045-black-mamba-warnings-assets-thumbs.png` at 168x94).
A crude MS Paint biology diagram on a transparent background: a nerve cell body (a lumpy circle at about x -560) with a
long yellow `#ffd21a` wire (the axon, black outline, about 40 thick along y 0) running right to a pink `#f4c6c4`
**muscle block** (x +300..+560, y -120..+140, with fibre lines). Where the wire meets the muscle, at **(+230, 0)**,
there is a **doorbell**: a grey square plate (about 110) with a round white push-button. Keep the wire clear on top
at x -300, -150 and 0 (y -40), because the shotlist draws blue "channel" rings and red X marks there. Anchor centre, about
1200 x 400. Used at 0.6-1.4. Shots: s136, s143-s150, s152, s154-s156, s174.

### `fire_alarm_kit`
**DONE (illustrator, 2026-11-12):** preview `assets/previews/045-black-mamba-warnings-assets-props.png` (+ `assets/previews/045-black-mamba-warnings-assets-thumbs.png` at 168x94).
A red wall-mounted fire-alarm call box (`#e0201b`, darker side) with its small glass front swung open on a hinge, and
inside it, where the button should be, a tiny green first-aid kit with a white cross. Front view. No text. Anchor centre,
about 260 x 320. Shot: s170.

### `umbrella_open` / `umbrella_folded` (a pair, same umbrella)
**DONE (illustrator, 2026-11-12):** preview `assets/previews/045-black-mamba-warnings-assets-props.png` (+ `assets/previews/045-black-mamba-warnings-assets-thumbs.png` at 168x94).
A plain black umbrella (`#2b2b2b` canopy with grey rib lines and a silver tip) with a curved wooden hook handle.
`umbrella_open`: the canopy is spread wide in side view, about 520 wide, its top at local y -560, the shaft vertical,
and the handle hook at the bottom. `umbrella_folded`: the same umbrella closed and furled with its strap, vertical,
about 90 x 560. Both have the anchor at the bottom of the handle (0,0) and stand upright on the ground. Shots: s102-s103.

## The mamba variants

### `black_mamba_reared` (28 shots: the head lift and the warning pose)
**DONE (illustrator, 2026-11-12):** preview `assets/previews/045-black-mamba-warnings-assets-snakes.png` (+ `assets/previews/045-black-mamba-warnings-assets-thumbs.png` at 168x94).
The front body rises **vertically** out of loose ground coils: about forty percent of the body is up, and the head is
level and facing right at about **(+120,-420)**, with the **mouth closed** and an alert eye at about (+140,-425). The neck is
slim, with no hood. The ground coils lie flat at x -260..+60, y -60..0. Anchor bottom-centre, where the coils touch
the ground. Bbox about x -280..+200, y -450..0. The silhouette must read clearly, because it is also used with
`silhouette: true`. Shots: s047, s069-s075, s077-s078, s083-s085, s087-s089, s099-s100, s115-s116, s119-s120, s125
(silhouette), s131-s133.

### `black_mamba_hood`
**DONE (illustrator, 2026-11-12):** preview `assets/previews/045-black-mamba-warnings-assets-snakes.png` (+ `assets/previews/045-black-mamba-warnings-assets-thumbs.png` at 168x94).
`black_mamba_reared` with exactly the same geometry, plus a **narrow hood**: the neck flap behind the head is spread to
about 1.5 times the head width, at about (+110,-340). That is much narrower than a cobra's hood. The mouth is closed.
Shots: s085-s086, s092-s095, s099-s101, s104-s110.

### `black_mamba_hood_gape`
**DONE (illustrator, 2026-11-12):** preview `assets/previews/045-black-mamba-warnings-assets-snakes.png` (+ `assets/previews/045-black-mamba-warnings-assets-thumbs.png` at 168x94).
The same pose and hood, with the **mouth gaping wide** to show the inky blue-black lining `#0b0f2a` and two small pale
fangs, like the library's `black_mamba_gape`. The mouth centre is at about (+150,-410). Shots: s085, s096-s097, s099-s100,
s111, s137 (silhouette).

### `black_mamba_coiled`
**DONE (illustrator, 2026-11-12):** preview `assets/previews/045-black-mamba-warnings-assets-snakes.png` (+ `assets/previews/045-black-mamba-warnings-assets-thumbs.png` at 168x94).
A black mamba basking: a loose, flat-ish pile of body coils with the head resting on the top coil at about (+100,-100),
calm and with the mouth closed. Anchor bottom-centre, about 300 x 130 (x -150..150, y -130..0). It sits on the mound
top, in the roof space, and on the ground at dawn. Shots: s029-s031, s036-s039, s041, s048-s049, s203-s204.

### `mamba_combat_pair`
**DONE (illustrator, 2026-11-12):** preview `assets/previews/045-black-mamba-warnings-assets-snakes.png` (+ `assets/previews/045-black-mamba-warnings-assets-thumbs.png` at 168x94).
Two male black mambas in combat: the lower bodies are wound around each other two or three times in a rope-like
twist, and both fronts are raised side by side with the heads at about **local y -380** (one meter off the ground at
scale 0.95), leaning on each other, mouths closed, rigid. It must read as wrestling, not as a heart shape or a hug.
Anchor bottom-centre, about 520 x 400. Shots: s079-s082.

### `cobra_hooded`
**DONE (illustrator, 2026-11-12):** preview `assets/previews/045-black-mamba-warnings-assets-snakes.png` (+ `assets/previews/045-black-mamba-warnings-assets-thumbs.png` at 168x94).
A generic African cobra (Cape cobra colouring: yellow-brown `#c9963a` with a darker back and a pale belly) reared up and
**facing left** (toward the mamba), with a **wide** spread hood centred at about (0,-320) and about 200 wide. That is
clearly a different snake from the mamba's narrow flap. Mouth closed. Anchor bottom-centre, about 300 x 420.
Shots: s092-s093, s101, s104-s109.

### `green_mamba`
**DONE (illustrator, 2026-11-12):** preview `assets/previews/045-black-mamba-warnings-assets-snakes.png` (+ `assets/previews/045-black-mamba-warnings-assets-thumbs.png` at 168x94).
The library `black_mamba` drawing (same pose, size and anchor: centre, bbox +-450 x +-130) recoloured as a green mamba:
a bright leaf-green `#3faa3a` body, a slightly yellower belly and a darker green back. Shots: s141-s142.

## Predators and the costume

### `brown_snake_eagle`, perched (8 shots)
**DONE (illustrator, 2026-11-12):** preview `assets/previews/045-black-mamba-warnings-assets-creatures.png` (+ `assets/previews/045-black-mamba-warnings-assets-thumbs.png` at 168x94).
A brown snake eagle (Circaetus cinereus) perched, side or 3/4 view facing right: dark chocolate-brown plumage all
over, a big rounded owl-like head with **large staring yellow eyes** (its defining feature), a hooked grey-black bill,
and long **bare pale-grey legs with heavy scales**. Upright stance. Anchor at the feet (0,0), which sit on a branch
line. About 260 x 380 tall. Shots: s050-s052, s054-s056, s061-s062.

### `brown_snake_eagle_glide`
**DONE (illustrator, 2026-11-12):** preview `assets/previews/045-black-mamba-warnings-assets-creatures.png` (+ `assets/previews/045-black-mamba-warnings-assets-thumbs.png` at 168x94).
The same bird gliding down to the right: broad wings spread and slightly raised, legs thrust forward and down, open
talons on scaled grey legs, with the talons at about (+220,+130). Anchor at the body centre, about 700 x 360. It is
also used as a `silhouette: true` reveal in the sky (s049). Shots: s049, s056-s057.

### `brown_snake_eagle_carrying_mamba`
**DONE (illustrator, 2026-11-12):** preview `assets/previews/045-black-mamba-warnings-assets-creatures.png` (+ `assets/previews/045-black-mamba-warnings-assets-thumbs.png` at 168x94).
The same bird flying up and to the right with its wings raised, gripping an olive-grey black mamba (library palette) in
its talons. The snake dangles below in a long S-curve to about local y +540 and is still twisting: the tail curls and
the head is turned up. No blood and no wounds. Anchor at the eagle's body centre, about 700 wide x 800 tall
(y -260..+540). Shots: s058-s059.

### `mongoose`
**DONE (illustrator, 2026-11-12):** preview `assets/previews/045-black-mamba-warnings-assets-creatures.png` (+ `assets/previews/045-black-mamba-warnings-assets-thumbs.png` at 168x94).
A slender African mongoose (Egyptian or slender mongoose type), standing and facing right: grizzled grey-brown fur, a
long low body, a pointed face, small round ears, and a long tapering tail with a dark tip. Calm and alert. Anchor
bottom-centre, about 380 x 150. Shots: s061-s064.

### `honey_badger`
**DONE (illustrator, 2026-11-12):** preview `assets/previews/045-black-mamba-warnings-assets-creatures.png` (+ `assets/previews/045-black-mamba-warnings-assets-thumbs.png` at 168x94).
A honey badger standing and facing right: a black lower body and legs, a broad silver-white mantle from the crown to
the tail, small eyes, heavy front claws, low and stocky. Anchor bottom-centre, about 420 x 200. Shot: s063.

### `snake_eagle_costume` (worn prop over Doug, `stand` pose)
**DONE (illustrator, 2026-11-12):** preview `assets/previews/045-black-mamba-warnings-assets-creatures.png` (+ `assets/previews/045-black-mamba-warnings-assets-thumbs.png` at 168x94).
Doug's homemade brown snake eagle suit, worn like `rat_costume`, with anchor = Doug's hips and listed after Doug at the
same x/y/scale. It has a chocolate-brown felt body tabard with scalloped feather rows over the torso, and cardboard brown
wings strapped along both arms (hanging, the tips at the hands). There is a **cardboard eagle-head hood** over the top of
his head with big yellow eyes and a hooked grey bill, cut open at the front so **Doug's whole face stays visible**.
The hood top is at about local y -440, and the shotlist sets `doug_cap` on top of the hood at y -470 x scale. Doug wears
`gear: ["cap_off"]` here, so there is one cap per frame, logged in decisions.md. Bare pale-grey "scaled" leg covers
from the knee down are optional. Shots: s066-s068.

### `snake_eagle_costume_off`
**DONE (illustrator, 2026-11-12):** preview `assets/previews/045-black-mamba-warnings-assets-creatures.png` (+ `assets/previews/045-black-mamba-warnings-assets-thumbs.png` at 168x94).
The same suit lying crumpled on the ground: the felt tabard slumped, one cardboard wing bent, and the eagle hood lying on
its side with one yellow eye showing. Anchor bottom-centre, about 360 x 120. Shot: s069.

### `horse_gallop`
**DONE (illustrator, 2026-11-12):** preview `assets/previews/045-black-mamba-warnings-assets-creatures.png` (+ `assets/previews/045-black-mamba-warnings-assets-thumbs.png` at 168x94).
The library `horse` palette (chestnut `#a0522d`, dark mane and tail, white blaze) in a full **gallop**, side view facing
right: legs extended front and back, mane and tail streaming, ears forward. The expression is neutral, not panicked. It
wears a brown saddle with its **seat top at about (-20,-330)** (Doug sits there with `pose: sit`). No rider is drawn.
Anchor bottom-centre (the lowest hoof on y 0), about 720 x 520. Shots: s006-s008, s011, s013.

---
**Illustrator, 2026-11-12: all 22 drawings are done.** Previews are in `assets/previews/045-black-mamba-warnings-*`: `-assets-props.png`,
`-assets-snakes.png`, `-assets-creatures.png`, `-assets-thumbs.png` (168x94 read test), `-in-context.png` (coiled mamba on the mound
top, `doug_cap` at y -510, hood silhouette) and `-costume-horse-on-doug.png` (the costume on stand/walk Doug, Doug `sit` in the saddle).
The generator scripts are in `build/art/` (git-ignored scratch).

---

## Art-review fixes (illustrator, 2026-11-12)
**DONE:** all 5 fixes from `art_review.md`. Previews are `assets/previews/045-black-mamba-warnings-assets-fixes.png` (sheet; tall drawings are cropped there as before) and
`assets/previews/045-black-mamba-warnings-fixes-closeup.png` (close-up `studio art` render). Anchors are unchanged and the bboxes stay within the requested sizes.
1. `brown_snake_eagle`, `_glide`, `_carrying_mamba`: the far eye is now about 60% size and drawn behind the head, so it peeks out over the front contour just above the bill base (3/4 view). It no longer touches the bill. The near eye and brow are unchanged. The costume hood is untouched.
2. `mongoose`: four slim tapered legs. The hind legs have a forward knee and a backward hock, the front legs have an elbow bend, and all four have small dark paws with toe ticks.
3. `snake_eagle_costume_off`: now one overlapping heap. The tabard is slumped with its top folded over, and shows the neck hole, a flopped shoulder strap with buckle, and the scalloped rows and hem. One cardboard wing lies diagonally across it, with a scalloped feathered trailing edge, feather slots, a crease where the outer panel bends up, and a dangling arm strap. The hood lies on its side against the right of the pile.
4. `cobra_hooded`: the head is in profile, about 0.4 of the hood width, set in front of the hood's top centre. Its snout and eye point left, it has a straight closed mouth and a heavy brow, and the snout tapers.
5. `mamba_combat_pair`: the necks are pressed together and lean inward. The right male arches over and bears down across the left male's neck (head facing left, snout tilted down). The left male shoves up under its jaw (head facing right). Both mouths are closed, and the heads sit at y about -416 and -358.
Generators: `episodes/045-black-mamba-warnings/build/art/{birds,creatures,more,mambas}.py`.
