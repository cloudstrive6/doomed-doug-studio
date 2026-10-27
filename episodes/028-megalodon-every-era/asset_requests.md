# 028-megalodon-every-era: asset requests (director)

House style: detailed tier for creatures, places and props (thick dark outlines, flat fills with interior shading); crude tier
(`auto_ink`, `keep_ink` faces) for the two humans. Facing right unless noted. Sizes are local units at scale 1 and match the
layout the shotlist was built against, so please keep the anchors and extents. Shots list where the shotlist uses each name.
Reused from the library (no request): `megalodon`, `megalodon_tooth`, `livyatan`, `livyatan_tooth`, `orca`, `orca_female`,
`orca_fin`, `great_white_shark`, `greenland_shark` (as the Pacific sleeper shark), `shark`, `sperm_whale`, `gray_whale`,
`humpback_whale`, `blue_whale`, `time_machine`, `chalkboard`, `placard` (the scorecard), `supernova`, `thermometer`,
`hot_tub`, `ice_block`, `manganese_nodule`, `burj_khalifa`, `school_bus`, `bed`, `north_america_ice_map`, `bc_map`,
`africa_map`, `britain_map`, `baby_mammoth`, `doug_sunglasses`, `doug_cap`, `water_splash`, annotation marks.

## `shark_cage` (highest priority: 225 shots)
Doug's shark-diving cage. Steel bars only, **no fill between the bars** (Doug is drawn first and must show through; the bars sit on
top of him). Anchor bottom-centre (floor at y=0). Extent x -160..160, y -470..0. Flat roof at y -440 with a small lifting eye /
shackle at (0,-470) where a cable attaches from above. Vertical round bars about every 40 units, three horizontal bands (top,
middle, bottom), a solid floor plate y -12..0, a small roof hatch outline. Bars mid-grey `#9aa3ab` with a dark `#3a3a3a`
outline and a pale highlight edge so the cage reads on bright cyan `#5cc6c9`, sky blue, olive `#5d6b45` and near-black
`#050a1f` water alike. Not a mine lift, no people inside (start from `mine_cage` geometry only if useful). The roof must hold
`doug_cap` at about (0,-460), and Doug sits on the roof in s132-s134 (roof is a seat at y -440).
Used at scale 0.5-0.95, empty in death beats, on dry ground (Ice Age, Canal) and dragged by a rope.
- Shots: s002-s303 (225 shots)
- **Done** (illustrator, part A): preview `assets/previews/028-megalodon-every-era-assets-a1.png` (in context: assets/previews/028-megalodon-every-era-assets-a-context.png)

## `megalodon_pup`
Newborn *Otodus megalodon*: same slim 2025-style design and palette as `megalodon` (slate back, jagged countershading, pale
belly), but a newborn's proportions: slightly larger head and eye relative to the body, softer fins, **mouth closed**, no teeth
showing. Flat hard eye, menacing not cute (no big sparkly eyes, no smile). Centre anchor, x -450..450, y -130..130.
Also used as a black silhouette with a thin white rim, so keep the outline clearly sharky.
- Shots: s002, s013, s014, s015, s016, s019, s020, s022, s023, s024, s025, s026, s027, s029, s234
- **Done** (illustrator, part A): preview `assets/previews/028-megalodon-every-era-assets-a1.png`

## `mosasaurus`
*Mosasaurus hoffmannii*, the Maastricht giant marine lizard. Must read differently from `tylosaurus`: **no long bony rostrum**,
a massive deep blunt skull, robust jaws slightly open with conical teeth (dark red mouth, no blood), long body, four paddle
flippers, a tail ending in a downturned crescent fluke. Dark grey-green back `#3f5a5a` with lighter scale texture, pale belly.
Mid-tone so it reads on chalky `#6aaabf` water. Centre anchor, x -520..520, y -130..150. Used as a red-rim silhouette reveal
(s030, s034, s035) and rotated up to -60 degrees (surfacing for air), so keep it readable when tilted.
- Shots: s030, s031, s034, s035, s036, s041, s047, s048, s049, s051, s052, s053, s054, s056, s057, s058, s309
- **Done** (illustrator, part A): preview `assets/previews/028-megalodon-every-era-assets-a1.png` (tilt and red-rim checks: assets/previews/028-megalodon-every-era-assets-a-context.png)

