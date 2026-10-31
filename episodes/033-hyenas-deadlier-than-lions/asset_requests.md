# 033-hyenas-deadlier-than-lions: asset requests (director)

House style: detailed tier for creatures, places and props (dark outlines 4-6, flat fills, interior shading); crude tier (Doug's line, `auto_ink`) for humans. Facing right unless noted. Sizes are local units at scale 1, and **the shotlist is laid out against these anchors, extents and key points**, so please keep them (a stand-in layout preview was checked against them). Listed in priority order: the episode devices and the hyena/lion family first (on screen most), then places and maps, then one-shot props.

CD and brief rules (decisions.md 2026-10-31, brief section 7) that apply to every drawing:
- **Every hyena keeps the heavy, sloped `spotted_hyena.json` build** (high shoulders, low rump, rounded ears, dark muzzle, spots). Never dog- or rat-like at feed size. **Giggling = mouth open, never a smile** (no upturned mouth corners). **No cubs anywhere**, no cute eyes.
- **Carcasses are outlines only.** No body is ever drawn being eaten, no blood, no ribs, no wounds. Lions never attack anything on screen.
- **032 separation:** no den, no bone piles, no fossils, no time machine.
- **Harar:** the hyena man is drawn respectfully and simply, never as the joke. The Sleepers drawings are quiet and plain (no hyena in the village frames, no injury).
- No Lion King look: lions are real big cats with hard stares, not cartoon heroes. No named-character styling.

Night palette for this episode (so mid-tone fills read): sky `#4a3f5e` (8 PM) → `#3b3550` → `#1b2f5a` → `#142446` → `#101c38` → city `#0b1020` → `#0c1424` → pre-dawn grey `#4a4f5e`; grounds `#2b3d33`-ish. Creatures need **mid-tone fills** (the library hyena's sandy-grey is right), not near-black.

Reused from the library (no request): `acacia_tree`, `africa_map`, `binoculars`, `calendar`, `city_skyline_night`, `clipboard`, `dinner_plate`, `doug_cap`, `eiffel_tower`, `exclamation_mark`, `field_guide`, `finish_banner`, `house`, `leopard`, `narrator_hand`, `pachycrocuta` (032 callback, alive, in a thought bubble only), `paw_print_icon`, `platform_scale`, `pork_chop`, `question_mark`, `record_book_open`, `red_x`, `referee_shirt`, `rubbish_bag`, `rubbish_bin`, `savanna_bush`, `school_bus`, `scientist`, `signboard`, `soccer_ball`, `speedometer`, `spotted_hyena` (the one with the bone: The Bite only), `stew_bowl`, `stick_sprinter`, `tall_savanna_tree`, `tent`, `thermometer`, `torch`, `wait_stopwatch` (as a plain stopwatch prop, not THE WAIT meter), `warning_triangle`, `water_splash`. **`hyena_cub` is not used.**

---

## Episode devices

### `lion_hyena_scoreboard`
**The LION | HYENA board (every shot: HUD icon; big on the tick beats).** A restyle of 024's `bear_moose_scoreboard` so it doesn't read as a re-skin.
- Look: same construction as `bear_moose_scoreboard` (brown wooden frame, dark green `#2f5a3a` board, ledge with chalk and eraser) but **cracked**: one jagged dark crack line `#1a2a1e` with a lighter chalky edge running from the top-right corner down-left about 180 units (keep it inside x +200..+390, y -240..-120, so it never enters a tally zone). Chalk-white `#f4f4ec` hand-lettered headers **LION** centred (-165,-150) and **HYENA** centred (+165,-150), a small chalk paw print beside each header (left of LION at about (-290,-150), right of HYENA at about (+290,-150)), a chalk underline at y -100, a chalk divider at x=0 (y -190..160).
- Anchor / size: centre, x -390..390, y -240..236 (identical to `bear_moose_scoreboard`).
- **Tally zones must stay empty:** LION ticks are drawn by the shotlist at local x -280, -254, -228 ... (26 apart), HYENA ticks at x +60, +86, +112 ... up to +268 (9 ticks), each from y -50 to +30, width 10 at scale 0.9. Nothing else in x -300..-30 / +40..+300, y -70..+50.
- Must still read as a chalkboard at scale 0.07 (HUD icon at (1408, 238), left of the `LION n | HYENA n` label): keep the frame thick and the board dark.
- Shots: s002-s199 (HUD, every non-sober shot); big at s019-s020, s062, s110, s186-s187.

### `field_guide_lion_hyena`
**Doug's field guide, two-page spread: LION left, SPOTTED HYENA right.** A variant of `field_guide_open` (same book, same 560x360 size, spine x=0, coffee ring, red ribbon, dog-ears).
- Left page: **LION** printed bold `#2b2b2b` centred (-140,-140); **FRIEND?** at (-190,-80) with an empty 44x44 tick box at (-75,-80). The rest of the left page stays blank (ruled lines fine): it stays empty all episode (the joke at the end).
- Right page: **SPOTTED HYENA** printed bold centred (+140,-140) (two words, ~26 units, fit inside x +20..+265); **FRIEND?** at (+90,-80) with an empty 44x44 tick box at (+205,-80).
- **Keep clear on the right page:** the MAYBE zone around (+150,-20) (~200x50) and the NO stamp grid x +20..+280, y +10..+140 (the shotlist stamps up to 7 red "NO"s at (55,40) (120,40) (185,40) (250,40) (55,105) (120,105) (185,105), 52 units each). The coffee ring goes on the **left** page, low.
- Anchor: centre. Used at scale 0.55 at (330, 880) on outcome beats, 1.3-1.4 for close-ups (s021, s197).
- Shots: s021, s026-s027, s048-s049, s069, s090-s091, s116, s132, s155, s171, s197.

### `thief_sign`
**Cardboard "THIEF" sign hung round an animal's neck (The Lie).**
- Look: a crude torn-cardboard sign `#c9a46a` with a darker edge, block capitals **THIEF** in black marker, two string ends meeting at the cord apex.
- Anchor: **the cord apex (0,0)**; card x -110..110, y +40..+150; the strings run from the apex to the card's top corners. ~220x150.
- Placement: hung on `spotted_hyena_plain` (s005-s006) then on `lioness` (s018), apex at the animal's neck.
- Shots: s005-s006, s018.

## Hyenas (all the `spotted_hyena` build, sandy-grey coat with dark brown spots, mid-tone)

### `spotted_hyena_plain`
**The workhorse hyena (94 uses).** Exactly the library `spotted_hyena` **without the bone**: mouth closed, dark muzzle, heavy brow, mean eye, round ears, sloping back. Anchor bottom-centre (feet on y=0), ~610x330 (x -262..+352, y -325..0), same as `spotted_hyena`; neck point about (+200,-230). Used flipped and as a black silhouette (`silhouette: true`, red `rim`), so keep the outline clean (legs separated, ears and tail clear).
- Shots: s005-s007, s010-s011, s015, s018, s025, s027, s033-s035, s042, s044-s047, s050, s068, s089, s108-s109, s112-s113, s121-s122, s124-s125, s128, s134, s137, s139-s140, s143-s146, s151-s154, s161, s163-s164, s166, s168, s178-s179, s189, s193-s196.

### `spotted_hyena_running`
Same build in a long loping gallop: front legs reaching forward, hind legs pushing back, back still sloped, head forward and low, tail out. Anchor bottom-centre (lowest hoof on y=0), ~640x300. Used at 0.26-0.75, flipped too.
- Shots: s013-s015, s051, s053, s058, s065, s081, s104, s162.

### `spotted_hyena_giggle`
Standing, head raised a little, **jaws open** (dark `#7a0d0d` mouth, a few teeth visible), ears slightly back, eye squinting. Tense, not happy: **no smile, no upturned corners.** Anchor bottom-centre, ~610x340; **mouth at about (+300,-260)** (the shotlist draws jagged sound lines from there). Also used as a silhouette with a red rim (s071).
- Shots: s028, s071-s076, s080, s082-s083, s087-s089.

### `spotted_hyena_whoop`
The whoop pose: head held low near the ground, neck stretched forward, mouth open in a long call. Anchor bottom-centre, ~640x280, **mouth at about (+330,-60)** (rings spread from there).
- Shots: s084, s093-s094.

### `spotted_hyena_sitting`
Sitting on its haunches, front legs straight, head up watching, mouth closed. Anchor bottom-centre, ~360x380 (x -180..180, y -380..0). Used flipped (facing left) at 0.46-0.6.
- Shots: s002, s017, s041, s149-s150.

### `spotted_hyena_cap`
Trotting calmly to the right with **Doug's red cap** held in its front teeth (cap exactly like `doug_cap`, `#e0201b`, brim forward, about 90 units wide at this scale). Mouth only around the cap, no damage to it. Anchor bottom-centre, ~640x330. Closing image.
- Shots: s198-s199.

### `spotted_hyena_diving`
A hyena going under at a night water hole: only the **hindquarters, hind legs and short tufted tail** above the surface, tilted forward ~40 degrees, with a ring of ripples at the waterline. No head visible. Anchor **(0,0) = centre of the ripple ring on the waterline**; the body sticks up to about y -260, ~320 wide. Water colour around it `#16304a`.
- Shots: s129, s131.

### `hyena_head_icon`
A small flat side-view hyena head (facing right): rounded ear, dark muzzle, two or three spots, small eye, thick outline. **Must read at scale 0.35-0.45 (about 45 px)** in crowds (130 of them), bus windows and the rank pyramid. Centre anchor, 120x100.
- Shots: s016, s057, s078, s085, s098-s103, s119, s176, s180, s185.

### `hyena_hockey` / `hyena_goalie`
Two gag drawings for the six-to-one hockey line: `spotted_hyena_plain` standing on the ice wearing a simple ice-hockey helmet (one colour, `#1f5a94`) with a hockey stick held crosswise in its jaws; `hyena_goalie` the same with a white goalie mask and two chunky blocker pads on its front legs. Anchor bottom-centre, ~560x380 each. Funny, not cute.
- Shots: s177.

## Lions (modern African lion; a real big cat, hard stare, no cartoon hero look)

### `lioness`
Adult lioness standing, side view facing right: tawny `#c9964a` coat, paler belly, heavy shoulders, dark tail tuft, small amber eye under a heavy brow. Anchor bottom-centre, 700x380 (x -350..350, y -380..0), neck point about (+230,-250). `cave_lion.json` may be adapted (warmer colour, no stripes). Used as a silhouette too.
- Shots: s003, s010-s011, s018, s064, s111, s159, s166-s167, s173-s175, s177-s178, s188, s190-s194, s198.

### `lioness_crouched`
Lying sphinx-like on the ground, front paws forward, **head up and alert** (looking over its shoulder is fine), facing right. Drawn so a `carcass_outline` placed just behind/beside it reads as "her kill" without any eating. Anchor bottom-centre, ~680x260.
- Shots: s002, s015, s017, s174-s175, s178, s190-s194, s198.

### `lioness_walking`
Walking mid-stride, facing right (flipped to walk away from Doug): relaxed, head level. Anchor bottom-centre, 700x380. Used as a silhouette too (s172).
- Shots: s015, s041, s172, s195.

### `lioness_sitting`
Sitting upright on her haunches, front legs straight, calm stare. Anchor bottom-centre, ~380x420 (x -190..190, y -420..0). Used tiny inside thought bubbles too (0.25).
- Shots: s043, s052-s053, s067, s107-s108, s201.

### `lioness_running`
A short charging run, body stretched, facing right (she is chasing a hyena off a kill; no contact). Anchor bottom-centre, ~760x330.
- Shots: s081.

### `lion_male`
Adult male lion standing, facing right: big **dark brown-black mane** `#3a2418` with a tawny face ring, heavy body, tail tuft, calm, imposing stare. Anchor bottom-centre, ~780x440. "EXCEPT HIM."
- Shots: s107-s108, s179.

### `lion_head_icon`
Small flat side-view **lioness** head icon (no mane), facing right, tawny with dark nose and ear backs, thick outline; reads at 0.8-1.4 (~110-170 px) next to `hyena_head_icon`. Centre anchor, 140x120.
- Shots: s016, s054-s056, s061, s176, s180, s183, s185.

## Other animals

### `carcass_outline`
**The "kill" shape, outline only (brief gore rule).** A wildebeest-sized animal lying on its side, drawn as a **pale flat shape with no interior detail**: fill `#d9cfb8`, outline `#6b6358` width 4, legs tucked, a hint of one curved horn at the head end. No eye, no ribs, no wounds, no blood, no bite marks. It must read as "a carcass shape" on the sunset ground (`#c9a24a`), night grounds and the near-black death backdrop. Anchor bottom-centre, 520x170 (x -260..260, y -170..0).
- Shots: s002, s010-s011, s015, s017, s041-s042, s081, s129, s174-s175, s178-s179, s190-s196, s198.

### `wildebeest`
Blue wildebeest standing, facing right: dark grey-brown with faint darker vertical stripes on the neck, black mane and beard, short curved horns, thin legs. Anchor bottom-centre, ~620x380. Also used as a black silhouette (no glow) in the three-panel strip and the hunt.
- Shots: s013-s015, s057, s104, s120.

### `gazelle`
Thomson's gazelle mid-leap, facing right: tan back, black side stripe, white belly, small ringed horns. Anchor bottom-centre, ~420x260. Used at 0.3-0.55 (a row of five at 0.35 must still read).
- Shots: s052-s054, s056.

### `zebra`
Plains zebra standing, facing right, bold black-and-white stripes, upright mane. Anchor bottom-centre, ~600x360. Used small (0.35) as "1 ZEBRA".
- Shots: s119.

### `donkey`
Grey domestic donkey standing, facing right: grey-brown coat, pale muzzle and belly, long ears, short upright mane, dark dorsal stripe. Calm. Anchor bottom-centre, ~480x380.
- Shots: s148, s150.

## Places and maps

### `harar_wall`
**Harar's old city wall at night.** A long whitewashed wall `#e8e4d8` with grey-blue shading `#c9c3b8`, rough plaster texture, a simple crenellated top, and **a small arched opening low in the wall (the hyena hole)** about 120x90 units centred at **(+200,-45)**, dark inside `#2a2620`. A wall lamp on a bracket at about (-450,-330) with a warm `#ffd36b` glow. Anchor bottom-centre, 1500x420 (x -750..750, y -420..0).
- Shots: s134, s136-s137, s139-s140, s143-s145, s149, s151, s155, s157, s198-s199.

### `harar_gate`
A whitewashed old city gate: thick square gatehouse with a rounded arch, **arch opening x -130..130, y -330..0** with a dark interior, a little crenellation on top, plaster texture. Anchor bottom-centre, ~640x600.
- Shots: s151-s154, s156.

### `ngorongoro_crater_map`
Top-down crater map: a ring of green-brown hills (`#6f8a4a` / `#4f6a3a`) around a **flat pale crater floor** `#e8dcb0` with a small blue soda lake near the bottom-left. Black frame, no text. Centre anchor, 900x700. **Keep the floor clear for dots** over an ellipse of about rx 340, ry 240 around (0,0) (hyena dots at x -300..+40, lion dots at x +140..+270, y -180..+180), lake outside that.
- Shots: s106.

### `ethiopia_map`
Ethiopia as a flat land shape (`world_map` style: flat green land, dark green outline, light-blue background, black frame, no labels). Projection **x = (lon - 40) x 40, y = -(lat - 9) x 40** (so Mekelle 39.47E 13.5N = (-21,-180), Harar 42.12E 9.31N = (+85,-12)). About 640x500, centre anchor.
- Shots: s146.

### `tanzania_map`
Tanzania, same style, with the Serengeti region lightly shaded (no text). Projection **x = (lon - 35) x 45, y = -(lat + 6) x 45** (Serengeti about (-9,-166)). Lake Victoria's southern shore at the top as light blue. About 560x520, centre anchor. Sober item: plain, no icons.
- Shots: s183-s185.

### `round_hut`
A round village hut: mud-brown wall `#8a6a4a`, conical thatch roof `#b8913a` with stroke texture, dark doorway. Mid-tone (night). Anchor bottom-centre, ~420x400.
- Shots: s158-s159, s161, s164.

## Humans (crude tier, `auto_ink`)

### `hyena_man`
**Respectful and simple.** A crude-tier man (Doug's line weight, big round head, grey crescent, no cap) seated on a low wooden stool, plain long-sleeved shirt and trousers, calm neutral face, one arm held out holding a strip of meat on a short stick at about **(+170,-200)**. No caricature, no costume, no comic expression. Anchor bottom-centre (stool feet on y=0), ~360x420.
- Shots: s143, s152-s154, s156, s199.

### `sleeper_on_mat`
A crude-tier person asleep on their back on a woven mat `#a08a4a` under a thin plain blanket, eyes closed, nothing else. Quiet, plain, not comic. Anchor bottom-centre, ~380x90.
- Shots: s158-s159.

### `stick_man_plain`
Generic crude-tier adult stick man standing (Doug's line weight, big round head with grey crescent, short hair, **no cap**, neutral face). Anchor **feet (0,0)**, about 450 tall. Six of them stand side by side on the giant jaw.
- Shots: s036.

## Props

### `leftovers_plate`
`dinner_plate` heaped with cold leftovers: a few chips, half a sandwich, peas, a spoon of mash. Nothing with a bone, nothing raw. Anchor centre, ~320x120.
- Shots: s023-s027, s049.

### `chew_bone_bow`
A white pet-shop chew bone (dog-bone shape) with a red ribbon bow tied in the middle. Anchor centre, ~220x90.
- Shots: s045-s047, s049.

### `walking_stick` / `walking_stick_halves`
A plain wooden walking stick with a rounded knob (vertical, 40x420, centre anchor), and the same stick in **two halves lying on the ground** slightly apart with clean splintered break ends (bottom-centre anchor, ~460x60). No damage elsewhere.
- Shots: s046 / s047-s049.

### `plate_bitten`
`dinner_plate` with a large **bite-shaped piece missing** from the right rim (a scalloped arc of tooth marks). Empty plate. Anchor centre, 300x90.
- Shots: s044.

### `hyena_skull_cutaway`
Side-view spotted hyena skull diagram (clean cream `#efe2c0`, brown outline, school-chart look): domed forehead crest, big jaws, and the **heavy cheek teeth (premolars) highlighted in red** `#e0201b` around (+80,+60). Clean, clinical, not a fossil (no rock, no cracks). Anchor centre, 640x380.
- Shots: s030-s032.

### `giant_cartoon_jaw`
A huge cartoon pair of closed jaws seen from the side (like a hydraulic press made of teeth): pale gums, big blunt white teeth interlocking, no blood. **Flat top surface at y -200 from x -320..+320** (six stick men stand on it). Anchor bottom-centre, ~820x260 plus the top lip.
- Shots: s036.

### `cartoon_bone` / `hair_tuft` / `meat_strip`
Three small icons for "the meat, the bone and even the hair": a cream dog-bone-shaped bone (220x90, centre); a tuft of sandy-brown animal hair with a few loose strands (160x120, centre); a small strip of cartoon meat `#c96a5a` with a pale fat edge, no blood (140x50, centre, also the hyena men's offering).
- Shots: s033 / s033 / s080, s153.

### `takeaway_box`
A white Chinese-style takeaway box with a wire handle and a small red logo blob (no text). Centre anchor, 120x130.
- Shots: s009.

### `safari_jeep`
A 1960s open-top field jeep, side view facing right: khaki `#b8a46a`, spare wheel on the back, **headlights off** (dark lenses), black wheels. A seated figure's hips go at about **(+60,-180)**. Anchor bottom-centre, ~760x360.
- Shots: s012, s037-s038.

### `burger_stack`
A ridiculously tall stack of quarter-pound burger patties (about 25 visible patties, brown with grill lines, a little cheese peeking out every few layers), a sesame bun top. Anchor bottom-centre, ~200x900 (top at y -900).
- Shots: s123.

### `lunchbox`
A small red lunchbox with a handle; a string is tied to the handle top at **(0,-70)**. Centre anchor, 160x120.
- Shots: s130.

### `microphone`
A handheld recording microphone with a black foam cover and a short cable. Centre anchor, 60x160.
- Shots: s076.

---
Editor/art notes: the night clock (top-left: a small sky window with a sinking moon, then a sun at DAWN) and the eyes in the dark are drawn inline in the shotlist, no asset needed. The sober cards (s160, s165, s181) are text only.
