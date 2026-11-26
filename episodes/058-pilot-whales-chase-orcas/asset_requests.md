# 058-pilot-whales-chase-orcas: asset requests (director, 2026-11-25)

The shotlist already places these by name, so please keep the **anchor, bounding box and key points** given here. The
generator (`episodes/058-pilot-whales-chase-orcas/build/gen_shotlist.py`, git-ignored scratch) puts things relative to them:
the cap on the grandmother's head, the cap on the flat costume, the calf against Sædís's flank, the tally marks in the board.
Everything **faces right** unless noted (the shotlist flips). House style: detailed tier, thick black outlines (5-6), flat
fills with interior shading. **Never cute**: no big eyes, no smiles, no pastel nursery look. No blood, no wounds, no bite marks.

**Art-director approval needed before keyframes** (decisions.md, CD 2026-11-25):
1. `who_ran_board` (the episode-only WHO RAN device; layout below).
2. `orca_costume` / `orca_costume_swim` / `orca_costume_flat` (new gear; must read as an orca at thumbnail size).
3. `pilot_whale_calf`: **CD condition: drawn plain** (dot eye, no cute proportions). The "NOT HERS" label stays in the shotlist
   (s133-s134) and is not baked into any asset.

**Layout notes that affect every drawing**
- The HUD now has two parts at top right: `DOUG DEATHS: N` (label at 1590,162) and the WHO RAN board under it (centre
  1590,322, scale 0.55, so about x 1425-1755, y 240-405). Surface scenes put the waterline at **y 520** (below the board), so
  fins and heads at the waterline never touch it.
- Pilot whales appear on surface blue `#3a9ad9`, twilight `#1b4f86`, midnight `#0b2447`, abyss `#050a1f`, cream maps
  `#f4f1dc` and white. Real pilot whales are black: please use a **charcoal `#2e3138` body with a lighter `#4a4f58` back
  highlight and pale grey markings** (the `false_killer_whale` family) so they still read on near-black water.
- Pilot whales vs orcas must be told apart at a glance: pilot whale = **round bulbous melon, no white eye patch, low broad
  hooked dorsal fin set well forward, long sickle flippers**. Orca = the library `orca`/`orca_female` (white eye patch, tall fin).

Reused from the library (no request): `orca`, `orca_female`, `orca_fin`, `pilot_whale_fin`, `loudspeaker`, `hydrophone`,
`dtag`, `research_ship`, `tour_boat`, `fishing_boat`, `rowboat`, `fishing_rod`, `inflatable_dinghy`, `squid_costume`,
`squid_costume_flat`, `doug_cap`, `sperm_whale`, `sperm_whale_top`, `gray_whale`, `dolphin`, `porpoise`,
`false_killer_whale`, `humboldt_squid`, `giant_squid`, `silver_fish`, `yellowfin_tuna`, `swordfish`, `tuna_head_hook`,
`sea_turtle`, `seagull`, `songbird`, `tree_branch`, `small_car`, `city_bus`, `stick_cyclist`, `shopping_trolley`,
`stick_man_plain`, `brown_dog_walking`, `sheep`, `bed`, `grey_wolf_sitting`, `front_door`, `placard`, `cinema_seat`,
`boot`, `bucket`, `banknote`, `dinner_plate`, `speedometer`, `music_note`, `ear_icon`, `heart_icon`, `clock`, `calendar`,
`chalkboard`, `dna_strand`, `journal_paper`, `magnifying_glass`, `binoculars`, `scientist`, `scientist_woman`, `diver`,
`water_splash_small`, `shark_fin`, maps (`fennoscandia_map`, `africa_map`, `north_america_map`, `hawaii_map`,
`south_america_map`), and the annotation set (`question_mark`, `exclamation_mark`, `warning_triangle`, `red_x`, `thermometer`).

---

## Episode HUD

