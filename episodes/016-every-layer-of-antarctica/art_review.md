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

## Keyframes round 1

Reviewer: art director · 2026-10-12 · scope: all 274 keyframes (`build/contact/sheet_01..23.png`), with crops at full size for the
counter zone and frame edges. I also ran a script check of the shotlist for wordart word counts, the safe area, the counter zone and
the meter.

### Verdict: FAIL (composition only, no asset redraws). Route everything below to the **director**.

What passes:
- **Doug is on-model in every shot.** The cap is always visible, the white auto-ink reads on the dark items, and the death beats
  (s026, s102, s151, s175, s199, s219, s244, s269) are cartoon-only and tick the counter. The alive `on_back` naps (s054-s057,
  s197-s198) do not tick it.
- **Silhouette reveals follow the bible.** On the underwater ones (s091-s092, s133-s135, s162) the rim is red and the glow is dark,
  and the colour reveal comes 1-3 beats later.
- **The ice-thickness ramp is monotonic per item and works.** I logged it in `channel/art_bible.md`. The item title cards are red,
  and the section headers (THIN ICE., THICK ICE., THE BOTTOM.) are white with an outline.
- **The counter never drops.** The ICE ABOVE DOUG meter only grows, except at fix 1.

### Required fixes (director)
1. **Meter regression, s017.** The meter shows `400 m`, then drops to `0 m` in s018. Keep it at `0 m`. The 400 M label already
   carries the lake depth.
2. **Font size 0 (the keyframe crash), s202 and s215.** `travel_suitcase` plus six `sticker_*` assets sit at `scale 0.073`. The sticker
   names render at 0.80-0.95 px (`BLOOD FALLS`, `MERCER LAKE`, `WEST ANTARCTIC`), which `int()` turns into 0. Remove the `sticker_*`
   elements, and keep the suitcase, wherever the suitcase scale is under 0.15. That means s083, s084, s087, s088, s108, s152,
   s154, s202, s215, s217, s218 and s222. At that size they render as 1-px text noise. The `max(1, ...)` clamp in `studio/paint.py`
   can stay as a safety net, but the shotlist must not rely on it.
3. **Counter / meter zone (x 1300-1860, y up to 260; wordart tops must be at y ≥ 290 there):**
   - Props touching the meter: s038, s039, s044, s046, s047, s053-s057 (the right cave icicle hits the ice-cube icon; move it to
     x ≤ 1250). s069-s080 (the right crevasse spike runs up through the meter; move it to x ≤ 1250, or keep its tip at y ≥ 300).
   - Inset frames crossing the zone: s135, s136 (REC frame: end it at x ≤ 1280 or start it at y ≥ 290), s188, s252 (world map frame:
     shrink it so it ends at x ≤ 1280, or start it at y ≥ 290).
   - Doug inside the zone: s187 (his head overlaps the meter label; put him on the block top at x ≤ 1150).
   - Wordart tops in the zone (lower them to y ≥ 330, or end them at x ≤ 1290): s036, s051, s052, s078, s119, s136, s137, s148,
     s151, s156, s167, s169, s170, s187, s190, s197, s198, s274.
4. **Safe area (x 64-1856, y 40-1040):**
   - Wordart past the edge: s012 PERFECTLY CLEAR, s025 JOINED THE PHOTO (starts at x about 0), s084 TWO EIFFEL TOWERS, s178 RADAR MAPS.
   - Wordart bottom below 1040: s028, s121, s189, s240 (raise y by 40).
   - Wordart left edge at x 60: s138.
   - Labels clipped at the bottom: s254 `DENMAN: 8 TIMES LOWER` (cut off at the frame edge; move it to y ≤ 990) and s019 `12+ KM INLAND`.
