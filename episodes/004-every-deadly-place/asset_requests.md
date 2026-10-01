# Asset requests: 004 Every Deadly Place

From the director, for the illustrator. The art director owns the suitcase and sticker set (series lore) and approves
the worn props. House style follows `assets/library/anglerfish.json` and `channel/art_bible.md`:
- Creatures, places and props are the detailed tier: outlines 4-6, flat fills plus `spray` shading, a darker back
  and lighter belly, and white eyes with black pupils.
- Humans are the crude tier, like `scientist`: 5 px lines, a big round head with the grey crescent, and `"auto_ink": true`.
- Everything faces **right** unless stated. Local coordinates are centred on the anchor, and sizes are local units at scale 1.

**Anchors matter.** I laid out all 282 shots with placeholder boxes at the sizes and anchors below and checked the
contact sheets. If an anchor or size is wrong, the drawing lands in the sky or covers Doug.

Tone: deadpan nature documentary for adults. Nothing cute, no big shiny "kids' show" eyes, no pastel nursery palette.
No gore anywhere. Dead animals (Natron, mazuku) are chalky grey cartoon shapes only.

Rig reference for **worn props** (`flip_flops`, `flamingo_costume`, `zapped_hair`, `cooling_suit` on the scientist):
anchor (0,0) = **Doug's hips** at Doug scale 1. Head centre (0,-218) r72, cap top about y=-300, cap brim points right
to x=+126, shoulders (0,-122), feet at y=+150, and stand-pose feet at x about ±32. Props must leave the **head, face
and red cap fully visible**.

Priority: A = hero or recurring, B = supporting, C = one-off. SIL = also used with `"silhouette": true`, so the
outer outline must be clean and recognisable.

---

## Art director: series lore (`places` playlist)

### travel_suitcase (A, art director owns the drawing)
- **What:** Doug's suitcase, the standard prop of the `places` playlist (series bible, from 004). It is a battered
  MS Paint travel suitcase. It must be **clearly distinct** from the over-packed `suitcase.json`: no "HEAVY" tag,
  no escaping sock and no bulging straps.
- **Look:** a flat, upright hard-shell case seen from the front. The body is about 380 wide x 270 tall
  (x -190..+190, y -270..0), in a scuffed tan-brown (`#a0522d` face, darker `#7a3d20` edge band) with two dents and
  one scratch. It has a short black carry handle on top (y -310..-270), two small corner wheels or feet at the bottom,
  and a thin vertical seam. Leave the face **plain**, because the stickers are separate assets placed on it.
- **Anchor:** bottom-centre on the ground (the wheels touch y=0).
- **Sticker slots** (the centres I place stickers at, in local units, filled in this order):
  row 1 (-120,-215), (0,-215), (120,-215); row 2 (-120,-150), (0,-150), (120,-150);
  row 3 (-120,-85), (0,-85), (120,-85). Keep these areas free of handles, locks or shading that would fight the stickers.
  Leave a **thin empty strip along the bottom** (about y -45..-10). The last shot (s282) puts a red arrow on it for
  "The suitcase still has room."
- **Carried:** in opener and arrival shots Doug holds it by the handle in his back hand at scale 0.55 x Doug scale,
  so the handle must read at small size. On death shots it stands alone at scale 0.6-0.95 so the stickers can be read.
- **Shots:** s002-s006, s011-s012, s023-s027, s029, s033, s045-s051, s054-s055, s072-s078, s101, s103-s104,
  s125-s129, s140, s146-s151, s171-s174, s177, s199-s204, s220-s221, s223, s237-s245, s273-s282.

### Travel stickers (A, art director, 9 assets, one per death)
- **What:** crude travel stickers, one per place where Doug died. Survivals (Lake Natron, Lake Maracaibo) get none.
- **Look:** each is about 110 x 60 (x -55..+55, y -30..+30), anchor centre. Use a different flat sticker shape and
  colour per place (oval, rectangle, scalloped, pennant), a 3-4 px dark outline, a slightly peeling corner, and the
  place name in bold caps. Where room allows, add one tiny icon. The text must stay legible at scale 0.6
  (≈ 66 px wide), so use big letters and two lines if needed. I rotate them a few degrees in the shot.
- **Names and suggested look:**
  | asset | text | icon idea |
  |---|---|---|
  | `sticker_death_valley` | DEATH VALLEY | sun or cracked ground, sand-yellow |
  | `sticker_snake_island` | SNAKE ISLAND | small yellow snake, green |
  | `sticker_morecambe_bay` | MORECAMBE BAY | wave line, blue |
  | `sticker_antarctica` | ANTARCTICA | snowflake, ice-blue |
  | `sticker_everest` | EVEREST | peak with flag, white/grey |
  | `sticker_naica` | NAICA | crystal, pale yellow |
  | `sticker_dallol` | DALLOL | neon yellow-green pool |
  | `sticker_nyos` | NYOS | **no icon, plain dark-blue oval**. The item is sombre (a real mass-casualty event) and its sticker must not be playful |
  | `sticker_nyiragongo` | NYIRAGONGO | volcano, lava red |
