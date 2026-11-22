# 055 asset requests (director, 2026-11-22)

11 new drawings. The shotlist already places them with the anchors, sizes and local coordinates below, so keep those or
tell me what changed and I'll re-place them. Creatures and props are the detailed tier (layered fills, interior shading,
outlines 3-5). Worn props sit over Doug: anchor = Doug's hips (0,0), same x/y/scale as the `doug` element, listed after
him, and his head, face and red cap stay fully visible.

**Kid appeal and gore are the top risks (brief section 7).** The calf and the costume are grey, wrinkled and deadpan: no big
eyes, no smile, no blush, no pastel, nothing plush. No wounds, bite marks or blood on any whale. Orcas never bite anything.

**HUD budget:** DOUG DEATHS plus THE RING card fill x 1300-1860, y 100-320 on every shot (the card is a 160x112 tile under the
counter, drawn in the shotlist, nothing to draw). Tall drawings stay below y 320 wherever they reach x > 1300.

**Reused from the library (no work needed):** `sperm_whale`, `sperm_whale_top` (every top-down ring is built from it, rotated
heads-in), `sperm_whale_fluke`, `sperm_whale_tooth`, `orca`, `orca_female`, `orca_fin`, `false_killer_whale`,
`false_killer_whale_fin`, `false_killer_whale_tuna` (048 callback), `research_ship`, `hydrophone`, `crt_tv` (the LIVE monitor),
`world_map`, `pacific_map`, `caribbean_map`, `north_america_map`, `iceberg`, `ice_chunk`, `dryas_flower` (the daisy),
`school_bus`, `small_car`, `house`, `fire_flames`, `fire_alarm_pull`, `journal_paper`, `trophy_cup`, `placard`, `signboard`,
`officer_cap`, `clipboard`, `calendar`, `clock`, `wait_stopwatch`, `binoculars`, `ear_icon`, `harbor_seal`, `porpoise`,
`salmon`, `small_fish`, `giant_squid`, `scientist`, `scientist_woman`, `narrator_hand_pencil`, `doug_cap`, `water_splash`,
`water_splash_small`, and the annotation set (`question_mark`, `exclamation_mark`, `red_x`).

**Art director, sign-offs (brief):** the calf costume below, and THE RING card (built in the shotlist: dark `#14365e` tile,
grey whale dots that join and close into a ring at item 5, small black fins with a white edge that only increase: 0, 2, 6,
9, 9 (item 7 flips to a mini world map with two red ticks at the Galápagos and one at the Gulf), 12, 20, 35; red frame from
death 408 on).

---

## 1. `sperm_whale_calf_costume` (129 shots: Doug's main look in items 1, 2, 4-9)
- Shots: s002-s014, s017-s018, s020-s026, s029-s035, s037-s043, s047-s054, s057, s068-s084, s087, s091-s128, s133-s177
  (where Doug appears), s188-s191, s198. Item 3's kayak run (s059-s066) is the only stretch without it.
