# 020 Deeper Underground: asset requests (director, 2026-10-16)

All placements in `shotlist.json` assume the **anchor, size and facing given here**. If you have to change one, tell me
and I will move the shots. House style follows `anglerfish.json`: thick black outlines, flat fills, and simple silhouettes that
read at thumbnail size. Creatures, places and machines are the detailed tier. Crude-tier humans set `auto_ink`.

The scene backgrounds use the 015 rock-strata ramp, one step darker per item (`#d9b77a` Movile to `#2a2a2e` Hidden Ocean). After that
the core items turn hot: lava `#ff5a1f`/`#ffb000` for the Outer Core and white-hot `#fff3c0` for the Inner Core. Cavities and tunnels
are the shaft cream `#f1e4c6`. Anything shown on the dark items (drill pod, stickers) needs mid-tone fills, not near-black.
No game references, nothing cute (brief section 7).

## Episode devices (art director approval: brief + decisions.md)

### earth_cross_section (recurring, reusable for any into-the-planet episode)
- What: a crude cutaway Earth shown between items. The scene draws the red "Doug" dot on top of it.
- Look: a full-disc slice through the planet with concentric layers. **Exact radii (fraction of the outer radius), because the dot
  positions depend on them:**
  - Crust: a thin brown rim `#8e4a2c`, about 8 units, with a thin green/blue surface line on the outside.
  - Mantle: down to 0.546, a red-brown to orange gradient (`#a65a32` outside, `#c0602a` inside), stepped bands are fine.
  - Transition zone: a faint darker band between 0.896 and 0.936. It must stay subtle, because the scene draws dashed rings on it.
  - Outer core: from 0.546 to 0.19, orange `#ff8a1f` with a few yellow swirl strokes.
  - Inner core: radius 0.19, white-hot `#fff3c0` with a yellow `#ffe24a` glow ring.
  - Black outline 6. No labels and no text.
- Anchor: the centre. Radius **exactly 400 units** at scale 1 (800 wide).
- Sizes: 0.18-0.3 (insets on title cards and the closing), 0.95-1.15 (opener, Kola, the "Nobody." titles), and 2.4-2.6 (only the top arc
  shows: s235-s255 transition zone, s258 core-mantle boundary). At 2.6 the layer edges must still look clean.
- Shots: s002-s005, every title card inset, s154, s201-s203, s214, s234-s236, s240, s242, s245-s246, s255, s257-s258, s262-s273,
  s276, s278, s280, s282-s283, s294-s297, s306-s308 (49 shots).

### depth_icon
- What: the icon for the episode-only **DOUG DEPTH** meter (like 015's shovel and 016's ice cube).
- Look: a small square of brown rock strata (3 bands) with a red down-arrow over it and a thick black outline. It must read at 32 px.
- Anchor: the centre, about 200x200. Used at scale 0.16 at (1366, 238) on every shot from s002 on.

### drill_pod / drill_pod_open / drill_pod_melted (new recurring vehicle, art director owns the design)
- What: Doug's crude MS Paint capsule for "Nobody." It is dry and industrial, **not a cute vehicle**.
- `drill_pod` (closed): an upright riveted steel capsule, mid-grey `#8d9096` with darker `#5a5f66` bands. It has one round porthole
  (dark glass with a white glint, centred at (0,-120), r 70) and a stubby exhaust on top. A grey conical nose drill points **down**, with
  spiral grooves.
  - Body x -160..+160, y -280..+200. Drill cone y +200..+360, tip at (0,+360).
  - Anchor: the body centre (0,0). Shots: s229 (0.7), s230 (0.45).
- `drill_pod_open`: the same pod with the front hatch swung open to the right. The hatch door hangs at x +160..+330 and keeps the
  porthole on it. Through the opening (x -180..+180, y -220..+130) you see a mid-grey `#8d9096` interior with a flat floor at y +130.
  - Doug is drawn inside by the scene, so keep the opening completely empty: upright at hip y +35 and scale 0.6, or `on_back` on
    the floor.
  - Please widen the body to x -220..+220 for this variant so the opening fits.
  - Anchor: the body centre. Shots: s231-s233 (0.9), s251-s254 and s274-s276 (1.0).
- `drill_pod_melted`: the pod sagged into a cartoon blob of grey metal in an orange puddle. There is a drooping porthole, the drill
  tip sticks out sideways, and there are a few bubbles. No body and no face. Anchor: bottom-centre, about 500x260. Shot: s277 (1.0).

