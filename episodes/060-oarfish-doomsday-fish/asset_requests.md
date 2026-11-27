# 060-oarfish-doomsday-fish: asset requests (director, 2026-11-27)

The shotlist already places these by name, so please keep the **anchor, bounding box and key points** given here. The
generator (`episodes/060-oarfish-doomsday-fish/build/gen_shotlist.py`, git-ignored scratch) puts Doug's hands, the
torch, the cap and the labels relative to them. Everything **faces right** unless noted (the shotlist flips). House style:
detailed tier, thick black outlines (5-6), flat fills with interior shading.

**CD conditions for this episode (decisions.md, 2026-11-27):**
- Every oarfish is **blank-eyed**: a plain round eye (white with a black dot, like the library `giant_oarfish`), no brows,
  no highlight sparkle, and **never a smile**. Keep any mouth line straight or slightly down, never curved up. It must not look cute.
- **No red on any cut or scar.** The stump and the cut end of the tail piece are clean, rounded and healed: the same silver as the
  body, a slightly paler `#e6ebf0` cap and one thin grey `#8a96a2` seam line. No pink, no maroon, no speckle, no flat cross-section,
  no bones showing.
- The parasites are **plain pale ribbons**: no segments, no hooks or suckers, no gore.
- No earthquake or disaster imagery anywhere (no cracked ground, no falling buildings, no waves hitting towns).

**Art-director approval needed before keyframes:** `oarfish_stump`, `oarfish_stump_short`, `oarfish_tail_piece` (the
autotomy drawings), `tapeworm_larva`, and `undersea_palace` (a cultural subject: draw it respectfully, as a fairy-tale palace,
with no text and no religious symbols).

**Episode HUD (no new drawing).** Under the counter, a size-28 `label` reads `DISTANCE TO FISH: <value>` at (1590,238), with the
library `tape_measure` at 0.16 as its icon (icon right edge ~30 px left of the label box). The values are 9,000 KM, 1 KM, 100 M, 10 M,
1 M, 0 M, then `0 M (HOLDING)`, blank on the s136 death, and `-1 M` in red-on-pink from s137 on. The art director should approve the device itself.

**Oarfish colour reference:** match the library `giant_oarfish` (silver `#c9d3dc`, bluish shading, red `#e0302a` dorsal fin and
crest, dark streaks and grey speckles) so all the new oarfish drawings read as the same animal.

---

## Oarfish (new views of the existing `giant_oarfish`)

### `oarfish_stump`: s003 s116 s117 s118 s120 s122 s129 s130 s134 s137 s174 s175 s176 s178
The healthy, living giant oarfish after autotomy, **vertical, head at the top** (same pose and anchor convention as
`giant_oarfish`). The body is about 60% of the full length and ends in a **neat rounded healed stump**: a smooth blunt dome
following the CD condition above. The red dorsal fin runs down the right edge and stops just short of the stump. The crest,
pelvic streamers and eye are the same as `giant_oarfish`. Calm, upright, perfectly fine.
- Anchor (0,0) = centre of the full-length fish, as in `giant_oarfish`, so the head is at the same place. Head top about y -500,
  crest top about y -540, stump bottom about y +110. x about -90..+80.
- Size in shots: scale 0.45-0.75 (about 300-490 px tall). It has to read at 0.45 on a living-room wall (s003) and at 0.5 inside
  a dark monitor feed (s174-s176, `#0b2447`), so keep the outline thick.
- The stump is pointed at with a red arrow and the label "SCAR" in s117, so the rounded end must be clearly visible.
- In s175 the red cap is placed on the fin at about local (+60,-300), so keep that part of the fin edge simple.

### `oarfish_stump_short`: s128
The same fish cut down to "only the head and abdomen": head, crest, pelvic streamers and about one head-length of body, ending in
the same clean rounded stump. Vertical, head up. Anchor centre; about x -90..+80, y -170..+170 (the head is at the top). Used at
0.9 on cream `#f4f1dc`, next to the label HEAD + ABDOMEN. Clean and calm, not pitiful, with no injury marks.

