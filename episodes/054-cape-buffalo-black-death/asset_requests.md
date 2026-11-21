# 054 asset requests (director, 2026-11-21)

32 new drawings. The shotlist already places them using the anchors, footprints and landmark points below (local units, scale 1).
Please keep those, or tell me what changed and I'll re-place them. I checked every shot with grey boxes of exactly these footprints
(`build/preview.py` → `build/preview/sheet_*.png`), so a drawing that grows much past its box will hit the HUD, the caption bar or a
neighbour. Everything faces RIGHT unless noted; the shotlist flips.

**Tiers.** Buffalo, birds, places and diagrams are the detailed tier: layered fills, interior shading (`spray`, darker back / lighter
belly), texture strokes 2-3, outlines 3-5. The one human (`cleaner_human`) is the crude tier: Doug's line weight, `auto_ink`,
`keep_ink` on white face fills. The two costume drawings are worn props over Doug's rig.

**Creative-director notes (decisions.md) that these requests carry:**
1. **Draw the buffalo fresh.** No 034 bison drawing and no 022 `water_buffalo` as a base, reference or recolour. Cape buffalo read
   differently: no hump-and-beard bison shape, no swept-back water-buffalo horns. Their horns droop down and out from a heavy fused
   **boss** on the forehead and curl up at the tips. The ears hang below the horns. The body is barrel-shaped with a straight back.
2. **Page-a-day calendar** for item 2 (`page_a_day_calendar`): a new desk-block calendar. It is not the library `calendar`, which is
   the 034 wall calendar with the red binding.
3. **Closing (s205-s206):** the red cap rides on a buffalo's **back** among oxpeckers (`cape_buffalo_bull` back line, below), not on
   a horn.
4. **HEAD COUNT board:** see the art director section at the end.

**Safety and tone (brief section 7):** no wounds, blood, gored or trampled animals, and no injured lion or calf, anywhere. The
oxpeckers' hide is clean: birds only, nothing drawn where they feed. The calf is not cute (adult proportions, small eyes, no big
baby eyes, no blush). Lions are the existing library lions. Nothing should look like a hunting trophy (no mounted heads, no rifles).

**Buffalo palette (please use it on every buffalo drawing so they match):**
- bull hide mid-charcoal `#4a4440`, shading `#34302d`, highlights `#6a625c`. This is mid-tone on purpose, as with the 034 bison rule:
  the buffalo has to read on the dusk oranges (`#e88a4a`, `#c9663a`) and on the dust tan, not vanish into them.
- dried-mud crust `#9a8462` in cracked plates on the flanks and legs of bulls (the "dagga boy" look), with `#7a6a4a` crack lines
- cows browner `#5a4a42`, calf red-brown `#7a4a2a`
- horns and boss `#2a2a2a` with ridged texture strokes, tips grey `#8a8a8a`; eyes small and dark with a hard, flat stare
- every buffalo that is used as `"silhouette": true` (noted below) needs one clean outer shape: no loose floating bits

**HUD (every shot from s004):** death counter (size-44 label centred at 1590,162), then the HEAD COUNT board under it: a rect
x 1380-1800, y 212-266, with `buffalo_head_icon` at scale 0.3 centred at (1338,239). Together they fill about x 1300-1860,
y 110-275. Tall drawings are placed so they stay below y 290 on that side.

**Reused from the library (no work needed):** `field_guide_open` (CAPE BUFFALO page, FRIEND? box left empty, NO / MAYBE stamps),
`compact_camera`, `reeds`, `savanna_bush`, `grass_tuft`, `safari_jeep`, `tourist_camera`, `lion_male`, `lion_male_leaning_back`,
`lioness`, `lioness_walking`, `lioness_running`, `lioness_crouched`, `lioness_sitting`, `lion_head_icon`, `croc_head_rising`
(silhouette only), `cow`, `dairy_cow`, `deer_fence`, `tick_unfed` (as a generic tick, small), `virus_blob` (foot-and-mouth),
`magnifying_glass`, `south_africa_map`, `tanzania_map`, `old_book`, `clipboard`, `chalkboard`, `reward_poster`, `signboard`,
`street_sign_blank`, `placard`, `small_car`, `bathroom_scale`, `upright_piano`, `small_table`, `stick_man_plain`, `lunchbox`,
`dust_plume`, `eye_icon`, `doug_cap`, `thermometer`, and the annotation set (`question_mark`, `exclamation_mark`,
`warning_triangle`, `red_x`).

