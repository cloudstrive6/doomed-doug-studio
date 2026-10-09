# Asset requests: 010 How Every Deadly Venom Would Kill Doug

From the director, for the illustrator (the art director approves). House style follows `assets/library/anglerfish.json`
and `channel/art_bible.md`:
- Creatures and props are drawn in the **detailed tier**: outlines 4-6, flat fills plus `spray` shading, darker back and lighter
  belly, white eyes with black pupils. Everything faces **right** unless stated otherwise. Local coordinates are centred on the anchor.
- **Anchors and sizes matter.** I laid out all 286 shots with outline placeholder boxes at exactly the sizes and anchors below and
  checked the contact sheets (counter zone, caption bar, crops, guide inset). `bc` = anchor at the bottom-centre (the lowest point
  sits on y=0, so the drawing spans y -h..0). `c` = anchor at the centre. Sizes are local units at scale 1, width x height. Where a
  note gives a local point (a spur, a stinger, a jaw, an eye cluster), I aimed arrows, rings or overlays at it, so please keep it there.
- **Tone (brief risk list: kid appeal HIGH, this is our most kid-adjacent lane).** Nature horror for adults. Every animal looks
  dangerous, not plush: no cute faces, no smiles, no blush, no big sparkly eyes, no pastel nursery colours. **No bites, wounds,
  swelling, blood or venom drips** on any drawing.
- **Dark scenes:** the fast-killers half runs on dark teal `#1f5f66` down to near-black `#03141a` / `#060c12`. Octopus, mamba,
  funnel-web, both jellyfish and the torch need mid-tone fills or pale outlines that read on those. The funnel-web is glossy black
  in life, so give it blue-grey highlights and a `#2a2f38`-ish body (not pure black), or it vanishes on `#0e1c22`.
- SIL = also used with `"silhouette": true` (black shape with a red glow), so the outer outline must be clean and recognisable as a
  black shape.
- Priority: A = hero (8+ shots), B = supporting (3-7), C = one-off.

Reused from the library (no work needed): `cat` (base for the cat costume), `large_dog`, `rat`, `lab_mouse`, `songbird`,
`steppe_bison` (the "large animal" a dragon bit), `carpenter_ant` (the "normal ant"), `jewel_wasp`, `mosquito`, `pufferfish`,
`small_fish`, `cone_snail` (the 001 callback), `octopus_arm`, `microbe`, `red_blood_cell`, `heart_icon`, `body_outline`,
`hand_outline`, `fingertip`, `scientist`, `rainforest_tree`, `leaf`, `burrow`, `house`, `front_door`, `fishing_boat`, `aquarium`,
`podium`, `bed`, `sofa`, `small_car`, `ruler`, `basketball`, `clock`, `calendar`, `kitchen_timer`, `speedometer`, `bathroom_scale`,
`test_tube_rack`, `petri_dish`, `library_book`, `dinner_plate`, `tin_can` (the grey paint tin), `fly_swatter`, `storm_cloud`,
`doug_cap`, `world_map`, `australia_map`, `india_map`, `pnw_map`, and the annotation set (`question_mark`, `exclamation_mark`,
`warning_triangle`, `red_x`, `thermometer`). Drawn inline in the shotlist (no asset needed): the DOUG DEATHS counter, the bandages on
Doug's hands, the charcoal bed, the light switch, the pain-scale bars, the rasp sound waves, the frying pan, the "NOT A MOUSE" sign,
the grey paint spray on Doug, the UV/torch beams, the scent cloud, the hornet swarm cloud, and the 12-page grid at the end.

**Engine notes for the art director (not illustrator work):**
- s253-s255: alive Doug floating on his back at the Irukandji dusk uses `pose: "on_back"` with `hopeful` / `flat` / `gritted`
  (not `dead`), body at the waterline. Please confirm this reading is OK, since `on_back` is otherwise our death pose.
- `studio/scene.py` had lost its `EDGE_PX` constant in commit 35ddca9 (every render crashed with `NameError`). I restored
  `EDGE_PX = 5` so keyframes could run. Please confirm the value.

---

## A. The field guide (new `animals` playlist prop, needs art-director approval)

### `field_guide_open` (A) **APPROVAL NEEDED**
- **What:** Doug's battered field guide, open flat. The new recurring prop for the `animals` playlist (brief section 4). At each
  animal Doug ticks a "FRIEND?" box. After a death a red "NO" is scrawled on the page, and survivals get an orange "MAYBE". It always
  survives and is never explained.