### `oarfish_tail_piece`: s003 s134 s135
The ~2 m rear section the fish let go of, **horizontal**. The **tail tip is on the right** (+400): thin and tapering, the end where
Doug holds it. The **front end is on the left** (-400): wider, rounded and sealed like the stump, with no flat cut and no red.
The red dorsal fin runs along the top edge, a few dark streaks run along it, and nothing hangs off it.
- Anchor centre; x -400..+400, y -50..+50 (the fin is included in that height). Used at 0.8 (s134-s135: Doug's silver hand sits
  on the right tip at local (+400,0)) and at 0.35 in the intro (s003).

### `oarfish_head_closeup`: s077 s078 s079 s080 s084 s088 s091 s092 s093 s094
A big side-view close-up of the head, **facing right** (the shotlist flips it so it faces Doug on the left). It has a long
silver head with a steep, blunt forehead profile. The eye is **big, round and blank** (white with a black dot, no brows, no
glint). The mouth is **small, closed and toothless**: a short straight line at the snout tip, with **no teeth drawn**, no smile
and no lips. There is a gill-cover curve, and the red crest rays sweep up and back from the top of the head. The two pelvic
streamers start under the head and trail down-left. The body runs **off to the left** as a plain silver ribbon with the red
dorsal fin on top.
- Anchor (0,0) = centre of the head. The snout tip / mouth is at about (+430, +40). The body extends to x -1000 (it runs
  off-frame after the flip). The crest stays inside x -250..+150 and y ≥ -380. The head body is about y -240..+220.
- The shotlist places it at (1050,640), flipped, at scale 1.0: the mouth lands at about x 620 and Doug is at x 400 "at arm's
  length". The crest must stay below y 260 there, out of the counter zone.
- In s080 a red arrow points at the mouth ("push the jaw forward"); a separate open variant is not needed for this.