### again_stamp
- What: the narrator's red rubber-stamp mark "AGAIN" (new series lore, brief and series bible).
- Look: red `#e0201b` rectangle outline with slightly rough ink edges and bold caps "AGAIN", tilted about -8 degrees, with a little
  ink speckle. About 120x50 at scale 1 (the same scale family as the stickers).
- Anchor: the centre. It sits over the 5th suitcase slot (local +14,+6 from it), from s183 to s308. The shotlist uses suitcase
  scales 0.165-0.32, and 1.5 on the closing card.

## Travel stickers (same family as `sticker_naica`, `sticker_vostok`; about 112x60, anchor centre, peeling corner)
| name | text | look |
|---|---|---|
| `sticker_movile_cave` | MOVILE CAVE | dark cave oval, a cream scum line on a green lake |
| `sticker_lechuguilla` | LECHUGUILLA | tan desert rectangle with a white gypsum chandelier |
| `sticker_veryovkina` | VERYOVKINA | grey limestone shield with a blue water drop |
| `sticker_mponeng` | MPONENG | gold-yellow stamp with a small mine headframe (used twice) |
| `sticker_the_moho` | THE MOHO | brown-over-red split band with a wavy black line |
| `sticker_hidden_ocean` | HIDDEN OCEAN | dark rock rectangle with a small green crystal and a blue drop |
| `sticker_outer_core` | OUTER CORE | orange circle with yellow swirls |
| `sticker_the_center` | THE CENTER | white-hot round badge (en-US spelling, CD gate) |

Each sticker appears on its death shot (s031, s058, s106, s157, s183, s231, s254, s277, s303) and then on every later suitcase.
All nine show on the closing card s307-s308 at scale 1.5.

## Creatures
### cave_centipede
- What: the "king of the cave", *Cryptops anophthalmus*, the eyeless Movile centipede.
- Look: a long, flat, pale **yellowish-cream** body `#e8d9a0`, darker `#c9b070` segment edges, about 21 segments and one pair of
  legs per segment. There are long antennae, curved forcipules at the head, and **no eyes**. It is creepy but clean, with no gore.
- Facing: right. Anchor: the centre, about 500x160 at scale 1.
- It also renders as a `silhouette` (s027, red glow, `glow_r` 330), so make the outline read as "centipede" in solid black.
- Shots: s016, s022, s025-s033 (0.4-1.3). It is the `tease_asset` for short01.

### devil_worm
- What: *Halicephalobus mephisto*, a nematode about 0.5 mm long.
- Look: a translucent pale-pink `#f2c8c0` slender worm in a gentle S, with a darker gut line, a tapered tail and a blunt head. Draw it
  as a scientific drawing, not a cartoon face.
- Facing: right. Anchor: the centre, **400 units long** at scale 1 (scale 0.5 = 0.5 mm against the credit card in s079-s080).
- Shots: s078 (silhouette, 3.2, fills the frame) and s079-s080 (0.5).