### `who_ran_board` (every shot s002-s219) - needs art-director approval
**DONE** (illustrator, 2026-11-26): preview `assets/previews/058-pilot-whales-chase-orcas-assets.png`. Awaiting art-director approval.
The WHO RAN scoreboard (staging only, never read aloud). Same construction as `lion_hyena_scoreboard` (brown wooden frame,
dark green `#2f5a3a` board, chalk ledge) but **small and wide, built to be read at scale 0.55**: local **x -300..300,
y -150..150**, centre anchor. Chalk-white `#f4f4ec` hand lettering, bold and chunky (it renders at about half size):
- `WHO RAN` centred (0,-108), about 40 units tall.
- `PILOT WHALES` centred (-150,-58) and `EVERYONE ELSE` centred (+150,-58), about 32-36 units (shrink to fit each half).
- Chalk underline at y -34 (x -280..280), divider at x = 0 from y -80 to y +130.
- **Tally zones left empty** (the shotlist draws them): left x -270..-20, y -20..+125 (chalk ticks, 1-7), right
  x +20..+270, same y (a red `ORCAS` is written there at the boss, s216 onward, centred about local (+150,+58)).
No crack, no paw prints, no "BEAR/MOOSE" look-alike details. Must stay legible on top of white, sky, sea and black frames.

---

## Pilot whales (charcoal family, see layout notes)

### `pilot_whale` (91 shots, s002-s221: the episode's main creature)
**DONE** (illustrator, 2026-11-26): preview `assets/previews/058-pilot-whales-chase-orcas-assets.png`.
Adult long-finned pilot whale, side view facing right. Long, robust charcoal body; **big round bulbous melon** overhanging a
very short mouth (no beak); small plain dark eye at about (+235,-15); **low, broad-based, strongly hooked (falcate) dorsal fin
set forward of mid-body**, tip at about (+30,-170); **long, narrow sickle-shaped pectoral flipper** (about a fifth of body
length) swept back below the front third; pale grey anchor-shaped throat patch and a faint grey saddle behind the fin; thick
tail stock and flukes at the left. Closed mouth, no teeth. **Anchor centre; bbox x -330..+330, y -170..+110.** Melon top at
about (+250,-80). Used at scale 0.18-0.75, flipped, rotated up to 55 degrees (diving), in pods of 3-11 overlapping copies,
and as a red-rimmed silhouette (`silhouette: true`, so the outline must be a clean closed shape).

### `pilot_whale_front` (s016, s019, s030, s058, s167, s204, s205, s215, s216, s222)
**DONE** (illustrator, 2026-11-26): preview `assets/previews/058-pilot-whales-chase-orcas-assets.png`.
The "wall of round black heads": the same whale seen head-on, swimming at the viewer. **A big round melon dome** filling the
top two thirds, small plain eyes far apart at about (-80,-10) and (+80,-10), short closed mouth line, the two long flippers
angled out at the sides and the dorsal fin tip just showing behind the top. Charcoal with grey highlight on the dome. Calm,
blank, not angry, no teeth. **Anchor centre; bbox x -150..+150, y -130..+130.** Used at 0.22-0.4 in crowds of 6-14.

### `pilot_whale_head` (s079-s081, beside Doug's boat)
**DONE** (illustrator, 2026-11-26): preview `assets/previews/058-pilot-whales-chase-orcas-assets.png`.
A pilot whale's round head surfacing beside a boat, facing right, side-on: the melon and the top of the head out of the water,
plain eye at about (+60,-70) just above the waterline, a white ripple around it. **Anchor bottom-centre on the waterline; bbox
x -120..+120, y -150..+12.** It "watches" Doug: deadpan, mouth closed.

### `pilot_whale_calf` (18 shots, s131-s168) - **CD condition: plain**
**DONE** (illustrator, 2026-11-26): preview `assets/previews/058-pilot-whales-chase-orcas-assets.png`. Drawn plain (dot eye, no sparkle, no smile).
Newborn long-finned pilot whale, side view facing right: shorter and stubbier than the adult, **slightly paler grey-black
`#4a4f58`**, faint pale fetal-fold bands across the flank, a small floppy dorsal fin, small round melon. **Plain dot eye, no
highlight sparkle, no big head, no smile, no cute proportions** (documentary, like `sperm_whale_calf`). **Anchor centre; bbox
x -160..+160, y -70..+60.** Shown at about 0.4-0.9, tucked against `orca_female`'s lower flank (the shotlist places it at
orca x -60, y +105 for an orca at 0.75), and alone with Doug.

