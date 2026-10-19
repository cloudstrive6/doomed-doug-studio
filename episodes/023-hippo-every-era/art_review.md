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