- **Look:** Small, worn MS Paint notebook seen from above, open to a double spread: cream pages `#fdf6e3` with faint blue ruled lines,
  a dark-brown cover edge `#5b3a22` peeking out around the pages, dog-eared corners, one coffee ring, a red ribbon bookmark hanging
  out of the bottom. Thick black outline (5). **Printed on the right page:** the word `FRIEND?` (black, handwritten-looking caps, about
  34 units tall) centred at (+90,-115), and an **empty** square tick box, 44x44, centred at (+205,-115). Nothing else written on it:
  the animal name, the tick and the stamp are overlaid per shot.
- **Facing / anchor / size:** Anchor `c`, 560x360 (x -280..+280, y -180..+180). Spine down the middle at x=0. **Keep these zones
  clear:** left page around (-140,-110) gets the animal name (text, 26-34 units); the tick box (+205,-115) gets a green tick;
  the stamp zone centred at (+140,+50), about 220x120, gets "NO" (110 units, red) or "MAYBE" (64 units, orange).
- **Shots:** at scale 0.55 bottom-left at (330, 880) on every outcome beat: s020-s024, s043-s045, s065-s069, s089-s092, s114-s117,
  s133-s136, s156-s160, s178-s184, s206-s210, s214, s230-s233, s253-s256, s279-s281. Hero close-ups at scale 1.1-1.2 on the beach:
  s282, s285, s286 (the `doug_cap` sits on top of the right page at (+140,-190)).
- If the art director rejects the prop for cost, tell me and I swap every guide inset for the cap-only close (brief section 4).
- **DONE** (illustrator batch 1): `assets/library/field_guide_open.json`, preview `assets/previews/010-every-venom-assets-b1.png`. c, 560x360 (ribbon hangs to y +202); FRIEND? at (+90,-115), empty 44x44 box at (+205,-115); name and stamp zones only carry faint ruled lines. Still needs art-director approval.

### `field_guide` (B)
- **What:** The same guide, closed, held in Doug's hand in the opening.
- **Look:** Small battered notebook, front cover `#5b3a22` with a cream paper label reading `FIELD GUIDE`, dog-eared corner, red
  ribbon bookmark hanging out of the bottom edge.
- **Facing / anchor / size:** Upright, cover facing the viewer. Anchor `c`, about 140x180. Placed at Doug's front hand, scale 0.42-0.45.
- **Shots:** s002, s003, s005.
- **DONE** (illustrator batch 1): `assets/library/field_guide.json`, preview `assets/previews/010-every-venom-assets-b1.png`. c, 140x180 (ribbon to y +122); FIELD GUIDE label reads at 0.45 as a cream patch.

---

## B. The twelve animals

### `platypus` (A)
- **What:** Adult male platypus (Ornithorhynchus anatinus), the hook item.
- **Look:** Dense dark-brown fur `#5a3a22` with a lighter tan belly, flat soft grey-black duck-like bill `#3a3a3a`, broad flat
  beaver-like tail, short legs with webbed front feet, small dark eyes set high. **The venom spur:** a small pale cream horn-like spur
  on the inside of the hind ankle, clearly drawn and visible. Low, crouched, walking pose. Not cute: no smile, no big eyes.
- **Facing / anchor / size:** Facing right. Anchor `bc`, about 600x230 (x -300..+300, y -230..0). **Keep:** bill tip at about
  (+300,-120); tail at the left end around (-300,-60); hind-ankle spur at (-150,-15); thigh/venom-gland area at (-130,-95)
  (an arrow and a dotted line run spur to thigh). Also used flipped (two males facing each other, s012; Doug-side pet, s020-s021).
- **Shots:** s005-s013, s018-s022 (scale 0.5-2.0; the s008/s010 close-up at 2.0 must hold up).
- **DONE** (illustrator batch 1): `assets/library/platypus.json`, preview `assets/previews/010-every-venom-assets-b1.png`. bc, bbox x -306..+306, y -212..0; bill tip (+306,-124), tail (-306,-62), cream spur at (-160,-20), thigh bulge at (-130,-95).

### `bullet_ant` (A, SIL)
- **What:** Bullet ant (Paraponera clavata) worker.
- **Look:** Large, dark, glossy reddish-black ant `#2a1410` with red-brown highlights `#6b2a1a`, big squarish head with strong
  mandibles, elbowed antennae, a hump-backed node (petiole) and a visible stinger at the abdomen tip. Thin leg hairs. Menacing.
- **Facing / anchor / size:** Facing right (on a vertical trunk in some shots; I rotate if needed). Anchor `c`, about 500x260.
  **Keep:** stinger tip at about (-250,+40).
- **Shots:** s025 (SIL), s026-s027, s029-s030, s033, s036, s040, s043-s044.
- **DONE** (illustrator batch 1): `assets/library/bullet_ant.json`, preview `assets/previews/010-every-venom-assets-b1.png`. c, bbox x -256..+252, y -122..+122; stinger tip (-256,+42).

