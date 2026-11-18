# 051 asset requests (director, 2026-11-18)

21 new drawings. The shotlist already places them with the anchors, sizes and local coordinates below, so please keep
them or tell me what changed and I'll re-place them. Creatures and places are the detailed tier (layered fills, interior
shading, outlines 3-5). The costume is a deadpan felt suit worn over Doug: anchor = Doug's hips (0,0), same x/y/scale as
the `doug` element, listed after him, and Doug's head, face and red cap stay fully visible.

**Gore and kid appeal are the top risks on this topic (brief section 7).** Orcas and sharks get no smiles, no blush, no
sparkly or oversized eyes. No wounds, bite marks, blood or organ imagery anywhere: the beached sharks are clean outlines
with X eyes, and the liver is a flat cartoon icon or a cutaway shape. The seal pups are animals, not plush toys.

**Size budget:** the HUD (DOUG DEATHS plus the SHARKS GONE stopwatch meter) fills x 1300-1860, y 110-260 on every shot.
Tall drawings (the island, the boat) are placed with that in mind, so please keep their heights at or under the numbers
given.

**Reused from the library (no work needed):** `great_white_shark`, `orca_bent_fin`, `shark_fin`, `shark_cage`,
`shark_costume`, `seal_costume`, `seal_costume_prone`, `seal_costume_flat`, `seal_island`, `cape_fur_seal`,
`wait_stopwatch` (HUD icon at 0.16, plus big prop), `field_guide_open`, `narrator_hand_pencil`, `doug_cap`,
`water_splash`, `south_africa_map`, `pacific_map`, `calendar`, `chalkboard`, `small_car`, `small_car_driving`,
`fuel_gauge` (its low needle is the "after the theft" gauge), `fuel_drum`, `thief_sign`, `heart_icon`, `magnifying_glass`,
`pencil`, `scientist`, `diver`, `tourist_camera`, `binoculars`, `clipboard`, `fishing_boat`, `small_fish`,
`ping_pong_table`, `signboard`, `bread_loaf`, `front_door`, `cardboard_box_open`, `compact_camera`, `balance_scale`,
`stadium`, `dryas_flower`, `gravestone`, `bucket`, `flat_rock`, and the annotation set (`question_mark`,
`exclamation_mark`, `warning_triangle`, `red_x`).
**Art director, one approval only:** the SHARKS GONE meter is the 022 `wait_stopwatch` icon at 0.16 beside a size-28
`label` under the counter ("SHARKS GONE: --", then ABOUT 5 MIN, HOURS, WEEKS, MONTHS, ABOUT 1 YEAR, YEARS, and YEARS in
red `#ffd2cc` / `#e0201b` at The Empty Bay). It's a relabel, so nothing needs drawing (brief section 2).

---

## Recurring across the episode

### `orca_fin_bent` (s002, s004, s007, s020, s025-s026, s034, s084, s087-s088, s092, s101, s105, s122, s129, s166, s170, s173, s198-s199)
- **Done (illustrator, 2026-11-18):** `assets/previews/051-great-white-flees-orcas-assets.png`; footprint as requested.
- It's the surfacing version of `orca_bent_fin` (Port and Starboard): the top of a male orca breaking the surface, a tall
  jet-black dorsal fin **collapsed and bent over**, flopping back and down toward the left (tail side), on a short strip
  of black back with the grey saddle patch behind the fin. Add a mid-grey highlight on the leading edge so it reads on dark
  dusk water `#14365e` (same trick as `orca_fin`), plus a white waterline ripple at the base.
- Facing right (it moves right; it gets flipped when it swims left). Anchor bottom-centre on the waterline (y = 0).
- About 280 x 260 (x -140..140, y -260..+10). It's used at 0.3-0.45 on the surface and at 0.1-0.18 as a map icon, so keep
  the silhouette chunky. **It must read as bent at 0.1.**

### `southeast_farallon_island` (s006, s014-s017, s094-s095, s097, s122, s130-s133)
- **Done (illustrator, 2026-11-18):** `assets/previews/051-great-white-flees-orcas-assets.png`; terrace top is a flat ledge at local y -148 (x 40..380): put pup anchors on y -148. Peak (-244,-185), lantern top -220.
- Southeast Farallon Island, California, seen side-on from the sea: a bare, jagged grey-brown granite island with white
  guano streaks, a rocky shoreline and a low flat marine terrace. Its peak is Lighthouse Hill, a steep cone on the left
  third with a tiny white lighthouse on top. No trees and no buildings except the lighthouse.
- It must look clearly different from `seal_island` (a long, low, flat South African outcrop): taller, jagged, with the
  cone.
- Anchor bottom-centre on the waterline. About 1000 x 220 (x -500..500, y -220..0), including the lighthouse. **Please
  don't exceed 220 tall:** it's used at 0.55-0.7 next to the HUD. Elephant seal pups are placed on its terrace at about
  local y -200 to -145, so leave a flat ledge there on the right half.

