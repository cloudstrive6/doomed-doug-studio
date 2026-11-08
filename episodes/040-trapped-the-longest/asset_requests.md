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

## Status (illustrator, 2026-11-08): all done
- Stickers (7): done, previews `assets/previews/040-props-1.png` (3x), `040-props-3.png` (0.8x). `sticker_south_pacific_gyre` is 130 wide.
- `sticker_roll`, `ice_pick`, `pneumatic_drill`, `longbow_broken`, `trophy_cup` (bottom anchor), `snowmobile` (bottom anchor), `sleeping_bag`: done, `assets/previews/040-props-2.png`.
- `permafrost_nematode`, `permafrost_nematode_active`, `pandoravirus`, `acanthamoeba`, `mammoth_pelvis`: done, `assets/previews/040-micro-final.png` (0.3x check `040-micro-1s.png`).
- `mammoth_dig_layout`: done (1500x800), `assets/previews/040-micro-3.png`.
- `giant_ground_sloth`, `gomphothere`, `columbian_mammoth`, `woolly_mammoth`, `short_faced_bear`: done, `assets/previews/040-mega-full.png`, silhouettes with red rim `040-mega-sil.png`, dark bg `040-mega-dark.png`.
  Note: wider than requested because of the tusks: gomphothere and columbian_mammoth ~720, woolly_mammoth ~600 local units. Scale down about 0.75-0.8 to fit the requested footprint.
- `neanderthal`, `mammoth_costume` (suitcase loop at local (150,138)), `amoeba_costume`, `amoeba_costume_flat`: done, `assets/previews/040-costume-test.png` (over stand/walk1/walk2, neanderthal on dark), `040-costume-assets.png`.

## Fixes after art review (illustrator, 2026-11-08): done, preview `assets/previews/040-fixes.png`
1. `mammoth_pelvis`: redrawn as a wide, flat hip girdle (broad iliac wings); obturator openings are tall slanted mid-tan teardrops set low, acetabula are side-facing cups on the outer edges, and the sacrum and dark holes are gone. Shown at 1.2x, 0.3x and 0.3x magnified.
2. `short_faced_bear`: the ears are now two rounded bumps on the head's top silhouette, and the head/body outlines are clipped so nothing crosses the shoulder.
3. `columbian_mammoth`: the body, head and trunk outlines are clipped to the outer silhouette, so there are no double lines across the face or neck. Also checked flipped on a dark background.
4. `woolly_mammoth`: same outline clipping; the ear is now a soft dark patch with no black ring.
5. `sticker_south_pacific_gyre`: still 130 wide. "SOUTH PACIFIC" is at size 15 across the full width, "GYRE" is at size 21 and the swirl is a small icon beside GYRE. 0.3x (and 5x magnified) next to `sticker_kolyma` 0.3x.
- Optional: `gomphothere` now has one clean, slightly upturned tusk pair (no crack lines, no seam).