### `asian_giant_hornet` (A, SIL)
- **What:** Northern (Asian) giant hornet, Vespa mandarinia.
- **Look:** Big orange-yellow head `#f2a51a` with dark eyes and black mandibles, dark brown-black thorax, abdomen banded dark
  brown `#3a2410` and yellow-orange `#f2b01a`, smoky-brown translucent wings held up (pale fill with dark veins), visible stinger.
  Should read as huge and aggressive.
- **Facing / anchor / size:** Facing right. Anchor `c`, about 520x340. **Keep:** stinger tip at about (-260,+40); wings spread
  across the top so a dotted wingspan line at y -170 (local) spans them. Used down to scale 0.22 in a swarm, so keep the silhouette
  bold. Rotated 170 deg as the swatted hornet (s066-s067).
- **Shots:** s047 (SIL), s048-s057, s062-s069, s277.
- **DONE** (illustrator batch 1): `assets/library/asian_giant_hornet.json`, preview `assets/previews/010-every-venom-assets-b1.png`. c, bbox x -266..+258, y -174..+164; stinger tip (-264,+44); wing tips at (-214,-172) and (+206,-174).

### `komodo_dragon` (A, SIL)
- **What:** Komodo dragon (Varanus komodoensis), adult.
- **Look:** Massive grey-brown lizard `#6f6450` with darker pebbly scale texture, heavy body low to the ground, thick bowed legs with
  curved claws, long muscular tail, long forked yellow tongue out, heavy lower jaw. Dusty, battered skin, no drool.
- **Facing / anchor / size:** Facing right. Anchor `bc`, about 900x300 (x -450..+450). **Keep:** mouth/lower jaw at about
  (+400,-70) (microbes cluster there in s071/s079); also used flipped.
- **Shots:** s070 (SIL), s071, s073-s076, s078-s080, s083, s086-s092, s277.
- **DONE** (illustrator batch 1): `assets/library/komodo_dragon.json`, preview `assets/previews/010-every-venom-assets-b1.png`. bc, bbox x -454..+484 (tongue past +450), y -216..0; lower jaw at (+400,-66).

### `komodo_head_scan` (C)
- **What:** Diagram of the 2009 head scan (Fry et al.): a side cross-section of a Komodo head.
- **Look:** Diagram style on a pale blue-grey card: head outline in grey with the skull/jaw in light bone colour, teeth, and the
  **venom gland in the lower jaw** filled bright yellow-orange `#ffb000` with a darker outline. No gore, clean "textbook" look.
- **Facing / anchor / size:** Facing right. Anchor `c`, about 600x360. **Keep:** the venom gland centred at about (+60,+90).
- **Shots:** s081.
- **DONE** (illustrator batch 1): `assets/library/komodo_head_scan.json`, preview `assets/previews/010-every-venom-assets-b1.png`. c, 600x360; gland ellipse centred (+60,+90), small 'FRY ET AL. 2009' caption top-left.

### `indian_red_scorpion` (A, SIL)
- **What:** Indian red scorpion (Hottentotta tamulus).
- **Look:** Reddish-orange to brick body `#c0582a` with darker back plates, two slim pincers forward, eight legs, segmented tail raised
  and curled over the back ending in a bulbous sting with a dark tip.
- **Facing / anchor / size:** Facing right (pincers right). Anchor `c`, about 520x300. **Keep:** sting at about (-60,-150).
  Also used flipped and tiny (0.22, rotated) climbing out of a boot.
- **Shots:** s093 (SIL), s094-s097, s102-s104, s107 (SIL), s108, s112-s113, s277.
- **DONE** (illustrator batch 1): `assets/library/indian_red_scorpion.json`, preview `assets/previews/010-every-venom-assets-b1.png`. c, bbox about x -232..+266, y -178..+120; sting tip at (-56,-146), bulb at (-106,-152).

### `indian_red_scorpion_uv` (B)
- **What:** The same scorpion under ultraviolet light.
- **Look:** Exactly the same geometry as `indian_red_scorpion`, but every fill in glowing blue-green (`#3dffc8` body, `#a8fff0`
  highlights, `#14b08a` darker plates), outline dark teal `#0a4a3c`. Built-in soft `spray` glow around it.
- **Facing / anchor / size:** Same as above (anchor `c`, 520x300).
- **Shots:** s109-s111, s115-s116.
- **DONE** (illustrator batch 1): `assets/library/indian_red_scorpion_uv.json`, preview `assets/previews/010-every-venom-assets-b1.png`. same geometry, built-in glow spray reaches r 230.