5. **Wordart over subjects or lines** (bible: never across landforms or frame lines). Move each one into clear sky, water or ice:
   - Glacier outline: s008, s009, s011, s023, s024, s025.
   - Drill or boiler: s004, s005, s107, s206, s213, s272.
   - Volcano plume and slope: s045.
   - Boulder: s138 (TOTAL DARKNESS), s147 (NOBODY KNOWS).
   - Sponge rim: s142.
   - Distance line: s144 (put SO FAR AWAY below the dashed line).
   - Canyon walls: s249, s256, s260, s261.
   - Arrows: s158, s245, s258.
   - Ocean trench bar: s253 (GO DEEPER).
   - Rope: s251, s267, s270, s271 (the vertical rope runs through the letters; shift the wordart sideways off the rope's x).
   - Minor overlaps: s205 (CAMP and the DEC 2012 label overlap; separate them by 30 px), s146 (the bubble tail crosses the
     625 TO 1,500 KM label), s182 (the UNDER THE ICE label sits on the scientist's hair).
6. **Wordart over 4 words** (rule 4): s016 `1.5 TO 2 MILLION YEARS` → `2 MILLION YEARS`, s126 `A LAKE IS A LAKE` → `A LAKE`,
   s190 `CAN'T SEE ANY OF IT` → `CAN'T SEE IT`, s204 `UP TO A MILLION YEARS` → `A MILLION YEARS`, s270 `THE END OF THE WORLD` →
   `END OF THE WORLD`.
7. **Layout variety.** These runs use the same composition 5+ times. Change the framing of at least every third shot (camera push-in,
   close-up, white diagram card, split panel):
   - s053-s057 (cave nap, 5)
   - s069-s077 (crevasse underside, 9). For example, a close-up on one slot for s073, and a white bar-chart card "1/10 area vs 1/4
     melt" for s076-s077.
   - s097-s103 (fish gap, 7). For example, a side-view tide diagram for s098-s099.
   - s125-s129 (fishing, 5)
   - s172-s176 (Mercer lakebed, 5)
   - s191-s196 (volcano cross-section, 6)
   - s233-s240 (Vostok borehole, 8). For example, push in on the borehole for s237-s239.
   - s256-s261 (canyon, 6)
   - s015-s019 (glacier side, 5). Optional: one push-in.
8. **Tall props under the caption bar:**
   - s083, s084, s108, s132 (drill top pokes into the chapter bar; lower the surface line, or move the drill to x ≤ 500).
   - s217, s218 (the snowcat/crew packing up sits at the caption bar's y; it is the beat's punchline, so lower the surface to
     y ≥ 160).
9. **s274:** the red rectangle under the suitcase reads as a glitch. Make the "room" slot a dashed outline on the suitcase face, or
   point a red arrow at a free patch.

Optional (non-blocking): s229-s240 have surface Doug at x ≈ 1245, right against the counter. Move him to x ≤ 1100.

Re-render after the fixes (`python -m studio keyframes 016-every-layer-of-antarctica`). I'll re-review the full set.

## Keyframes round 2

Reviewer: art director · 2026-10-12 · scope: all 274 re-rendered keyframes. I rebuilt `build/contact/sheet_01..23.png` from
the fresh `build/keyframes` because the last single-shot render had left only `sheet_01`. I cropped the counter/meter zone, the
frame edges and every round-1 hotspot at full size, and ran a script check of the shotlist for wordart word counts, stickers on
small suitcases, and the counter and meter sequence.

### Verdict: FAIL (4 small composition fixes, no asset work). Route everything below to the **director**.

Round-1 fixes I checked as done:
- **1.** The s017 meter now reads `0 m`. The meter only climbs (0 → 25 → 587 → 740 → 800 → 872 → 1,087 → 2,000 → 3,200 → 3,766 → 4,000)
  and the counter goes 130 → 139 with no drops.
- **2.** No `sticker_*` sits on a suitcase scaled under 0.15. s273 still shows all nine stickers.
- **3.** The counter/meter zone is clear: the cave icicles and crevasse spikes moved, the REC and world-map frames end at about x 1260, and
  s187 Doug is at about x 940. The listed wordart now clears the zone.
- **4.** Safe area: s012, s025, s084, s178, s028, s121, s189, s240, s138, s254 and s019 are all inside.
- **5.** The listed overlaps are cleared, including the glacier, drill, boulder, rope and arrow shots, plus s205, s146 and s182.
- **6.** Every wordart is 4 words or fewer.
- **7.** Variety: s073 close-up, s076-s077 bar chart, s127 push-in, s173 close-up, s237-s239 borehole push-in, s259-s260 canyon push-in, and
  push-ins on s054/s056/s057 and s193/s194. Those runs now pass.
- **8 and 9.** The drill tops and s217/s218 clear the caption bar. s274 now has a dashed "room" slot with an arrow, and it reads.
- Doug is on-model everywhere and the cap is always visible. The death beats stay cartoon-only, zone colours match the art bible,
  and the optional move of surface Doug in s229-s240 is done.

### Required fixes (director)
1. **s034 CRACKS, s035 FROM BELOW: wordart sits on the ice-slope outline.** Both are at `y 390, size 90`. The letter bottoms
   (about y 428) cross the top edge of the slope poly (y about 400-440 across the text span). Set `y 330` in both (the top stays at about 292, still
   clear of the meter). s036 ICE CHIMNEYS is fine.
2. **s194 COULD INCREASE: the baseline sits on the new thin-ice line (y 506), and the right end runs into the orange glow around the
   melt lens.** Move it to `x 560, y 420` so it sits in the pale band, left of the lens (lens x 1030-1330).
3. **s202 7 EMPIRE STATE BUILDINGS: the borehole (rect x 748-772) runs through the word BUILDINGS.** Same rule as the round-1 rope
   fixes. Change the text to `7 EMPIRE STATES` at `x 390, y 760, size 64` (it spans about x 90-690, clear of the hole and the building stack).
4. **Layout variety, s262-s266 (glacier grounding-line diagram, 5 in a row, all with no camera).** I missed this run in round 1. Add one
   framing change, e.g. a push-in on the reverse slope for s265 (`{"move": "zoom_in", "x": 600, "y": 760, "zoom": 1.25}`)
   so the EASIER arrows fill the frame.

### Optional (non-blocking)
- The ICE ABOVE DOUG meter sits right on the ice-surface line in the drill cross-sections (s085-s086, s154, s158, s201-s204, s228-s229,
  s233-s236, s239-s240, s242, s245, s248-s251). It stays fully legible because the box is opaque, so I'm not blocking on it. In future
  episodes, put the surface line at y ≥ 280 or ≤ 200 in shots that use the meter.

Re-render only s034, s035, s194, s202 and s262-s266 (`python -m studio keyframes 016-every-layer-of-antarctica --shots ...`). Then rebuild
the full contact sheets, because a partial render wipes them. I'll do a quick re-check of those 9 shots only.

## Keyframes round 3

Reviewer: art director · 2026-10-12 · scope: s034, s035, s138, s193, s194, s202, s261, s262-s266 (`build/keyframes`, all
rendered 17:59). `python -m studio keyframes` skips the camera for 1920x1080 canvases, so `assemble.keyframes` shows push-in shots
at zoom 1.0. To get the real end-of-move frames for s193, s194, s261 and s265, I rendered `fit_frame(img, camera_rect(cam, u=1.0))`
myself (plus u=0 for `from/to` moves). I also measured each label's pixel box on those frames against the art-bible safe area
(x 64-1856, y 40-1040). That check turned up a safe-area problem in the counter on other push-in shots that rounds 1 and 2 never
looked at, because those reviews used only the static keyframes. I list it below as fix 4.

### Verdict: FAIL (4 composition fixes, all director; no asset work)

Passed this round:
- **s034 CRACKS / s035 FROM BELOW:** at y 330 the letter bottoms sit at about y 362, about 30 px above the slope line. Pass.
- **s138 TOTAL DARKNESS:** clear of the boulder and the 260 KM label, legible on the dark water. Pass.
- **s193 MELT:** clear of the lens at both ends of the push-in. Pass.
- **s194 COULD INCREASE** (x 640, y 400): on the keyframe it spans x 315-965 in the pale band, left of the glow (about x 980). At
  the end of the push-in it spans x 75-820. Both are inside the safe area. Pass.
- **s202 7 EMPIRE STATES:** spans x 110-670, clear of the borehole and the building stack. Pass.
- **s262, s264:** pass.
- **s265:** the 1.25 static group zoom on the reverse slope gives the run its framing change, and the EASIER arrows fill the frame.
  The counter and meter sit unscaled outside the group. Pass. The s262-s266 variety point (round-2 fix 4) is closed.
- Doug is on-model with the cap visible in every shot here. Counter 131 → 138 and meter 25 m → 4,000 m are monotonic. Zone colours
  are unchanged.

### Required fixes (director)
1. **s261, end of the new push-in (`to [960, 500, 1.1]`): text is outside the safe area on both sides.** The counter's right edge
   ends at x 1903 and the meter at x 1865. The SEA LEVEL label's left edge ends at x 33. Set the label `SEA LEVEL` to `x 330`
   (keep y 330) and the camera to `{"from": [960, 540, 1.0], "to": [1008, 500, 1.1], "ease": "smooth"}`. I verified the result:
   counter ≤ 1850 and SEA LEVEL ≥ 100.
2. **s263 LIFTS OFF AND FLOATS (1600, 380): the label box's lower-left corner sits on the ice-shelf top outline.** Move it to
   `y 320`. That clears the outline and stays about 30 px below the meter box. Verified.
3. **s266: the red arrow runs behind the UNDER THE ICE box** (about x 650-760, y 820-860), so the arrow looks cut in two. Move
   `LOWEST GROUND` to `(600, 540)` and `UNDER THE ICE` to `(600, 620)`. Both then sit in clear dark ice above the arrow. Verified.
4. **Counter outside the safe area at the end of push-ins (missed in rounds 1-2, found with the camera-frame check).** On every
   zoom shot below, the camera crop pushes the DOUG DEATHS box past x 1856, and on some it also pushes the box above y 40. Change
   only the camera centre. Zoom, ease and the rest of the shot stay as they are. I re-measured every row at u = 0, 0.5 and 1 with
   these values, and every label stays inside x 64-1856, y 40-1040:

   | Shot | Now (right edge / top) | New camera |
   |---|---|---|
   | s005 | 1872 (DID NOT AGREE 1901) | `zoom_in x 1006, y 560, zoom 1.06` |
   | s022 | 1859 | `zoom_in x 970, y 560, zoom 1.05` |
   | s056 | 1900 / top 12 | `from [960,540,1.0] to [1037,565,1.14]` |
   | s057 | 1884 | `zoom_in x 993, y 600, zoom 1.08` |
   | s083 | 1874 / top 13 | `from [1023,470,1.12] to [1023,570,1.12]` |
   | s095 | 1886 | `zoom_in x 993, y 560, zoom 1.08` |
   | s112 | 1881 / top 32 | `zoom_in x 1008, y 580, zoom 1.1` |
   | s114 | 1859 / top 32 | `zoom_in x 1008, y 580, zoom 1.1` |
   | s124 | 1868 | `zoom_in x 978, y 760, zoom 1.06` |
   | s129 | 1883 | `zoom_in x 993, y 610, zoom 1.08` |
   | s148 | 1883 | `zoom_in x 993, y 610, zoom 1.08` |
   | s161 | 1902 (meter 1864) | `zoom_in x 1008, y 560, zoom 1.1` |
   | s176 | 1868 | `zoom_in x 978, y 620, zoom 1.06` |
   | s196 | start frame 1920 / top 13 | `from [1023,570,1.12] to [960,540,1.0]` |
   | s219 | 1868 | `zoom_in x 978, y 560, zoom 1.06` |
   | s239 | 1874 | `zoom_in x 1023, y 540, zoom 1.12` |

   Rule of thumb for future push-ins on shots that carry the counter: keep `cx ≥ 1817 − 890/zoom` and `cy ≤ 127 + 500/zoom`.

### Note for the engine (non-blocking, route to the showrunner)
`assemble.keyframes` applies `camera_rect(..., 1.0)` only when the canvas isn't 1920x1080, so every push-in reviews at zoom 1.0.
Rendering the end-of-move frame for every shot that has a camera (and the start frame for `from` and `zoom_out` moves) would have
caught fix 4 in round 1.

After the fixes, re-render s005, s022, s056, s057, s083, s095, s112, s114, s124, s129, s148, s161, s176, s196, s219, s239, s261, s263
and s266, then rebuild the contact sheets. I'll re-check those shots on their camera end frames only.
