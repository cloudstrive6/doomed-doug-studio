# Art review: 016 Every Layer of Antarctica (assets)

Reviewer: art director · 2026-10-12 · scope: the 43 new library drawings in `asset_requests.md`.

## Verdict: PASS. All 43 assets APPROVED. 2 got small fixes from me. No redraws needed.

How I checked:
- I looked at every preview sheet (`assets/previews/016-*`).
- I measured each JSON's bbox and anchor against the request.
- I rendered 32 keyframes that use the new assets, including every death beat (s026, s080, s151, s175, s199, s219, s244,
  s272) and every silhouette reveal (s092, s134, s162).
- I zoomed in on the frozen-Doug props, the hook and cap, and the tardigrade.

The detailed tier holds against crude Doug: 3-5 px outlines, layered flat fills and spray shading. Everything is
on-palette. Nothing is gory, cute or penguin-adjacent.

Note: the grid preview centres every asset, so the tall bottom-anchored ones (`hot_water_drill`, `diving_platform`,
`fridge`, `sponge_boulder`, `frozen_doug_column`) look cropped on the sheets. That is a preview artefact. The assets are
complete, and they render whole in the shots.

## Fixes applied by the art director (trivial, safe, no layout change)
1. **`tardigrade`: mouth tube.** The snout was a 32-unit disc with a big dark dot, and at hero size (s162-s168) it read as
   a pig's nose. That pushes it toward "cute farm animal". I narrowed it into a short pointed tube (x 140..174, y -24..-3)
   and made the opening a small dark dot at (172,-14). The bbox, anchor, facing and silhouette-with-rim outline are all
   unchanged.
2. **`frozen_doug_column`: raised arm.** The waving arm was drawn in `#6f97b3` at width 5. On the `#8fc2e0` shaded side,
   at scale 0.5, it disappeared in s219, so the requested "one arm raised" didn't read. I changed the arm and hand to the
   face-line colour `#4a6f8c` (arm width 7, hand r 12, width 4). It is still pale and ghostly, and it now reads as a hand
   waving up. Geometry is unchanged.

Check render: `assets/previews/016-ad-fixes.png`.

## Per-asset verdicts

### Recurring props
| Asset | Verdict | Notes |
|---|---|---|
| `hot_water_drill` | APPROVED | Pulley at exactly (0,-620). Centre column x -30..+30 is empty below the pulley (checked in the JSON). Legs at ±170 have snow drifts. The orange reel and boiler sit at the right. Reads at 0.9, 0.3 and 0.15. No text. |
| `ice_cube_icon` | APPROVED | Reads at 0.16 next to the meter label on light (s004) and on dark (s151, s244). |
| `rope_hook` | APPROVED | The tie-on ring is at (0,0) and the lower bend is open. The cap hangs cleanly in s272. |

### Travel stickers (all APPROVED)
The family matches `sticker_crevasse` / `sticker_la_brea`: a peeling corner, bold caps text, and 112x60 (or 130x64 for
two-line names). On the s273 closing card all nine names read, and every shape is distinct (rect, pennant, oval, shield).
- `sticker_blood_falls`: rust drip on a white stamp. No splatter. At 1.6 the drip looks a bit like a plunger, which is
  acceptable. Optional: thin the base puddle if the illustrator touches it again.
- `sticker_thwaites`, `sticker_ross_ice_shelf`, `sticker_filchner_ronne`, `sticker_mercer_lake`,
  `sticker_west_antarctic_rift`, `sticker_lake_ellsworth`, `sticker_vostok`, `sticker_denman`: on-brief. The colours step
  pale to black in item order, which echoes the ICE ABOVE DOUG ramp.

### Blood Falls
| Asset | Verdict | Notes |
|---|---|---|
| `taylor_glacier_front` | APPROVED | The central face x -150..+150 is plain. The striations and blue cracks are good. The brown ground runs to y +64, as noted. |
| `blood_falls_stain` | APPROVED | Palette is `#c8501e`→`#8a1a10` plus orange highlights. It reads as matte iron rust, not blood. No droplets. The apron at the base is a frozen orange sheet, not a red pool. |
| `five_story_building` | APPROVED | 5 rows x 4 windows, 312x500, same family as `six_story_building`. |
| `rusty_nail` | APPROVED | Head at left, patchy rust, flakes. Reads at 1.4. |
| `ice_chunk` | APPROVED | Opaque, with a shaded side and cracks. Doug's legs and the cap read in s026 and s080. |

### Erebus
| Asset | Verdict | Notes |
|---|---|---|
| `mount_erebus` | APPROVED | Mostly snow with dark ridges, a faint orange crater glow and the plume inside the bbox. Clearly not the grey `volcano`. |
| `ice_chimney` | APPROVED | Bulging frosted tower with a dark open top. Reads at 0.4. |
| `tshirt_hanger` | APPROVED | |
| `folded_jacket` | APPROVED | Doug's head rests on it in s054. |
| `tardigrade` | APPROVED (after fix 1) | Segmented, eight-leg read with claws, documentary tone. The red-rim silhouette reads in s162. |

### Thwaites / Fish
| Asset | Verdict | Notes |
|---|---|---|
| `manhattan_outline` | APPROVED | World-map green with a Central Park patch. Long and narrow. |
| `icefin_robot` | APPROVED | Reads both vertical (s067) and level (s069). No text. |
| `ice_fish` | APPROVED | Mid-tone whitish-pink with visible spine rays. It reads on navy (s095), and the silhouette and rim are clean (s092). |
| `diving_platform` | APPROVED | Top board at -700 reaching about +200, with lower boards and a ladder. Its top touches the ceiling in s088. |
| `teaspoon` | APPROVED | Bowl centre at about (+109,0), with the pale-blue pool. |

### Sponge Boulder
| Asset | Verdict | Notes |
|---|---|---|
| `sponge_boulder` | APPROVED | Cream vase sponges and stalked animals on a mid-tone rock. It reads on `#153f6a`. The outer outline is clean for the s134 rim. |
| `fridge` | APPROVED | |
| `frozen_doug_seated` | APPROVED | Squat, opaque and frosted. A faint X-eyes head shows inside. The flat ledge at -420 holds the cap (s151). The faint seated stick lines are acceptable: they are pale and ghostly, not a body. |

### Mercer / Volcanoes / Ellsworth
| Asset | Verdict | Notes |
|---|---|---|
| `microscope` | APPROVED | |
| `poppy_seed` | APPROVED | Blue-grey kidney shape with a net texture. |
| `clipboard` | APPROVED | |
| `mount_fuji` | APPROVED | |
| `meltwater_wave` | APPROVED | Same grammar as `mud_wave`, in water colours. It reads in s199. |
| `snowcat` | APPROVED | Reads at 0.22 and 0.5. |
| `fuel_drum` | APPROVED | No text. |
| `frozen_doug_column` | APPROVED (after fix 2) | |

### Vostok / Denman
| Asset | Verdict | Notes |
|---|---|---|
| `lake_vostok_outline` | APPROVED | 576x121 at the same 2.5 u/km as Ontario. |
| `lake_ontario_outline` | APPROVED | 780x203, dashed orange-red, outline only. |
| `frozen_doug_wave` | APPROVED | Narrow stem into a curling, splashing crest with frozen droplets and X eyes at (0,-520). It does not echo the 012 amber bead. The cap sits on the crest in s244. |
| `flag_doug_was_here` | APPROVED | Upright two-line text. The pole base is at (0,0). It reads at 0.8 (s267). |

## Redraws needed
None.