### `saw_scaled_viper` (A, SIL)
- **What:** Saw-scaled viper (Echis), coiled in its threat display.
- **Look:** Small, sandy-brown snake `#b08a5a` with a row of pale, dark-edged saddle blotches, rough keeled scales (short texture
  strokes), pear-shaped head with a pale cross/arrow mark on top. **Coiled in tight C-shaped loops** (figure-8 posture), head raised
  slightly at the front. Small and unassuming, not cartoon-cute.
- **Facing / anchor / size:** Facing right. Anchor `c`, about 420x220. **Keep:** head at about (+150,-60). Used tiny (0.3) by Doug's
  foot and big (2.4) for the scales close-up, so the scale texture should hold up at 2.4.
- **Shots:** s118 (SIL), s120-s122, s124-s128, s132-s136, s227-s229, s277.
- **DONE** (illustrator batch 1): `assets/library/saw_scaled_viper.json`, preview `assets/previews/010-every-venom-assets-b1.png`. c, bbox about x -210..+214, y -98..+110; head centre (+160,-66).
- **REVISED** (art review fix 2): removed the two width-5 black stubs (old elements 72 and 168) at the left coil seam; the continuous outline is unchanged and the left loop end no longer reads as a second head at 2.4. Preview `assets/previews/010-every-venom-assets-b1.png` (re-rendered).

### `blue_ringed_octopus` (A)
- **What:** Blue-ringed octopus (Hapalochlaena) at rest.
- **Look:** Small, golf-ball-sized body, **dull ochre-brown** `#a07a3a` with faint darker rings, short curling arms. Calm, not cute:
  small slit-pupil eyes, no smile.
- **Facing / anchor / size:** Anchor `c`, about 360x260 (mantle top-centre, arms spread down/out).
- **Shots:** s138-s142, s150-s151, s159, s277.
- **DONE** (illustrator batch 1): `assets/library/blue_ringed_octopus.json`, preview `assets/previews/010-every-venom-assets-b1.png`. c, bbox about x -186..+186, y -134..+134.

### `blue_ringed_octopus_flash` (A)
- **What:** The same octopus, disturbed, rings flashing.
- **Look:** Identical geometry to `blue_ringed_octopus`, but the body turns bright yellow `#f2d23a` and the rings are vivid electric
  blue `#1f6bff` with black edges, plus a faint blue `spray` glow. This is the warning flash, so it should read as "danger".
- **Facing / anchor / size:** Same (anchor `c`, 360x260). Doug lifts it in cupped hands at scale 0.3.
- **Shots:** s141-s147, s153, s155-s158.
- **DONE** (illustrator batch 1): `assets/library/blue_ringed_octopus_flash.json`, preview `assets/previews/010-every-venom-assets-b1.png`. same geometry; blue glow spray r 200.

### `black_mamba` (A, SIL)
- **What:** Black mamba (Dendroaspis polylepis), the "it's not black" item.
- **Look:** Long, slim, **olive-grey** snake `#7c8a5a` / `#8a8f96` (absolutely not black), paler belly, coffin-shaped head held up in
  front, mouth closed, small dark eye. Long gentle S-curves.
- **Facing / anchor / size:** Facing right. Anchor `c`, about 900x300. **Keep:** head (and closed mouth) at about (+400,-100), where
  the s174 arrow lands. Also used flipped and as a SIL.
- **Shots:** s119 (SIL), s161 (SIL), s162-s170, s173-s175, s178-s180, s182, s184, s277.
- **DONE** (illustrator batch 2): `assets/library/black_mamba.json`, preview `assets/previews/010-every-venom-assets-b2a.png`. olive-grey, head/closed mouth at (+400,-100); bbox x -450..+458.

### `black_mamba_gape` (B)
- **What:** The black mamba's threat display: front body reared up, mouth wide open.
- **Look:** Olive-grey head and neck reared, mouth gaping very wide to show the **inky blue-black mouth lining** `#0b0f2a` (the only
  black part). Small fangs. No drool, no venom drops.
- **Facing / anchor / size:** Facing right. Anchor `c`, about 600x500. **Keep:** the centre of the open mouth at about (+150,-100)
  (a red ring and "BLACK" label sit there). Also used flipped.
- **Shots:** s175-s177, s181.
- **DONE** (illustrator batch 2): `assets/library/black_mamba_gape.json`, preview `assets/previews/010-every-venom-assets-b2a.png`. mouth centre about (+150..+180,-100), inky #0b0f2a lining; bbox x -275..+290, y -245..+250.

### `funnel_web_spider` (A, SIL)
- **What:** Male Sydney funnel-web spider (Atrax robustus) in its rearing threat pose.
- **Look:** Glossy blue-black body `#2a2f38` with blue-grey shine highlights, bare shiny carapace, long dark legs, the front legs
  raised high, and **large downward-pointing fangs** shown (no venom drops). The male has a spur on the second leg. Menacing.