## `mosasaurus_skull`
The famous Maastricht skull (the one taken to Paris in 1795): side view of a long toothy reptile skull with lower jaw, cream
`#e8dcc0` bone with brown `#8a6a3a` old-engraving hatch lines, partly set in a pale limestone block at the bottom edge. A museum
fossil, not a fresh skull. Centre anchor, x -260..260, y -110..110.
- Shots: s039, s040, s043, s044, s045
- **Done** (illustrator, part A): preview `assets/previews/028-megalodon-every-era-assets-a1.png`

## `ichthyotitan`
*Ichthyotitan severnensis*, a whale-sized late Triassic ichthyosaur (more than 25 m). A massive streamlined ichthyosaur: long
narrow toothy jaws, a relatively small eye for its size, a dorsal fin, a vertical crescent tail, four flippers. Bulkier than
`ichthyosaur` (Stenopterygius), not just a scaled copy. Slate blue-grey back, pale belly, mid-tone so it reads on `#2a6aa6`
and `#3f8fc4`. Centre anchor, x -560..560, y -140..140. Used up to scale 1.6 as a "ceiling" passing over the cage, and as a
silhouette with a red rim (s062). Keep the reconstruction generic: only the jaw is known.
- Shots: s062, s068, s070, s071, s074, s075, s077, s079, s080, s082
- **Done** (illustrator, part A): preview `assets/previews/028-megalodon-every-era-assets-a1.png`

## `ichthyotitan_jaw`
The reassembled *Ichthyotitan* lower-jaw bone (surangular): a long, narrow, gently curved bone, pale grey-brown fossil with a
darker edge, several visible crack lines where the pieces were glued back together. No teeth. Centre anchor, x -420..420,
y -80..80.
- Shots: s066, s072, s073, s074, s078
- **Done** (illustrator, part A): preview `assets/previews/028-megalodon-every-era-assets-a1.png`