- **Shots:** each appears from its death shot onward. The `slap` pop-in is at s025 (Death Valley), s047 (Snake Island),
  s076 (Morecambe), s127 (Antarctica), s149 (Everest), s174 (Naica), s201 (Dallol) and s278 (Nyiragongo).
  `sticker_nyos` is already there at s221 with no pop-in, by script direction. All nine are on the final frame,
  s280-s282.

---

## Worn props and Doug-adjacent (art director approves)

### flip_flops (A) and flip_flops_cracked (C)
- **What:** Doug's flip-flops, worn across the Hours and Minutes bands (script: Death Valley, Natron, Antarctica).
- **Look:** two flat soles under Doug's stand-pose feet, centred at about (±32, +150) and each about 60 x 18, with a
  thin Y strap rising to the foot point. Bright cheap colours: a blue sole and a yellow strap. `flip_flops_cracked` has
  the same geometry, but the soles are faded and cracked (2-3 zigzag crack lines, a chipped edge) for "dry and cracked" (s101).
- **Anchor:** Doug's hips at Doug scale (bbox about x -75..+75, y +135..+160). I only use it with `stand` and `point`.
  Panic shots (s013-s014) use the same prop, which is fine if it reads as roughly under the feet.
- **Shots:** flip_flops s011-s014, s022, s104, s125-s128; flip_flops_cracked s101.

### flamingo_costume (A, costume gag)
- **What:** Doug zipped into a **lesser flamingo** costume to "blend in" (the costume gag, played straight). The red cap
  stays on top, and his head and face stay fully visible.
- **Look:** a pink (`#f4a3b8`, deeper `#e0708f` wing patch) feathered body suit from the shoulders (y -130) to below the
  hips (y +100), so it covers his torso and thighs. A visible zipper runs down the front. A long S-neck rises from his
  back shoulder to a **flamingo head beside (not over) Doug's head**, at about (-120,-330), with a downturned dark-tipped
  bill. **One pink leg folded up** at the side, knee bent back flamingo-style, sells "stands on one leg".
- **Anchor:** Doug's hips (bbox about x -110..+110, y -300..+100). Use with `stand`. I draw shallow water over his
  lower legs after the costume.
- **Shots:** s098-s100.

### zapped_hair (B)
- **What:** after the lightning strike, "his hair is pointing in several new directions".
- **Look:** spiky black hair tufts poking out **under the cap brim and behind the ears** (6-8 jagged spikes around the
  head outline at y -300..-160), plus two tiny soot smudges on the cheeks. Do not cover the eyes, mouth or cap. This is
  a prop like `head_towel`; it does not change the design.
- **Anchor:** Doug's hips at Doug scale. I use it with the `sit` pose, so the head is at (0,-148), drop 70.
  **Please check the sit-pose head position** (rig `drop`). If it's easier, draw it for the stand head and tell me the
  offset.
- **Shots:** s240-s244.

### cooling_suit (C)
- **What:** the ice-packed cooling suit that Naica scientists wore.
- **Look:** a bulky pale-orange coverall with a grid of blue ice-pack pouches on the chest and sleeves, worn over the
  `scientist` asset. Leave the face and glasses visible.
- **Anchor:** the scientist's hips (same rig as Doug, bbox about x -110..+110, y -200..+100).
- **Shots:** s169-s170.

---

## Snake Island

### golden_lancehead (A, SIL)
- **What:** golden lancehead pit viper (*Bothrops insularis*), endemic to Queimada Grande. It is the item's hero.
- **Look:** a pale golden-yellow to tan body (`#d9b44a`, darker blotches `#a8862a`), coiled on a branch with the
  head raised to the right. It has a broad **arrow-shaped (lance) head**, a dark stripe behind the eye, a vertical
  pupil and a pale belly. It should look calm and unnerving, not cute and not aggressive-gory. No fangs on display.
  The silhouette needs a clear raised head.
- **Anchor:** bottom-centre of the coil, where it sits on the branch top. Size about 440 x 270 (x -210..+230,
  y -260..+10). It is also used tiny (scale 0.22) in grid cells and as a crowd of neighbours.
- **Shots:** s030 (silhouette, glow_r 380), s031-s032, s034-s037, s039-s040, s043-s049.

## Morecambe Bay