- **Facing / anchor / size:** Facing right. Anchor `bc`, about 420x260 (feet on y=0). **Keep:** fangs at about (+160,-240)
  (the s193 arrow).
- **Shots:** s185 (SIL), s186-s187, s189-s195, s199, s203-s206, s208-s210, s277.
- **DONE** (illustrator batch 2): `assets/library/funnel_web_spider.json`, preview `assets/previews/010-every-venom-assets-b2a.png`. #2a2f38 with blue-grey shine; fangs hang from (+150..+172,-222) to y -168 (chelicerae at (+150,-240)); raised front legs reach y -305, a little above the 260 box.

### `inland_taipan` (A, SIL)
- **What:** Inland taipan (Oxyuranus microlepidotus), summer colouring.
- **Look:** Pale straw-to-light-brown snake `#c9a46a` with a slightly darker head, scales outlined in a faint darker net, dark eye,
  long smooth body in a relaxed S-curve. Calm and shy-looking but still a dangerous snake (no smile).
- **Facing / anchor / size:** Facing right. Anchor `c`, about 800x260. Also used flipped (leaving, s231) and as a SIL.
- **Shots:** s119 (SIL), s211 (SIL), s212, s217-s224, s226, s228, s231.
- **DONE** (illustrator batch 2): `assets/library/inland_taipan.json`, preview `assets/previews/010-every-venom-assets-b2a.png`. head at about (+362,-26); bbox x -405..+414.

### `inland_taipan_winter` (C)
- **What:** The same snake in winter colouring (it darkens to absorb heat).
- **Look:** Identical geometry to `inland_taipan`, but dark glossy brown `#4a3020` with a near-black head `#1e1410`.
- **Facing / anchor / size:** Same (anchor `c`, 800x260).
- **Shots:** s218-s219.
- **DONE** (illustrator batch 2): `assets/library/inland_taipan_winter.json`, preview `assets/previews/010-every-venom-assets-b2a.png`. same geometry as inland_taipan.

### `irukandji_jellyfish` (B)
- **What:** Irukandji jellyfish (Carukia barnesi): fingertip-sized box jelly.
- **Look:** Tiny, transparent, **box-shaped bell** with a pale fill `#dff6ff`, light outline `#7fb2c9`, faint red-brown dots
  (stinging-cell clusters) on the bell, and four very long, thin, pale threads hanging straight down. Nearly invisible on purpose,
  but the outline must read on dark teal `#123c48`.
- **Facing / anchor / size:** Anchor at the **bell centre**: bell about 80x80 (x -40..+40, y -40..+40), threads down to y +400
  (bbox x -60..+60, y -40..+400). Used at 0.4 (tiny in the sea) up to 3.0 (bell close-up, threads run off the frame).
- **Shots:** s234, s236-s238, s240-s242, s247, s253.
- **DONE** (illustrator batch 2): `assets/library/irukandji_jellyfish.json`, preview `assets/previews/010-every-venom-assets-b2a.png`. bell x -40..+40, threads to y +398.

### `box_jellyfish` (A, SIL)
- **What:** Australian box jellyfish (Chironex fleckeri), the boss.
- **Look:** Cube-shaped, nearly transparent bell, pale fill `#cfefff` with a light blue outline `#6fb7d6` and subtle white highlights;
  at each of the **four lower corners** a fleshy arm (pedalium) with a bunch of long, thin, pale tentacles trailing down. Small dark
  eye clusters (rhopalia) visible near the bottom of each side. Must read on near-black `#03141a` and as a clean SIL.
- **Facing / anchor / size:** Anchor at the **bell centre**: bell about 340x260 (x -170..+170, y -130..+130), tentacles down to y +700.
  **Keep:** the four eye clusters at about (-120,+95), (+120,+95), (-50,+115), (+50,+115). I also draw it with `ink` overrides
  (`#24505c`, `#163a44`) to make it fainter in the water, so keep black outlines as the only outline colour.
- **Shots:** s257 (SIL), s258, s259 (SIL), s260, s262-s264, s267 (SIL), s268-s269, s271, s273-s276, s278.
- **DONE** (illustrator batch 2): `assets/library/box_jellyfish.json`, preview `assets/previews/010-every-venom-assets-b2b.png`. eye clusters exactly at the four requested points; black outlines only (ink-overridable); pedalia flare out, so bbox x -245..+245, tentacles to y +700.
- **REVISED** (art review fix 1): each rhopalium cluster is now 6 equal dots (r 2.5) in a 2-wide x 3-tall block (x ±4, y -6/0/+6); no smile arc, no big eye pair. Cluster centres unchanged at (-120,+95), (+120,+95), (-50,+115), (+50,+115). Preview `assets/previews/010-every-venom-assets-b2b.png` (re-rendered).