### `pilot_whale_old` (s168, s175, s179, s181-s184: "the grandmother")
**DONE** (illustrator, 2026-11-26): preview `assets/previews/058-pilot-whales-chase-orcas-assets.png`.
A large old female pilot whale, same pose, bbox and anchor as `pilot_whale` (centre, x -330..+330, y -170..+110), so they swap
1:1. Differences: a **pale grey patch on the melon and around the eye**, a few faint pale scratch lines on the flank, a small
nick in the dorsal fin, slightly heavier body. Not wrinkled-cute, no eyelashes. **Head top at (+250,-80)**: at s183-s184
`doug_cap` sits there (the shotlist flips her to face left and puts the cap at her x - 250 x scale, y - 80 x scale - 18).

---

## Orca costume (Doug gear; art-director approval)

### `orca_costume` (s003, s004, s029, s030, s181, s182, s215, s216, s221; thumbnail)
**DONE** (illustrator, 2026-11-26): preview `assets/previews/058-pilot-whales-chase-orcas-assets.png`. Awaiting art-director approval.
Doug's cheap homemade orca suit for **upright poses** (float, stand, wave), worn over Doug: **anchor = Doug's hips, listed after
Doug at the same x/y/scale** (flip with him). Black felt suit over the torso and legs with **a big white felt eye-patch oval on
each side of the hood**, white belly panel, **tall straight black felt dorsal fin rising behind his head** (tip about
(-110,-330), clear of the head and cap), two paddle flipper mitts on the arms, felt flukes behind the legs, a **visible front
zip** with pull tab (he "zips it back up" at s215). The hood frames the face: **face and red cap fully visible** (cap on top,
as in the brief). Must read as an orca at thumbnail size (about 60 px tall). Bbox about x -200..+160, y -330..+80. Deadpan,
adult-coded, no cartoon smile on the suit.

### `orca_costume_swim` (s214)
**DONE** (illustrator, 2026-11-26): preview `assets/previews/058-pilot-whales-chase-orcas-assets.png`. Awaiting art-director approval.
The same suit fitted to Doug's `swim1`/`swim2` loop (torso leaned forward, head up): fin standing up from the back, flukes
trailing behind the legs. Anchor = Doug's hips, list after Doug at the same x/y/scale. He wears `sweat` gear too.

### `orca_costume_flat` (closing s217-s219)
**DONE** (illustrator, 2026-11-26): preview `assets/previews/058-pilot-whales-chase-orcas-assets.png`. Awaiting art-director approval.
The empty orca suit floating flat on the surface after the boss (no Doug inside): crumpled black felt lying horizontally on the
waterline, white eye-patch and belly panel showing, dorsal fin flopped over, flukes limp at the left, zip half open. The felt
"eye" is drawn as an X. No Doug, no bite marks, no tears. **Anchor centre on the waterline; bbox x -230..+230, y -60..+40**;
`doug_cap` is placed on its top at local (0,-60) by the shotlist.

---

## Other creatures

### `oceanic_whitetip` (17 shots, s082-s105)
**DONE** (illustrator, 2026-11-26): preview `assets/previews/058-pilot-whales-chase-orcas-assets.png`.
Oceanic whitetip shark, side view facing right: bronze-grey `#8a7f70` back, white belly, **very long, broad, rounded
paddle-like pectoral fins** and a **tall rounded first dorsal fin**, both with **mottled white tips** (also on the tail lobes),
blunt rounded snout, small round eye, closed mouth (no teeth showing). **Anchor centre; bbox x -380..+380, y -200..+150.**
Used at 0.22-0.95 and as a red-rimmed silhouette (s082).

### `beluga` (s013, s014)
**DONE** (illustrator, 2026-11-26): preview `assets/previews/058-pilot-whales-chase-orcas-assets.png`.
Beluga whale, side view facing right: all-white body with pale grey shading, small rounded melon, short beak, no dorsal fin
(low ridge), small paddle flippers. Plain eye, no smile. **Anchor centre; bbox x -260..+260, y -100..+100.**

### `beaked_whale` (s014)
**DONE** (illustrator, 2026-11-26): preview `assets/previews/058-pilot-whales-chase-orcas-assets.png`.
Cuvier's beaked whale, side view facing right: long spindle body, grey-brown `#7a7f88` with paler head and faint pale scratch
lines, short beak, small dorsal fin far back. Plain eye. **Anchor centre; bbox x -280..+280, y -85..+85.**