## Places, machines, props
| name | what / look | anchor, size | shots |
|---|---|---|---|
| `mine_headframe` | steel lattice A-frame mine headframe, grey `#8d9096`, two big sheave wheels on top, cable down the middle. **Keep centre column x -25..+25 empty** (the shaft is drawn there) | bottom-centre = shaft mouth; 340 wide x 520 tall | s062-s075, s111-s112, s123, s137, s160-s169, s176-s178 (0.55-0.7) |
| `mine_cage` | open steel lift cage, two decks, packed with 6-8 crude-tier miners in yellow hard hats (identical heads), mesh sides | centre; 300x420 | s164 (0.22), s165-s167 (1.0, Doug is drawn beside it), s168 (0.2) |
| `mine_fan` | big industrial ventilation fan in a square steel frame, grey blades | bottom-centre; 300x300 | s178-s180 |
| `drilling_rig` | small land drilling derrick (Movile 1986 / Kola): steel lattice tower with crown block, tiny cabin, pipe rack; **centre column x -15..+15 empty** | bottom-centre on the ground; 360 wide x 600 tall | s009-s010 (0.45), s187-s199 (0.3-0.4) |
| `borehole_cap` | the Kola hole today: small rusty round steel cap welded shut and bolted to a concrete slab, rust streaks `#b0521a` | bottom-centre; 260x110 | s206-s211 (0.6) |
| `gypsum_chandelier` | Lechuguilla gypsum chandelier: cluster of white/cream branching crystal blades hanging from the ceiling, faint glints | **top-centre = ceiling attachment**; 260 wide x **660 tall** (= 6 m next to Doug at 0.45) | s043-s044, s050, s055 (0.6-1.0) |
| `gypsum_cluster` | low cluster of white gypsum crystals on the floor, flat-ish top at (0,-170) for the cap | bottom-centre; **at least 240 wide** (it covers Doug's knocked-off cap) x 180 | s058, s060 (0.6) |
| `juina_diamond` | small dull brown, scruffy rough diamond (not sparkly), with one tiny bright green speck (ringwoodite) at local (+20,-10) | centre; 220x200 | s237-s241, s245 |
| `rug` | small worn rectangular rug in perspective, faded red with a cream border and fringe | bottom-centre lying flat; 360x70 | s155-s159 (0.8) |
| `houseplant` | potted houseplant: terracotta pot, broad green leaves, top leaf flat at y -300 (the cap sits there) | bottom-centre; **pot at least 180 wide** (it covers the cap on the ground), 300 tall | s155-s159 (0.8) |
| `water_glass` | plain tumbler of slightly cloudy grey-brown water (it is brine, not clear tap water) | centre; 110x170 | s120-s122, s130, s133 |
| `water_glass_empty` | same tumbler, empty, a few drops left | centre | s131 |
| `antibiotic_capsule` | plain two-tone capsule (white and blue), no text | centre; 160x70 | s052-s054 |
| `compass` | round brass pocket compass with a red-and-white needle | centre; 160x160 | s274-s276 (0.35) |
| `stretcher` | rescue stretcher (orange basket litter), empty, plain; it is used on a sober card so keep it neutral | centre; 420x140 | s048-s049 (0.9) |
| `burj_khalifa` | Burj Khalifa silhouette in steel-blue-grey, stepped spire | bottom-centre; **exactly 600 tall** so copies stack | s089 (x3, 0.49) |

## Crude-tier human
### scientist_woman
- What: a crude-tier stick-figure researcher (Doug's tier, 5 px lines, big round head with a grey crescent), with no cap, longer dark
  hair, round glasses and a white lab coat. Neutral face, `auto_ink`.
- It stands in for Barbara Sherwood Lollar and Inge Lehmann, so it is generic, not a likeness.
- Anchor: the hips (0,0), feet at +150, facing right. Same proportions as `scientist`.
- Shots: s113, s116-s123, s131, s281, s295, s298-s299 (0.38-1.0).

## Reused from the library (no action)
`world_map`, `south_africa_map`, `north_america_map`, `travel_suitcase`, `doug_cap`, `cave_spider`, `sandwich`, `heart_icon`, `microbe`,
`worm_icon`, `scientist`, `caver`, `eiffel_tower`, `mount_everest`, `tent`, `storm_cloud`, `phone`, `water_splash`, `magnifying_glass`,
`vial`, `bucket`, `doormat`, `library_book`, `angry_sun`, `thermometer`, `humidity_meter`, `hot_tub`, `factory`, `ice_chunk`,
`deck_chair`, `gypsum_crystal`, `sticker_naica`, `sticker_denman`, `speedometer`, `loudspeaker`, `dinner_plate`, `bank_card`,
`narrator_hand`, `research_ship`, `dollar_bill`, `journal_paper`, `clipboard`, `volcano`, `balance_scale`, `water_bottle`, `snorkel`,
`snorkel_gear`, `house`, `kitchen_chair`, `flag_doug_was_here`, `finish_banner`, `microscope`, plus the annotations.

## Illustrator status (2026-10-16): all done
Every request above is drawn in `assets/library/` with the anchor and size asked for, unless a note below says otherwise.
Previews are in `assets/previews/`: `020-gated-a.png` (earth_cross_section, drill_pod, drill_pod_open, drill_pod_melted),
`020-gated-b.png` (depth_icon, again_stamp), `020-gated-context.png` (Earth at 2.6 and 0.2, the open pod with Doug at hip +35 and scale 0.6,
the meter icon at 0.16, the stamp on the suitcase, all on dark strata), `020-stickers.png`, `020-context-c.png` (all nine stickers + AGAIN on
the suitcase), `020-assets-a.png`, `020-assets-b.png`, `020-context-b.png` (tall assets in full, centipede silhouette with glow_r 330, dark-cave checks).

- [x] earth_cross_section: the radii are exact (outer 400; 0.936/0.896 transition band; 0.546; 0.19). Wobble is damped on the rings so edges stay clean at 2.6. **Needs art-director approval.**
- [x] depth_icon. **Needs art-director approval.**
- [x] drill_pod / drill_pod_open / drill_pod_melted: the open hatch door spans x +186..+330 (hinged just outside the x 180 opening). The opening is completely empty and the floor is at y 130. The melted pod is ~500x280, anchored bottom-centre. **Needs art-director approval.**
- [x] again_stamp: the letters are drawn as strokes so the whole stamp tilts -8 degrees (engine text cannot rotate). **Needs art-director approval.**
- [x] sticker_movile_cave, sticker_lechuguilla, sticker_veryovkina, sticker_mponeng, sticker_the_moho, sticker_hidden_ocean: about 112x60.
- [x] sticker_outer_core, sticker_the_center: round badges r 38 with two-line text (THE CENTER has a ray ring out to r 50).
- [x] cave_centipede: about 560x200 including the antennae and trailing last legs; no eyes. Silhouette checked.
- [x] devil_worm: exactly 400 long.
- [x] mine_headframe: x -25..+25 is empty for the full height. The hoist cables drop at x +-32, just outside the column rather than down the exact middle. 360x520.
- [x] mine_cage (7 miners), mine_fan, drilling_rig (x -15..+15 empty below the crown block), borehole_cap
- [x] gypsum_chandelier (top-centre anchor, 660 tall), gypsum_cluster (flat top at y -170, about 60 wide; 300 wide)
- [x] juina_diamond (green speck at +20,-10), rug, houseplant (pot 184 wide, rim 204; flat top leaf at y -300)
- [x] water_glass, water_glass_empty, antibiotic_capsule, compass, stretcher, burj_khalifa (exactly 600 tall; stacking checked)
- [x] scientist_woman (`auto_ink`, built from `scientist`)

### Art-review revisions (2026-10-16): done, back to the art director
Previews: `assets/previews/020-revise.png` (standard tiles) and `assets/previews/020-revise-zoom.png` (full size, on white and on dark rock, plus a 168 px tile).
Each asset keeps its anchor and its size. Checked in context in s062, s164, s206, s157 and s048.
- [x] mine_headframe: one full-width steel sheave deck (`#5a5f66`, outline 4, y -472..-450) ties both legs together, and both wheels sit on it on bearing blocks. A light lattice cross-brace runs between the legs from y -310 to -452 only. The inner legs are centred at x +-35, so their inner edges are at about +-30 and the empty column is about 60 wide. The hoist ropes are black, width 4. **Deviation:** they drop at x +-14 from the inner wheel rims, not at x +-32. At +-32 they sat on the legs' black outline and could not be seen (the original fault). At +-14 they fall into the shaft mouth, which the shots draw +-31 to +-40 local wide. The column below y -300 contains only the two ropes. In s164 the cage hangs between them.
- [x] borehole_cap: steel `#6a6e75` / `#4f535a` with rust patches and streaks (`#b0521a` / `#c86a2a`). The flat top plate is light grey with an irregular `#3f4349` zigzag weld bead (width 3). The knob and the lid dots are gone. Light-grey hex bolts (`#a8acb2`, outline 2) sit on the flange only. The cylinder is 25 tall. I made the flange narrower (rx 64) so it doesn't read as a hat brim. The slab and its rust streaks are kept. The cap is now about 260x80 because the cylinder is lower.
- [x] houseplant: the top leaf is a side-view lens with a pointed tip on the right, a `#2e8b3a` midrib with side veins and a darker underside crescent. Its top edge is flat at y -300 from x -66 to +84 (150 wide). The main stem curves up and joins the underside off-centre at x -30. The pot and the other leaves are unchanged.
- [x] stretcher: a long flat tray with squared ends and a flat bottom. A steel top rail (`#a8acb2`, width 6, black outline) runs round the rim. Three black cross straps have small grey buckles. The rim loops that looked like basket handles are removed. It is empty and neutral, 420x140, anchor centre.
