# 030-trapped-in-amber: art review (art director, 2026-10-28)

**Verdict: PASS.** All 40 new assets are approved. Keyframes pass after the shot-level fixes listed below, which I made in
`shotlist.json` and re-rendered. Nothing blocks `art_approved`. The thumbnail (`s001` scene_ref) is still missing; that is the
graphic designer's job, and it does not block keyframes (they render a "thumbnail pending" placeholder; `validate` flags only that).

## How I reviewed
- Sheets: `assets/previews/030-trapped-in-amber-assets-a.png`, `-a-fitted.png` (with the bead sandwiches),
  `030-trapped-in-amber-assets-illustrator-b.png`. I also rendered fitted sheets for the 14 assets after `oculudentavis_specimen`
  (their old 030-assets-a..e previews crop). I ran a silhouette test (purple spray on `#2c1f12`) for `enantiornithine`,
  `big_cretaceous_snake`, `hell_ant`, `amber_spider`, `parasitic_wasp` and `feathered_dino_looming`.
- Keyframes: `python -m studio keyframes 030-trapped-in-amber` (217 frames, 19 contact sheets). I checked every sheet, then
  re-rendered the shots I changed.

## Assets (40): style consistency
House check across all of them: detailed tier (dark outlines, flat fills, interior shading/spray), on the amber/forest palette,
bold silhouettes, nothing gory (`belone_fossil` is flat and dry; the death beats only show the cap). No cute eyes on any creature;
every toothed animal has a hard small eye under a brow. The bead sandwich reads as amber at tray scale 0.22 (`s032`, `s212`).

| # | Asset | Verdict | Note |
|---|---|---|---|
| 1 | `amber_bead` | APPROVED | Honey core, darker lower-right rim, plain core region as specified. Reads at 130 px. |
| 2 | `amber_bead_glint` | APPROVED | The outline matches the bead, and the glints sit at the rim. The sealed-in look works on every specimen. |
| 3 | `feather_tick` | APPROVED | Loose barbs, and the tick is clear at 1.1 and at 0.35 on the family tree. |
| 4 | `dracula_tick` | APPROVED | Balloon body with tiny legs, no face. Still reads as a blob with legs at 0.15 on the nest. |
| 5 | `tick_unfed` | APPROVED | |
| 6 | `coin_edge` | APPROVED | No text and no portrait. |
| 7 | `film_poster_generic` | APPROVED | No title, logo or skeleton badge (CD decision 5). The centre is dark for the bead. |
| 8 | `dna_strand` | APPROVED | |
| 9 | `moa` | APPROVED | Correct scale against Doug at 0.31 (`s017`). |
| 10 | `feather_nest` | APPROVED | |
| 11 | `enantiornithine` | APPROVED | Teeth and the wing-tip claw survive in silhouette. Minor: the raised wing is a lumpy mass, and the claw is small (see illustrator note 1). |
| 12 | `feathered_dino_looming` | APPROVED | The cut neck stays off-frame at x 1940 (`s028`-`s030`, `s208`-`s209`). Teeth show white in the silhouette, which works. |
| 13 | `dna_kit` | APPROVED | The blank screen takes the "ERROR" overlay cleanly (`s027`). |
| 14 | `test_tube_dino` | APPROVED | |
| 15 | `amber_spider` | APPROVED | Fangs forward, front legs raised. The lower legs read as about 6 lines; acceptable at bead scale. |
| 16 | `parasitic_wasp` | APPROVED | |
| 17 | `hell_ant_grip` | APPROVED | Horn, upswung jaws and pinned nymph all read at 1.1. |
| 18 | `hell_ant` | APPROVED | Silhouette is clear. |
| 19 | `vampire_ant` | APPROVED | The metallic paddle reads (`s067`). |
| 20 | `rice_grain` | APPROVED | |
| 21 | `cockroach_costume_empty` | APPROVED | Flat and empty, with the cap on top (`s075`). |
| 22 | `ammonite_shell_empty` | APPROVED | The sand-packed opening faces **down** (local x -30..16, y 49..124), not lower right as requested. I fixed the `s099` arrow to match (see below). |
| 23 | `beach_towel` | APPROVED | |
| 24 | `xiaophis_skeleton` | APPROVED | Headless chain that reads as a backbone. |
| 25 | `shed_snake_skin` | APPROVED | |
| 26 | `big_cretaceous_snake` | APPROVED | Reads as a snake in silhouette. |
| 27 | `oculudentavis_skull` | APPROVED | |
| 28 | `oculudentavis_specimen` | APPROVED | |
| 29 | `tiny_saddle` | APPROVED | |
| 30 | `retracted_stamp` | APPROVED | |
| 31 | `bee_hummingbird` | APPROVED | The magenta throat patch is the real gorget, not a blush. |
| 32 | `belone_fossil` | APPROVED | Flat museum look, not gory. |
| 33 | `amber_lump_claw` | APPROVED | |
| 34 | `belone_scan` | APPROVED | Same x-ray family as the library scans. |
| 35 | `eva_tail` | APPROVED | 8 vertebrae are visible. |
| 36 | `amber_market_stall` | APPROVED | |
| 37 | `price_tag` | APPROVED | |
| 38 | `kachin_map` | APPROVED | Sober-card palette, no labels. |
| 39 | `specimen_tray` | APPROVED | Slots line up with the 160 px bead spacing at 0.8. |
| 40 | `narrator_hand_pencil` | APPROVED | Crude tier, auto-ink. Stays below the counter zone. |