### sands_guide (C)
- **What:** a crude-tier human: the King's Guide to the Sands, who leads walkers across the bay.
- **Look:** Doug's tier (5 px lines, round head with crescent). Give him a **green** flat cap (not red, so he can't be
  mistaken for Doug), wellies, and a tall bare branch or staff held upright.
- **Anchor:** hips (like `scientist`, feet at +150, bbox about x -80..+80, y -320..+150). `"auto_ink": true`.
- **Shots:** s056-s057.

## Lake Natron

### lesser_flamingo (A)
- **What:** lesser flamingo (*Phoeniconaias minor*), adult, standing in shallow water.
- **Look:** deep pink body with crimson wing coverts, long thin pink legs, an S-neck, and a **dark, almost black-red,
  downturned bill** (lesser flamingos have a darker bill than greater ones) with a red eye. Detailed tier.
- **Anchor:** bottom-centre at the feet. Size about 260 x 520 (x -130..+130, y -520..0). Used at scale 0.5-1.4 and
  in flocks.
- **Shots:** s086-s090, s098-s100, s102.

### flamingo_chick (A, the creative director's nursery kicker)
- **What:** a lesser flamingo chick for the Natron kicker "the main nursery of the lesser flamingo" (s102). The CD
  wants this beat to land visually.
- **Look:** a fluffy **grey-white down** chick (not pink yet) with a straight, short, dark bill (chicks' bills aren't
  bent yet), stubby thick pinkish-grey legs, and a small dark eye. A round, downy silhouette. It should be appealing
  but documentary, not a cartoon mascot: no eyelashes and no smile.
- **Anchor:** bottom-centre. Size about 160 x 180. I place nine of them at scale 0.5 on two salt-crust islands.
- **Shots:** s102.

### flamingo_nest (B)
- **What:** a flamingo mud nest: a low truncated cone of dried mud with a shallow dip on top.
- **Look:** grey-brown mud cone, about 220 wide x 110 tall, with a few crack lines. Empty top (no egg).
- **Anchor:** bottom-centre.
- **Shots:** s089-s090, s102.

### jackal (C)
- **What:** the predator kept out by the caustic moat (s090), a black-backed jackal.
- **Look:** a slim dog-like canid facing right, with a ginger body, a black-and-silver saddle on the back, big ears and
  a bushy tail. Standing alert at the water's edge.
- **Anchor:** bottom-centre at the feet, about 400 x 280.
- **Shots:** s090 (with a red X over it).

### stone_bird (B) and stone_bat (C)
- **What:** the chalky, salt-preserved animals from Nick Brandt's photos. We never use his photos; this is our own
  cartoon stand-in.
- **Look:**
  - `stone_bird`: a small songbird shape perched **upright** on its feet, entirely chalky white-grey (`#d9d6cf`,
    shading `#b7b2a8`), with a slightly crusty texture made of spray dots. The eye is a closed grey line, never X eyes
    and never gore.
  - `stone_bat`: a chalky grey bat lying flat with its wings half spread, in the same colours.
- **Anchor:** `stone_bird` bottom-centre at the feet, about 220 x 300. I also use it rotated 80° lying on the shore.
  `stone_bat` is anchored at the centre, about 300 x 120.
- **Shots:** stone_bird s092-s097; stone_bat s094-s095.

### ammonia_bottle (C)
- **What:** a household ammonia bottle, the pH 11 comparison.
- **Look:** a plain white plastic jug-bottle with a blue cap and a blank blue label. **No brand.** About 160 x 380.
- **Anchor:** bottom-centre.
- **Shots:** s083.

## Antarctic Plateau

### research_hut (B)
- **What:** a small polar station hut for "Vostok Station".
- **Look:** a low box hut on short stilts, with orange-red walls, one small square window glowing yellow, a radio mast,
  snow drifts against the walls, and snow on the roof. No flags or text.
- **Anchor:** bottom-centre, about 520 x 300.
- **Shots:** s104, s107-s110, s114, s125-s128.

### sunscreen (C)
- **What:** a tube of sunscreen in Doug's front hand.
- **Look:** a white squeeze tube with an orange flip cap and a yellow sun symbol. No brand. About 70 x 180.
- **Anchor:** centre (where the hand grips).
- **Shots:** s125-s128.

### satellite (B)
- **What:** a generic Earth-observation satellite (used for the Antarctic ridge map and the NASA lightning sensor).
- **Look:** a gold-foil box body with two blue solar panel wings and a small dish or sensor pointing down. No logos.
- **Anchor:** centre, about 520 x 260.
- **Shots:** s115, s127-s128, s226.

## Everest Death Zone