### `oarfish_head_open`: s143 s144 s145
The same head with the **jaw pushed forward and open**: a round dark mouth opening `#3a2a30` about 180 px tall at the snout,
with faint pale comb lines (the gill rakers) just inside. **Still no teeth.** It must read as a tunnel entrance that a
thumb-sized Doug can walk into. Same anchor and footprint as `oarfish_head_closeup` (mouth opening centred near (+430,+40)).
It lies on a beach (sand at y 550+), so the lower jaw can rest flat. The fish is dead here, but the eye stays **blank and round,
not an X** (an X eye here would read like Doug's death grammar).

### `streamer_fish`: s108 s109 s110
The streamer fish (*Agrostichthys parkeri*), the oarfish's close relative: a **much slimmer, longer and darker** silver ribbon
(`#b8c2cc` with a blue-grey `#6a7a8a` back) with a thin pinkish-red dorsal fin along its whole length. It has a small head with no
tall crest, only 2-3 short rays, a round blank eye, and a thread-like tail tip. Horizontal, facing right. Anchor centre; x -400..+400,
y -60..+60. At scale 0.9 on cream it sits next to the oarfish. It must look clearly **different** from the oarfish (no big
crest, no oar-tipped streamers). A yellow zigzag is drawn above it in s109 ("mild shock"), so keep the top edge clean.

## Parasites and prey

### `tapeworm_larva`: s004 s152 s153 s154 s157 s158 s159 s160 s162 s163 s164 s165 s166 s168 s170 s171
A larval tapeworm, cartoon: a **plain, pale, unsegmented ribbon** (`#f3ecd6` fill, soft `#b8a88a` outline) in a gentle S-wave.
One end is a little rounder and carries **two small black dot eyes**: a deadpan look, no mouth, no expression. No segment lines,
no hooks, no suckers. A faint darker strip runs along one edge for volume. It must differ from the library adult `tapeworm`,
which is segmented.
- Anchor centre; x -200..+200, y -30..+30, with the dot-eye end on the right.
- It is used rotated (80-100 degrees) hanging from the gut walls and flat (-8..5 degrees) on the floor, at scale 0.2-0.6. It must
  read on flesh pink `#f4c6c4` / `#e79aa0`. It is also used as a dark silhouette with a thin cream rim far down the corridor
  (s152-s153) and with a red rim in the intro (s004), so the outline shape matters.

### `krill`: s068 s069 s082 s083 s085 s150 s151
One krill, side view facing right: a curved, translucent pink-orange `#f08a7a` shrimp body (the same colour as the library
`krill_cloud`) with a big black eye, feathery legs underneath and two long antennae. Anchor centre; x -120..+120, y -50..+50.
It is used at 1.4 on cream (s085, next to a ruler and the label 1-2 CM), at 0.25-0.35 caught on the comb and lying on the gut floor,
and as a **black silhouette** at 0.5 against a pale glow (s068-s069 "dark shape"), so the silhouette needs a clear shrimp outline.

### `shortfin_mako`: s167 s168 s169
The shortfin mako shark, **calm, diagram style** (it is only the tapeworm's future host, not an attacker). It has a sleek
metallic blue `#2f5f9f` back, a white belly, a long conical **pointed snout**, a big black eye and a crescent (lunate) tail. The
mouth is **closed**, a short line with no teeth showing. Horizontal, facing right. Anchor centre; x -330..+330, y -120..+120.
Used at 0.8 on cream with the label ADULT under it. It must read as a mako and not as the generic `shark`.

## People and props

### `undersea_palace`: s007 s008 s009
Ryūgū-jō, the sea god's palace from Japanese folklore, as a **gentle fairy-tale drawing on the sea floor**. It has a
vermilion-red `#d9452b` palace with layered, curved, dark-green-grey tiled roofs, white walls, a small arched gate and
coral and seaweed at its feet. It is detailed tier, with no text, no flags and no religious symbols. Anchor bottom-centre (base
on the sand at y=0); x -400..+400, y -500..0. Used at 0.9 on surface water `#3a9ad9` with sand at y 880. A silver oarfish rises
beside it (right), so keep the right edge clean.

### `rooster`: s014 s015
A farmyard rooster facing right: a tall red comb, wattles, glossy dark-green and black sickle tail feathers arching up, a
copper-orange neck hackle, yellow legs and a slightly smug half-lidded eye. Anchor bottom-centre (feet on y=0); x -150..+150,
y -300..0. Used at 1.1 on cream, next to a row of weather-forecast cards. It must not be confused with the library `chicken` (hen).

### `bean_tin`: s018 s019
A sealed tin of baked beans: a grey metal can with top and bottom rims and an orange label with a cartoon bean pile. **No
brand and no text.** Anchor centre; x -50..+50, y -70..+70. It sits on the floor at 0.55 beside the library `hiking_backpack` and `torch`.

### `spyglass`: s023 s024 s031 s033 s036 s038
An old brass telescope: three telescoping brass `#c9a03a` sections, darker brass rings, a dark eyepiece at the left end and a
wider objective lens at the right end with a pale glint. Anchor (0,0) = the **grip at the eyepiece end** (Doug's front hand);
the tube runs right to x +300; y -25..+25. Used at 0.45-0.5, held level in Doug's `point` hand and in the cook's hand.

### `ship_cook`: s036 s038
A crude-tier stick-figure ship's cook (Doug's tier: 5 px lines, big round white head with the grey crescent, no cap). He wears
a tall white chef's toque, a white apron over the stick body, and a wooden spoon in the back hand. His face is flat and
unimpressed (he "says nothing at all"). The **front hand is held out at about local (+110,-140)**, so the `spyglass` (placed
separately) can sit there. Anchor = hips (0,0) like `scientist`: feet at +150, head top about -320. Facing right. Set
`auto_ink` with `keep_ink` on the face. Used at 0.55-0.6 on a wooden deck and on cream.

### `stick_man_arms_up`: s056
A generic crude-tier stick man (as `stick_man_plain`: no cap, neutral face) with **both arms straight up, hands at about
(-60,-700) and (+60,-700)**, as if holding something overhead. Anchor = feet (0,0); x -100..+100, y -700..0. `auto_ink`. Six of
them hold a beached oarfish over Doug's head at scale 0.42 (the fish bottom rests at y ~606 on canvas).

### `rope_puller`: s142 s155
A crude-tier stick man (no cap) **leaning back at about 25 degrees, pulling on a rope** that runs off to the left: both hands
together at about (-90,-250), heels dug in, knees bent. Anchor = feet (0,0); x -120..+80, y -430..0. `auto_ink`. Fifteen are drawn
in a row at 0.26 on sand to drag the Catalina fish ashore (the rope line is drawn in the shotlist), so it must read at about 110 px tall.

### `cooler_box`: s045 s048 s049
A white and blue field cooler (a lab sample cooler): a box with a lid, a handle and a white sticker area. No logos and no text.
Anchor centre; x -110..+110, y -80..+80. It stands on sand between two stick scientists at 0.45-0.5.

### `desk_drawer`: s076
An open wooden desk drawer seen slightly from above: a brown `#8b5a2b` front with a round knob, the drawer pulled out to show a
cream interior holding a few pens and a small stack of pre-printed **blank** label stickers. No text. Anchor centre; x -400..+400,
y -200..+200; the interior's opening edge is at about y -150. The narrator's hand lowers a red "DOUG DEATHS: 428" label sticker
(a shotlist `label`) into it from the right at about (1010,600) on canvas.

### `krill_costume`: s089 s090
A flat, empty krill costume held up on a hanger (the narrator considers it and puts it away): a pink-orange `#f08a7a` curved
krill suit with a face opening (no Doug inside), printed black eyes on the hood, two antenna stalks, a row of floppy felt legs
and a zipper down the front. The library `*_costume_flat` pieces carry printed X eyes; this one is **unworn and alive-looking**, so
use plain dot eyes instead. Anchor centre; x -200..+200, y -250..+250, with the hanger hook at about (0,-250) for the narrator's
fingertips. Used at 0.5-0.7 on twilight `#1b4f86`, so give it a thick black outline.

### `park_bench`: s105 s106
A wooden park bench: brown `#a0522d` slats (three seat, two back) on black cast-iron legs and armrests, with a glossy "wet" sheen
(a few white highlight strokes). No sign baked in: WET PAINT is a separate shotlist label above it. Anchor bottom-centre (feet on
y=0); x -350..+350, y -260..0. Used at 1.2 on cream.

---

Reused from the library (no request): `giant_oarfish` (vertical, and rotated -90 for horizontal), `giant_oarfish_beached`,
`krill_cloud`, `tape_measure` (also the HUD icon), `phone`, `sofa`, `torch`, `hiking_backpack`, `hard_hat`, `old_book`,
`silver_fish`, `red_x`, `question_mark`, `exclamation_mark`, `warning_triangle`, `thermometer`, `mayflower_ship`,
`record_book_open`, `water_splash`, `doug_cap`, `old_drawing_card`, `chicken`, `calendar`, `scientist`, `scientist_woman`,
`stick_man_plain`, `tourist_camera`, `minivan`, `beach_towel`, `microphone`, `yellow_submarine`, `rov`, `broom`, `shark`,
`giant_isopod` (at 0.2 as the fin's parasitic isopod), `narrator_hand`, `ruler`, `city_bus`, `rice_grain`, `pressure_gauge`,
`lizard`, `car_half`, `diver`, `microscope`, `gravestone`.