### Illustrator notes (non-blocking, library hygiene for reuse)
1. `enantiornithine`: when this asset is next reused, make the raised wing a cleaner feathered fan, and make the
   leading-edge claw slightly larger so it reads at 0.5 scale.
2. `ammonite_shell_empty`: if it is reused with arrows, either note in the asset's `description` that the opening faces down,
   or rotate the sand patch to the lower right.
3. `assets/previews/030-assets-a*.png` / `-b..e.png` are stale intermediate previews (two of them crop the assets). Delete them
   or regenerate them as fitted sheets.

## Keyframes
Consistency is good. Doug is on-model in every shot (red cap always visible, ghost included). The zone ramp follows the director's
size bands: Bugs `#4a3520`, Bigger `#3b2a17`, Backbones `#2c1f12`, Dinosaur `#1a120b`. The counter ticks 240 to 246 on the six death
beats, and there is no Doug/counter/wordart on the Kachin sober card. Text stays inside the safe area, and nothing is gory.

### Fixed by me in `shotlist.json` (re-rendered and verified)
1. **s052:** two `narrator_hand_pencil` arms were stacked on screen. The engine has no "disappear", so the "raise, then lower" pair
   rendered as two arms. Now there is one arm at (1420, 380).
2. **s099:** the "SAND" arrow pointed at empty amber. It now ends on the shell's sand-packed opening (1080, 640).
3. **s136:** the "BEE HUMMINGBIRD" wordart overlapped the "OCULUDENTAVIS" label, with 3 labels on screen. I removed the
   skull label (the skull was named in `s135`) and centred the wordart over the hummingbird.
4. **s137:** 3 labels on screen. I dropped the unspoken "TINY DINO!".
5. **s171:** the "WING CLAWS" arrow pointed at the back/tail. It now ends on the wing-tip claw (1135, 370); I moved the label to
   (640, 230).
6. **s178:** the silhouette bird's wing touched the "DOUG DEATHS" counter. I lowered the bird to y 600 (and its glow to y 500).
7. **s180:** ghost Doug sat on top of the "LESS PARENT" wordart. I moved the wordart to (760, 190) and the ghost to (560, 380).
8. **Layout variety:** the bead-hero layout (bead at 1060,540 @1.1 with Doug at the left) ran 5-7 shots in a row in five places.
   I mirrored one shot in each run (bead to x 820; Doug to the right, facing left; labels and wordart follow the bead):
   - **s009** (run s007-s011)
   - **s058** (run s056-s062)
   - **s069** (run s066-s071; the beetle and warning triangle also moved to x 1400 and flipped toward the bead)
   - **s097** (run s096-s100)
   - **s110** (run s108-s112)

   No run of identical compositions is now longer than 4.

### Director notes (non-blocking; consider them for the editor pass or the next episode)
1. Purple silhouette glows (`#5e4670`) are almost invisible on the brown/orange forest grounds (`s003`, `s004`, `s028`, `s178`,
   `s208`). The silhouettes still read, but the reveal loses its glow. Next time, raise the spray density to about 0.35 or use a
   `rim`.
2. The bead-hero layout is still about 35% of the episode. It is the device, and labels/arrows change on every shot, but the next
   amber-style device should plan alternate layouts (close crop, two-up, side-by-side scale card) from the start.
3. `s105` wordart "BACKBONES" is immediately followed by the `s106` "BACKBONES." section card. The repeated word is acceptable,
   but a different `s105` wordart (e.g. "NEXT SIZE UP") would land the card harder.
4. `s210` is a 1.2 s black frame with only the counter. I read it as a deliberate cut-to-black before the cap seals; keep it at
   1.2 s or less.

## Required fixes
None outstanding. Items 1-8 above are done. The graphic designer still owes `thumbnail.json` for `s001` (the normal
packaging step).