### `box_jellyfish_eyes` (C)
- **What:** The same box jellyfish with its 24 eyes lit.
- **Look:** Identical geometry to `box_jellyfish`, with the four eye clusters (6 small eyes each, 24 in total) glowing yellow
  `#ffe24a` with a small `spray` glow each. Placed on top of `box_jellyfish` (appear 0.3), so it must line up exactly.
- **Facing / anchor / size:** Same (anchor bell centre).
- **Shots:** s269.
- **DONE** (illustrator batch 2): `assets/library/box_jellyfish_eyes.json`, preview `assets/previews/010-every-venom-assets-b2b.png`. full redraw of box_jellyfish + 24 lit eyes; lines up at the same x/y/scale.
- **REVISED** (art review fix 1): the 24 lit eyes use the same 2x3 block layout as `box_jellyfish` (identical x/y/r), so the overlay still lines up. Preview `assets/previews/010-every-venom-assets-b2b.png` (re-rendered).

---

## C. Costume and creatures for the funnel-web row

### `cat_costume` (B)
- **What:** Doug's homemade cat costume (worn prop) for the funnel-web gag, "zipped into an entire cat". Based on `cat.json` colours.
- **Look:** Orange tabby onesie `#f08a2a` with darker tabby stripes `#c0601a`, white chest panel, front zipper with a pull tab, mitten
  paws at the hands, a long striped tail out of the back at hip height, and a cat hood bunched round his neck and chin with **two
  pointed cat ears at the back of the head, left of the cap dome** (about x -95..-40, y -300..-240 local) so they never cover the cap
  or the face. Doug's face and red cap stay fully visible (art bible costume rule). Played straight and grim, not mascot-cute.
- **Facing / anchor / size:** Worn prop at Doug's x/y/scale, `stand` pose (hips at 0,0, neck y -150, feet y +150). Placeholder box
  was x -85..+85, y -140..+150.
- **Shots:** s202, s205.
- **DONE** (illustrator batch 2): `assets/library/cat_costume.json`, preview `assets/previews/010-every-venom-assets-b2b.png`. checked over Doug `stand`: hood clears the cap and face, ears at x -125..-56, y -326..-232; tail reaches x -176.

### `cat_costume_sit` (B)
- **What:** The same costume for Doug's `sit` pose (he sits smugly on the back step).
- **Look:** As `cat_costume`, posed for `sit`: hip drops to y +70, legs go straight forward to about (+152,+70), torso from (0,+70) up
  to the neck at (0,-80), head centre (0,-148). Leg sleeves along the legs, tail curling behind at about (-60,+60).
- **Facing / anchor / size:** Worn prop at Doug's x/y/scale (`sit` pose). Placeholder box was x -85..+160, y -80..+90.
- **Shots:** s206-s209.
- **DONE** (illustrator batch 2): `assets/library/cat_costume_sit.json`, preview `assets/previews/010-every-venom-assets-b2b.png`. checked over Doug `sit`.

### `cat_costume_flat` (C)
- **What:** The cat costume after the death beat (s210), like `crab_costume_flat`.
- **Look:** The empty orange tabby suit lying flat and deflated on the step, hood flopped with the two ears drooping and **white X eyes
  on the hood's cat face**. No Doug, no tears. I place `doug_cap` beside it.
- **Facing / anchor / size:** Anchor `bc`, about 500x160.
- **Shots:** s210.
- **DONE** (illustrator batch 2): `assets/library/cat_costume_flat.json`, preview `assets/previews/010-every-venom-assets-b2b.png`. bc, bbox x -298..+262, y -112..0.

### `monkey` (B)
- **What:** Generic macaque, the "primates" in the toxin row.
- **Look:** Sitting brown-grey macaque `#8a7058` with a pinkish face, small ears, long tail curled beside it. Neutral expression.
- **Facing / anchor / size:** Facing right. Anchor `bc`, about 260x340.
- **Shots:** s200-s203.
- **DONE** (illustrator batch 2): `assets/library/monkey.json`, preview `assets/previews/010-every-venom-assets-b2b.png`. bc, bbox x -146..+138, y -330..0.

### `rabbit` (C)
- **What:** Ordinary brown rabbit, one of the mammals that shrug the venom off.
- **Look:** Brown-grey wild rabbit `#9a7a5a`, pale belly, long upright ears, white tail tuft, sitting. Not a cartoon bunny.
- **Facing / anchor / size:** Facing right. Anchor `bc`, about 260x220.
- **Shots:** s200-s202.
- **DONE** (illustrator batch 2): `assets/library/rabbit.json`, preview `assets/previews/010-every-venom-assets-b2b.png`. bc, bbox x -136..+152, y -228..0.

