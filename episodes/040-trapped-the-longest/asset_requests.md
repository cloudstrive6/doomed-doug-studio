# 040 asset requests (director, 2026-11-08)

House rules apply: thick black outlines, flat fills, detailed tier for creatures and places, crude tier for people.
Facing right unless noted. Never a drawn body, skull, bones of a person, blood or a baby mammoth (brief section 8).

## Travel stickers (same family as `sticker_naica` / `sticker_lechuguilla`)
About 112x60, centred anchor, slightly peeling corner, bold caps that stay legible at scale 0.3-0.5. They sit in the
`travel_suitcase` slots (x -120/0/+120, y -215/-150/-85) at the suitcase's scale. All are used in s170, s195 and s198-s202 (end slate).
| name | text | look | first shot |
|---|---|---|---|
| `sticker_nutty_putty` | NUTTY PUTTY | sandy tan rectangle, a small dark crack icon | s023 |
| `sticker_otztal_alps` | ÖTZTAL ALPS | pale ice-blue, white peak icon (keep the Ö umlaut legible) | s074 |
| `sticker_hoyo_negro` | HOYO NEGRO | dark teal oval, one small torch-beam icon | s100 |
| `sticker_kolyma` | KOLYMA | brown-grey, a white ice-wedge stripe | s125 |
| `sticker_yukechi` | YUKECHI | lilac-grey, a small blue lake shape | s146 |
| `sticker_hot_springs` | HOT SPRINGS | ochre, a little green-teal pond | s170 |
| `sticker_south_pacific_gyre` | SOUTH PACIFIC GYRE (two lines) | navy with a white swirl; may be ~130 wide | s198 |

## Creatures and specimens
- `permafrost_nematode`: Panagrolaimus kolymaensis, scientific-drawing nematode **curled in a tight C/coil (dormant)**, translucent
  pale cream-pink, blunt head, thin gut line. Same family as `devil_worm` but clearly a different pose. ~300x200, centre anchor.
  Shots s104, s105, s121, s122.
- `permafrost_nematode_active`: the same worm **uncurled in a lively S**, a few motion ticks at the tail. ~360x140, centre anchor.
  Used small (0.25-0.5) and many times (s106, s111, s114-s120, s123).
- `pandoravirus`: Pandoravirus yedoma, a **smooth amphora/oval particle** (lilac-grey #c8a0d8 with darker rim) with a **small round
  opening (ostiole) at one end** and a thin layered wall. Not spiky, not a "pandemic ball", no face. ~400x260, centre anchor.
  Used as silhouette (s126, s129) and full (s130-s145).
- `acanthamoeba`: Acanthamoeba host amoeba, microscope-diagram icon: irregular pale grey-green blob with **many fine spiky
  acanthopodia** (short thorn-like projections), one nucleus with a dark nucleolus, vacuoles. No face. ~360x280, centre anchor. s138-s140.
- `giant_ground_sloth`: Ice Age ground sloth (Nothrotheriops/Megalonyx type), standing on all fours, shaggy brown, long claws curled
  under, small head. Used **as silhouette** with a red rim (s088, s089). ~500x330, **bottom-centre anchor**.
- `gomphothere`: elephant relative (Cuvieronius type), elephant-like, straight-ish tusks, shorter trunk, slightly smaller than an
  elephant. Silhouette use (s088, s089). ~520x380, bottom-centre anchor.
- `columbian_mammoth`: adult Columbian mammoth, standing, facing right: very tall high-domed head, big curved tusks, **sparse** brown
  hair (not woolly), sloping back. Adults only. ~560x460, bottom-centre. Silhouette in s147; full in s151, s156, s165, s166 (also flipped).
- `woolly_mammoth`: adult woolly mammoth, shaggy reddish-brown long fur, smaller ears, curved tusks, shoulder hump. Not a calf
  (distinct from `baby_mammoth`). ~480x400, bottom-centre. s151.
- `short_faced_bear`: Arctodus simus, very long-legged, short-snouted bear, tawny-brown, standing on all fours. ~460x320, bottom-centre. s151.
- `neanderthal`: crude-tier stick person (Doug's tier, `auto_ink`), heavier brow ridge, simple fur wrap, neutral face; a plain "who was
  alive then" figure, no caricature. Feet anchor, same scale family as `stick_man_plain`. s111.
- `mammoth_pelvis`: one mammoth pelvis bone, off-white #efe2c0 museum-clean, front view (the butterfly-shaped hip girdle with two
  round openings). Animal bone only. ~360x260, centre anchor. s164 (four in a row).

## Props and places
- `mammoth_dig_layout`: the Hot Springs dig seen **from above** as a clean museum layout: tan sediment, white grid strings in
  squares, several cream mammoth bones (tusks, long bones, a skull dome) lying neatly in the ground, a wooden walkway edge along the
  bottom. No struggling animals. ~1500x800, centre anchor (fills most of the frame at scale 1.0). s149, s150.
- `mammoth_costume`: adult-coded deadpan mammoth suit worn over Doug's `stand`/walk poses (anchor = Doug's hips at scale 1, like
  `squid_costume`): brown felt body, sewn-on trunk hanging forward, two stiff felt tusks, Doug's head, flat face and red cap fully
  visible above. No cute eyes. If possible a small handle loop at the trunk tip where the suitcase could hang. s167, s168.
- `amoeba_costume`: grey #a9adb3 felt blob suit with one big darker nucleus patch on the belly, a few stubby pseudopod lobes, worn
  over `stand` (hips anchor at scale 1). Head, flat face and red cap visible. Deadpan. s144.
- `amoeba_costume_flat`: the same costume deflated flat on a slide (death beat), cap NOT included (placed separately). ~420x160,
  centre anchor. s145 (inside a microscope eyepiece circle), s146 (in a dish).
- `snowmobile`: dark snowmobile with a rider-less seat, black track, front skis, a small windscreen, side view facing right.
  ~420x200, bottom-centre. s032, s033 (one flipped).
- `sleeping_bag`: rolled-out mummy sleeping bag, dark green with an orange lining edge, zip line. ~420x150, centre anchor. s044, s048, s049.
- `sticker_roll`: a small roll of blank travel stickers on a spool (white backing, a few red-edged stickers peeking). ~160x120,
  centre anchor. s050 (the narrator's hand puts it back in a drawer).
- `ice_pick`: a classic mountaineering ice axe/pick, grey steel head, wooden shaft. ~300x200, centre anchor. s067, s068.
- `pneumatic_drill`: a crude jackhammer (pneumatic drill), grey body with a hose, two handles, chisel bit pointing down. ~260x360,
  centre anchor. s067, s068 (a red X goes over it).
- `longbow_broken`: Ötzi's unfinished yew longbow in two pieces (long pale-brown stave snapped near one end). Object only.
  ~600x120, centre anchor. s069.
- `trophy_cup`: plain gold trophy cup on a dark base, blank plaque. ~240x320, bottom-centre. s132, s133 (one small and tipped, one big).

Not requested (built from primitives in the shotlist): the cave cross-section, the rope/pulley rig, the Utah seal slab, the car
cutaway under the drift, the Hoyo Negro chamber, the sinkhole, the sediment core, the battery and the day clock.

## Note for the graphic designer (thumbnail = s001)
Script line 16 is outdated (CD, 2026-11-08 and brief section 8): if Hero A is used, the awake worm goes in a **permafrost**
cutaway; a seafloor cutaway gets microbe dots, not a worm. s001 carries the words "Utah sealed a cave," so a Hero B cave image
also works as the opener.
