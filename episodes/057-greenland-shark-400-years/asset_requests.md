# 057-greenland-shark-400-years: asset requests (director, 2026-11-24)

The shotlist already places these by name, so please keep the **anchor, bounding box and key points** given here.
The generator (`episodes/057-greenland-shark-400-years/build/gen_shotlist.py`, git-ignored scratch) places things relative to
them: the copepod on the eye point, the cap on the upturned cake, Doug's suit on the `on_back` rig. Everything **faces right**
unless noted (the shotlist flips). House style: detailed tier, thick black outlines (5-6), flat fills with interior shading.
**Never cute** (pup, cake, cards are deadpan office-party, not a kids' party): no big eyes, no smiles, no pastel nursery look.
No blood, no wounds, no eye damage, no stomach contents beyond black silhouettes.

**Art-director approval needed before keyframes** (CD decisions.md 2026-11-24):
1. `shark_age_icon` + the SHARK AGE HUD label (episode-only device, layout below).
2. `harp_seal_costume_prone`: must read clearly differently from 051's grey `seal_costume` / `seal_costume_prone`.

**Dropped:** the paper party hat at item 7 (facts.md director note). The Teenager uses the card only; no hat asset is requested
and `paper_crown` is not used anywhere in the episode.

Reused from the library (no request): `greenland_shark` (eye at local (380,-36): the copepod overlays there), `ringed_seal`,
`reindeer`, `horse`, `polar_bear` (silhouettes on the FOUND INSIDE card), `whale_carcass`, `whaleboat`, `fishing_boat`,
`baited_camera_lander`, `shark_fin`, `arctic_map`, `usa_map`, `yellow_submarine` (Doug's crude sub, item 8), `torch`, `tape_measure`,
`ruler`, `clipboard`, `journal_paper`, `newspaper_blank`, `calendar`, `calendar_page_flying`, `page_a_day_calendar`, `clock`,
`placard` (WELCOME), `picnic_blanket`, `picnic_basket`, `sandwich`, `dinner_plate`, `kitchen_counter`, `water_glass_empty`,
`shipping_crate`, `fridge`, `dna_strand`, `sticking_plaster`, `heart_monitor`, `magnifying_glass`, `speed_camera`, `finish_banner`,
`freshwater_snail`, `fingertip`, `small_car`, `stick_man_plain`, `scientist`, `signboard`, `binoculars`, `eye_icon`, `silver_fish`,
`water_splash`, `crt_tv` (LIVE feed), `doug_cap`, plus the annotation set (`question_mark`, `exclamation_mark`, `warning_triangle`,
`red_x`, `thermometer`).

Palette notes: water under the sea ice is always surface `#3a9ad9` (art bible); the sky steps down one shade per item
(`#cfe9ff` to night `#1b2f5a` at the boss), so creatures must read on `#3a9ad9`, on cream `#f4f1dc` and on midnight `#0b2447`.
Greenland shark grey-brown is the library `#6e6a64`; keep every new shark drawing in that family.

---

## Episode HUD

### `shark_age_icon` (HUD icon, every shot s002-s206) - needs art-director approval
Tiny crude birthday card: a folded cream `#fff6dc` card standing open in 3/4 view, black outline 6, one red-and-white striped candle
with a small yellow flame on top, and a tiny grey `#6e6a64` shark fin doodled on the front. Must read at **scale 0.16 (about 32 px)**.
Anchor centre, bbox about x -100..100, y -100..100. It sits left of the size-28 `SHARK AGE: <n>` label at (1590,238) under the death
counter (icon right edge about 30 px left of the label box, moved by the generator as the value grows). Values: `?`, `0`, `~10`,
`~50`, `~100`, `~100`, `~150`, `~250`, then `~392 (±120)` red-on-pink `#ffd2cc`/`#e0201b` from s187 to the end, plus a second
red label `+ 1 MIN` under it on the LIVE-feed closing (s205-s206). Staging only, never read aloud. No "THE MENU"/stopwatch look.

---

## Greenland shark family (same palette as library `greenland_shark`: grey-brown `#6e6a64`, darker back, paler belly, fine dark spots)

### `greenland_shark_head` (close-up, item 1)
The shark's head and front body in close-up, facing right: blunt rounded snout, underslung closed mouth line (no teeth showing),
small gill slits, the skin texture and spots at large size. **The eye is a small plain dot** (pale grey `#c9d0d2` ring, black pupil,
no damage, no scarring shown). **Anchor = eye centre (0,0)**. Bbox about x -900..+300, y -320..+300; the body continues off to the
left and **ends in a straight cut at x -900** that is always placed off-frame (at x 1180, scale 1.15 it starts at x -55). No copepod
baked in (it is overlaid as `eye_copepod` at the anchor).
Shots: s006, s008, s010, s011, s016, s020 (at (1180-1300, 560), scale 1.15).

### `greenland_shark_face` (head-on, item 1 death)
The same shark seen head-on, turned toward the viewer: wide flat blunt head filling the frame, small dot eyes far apart at about
(-230,-60) and (+230,-60), closed underslung mouth line, pectoral fins just visible at the sides. Slow and menacing, **no teeth, no
open mouth**. Anchor centre, about 760x520. Shot: s021 (960, 560, scale 1.1; `eye_copepod` overlaid at its left eye (-230,-60)).

### `eye_copepod` (the parasite, item 1 and on every close shark)
*Ommatokoita elongata* as a pale cartoon streamer: a small cream-white `#f3ecd6` body with two long thin trailing egg-sac strings
(paler `#fbf7ea`, black outline 3), hanging down and slightly back from the attachment point. Soft, almost ribbon-like; **no eye
wound, no red, no anchor hooks shown**. **Anchor = the attachment point (0,0) at its top**; bbox about x -40..+30, y 0..+170.
Used at scale ~0.25-0.6 on full sharks (overlaid at the library shark's eye (380,-36) x scale) and 1.0 on the close-up, and at
1.9 alone on a cream diagram card (s007), so the body needs simple segment lines that read large too.
Shots: s002, s005-s008, s010, s011, s016-s018, s021, s022, s075, s185-s188.

### `eye_copepod_wave`
Exactly `eye_copepod` (same anchor and bbox) with one tiny cartoon "arm" (a short pale leg stroke) raised as if waving back at Doug.
Deadpan, not cute: no face. Shot: s020 ("Doug has found the only thing down here that waves back.").

### `greenland_shark_pup` (item 2)
A near-term pup (~37 cm): same species shape as `greenland_shark` but shorter and slimmer, proportionally slightly bigger head,
same grey-brown with fewer spots, **plain small dot eyes** (no big eyes, no smile), yolk-free. Facing right, anchor centre,
about 400x130. Must read at 0.13 (ten tiny pups in a row inside the mother on a cream card, s027) and at 0.45-0.9.
Shots: s024, s027, s028, s033, s039, s040, s042-s045.

---

## Seals (item 4)

### `harp_seal`
Adult harp seal swimming, facing right: silver-grey `#c9ccd0` body, **black face mask** and the bold black **harp/horseshoe
saddle mark** on the back and flanks, pale belly, dark eye, short whiskers, fore flippers tucked, hind flippers together. Adult,
not the white pup. Anchor centre, about 420x150. Also used as a black silhouette (glow_r 0) inside a dotted stomach outline on a
cream card (s079, s080), so the outer outline must be clean.
Shots: s079, s080, s081, s083, s090.

### `harp_seal_sleeping`
The same harp seal asleep in the water "bottling": body vertical, head up, eyes closed (two short curved lines), relaxed flippers.
Anchor centre, about 160x420. Shots: s084 (under the ice), s087 (beside the floe edge).

### `harp_seal_costume_prone` (Doug's suit) - needs art-director approval (must differ from 051)
Doug's homemade **harp seal** suit worn lying flat, built like the library `seal_costume_prone` so it slots onto the `on_back` rig:
place it **after Doug at x = Doug x + 30 x scale, same y and scale, `rotate: -90`** (drawing stored pre-rotated like
`seal_costume_prone`). Head end at the left, tail flippers past his feet at the right; Doug's head, sleepy face and red cap stay fully
visible. What makes it read as a different suit from 051's plain grey `#8a8f96` speckled sack: **pale silver `#d9dcdf` felt, a big
black felt harp/horseshoe saddle patch sewn on the back** (visible stitching), a black felt face-mask hood band round his head,
and a pillow-soft rolled shape. Covers about 540x170 at scale 1 (Doug-frame x -314..292, y -96..72).
Shots: s087, s088 (Doug at (860, 388), scale 0.6, asleep at the edge of an ice floe). The death (s089) shows only the tipped floe,
a splash and the cap, so no flat/empty variant is needed.

---

## Birthday cake (opening and boss)

### `birthday_cake_candles`
A tall, slightly lopsided two-tier office birthday cake, **crowded with far too many thin lit candles** (a dense forest of about
40-60 striped candles, flames yellow `#ffe24a` with white cores), white icing with a pale blue `#bfe6ff` drip edge, on a plain
round board. Deadpan, not a kids' cake: no sprinkles, no smiley, no "Happy Birthday" text. **Anchor bottom-centre** (board on y=0),
about 360x420 (flames top at y about -420). Used at 0.42-0.5 next to Doug at the ice hole (crouch pose, his front hand at the cake's
left side) and at 1.3 alone on a cream card. Shots: s003, s004, s197, s198, s202, s203.

### `birthday_cake_upside_down`
The same cake fallen upside down on the seabed after the boss death: tiers squashed flat on top of each other, board on top,
icing smeared out at the base, a few snuffed candles (no flames, a thin grey smoke wisp at most) sticking out sideways.
**Anchor bottom-centre**, about 360x220; **flat top (the board) at local y -200**, where the generator sets `doug_cap`
(LIVE-feed closing, scale 0.32 inside the `crt_tv` screen, dark seabed). Shots: s205, s206.

---

## Iceland and fisheries (items 6, 7, 9)

### `shark_meat_slab`
A plain slab of pale grey-white `#d8d6cf` shark meat with a slightly darker grey `#b8b4aa` skin edge along the top, faint grain
lines, flat fills. **Not red, not bloody, no bone.** Anchor centre, about 420x200. Sits on `dinner_plate` and on its own under a
yellow warning triangle. Shots: s115-s120, s122.

### `hakarl_drying_shed`
Icelandic hákarl drying shed: a small open-sided wooden shed of weathered grey-brown slats `#8a7a62` with wide gaps, a pitched
corrugated roof, and **rows of pale cream-yellow `#e8dcb0` meat strips hanging** from poles inside (visible between the slats).
Anchor bottom-centre (ground y=0), about 520x440. Shots: s123, s124, s135, s136.

### `hakarl_cube`
One small pale cream-yellow cube of hákarl speared on a plain wooden toothpick. **Anchor = the toothpick's end (the grip)**,
toothpick pointing up-left from the grip; about 120x160. Used at 0.4-0.6 in Doug's hand at a counter. Shots: s124, s137.

### `trawl_net`
A crude trawl net: a long cone of black mesh (cross-hatched lines) with a rope frame mouth at the right and the closed cod end at
the left, two tow lines leaving the mouth up and right. Empty (the shotlist adds the shark and `silver_fish` on top). Anchor
centre, about 640x300. Shots: s132, s133, s151, s154, s200.
