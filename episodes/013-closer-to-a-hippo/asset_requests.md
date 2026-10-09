# Asset requests: 013 Why Hippos Get Deadlier the Closer Doug Gets

From the director, for the illustrator (the art director approves). House style: `assets/library/anglerfish.json` and
`channel/art_bible.md`.
- **Detailed tier** for every creature and prop: outlines 4-6, flat fills plus `spray` shading, darker back, lighter belly. Everything
  faces **right** unless noted. Local coordinates are centred on the anchor.
- **Anchors and sizes.** I laid out all 253 shots with placeholder boxes at exactly the bboxes below and checked the contact sheets
  for the counter/meter zone, caption bar, crops and overlaps. `bc` = anchor at bottom-centre (the lowest point sits on y=0, drawing spans
  y -h..0). `c` = anchor at the centre. Sizes are local units at scale 1 (width x height). Please stay inside the bbox. Where I give a
  local point (eye, canine tip, gape), arrows or dotted lines in the shotlist aim at it, so please put that feature there.
- **One hippo, many poses.** All hippo drawings are the **same animal** (same palette, same head shape, same eye/ear/nostril layout),
  so they cut together. Scale: **180 units = 1 m** (a 4 m adult is 720 long, 1.5 m at the shoulder = 270).
- **Hippo palette:** body grey-brown with a purple cast `#8a7f8f`, darker back `#6f6474`, paler flank/belly `#a89ca8`, pink-flesh
  `#c99a9a` only around the eyes, ears, mouth corners and belly crease. Eyes small, high and mean (white with a small black pupil and a
  heavy brow line). Mouth interior a flat cartoon pink `#c96a7a` with a darker throat `#8e2e3e`; **no tongue detail, no saliva, no gums**.
  Teeth ivory `#f2ecd8` with a pale yellow `#e0d4a0` root shade.
- **Tone (brief section 7, HIGH kid-appeal risk).** The hippo must look **dangerous, not cuddly**: heavy barrel body, short thick legs,
  small eyes, no smile, no blush, no round "cartoon hippo" proportions, no eyelashes, no pastel nursery colours. **No blood, no wounds, no
  teeth touching Doug anywhere.** The red sweat is **orange-red** (`#e8662a`, highlights `#f0902a`, never `#7a0d0d` or a blood red).
- **Priority:** A = hero (8+ shots), B = supporting (3-7), C = one-off.

