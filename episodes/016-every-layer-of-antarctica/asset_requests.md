# 016 Every Layer of Antarctica: asset requests (director, 2026-10-12)

All placements in `shotlist.json` assume the **anchor, size and facing given here**, so please keep them (or tell me
and I will move the shots). House style as `anglerfish.json`: thick black outlines, flat fills, simple silhouettes that
read at thumbnail size. Creatures and places are the detailed tier; crude-tier humans set `auto_ink`.
Scenes run on the episode's **ICE ABOVE DOUG ramp**: pale ice `#e6f2f9` (item 1) darkening every item to near-black
`#0b0d16` (Denman). Water under the ice follows a darker ramp (`#1b4f86` at Thwaites to `#050a1f` at Denman). Anything
used on the dark items (ice_fish, sponge_boulder, tardigrade, frozen_doug_*) needs mid-tone fills, not near-black.

No penguins, seals or cute wildlife. Doug's design is locked; the three frozen-Doug blocks are props (see notes).

## Recurring props

### hot_water_drill
- What: the hot-water drilling rig that lowers Doug down every borehole (the episode's "rope rig").
- Look: an A-frame / tripod derrick of grey steel struts (legs at about x -170 and +170 at the ground), a pulley wheel at
  the apex, an orange hose reel drum and a small boxy **boiler/heater unit** (orange-red with a stubby chimney) standing
  to the right of the derrick (x +200..+420, y -220..0). Snow drifts at the feet. No text, no flags.
- **The centre column x -30..+30 must stay empty** (the rope and the hole are drawn there by the scene).
- Anchor bottom-centre = the borehole mouth (0,0). Pulley at **(0,-620)**. Bbox about x -200..+420, y -640..0. Faces right.
- Sizes: 0.9 (surface close-ups), 0.3-0.32 (cross-sections), 0.15 (Ellsworth column).
- Shots: s002-s003, s004-s005, s066-s068, s083-s084, s105-s110, s124, s131-s138, s154, s158, s202, s205-s218 (camp, boiler
  gets a red X in s210), s224, s232-s245, s272 (49 shots).
- **Done** (illustrator, 2026-10-12): assets/previews/016-assets-props.png, in context assets/previews/016-assets-context.png

### ice_cube_icon
- What: the icon for the episode-only **ICE ABOVE DOUG** meter (like 015's shovel icon).
- Look: one pale-blue ice cube in 3/4 view, white highlight on the top face, darker side face, thick black outline.
  Must read at 32 px.
- Anchor centre, about 200x200. Used at scale 0.16 at (1366, 238) on every shot (s002-s274).
- **Done** (illustrator, 2026-10-12): assets/previews/016-assets-props.png (checked at 0.16 on dark in 016-assets-context.png)

### rope_hook
- What: the empty end of Doug's rope: a steel carabiner/hook.
- Look: grey steel snap-hook with a darker gate line, a small ring at the top where the rope ties on.
- Anchor = the tie-on point at the top (0,0); hook hangs down to about y +130; about 70 wide. The red cap (`doug_cap`)
  hangs from the hook's lower curve in s272, so leave the lower bend open.
- Shots: s270 (drops into the canyon), s271 (snags the cap), s272 (closing: the rope comes up with only the cap).
- **Done** (illustrator, 2026-10-12): assets/previews/016-assets-props.png, cap hang check in 016-assets-context.png

## Travel stickers (places playlist, art-director-owned series lore)
Same family as `sticker_crevasse` / `sticker_la_brea`: about 112x60, anchor centre, slightly peeling corner, bold caps
text legible at scale 0.2-0.3 on the suitcase and at 1.6 on the closing card. Two-line names may widen to ~130x64.

| name | text | look |
|---|---|---|
| `sticker_blood_falls` | BLOOD FALLS | white glacier stamp with a rust-red drip down the middle (rust, not blood: orange-red, no splatter) |
| `sticker_thwaites` | THWAITES | pale-blue pennant, small ice cliff with a dark slot cut up into its underside |
| `sticker_ross_ice_shelf` | ROSS ICE SHELF | flat white shelf over a dark-blue band, tiny pale fish |
| `sticker_filchner_ronne` | FILCHNER-RONNE | navy oval, small cream sponge vase on a grey rock |
| `sticker_mercer_lake` | MERCER LAKE | glacier-blue rectangle, a tiny tan shell (ostracod) |
| `sticker_west_antarctic_rift` | WEST ANTARCTIC RIFT | cobalt shield, small dark cone with an orange glow under a white lid |
| `sticker_lake_ellsworth` | LAKE ELLSWORTH | deep-navy rectangle, a thin vertical borehole line with a white X |
| `sticker_vostok` | VOSTOK | near-black oval with a blue water splash shooting up |
| `sticker_denman` | DENMAN | black stamp with one faint red stripe and a deep V canyon |

Shots: each appears on its death shot (BF s026, TH s080, FISH s102, SPONGE s151, MERCER s175, VOLCANOES s199,
ELLSWORTH s219, VOSTOK s244, DENMAN s269) and then on every later suitcase, all nine on the closing card s273-s274.
- **Done** (illustrator, 2026-10-12): all nine drawn, assets/previews/016-assets-stickers.png

## Blood Falls

### taylor_glacier_front
- What: the front face of Taylor Glacier, McMurdo Dry Valleys.
- Look: wide white-to-pale-blue ice cliff with a fairly flat top edge, vertical striations and blue shading in the cracks,
  sitting on brown valley floor. **Leave the central face (x -150..+150, y -330..0) plain** for the stain overlay.
- Anchor bottom-centre, about 1200x480 (x -600..600, y -480..0). Scale 1.0. Shots s008-s011, s023-s026.
- **Done** (illustrator, 2026-10-12): assets/previews/016-assets-bloodfalls.png, with stain in 016-assets-bloodfalls-scene.png (ground runs to y +64)

### blood_falls_stain
- What: the "blood" fall itself as an overlay that pops onto `taylor_glacier_front` (same anchor and scale).
- Look: a rust-orange (`#c8501e`) to deep iron-red (`#8a1a10`) stain pouring from a crack at (0,-330) down the face,
  darker streaks, fanning out on the ground at the base (x -240..+240, y -20..+40) into a frozen orange-red apron.
  It must read as **rust**, not gore: matte, iron-oxide orange-red, no splatter, no droplets.
- Anchor bottom-centre (same point as the glacier). Shots s009-s011, s023-s026.
- **Done** (illustrator, 2026-10-12): assets/previews/016-assets-bloodfalls-scene.png

### five_story_building
- What: a plain five-storey block for the "about five storeys high" scale beat (same family as `six_story_building`).
- Exactly five rows of four blue windows, flat roof. Anchor bottom-centre, 312x500. Scale 0.66 in s009.
- **Done** (illustrator, 2026-10-12): assets/previews/016-assets-bloodfalls.png

### rusty_nail
- What: an old iron nail left out in the rain (the rust simile).
- Look: horizontal nail, flat head at the left, point at the right, grey steel with patchy orange-brown rust and flakes.
- Anchor centre, about 380x90. Scale 1.4 in s014.
- **Done** (illustrator, 2026-10-12): assets/previews/016-assets-bloodfalls.png

### ice_chunk
- What: an opaque block of glacier ice that falls on Doug (Blood Falls s025-s026, Thwaites s080).
- Look: irregular, solid (NOT outline-only like `ice_block`): white-blue faces `#e9f4fb`, `#bcd8ec` shaded side,
  a few cracks, flat bottom. Doug's legs stick out from under it; the cap sits on top in s026.
- Anchor bottom-centre, about 420x300. Scales 0.6-0.7.
- **Done** (illustrator, 2026-10-12): assets/previews/016-assets-bloodfalls.png

## Erebus Ice Caves

### mount_erebus
- **Done** (illustrator, 2026-10-12): preview `assets/previews/016-erebus-assets.png`.
- What: Mount Erebus, Ross Island: Earth's southernmost active volcano.
- Look: broad snow-white volcano with dark rock streaks and ridges, a summit crater with a faint orange glow and a soft
  steam plume (inside the bbox), a few small knobs on the upper slopes. Not the generic grey `volcano`: this one is
  mostly snow.
- Anchor bottom-centre, about 1400x640. Scale 1.0. Shots s030, s037, s045.

### ice_chimney
- **Done** (illustrator, 2026-10-12): preview `assets/previews/016-erebus-assets-b.png`.
- What: a hollow fumarolic ice tower on Erebus's slopes.
- Look: rough white/pale-blue chimney, slightly bulging, open dark top, frosted texture. Steam is sprayed by the scene.
- Anchor bottom-centre, about 140x260. Scales 0.4-0.5. Shots s036, s037, s045.

### tshirt_hanger
- **Done** (illustrator, 2026-10-12): preview `assets/previews/016-erebus-assets-b.png`.
- What: a plain light-blue T-shirt on a wire coat hanger ("comfortable in a T-shirt").
- Anchor centre, about 260x280, hook at the top. Scale 0.9 in s043.

### folded_jacket
- **Done** (illustrator, 2026-10-12): preview `assets/previews/016-erebus-assets-b.png`.
- What: Doug's jacket folded into a pillow (survival beat, Erebus).
- Look: dark-blue puffer jacket folded into a neat oblong with a sleeve tucked in, quilt seams.
- Anchor bottom-centre, about 200x70. Scales 0.7-0.8. Shots s053-s057 (Doug's head rests on it in s054-s057).

### tardigrade
- **Done** (illustrator, 2026-10-12): preview `assets/previews/016-erebus-assets-b.png`.
- What: a tardigrade (water bear). Used for Erebus DNA traces (s049-s052) and the Mercer microscope (s162-s168).
- Look: plump segmented pale tan-pink body, eight stubby legs with tiny claws, small round mouth tube, two dot eye
  spots. Documentary-cartoon, not cute. Clean outline: it is also used as a **silhouette with a red rim** (s162).
- Anchor centre, facing right, about 300x180. Scales 0.25-0.9.

## Thwaites From Below

### manhattan_outline
- **Done** (illustrator, 2026-10-12): preview `assets/previews/016-thwaites-fish-assets.png`.
- What: Manhattan island for the "two thirds of the area of Manhattan" comparison.
- Look: the island outline, flat green `#6cbf5a` with dark green outline (world_map style), long and narrow, upright.
- Anchor centre, about 220x720. Scale 0.9 in s062.

### icefin_robot
- **Done** (illustrator, 2026-10-12): preview `assets/previews/016-thwaites-fish-assets.png`.
- What: Icefin, the long narrow under-ice robot lowered through the Thwaites borehole.
- Look: long yellow cylinder with a rounded nose at the right, a red stripe, small fins at the tail, a camera window and
  a light at the nose. No text.
- Anchor centre, horizontal, about 500x70. Used rotated 90 in s067-s068 and level in s069.

## The Fish Under the Ice

### ice_fish
- **Done** (illustrator, 2026-10-12): preview `assets/previews/016-thwaites-fish-assets.png`.
- What: the pale, see-through fish (about 20 cm) filmed under the Ross Ice Shelf grounding zone in 2015.
- Look: slim translucent whitish-pink `#f1e6e6` body, faint visible spine and pale fins, big dark eye, slight blue
  shading on the back. Mid-tone, so it reads on dark navy water. Clean outline for the **silhouette with red rim** reveal
  (s091-s092).
- Anchor centre, facing right (scenes flip it), about 300x110. Scales 0.45-1.3. Shots s091-s103.

### diving_platform
- **Done** (illustrator, 2026-10-12): preview `assets/previews/016-thwaites-fish-assets.png`.
- What: an Olympic 10 m high-diving tower (scale for the 10 m water gap).
- Look: grey concrete tower with a ladder, the top board at y -700 sticking out to the right to about x +200.
- Anchor bottom-centre, about 420x700. Scale 0.514 in s088 (its top board touches the ice ceiling).

### teaspoon
- **Done** (illustrator, 2026-10-12): preview `assets/previews/016-thwaites-fish-assets.png`.
- What: a silver teaspoon holding lake water.
- Look: horizontal, handle left, bowl right with a pale-blue pool of water; bowl centre at **(+110, 0)**, radius ~55.
- Anchor centre, about 360x100. Scale 2.2 in s118-s119 (a magnifying glass sits over the bowl).

## The Sponge Boulder

### sponge_boulder
- **Done** (illustrator, 2026-10-12): preview `assets/previews/016-sponge-assets.png`.
- What: the seabed boulder under the Filchner-Ronne Ice Shelf covered in sponges and stalked animals (BAS 2021).
- Look: lumpy grey-brown boulder with several cream/pale-yellow vase sponges, thin stalked animals with pale heads, small
  white specks. Mid-tone (reads on `#153f6a`). Clean outer outline: it is a **silhouette with red rim** first (s133-s135).
- Anchor bottom-centre, about 700x420. Scales 0.45-1.3. Shots s133-s151.

### fridge
- **Done** (illustrator, 2026-10-12): preview `assets/previews/016-sponge-assets.png`.
- What: a plain white kitchen fridge ("colder than the inside of a refrigerator").
- Anchor bottom-centre, about 300x560. Scale 1.0 in s140.

### frozen_doug_seated (death 134)
- **Done** (illustrator, 2026-10-12): preview `assets/previews/016-sponge-assets.png`.
- What: Doug frozen while sitting still next to the boulder. CD note: **squat seated block with frost**.
- Look: an opaque, rounded, squat ice block (`#bfe0f0` with `#8fc2e0` shading) heavily crusted with white frost on
  top and sides. Inside, only a pale cartoon shape: a round head outline with **X eyes** and an open O mouth, two pale
  seated-leg lines. Not a visible body.
- Anchor bottom-centre, about 380x420; flat top ledge at (0,-420) where the scene puts `doug_cap`. Scale 0.8 in s151.

## Mercer Subglacial Lake

### microscope
- **Done** (illustrator, 2026-10-12): preview `assets/previews/016-assets-mercer-volcanoes-ellsworth.png`.
- What: a classic lab microscope (white/grey body, black eyepiece, stage with a slide).
- Anchor bottom-centre, about 260x420. Scale 1.2 in s159, s164.

### poppy_seed
- **Done** (illustrator, 2026-10-12): preview `assets/previews/016-assets-mercer-volcanoes-ellsworth.png`.
- What: one poppy seed drawn big for the size comparison: dark blue-grey kidney shape with a fine net texture.
- Anchor centre, about 120x100. Scale 0.8 in s161-s163.

### clipboard
- **Done** (illustrator, 2026-10-12): preview `assets/previews/016-assets-mercer-volcanoes-ellsworth.png`.
- What: Doug's clipboard: brown board, silver clip, white sheet with scribbled lines.
- Anchor centre, about 120x170. Scale 0.5 in s173-s175 (drifts up, rotated 25, after the death).

## Volcanoes Under the Ice

### mount_fuji
- **Done** (illustrator, 2026-10-12): preview `assets/previews/016-assets-mercer-volcanoes-ellsworth.png`.
- What: Mount Fuji silhouette for the "about the height of Mount Fuji" comparison.
- Look: the classic symmetric cone, blue-grey with a white snow cap and streaks.
- Anchor bottom-centre, about 900x420. Scale 0.95 in s186-s187.

### meltwater_wave (death 136)
- **Done** (illustrator, 2026-10-12): preview `assets/previews/016-assets-mercer-volcanoes-ellsworth.png`.
- What: a cartoon wave of meltwater that sweeps Doug away.
- Look: same shape as `mud_wave` (curling crest at top right, rolling right) but water colours: pale blue-white crest,
  blue body `#3a9ad9` with darker swirls, white foam. No bodies (Doug's legs are drawn by the scene).
- Anchor bottom-centre, about 910x440. Scale 1.2 in s199.

## Lake Ellsworth

### snowcat
- **Done** (illustrator, 2026-10-12): preview `assets/previews/016-assets-ellsworth-vostok-denman.png`.
- What: the drill crew's tracked polar vehicle towing a loaded sledge.
- Look: orange tracked snowcat with a boxy cab and windows, facing right, towing a low wooden sledge with lashed crates
  to the left.
- Anchor bottom-centre, about 700x300. Scales 0.22 (driving away on the surface) and 0.5 (camp). Shots s205-s218.

### fuel_drum
- **Done** (illustrator, 2026-10-12): preview `assets/previews/016-assets-mercer-volcanoes-ellsworth.png`.
- What: an empty fuel drum (the attempt ran out of fuel).
- Look: blue-grey steel drum with a red band and rolling hoops, bung on top, a dent. No text.
- Anchor bottom-centre, about 160x230. Scale 0.6 in s213.

### frozen_doug_column (death 137)
- **Done** (illustrator, 2026-10-12): preview `assets/previews/016-assets-ellsworth-vostok-denman.png`.
- What: Doug sealed in the borehole as it froze shut. CD note: **tall thin column inside the borehole walls**.
- Look: a tall narrow cylinder of clear-blue ice with vertical streaks and borehole-wall ridges. Inside near the top, a
  pale cartoon head outline with **X eyes**, one arm line raised (he was waving up). Not a visible body.
- Anchor bottom-centre, about 150x700; top at (0,-700) where the cap sits. Scale 0.5 in s219, s221.

## Lake Vostok

### lake_vostok_outline / lake_ontario_outline
- **Done** (illustrator, 2026-10-12): preview `assets/previews/016-assets-ellsworth-vostok-denman.png`.
- What: top-down outlines for "roughly the size of Lake Ontario". **Same km scale for both** (about 2.5 units per km).
- `lake_vostok_outline`: elongated lake, about 575x125 (230 x 50 km), laid horizontally, fill `#1b3f73` with a lighter rim.
- `lake_ontario_outline`: Ontario's shape, about 780x210, **outline only** in a dashed or solid orange-red line so it reads
  laid over Vostok.
- Anchor centre (both). Scale 1.4 in s225-s226.

### frozen_doug_wave (death 138)
- **Done** (illustrator, 2026-10-12): preview `assets/previews/016-assets-ellsworth-vostok-denman.png`.
- What: Doug lifted by the surging lake water and frozen mid-wave. CD note: **a splashing wave shape frozen mid-surge**;
  must not echo 012's amber "preserved" bead.
- Look: a narrow base widening up into a curling, splashing crest of glassy blue-white ice with frozen droplets around
  it. A pale cartoon head with **X eyes** inside the crest at about (0,-520). Not a visible body.
- Anchor bottom-centre, about 520x700; top centre at about (-20,-700) where the cap sits. Scales 0.6 (s244) and 0.3 (s245).

## The Deepest Point on Land

### flag_doug_was_here
- **Done** (illustrator, 2026-10-12): preview `assets/previews/016-assets-ellsworth-vostok-denman.png`.
- What: the small flag Doug plants on the Denman canyon floor.
- Look: thin grey pole from (0,0) up to (0,-300) with a red tip, a white cloth flag from x 0..+200, y -300..-190, with
  hand-lettered black "DOUG WAS HERE" in two lines (keep the text upright; the asset is never rotated).
- Anchor = the pole base on the ground. Scale 0.8 in s267-s268.

## Notes for the art director
- Frozen deaths 134/137/138 are props over a hidden Doug: `doug_cap` sits on top of each (squat block, tall column,
  wave crest), and the counter ticks on them. Doug's X-eyes face shows faintly through opaque ice; no living expression,
  so they are not the 012 "preserved" variant.
- Death 131 and 132 show Doug's legs out from under `ice_chunk` (on_back, dead); 131 has the cap on top of the block,
  132 has the cap floating up against the ice ceiling. 133 is on_back between the lowered ice and the seabed with
  `cap_off`. 135 is on_back on the Mercer lake floor with a ghost. 136 shows legs out of the meltwater wave and the cap
  spinning above it. 139 is the cap alone on the canyon floor; s270-s271 then drop the empty rope hook onto it, so the
  closing rope (s272) comes up with the cap (CD note 2).
- No 012 crevasse callback anywhere; the only callback is the 004 inset in s023 (`sticker_antarctica`).
