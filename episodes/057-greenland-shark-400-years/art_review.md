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