### `elephant_seal_pup` (s016, s094, s096, s098, s100-s102, s105, s111-s115, s128)
- **Done (illustrator, 2026-11-18):** `assets/previews/051-great-white-flees-orcas-assets.png`; bbox x -158..162, y -134..0.
- A northern elephant seal weaner (the young seals the Farallon sharks hunt): a fat, smooth, silver-grey torpedo body with
  a paler belly, a round head with a short muzzle and whiskers, dark eyes, short front flippers and the hind flippers
  together at the back. It's lying on its belly with its head slightly raised.
- **Not cute:** normal-sized eyes, a neutral mouth line, and no blush or smile. It's an animal on a beach.
- Facing right, anchor bottom-centre (belly on the ground). About 300 x 150 (x -150..150, y -150..0). It's used at 0.3-0.45 in
  crowds of 2-8, often several in one frame.

### `tour_boat` (s022-s026, s072-s074, s076, s087-s091, s143-s144)
- **Done (illustrator, 2026-11-18):** `assets/previews/051-great-white-flees-orcas-assets.png`; wheelhouse x 196..346, top -270 incl. antenna (roof -252); deck y -70, rail -126; davit tip (+200,-120).
- A Gansbaai-style cage-diving tour boat: a white hull with a blue stripe, a small wheelhouse at the front, a railed open
  rear deck, and a short davit arm at the stern that a cage cable hangs from. Leave room on the deck for two
  `tourist_camera` figures. No logos and no text.
- Facing right, anchor = waterline centre. About 700 x 320 (x -350..350, y -260..+60): the hull bottom is at +60 and the
  top of the wheelhouse is at -260. **Please keep it within 260 above the waterline.** The cage is the separate library
  `shark_cage`: the shotlist runs a cable from about local (+200, 0) down to the cage, so put the davit tip at about
  (+200, -120).

### `sevengill_shark` (s052, s054-s060, s062-s063, s065, s068-s069, s142-s144)
- **Done (illustrator, 2026-11-18):** `assets/previews/051-great-white-flees-orcas-assets.png`; x -404..398, y -104..126.
- Broadnose sevengill shark (*Notorynchus cepedianus*), side view facing right. It needs to look clearly different from
  `great_white_shark`:
  - a broad, blunt, rounded snout with small eyes;
  - **seven gill slits** (count them: this is the gag);
  - **one** small dorsal fin set far back near the tail, and no front dorsal fin;
  - a long upper tail lobe;
  - a silvery grey to grey-brown back with **many small black spots**, and a pale belly.
- Closed mouth, a calm, neutral eye, no teeth showing and no smile.
- Anchor centre. About 800 x 260 (x -400..400, y -130..130). It's used at 0.24-0.3 in crowds of up to 12, and at 0.65-1.0
  as the hero. Keep a clean outer outline: it's also used as a silhouette with a red rim (s052, s142).

### `bronze_whaler` (s137-s142, s148-s149, s151-s154)
- **Done (illustrator, 2026-11-18):** `assets/previews/051-great-white-flees-orcas-assets.png`; x -372..380, y -128..128.
- Bronze whaler or copper shark (*Carcharhinus brachyurus*), side view facing right. It's a slender requiem shark:
  - a **bronze to olive-grey back with a coppery sheen** fading to a white belly;
  - a bluntly pointed snout and a round dark eye;
  - a tall first dorsal fin with a dusky tip, long curved pectoral fins and dusky fin tips;
  - five gill slits.
- It must not look like the great white (keep it slimmer, with no jagged countershading line). Closed mouth, no teeth.
- Anchor centre. About 760 x 260 (x -380..380, y -130..130). It's used at 0.08 (a map icon) up to 0.75 (the title card), and
  swarms of 3-5 at 0.4.

### `kelp_stalk` (s053-s057, s061-s069, s071)
- **Done (illustrator, 2026-11-18):** `assets/previews/051-great-white-flees-orcas-assets.png`; float bulb at (-12,-588); fronds stream right to x +90.
- One stand of False Bay sea-bamboo kelp (*Ecklonia maxima*): a rock holdfast at the bottom, a long, smooth, olive-brown
  hollow stipe rising nearly straight with a gentle bend, a gas float bulb near the top, and a tuft of long, flat,
  strap-like fronds streaming to one side. Use darker and lighter olive-brown shading.
- Anchor bottom-centre (the holdfast on the sea floor). About 180 x 720 (x -90..90, y -720..0). It's used at 0.8 on the
  item 3 water `#4f8a7f` (a green ground), so give it a dark outline and a brown, not green, body so it separates from the
  water.

---

## 1. The Exit