## `fossil_hunter_girl`
Crude tier (Doug's line weight, big round head with the grey crescent, oval eyes, meme face), `auto_ink`. An 11-year-old fossil
hunter on a beach: no cap, a ponytail, plain jacket, holding a small piece of bone in the front hand. Plain and matter-of-fact,
not a kids-show character. Anchor bottom-centre (feet y=0), about x -60..60, y -260..0, facing right. Also used as a black
silhouette (scale bar on the jaw card), so the outline should read as a child.
- Shots: s063, s064, s065, s066, s069, s078
- **Done** (illustrator, part A): preview `assets/previews/028-megalodon-every-era-assets-a-context.png`

## `fossil_hunter_dad`
Crude tier, `auto_ink`: an adult man (the father), short hair, no cap, outdoor jacket, small geological hammer in the front hand.
Anchor hips (0,0), feet +150, head top about -325 (same rig as `scientist`), facing right.
- Shots: s063, s064, s065, s069
- **Done** (illustrator, part A): preview `assets/previews/028-megalodon-every-era-assets-a-context.png`

## `sun_hat`
Worn prop perched on Doug's cap (the `hard_hat` convention): wide floppy straw sun hat `#e8c07a` with a red band. Anchor = Doug's
hips, rim at y -294, x -130..130, y -340..-290, so the cap dome and brim stay visible below. Worn with `doug_sunglasses` at the
same x/y/scale, standing poses only.
- Shots: s097, s098, s099, s100, s104, s106, s107, s108, s109, s110
- **Done** (illustrator, part A): preview `assets/previews/028-megalodon-every-era-assets-a-context.png` (on Doug, with doug_sunglasses)

## `livyatan_skull`
The 3 m *Livyatan* fossil skull lying in desert sand: long massive skull in side view, huge conical teeth in both upper and lower
jaws (cream), pale tan-grey bone with brown cracks, sand piled at the base. Not gory. Anchor bottom-centre (sand line y=0),
x -420..420, y -150..0.
- Shots: s115, s116
- **Done** (illustrator, part A): preview `assets/previews/028-megalodon-every-era-assets-a2.png`

## `orca_tooth` / `orca_tooth_worn`
Cartoon dental comparison, not medical. `orca_tooth`: one healthy orca tooth, vertical, conical and slightly curved, cream-white
enamel, pointed tip, darker root. Centre anchor, x -60..60, y -180..180. `orca_tooth_worn`: the same tooth worn flat almost to the
gum line, flat top with a few scratch lines, a pink gum band at the base. Centre anchor, x -60..60, y -120..120.
- Shots: `orca_tooth` s146, s147 · `orca_tooth_worn` s147, s150
- **Done** (illustrator, part A): preview `assets/previews/028-megalodon-every-era-assets-a2.png`

## `toothbrush`
Plain toothbrush, horizontal: blue handle, white bristles at the right end. Centre anchor, x -200..200, y -25..25.
- Shots: s161, s162
- **Done** (illustrator, part B): preview `assets/previews/028-megalodon-every-era-assets-b-props.png`

## `rubber_duck`
Classic yellow rubber duck with an orange beak, facing right. Anchor bottom-centre, sitting on the waterline (y=0), x -80..80,
y -120..10.
- Shots: s178, s189, s190
- **Done** (illustrator, part B): preview `assets/previews/028-megalodon-every-era-assets-b-props.png`

## `statue_of_liberty`
Simple MS Paint Statue of Liberty: green copper `#6fa59a` statue with a darker shaded side, raised torch arm with a yellow flame,
on its grey stone pedestal. Anchor bottom-centre, x -90..90, y -620..0 (ground to torch tip; the 93 m figure in the script is
ground to torch).
- Shots: s198
- **Done** (illustrator, part B): preview `assets/previews/028-megalodon-every-era-assets-b-statue.png` (bottom-anchored, so the grid preview crops it; this is a scene render). Pedestal about half the height, torch tip at y -620

## `beringia_map`
Siberia and Alaska at the Last Glacial Maximum, in the `world_map` style (flat green land, dark outlines, light-blue sea, black
frame, no labels). The exposed Bering land bridge is a pale tan `#e8d6a8` band joining the two, with today's coastline drawn as a
dashed line across it. Centre anchor, x -700..700, y -420..420. The bridge should sit near the centre (a mammoth is placed at
local (0,+50)).
- Shots: s200, s201
- **Done** (illustrator, part B): preview `assets/previews/028-megalodon-every-era-assets-b-maps.png` (in a scene: `assets/previews/028-megalodon-every-era-assets-b-maps-context.png`). Bering Strait gap at about local (30,-38); (0,+50) is tan bridge ground beside the small St Lawrence Island outline

## `panama_seaway_map` / `panama_isthmus_map`
A matching pair, same frame and projection, `world_map` style, no labels, centre anchor x -700..700, y -420..420.
`panama_seaway_map`: about 10 million years ago, the southern end of Central America and northern South America with an open
blue seaway gap where Panama is today, centred on (0,0) (a red ring is drawn there). Pacific bottom/left, Caribbean top/right.
`panama_isthmus_map`: today, the same coast with the thin S-shaped isthmus closing the gap, and the Panama Canal as a thin blue
line across the isthmus from about local (-145,+65) to (+145,-80).
- Shots: `panama_seaway_map` s009, s221, s226 · `panama_isthmus_map` s222, s227, s228, s235
- **Done** (illustrator, part B): preview `assets/previews/028-megalodon-every-era-assets-b-maps.png` (at 0.62 in a scene: `assets/previews/028-megalodon-every-era-assets-b-maps-context.png`). The seaway gap runs from x -190 to x +250 at y 0. The canal is drawn on land only and stays on your s235 dashed line, from (-145,65) to the Caribbean coast at about (132,-73)

## `container_ship`
Modern container ship, side view facing right: dark hull with a red bottom stripe, stacks of multicolour containers, white
bridge tower at the stern. Anchor = waterline centre, x -520..520, y -260..60.
- Shots: s233, s234, s237
- **Done** (illustrator, part B): preview `assets/previews/028-megalodon-every-era-assets-b-props.png` (on water: `assets/previews/028-megalodon-every-era-assets-b-context.png`)

## `hms_challenger`
HMS *Challenger* (1870s steam-assisted sailing corvette): black wooden hull with a white band and a row of gun ports, three masts
with furled sails and rigging, one funnel between the masts, facing right. A period ship, not the modern `research_ship`. Anchor
= waterline centre, x -420..420, y -480..60.
- Shots: s095, s247, s248
- **Done** (illustrator, part B): preview `assets/previews/028-megalodon-every-era-assets-b-props.png` (on water: `assets/previews/028-megalodon-every-era-assets-b-context.png`)

## `manganese_tooth_nodule`
A manganese nodule cut in half: dark brown-black concentric growth rings around a pale grey triangular shark tooth at the centre,
lumpy outer edge like `manganese_nodule`, pale rim so it reads on dark water. Centre anchor, x -160..160, y -120..120.
- Shots: s249, s251
- **Done** (illustrator, part B): preview `assets/previews/028-megalodon-every-era-assets-b-props.png`

## `megalodon_vertebra`
A fossil megalodon vertebra seen end-on: a round disc (centrum), grey-brown, with clear concentric growth rings (alternating dark
and light bands). Centre anchor, x -180..180, y -180..180.
- Shots: s018
- **Done** (illustrator, part B): preview `assets/previews/028-megalodon-every-era-assets-b-props.png`

## `stone_tool`
An early stone tool (Lomekwi-style): a grey-brown chipped stone core with visible flake scars and a sharp edge. Centre anchor,
x -90..90, y -110..110.
- Shots: s287, s288
- **Done** (illustrator, part B): preview `assets/previews/028-megalodon-every-era-assets-b-props.png`

## `sea_turtle`
A generic sea turtle swimming, facing right: green-brown shell with scutes, paler underside, four flippers, small head. Centre
anchor, x -220..220, y -130..130.
- Shots: s290, s291, s294
- **Done** (illustrator, part B): preview `assets/previews/028-megalodon-every-era-assets-b-props.png` (on water: `assets/previews/028-megalodon-every-era-assets-b-context.png`)

## Keyframe review round 1 fixes (visual_review items 3, 6, 9)
- `mosasaurus` silhouette: redrawn (6c83369) so the silhouette follows the tapered snout and zig-zag jaw, with no blunt
  head; it no longer matches the boxy Livyatan silhouette. Checked in s030/s034/s035/s036/s113 keyframes.
  **Done** (illustrator): preview `assets/previews/028-mosasaurus-silhouette-check.png` (normal / silhouette / on water / livyatan)
- `burj_khalifa`: redrawn (6c83369), stepped setbacks + podium + spire, reads at scale 0.25 in s252. The label and keeping
  the top copy below the HUD are director items. **Done**: preview `assets/previews/028-megalodon-every-era-assets-r2b.png`
- `city_bus` (NEW, swap for `school_bus` in s049, s071, s156): white/red transit bus, flat front, LED route sign "42 CITY",
  anchor bottom-centre (tyres at y 0), x -310..326, y -284..0 (school_bus: x -310..310, y -270..0).
  **Done** (illustrator): preview `assets/previews/028-megalodon-every-era-assets-r2.png`
