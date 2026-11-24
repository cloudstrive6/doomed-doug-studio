# 057-greenland-shark-400-years: art review, assets (art director, 2026-11-24)

Reviewed: `assets/previews/057-greenland-shark-400-years-assets-a.png` / `-b.png` (15 new assets), compared with
`assets/previews/057-ref.png` (library `greenland_shark`, 051 `seal_costume_prone`, `ringed_seal`), and **in context** on 12 test
keyframes (s002, s007, s020, s021, s027, s079, s087, s088, s115, s124, s187, s205; scratch, `build/keyframes/`) at 1080p, including
2x crops of the HUD and the costume. Checked against the art bible and style bible section 7 (Art Director rules 1-9).

## Verdict: PASS (assets), with 2 required illustrator fixes

13 of 15 assets are APPROVED as drawn. `shark_age_icon` (approved as a device, icon needs a readability pass) and `shark_meat_slab`
need fixes. Neither fix changes an anchor, bbox or key point, so **keyframes may proceed now**; the fixed drawings must be in the
library before the final render. Nothing gory, nothing cute, every creature on the detailed tier against crude Doug (rule 1), the
shark family stays in the library `#6e6a64` grey-brown, and everything reads on `#3a9ad9`, cream `#f4f1dc` and dark backgrounds.

## Explicit decisions requested by the CD