### `central_california_map` (s007-s009, s039, s124-s126)
- **Done (illustrator, 2026-11-18):** `assets/previews/051-great-white-flees-orcas-assets.png`; footprint as requested.
- A regional map in the `world_map` / `south_africa_map` style: flat green land, a dark outline, light-blue sea, white
  wave ticks, a black frame and no labels.
- **Projection:** lon -124.0..-121.2, lat 36.6..38.4, 400 px per degree, 1120 x 720, anchor centre at lon -122.6 /
  lat 37.5. So x = (lon + 122.6) x 400 and y = -(lat - 37.5) x 400.
- **Must show:**
  - the San Francisco peninsula and the Golden Gate opening into San Francisco Bay;
  - the coast running south past Half Moon Bay to Año Nuevo Point and the top of Monterey Bay (bottom right);
  - the Farallon Islands as a small clear rock group at about (-123.0, 37.70), local (-160, -80);
  - Año Nuevo Island as a small dot just off the point at about (-122.33, 37.11), local (+108, +156).
- The shotlist puts its own red and green pin circles on those two points, so don't draw pins.
- Placed at (760, 600) scale 0.85, so the frame lands at x 284..1236, y 294..906.

### `fire_alarm_pull` (s009)
- **Done (illustrator, 2026-11-18):** `assets/previews/051-great-white-flees-orcas-assets.png`; x -80..90, y -118..128.
- A classic red wall fire-alarm pull station: a red `#e0201b` box with a darker side, a white T-shaped pull handle in the
  middle (pulled down), and a small white stripe on top with no text. The pulled state reads "someone pulled the fire
  alarm".
- It's not the 040 `fire_alarm_kit`: that one is a gag with a first-aid kit inside.
- Anchor centre, about 180 x 260. Used at 0.9.

---

## 2. The Liver

### `great_white_beached` (s029-s035)
- **Done (illustrator, 2026-11-18):** `assets/previews/051-great-white-flees-orcas-assets.png`; x -410..410, y -194..12.
- A great white lying on its side on the sand: the same species look as `great_white_shark` (slate back, jagged
  countershading, white belly), lying flat with the tail slightly curled and the pectoral fin flat on the sand.
- **Clean outline, X eyes (cartoon dead), no marks, no open belly, no blood, no wounds.** A small sand-colour shadow
  under it.
- Facing right, anchor bottom-centre (the body resting on the sand at y = 0). About 800 x 200 (x -400..400, y -200..0). It's
  used at 0.42 in a field of five (each gets a liver icon with a red X beside it), and at 0.6-0.65 alone.

### `shark_liver_icon` (s030, s033-s034, s063)
- **Done (illustrator, 2026-11-18):** `assets/previews/051-great-white-flees-orcas-assets.png`; x -106..106, y -60..64.
- A flat cartoon icon of a shark liver: a long, smooth, **two-lobed** shape like a pair of tapering lobes joined at the
  top, in a pale creamy yellow-tan (`#e9c46a` with a lighter highlight, since shark liver is pale and oily), with a thick
  dark outline and one white shine.
- Diagram-like and food-free: **not** the dark red `liver_plate` liver, with no veins and no blood. It gets a red X laid
  over it.
- Anchor centre, about 220 x 140. Used at 0.3-0.6.

### `great_white_cutaway` (s036-s037, s041-s042)
- **Done (illustrator, 2026-11-18):** `assets/previews/051-great-white-flees-orcas-assets.png`; liver x -232..130, y -46..76; oil_drop at (-48,+40) lands on it.
- The `great_white_shark` outline with the same pose, anchor and footprint (x -428..405, y -165..160), drawn as a crude
  diagram cutaway:
  - the body is a pale cream `#f4f1dc` window with the outer outline intact, a slate back strip along the top and the
    eye kept;
  - inside, one huge **yellow `#ffe24a` two-lobed liver** fills the front-to-middle of the belly cavity, from about
    x -230 to +130 and y -20 to +120 (about a quarter of the body);
  - a thin dark outline round the liver, and **no other organs**.
- It's a textbook diagram, not anatomy: no flesh tones and no blood.
- Used at 1.05 on a cream card. The shotlist puts `oil_drop` at about local (-48, +40), so keep the liver's centre there.

### `oil_drop` (s042)
- **Done (illustrator, 2026-11-18):** `assets/previews/051-great-white-flees-orcas-assets.png`; footprint as requested.
- A fat cartoon droplet in golden amber oil `#e8a33a` with a honey highlight and a white shine, plus a thick dark outline.
  No face. Anchor centre, about 120 x 160. Used at 0.6 on top of the cutaway liver.

### `fuel_gauge_full` (s044)
- **Done (illustrator, 2026-11-18):** `assets/previews/051-great-white-flees-orcas-assets.png`; footprint as requested.
- Exactly the library `fuel_gauge` (same housing, face, E/F and pump icon) with the red needle pointing at **F**.
  Anchor centre, about 300 x 170. Used at 0.9. (The existing `fuel_gauge` with its low needle is the "after" shot, s045.)