---

## D. Props and scale objects

### `pill_bottle` (C)
- **What:** Prescription bottle for the morphine beat.
- **Look:** Orange translucent pharmacy bottle `#f0a030` with a white child-proof cap and a white label printed `MORPHINE` in black.
  No pills spilling.
- **Facing / anchor / size:** Upright. Anchor `c`, about 160x240.
- **Shots:** s013, s015.
- **Done** (illustrator batch 3): `assets/library/pill_bottle.json`, preview `assets/previews/010-every-venom-assets-c1.png`

### `staple` (C)
- **What:** One office staple (15-18 mm platypus spur comparison).
- **Look:** A single bent silver staple `#b8bcc4`, seen from the side (a flat "U"), with a dark outline.
- **Facing / anchor / size:** Horizontal. Anchor `c`, about 120x40.
- **Shots:** s009.
- **Done** (illustrator batch 3): `assets/library/staple.json`, preview `assets/previews/010-every-venom-assets-c1.png`

### `paperclip` (C)
- **What:** Standard paperclip (bullet ant ~2 cm).
- **Look:** Silver wire paperclip `#b8bcc4`, horizontal, the classic double loop, dark outline.
- **Facing / anchor / size:** Horizontal. Anchor `c`, about 240x80.
- **Shots:** s029.
- **Done** (illustrator batch 3): `assets/library/paperclip.json`, preview `assets/previews/010-every-venom-assets-c1.png`

### `ant_glove` (C)
- **What:** The woven glove of the Sateré-Mawé coming-of-age ceremony, shown as an object only (no people, no Doug; the brief asks
  for respect and no jokes).
- **Look:** A tube-shaped sleeve woven from pale straw-coloured palm fibre `#d8b878`, with a simple woven crosshatch pattern and a few
  feather tufts at the rim. A few small dark ants visible in the weave. Plain and respectful, no decoration that could read as a
  costume.
- **Facing / anchor / size:** Upright. Anchor `c`, about 300x360.
- **Shots:** s041-s042.
- **Done** (illustrator batch 3): `assets/library/ant_glove.json`, preview `assets/previews/010-every-venom-assets-c1.png`

### `honeybee` (C)
- **What:** Western honeybee worker for the stinger comparison.
- **Look:** Golden-brown body with dark bands, fuzzy thorax, clear wings, small stinger.
- **Facing / anchor / size:** Facing right. Anchor `c`, about 220x150 (draw it at the same scale as the hornet: about 40% of its length).
- **Shots:** s053.
- **Done** (illustrator batch 3): `assets/library/honeybee.json`, preview `assets/previews/010-every-venom-assets-c1.png`

### `matchbox` (C)
- **What:** A closed matchbox (the hornet is "the length of a matchbox"). The library `matchbox_charger` has cables in it, so it doesn't work here.
- **Look:** Closed rectangular matchbox with a red/yellow label and a brown striker strip on the side.
- **Facing / anchor / size:** Horizontal, 3/4 view. Anchor `c`, about 260x170.
- **Shots:** s051.
- **Done** (illustrator batch 3): `assets/library/matchbox.json`, preview `assets/previews/010-every-venom-assets-c1.png`

### `beehive` (C)
- **What:** Wooden honeybee hive box that the hornets raid.
- **Look:** Stacked white/pale-yellow wooden hive boxes `#f2e6b0` with a flat lid, a dark entrance slot at the bottom, a few bees.
- **Facing / anchor / size:** Front view. Anchor `bc`, about 280x300.
- **Shots:** s057-s058.
- **Done** (illustrator batch 3): `assets/library/beehive.json`, preview `assets/previews/010-every-venom-assets-c1.png`

### `mouthwash_bottle` (B)
- **What:** The giant bottle of mouthwash Doug brings the Komodo dragon.
- **Look:** Big translucent green bottle `#3cc08a` with a white screw cap (sealed) and a white label printed `MOUTHWASH`.
- **Facing / anchor / size:** Upright. Anchor `c`, about 160x300. I rotate it 90 deg when it rolls away (s092), so keep the label readable sideways.
- **Shots:** s089, s092.
- **Done** (illustrator batch 3): `assets/library/mouthwash_bottle.json`, preview `assets/previews/010-every-venom-assets-c1.png`, assets/previews/010-every-venom-assets-c3.png (dark bg / rotated / bottom-anchored check)

