# 047-wolverine-snow-climb: asset requests (director, 2026-11-14)

The shotlist already places these by name (generator: `episodes/047-wolverine-snow-climb/build/gen_shotlist.py`, git-ignored;
re-run it after any geometry change), so please **keep the anchor, bounding box and key points** given here: Doug, the cap,
props and arrows are placed on those points. Everything faces right unless noted. House style: detailed tier, thick black
outlines (5-6), flat fills with interior shading. Brief sec 7: **no cute wolverine, no mascot face, no Marvel pose or claws,
no kits anywhere, no blood, no carcass detail** (the library `carcass_outline` is the only "kill" shape). Every wolverine
variant uses the library `wolverine` palette exactly: dark brown `#3e2a1e` coat, darker back and legs, pale tan `#c9a46a`
flank band to the bushy tail, pale forehead band, small round ears, long pale claws.

Reused from the library (no request): `wolverine`, `wolverine_skull` (not used), `radio_collar`, `pine_tree`, `snowy_fir`,
`boulder`, `grey_wolf`, `grizzly_bear`, `moose`, `carcass_outline`, `meat_strip`, `sandwich`, `bread_loaf`, `small_table`,
`dinner_plate`, `leftovers_plate`, `fridge`, `toddler`, `stick_man_plain`, `scientist`, `clipboard`, `telephone_pole`
(car-park lampposts), `signboard`, `street_sign_blank`, `reward_poster`, `old_book`, `journal_paper`, `banknote`, `price_tag`,
`calendar`, `alarm_clock`, `wait_stopwatch`, `satellite`, `world_map`, `usa_map`, `house`, `empire_state_building`, `small_car`,
`hiking_backpack`, `fallen_log` (firewood), `snow_shovel`, `snow_shelter`, `snow_dust_cloud`, `ice_block`, `house_fly`,
`ground_beetle`, `boot`, `paw_print_icon`, `field_guide`, `field_guide_open`, `narrator_hand_pencil`, `doug_cap`, plus the
annotation set (`question_mark`, `exclamation_mark`, `warning_triangle`, `red_x`, `thermometer`).

---

## Episode device

### `altitude_stake` (every shot from s002: the HUD meter icon)
The ALTITUDE stake from the brief: a crude striped wooden snow stake, upright. **Centre anchor, 100 x 400 (x -50..50,
y -200..200)**, used at 0.24 at (1405, 238), just left of the "ALTITUDE: ..." label under the death counter. Four colour bands
from the bottom up, separated by short black tick marks: FOREST `#2f5a48` (y +92..+200, the bottom tip is pointed like a stake
pushed into snow), TREELINE `#b9cde0` (y 0..+92), SNOW `#f7fbff` (y -92..0), SUMMIT `#8d99a6` (y -200..-92, flat top with a
small cap of snow). Thick black outline (6) so it reads on every backdrop (pale sky, cream, black, dawn orange). **No text**
(it would be under 3 px) and nothing at x = 0 on the band centres y +137, +46, -46, -137: the shotlist draws Doug's red dot there.

## Item 1 (The Reindeer)

### `reindeer` (s002, s005, s008, s009, s121, s122, s126, s127, s130)
Adult female (cow) semi-domestic reindeer, standing, side view. Grey-brown coat `#8a7a66` (darker back), pale cream `#e8e0d0`
neck mane and belly, white rump patch, short tail, dark lower legs, broad splayed hooves, dark muzzle, **modest branched antlers**
(cows carry small ones). Calm, not cute: small eye, no big lashes. **Anchor bottom-centre (hooves on y = 0), about 620 x 520 incl.
antlers (x -300..320, y -520..0), shoulder top near y -360.** Used at 0.4-0.75. In s121/s122 it is a plain silhouette, so the
outline must read as "reindeer" in black. In s126, s127 and s130 the shotlist covers everything below its belly with snow
(y > -200 local hidden), so the top half alone (back, head, antlers) must read.

