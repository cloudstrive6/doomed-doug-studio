# 023-hippo-every-era: art review (art director)

## Round 1: new library assets (41), 2026-10-19

**Verdict: PASS.** All 41 drawings are APPROVED. Five of them needed small fixes, and I made those myself (listed below). No
revisions go back to the illustrator. Keyframes are not part of this round. They get their own review after `keyframes`.

Checked against: the requests in `asset_requests.md`, art bible two-tier rule (detailed creatures/places vs crude Doug), style
bible section 7 rules 1, 7 and 8, the house creature reference (`t_rex`, `cave_lion`), bold silhouette at small size, and no gore.
I rendered each asset at 1:1 and the backdrops at full 1920x1080. The fixed assets are on
`assets/previews/023-hippo-every-era-assets-ad-fixes.png`.

### Fixed by the art director (now APPROVED)
1. `inostrancevia`: the near-side legs were drawn **on top of** the body, starting at the back line. That left boxy trapezoid
   "panels" with black seams across the shoulder and hip. I moved the near legs (elements and claw ticks) behind the body. Now
   the legs come out of the belly and the silhouette is one clean shape. Nothing else changed.
   Optional polish if the illustrator has time later: bend the legs at elbow and knee for a more sprawling, semi-upright gait.
   This does not block anything.
2. `allosaurus`: the near and far thigh polygons were hard-cornered boxes. I set them to `smooth`, so they read as drumstick
   thighs. The eye horns, longer arms and slimmer head still make it read clearly differently from `t_rex`, and the silhouette
   stays distinct for the Short end-card.