---

## Buffalo

### `cape_buffalo_bull` **DONE** (assets/previews/054-assets-a.png)
The workhorse: an old Cape buffalo bull (*Syncerus caffer caffer*) standing, side view, facing right, head held a little low.
- Look: heavy barrel body on short thick legs; a straight back with a slight rise at the shoulders; a short neck; a big head with a
  fused **boss** across the forehead and horns that sweep down and out, then curl up and forward at the tips. Ears hang below the
  horns. Thin tail with a dark tuft. Dried-mud crust plates on the flanks and legs. Muzzle dark and wet-looking.
- **Anchor bottom-centre (hooves on y=0). Footprint x -390..390, y -430..0.** Horn tips at about y -400.
- **Back line (important):** the top of the back is a fairly flat surface from (-260,-330) to (+130,-340). The shotlist stands
  oxpeckers (feet anchor) and the red cap directly on it (s046, s048, s050, s052, s061, s070, s205, s206). Please keep it smooth and
  free of spikes there. The shoulder rise sits just behind the head, at about x +150.
- Used as `silhouette: true` in s025. Used flipped (walking away, facing left) in the closing.
- Size: about 1.5 m at the shoulder, so it towers over Doug (Doug at scale 0.5 is about 225 px tall).
- Shots: s002, s009, s011, s013-s016, s025, s032-s035, s045-s048, s050, s052, s059-s061, s070, s074, s080-s081, s085, s114, s119-s124, s127, s129-s133, s158, s162, s164, s166, s179, s189, s204-s206.

### `cape_buffalo_bull_front` **DONE** (assets/previews/054-assets-a.png)
The same bull **head-on**, staring straight at camera with the head low and the boss front and centre. Horns spread wide and droop,
then curl up at the tips. Mud on the chest and legs. The hard stare is the point (this is the "retired neighbour" glaring over the fence).
- **Anchor bottom-centre. Footprint x -320..320, y -500..0.** Boss centre about (0,-380). Horn tips about (±310,-420): s031 draws a
  red dotted line between them at that height.
- Shots: s017-s018, s031, s039, s157, s159, s161, s167-s169.

### `cape_buffalo_wallowing` **DONE, revised after art review fix 1** (assets/previews/054-assets-r1.png)
_Revision: the full-height bands are now 5 short irregular mud drips (some slanting) off the back line. The back has a shoulder rise behind the head and a rounded rump. The mud lip, the anchor and the boss at (+200,-170) are unchanged; drawn x -345..345 (the lip, as before)._
The old bull lying in a mud wallow up to his shoulders: only the top of the back, the head, the boss, the horns and the stare are
above the mud. Wet dark mud streaks on the visible hide.
- **Anchor = the mud surface line (0,0). Footprint x -330..330, y -230..+10.** Head on the right, boss at about (+200,-170).
  The shotlist draws the mud pool (`#8a6a4a` ellipse) under it. Please add a soft mud-coloured lip along y 0 so the body visibly
  sinks into it, with no hard cut line.
- Shots: s004-s008, s012, s019-s022.

### `cape_buffalo_lying` **DONE** (assets/previews/054-assets-a.png)
A bull lying down on his belly (sternal), legs folded under, head up, side view facing right. He looks settled and in no hurry.
- **Anchor bottom-centre. Footprint x -350..350, y -320..0.** Muzzle tip at about (+340,-150): s041/s042 draw chewing marks just
  right of it.
- Used as `silhouette: true` (glow_r 0) in s075, s079, s082.
- Shots: s015-s016, s041-s044, s074-s075, s079, s082, s102.

### `cape_buffalo_head_boss` **DONE, revised after art review fix 2** (assets/previews/054-assets-r1.png)
_Revision: the boss grid is now broken wavy transverse ridges following the dome, plus short cracks and a dark hair edge. The neck widens into shoulders that run down to local y +380. Nothing above y +200 moved. **NEW FOOTPRINT x -360..360, y -260..+380** (director: s026 bottom y 1101, s027/s030 bottom y 1096, all off-frame)._
A close-up of a bull's head in 3/4 front view, from the neck up: the boss as a thick ridged helmet across the top of the skull
(clearly one continuous shield), horns sweeping out of it, ears below, a flat hard stare, mud specks. This is the "helmet" hero
drawing, so give the boss texture plenty of detail (ridges, grooves, a darker edge where it meets the hair).
- **Anchor centre. Footprint x -360..360, y -260..260.** Boss centre about (0,-130). The neck runs off the bottom edge (it is always
  placed so the bottom is cropped by a card or another element; no flat cut line visible).
