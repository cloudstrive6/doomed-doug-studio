# 056-king-cobra-snake-eater: asset requests (director, 2026-11-23)

The shotlist already places these by name, so please keep the **anchor, bounding box and key points** given here.
The generator (`episodes/056-king-cobra-snake-eater/build/gen_shotlist.py`, git-ignored scratch) places things relative to
them: Doug's cap on the nest top, the ticket in Doug's hand, the HUD-safe tops of reared snakes. Everything **faces right**
unless noted (the shotlist flips). House style: detailed tier, thick black outlines (5-6), flat fills with interior shading,
documentary-cartoon. **Never cute**: no big eyes, no smiles, no pastel nursery look (hatchlings especially). No blood,
no venom drops, no wounds, no partly digested prey.

Reused from the library (no request): `india_map`, `malaysia_map` (has the Singapore dot), `black_mamba_reared` (045 callback,
s086/s092-s093), `snake_jaw_below`, `snake_jaw_below_spread`, `snake_enclosure`, `frog`, `rat`, `large_dog`,
`brown_dog_walking`, `great_white_shark`, `shark`, `sofa`, `house`, `front_door`, `red_barn`, `rainforest_tree`, `tree_branch`,
`fallen_log`, `fern`, `leaf`, `tree_stump`, `signboard`, `journal_paper`, `highspeed_camera`, `tourist_camera`, `scientist`,
`scientist_woman`, `stick_man_plain`, `binoculars`, `clipboard`, `calendar`, `kitchen_timer`, `wait_stopwatch`, `clock`,
`hand_bell`, `price_tag`, `dinner_plate`, `silver_fish`, `meat_strip`, `radio_collar`, `doug_cap`, `gravestone_plain`, plus the
annotation set (`question_mark`, `exclamation_mark`, `warning_triangle`, `red_x`).

---

## Palettes (binding; CD decisions.md 2026-11-23)