### climber (B)
- **What:** a crude-tier mountaineer (Doug's tier, no red cap).
- **Look:** an orange down suit, a blue beanie, a backpack with a **yellow oxygen bottle** and a hose to a small face
  mask, and an ice axe in one hand. `"auto_ink": true`.
- **Anchor:** hips (feet +150), bbox about x -80..+80, y -320..+150.
- **Shots:** s136-s138 (tiny at 0.25 on the route, and at 0.6 for "bottled oxygen").

### helicopter (C)
- **What:** the helicopter that drops Doug on the summit.
- **Look:** a small red-and-white helicopter in side view facing right (I flip it), with the rotor as a long flat line
  and skids.
- **Anchor:** centre, about 600 x 260.
- **Shots:** s140.

## Cave of Crystals

### gypsum_crystal (A)
- **What:** one giant selenite (gypsum) crystal beam from Naica, reused many times and rotated to build the cave.
- **Look:** a long, faceted, translucent milky-white prism (`#f5f0d8`, face shading `#e2dcbf` and `#cfc8a8`), with
  long straight facets, squared or slightly pointed ends, a faint inner glow and a few white highlight streaks.
  It must read on a dark brown cave background.
- **Anchor:** centre. Size about 700 x 110 (x -350..+350, y -55..+55).
- **Shots:** s151, s153-s162, s167-s176 (Doug sits on it at s171-s174).

### humidity_meter (C)
- **What:** a dial hygrometer.
- **Look:** a round dial with a brass rim, a white face, a red needle pointed near the top end, and a small droplet icon
  on the face. No text other than optional 0 and 100.
- **Anchor:** centre, about 300 x 300.
- **Shots:** s161-s162.

### kitchen_timer (B)
- **What:** Doug's ten-minute kitchen timer.
- **Look:** a white round dial kitchen timer with a twist top and a red pointer. Optionally egg-shaped, about 220 x 220.
- **Anchor:** centre.
- **Shots:** s171-s174, s176.

## Dallol

### magnifying_glass (B)
- **What:** Doug's big magnifying glass.
- **Look:** a black handle and a round lens (r about 70) with a thick brass rim and a white glint.
- **Anchor:** **the handle end**, which is Doug's hand. The handle runs to the right and slightly up, and the lens
  centre is at about (+190,-60). Bbox about x 0..+270, y -140..+20.
- **Shots:** s199-s200.

### lemon (C)
- **What:** a lemon, the pH 2 comparison.
- **Look:** a yellow lemon with darker dimple dots and a small green leaf. About 220 x 150.
- **Anchor:** centre.
- **Shots:** s187-s190.

## Lake Nyos (sombre item: plain, factual drawings only)

### soda_bottle (C)
- **What:** "a sealed bottle of soda" (dissolved CO2 under pressure).
- **Look:** a clear green plastic soda bottle with the cap on and small bubbles inside. No label or brand.
  About 140 x 380.
- **Anchor:** centre.
- **Shots:** s208.

### degassing_raft (B)
- **What:** the Lake Nyos degassing pipe: a small floating raft with a vertical pipe that sends up a fountain of water.
- **Look:** a small grey-and-orange raft platform (about 360 wide) floating at the waterline, with a thin vertical pipe
  rising to a **white water-and-gas fountain plume** about 200 tall. Only a short pipe stub shows below the waterline
  (to y +60), because the lake is drawn small.
- **Anchor:** the waterline centre. Bbox about x -180..+180, y -260..+60.
- **Shots:** s215-s216 (scale 0.8), s222 (0.35).

## Lake Maracaibo

### storm_cloud (A)
- **What:** a towering night thunderstorm cloud over the lake (Catatumbo lightning).
- **Look:** a dark slate-purple cumulonimbus (`#3a3a55`, lighter tops `#5a5a7a`), lumpy with a flat-ish base and an
  inner glow spray in pale yellow where lightning lights it. I draw the bolts separately, so draw no bolts.
- **Anchor:** centre, about 700 x 300.
- **Shots:** s223, s225, s230, s232-s238, s240-s244.

### fishing_rod (B)
- **What:** Doug's long fishing rod, held up into the storm.
- **Look:** a thin rod with a cork grip and a small reel. The rod runs up and to the right to its tip at about
  (+340,-480), and a fishing line hangs from the tip down to the water at about (+360,-60).
- **Anchor:** **the grip**, which is Doug's hand in the `sit` pose. Bbox about x -30..+360, y -490..+80. Keep it a
  thin line drawing, since it sits in front of Doug.
- **Shots:** s237-s244.

### water_bottle (C, Death Valley)
- **What:** Doug's one small water bottle.
- **Look:** a small clear plastic bottle with a blue cap and a little water inside, about 50 x 120.
- **Anchor:** the grip centre (Doug's front hand). It is drawn upside down and empty at s022.
- **Shots:** s011, s022.