### A. SHARK AGE card (`shark_age_icon` + `SHARK AGE: <n>` label): APPROVED as a device, icon fix required (illustrator)
The device is approved: it sits in the established second-meter slot (size-28 label at (1590,238), icon at 0.16 to its left, like 022's
stopwatch and 049's target), it is a different object from the death counter, the values with `~` and `(±120)` keep the science honest,
and the red-on-pink switch at the s187 reveal plus `+ 1 MIN` on the LIVE feed is a good closing beat. The label is legible on every
tested background. Recorded in the art bible (Recurring layouts, "SHARK AGE").

But at 32 px the icon only half-reads (s002 crop): the **candle flame disappears completely**, the fin is a speck, and the text lines on
the left panel plus the blue water squiggle under the fin turn into noise. Fixes (`assets/library/shark_age_icon.json`):
1. Flame about 2.5x bigger: a yellow `#ffe24a` teardrop with a black outline (4) so it survives on `#cfe9ff`, `#3a9ad9` and dark beats.
2. Candle about 1.5x thicker, keep red/white stripes (2-3 stripes only).
3. Fin about 2x bigger, solid `#6e6a64` with black outline, filling ~60% of the front panel height.
4. Delete the text lines on the inside panel and the blue water squiggle under the fin.
Keep the card shape, cream `#fff6dc`, outline 6, anchor and bbox. Re-run `python -m studio asset-preview shark_age_icon --scale 0.16`
and check it at actual size.

Director fixes for the device (shotlist generator):
5. **s187: two icons on screen.** The old icon at (1399,238) stays while the second one appears at (1338,238) with `appear: 0.3`, and the
   widened red label covers the old one. Exactly one icon per shot: drop the old icon in s187 (or start the shot with the icon already at
   the new x).
6. Icon gap: for the `~392 (±120)` label the icon right edge is ~58 px from the label box (s188-s206); move it to ~30 px (about x 1366)
   so it matches the earlier values (s002 gap is right).

### B. `harp_seal_costume_prone`: APPROVED
It clearly reads as a different suit from 051's: pale silver felt vs. grey; a big black horseshoe saddle with white stitching vs. pale
speckles; a black mask hood round Doug's head vs. a grey hood. At scale 0.6 on the floe (s087, s088) the saddle is the first thing you
see. Doug's head, sleepy face and red cap are fully visible (rule 2), the suit slots onto the `on_back` rig correctly, the tail flippers
sit past his feet. No fix needed. Recorded in the art bible (harp suit vs. 051 suit, never mixed in one episode).
Nit (optional): the small white spray patch in the middle of the belly reads as a smudge at 0.6; it can go.

## Per-asset results

| # | Asset | Result | Notes |
|---|---|---|---|
| 1 | `shark_age_icon` | FIX | See A, fixes 1-4. |
| 2 | `greenland_shark_head` | APPROVED | Matches the library shark exactly (palette, spots, gill slits); dot eye clean, no damage; closed underslung mouth. The shading spray bleeds a little outside the outline at the top edge, as on the library shark, so it is consistent; not required. |
| 3 | `greenland_shark_face` | APPROVED | Wide flat head, far-apart dot eyes, closed mouth, no teeth. Slow and menacing. |
| 4 | `eye_copepod` | APPROVED | Pale streamer, segment lines read at 1.9 (s007) and on the eye at 1.15 (s020); no wound, no red, no hooks. |
| 5 | `eye_copepod_wave` | APPROVED | Raised leg reads at 1.0 in s020 ("hi friend?"); no face, deadpan. |
| 6 | `greenland_shark_pup` | APPROVED | Plain dot eyes, no smile; reads at 0.13. Director note for s027: the pups have the same value as the mother's body, so give the dotted womb oval a pale cream `#f4f1dc` fill (as the stomach card in s079 does) so the ten pups pop. |
| 7 | `harp_seal` | APPROVED | Black mask and harp saddle read at a glance; clean silhouette works as the s079 black cut-out. |
| 8 | `harp_seal_sleeping` | APPROVED | Bottling pose reads in s087. |
| 9 | `harp_seal_costume_prone` | APPROVED | See B. |
| 10 | `birthday_cake_candles` | APPROVED | Lopsided two tiers, a forest of striped candles, pale blue drip, no text, no sprinkles: office party, not kids' party. |
| 11 | `birthday_cake_upside_down` | APPROVED | Reads as a squashed upturned cake; the cap sits well on the board inside the `crt_tv` (s205). |
| 12 | `shark_meat_slab` | FIX | See fix 7. |
| 13 | `hakarl_drying_shed` | APPROVED | Slats, corrugated roof, hanging cream strips all read in s124. |
| 14 | `hakarl_cube` | APPROVED | Cube on a toothpick reads at 0.5. (Keyframe note for the director: in s124 it floats beside Doug, not in his hand.) |
| 15 | `trawl_net` | APPROVED | Cone mesh, floats and weights read; cod end left, mouth right as requested. |

7. **`shark_meat_slab` (illustrator):** on the plate (s115) it reads as a bar of soap or a bread roll, not meat, and "THE MENU" depends
   on it reading as shark. Also the darker skin band is on the front side with chevrons, not along the top as requested. Fix: make it a
   fillet/steak shape (irregular, one end thicker, one angled cut face), put the muscle flake lines (W/chevron myomere lines, grey
   `#b8b4aa`) on the **top cut face**, and run the darker `#b8b4aa` skin strip along the top back edge only. Keep it pale grey-white
   `#d8d6cf`, no red, no bone, same anchor and about 420x200.

## Routing
- Illustrator: fixes 1-4 (`shark_age_icon`) and 7 (`shark_meat_slab`); re-preview both, no anchor changes.
- Director: fixes 5-6 (s187 double icon, icon gap), plus the s027 womb fill and the s124 cube placement notes for the keyframe pass.
- Keyframe review follows separately once the full set is rendered.

---

# 057 keyframe review (art director, 2026-11-24)

Reviewed: all 18 contact sheets in `build/contact/` (s001-s208 + endslate, fresh full render, final assets), plus 1:1 crops of the
full-res keyframes for the HUD icon, s115, s124, s131, s138, s043, s053 and s205. Nothing re-rendered.

## Verdict: FAIL (director: 1 composition fix, 3 text-collision fixes; assets PASS)

Style, Doug and colour are solid across all 208 shots. Doug is on-model in every shot (cap always visible, including the ghosts in
s021/s089/s184/s205-s208 and the X-eyes in s063-s065), the `sunburn` + `sweat` gear in s137-s139 is the approved gear used correctly, the death
counter runs 414 → 420 on the right beats (s021, s063, s089, s112, s183, s204), and SHARK AGE runs `?` → 0 → ~10 → ~50 → ~100 → ~150 → ~250 →
~392 (±120) without a skip. The ocean ramp is correct: surface `#3a9ad9` for all cold/under-ice water (s165-s166 included, which matches the
bible rule), with the twilight and midnight bands spent only on the descent (s163-s164, s178-s184). Silhouette-then-reveal is used
correctly (s004, s088, s111, s184, s201-s204). No gore anywhere: the reindeer arrow in s091 points at the animal, not a wound, and every
death is a cap, a splash or a blackout.

## Asset verification

- **`shark_age_icon`: PASS.** Fixes 1-4 are in. At actual size (checked 1:1 on `#cfe9ff` s002, near-black s021, midnight s183 and grey s205)
  the yellow flame with black outline now reads on every background, the fin is a clear grey triangle filling the front panel, and the
  panel text lines and water squiggle are gone. Director fixes 5-6 are in too: s187 now has exactly one icon at x 1367, and the gap to the
  `~392 (±120)` label matches the earlier values.
- **`shark_meat_slab`: PASS.** In s115 it now reads as a fish fillet on a plate: an irregular loaf with one thicker end, the angled cut face
  on the right, and grey W/chevron flake lines on the top face. Pale grey-white, no red, no bone. "THE MENU → THE MEAT" now lands. (Nit, not
  required: the darker band now runs along the lower side rather than the top back edge. It still reads as skin vs. flesh, so leave it.)
- Earlier keyframe notes are done: s027 womb oval is pale-filled so the ten pups pop, and in s124 the hákarl cube is now in Doug's hand.

## Required fixes (director, `build/gen_shotlist.py` → shotlist)

1. **s115-s120: the same composition six times in a row** (slab centre-left, Doug right, one sign above, one label below). s118 and s120
   are near-duplicates. Keep s115-s118 as they are and re-stage the last two:
   - **s119 (urea / TMAO):** close-up. `shark_meat_slab` at about scale 2.0 filling the left 60 % of frame, cut face visible. Two red
     curved arrows run into the flesh from `UREA` (upper left) and `TRIMETHYLAMINE OXIDE` (lower right). Doug small, bottom right,
     `flat`. No warning triangle in this shot.
   - **s120 (HAZARDOUS):** a different layout. Doug big (scale ~0.7) centre-left, `gritted` + `sweat`, arm out holding a fork with a small
     slab chunk at arm's length. A big yellow warning triangle behind/right of him, and `HAZARDOUS` WordArt bottom right. No plate.
2. **s053, s054: the vertical divider line cuts through the "R" of `4 CM A YEAR`.** Move the label left so its right edge clears the divider
   by ≥ 30 px (or move the divider to x ≥ 1020 in s053's frame coordinates). Same fix in both shots.
3. **s131: the `2014` date tag covers the newspaper masthead** ("THE DAILY N…"). Move the tag to sit above the paper's top-right corner
   (as on the 1957/2016/2020 papers in s026, s145, s148), or shorten the masthead so the tag no longer overlaps it.
4. **s043: the `WELCOME` text is not rotated with the fallen banner.** It sits horizontal and spills off the board's top edge. Rotate the
   text with the board (same angle, same centre), or make it a separate rotated `text` inside the board.

## Nits (optional, do them if you are already touching the shot)

5. s003: the red down arrow's shaft passes over the final "E" of `BIRTHDAY CAKE`. Move the arrow ~40 px right.
6. s096, s110: the `POLAR BEAR (REMAINS)` row is a smaller font than the other "FOUND INSIDE" rows. Use one size for all rows (shrink
   all to fit, or widen the card).
7. s192 (and s193): the three biggest sharks overlap each other in a pile-up. Widen the x steps or reduce the top scale so each shark
   has its own space.
8. s187/s188: `~392 YEARS` crosses the dorsal fins. It is legible because of the black outline, so no fix is required. If you move it,
   y ≈ 330 clears the fins.

Variety elsewhere is fine. The repeated giant-head shots (s006-s016) are broken up by s007/s009/s012-s015, the reveal build s185-s188
earns its repetition, and the A/A' hold pairs (s041-s042, s061-s062, s158-s161) are deliberate.

## Routing
- Director: fixes 1-4 (and nits 5-8 if convenient). Then re-render only `--shots s043,s053,s054,s119,s120,s131`
  (plus s003,s096,s110,s192,s193 if the nits are taken) and send the new sheets back for a quick re-check.
- Illustrator: nothing. Both re-drawn assets pass.
- Graphic designer: s001 is still `(thumbnail pending)`. That is expected at this stage, but it must be filled before the final render.

---

# 057 keyframe review, round 2 (art director, 2026-11-24)

Reviewed: all 18 fresh contact sheets in `build/contact/` (s001-s208 + endslate, rendered 18:06 after commit `51970f2b`), the
new-asset preview `assets/previews/057-greenland-shark-400-years-assets-fix.png`, and 1:1 crops of s028, s046, s120, s137, s176
and the s187 HUD from `build/keyframes/`. Checked against round 1 above and `visual_review.md` round 1. Nothing re-rendered.

## Verdict: FAIL (1 required director fix: s137; everything else PASS)

Every round-1 art fix and every visual-review fix I re-checked is in. One new problem: the new plate in s137 sits on the floor
instead of the counter. It is a one-shot placement fix.

## New assets: PASS (all three)

- **`ruler_40cm`: APPROVED.** Same yellow ruler and footprint as `ruler`, 0-40 cm in 5s, numbers legible at 1:1. In s028 the pup
  now runs from about 1 to about 37, so "37 CM" matches the drawing. Leaving `ruler` (0-30) alone is correct; s045/s048 use it with
  no number claim.
- **`heart_monitor_slow`: APPROVED.** Same body as `heart_monitor` with a green flat trace and one blip on a dark screen. In s167
  and s168 it reads as a heart monitor straight away. It no longer looks like a microwave.
- **`hakarl_plate`: APPROVED as a drawing.** Pale cube with flake lines, a toothpick and a white plate, all on-palette. At 0.55 the
  cube is about 82 px. That is what was asked for, and it reads as one cube of food. (Placement problem in s137: see fix 1.)
- `hakarl_cube` (enlarged): reads in Doug's hand in s124. Approved.

## Round-1 fixes verified

| Fix | Shot(s) | Result |
|---|---|---|
| AD 1: meat run variety | s115-s120 | PASS. s116 is now the shark face + warning, s119 is the UREA / TRIMETHYLAMINE OXIDE close-up (slab about 2.0, Doug tiny bottom right), s120 is Doug big with `gritted` + `sweat`, arm out, chunk on a fork, big triangle, HAZARDOUS. No more than two similar frames in a row. |
| AD 2 / VR 8: divider vs. label | s053, s054 | PASS. `4 CM A YEAR` clears the divider in both shots. `4X FASTER` is on the fingernail side. |
| AD 3 / VR 15: 2014 tag | s131 | PASS. Plain document + `ICELAND GOV.` + flag; the tag sits above the top-right corner. |
| AD 4 / VR 7: WELCOME | s043 | PASS. Text rotated with the fallen board. |
| Nits 5-8 | s003, s096/s110, s192/s193, s187/s188 | PASS. The arrow clears the E. One font size for all FOUND INSIDE rows. Sharks have their own space, and the BORN BEFORE box wraps separate shapes. The wordart is up in clear water above the fins. |
| VR 1: last death | s204 | PASS. Cap on a dashed line, cake sinking, faint shark outline, counter 420 in red. No longer a black frame. |
| VR 3/4: variety | s185-s188, s061-s065 | PASS. s187/s188 are the eye close-up (A/A' pair, deliberate). s064 is the underwater nose-against-tape close-up. |
| VR 6, 9-14, minors | s192-3, s028, s137, s046, s030, s027, s015, s167, s022/s090, s194, s101, s158, s013, s203 | PASS, except s137 (fix 1). The calendar page in s046 is now readable in the open sky. There is one cap per post-death frame. WHALE MEAT is labelled. The s158 tail is in frame. The map inset sits by WESTERN GREENLAND. The s203 slab tilts. |
| HUD | all | PASS. Exactly one `shark_age_icon` per shot (s187 checked 1:1). Counter 414 → 420 on s021/s063/s089/s112/s183/s204. SHARK AGE runs ? → 0 → ~10 → ~50 → ~100 → ~150 → ~250 → ~392 (±120) → `+ 1 MIN`. |

Doug is on-model in every shot. The cap is always visible, including the ghosts and the submersible porthole. Zone colours follow
the bible, with surface `#3a9ad9` under the ice and the depth ramp only in The Deep. There is no gore anywhere.

## Required fix (director, `build/gen_shotlist.py` → shotlist)

1. **s137: the plate is on the floor, not on the counter.** `hakarl_plate` is at (1130, 830). That is floor level, just past the
   counter's right edge, so the plate overlaps the cupboard door and the cube is level with Doug's knees. "Doug has ordered one cube"
   needs it served on the worktop. `kitchen_counter` at (760, 900) scale 1.6 has its worktop surface at y ≈ 516 (x 440-1080).
   - Move `hakarl_plate` to about **(960, 518)**, scale 0.55 unchanged.
   - The cube top then reaches y ≈ 390, so move the `HÁKARL: TRADITIONAL` label up to **y ≈ 290** and it will not touch the cube.
     The flag stays where it is.
   - Re-aim the red arrow so it ends about 20 px from the cube's right face, coming from the right at y ≈ 450-470
     (e.g. (1210, 470) → (1060, 440)). Do not cross the flagpole or the label.
   - Optional (VR 10 asked for it): Doug's expression `flat` → `worried` / uneasy.
   Re-render `--shots s137` only and send the sheet back for a quick look.

## Nits (optional)

2. s098: the `HUNDREDS OF M` label looks cut off. Write `HUNDREDS OF METERS` (it fits at size 40).
3. s120: the fork reads more like grey tongs, and the speed lines behind the chunk make it look thrown. Drop the speed lines if you
   are touching the shot anyway. The pose and the warning read fine as they are.

## Still open elsewhere (not art)
- s001 is still `(thumbnail pending)` (graphic designer; needed before the final render).
- Contact-caption font shows "h?karl" (editor: confirm the á glyph in the subtitle font). The on-frame HÁKARL is correct.

## Routing
- Director: fix 1 (plus nits 2-3 if convenient). Re-render `s137` (and `s098`, `s120` if touched).
- Illustrator: nothing. All three new assets pass.