3. `inostrancevia_tooth`: the root was a narrower, dark-brown dome, so the tooth read as a lipstick or bullet cap. I widened the root base to match
   the crown, so the outline is continuous, and recoloured it bone-tan (#c4a26a, shade #a07e48). I also softened the gumline seam.
   Size is unchanged (about 110x430, still clearly longer than `bank_card`).
4. `jurassic_conifer`: four green ellipse "pucks" sat on the trunk at each branch tier, so the tree looked like a skewer.
   I removed them. The trunk now runs up through the tiers like an araucaria.
5. `trafalgar_square`: the **fountain stem** ended on the far rim of the basin, so the dish seemed to float behind the water,
   and the side jets landed on the paving. I lengthened the stem to y -88, so it stands in the water, and added a
   pale ripple ring at its base. Both jets now arc down into the basin. Also checked: Nelson's Column top is at y -975
   (clears the caption bar), the counter zone at the top right is plain sky, and the hippo stands in the basin at (0,-80).

### APPROVED as delivered
| Asset | Note |
|---|---|
| `ambulocetus` | Croc-snout whale, big webbed hind foot reads. Mid-tone fill OK on shallows. |
| `archaeopteris` | Tiered frond crown, dark undersides. Reads on #b9c4a8. |
| `bowling_pin` | Clean, two red stripes, grey side shading. |
| `britain_map` | Matches the world_map style. Frame, wave ticks, no labels. |
| `bronze_lion` | Reads as a statue (bronze plus stone plinth), not a cat. |
| `canoe_paddle` | OK. |
| `climactichnites_slug` | Flat, faceless, no tentacles. Clearly not 014's `slug`. |
| `climactichnites_trail` | The ladder trail reads well on the slab. |
| `croc_head_rising` | Jaws closed, yellow slit eye, water streaming. A head, not the log gag. |
| `cycad` | Wide enough to hide a 0.5 Doug. |
| `ginkgo_branch` | Fan leaves read even when small. |
| `gorgonopsian_skull` | The saber drops well below the lower jaw. Matches the live animal. |
| `grass_tuft` | Tiny tuft, not a meadow (CD note respected). |
| `hippo_trackway_slab` | Four-toed prints with drag scratches. |
| `hippo_whale_portrait` | Deadpan, half-lidded and flat-mouthed. Adult-coded, and different from 019's frame. |
| `hyneria` | Rhombic scales, lobed fins, fangs. The red is mouth interior, not blood. |
| `hynerpeton` | Not cute, no smile. |
| `pakicetus` | Slender, long snout. One shot only. |
| `platform_scale` | Blank dial face, hazard edge. |
| `purussaurus` | Broad blunt snout and scute row. The silhouette works for the end-card. |
| `purussaurus_skull` | OK. |
| `reeds` | Dense enough to hide `cave_lion` at 0.6. |
| `rosette_badge` | Blank centre for the wordart. |
| `sauropod_footprint` | Water, shine line, rim. Sized for one hippo foot. |
| `spotted_hyena` | Sloping back, spots, dark muzzle, bone. Not cute. |
| `time_machine_hippo_ears` | Ears and eyes in the window, rump bulge. Reads as "inside and safe". |
| `time_machine_hippo_squeeze` | Cartoon rump plus a kicked hind foot. Comic, not crude beyond our tone. |
| `titanoboa` | Long gentle S, saddles. The silhouette works for the end-card. |
| `titanoboa_coil` | Two humps that tile. |
| `titanoboa_head_fish` | Limp silver fish crosswise, no blood. |
| `tourist_map` | No readable text, red dot. |
| `trafalgar_ghost` | Thin grey lines only. Column top stays low at 0.75. |
| `trex_teeth_row` | Banana teeth, gum line. |
| `triceratops` | Frill, brow horns, beak. Not cute. |
| `water_jug` | Translucent, water line visible. |
| `zircon_crystal` | Pink-brown prism with pyramid ends. Works as a speck. |

### Capless-Doug outro exception (s297-s298): CONFIRMED
Approved as a logged one-off under the art bible "Capless upright Doug (from 008)" rule. This is the same device as the 008 close,
where the orca wears the cap. Conditions, all met in the current shotlist:
1. `doug_cap` sits on the hippo in both s297 and s298, so the red cap is always in frame (style bible 7.2 intent kept).
2. Doug is upright (`stand`) with `gear: ["cap_off"]` only. No other change to his design. Expressions `flat` (s297) and `smirk`
   (s298) come from the engine's set.
3. The exception is logged in `decisions.md` (director, shotlist entry).
It must not spread: no other shot in 023 may use upright `cap_off`. At keyframes, I will check that the cap on the hippo
reads at full frame and that the s298 arrow lands on it.

## Keyframe review (art director), 2026-10-19

**Verdict: PASS.** I reviewed all 301 keyframes on the 26 contact sheets and opened the close calls at full 1080p.
I fixed 21 shots myself in `shotlist.json` (layout changes only, no new assets) and re-rendered them. Then I rebuilt
the full keyframe set and contact sheets. `validate shotlist` is OK. Nothing goes back to the director or the illustrator.

Checked against: art bible (safe area, counter zone x 1300-1860 / y 110-270 with the hippo tally, "tall props stay below
the chapter bar", the wordart-crossing rule, red title cards) and style bible section 7 rules 1-9.

### Passed as rendered
- **Doug on-model in every shot.** Red cap present everywhere, including ghost floats, cap-only death beats and the s176 hide
  (cap now peeks out from the cycad). The expressions come from the fixed set. Ink is correct on the dark Hadean and space shots.
- **Zone colours hold per era.** Ice Age London: blue sky, green river, brown bank. Turkana: amber sky. Purussaurus and
  Titanoboa: green hills over olive water. Morrison: tan desert. Gorgon: ochre. Hyneria: sage/murky brown. Bare Land: grey
  with brown hills. Archean: rust sky over teal sea. Hadean: violet-black with the big Moon. Beige `#f4f1dc` is used only for
  explainer/infographic cuts, and that is consistent.
- **Title cards** are all red with a black outline, with a date label under each. Reveals use a silhouette plus glow, then the
  full reveal (Turkana croc, Purussaurus, Titanoboa, T. rex, Allosaurus, sauropod, gorgonopsian, Hyneria, and the hippo itself in s199).
- **Layout variety is good.** Maps, scales, bus/car comparisons, a phylogeny tree, a seesaw, a pie chart, a timeline bar,
  chalkboard verdicts and split screens all appear. No run of 5 identical compositions. No gore: the deaths are splashes,
  X-eyes, ghost floats and a dropped cap.
- **Capless-Doug outro (s297-s298):** the cap reads on the hippo at full frame. The s298 arrow now lands on the cap (see fix 21).

### Fixed by the art director
1. s014: moved "TRAFALGAR SQUARE" left (x 800) so it no longer crosses the ghost column's statue.
2. s018: "WARM SPELL" was sitting on Doug's head. Moved it to (1000, 500) and moved the sun to (620, 330).
3. s035: moved ghost Doug off the bronze lion statue, to (250, 540).
4. s042: raised "HALF A BUS" to y 185, clear of the bus roof.
5. s108: moved the Titanoboa title to the open swamp (y 760, date at 890). It had been touching Doug's cap, and the card was top-heavy.
6. s113: raised "LONGER THAN A BUS" to y 190, clear of the bus roof.
7. s115: the angry sun was in the counter zone, on top of the hippo tally. Moved it to (1150, 400) and moved "VERY HOT" to x 680.
8. s116: moved "AVERAGE YEARLY" and the 30-34 °C label to x 1180, off the thermometer ticks.
9. s158: the conifer crown was inside the counter box. Changed it to (1680, 720) at scale 0.45.
10. s162: "REDWOOD TALL" crossed the conifer crown. Changed it to x 380, size 76.
11. s174: "35 M" collided with "40 TONNES". Moved it to the ground under the silhouette (y 995).
12. s176: Doug was fully hidden, with no cap in frame (7.2). Moved him to x 1290 so the cap and legs peek out.
13. s182: the descending sauropod foot crossed the chapter bar. Moved the foot and footprint to x 600 and Doug to x 1100, facing left.
14. s205: the Archaeopteris crown sat behind the counter. Changed it to (1790, 620) at scale 0.35.
15. s208: the Archaeopteris at scale 0.9 ran through the counter and off the top. Changed it to (1150, 640) at scale 0.6, with its label at (1150, 680).
16. s213: "5 CM FANGS" covered the fish's head. Moved it below the fish to (1450, 880), with the arrow pointing up to the fangs.
17. s214: "SHARK TEETH: SMALLER" ran into swimming Doug. Moved it under the shark (y 935).
18. s249: the "SUNLIGHT" label sat on the time machine's sign. Moved it next to the sun (480, 300).
19. s268: ghost Doug was rising into the sun. Moved him to the open right side (1600, 640).
20. s276: the early-Earth "land" was two hard black squares, which looked off-tier. Redrew them as rounded, dark-brown crust islands.
21. s298: the arrow ended about 200 px above the cap. It now runs from (1300, 450) to (1120, 800), onto the cap. Also moved "ALL TWELVE" to (1250, 380), size 100.

### Accepted / notes (no action required)
- s124 (`pan_right` on a 3840-wide canvas) has no counter, because scene labels scroll with the pan and the engine has no
  screen-fixed overlay. This is one shot, the count doesn't change, and the counter is back in s125. Accepted.
- s001, s059, s157, s226 and s247 have no caption bar on purpose (cold open and the one-line "NO HIPPOS." / "NO GRASS." /
  "NO PLANTS." / "NO AIR." stingers before each title card). The device is consistent, so it is accepted.
- Minor busy-backdrop overlaps are left as they are because the outlined text stays legible: s006 (title over the window
  corner), s035 ("A LONDONER" over the dome), s296 (chalkboard in front of Nelson's Column).

## Round 2: director's visual-review fixes (art director), 2026-10-19

**Verdict: PASS.** I re-rendered the 10 changed shots plus their neighbours (s002-s009, s055, s123-s125, s283-s287) from
the current `shotlist.json` and checked each at full 1080p. `validate shotlist` is OK.

### Checked
1. **s124 (pan dropped).** This is now a static 1920 frame: Doug on the left bank (cap and head clear of the coils), four
   coil humps, then `hippo_submerged` in the gap between the coils with ears, eye and nostrils above the waterline. The `!` and
   the red arrow carry off-frame right for "just keeps going". The full DOUG DEATHS 190 / chalkboard / HIPPO SURVIVED 3/12
   HUD is back. The hippo cutaway (body visible below the waterline) matches s125, so the Titanoboa stop stays consistent.
   This resolves the Round 1 "s124 has no counter" note.
2. **s003.** Close-up on the hippo's face for "did not agree". It breaks the s002-s004 room run. "SIGNED: NOBODY" only
   touches the brow line and stays legible. Doug is off-frame here, which is fine for an intro reaction cut (topbar off, as in s001-s005).
3. **s008.** The hippo is wedged in the time machine with the door bulging and motion lines, and "DOES NOT FIT" is set clear of the drawing.
   It breaks the s006-s009 run. Doug is on-model with his cap.
4. **s056.** A calf hippo now stands between the adult and the croc, and the CALVES arrow lands on it. Ghost Doug keeps his cap.
5. **s096.** All three arrows land: LONG SNOUT on the snout tip, JAWS on the tooth row, BIG FEET on the hind foot.
   Labels sit in open sand/sky and clear the HUD.
6. **s145.** The stray parallelogram is gone. A small T-rex silhouette now stands on the horizon. **Fixed by me:**
   it used the default red reveal glow, which at scale 0.3 rendered as a tight red speckle around the feet, close to
   "blood at the feet" at feed size. I set `"glow_r": 0` to match every other small silhouette in 023 (s038/s049/s220/s222/s225).
   Re-rendered and verified: it is a clean black silhouette.
7. **s154.** There is now a three-toed T-rex footprint, sand-rimmed, with the cap pressed flat in the heel, over the picnic blanket. It reads as
   "stomped" and not as a pool. No gore.
8. **s284.** The O2 dial reads 0% with "NO OXYGEN" wordart. It is a distinct visual from s283/s285.
9. **s286.** A close-up of the hippo in the pool with the Moon cropped top-left breaks the Hadean run. White ink on Doug is correct on the dark ground.
10. **s297.** Capless Doug is now large, in the foreground on the right, with a "DOUG SURVIVED: 3 / 12" label and a red arrow onto him. The cap
   sits on the hippo and reads at full frame. This closes advisory 16. The exception is still limited to s297-s298.

### Variety
The s002-s009 room shots now go wide, close, wide, wide, squeeze, wide, so there are never more than 2 similar frames in a row. The Hadean s283-s287 run is
broken by the s284 dial and the s286 close-up. Nothing goes back to the director or the illustrator.