### `costume_xray` (s048)
- **Done (illustrator, 2026-11-18):** `assets/previews/051-great-white-flees-orcas-assets.png`; clip top at y -284.
- An X-ray film card, portrait: a dark navy `#0b2447` panel with a thin light frame and a clip at the top. On it, a pale
  cyan `#9fe6ff` outline of Doug in the `shark_costume` (the costume's fin, tail and belly panel), and inside it Doug's
  crude stick skeleton: a round skull with the cap outline on top, a line spine, a few rib lines, arm and leg lines.
- A **dashed empty oval in the belly** where a liver would be. No text on the card: the shotlist adds a
  "LIVER: NOT FOUND." label under it.
- Anchor centre, about 460 x 540 (x -230..230, y -270..270). Used at 0.75.

---

## 3. The Cousins

### `shark_costume_sevengill` (s067-s069)
- **Done (illustrator, 2026-11-18):** `assets/previews/051-great-white-flees-orcas-assets.png`; gill lines x 14..79 (they run over the belly panel edge so all seven show).
- Doug's library `shark_costume` (same felt suit, fit, anchor = hips, bbox about x -196..+124, y -336..+70), with
  **seven** hand-drawn black marker gill lines instead of three (slightly wobbly, unevenly spaced, so they're clearly
  drawn on) and a scatter of small black marker dots on the grey felt for the spots.
- Everything else is unchanged: the dorsal fin, the felt teeth, the stitched belly panel and the tail. Head, face and cap
  stay fully visible.
- It's listed after Doug at the same x/y/scale, in `stand` and `float` poses, at 0.45-0.6.

---

## 5. The Seals

### `elephant_seal_bull` (s112-s113)
- **Done (illustrator, 2026-11-18):** `assets/previews/051-great-white-flees-orcas-assets.png`; faces left; x -446..462, y -406..0.
- An adult male northern elephant seal, hauled out side-on and facing left toward Doug (who lies to its left). It's
  enormous and heavy:
  - a grey-brown body;
  - a thick, wrinkled, rough pinkish-grey chest shield (texture lines only, **no scars that read as wounds**);
  - the big drooping **proboscis** nose hanging over its mouth;
  - its front body slightly reared, and small dark eyes.
- Menacing by bulk, not by teeth: the mouth is closed.
- Anchor bottom-centre (belly on the rock). About 900 x 420 (x -450..450, y -420..0). Used at 0.8, first as a silhouette
  (with a purple `#5e4670` glow, because it's on brown rock) and then in full colour.

### `elephant_seal_bull_flat` (s114-s115)
- **Done (illustrator, 2026-11-18):** `assets/previews/051-great-white-flees-orcas-assets.png`; faces left, head at the left end, under y -120 from x -450 to -165; x -474..462.
- The same bull, now lying fully flat and relaxed on its belly, head down on the rock, eyes shut and content, with its
  bulk spread wide. It's the "rolled onto him" image: the shotlist puts `seal_costume_flat` (drawn first) sticking out from under its
  left end (it ends at about local x -165, so keep the bull's left edge low and flat there) and `doug_cap` on a rock further left.
- Anchor bottom-centre. About 900 x 260 (x -450..450, y -260..0). Used at 0.8.

### `speed_camera` (s110)
- **Done (illustrator, 2026-11-18):** `assets/previews/051-great-white-flees-orcas-assets.png`; x -90..90, y -598..0.
- A roadside speed camera: a grey box camera housing with a dark lens window and a small flash panel on top of a tall grey
  pole, on a small concrete foot. No text and no brand. It must read as "speed camera" at 0.9 (a red X goes over it).
- Anchor bottom-centre (the foot on the road verge). About 200 x 600 (x -100..100, y -600..0).

---

## 6. The Year

### `autumn_leaf_icon` (s117-s118, s128, s130, s134)
- **Done (illustrator, 2026-11-18):** `assets/previews/051-great-white-flees-orcas-assets.png`; footprint as requested.
- A single orange-red autumn leaf (maple-like, five points) with a darker vein, a short stem and a thick outline. Season
  icon. Anchor centre, about 150 x 150. Used at 0.3-0.55, sometimes falling (several in one frame).

### `snowflake_icon` (s117-s118, s128, s131, s134)
- **Done (illustrator, 2026-11-18):** `assets/previews/051-great-white-flees-orcas-assets.png`; footprint as requested.
- A crude six-armed white snowflake with small side branches, a white fill, a light blue `#9fd0ee` outline and a dark
  outer edge so it reads on pale winter sky and on cream cards. Season icon. Anchor centre, about 150 x 150. Used at 0.3-0.55.
