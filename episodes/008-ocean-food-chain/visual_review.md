# Visual review: 008-ocean-food-chain

## Round 1: pre-render keyframes (2026-10-05)

Scope: all 321 keyframes (`build/keyframes/s001..s321.png`), re-rendered from the current `shotlist.json` with
`python -m studio keyframes 008-ocean-food-chain` (27 contact sheets). Before that, `build/contact/` held only a stale partial
`sheet_01`. I checked the suspect shots at full 1920x1080.

VERDICT: FAIL

Overall the episode is in good shape. Doug is on-model in every costume (red cap and white head always visible while
he's alive). The death counter climbs correctly, 65 to 74, with exactly 9 deaths (s032, s059, s077, s137, s163, s193,
s219, s247, s277). Both survivals (trevally s111, orca s310/s318) carry no increment. Section cards are consistent
(REEF / OPEN WATER / APEX / NO PREDATORS), the creature drawings are recognisable, and every death is a cartoon death.
s290 (livers removed) is not depicted, which is correct. The tone is never nursery-like. The fixes below are what
blocks a PASS.

### Required fixes

1. **s246, s047, s270, s279: red silhouette glow reads as blood in the water** (director, with art director if needed).
   `glow_r` draws a red speckled cloud around the silhouette. In s246 that cloud sits in the water directly under Doug,
   one shot before his death, so it reads as a blood pool. In s270 the red clouds around the orcas next to the whales
   read the same way. Remove `glow_r` from those four silhouette assets. If the art director prefers to keep a menace
   cue, they can add a non-red glow colour option (for example dark navy or white) and use that instead.
2. **s059: Doug is not identifiable in his own death shot** (director). Only `reef_fish_costume_flat` with X eyes is
   visible, with no cap and no head, so it reads as "a fish died". Every other death keeps the cap (see s032, s219).
   Add `{"type":"asset","name":"doug_cap","x":1080,"y":890,"scale":0.5}` (on the sand at the crack mouth). Keep it in
   s060 too, so the ghost-with-cap and the cap on the floor stay consistent.
3. **s077: same problem as s059** (director). Only `crab_costume_flat` is visible, with no cap. Add `doug_cap` beside
   the crab, for example `x≈1330, y≈890, scale 0.5`. Carry it into s078.
4. **s018: stray zigzag line** (director). The "crack" line `[[1430,600],[1470,650],[1440,700],[1480,740]]` hangs
   below the snail in open water and looks like a drawing error. Move it onto the shell, for example
   `[[1400,500],[1425,535],[1405,565],[1435,600]]` (black, width 4), or use `snail_shell_cracked` as in s032.
5. **s189 and s317: white "flash" blob reads as grey static** (director). The `spray` with r 90–100 and density
   0.4–0.5, at (1500,300) in s189 and (1300,500) in s317, renders as a fuzzy grey noise disc. On s189 it also floats in
   an aerial river view. Replace it with a recognisable camera-flash cue: the `highspeed_camera` asset or a small
   phone/camera icon plus a white starburst. Otherwise remove it, since the "BULL SHARK, 2014" and "2024" labels already
   carry the beat.
6. **s312: "RIP DOUG" on the gravestone is illegible** (director). `red_x` at (1450,450) sits on top of the engraving,
   so the joke ("we are slightly less pleased") loses its setup. Let the text read first. Either shrink the `red_x` to
   about 0.6 and give it `appear: 0.6`, or replace it with a single red diagonal stroke from the top-left to the
   bottom-right corner of the stone that leaves "RIP" and "DOUG" readable.
7. **s060: wordart "INFORMANT" is printed across the grouper's body** (director). The key subject (the head-standing
   grouper) is half covered. Move the wordart to the empty upper right, for example `x 1450, y 330`, below the counter,
   or to the left at `x 520, y 560`.
8. **s061: title "GIANT PACIFIC OCTOPUS" overlaps the octopus head and arms** (director). Move the octopus down or
   right (for example `y 640`), or the title up to `y 250`, so the text sits on clear water.
9. **s105: the red arrow cuts through "HUNT THE SKY"** (director). Start the arrow above the wordart line, or move the
   wordart to `y 230`, so the arrow runs from the fish's nose up into clear sky.
10. **s282: the orca's dorsal fin pokes through "KILLER WHALE"** (director). Move the wordart to `y 250`, or the orca
    down to `y 640`.
11. **s191: the tide table floats about 180 px above Doug's hand** (director). Narration says he is "holding a tide
    table". Move `tide_table` down to Doug's hand height (about `x 790, y 730`) as in s192, and keep the "x2" label
    next to it.

### Advisory (fix if cheap; not blocking)

- **s316, s317 (illustrator/director):** the salmon "hat" sits on the orca's back behind the blowhole, not on its head.
  Shift `salmon` forward to about `x 1180, y 500` so it rests above the eye patch ("like hats").
- **s058 (director):** the moray approaching from the right is a featureless black smear cut off at the frame edge.
  Either use the normal moray asset (as in s059) or keep the silhouette but show the head end.
- **s058–s060 (director):** the head-standing grouper's tail is tucked under the "GIANT MORAY" topbar label. Lower the
  grouper about 40 px.
- **s113, s122, s125 (director):** the title "GOLIATH GROUPER", the "SWALLOWED WHOLE" box and "BOOM" all touch the
  grouper's dorsal fin. Nudge the labels up 30–50 px. On s125, "SWIM BLADDER" has no pointer. Add a short arrow to the
  belly.
- **s015–s019 (director):** the "DOUG DEATHS" counter sits on the slow-motion inset's top-right border. Shrink the
  inset to `w 1500` or start it at `y 220`.
- **s186, s212, s213, s288, s289 (director):** labels or animal icons straddle the map frame border ("TORRES STRAIT",
  "16 MARATHONS", "+1,800 KM", the orcas and the crossed-out shark). Keep them fully inside or fully outside the map.
- **s290 (director):** the red X sits on the east coast (near Durban), not at Gansbaai or over the sharks. Move it onto
  the shark icons, or drop it.
- **s235, s236 (illustrator/director):** the sunrise sun is an unfilled yellow outline arc and reads as a stray curve.
  Fill it (`#ffd54a`) as on the other suns.
- **s299 (director):** "15 OF ~40". The 15 patterned orca icons look almost the same as the 25 silhouettes at
  playback size. Outline the 15 in red or grey out the other 25.
- **s094:** "ILE AUX GOELETTES" is missing its accents (Île aux Goëlettes). Fine if the font can't render them.
- **Variety:** s119–s122 (grouper big close-up on the wreck, four in a row) and s259–s261 (whale on black with click
  arcs) are the closest the episode comes to stale runs. Each shot adds a new label or arrow, so this isn't blocking,
  but one camera move (`zoom_in` on the mouth for s121–s122) would help.

### Not issues (checked)

- s255 ends on a cropped Eiffel Tower at the top edge. That is the end state of its `pan_down` through 6 towers, which
  is intended.
- s158–s160 is an x-ray of the shark's stomach (cans, bottle, sacks). It's schematic and not gore.
- s032, s137, s163, s193, s219, s247, s277 are cartoon deaths (X eyes, cap, splash). No blood, organs or dismemberment.
- s161 "EPISODE 6: 0 SHARK DEATHS" matches the series bible (006: "Sharks never hurt Doug").

Re-screen after fixes: re-run `keyframes --shots` on the changed ids and send me the new sheets.