- Shots: s026-s027, s030.

### `boss_stage_1`, `boss_stage_2`, `boss_stage_3` **DONE** (assets/previews/054-assets-a2.png)
A three-step diagram of the horn bases from the front (the same framing each time, only the horns change), on a transparent background:
1. young bull: two separate horn bases with a clear gap of hair between them, horns thin;
2. older: the bases thicker and spreading toward each other, a narrow gap left;
3. mature: the bases fused into one continuous shield across the top of the head, solid and dark.
- **Each: anchor centre, footprint x -160..160, y -140..140.** Same head outline in all three so they read as a sequence. No text
  (the shotlist adds YOUNG / OLDER and the SOFT / HARD labels).
- Shots: s028-s029, s036-s038.

### `cape_buffalo_cow` **DONE** (assets/previews/054-assets-a.png)
An adult cow standing, side view facing right: a lighter build than the bull, browner hide, thinner horns with **no boss** (a gap
of hair between the horn bases), no mud crust. Head up and alert (she is "voting": staring in one direction).
- **Anchor bottom-centre. Footprint x -350..350, y -380..0.** Used flipped (facing left) in most shots.
- Shots: s013-s014, s097-s101, s104, s108-s110, s132, s141.

### `cape_buffalo_cow_lying` **DONE** (assets/previews/054-assets-a.png)
The cow lying down (sternal), head up, side view facing right.
- **Anchor bottom-centre. Footprint x -320..320, y -280..0.**
- Shots: s095, s097-s099, s107.

### `cape_buffalo_charging` **DONE** (assets/previews/054-assets-a.png)
A bull in a heavy charging run, side view facing right: head down so the boss leads, horns forward, legs mid-gallop, a couple of
small dust puffs at the hooves (tan `#e2d3b0`, no stars). No contact with anything.
- **Anchor bottom-centre (lowest hoof on y=0). Footprint x -400..400, y -400..0.** Used flipped.
- Shots: s040, s140, s149, s165.

### `cape_buffalo_calf` **DONE** (assets/previews/054-assets-a.png)
A calf a few months old, standing, side view facing right: red-brown hide, small stubby horn buds, adult proportions, small eyes. It
must not look cute (brief risk: no nursery look) and must not look hurt. In s150 it is simply walking back to the herd, unharmed.
- **Anchor bottom-centre. Footprint x -190..190, y -250..0.**
- Used as `silhouette: true` (glow_r 0) in s146-s148.
- Shots: s013-s014, s102, s146-s148, s150.

### `buffalo_herd_wall` **DONE** (assets/previews/054-assets-a2.png)
A herd bunched tight and facing the viewer: about six to eight identical buffalo heads and shoulders in two staggered rows, horns
pointing out, all with the same hard stare (style bible: crowds are drawn as repeated identical heads). A solid wall of bodies, with
the front row lower and larger.
- **Anchor bottom-centre. Footprint x -700..700, y -420..0.**
- Used as `silhouette: true` (glow_r 0) in s113, and flipped in s204 (there it should read as the herd walking away into the dust,
  which is fine at that small size).
- Shots: s111, s113, s135-s139, s141-s143, s148-s153, s175-s177, s179, s196-s197, s204.

### `buffalo_herd_resting` **DONE, revised after art review fix 3** (assets/previews/054-assets-r1.png)
_Revision: 8 animals, every head up at 1.3x with clear air round each pair of horns. The back four (facing right) sit at ground y -32/-60/-34/-62; the front four (facing left) have raised heads; small gaps between rumps; bulls and cows mixed. The silhouette shows 8 horned heads. Footprint unchanged._
A herd lying down in grass at rest, side-on: a long row of about eight lying buffalo with overlapping backs and heads, horns of
different sizes (cows and a bull or two), some heads up and some down, all calm. It must read as "dozens of identical buffalo".
- **Anchor bottom-centre. Footprint x -750..750, y -280..0.**
- Used as `silhouette: true` (glow_r 0) in s091.
- Shots: s005, s064-s069, s091-s101, s104, s107-s109, s131-s135.