### `uv_torch` (B)
- **What:** Ultraviolet torch (blacklight flashlight) for the scorpion beat.
- **Look:** Black rubberised handle, purple lens `#9a4aff` with a small glow at the lens end.
- **Facing / anchor / size:** **Anchor at the handle end** (Doug's hand), body running to the right, lens at about (+250,0). About
  260x80 (x 0..260, y -40..+40). I draw the purple beam inline from the lens.
- **Shots:** s108-s109, s114-s116.
- **Done** (illustrator batch 3): `assets/library/uv_torch.json`, preview `assets/previews/010-every-venom-assets-c1.png`, assets/previews/010-every-venom-assets-c3.png (dark bg / rotated / bottom-anchored check)

### `torch` (B)
- **What:** Ordinary torch (flashlight) for the box jellyfish night wade.
- **Look:** Same shape as `uv_torch`, yellow/grey body with a warm white lens `#fff3b0`. Must read on near-black water.
- **Facing / anchor / size:** Same as `uv_torch` (anchor at the handle end, lens at +250).
- **Shots:** s279-s281.
- **Done** (illustrator batch 3): `assets/library/torch.json`, preview `assets/previews/010-every-venom-assets-c2.png`, assets/previews/010-every-venom-assets-c3.png (dark bg / rotated / bottom-anchored check)

### `boot` (B)
- **What:** Doug's work boot (the scorpions are inside it, and he is wearing it).
- **Look:** Brown leather lace-up work boot `#7a4a2a`, dark sole, open top with a dark opening, side view.
- **Facing / anchor / size:** Toe pointing right. Anchor `bc`, about 220x200. Worn on Doug's front foot at scale 0.45, so the
  opening at the top (0,-200) sits on his shin. Also rotated -80 deg lying on the floor (s117).
- **Shots:** s114-s117.
- **Done** (illustrator batch 3): `assets/library/boot.json`, preview `assets/previews/010-every-venom-assets-c2.png`, assets/previews/010-every-venom-assets-c3.png (dark bg / rotated / bottom-anchored check)

### `binoculars` (C)
- **What:** Binoculars (Doug scanning for something big; Auffenberg watching dragons).
- **Look:** Black binoculars with two barrels and grey lens rims, front view at a slight angle.
- **Facing / anchor / size:** Anchor `c`, about 160x90.
- **Shots:** s078, s133-s134.
- **Done** (illustrator batch 3): `assets/library/binoculars.json`, preview `assets/previews/010-every-venom-assets-c2.png`, assets/previews/010-every-venom-assets-c3.png (dark bg / rotated / bottom-anchored check)

### `golf_ball` (C)
- **What:** Golf ball (the octopus is about this size).
- **Look:** White ball with dimple dots and a light grey shading crescent.
- **Facing / anchor / size:** Anchor `c`, about 120x120. Draw it at the same scale as the octopus (golf-ball body).
- **Shots:** s139.
- **Done** (illustrator batch 3): `assets/library/golf_ball.json`, preview `assets/previews/010-every-venom-assets-c2.png`

### `seashell` (C)
- **What:** An empty-looking spiral seashell (people pick these up with a blue-ringed octopus hiding inside).
- **Look:** Cream-and-tan whelk/cone-like spiral shell `#e8d4b0` with brown bands, opening facing right and slightly down. Dark
  opening, nothing visible inside (I add an `octopus_arm` tip poking out at the opening).
- **Facing / anchor / size:** Anchor `c`, about 300x200. **Keep:** the opening at about (+130,+40).
- **Shots:** s154.
- **Done** (illustrator batch 3): `assets/library/seashell.json`, preview `assets/previews/010-every-venom-assets-c2.png`, assets/previews/010-every-venom-assets-c3.png (dark bg / rotated / bottom-anchored check)

### `guitar` (C)
- **What:** Acoustic guitar (Irukandji tentacles reach about a meter, "roughly the length of a guitar").
- **Look:** Classic acoustic guitar, wooden body `#c08040`, dark neck, sound hole, six strings.
- **Facing / anchor / size:** Horizontal, neck to the right. Anchor `c`, about 500x180. I rotate it 90 deg.
- **Shots:** s238.
- **Done** (illustrator batch 3): `assets/library/guitar.json`, preview `assets/previews/010-every-venom-assets-c2.png`

### `basketball_hoop` (C)
- **What:** Regulation basketball hoop (3.05 m), the box jellyfish tentacle comparison.
- **Look:** Pole `#555`, white backboard with a red square, orange rim with a white net. Rim at about y -600, backboard top at y -700.
- **Facing / anchor / size:** Side/front view. Anchor `bc`, about 300x700.
- **Shots:** s265.
- **Done** (illustrator batch 3): `assets/library/basketball_hoop.json`, preview `assets/previews/010-every-venom-assets-c2.png`, assets/previews/010-every-venom-assets-c3.png (dark bg / rotated / bottom-anchored check)