### `owl` (s027, s028, s211, s212)
**DONE** (illustrator, 2026-11-26): preview `assets/previews/058-pilot-whales-chase-orcas-assets.png`.
A tawny owl perched facing the viewer (3/4), brown mottled plumage, round facial disc, dark eyes, small hooked beak, talons
gripping (it sits on the library `tree_branch`). Grumpy-plain, not cute. **Anchor centre; bbox x -110..+110, y -150..+150**
(feet at y +150). Shown with 2-4 library `songbird`s around it (mobbing); also small (0.42) inside a thought bubble.

### `cheetah` (s048)
**DONE** (illustrator, 2026-11-26): preview `assets/previews/058-pilot-whales-chase-orcas-assets.png`.
Cheetah in full sprint, side view facing right, legs fully stretched: tan coat with black spots, black tear lines on the face,
long tail. **Anchor centre; bbox x -280..+280, y -120..+120.** Shown at 0.6 next to a pilot whale ("the cheetahs of the deep sea").

---

## Places and props

### `iceland_map` (s129, s132, s147, s185, s188, s189)
**DONE** (illustrator, 2026-11-26): preview `assets/previews/058-pilot-whales-chase-orcas-assets.png`.
Iceland in the `world_map`/`fennoscandia_map` style: flat green land `#6cbf5a` with a white ice-cap patch or two, dark green
coast, light-blue `#bfe6ff` sea with white wave ticks, black frame, no labels. **Projection x = (lon + 19) x 60,
y = -(lat - 65) x 142; frame lon 25 W..13 W, lat 63 N..67 N (x -360..+360, y -284..+284), anchor centre.** Include the
**Westman Islands** (check point lon -20.3, lat 63.43 -> about (-78,+223)) and the **Snæfellsnes peninsula with Breiðafjörður
to its north** (red dot in the bay at lon -23, lat 65.2 -> about (-240,-28)). Shown at scale 1.25 centred (720, 520).

### `fisherman_hat` (s078-s081)
**DONE** (illustrator, 2026-11-26): preview `assets/previews/058-pilot-whales-chase-orcas-assets.png`.
Yellow `#ffd21a` oilskin sou'wester (long back brim, short front brim, chin strap), worn **perched on Doug's cap** like
`sun_hat`: anchor = Doug's hips at scale 1, **fitted to the `sit` pose (which drops the head 70 units): rim at about y -224** so
the red cap dome and brim stay visible below. List after Doug at the same x/y/scale.

### `longline_hook` (s075, s078, s079) and `longline_hook_baited` (s062-s077)
**DONE** (illustrator, 2026-11-26): preview `assets/previews/058-pilot-whales-chase-orcas-assets.png`. (`longline_hook` and `longline_hook_baited`.)
A grey steel longline J hook on its short branch line. `longline_hook`: **empty** (it is reeled in empty three times).
`longline_hook_baited`: the same hook with a small silver baitfish threaded on it. **Anchor = the tie point at the top of the
hook eye (0,0); hook hangs down to about y +110; bbox x -30..+30 (baited: x -40..+60), y 0..+130.** Must match the existing
`tuna_head_hook` hook shape. No hooked whales anywhere (brief: no entanglement imagery).

### `pub_front` (s202)
**DONE** (illustrator, 2026-11-26): preview `assets/previews/058-pilot-whales-chase-orcas-assets.png`.
A crude pub frontage (concept beat): brick or dark-wood front, a hanging pub sign with a blank board, big front door wide open,
two windows. No logos, no readable text, no drinks visible. **Anchor bottom-centre; bbox x -350..+350, y -520..0**; the open
door is about x -60..+60. Library stick men run out of it.

### `dive_mask` (s045)
**DONE** (illustrator, 2026-11-26): preview `assets/previews/058-pilot-whales-chase-orcas-assets.png`.
A dive mask pushed up as if on a forehead: oval blue `#3a7ad9` frame, pale glass, black strap. **Anchor centre; bbox x -75..+75,
y -40..+40.** It sits on a pilot whale's melon (the joke: "holding its breath the whole time").