**Reused from the library (no work needed):** `world_map`, `loudspeaker` (the playback speaker, also Doug's speaker), `acacia_tree`,
`savanna_bush`, `canoe`, `small_car`, `sofa`, `suitcase`, `bathroom_scale`, `kitchen_timer` (egg timer), `ruler`, `front_door`,
`speedometer`, `calendar`, `torch`, `sunscreen`, `microbe`, `blue_whale`, `dolphin`, `scientist`, `dust_cloud`, `water_splash`, `doug_cap`,
`doug_sunglasses`, `field_guide`, `field_guide_open`, `heart_icon`, `gravestone`, and the annotation set (`question_mark`,
`exclamation_mark`, `warning_triangle`, `red_x`, `thermometer`).

**Drawn inline in the shotlist (no asset needed):** the DOUG DEATHS counter and the DISTANCE TO HIPPO meter (label under the counter at
(1590, 238), size 28; the art director may add a ruler icon), all backgrounds (Colombian pasture and brown river, dusk savanna and hill,
night path, riverbank mud, murky river, underwater cross-sections, Moon surface, flat pink-red), the Escobar paddock fence (posts and
rails, broken in s010), the census drone, footprints, the street and road markings, the bar chart, sound arcs, football pitches, the
playback panels, the skin cross-sections and fluid drops, test tubes and bench, sun rays, the bank card, the jaw-angle and door diagrams,
film frames and the tripod camera, the stride bar, the river-territory lines, the blank sign, tally marks, ripples, the paddle, the
"500?" papers and the four empty boxes.

---

## Creatures

### `hippo` (A): adult common hippo standing, side view
s008-s010, s039-s041, s051, s053-s054, s061 (as a silhouette), s063-s064, s072, s074-s076, s079-s080, s082-s085, s090, s133-s134,
s141-s142, s149-s150, s196-s197, s207, s211-s215, s217-s218, s230-s231, s236, s238
- `bc`, **720 x 330** (x -360..+360, y -330..0), facing right. Head at the right end (x +200..+360), mouth **closed**, the tip of one
  lower canine just showing at the lip corner. Eye at about (+270, -260), small ear at (+215, -300), nostrils on top of the snout tip at
  (+345, -235).
- Real look: huge barrel body, back almost level, very short thick legs (four visible, feet on y=0), broad square muzzle, thick neck
  folds, small stubby tail with a flat tuft at the left end (x -360, y -200). Faint skin creases and a couple of pale old scratch lines
  on the flank (no wounds).
- Used flipped (`flip: true`) and at scales 0.33-1.15, as small as 240 px wide, so the silhouette has to read at that size.
- Bull Territory (s195-s218): two of these stand **chest-deep**; water is drawn over the lower ~40% of the body, so make sure the head
  and back read on their own.

### `hippo_yawn` (A): the threat yawn, side view
s028-s029, s118-s125, s127-s128, s133-s140, s195, s203-s206, s216, s224
- `bc`, **760 x 560** (x -380..+380, y -560..0), facing right. Same body as `hippo`, front end raised slightly, jaws open to about
  **150 degrees**: upper jaw tipped up and back, lower jaw dropped forward.
- Local points I aim at: **upper jaw tip (+330, -510)**, **lower jaw tip (+330, -165)**, gape centre (+260, -330), **molars at the back
  of the mouth (+140, -290)** (a few flat grinding teeth), **lower canine tips (+330, -225)**: two long curved ivory tusks pointing up and
  slightly forward, much longer than the small upper canines and incisors.
- Real look: mouth interior flat pink, teeth clearly visible, small mean eyes squeezed by the raised muzzle, ears flat back.
- Used flipped (two yawning bulls facing each other, s124, s133, s203-s206, s216) and rotated ±12 degrees for rearing (s206).

### `hippo_waterline` (A): only ears, eyes and nostrils above the water
s011-s012, s014-s017, s020, s022, s024, s026-s027, s030, s032-s038, s042-s043, s050-s051, s069, s111, s115, s117, s143, s157, s171,
s173, s178-s180, s183, s185, s189-s190, s192, s198-s202, s233-s234, s237, s251-s252
- `c` with **y=0 = the water surface**, **300 x 90** (x -150..+150, y -70..+20), facing right. The flat top of the head breaks the
  surface: **ears at (-75, -70)**, **eyes at (+15, -55)** (two bumps, the near eye open, small pupil), **nostrils at (+120, -35)** on the
  snout bump. A thin pale ripple ring (`#d8e2c0`) around the waterline, plus a darker shape just under the surface.
- My arrows in s157 and s171 point at exactly those three points (the asset is shown at scale 2.2-2.4 there), so it must hold up big.
- Also the map icon on `africa_map` (scale 0.12) and the "rock with ears" reveal in s189: drawn **on top of `hippo_rock` at the same
  anchor and scale**, so its footprint must fully cover the rock's (stay at least as wide and as tall above y=0).
- Used flipped in s202.

### `hippo_rock` (B): the "smooth grey rock" (a hippo's back at the surface)
s168, s170, s174, s181-s182, s184, s186, s188-s189, s194
- `c` with y=0 = the water surface, **320 x 80** (x -160..+160, y -60..+20). A smooth, rounded grey dome just breaking the water, the same
  skin colour as the hippo's back, a highlight on top, a ripple ring. **No eyes, ears or nostrils**: from the canoe it must look exactly
  like a river rock. Must fit inside the `hippo_waterline` footprint (see above).

### `hippo_grazing` (B): head down, grazing on land
s052, s055-s056, s058, s070-s071, s093, s224
- `bc`, **720 x 300** (x -360..+360, y -300..0), facing right. Same body as `hippo`, neck and head lowered so the **mouth is at grass
  level at (+330, -15)**, lips around a tuft of grass. Eyes still visible, ears up.

### `hippo_red_sweat` (B): the "bleeding" hippo
s094-s097, s100, s112-s114
- Same geometry and anchor as `hippo` (`bc`, 720 x 330). Add a glossy **orange-red** coating on the back, neck and face: patches of
  `#e8662a` with lighter `#f0902a` gloss highlights and a few white shine dots, plus 3-4 small orange drips on the flank. It must read
  as "shiny and wet", **never as wounds or blood** (the narration says "NOT BLOOD").

### `hippo_trot` (B): full-speed trot, all four feet off the ground
s077-s079, s081, s086 (silhouette), s087-s089, s091, s209-s210
- `bc`, **760 x 380** (x -380..+380, y -380..0), facing right. Body level and stretched, legs in a trot (diagonal pairs), **every foot
  off the ground: the lowest hoof at y -45**, a clear gap of daylight under all four feet around (0, -30), and a flat grey shadow ellipse
  on y=0 under the body. Ears back, mouth closed. My red arrow in s087 points into that gap.

### `hippo_underwater` (B): bounding along the riverbed
s151-s156, s160-s161, s164 (silhouette), s165, s187, s191
- `c`, **720 x 360** (x -360..+360, y -180..+180), facing right. Whole body in a slow bound (the Moon-walk gait): front legs reaching
  forward, hind legs pushing back, no foot touching anything. **Ears folded shut, nostrils closed** (slit lines), eyes open. A few small
  bubbles above. Use a **mid-tone** body (`#8a7f8f`, darker back `#6f6474`) so it reads on the murky water `#5d6b45` and on the
  black Moon panel in s155-s156.

### `hippo_sleeping` (B): asleep underwater
s147-s148, s175-s177
- `c`, **700 x 320** (x -350..+350, y -160..+160), facing right. Same mid-tone body, legs hanging relaxed, **eyes shut** (two curved
  lines), ears folded, nostrils shut. Used three times in one diagram (sinking, rising to breathe, sinking again), so a calm, neutral pose.

### `hippo_submerged` (C): a hippo lying just under the surface
s172
- Anchor (0,0) on the **water surface**, **720 x 370** (x -360..+360, y -70..+300), facing right. The whole body sits under the surface
  line (drawn mid-tone, as seen through murky water), and only the eyes, ears and nostrils poke above y=0 at the right end (same layout
  as `hippo_waterline`, at x +230..+350). Shows "only those showing, breathing, watching and listening".

### `hippo_mouth_front` (A, boss): the open mouth like a doorway, front view
s219-s221, s225, s239-s243, s245-s250 (s219 and s245-s248 as a silhouette)
- `bc`, **1100 x 980** (x -550..+550, y -980..0), facing the viewer. The mouth is open as wide as it goes: the **upper jaw and head at
  the top** (y -980..-640: broad muzzle with two big nostrils, two small mean eyes and small ears on top), the **lower jaw at the bottom**
  (y -140..0, a wide flat chin resting on the riverbank). Between them a tall **flat dark pink-red opening** (`#8e2e3e`, deeper
  `#6e1e2e` at the back), about x -380..+380, y -620..-140, like a doorway. Two big lower canines rise from the lower jaw at x ±330 to
  about y -420; two short upper canines hang at x ±300. A row of flat molars hinted deep inside at the back. **No tongue detail, no
  saliva, no anatomy beyond teeth and a flat interior.**
- Doug (scale 0.32, about 145 px tall) stands right in front of the lower lip at x 0 holding a lettuce, so keep the lower-jaw centre
  simple and light enough that his black lines read (or tell me and I'll set his ink).
- Used at scale 0.5-0.75. As a silhouette (s219, s245-s248) it has to read as a gaping mouth from the outline alone.

### `hippo_canine` (C): one lower canine, diagram
s129-s132
- `c`, **767 x 200** (x -383..+383, y -100..+100), lying horizontal, **tip pointing right**. It is drawn at the **ruler's scale**
  (`ruler` = 14.33 units per cm, so 767 = 50 cm): in s130 it sits above one and a half rulers. A long curved ivory tusk, bending gently
  upward toward a sharp, bevelled tip (the honed wear facet as a flat paler face at the tip), the root end at the left yellower and blunt.
  Also used at 0.5 (the female's) and rotated -30 / +150 for the "lower grinds against upper" diagram.

---

## Props and places

### `lettuce` (B): the peace offering
s220-s222, s225, s239-s243, s247, s249-s250
- `c` = Doug's hand grip, **220 x 190**. A big round iceberg or butterhead lettuce: light green `#9be07a` outer leaves with darker `#5aa83a`
  veins and ruffled edges, a paler core. Shown at 0.32 in Doug's hand by the mouth, at 1.0 in close-ups. (It sits on dark pink-red and
  dusk backgrounds, never on grass.)

### `tent` (B): Doug's small camping tent
s059-s065
- `bc`, **380 x 240** (x -190..+190, y -240..0). A small two-person dome tent, green `#3f7a4a` fly with an orange `#e07a2a` trim, the
  front door zipped shut (zip line down the middle), two guy lines and pegs. Reads on the night background (`#2b3d33` ground, blue sky):
  keep the fills mid-tone, not dark. In s062 and s065 a yellow torch glow is sprayed over it from inside.

### `sticking_plaster` (B): adhesive bandage
s112-s117
- `c` = Doug's hand grip, **220 x 80**. A tan `#e8b98a` strip with rounded ends, a paler `#f6e0c8` pad in the middle and tiny vent dots.
  Held at 0.5 just beyond Doug's pointing hand.

### `dung_cloud` (C): the honk reply
s044
- `c`, **760 x 480** (x -380..+380, y -240..+240). A flat brown scribble cloud (`#7a5a2a`, darker scribbles `#5a3e1a`) sweeping over the
  hill from the right: loose zigzag scribble texture and a few motion lines, nothing lumpy or detailed. Gross but abstract; one shot only
  (brief: "keep it to one shot", kid-appeal risk).

### `africa_map` (B): Africa with its hippo rivers
s185, s232-s234, s237
- `c`, **900 x 888**, in the `world_map` style (flat green `#6cbf5a` land, dark green outline, light-blue sea, white wave ticks, black
  frame, no labels). Projection so I can place icons: **lon -20..55 E, lat -36..38, 12 units per degree, centred at lon 17.5 / lat 1**:
  `x = (lon - 17.5) * 12`, `y = -(lat - 1) * 12`. Include Madagascar and the Arabian Peninsula's edge.
- Main rivers as blue lines (`#3a9ad9`, width 4-5): Nile (with the White and Blue Nile), Niger, Congo, **Zambezi**, **Kafue** (Zambezi
  tributary, about lon 26-28, lat -15.5), the **Okavango Delta** (a small fan at lon 22.5-23.5, lat -19), Limpopo, Orange. Lake Victoria
  and Lake Tanganyika as blue shapes.
- I put `hippo_waterline` icons (scale 0.12) at (24,-19), (32,-25), (27,-14), (35,-13), (30,-8), (31,15), (5,10) and a red ring
  around the Kafue (26,-15) and southern Africa (27,-24).

### `astronaut` (C): crude-tier astronaut on the Moon
s156
- Doug's tier (5 px lines, big round head), **no red cap**, `"auto_ink": true` like `diver`/`scientist`: white spacesuit with a backpack,
  round white helmet with a gold `#e0b030` visor, mid-bound pose (knees bent, one foot up). Anchor at the hips like Doug, about **180 x 480**
  (x -90..+90, y -330..+150). Shown at 0.6 on the black Moon panel, facing right.