### `buffalo_megaherd` **DONE, revised after art review fix 4** (assets/previews/054-assets-r1.png)
_Revision: 5 rows at 1.0/0.7/0.5/0.35/0.25 with no backing rectangles. Each row's horns and bosses stand above the row in front, so the skyline is broken horns. The rows narrow toward the back and step down at both ends, with a lone animal past a gap on each side. Dust sits only behind and between the far rows. Checked as a silhouette with glow_r 0 at 0.33. Anchor and footprint box unchanged, but the drawn extent is now about **x -790..870, y -375..0**, a mound that is lower at the ends, no longer a full-width bar._
The dry-season super-herd: a dense mass of buffalo heads and backs filling a wide strip, with the front rows larger and the back rows
smaller toward the horizon, where the top edge fades into tan dust (`#c8b58a` / `#e2d3b0`). It should read as a thousand or more
buffalo at a glance. Repeated identical heads are fine.
- **Anchor bottom-centre. Footprint x -950..950, y -380..0.**
- Used as `silhouette: true` (glow_r 0) at small scale.
- Shots: s003, s180, s185-s186, s188, s193, s199-s202.

### `buffalo_head_icon` **DONE** (assets/previews/054-assets-a.png)
A small flat front-view buffalo head icon: the boss and drooping horns, ears, eyes and muzzle, thick outline, mid-charcoal fill. This
is the HEAD COUNT board's icon at **scale 0.3 (about 48 px wide)**, so it must read at that size: chunky shapes, no thin detail. It
is also used large (1.0-1.6) on cream cards, the review page and the job poster.
- **Anchor centre. Footprint x -80..80, y -55..55.**
- Shots: every shot from s004 (HUD), plus s051, s103, s116, s128, s160, s171, s184, s207.

## Birds

### `oxpecker` **DONE** (assets/previews/054-assets-b.png)
A red-billed oxpecker perched and clinging, side view facing right: plain olive-brown back and wings, pale buff belly, a bright red
bill, a yellow eye-ring around a red eye, and a stiff tail pressed down as a prop (they climb like woodpeckers). Feet gripping.
- **Anchor = feet, bottom-centre (0,0). Footprint x -70..80, y -95..0.** It stands on the buffalo back line, on Doug's chest, and on
  the ground.
- Shots: s046-s050, s052-s059, s061, s065-s066, s070, s205-s206.

### `oxpecker_yellow` **DONE** (assets/previews/054-assets-b.png)
The yellow-billed oxpecker: the same pose and size, with a thicker bill that is yellow at the base and red at the tip, a paler rump
patch, and the same yellow eye area. It sits next to `oxpecker` in s049 at scale 2.4, so the bill difference must be obvious.
- **Anchor = feet. Footprint x -70..80, y -95..0.**
- Shots: s049, s051.

### `oxpecker_flying` **DONE** (assets/previews/054-assets-b.png)
The red-billed oxpecker in flight, wings up, facing right.
- **Anchor centre. Footprint x -100..100, y -70..70.**
- Shots: s065, s067, s070.

## Places, props and diagrams

