# 039-chimp-family-tree: asset requests (director)

House style: creatures, places and props are drawn in the detailed tier (outlines 4-6, flat fills, interior shading with `spray`,
darker backs and lighter bellies). Doug's costumes are worn props (anchor = Doug's hips, listed after Doug at the same x/y/scale).
Everything faces **right** unless noted. Sizes are local units at scale 1.

**I laid out the shotlist against the anchors and extents below.** I rendered a stand-in pass with magenta boxes of exactly these
extents (`episodes/039-chimp-family-tree/build/asset_specs.json`, `build/render_standins.py`) and checked it on contact sheets, so please
keep them. If something has to move, tell me and I will re-place it.

24 new drawings (5 of them costumes, the brief's cap). Priority by shot count: `chimp_costume` (40 shots), `red_colobus` (22),
`chimp_head_icon` (18), `chimpanzee_standing` (18), `bushbaby` (15), `fruit_tree` (12), `bonobo` (11).

## Rules for every drawing in this episode (CD brief section 7)
- **Kid appeal is HIGH (chimps are a kids' and meme favourite).** Adult apes only, real proportions, unsmiling, small dark eyes under a
  heavy brow, **no eye shine, no smiles, no blush, no baby chimps, no clothes on any animal, no bananas.** Match the existing
  `chimpanzee.json` / `chimpanzee_sitting.json` look exactly (black-brown coat #2e2620-ish with brown hair strokes, bare grey-tan face,
  heavy brow, big ears).
- **No gore.** No wounds, no blood, no bodies, no meat, no dead animals. The spear tip never touches anything in a drawing.
- **Silhouettes:** `chimpanzee_standing`, `chimpanzee`, `chimp_head_icon`, `bushbaby`, `fruit_tree`, `hollow_tree`, `leaf_nest`,
  `maize_sack`, `chimpanzee_old_male` are also used as `silhouette: true` with a thin red or grey `rim` on night/black backgrounds, so each
  needs a clear outer shape (separated limbs, readable head) that reads as that thing in solid black.
- Costumes: Doug's head, face and red cap stay fully visible; the cap always sits on top; nothing cute (no big eyes on hoods, no smiles).

## Episode palette (for reference; the shotlist draws the backgrounds)
| Item | Backdrop |
|---|---|
| Cold open + 1 The Spear (Fongoli, Senegal) | dry savanna: sky `#f6dcae`, grass `#d9b45a` |
| 2 The Monkey Hunt (Ngogo, Uganda) | sky `#cfe9ff`, forest floor `#2e8b3a` |
| 3 The Gorilla (Loango, Gabon) | overcast `#b9c4a8`, forest `#2e4a2e`, ground `#4a3b2a` |
| 4 The Human (Bossou farm edge) | `#f6c45a` sky, maize field `#c9c46a`, track `#a07a4a`, forest edge `#1d5e27` |
| 5 The Bonobo (Congo River) | `#e8c39a` sky, river `#9a7a4a`, south bank `#6fb24f` |
| 6 The Patrol (dusk ridge) | `#b8573a` / `#7a3b3a`, ridge `#3a3428` |
| 7 The Neighbours | late dusk `#4a3f5e`, ground `#33302a` |
| 8 The Old King (Fongoli at night) | `#1b2f5a`, ground `#2b3d33` |
| 9 The Split | near-black `#0b1020`, ground `#141e1a` |
| Death beats / cards | `#0b0f14` / cream `#f4f1dc` / sober `#15181a` |

So: the chimp coat must read on light sand, green, overcast olive **and** on dark dusk purple and night blue. Keep a slightly lighter
brown rim/hair-stroke on the back and a grey-tan face, as in `chimpanzee.json`.

HUD (drawn by the shotlist, no request needed): `DOUG DEATHS: N` at (1590,162); the **FAMILY TREE** sign is a small cream board at
x 1090-1228, y 98-266 (trunk, five side twigs, CHIMP at the tip, a red dot that climbs one twig per item, a red ring for SAME GROUP);
the `SPLIT: ...` label (size 26) is right-aligned to x 1814 at y 238. Values only from facts.md.

Reused from the library, no request needed: `chimpanzee`, `chimpanzee_sitting`, `silverback_gorilla`, `silverback_walking`,
`gorilla_icon`, `african_bush_elephant` (silhouette only, as the forest elephant), `africa_map`, `world_map`, `tanzania_map`,
`field_guide_open`, `paper_crown`, `doug_cap`, `chalkboard`, `calendar`, `clipboard`, `signboard`, `record_book_open`, `dna_strand`,
`magnifying_glass`, `clock`, `phone`, `ear_icon`, `music_note`, `soccer_ball`, `tree_branch`, `tree_stump`, `rainforest_tree`,
`tall_savanna_tree`, `acacia_tree`, `savanna_bush`, `grass_tuft`, `narrator_hand_pencil`, `question_mark`, `exclamation_mark`,
`warning_triangle`, `red_x`.
Drawn with primitives in the shotlist: the FAMILY TREE sign and the big family-tree cards, chalk lines, territory blobs, bar charts,
calendars grids, football pitches, the playground, the river cross-section, sound marks, the town sign text, the name tag.

---

## Creatures

### `bushbaby`
- **What:** lesser bushbaby (Senegal galago, *Galago senegalensis*), a small nocturnal prosimian; adult.
- **Look:** sitting upright on a branch, three-quarter view facing right. Soft grey-brown fur `#9a8a74` with a paler cream-grey belly
  `#d8cdb8`, darker eye rings. **Very large, thin, rounded ears** (pinkish-grey insides `#c9aea0`, translucent look via a lighter centre),
  large dark eyes but **no shine, flat unimpressed look under a slight brow**, small nose, long thin bushy tail curling down past the branch,
  long hind feet gripping. Adult and real, not a plush toy.
- **Size/anchor:** bottom-centre = where it sits on the branch; x -110..130, y -260..0 (tail may hang below y 0 to +80, inside x -110..130).
- **Facing:** right. Used tiny (0.32-0.42) on the family-tree cards and as a black silhouette inside the tree hollow (s012).
- **Shots:** s012 (silhouette), s019-s021, s047-s048, s074-s075, s098-s099, s102, s196-s198, s204.

### `red_colobus`
- **What:** an adult male Ugandan red colobus (*Piliocolobus tephrosceles*), a true monkey.
- **Look:** seated on a branch, facing right. **Red-brown crown and cap of fur** `#b0482a` on the head, dark charcoal-grey back and shoulders
  `#4a4440`, pale grey-cream belly and limbs `#c8beb0`, dark bare face with a short muzzle, small eyes (no shine), no thumb visible. A
  **very long thin tail hanging straight down** below the branch to about y +260. Calm, alert, unsmiling.
- **Size/anchor:** bottom-centre = the seat on the branch (y 0); x -130..150, y -340..+260 (tail).
- **Facing:** right (used flipped as the defenders facing the chimps).
- **Shots:** s027-s032, s035-s036, s043-s045, s047-s048, s074-s075, s098-s099, s102, s196-s198, s204 (also small 0.26-0.32 in rows/groups).

### `bonobo`
- **What:** an adult bonobo (*Pan paniscus*).
- **Look:** seated on the ground, facing right. Slimmer than `chimpanzee_sitting`, longer legs. Black coat `#1f1b18` with dark-brown hair
  strokes, **black face** (not grey-tan), small ears, **hair parted down the middle on top of the head** (long side whiskers), reddish-pink
  lips closed. Unsmiling, calm. Same detail tier as `chimpanzee_sitting`.
- **Size/anchor:** bottom-centre (rump/feet on y 0); x -140..170, y -380..0.
- **Facing:** right (also used flipped).
- **Shots:** s100-s102, s104, s112-s114, s196-s198, s204.

### `chimp_head_icon`
- **What:** small flat icon of an adult chimp head and shoulders, front view (crowds, counts, the classroom, the football team, the 200-strong community).
- **Look:** black-brown fur `#2e2620`, grey-tan face `#b8a48a`, heavy brow, big round ears out to the sides, small dark eyes (no shine),
  closed flat mouth. Thick black outline with a mid-brown rim highlight so it reads on cream, green, dusk and near-black. Same family as `gorilla_icon`.
- **Size/anchor:** centre; x -60..60, y -60..60. Used at 0.3-0.8 (dozens per shot).
- **Shots:** s033, s056, s058, s063, s069-s071 (silhouette on the ridge), s077-s079, s090, s124-s125, s180, s182-s183, s194-s195.

### `chimpanzee_standing`
- **What:** the same adult male as `chimpanzee.json`, **standing upright on two legs** in a display posture.
- **Look:** upright, slightly hunched, long arms hanging to the knees, **hair standing on end** along the shoulders and arms (bristling
  outline), heavy brow, flat stare. No raised fist, no open mouth, no weapon.
- **Size/anchor:** bottom-centre (feet on y 0); x -120..140, y -520..0.
- **Facing:** right (used flipped).
- **Shots:** s003-s004, s061 (ring of silhouettes), s065, s067, s119, s128, s153, s158, s161, s173, s176, s200-s202, s205, s207-s208
  (mostly silhouettes with a grey or red rim).

### `chimpanzee_old_male` (Foudouko)
- **What:** Foudouko, Fongoli's former alpha male, older, sitting alone at the woodland edge.
- **Look:** built on `chimpanzee_sitting` (same pose and footprint), but older: **grey-white hairs on the chin and lower back**, thinning
  hair and a balding brow ridge, thinner arms, a slightly drooping lower lip (closed). Flat, tired stare. Not frail-pitiful, not cute.
- **Size/anchor:** bottom-centre, x -134..178, y -368..0. **Head top at about local (+95, -368)**: a `paper_crown` is perched there in
  s175-s176 (crown anchor (1226,700) at scale 0.36 with the chimp at (1150,864) scale 0.8). Keep the head top near that point.
- **Facing:** right.
- **Shots:** s155 (silhouette), s158 (silhouette), s160, s162, s173-s176, s179.

### `chimpanzee_spear_bite`
- **What:** the cold-open image: an adult chimp shaping a spear with its teeth (Fongoli).
- **Look:** seated, facing right, holding a straight stripped stick (about 75 cm, pale peeled wood `#c9a87a`) in both hands, the **tip held
  between the front teeth**, eyes looking down along the stick. Same coat and face as `chimpanzee.json`.
- **Size/anchor:** bottom-centre, x -150..220, y -400..0 (the stick may run out to x +220).
- **Shots:** s002.

### `chimpanzee_spear_jab`
- **What:** an adult chimp jabbing a spear into a tree hollow.
- **Look:** standing upright, facing right, both hands gripping the stick and thrusting it forward and slightly up; **spear tip at about
  local (+350, -300)**. Focused, flat expression. The tip ends in clear air (the shotlist places the hollow beyond it).
- **Size/anchor:** bottom-centre, x -150..360, y -430..0.
- **Shots:** s011.

### `chimpanzee_spear_carry`
- **What:** a smaller female/adolescent chimp walking to a hunt with her spear.
- **Look:** knuckle-walking on three limbs, facing right, one hand holding the stick so it rests along her shoulder and points forward.
  Slimmer and smaller-headed than the male (we place her at 0.5-0.9). Adult female, not a baby.
- **Size/anchor:** bottom-centre, x -200..240, y -300..0.
- **Shots:** s010, s018, s026, s159.

## Doug costumes (5)

### `chimp_costume`
- **What:** Doug's chimp costume for items 5-9, played straight.
- **Look:** dark brown-black shaggy bodysuit `#3a2c22` with lighter brown fur ticks `#6a5440` and a **mid-brown outline highlight** so it
  reads on night blue and near-black; pale tan chest patch; **hood as a C round the back of the head and under the chin, with two big
  round tan chimp ears `#c9a27a` sticking out sideways**; fur leg sleeves down to the feet. **Sleeveless at the arms** (fur vest only to the
  shoulders), so Doug's own arms stay free in every pose. No mask, no ape face: head, face and cap fully clear.
- **Poses it must fit:** `stand`, `walk1`, `walk2`, `point`, `wave` (anchor = hips, list after Doug at the same x/y/scale; flipped when he faces left).
- **Size:** bbox about x -150..150, y -330..160.
- **Shots:** s115-s119, s121-s122, s128, s130-s134, s137, s150-s152, s156-s162, s173-s176, s179-s184, s186, s191, s195, s200-s202.

### `chimp_costume_sit`
- **What:** the same chimp costume fitted to the `sit` pose (hip drop 70), for the bonobo group.
- **Size:** bbox about x -110..170, y -260..115. The shotlist pins a small white `BONOBO` name-tag label on the chest at about (+15, -40) x scale; keep that area plain.
- **Shots:** s111-s113.

### `gorilla_suit_dark`
- **What:** Doug's **dark** gorilla suit for The Gorilla. The art director may make it a recolour of `white_gorilla_suit` (same geometry), but it must read **dark**, never white.
- **Look:** charcoal `#3a3a3a` shaggy felt with grey fur ticks `#6a6a6a`, a lighter grey saddle patch on the back (silverback joke),
  hood C and small crest with brow ridge on the cap dome as in the white suit. Grey `#8a8a8a` outline highlight so it reads on the olive forest.
- **Pose:** `sit` (anchor = hips, hip drop 70). Also used once lying empty on the ground, `rotate: -80` (s091), so it must read as an empty suit.
- **Size:** bbox about x -100..170, y -260..115 (same as `white_gorilla_suit`).
- **Shots:** s068-s071, s089-s091.

### `bushbaby_costume_sit`
- **What:** Doug's bushbaby costume, asleep curled in the tree hollow.
- **Look:** grey-brown fur onesie `#9a8a74` with a cream belly, fitted to `sit`; hood C round the head with **two huge round thin ears**
  standing up behind the cap (pink-grey insides); a long bushy tail curling round in front of his feet. **No eyes on the hood, nothing cute.**
- **Size:** bbox about x -120..180, y -330..115.
- **Shots:** s022-s023 (Doug at scale 0.34 inside the hollow, expression `sleepy`).

### `red_colobus_costume_sit`
- **What:** Doug's red colobus costume, sitting on a branch behind three big colobus males.
- **Look:** dark charcoal-grey suit with pale grey-cream limbs and belly, a **red-brown fur ruff round the cap** (the colobus crown, around
  the cap, never over it), hood C, and a **very long thin tail hanging straight down** to about y +400.
- **Pose:** `sit` (hip drop 70).
- **Size:** bbox about x -120..170, y -280..400.
- **Shots:** s042-s045.

## Places and props

### `hollow_tree`
- **What:** a thick savanna woodland tree trunk with a day-roost hollow (Fongoli).
- **Look:** grey-brown bark `#7a6650` with vertical bark strokes, **broken-off top at y -640 (no crown, so it stays clear of the HUD)**,
  two short stub branches. One **dark oval hollow** centred at (0,-360), rx 90, ry 110 (spans y -470..-250), interior `#1a120c` with a
  little depth shading, and a **flat lip/ledge at y -270** along its lower edge (the cap rests there; Doug sits inside on it).
- **Size/anchor:** bottom-centre; x -180..180, y -640..0.
- **Shots:** s005-s006, s010-s012, s022-s024 (s024 as a dim silhouette), s159.

### `leafy_stick` / `stripped_stick` / `chimp_spear`
- **What:** the three stages of a Fongoli spear, about 75 cm each, horizontal, pointing right.
- **Look:** `leafy_stick`: a freshly snapped branch with side twigs and green leaves. `stripped_stick`: the same stick with twigs and
  leaves removed, pale peeled wood `#c9a87a`, small knot scars. `chimp_spear`: the stripped stick with the **right end chewed to a rough point**
  (frayed bite marks, no colour on the tip).
- **Size/anchor:** centre; `leafy_stick` x -300..300, y -60..60; the other two x -300..300, y -25..25 (tip at x +300).
- **Shots:** leafy/stripped s007-s008; `chimp_spear` s008-s009, s023, s157, s159 (rotated -75 leaning on a tree).

### `fruit_tree`
- **What:** a big rainforest fruit tree at Loango where chimps and gorillas both feed.
- **Look:** thick buttressed grey-brown trunk, a broad dark-green crown with clumps of **round yellow-orange fruit** (generic, not figs, not bananas).
- **Size/anchor:** bottom-centre; x -360..360, y -720..0 (crown y -720..-380, trunk clear below it so apes can sit at its foot).
- **Shots:** s053-s055, s065, s067-s071, s072 (dim silhouette), s147-s148 (tiny, 0.3, on the territory map).

### `maize_stalk`
- **What:** one mature maize plant at the edge of a Guinean farm.
- **Look:** tall green stalk with long drooping leaves, a tassel on top, one husked cob half-showing on the side.
- **Size/anchor:** bottom-centre; x -70..70, y -420..0. Used in rows of five at 0.8-0.85.
- **Shots:** s084, s087-s088, s093-s094.

### `maize_sack`
- **What:** Doug's sack of maize (crop context of the Bossou attacks).
- **Look:** tan burlap sack (like `burlap_sack`) tied at the neck, with **three yellow maize cobs poking out of the top**.
- **Size/anchor:** centre; x -90..90, y -100..100. Carried behind Doug's shoulder at 0.45 and lying on the track at 0.8-0.9 (the cap sits on top).
- **Shots:** s093-s095, s097.

### `leaf_nest`
- **What:** Doug's "tidy leaf nest" in the taken territory (a chimp-style sleeping nest of bent leafy branches, here on the ground).
- **Look:** an oval bowl of interwoven green leafy branches `#3f7a32`, darker inside, a few twig ends, neat. Top surface at y -100.
- **Size/anchor:** bottom-centre; x -210..210, y -140..0.
- **Shots:** s150-s154 (s153 has `doug_cap` sitting in it; s154 as a dim silhouette).

### `chimp_hand_reach`
- **What:** a large adult chimp arm and hand entering **horizontally from the right edge** and gripping the top of Doug's sign.
- **Look:** black-brown hairy forearm, grey-tan bare fingers and palm, fingers curled over (grip point at the anchor). The arm runs off to the right.
- **Size/anchor:** anchor (0,0) = grip point; x -60..520 (arm to the right, off-frame), y -110..70. Must stay clear of the HUD (it enters at y ~670).
- **Shots:** s152.

### `armwrestle_photo`
- **What:** the 011 callback: a small framed photo of Doug losing an arm-wrestle to a chimp.
- **Look:** wooden frame with glass glare (like `family_photo_frame`), inside: crude Doug (red cap, gritted teeth) and an adult chimp at a
  small table, hands locked, Doug's arm clearly going down, the chimp's face flat and bored. Crude-tier Doug, detailed-tier chimp.
- **Size/anchor:** centre; x -160..160, y -120..120 (used at 1.8).
- **Shots:** s092.