- What: Doug's homemade grey felt sperm whale calf suit, same build as `gray_whale_calf_costume` (021) but a sperm whale:
  - **Hood:** a blunt, block-shaped grey head (the sperm whale's box nose) jutting forward *above* the cap brim, with a
    flat front face, an S-shaped blowhole slit at the front-left top, deep wrinkle lines and a few pale scar rings.
    A narrow pale underslung jaw line can run along the hood's lower edge. A tiny eye at most, set low and back, or none.
    **No big eyes, no smile, no teeth showing.** Grey C of hood round the back of the head and under the chin, face and
    the whole red cap clear.
  - **Body:** dark grey `#5a5f66`-ish felt (match `sperm_whale`'s grey family) with a darker back side, wrinkled ridges,
    a zipper; small paddle flipper mitts at the float hands (±102, -138); tail stock and triangular notched flukes out of
    the lower back to about (-222, +158).
- Facing right; the shotlist sets `flip: true` with Doug `facing: left`.
- Fitted to the `float` pose (every costume shot uses `float`). Scales used: 0.3-0.8 (0.3 in top-down rings, 0.75-0.8
  for close-ups). Must read on light sky `#8fd3ff`, mid sea `#2a6aa6`-`#18497e` and dark `#14365e` (Doug auto-inks white
  there, so keep the suit's own outline black and the fills mid-grey).

## 2. `sperm_whale_calf` (32 shots)
- Shots: s002, s005, s006, s013-s016, s022, s024-s028, s030-s032, s034, s036-s038, s041-s046, s048, s051, s055-s057, s067.
- What: a real newborn sperm whale, side view facing right. Same style as `sperm_whale` but a calf: paler slate grey,
  shorter boxy head (about a quarter of the length, not a third), smooth-ish skin with soft wrinkles, few or no scar rings,
  small paddle flippers, notched flukes, small half-lidded eye (it sleeps through death 403, and the same drawing has to
  work awake). **Not cute:** no big round eye, no smile, no blush.
- Size: about 415 x 130 at scale 1 (x -210..+205, y -65..+65), anchor centre. Used at 0.2-0.62: next to `sperm_whale` at
  0.4-0.45 it is about a third of the adult's length, as in life (4 m vs 11 m).
- Used once at `rotate: -14` (rolling over in its sleep, s044) and on cream cards next to `small_car`.

## 3. `big_headphones` (s081-s084)
- What: enormous padded over-ear headphones, black band and cups with grey padding, a coiled grey cable dropping from the
  front cup. Worn prop on the costume: anchor = Doug's hips, listed **after** `sperm_whale_calf_costume` at the same
  x/y/scale (0.6 and 0.75), fitted to the `float` pose: band arcs over the hood, cups over the ears at the sides of the head.
  Face and cap stay clear. The shotlist draws the hydrophone cable from his front float hand (+102, -138).

## 4. `sea_kayak` (s059-s064)
- What: a single sea kayak, side view facing right: long low red or yellow hull (pick one that reads on `#dfe7ee` ice sky
  and `#3a9ad9` water), pointed upturned ends, dark cockpit rim, deck bungees, a double-bladed paddle resting across the
  deck in front of the cockpit (Doug's hands don't have to hold it).
- Anchor (0,0) = waterline at the hull centre; hull about 640 x 90 (x -320..320, y -60..+30).
- Doug sits in it: the shotlist draws Doug (`sit`, once `point`) **before** the kayak at x = kayak x, hip y = waterline - 40,
  Doug scale 0.6 with kayak scale 0.9, so the cockpit rim must hide his legs and hips (rim top about y -45 local x 0.9).

## 5. `cap_snow` (s060-s064)
- What: a small heap of snow sitting on top of Doug's cap (snow building up as he waits), white `#ffffff` mound with pale
  blue-grey `#cfd8e0` shading and 3-4 loose flakes. Worn prop: anchor = Doug's hips, same x/y/scale (0.6), fitted to the
  `sit` and `point` poses (same head position). Sits on the cap crown, never covering the brim or face.

## 6. `doug_frozen_kayak` (s065 death 404, s066 close-up)
- What: the death 404 image (brief: "iced over, cap frozen on top; **not** the 007 ice-block return"). The same kayak as
  `sea_kayak` with Doug seated in it, turned stiff and frost-white: pale `#e9f4fb` body and head with `#bcd8ec` frost
  shading and a few icicles off the arms, X eyes, flat mouth, frost crust on the shoulders. The red cap stays red but frosted
  white on the crown (it must still read as the cap), still facing right, "toward the tropics". No ice block around him.
- Anchor and scale identical to `sea_kayak` (waterline centre); Doug's figure matches a rig Doug at 0.667 x asset scale with
  hips at local (0, -44). Placed at 0.9 (s065) and 1.2 (s066, close-up with zoom).

## 7. `shift_rota_clipboard` (s035, s039, s040)
- What: a big clipboard: brown board, silver clip at the top, white sheet with a faint grey ruled table (3-4 rows, a narrow
  time column on the left). **Blank** of text: the shotlist overlays "SHIFT ROTA", "08:00 GRAN", "09:00 AUNT" and Doug's
  name pencilled in red in another handwriting. Deadpan office paperwork, not a nursery chart.
- Anchor centre, about 380 x 500 (x -190..190, y -250..250). Sheet clear for text from y -200 to +80 (title at -180, rows at
  -80, -20, +40/+50), x -150..+150. Clip above y -200.

## 8. `bunker_cutaway` (s016, "a family that owns a bunker and won't use it")
- What: backyard bunker in cross-section under a lawn: above ground only a low hatch (open lid) and a vent pipe (≤ 60 px
  tall); below, brown soil cutaway `#8a6a4a` with a grey concrete room (shelf with tins, a bunk) reached by a **steep, narrow
  ladder-stair** from the hatch. The stairs are the joke, so make them steep.
- Anchor (0,0) = ground line at the centre; about 760 wide (x -380..380), soil cutaway down to y +440; hatch at local
  (+280, 0) (the calf sits beside it at +340). Ground in the shot is lawn green `#7cc25a` from y 520 down.

## 9. `castle_wall_cannons` (s124, "a castle wall lined with cannons, and nobody has lit a single one")
- What: a grey stone crenellated castle wall, front view, block texture, 4 black cannon muzzles poking out of embrasures,
  fuses unlit (no flames, no smoke, no sparks). Flat cartoon, no figures.
- Anchor bottom-centre on the ground; about 1400 x 400 (x -700..700, y -400..0). Keep the top at y ≥ -400 so the
  crenellations stay under the HUD (placed at (960, 760), scale 1).

## 10. `hand_bell` (s079, s080, hide-and-seek analogy)
- What: brass hand bell with a turned wooden handle, gold `#d9a63a` with a lighter highlight and dark rim, clapper visible
  under the mouth. Anchor centre, about 200 x 260. Used at 0.55-0.7, rotated -15; the shotlist adds the ring lines.

## 11. `pilot_whale_fin` (s133, s137, s138)
- What: a surfacing short-finned pilot whale: a **low, very broad-based, strongly hooked** black dorsal fin set well
  forward, on a strip of black back with a hint of the round melon at the right; mid-grey leading-edge highlight so it reads
  on `#1f5a94` water; white ripple at the waterline. Must look clearly different from `false_killer_whale_fin` (taller,
  narrower) and `orca_fin` (tall and straight).
- Facing right, anchor bottom-centre on the waterline (y = 0), about 300 x 180 (x -150..150, y -180..+10). Used at 0.25-0.5.