### `reindeer_costume` (s018, s019)
Doug's homemade reindeer suit, a worn prop on the `stand` pose: **anchor = Doug's hips, listed after Doug at the same x/y/scale**
(the shotlist sets `flip` when Doug faces left). Same fit as `moose_costume`: grey-brown felt `#8a7a66` body suit with a pale
cream neck bib, zipper, short sleeves, dark split hoof mitts at about (+-106, +20), a little white tail. Hood round the back of
the head and under the chin, **face fully visible**. Two branched cardboard-brown reindeer antlers rise from the hood at both
temples and spread up and outward (tips about (+-260, -470)) so that **the red cap sits on top in the middle, between and above
the antler bases** (brief: "cap on top of the antlers"). No text.

### `reindeer_costume_flat` (s020, death 357)
The suit gone flat with Doug in it, for `pose: "on_back"`: **listed after an `on_back` Doug at the same x/y/scale, no rotate**.
On_back joints (scale 1): hips (0,0), shoulders (-122,0), neck (-150,0), head centre (-218,0), feet out to about (+150,+70),
ground line y +70. Rumpled felt suit over the torso and legs (x -150..+170, y -50..+70), hoof mitts flopped on the ground, the
two antlers lying splayed on the ground behind the head (x -300..-430, y +10..+70). **Never cover the face, the X eyes or the
cap** (head centre (-218,0), radius about 75, cap above it). Reads on the black death backdrop `#0b0f14`.

### `lynx` (s007)
Eurasian lynx standing, side view: tawny grey `#b89a72` coat with dark spots, pale belly, cheek ruff, **black ear tufts**,
short black-tipped bob tail, long legs, big paws. Anchor bottom-centre, about 520 x 360 (x -250..270, y -360..0), the same
footprint as `grey_wolf` and `grizzly_bear` (they stand in a row at 0.42).