- **King cobra** (*Ophiophagus*): long olive / khaki body `#6b7a3a`, darker olive back `#4f5a2a`, **pale cream-yellow chevron
  bands** `#e8e0a8` (thin, pointing toward the head, about 14-18 along the body, fading toward the head), pale yellow throat
  `#e8d890`, large smooth head shields, a small dark eye with a heavy brow, a **narrow** hood (barely wider than the neck,
  never the wide Naja disc). Mouth lining when open: pale pink-grey `#c8a0a0` (not the mamba's ink black). It must not read
  as the 045 grey mamba (`#7f8865`) or as `cobra_hooded` (wide yellow-brown hood). Longer and heavier than any other snake in
  the episode.
- **Banded krait** (*Bungarus fasciatus*): bold, equal-width **black and bright yellow** `#f2d21a` rings, blunt rounded tail
  tip, a raised ridge along the spine (triangular cross-section reads as a slight peak on the back line), black head with a
  yellow chevron on the nape. This is the thumbnail krait.
- **Common krait** (*B. caeruleus*): glossy **blue-black** `#1e2330` with thin **paired white crossbands** `#f0f0f0`, small
  head, mid-tone highlight `#3a4256` on the back so it reads on night scenes. **Must never be shown inside a king cobra**
  (CD packaging guard): it only appears on its own, as the night-hut krait.
- **Indian rat snake** (*Ptyas mucosa*): warm brown / olive-brown `#8a6a3a` with faint darker crossbars toward the tail,
  pale yellow belly, **large round eye** with a dark ring (not cute: neutral, side-on). Harmless-looking.
- **Indian cobra** (*Naja naja*): mid-brown `#7a5a32`, **wide spread hood** with the pale **spectacle mark** on the back of
  the hood shown slightly turned, cream throat. Clearly smaller and wider-hooded than the king cobra.
- **Pit viper** (Malabar / bamboo type): bright leaf green `#5fae3a` with a paler belly line, **triangular head**, a small
  orange-yellow eye with a vertical pupil, heat pit dot in front of the eye.
- **Clouded monitor** (*Varanus nebulosus*): grey-brown `#7a6a52` with **pale cream clouded spots** in rough bands, long
  slender neck, long tail, strong clawed legs, calm half-lidded eye. Mid-tone (it lives on night scenes `#1b2f5a`/`#2b3d33`).
- **Reticulated python**: thick body, gold-tan `#c9a24a` with a black **net pattern** enclosing grey-tan diamonds and small
  white flank spots, a dark line through the eye. Clearly heavier but shorter than the king cobra.

---

## King cobra drawings (one geometry family; they cut against each other)

### `king_cobra_reared` (48 shots: the episode's hero drawing)
The king cobra reared about a third of its length, facing right, front body nearly upright, **narrow hood** slightly spread,
head held level, mouth closed, the rest of the body in loose flat ground coils trailing left. Anchor **bottom-centre** (ground
y 0). Bbox **x -320..+200, y -600..0**; head centre about (+110,-560), mouth tip (+190,-555). Used at 0.5-1.15 and flipped.
Must read at 0.5 in a row of four (s209-s213) and as a silhouette with red glow (s004, s016, s194).
Shots: s002, s004, s016, s017, s019, s020, s024, s027, s069, s070, s078, s079, s082, s084-s086, s088, s093, s095, s098, s112,
s113, s115, s130, s131, s135, s146-s148, s156, s166, s167, s185, s187-s190, s194, s195, s203, s209-s214, s217, s218 (+ more).

### `king_cobra_reared_gape`
**Same pose and geometry** as `king_cobra_reared`; only the mouth changes: open about 35 degrees (pale pink-grey lining, two
small fangs at the front, no drool). Used for the growl (item 4) and the frozen half-hour (item 5).
Shots: s047, s090, s099, s116, s117.

### `king_cobra_crawl`
The whole king cobra stretched out on the ground in a long, shallow S, head raised a little at the right, **forked tongue
flicking** forward. Anchor bottom-centre. Bbox **x -520..+560, y -110..0**, head about (+470,-55), tongue tip (+560,-55).
Also used rotated -80 climbing a trunk (s031) and small (0.35-0.5).
Shots: s030, s031, s033-s035, s041-s043, s049, s056-s059, s064, s104, s106-s108, s123, s124, s153, s154, s174, s184, s203, s215.

### `king_cobra_strike`
Front third raised off the ground and lunging right, mouth wide open, the rest of the body on the ground behind. Anchor
bottom-centre. Bbox **x -450..+470, y -320..0**, open mouth at about (+450,-260). Used biting a stone, a rat snake, a viper, a
bullfrog and a python. Shots: s036, s037, s050, s072 (flipped, at Doug's feet), s110, s132, s137, s138, s157.

### `king_cobra_swallowing_<prey>` (5 palette variants of ONE drawing)
The king cobra lying on the ground, head at the right, its jaws stretched around the **rear end of a prey snake that leaves
its mouth and lies on the ground to the right** (prey goes in head first, so only the **tail end** is visible, about 400
long, ending in a tail tip). Cobra body x -560..+150, head about (+120,-70); prey x +150..+560. Anchor bottom-centre, bbox
**x -560..+560, y -140..0**. A slight lump in the cobra's neck. No blood. Variants, only the prey's colours change:
- `king_cobra_swallowing_krait`: banded black/yellow krait tail (s018). Matches the thumbnail.
- `king_cobra_swallowing_rat_snake`: brown rat snake tail (s051-s054, s063).
- `king_cobra_swallowing_naja`: Indian cobra tail, mid-brown (s080).
- `king_cobra_swallowing_viper`: short green pit-viper tail, prey part only ~200 long (s114, s118).
- `king_cobra_swallowing_king`: **olive with pale chevrons**, the same as the king cobra; the prey body is a bit thinner so the
  two read as big and small (s196, s197, s199, s204, s216).

### `king_cobra_bulge`
After the meal: the king cobra lying stretched out with a **long smooth bulge** in the middle of the body (centre about (0,-100)
at the top), head at the right resting on the ground, eye half-closed, smug-flat. Anchor bottom-centre, bbox **x -520..+520,
y -130..0**. This is the swallowed-Doug death image (the `doug_cap` sits on the ground beside it, about x +600). The bulge is a
plain rounded swelling, no outline of a body inside it.
Shots: s026, s065, s073, s074, s100, s149, s150.

### `king_cobra_head_tongue`
Close-up of the king cobra's head and neck in profile facing right, big head shields, eye, nostril, and a long **forked
tongue** out and flicking (two tips, dark grey-pink). Anchor centre, bbox **x -350..+380, y -200..+200** (tongue tips near
(+370,+40)). Shot: s032.

### `king_cobra_fight`
Two adult king cobras locked in a fight: front bodies wrapped round each other in a rolling tangle, each with its mouth
**clamped on the other's neck** (no wounds, no blood), tails splayed. One slightly smaller. Anchor centre, bbox **x -400..+400,
y -225..+225**. Shots: s201, s202.

### `king_cobra_hatchling`
A hatchling king cobra: slim, **near-black with thin pale yellow crossbands**, small head, adult proportions (small eye, no
baby-face, no big eyes), loose S. Anchor centre, bbox **x -150..+150, y -45..+45**. Shots: s184, s185, s193, s194.

---

## The nest (item 8 + the closing)

### `king_cobra_nest`
A big **mound of dead leaves** on the forest floor: brown/tan/rust leaves `#8a5a2a` / `#b07a3a` / `#c99a5a` heaped into a
rounded dome, a few twigs, lit upper-left, darker base. Anchor bottom-centre, bbox **x -380..+380, y -280..0**; **flat-ish top
at (0,-280)** where the shotlist rests `doug_cap` and the `deli_ticket_9` in the closing (s220-s221). Must stay distinct from the
Komodo `nest_mound` (earth, not leaves). Mid-tone: it is used on dusk `#b8573a`/`#7a3b3a` and the closing slate `#2a2030`.
Shots: s171, s172, s178, s186-s190, s220, s221.

### `king_cobra_on_nest`
The same mound with the **female coiled on top** (loose coils on the top, head resting on the coils facing right, alert eye).
Same anchor and mound geometry; coils rise to about y -420. Shots: s173, s175, s176, s181, s183, s191, s192.

### `king_cobra_nest_cutaway` and `king_cobra_nest_cutaway_empty`
The same mound with a **cross-section window** in the front showing a hollow chamber (darker brown) inside. `_cutaway` has
about 20 white leathery eggs (elongated ovals, faint grey shading) in the chamber; `_empty` has the bare chamber. Same anchor
and bbox. The cut edge is a clean leaf-litter edge (no meat-coloured interior). Shots: s177 (empty), s179, s180, s184.

---

## Other snakes and the lizard

### `banded_krait`
Banded krait in a relaxed horizontal S, head right, closed mouth. Anchor centre, bbox **x -320..+320, y -60..+60**. Shots: s002,
s016, s017, s019, s020, s021 (silhouette), s086, s139, s140, s170.

### `common_krait`
Common krait in a horizontal S, head right. Anchor centre, bbox **x -320..+320, y -55..+55**. Used as a red-glow silhouette
in the night hut (s005-s007) and in colour on night scenes. Shots: s005-s007, s009, s010, s012, s014, s015, s017.

### `krait_swallowing_krait`
A common krait with a **smaller common krait's tail** going into its mouth (same rules as the king cobra swallowing drawings).
Anchor centre, bbox **x -400..+400, y -70..+70**. Shot: s013.

### `indian_rat_snake`
Indian rat snake in a horizontal S, head right, alert, mouth closed. Anchor centre, bbox **x -380..+380, y -60..+60**.
Shots: s027 (silhouette), s028, s033, s038-s040, s045, s050, s059, s064, s068, s071, s075, s139, s140, s170.

### `indian_rat_snake_puffed`
The rat snake's defence: front body raised in an S, **throat puffed out** wide (a balloon-like swollen neck), mouth slightly open,
growling. Anchor bottom-centre, bbox **x -210..+210, y -380..0**, mouth about (+180,-300). Shots: s046, s047, s069, s070
(flipped, mouth at the king cobra's head).

### `indian_cobra`
Indian (spectacled) cobra reared with its **wide hood** spread, head level, facing right. Anchor bottom-centre, bbox **x -220..+160,
y -480..0**. Clearly smaller than `king_cobra_reared` at the same scale. Shots: s002, s076 (silhouette), s077, s079, s081, s083-s086,
s089, s101, s170.

### `pit_viper_green`
A small green pit viper in a compact coil, head right, as if resting on a branch (no branch in the drawing). Anchor centre, bbox
**x -140..+140, y -65..+65**. Shots: s102 (silhouette), s103, s109-s111, s113, s115, s119-s125, s170, s212.

### `clouded_monitor`
Clouded monitor lizard walking right, side view. Anchor bottom-centre (feet on y 0), bbox **x -380..+340, y -150..0** (tail to
the left). Used as a silhouette (s127, s148) whose outline should loosely match a crouching Doug, so keep the head up and the
legs clear. Shots: s127-s129, s131, s132, s134, s139, s140, s142, s148, s150, s170.

### `reticulated_python`
Reticulated python stretched in a heavy S on the ground, head right. Anchor bottom-centre, bbox **x -620..+620, y -170..0**.
Shots: s151 (silhouette), s152, s154, s157, s160, s166, s170.

### `cobra_python_dead_pair`
The 2018 pair as a cartoon "photo": a reticulated python **coiled twice around a king cobra**, the cobra's mouth near the back of
the python's head, both lying still with **cartoon X eyes**. No blood, no wounds. Anchor centre, bbox **x -400..+400,
y -175..+175**. Sits inside a cream photo frame. Shots: s161-s163.

### `snake_knot_doug`
Doug's item 7 death: a **cartoon knot** of the king cobra (olive/chevrons), the python (net pattern) and Doug's empty **python
tube suit** (zipper visible, X-eyed empty face hole, no body), all tied together like a pretzel. Both snakes' heads poke out
with X eyes. Anchor bottom-centre, bbox **x -300..+300, y -320..0**; a flat spot on top at **(0,-330)** where `doug_cap` sits.
Shots: s168, s169.

---

## Doug's snake costumes (worn props; art director signs off: one base drawing + palette variants)

**Base**: a zipped **tube suit** from the neck to the ankles over Doug's `stand` rig, covering both legs as one tube
(wide enough at the bottom for leg spreads up to the `walk1/walk2` and `arms_up` stance), with a front zipper, **arm holes** so
Doug's own arms show, an open neck so **head, face and red cap are fully visible**, and a **tail** trailing on the ground behind
him to the left (to about x -260, y +150). Anchor = Doug's hips (0,0), Doug scale 1 units (neck y -150, feet y +152); listed after
Doug at the same x/y/scale, flipped with him. Deadpan felt, never a mascot (no cartoon snake face on the suit).
Poses used: stand, point, hands_hips, thumbs_up, shrug, arms_up, cower, walk1/walk2, wave.

| Name | Pattern | Shots |
|---|---|---|
| `snake_costume_krait` | black and yellow bands | s023, s024 |
| `snake_costume_rat` | brown `#8a6a3a`, pale belly panel | s029-s059, s063-s071 (41) |
| `snake_costume_cobra` | brown, plus a **cardboard hood** `#c9a46a` taped on: two flat flaps either side of the head (x ±75..±135, y -330..-170), visible tape strips, never crossing the face | s078-s098 (15) |
| `snake_costume_cobra_droop` | as `_cobra`, the cardboard flaps **drooping** down to the shoulders | s099 |
| `snake_costume_python` | fat, wider tube, gold-tan with black net pattern | s152-s170 (12) |
| `snake_costume_king` | olive with pale chevrons, a **narrow** felt hood behind the neck (flaps only up to the jaw line), cap on his head reads as "on the hood" | s003, s004, s217, s218 |

### `snake_costume_rat_flat`
The rat snake suit lying flat for an `on_back` Doug (house convention: drawn for `rotate: -90` at Doug's x/y, shifted +30 x
scale; see the 003 `ammonite_costume_flat`). Zipper visible. Also used on its own lying on the ground as "the costume he took
off" (s145). Shots: s072, s145.

---

## Deli props (the NOW SERVING device)

### `deli_ticket_9` (117 shots)
A small paper deli queue ticket: off-white `#f4f1e8`, a perforated / torn top edge, a thin red band, and a **big bold black "9"**
printed in the middle. Anchor = **bottom-centre (the edge Doug's fingers hold)**, bbox **x -40..+40, y -110..0**. It is drawn at
Doug's scale (0.4-0.75) on his front hand, so the 9 must read at 40 px tall; keep the art minimal. Also lies on the ground rotated
(-70..-80) in death and closing shots. Shots: nearly every Doug shot (s003 onward).

### `deli_counter`
An empty deli counter, front view: a long glass display case (pale blue glass with highlight streaks, steel frame) with **empty**
steel trays inside, a pale wood top, and a red **ticket-roll dispenser** on a short post at the right end (top about (+430,-560)).
Anchor bottom-centre, bbox **x -500..+500, y -560..0**. No food, no text. Shots: s207, s222, s223.

### `takeaway_box_krait`
The library-style white takeaway box (folded flaps, wire handle) with a **banded krait's tail** hanging out over the rim.
Anchor centre, bbox about **x -80..+120, y -110..+90**. Shot: s022.

### `garden_rake`
A garden rake held by Doug: anchor = **the grip point in his front hand (0,0)**, the wooden handle runs down and forward to the
metal tine head at about **(+120,+150)** (Doug scale 1 units), tines touching the ground line at Doug's feet. Brown handle `#a0522d`,
grey tines. Shots: s186-s192.

### `rice_plants`
A tileable row of young rice shoots standing in shallow water: bright green `#7cc25a` / darker `#4f9a3a` blade tufts in neat rows,
a thin water-shine line at the base. Anchor bottom-centre, bbox **x -320..+320, y -150..0**. Used 4 across at 0.8 on the paddy
(`#8fb8a8` water). Shots: s028, s029, s033, s036, s037, s039, s040, s045-s047.

---

## For the art director (engine, not illustrator)

1. **Pose `all_fours`** (s147, s148: "Doug drops to all fours ... and now he looks exactly like a lizard"). Doug on hands and
   knees, body roughly horizontal, head up facing forward so the cap reads, hips at the usual y, hands and knees on the same ground
   line as `stand` feet. Until it exists the shotlist uses `crouch` as a placeholder; swap s147/s148 to `"pose": "all_fours"`
   once added (the clouded-monitor silhouette beside him in s148 is the visual rhyme).
2. **NOW SERVING HUD** (episode-only, staging only): drawn from elements on every shot from s005, under the death counter: a
   `#1a1a1a` rect x 1390-1790, y 212-266, `#5a5a5a` 5 px frame, red `#ff4a3a` bold size-26 text "NOW SERVING: n" centred at
   (1590,239). Ticks 1-9 by item, flips to red-on-pink (`#ffd2cc` / `#e0201b`, counter too) at s218 "His number has been called"
   and shows 10 in the closing. Reserved zone x 1300-1860, y 110-275 (checked for every new asset placement in the generator).
3. Costume sign-off (base + 5 variants above), the king cobra design (olive, pale chevrons, narrow hood; distinct from 045's mamba
   and `cobra_hooded`), and the hatchlings (not cute).

---

## Illustrator status (2026-11-23): DONE, 40 drawings in `assets/library/` (all except the art director's `all_fours` pose)

Previews (git-ignored, regenerate with `python -m studio asset-preview ...`):
`assets/previews/056-assets-kingcobra.png` (king cobra family), `assets/previews/056-assets-others.png` (nest family, other
snakes, lizard, python, dead pair, knot), `assets/previews/056-assets-props.png` (costumes, deli props, rake, rice).

- [x] King cobra: `king_cobra_reared`, `king_cobra_reared_gape`, `king_cobra_crawl`, `king_cobra_strike`, `king_cobra_bulge`,
  `king_cobra_head_tongue`, `king_cobra_fight`, `king_cobra_hatchling`, `king_cobra_swallowing_krait` / `_rat_snake` / `_naja` /
  `_viper` / `_king` (kingcobra sheet)
- [x] Nest: `king_cobra_nest`, `king_cobra_on_nest`, `king_cobra_nest_cutaway`, `king_cobra_nest_cutaway_empty` (others sheet)
- [x] Others: `banded_krait`, `common_krait`, `krait_swallowing_krait`, `indian_rat_snake`, `indian_rat_snake_puffed`, `indian_cobra`,
  `pit_viper_green`, `clouded_monitor`, `reticulated_python`, `cobra_python_dead_pair`, `snake_knot_doug` (others sheet)
- [x] Costumes: `snake_costume_rat`, `_krait`, `_cobra`, `_cobra_droop`, `_python`, `_king`, `snake_costume_rat_flat` (props sheet)
- [x] Props: `deli_ticket_9`, `deli_counter`, `takeaway_box_krait`, `garden_rake`, `rice_plants` (props sheet)

Notes for the director / art director (things that changed from the brief):
- `snake_costume_cobra`: the cardboard flaps sit at x ±134..±190 (not ±75..±135), because Doug's cap brim reaches x +128 and the
  right-hand flap would have covered it. Tape strips run below the chin.
- Costumes on `cower`: that pose drops Doug's head about 40 units, so the collar overlaps his chin. Place the suit at
  y + 40 x scale for cower shots (or use another pose).
- `deli_ticket_9`: the 9 is drawn with shapes, not text, so it turns with the ticket when it's rotated on the ground.
- Measured bboxes are in each JSON `description`. They differ a little from the brief (for example `king_cobra_crawl` y -86..0,
  `king_cobra_bulge` bulge top -108, `king_cobra_on_nest` coils to -423, `snake_knot_doug` top -338), but every anchor and key point is as requested.
- Generator scripts: `episodes/056-king-cobra-snake-eater/build/illus/` (scratch; `python build_all.py [names]` rebuilds them).

---

## Round 2 changes (illustrator, 2026-11-23; visual_review.md Round 1 items 5, 8, 13, 16)

Preview: `assets/previews/056-assets-round2.png` (regenerate with `python -m studio asset-preview journal_paper_cobra_python
king_cobra_swallowing_python king_cobra_crawl_tagged king_cobra_strike_tagged stopwatch_30min deli_counter --out 056-assets-round2.png`).
Generator: `build/illus/gen_r2.py`. I have not touched shotlist.json; the director needs to make the name swaps below.
I test-rendered s030, s132, s116, s158, s164 and s222 with these swaps applied and all six read correctly.

- [x] **Item 5, s158**: new **`journal_paper_cobra_python`**. It drops in for `journal_paper` (same centre anchor and 360x480 size).
  The engraved monitor-lizard plate is replaced by a colour photo of a dusk wetland with a king cobra swallowing a reticulated
  python. Director: in s158, change `journal_paper` to `journal_paper_cobra_python`. `journal_paper` itself is unchanged, so
  s133 and other episodes are not affected. If the photo looks small at scale 1.0, scale 1.2-1.3 still clears the
  WETLAND RESERVE label. There is also a new standalone **`king_cobra_swallowing_python`** (same family and bbox as the other
  `king_cobra_swallowing_*` drawings) if a full-size shot is wanted.
- [x] **Item 8, s030 / s132**: new **`king_cobra_crawl_tagged`** and **`king_cobra_strike_tagged`**. They have the same geometry
  and anchors as `king_cobra_crawl` / `king_cobra_strike`, plus a safety-orange radio collar on the neck (grey transmitter box with
  a red light, light-grey whip antenna). It reads on navy and on cream.
  Director: change the cobra asset name and **delete the `radio_collar` element** in both shots.
  - s030 (crawl at 1340,760 x0.7): the collar sits at about scene (1574,718). Move the RADIO TAG label to about (1574,620), just
    above it.
  - s132 (strike at 700,866 x0.8): the collar sits at about scene (776,743). Add a RADIO TAG label at about (600,640) if wanted.
- [x] **Item 16, s116 / s164**: new **`stopwatch_30min`**. It drops in for `wait_stopwatch` (same anchor and size), with a red
  hand pointing to 30 and the elapsed half of the face shaded pink. Director: change the name in s116 and s164.
  `wait_stopwatch` keeps its blank face because 022 overlays text on it.
- [x] **Item 13, s222 / s223**: **`deli_counter`** is fixed in the library, so no shotlist change is needed. The red ticket
  dispenser moved +20 (now x +406..+494, top at y -560), so at x=700 it sits fully behind the "10" box (x 1100-1520). In s207,
  which has no box, it still shows at the right end of the counter.