### `acacia_tree_day` **DONE** (assets/previews/054-assets-c.png)
A flat-topped umbrella thorn acacia in daylight (the library `acacia_tree` is a near-black sunset silhouette, so it doesn't work here):
grey-brown trunk with bark strokes forking low, a wide flat green crown, a few visible thorns on the twigs.
- **Anchor bottom-centre. Footprint x -380..380, y -680..0.** Crown y -680..-540.
- **Branch (important):** one long, nearly horizontal branch leaves the trunk to the right with a flat top surface at **y -330 from
  x +60 to +400**. Doug sits on it (seat at +200, -330, Doug scale 0.45, head up to y about -500) and the page-a-day calendar stands
  on it at (+330,-330) at scale 0.8 (top about y -490). Keep clear air above that branch up to the crown bottom (y -540).
- Shots: s040-s046, s073.

### `page_a_day_calendar` **DONE** (assets/previews/054-assets-c.png)
A desk page-a-day calendar: a small block of tear-off pages in a plain plastic or wooden stand, the top page white with a thin red
header strip, and a few torn stubs at the top edge where pages were ripped off. It is not the 034 wall calendar.
- **Anchor bottom-centre. Footprint x -90..90, y -200..0.** **Blank page area centred on (0,-105), at least 132x90 clear**: the
  shotlist writes AGE 2 / AGE 5 / AGE 9 and DAY 1 / DAY 2 / DAY 3 there, and covers the old text with a white rect of exactly
  x -66..66, y -150..-60.
- Shots: s036-s038, s041-s046.

### `calendar_page_flying` **DONE** (assets/previews/054-assets-c.png)
One torn-off page in mid-air: white with the thin red header strip, curling, with a couple of small motion ticks. Blank.
- **Anchor centre. Footprint x -60..60, y -50..50.**
- Shots: s037-s038, s042.

### `garden_fence` **DONE** (assets/previews/054-assets-c.png)
A suburban white picket fence section with a little gate in the middle, posts sunk in a lawn line. It must hide the bull's legs
(the bull stands behind it).
- **Anchor bottom-centre. Footprint x -500..500, y -230..0.**
- Shots: s017-s018, s039.

### `cleaner_human` **DONE** (assets/previews/054-assets-b.png)
Crude tier (Doug's line weight 5, `auto_ink`), a generic stick-figure house cleaner: big round white head with the grey crescent, a
headscarf, a blue apron over the body line, and a feather duster raised in the back hand. **Front hand free at about (+115,-240)**:
the shotlist puts `juice_box` there.
- **Anchor = feet (0,0), like `stick_man_plain` (hips at (0,-150)). Footprint x -120..140, y -460..0.** Neutral, pleasant face. No cap.
- Shots: s062-s063.

### `juice_box` **DONE** (assets/previews/054-assets-b.png)
A small kids'-style juice box with a bendy straw: a red-pink fruit-punch carton with a simple cartoon cherry on the front, a white
straw bent over the top-left corner. It must read as a juice box, not as anything medical. The shotlist writes DOUG on the front
(centre about (0,+15), 22 px white text with a black outline) for the "little sip of you" joke.
- **Anchor centre. Footprint x -40..40, y -60..60.**
- Shot: s063.

### `car_wash_brush` **DONE** (assets/previews/054-assets-b.png)
An upright car-wash roller brush: a tall cylinder of dense blue and red bristle strips on a grey metal frame and axle, with curved
spin lines either side.
- **Anchor bottom-centre. Footprint x -160..160, y -620..0.**
- Shot: s077.

### `crash_helmet` **DONE** (assets/previews/054-assets-b.png)
A small full-face motorbike crash helmet: glossy white with one red stripe and a dark visor. It sits on the roof of `small_car`.
- **Anchor bottom-centre. Footprint x -95..95, y -140..0.**
- Shots: s034-s035.

### `cow_costume` **DONE** (assets/previews/054-assets-b.png)
Doug's cow costume (a worn prop, built like `sheep_costume`): a black-and-white Holstein-patch onesie over the torso, arms and legs,
hoof mittens and hoof boots, and a hood forming a C round the back of the head with two small pale horns and floppy ears behind the
cap. **Face and red cap fully visible.** No udder.
- **Anchor = Doug's hips: listed after Doug at the same x/y/scale. Fitted to the `stand` pose. Footprint about x -150..130,
  y -292..158.** Used flipped (Doug facing left, scale 0.6).
- Shots: s131-s133.

### `cow_costume_flat` **DONE** (assets/previews/054-assets-b.png)
The cow costume lying empty and flat on the grass (same family as `bee_costume_flat`): a squashed patchy suit with a collapsed
collar hole on the right, the hood flopped, and **printed X eyes on a small cow face** on the hood front, plus a zipper so it reads as
a costume, never as a dead cow. No Doug inside.
- **Anchor bottom-centre (ground y=0). Footprint x -260..260, y -150..0. `doug_cap` goes at about (+120,-75).**
- Shots: s134-s135.

### `botswana_map` **DONE** (assets/previews/054-assets-c.png)
Botswana in the `world_map` style: flat green land with a dark outline, a black frame, no labels and no fences (the shotlist draws
the red fence lines). Show the Okavango Delta as a light-blue fan in the north-west, the Makgadikgadi salt pans as pale cream
patches, and a faint lighter tan patch for the Mababe Depression. Neighbouring countries in a muted grey-green outside the border
(so Botswana reads as the subject).
- **Projection: lon 19.5..29.5 E, lat 17.5..27.0 S, 80 px per degree, x = (lon - 24.5) x 80, y = -(lat + 22.25) x 80, anchor centre.
  Footprint about x -400..400, y -380..380.** The shotlist draws fences at fixed lon/lat (Namibia border fence at 20 E, the Northern and
  Southern Buffalo Fences round the delta, the Kuke fence near 21 S) and rings Mababe at (24.4 E, 18.75 S), so please keep the
  projection exact.
- Shots: s115-s116, s187.

### `globe_earth` **DONE** (assets/previews/054-assets-c.png)
A cartoon Earth globe (no stand): blue oceans, flat green continents with dark outlines, Africa facing the viewer, a thin white
highlight arc. On a navy card.
- **Anchor centre, radius 240 (footprint x -250..250, y -250..250).** s117 draws a red dashed arc a quarter of the way round over the top.
- Shot: s117.

### `parasite_blob` **DONE** (assets/previews/054-assets-c.png)
The Corridor disease parasite stand-in (*Theileria parva*, never named on screen): a faceless cartoon blob, a pale orange-pink
teardrop or comma shape `#f0a080` with a darker `#c0604a` nucleus dot and a soft outline. Not purple and not spiky, so it never looks
like `virus_blob`. No face.
- **Anchor centre. Footprint x -65..65, y -65..65.** Reads at scale 0.6.
- Shots: s124-s125, s127.

---

## Art director sign-off

1. **HEAD COUNT board (brief section 2, decisions note 4).** The shotlist draws it, so no asset is needed apart from `buffalo_head_icon`.
   It is a cream `#e8dcc0` board (x 1380-1800, y 212-266, brown `#5a3a1e` 5 px frame), text "BUFFALO VS DOUG: <n>" in bold `#2b2b2b`,
   size 25, centred at (1590,239), with the icon at 0.3 to its left. It is staging only and never read aloud. Values, which only ever go up:
   **1** (s004-s091), **DOZENS** (it pops in at s092 "The herd."), **HUNDREDS** (it pops in during s185 "swells into hundreds"),
   **1,000+** (it pops in during s199 "A thousand buffalo arrived"), then at the boss death (s203) the board turns red-on-pink
   `#ffd2cc` / `#e0201b` and a large red "1,000+" stamp appears mid-frame. It stays red through the closing. One deviation from the script's
   stage direction: item 9 asked for the board to read "5,000?" at the dust-cloud line, which would make the count go down to
   1,000+ afterwards. I kept the board monotonic as the brief requires and put "ABOUT 5,000" on a label beside the herd in s193 instead.
2. **Buffalo palette** above (mid-charcoal hide so it reads on the dusk ramp). Please confirm it, or set the values you want in the art bible.
3. **Episode colour ramp (shotlist, no asset):** one step per item, from bright midday to dusty dusk as the head count grows:
   Dagga Boy hot sun `#fff3c0` / ground `#c9a24a` (mud `#8a6a4a`); Boss `#cfe9ff` / `#d9b45a`; Hitchhikers `#8fd3ff` / `#c9a24a`;
   Thicket `#f6dcae` / `#b8913a`; Vote dusk bands `#8a6a8a` over `#e59a5e` / `#b8913a`; Carrier `#f6c45a` / `#b8913a`; Bodyguards
   `#f2a24a` over `#f6c45a` / `#9a7a4a`; Lion Killer `#b8573a` over `#e88a4a` / `#8a6a3a`; Megaherd `#9a4a32` over `#c9663a` / `#7a5a3a`;
   closing `#c9663a` over `#e59a5e`. Death beats `#0b0f14` / `#141a14`, diagram cards cream `#f4f1dc`, the "200 a year" honesty
   cards `#4a4f5e` with white text, outro `#2a2030`. None of the grounds is green, so the default wordart is used, except on
   the lawn (s017, s018, s039), where all the text is a speech bubble, labels or wordart placed in the sky.
4. **Judgement calls to look at:** s126 puts small red Xs over 8 of 10 cartoon cows for "kills about eight in every ten" (it is cartoon
   and has no bodies, but tell me if you would rather grey them out). s075 uses a red glow behind a lying-bull silhouette in the reeds,
   on a green and tan ground, not on red or brown, so I kept red rather than the purple `#5e4670`.