### `fennoscandia_map` (s006, s011)
Norway, Sweden, Finland (with the edge of Russia's Kola peninsula and the Baltic) in the `world_map`/`europe_map` style: flat green
land, dark green outline, light-blue sea with white wave ticks, black frame, **no labels**. Projection x = (lon - 18) * 28,
y = -(lat - 63) * 50; frame lon 4E..32E, lat 55N..71N (x -392..392, y -400..400), anchor centre. Faint dashed country borders;
Sweden and Finland a slightly lighter green so each can be ringed. Key points (the shotlist rings these): Finland centre (26E 64N)
= (+224, -50); Sweden centre (15E 62N) = (-84, +50). Used at 1.0 centred at (760/700, 560).

## Item 2 (The Glutton)

### `wolverine_bloated` (s022, s026, s028, s029, s033, s034, s035)
Olaus Magnus's legendary "gulo" (1555), told as a myth: the library wolverine with a **huge round belly stretched tight like a
drum** (a few taut highlight arcs), short legs barely reaching the ground, same head and palette. Comic, not gross: nothing
leaking, nothing implied about emptying. Anchor bottom-centre, about 460 x 340 (x -220..240, y -340..0). Used from 0.22 (as a
little drawing on an old map and on an old book cover) to 0.8, so keep the silhouette simple.

### `old_map_north` (s026)
Antique "Carta Marina"-style map of the north (inspired, not copied): parchment `#e9dcc0` sheet with torn edges, brown ink
coastlines of Scandinavia and the North Sea, wavy sea hatching, a compass rose, a tiny sea serpent and a little ship in the sea.
**No readable text.** Centre anchor, about 900 x 620 (x -450..450, y -310..310). Keep a clear land patch at about (+135, -40)
(northern Scandinavia): the shotlist puts a small `wolverine_bloated` there.

### `twin_pines` (s029, s039, s040, s041, s042)
Two straight pine trunks growing very close together. **Anchor bottom-centre = the middle of the gap at the ground.** Bark
`#7a4f2c` with darker grooves, each trunk about 110 wide. The gap is a narrow V/hourglass: about 140 wide at the ground
(x -70..+70), **pinched to about 60 at y -150..-200** (x -30..+30, Doug's hip height), then opening to about 300 wide at
y -300..-480 (x -150..+150, Doug's head and cap height). Crowns of dark pine tiers `#2f5a48` from y -560 up to about -1000;
overall about x -300..300, y -1000..0. **The gap must be transparent** (nothing drawn in it): in s040/s041 the shotlist draws
Doug at x = 0 (same scale, `elbows_out` pose) *before* the pines, so the trunks hide his arms and he reads as wedged, head
and cap free in the opening. Used at 0.7 with the base at y 990.

## Item 3 (The Fridge)

### `chest_freezer` (s052)
White chest freezer **with no lid**: open top showing a pale-blue empty interior rim, grey kick grille, and an unplugged power
cord lying on the floor ending in a plug. No brand. Anchor bottom-centre, about 520 x 320 (x -260..260, y -320..0).

### `frozen_food_lump` (s059, s060)
A cached lump of food frozen solid: rounded lump under a pale blue-white ice crust `#dfeef8` with frost sparkle and a slightly
darker blue shadow, a vague brown core `#8a5a3a` just showing at one crack. **No bone, no raw-meat texture, no blood.** Anchor
bottom-centre, about 260 x 160. Sits beside frozen Doug in the boulder cache.

## Item 4 (The Trapline)

### `box_trap` (s063, s064, s065, s066, s073, s074)
Old cartoon wooden box trap, **empty**, door raised: weathered planks `#8a6a4a` with nail dots, a simple lifted plank door at
the front. No animal, no spring or jaw mechanism, nothing how-to. Anchor bottom-centre, about 300 x 200. Used at 0.42-0.6 in a
row along a dotted trail; `meat_strip` sits on top of it at about (0, -165) local.

### `log_cabin_open` (s061, s067, s076)
A small trapper's log cabin, exterior, 3/4-ish front view: horizontal round logs `#8a5a3a` with pale cut ends, snow on the roof,
a stone chimney, one small window, and the **plank door hanging open on one hinge at an angle**, dark interior behind it. Anchor
bottom-centre, about 620 x 560 (x -310..310, y -560..0). Used at 0.55-0.75 on the treeline snow.

## Items 5-7 (The Nose, The Range, The Snowshoes)

### `wolverine_trotting` (31 shots: s019, s056, s061, s063, s065-s067, s072, s089, s095-s100, s104, s106, s108, s110, s113, s115, s118, s120, s125-s127, s129, s130, s134, s135, s166)
The library wolverine in a purposeful trot: back arched, head held low and forward, one front and the opposite hind leg
lifted, tail out behind. **Anchor bottom-centre (paws on y = 0), about 520 x 230 (x -230..290, y -230..0).** **Mouth point at
(+270, -120)**: the shotlist puts a `meat_strip` (s056, s066, s072) or a `sandwich` (s095-s098) in its jaws there, so the
mouth should be slightly open, holding-shaped, not a wide snarl. Also used as a silhouette in s019 (a low shape trotting
in) and as small as 0.14 far away (s099), so the low, long silhouette must read.

### `wolverine_digging` (s038, s046, s089, s092, s095)
The library wolverine head-down in a hole it is digging: rear end and tail up in the air, forelegs and head hidden below the
snow line, snow clumps flying back behind it. **Anchor (0,0) = the snow surface at the hole**, about 420 x 280 (x -220..200,
y -260..+20). It sits on a flat snow surface (s038, s046) and on the top line of a snow cross-section (s089, s095).

### `wolverine_paw` (s124)
Close-up of one wolverine forepaw, seen from the front/below: broad, dark-brown furry paw `#3e2a1e`, five toe pads, **five long
pale curved claws** `#e8e0d0`, furred sole; reads as "this foot is a snowshoe". No blood, no Marvel-style claws (claws stay
curved and animal). Centre anchor, about 420 x 420. Used at 1.1 on cream.

### `paper_map` (s116, s117, s118)
Doug's folded paper hiking map: cream `#efe6cc` sheet with fold creases, green and brown contour blobs and a **red dotted trail
that runs right off one edge of the paper** (the joke: "the map ran out first"). Centre anchor, about 400 x 280. Used held in
Doug's front hand (0.35), large on the ground (1.6), and rotated 25 degrees blowing away (0.6). No text.

### `high_heel` (s131)
A red stiletto high-heel shoe, side view, toe right, **sinking**: the heel and the toe pushed into a little mound of wet sand
`#e8c07a` drawn as part of the asset. Anchor bottom-centre at the sand line, about 280 x 220.

### `snowshoe` (s131)
A classic teardrop wooden-frame snowshoe with rawhide criss-cross lacing and a toe strap, lying flat on snow, seen in a low 3/4
view. Anchor bottom-centre, about 440 x 150.

## Item 8 (The Snow Den)

### `wolverine_den_cutaway` (s143, s144, s145, s146)
Cross-section of a wolverine snow den. **Anchor (0,0) = the snow surface at the centre.** A soft drift mound on top (to y -60);
the cut face of the snowpack `#e6eef5` with faint layer lines from y 0 down to +520; two or three grey boulders `#7a6a58`
half-buried near the bottom (y +360..+520); a network of 2-3 winding tunnels (hollow `#cfe2ee`, darker rims `#9fb6cc`) round
the boulders, with **one entrance at the surface near (+250, 0)** and a chamber at about **(-140, +300)** (the shotlist stands
the library `wolverine` there at 0.32, so the chamber floor is at y +300 and about 220 wide). **Empty: no kits, no bones.**
About 1500 wide (x -750..750, y -60..+530), side edges unoutlined so the shot's own snow cross-section continues; the shot draws
brown ground from y +530. Used at 1.0 with the surface at y 470.

### `doug_snowdrift` (s153, death 362)
A snowdrift in the shape of Doug sitting hunched: a big round head bump on top, rounded shoulders and a knee bump, pure snow
`#f7fbff` with pale-blue shadow `#cfe2ee` and a soft grey outline. **No face, no limbs showing.** Flat ledge on top of the head
bump at **(0, -380)** for `doug_cap`. Anchor bottom-centre, about 360 x 380. Used at 0.75 exactly where `snow_shelter` stood in
the previous shot.

## Item 9 (The Climb)

### `mount_cleveland` (17 shots: s003, s154, s157-s159, s161, s162, s165-s167, s172-s178)
Mount Cleveland, the highest peak in Glacier National Park, as a steep tower of dark rock under ice and snow: rock `#6b5b4b` /
`#7a6a58`, ice and snow `#dfe7ee` / `#f7fbff` in streaks and ledges, shadowed right face. **Anchor bottom-centre; the summit is
exactly at (0, -900).** The **left face is the climb**: a clean, steep silhouette edge from (-450, 0) to (0, -900); the
**right face is the far side**: from (0, -900) down to (+550, 0). Doug, the climbing wolverine, a dotted track and paw prints
are placed *on* those two straight edges at fixed fractions, so keep them nearly straight lines with only small notches (low
shoulders may spread to about x -650 and +700 below y -150). **No summit flag** (the shotlist draws one in s175). Used at 0.95
(base y 1100), 1.0 (dawn close, base y 1160) and 2.1 on a 1920 x 2160 canvas for a pan up (s162), so details must survive both.

### `wolverine_climbing` (s003, s162, s164, s172, s173)
The library wolverine climbing the steep left face of `mount_cleveland`: body pitched nose-up along a slope rising to the right
at about 63 degrees (the face's angle), claws dug in, tail trailing down. **Anchor = the hind paws (0,0)**; the body extends up
and to the right to about (+170, -280). About 300 x 320. Used at 0.2-0.5.

### `crampons` (s172, s173, s174)
Doug's crampons, **strapped on backwards** (the joke): grey steel spiky frames under both boots with red straps, the long front
points sticking out behind the heels instead of in front of the toes. Worn prop for the **`stand` pose only**: anchor = Doug's
hips, listed after Doug at the same x/y/scale/rotate; feet are at about y +152 (check the exact foot points with a test render
of Doug `stand` at scale 1). Small: about 80 x 30 per foot at scale 1.
