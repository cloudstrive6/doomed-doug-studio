# Art review: 008 Every Step of the Ocean Food Chain, round 1 (assets)

Reviewer: art director, 2026-10-05. Scope: all new library assets from `asset_requests.md` (items 1-11) plus the
`cap_off` engine request. Keyframes are not reviewed in this round.

Checked against `channel/art_bible.md`, style bible section 7 (Art Director rules 1-9) and the director's sizes and
anchors. Sources: every `assets/previews/008-*` sheet, plus my own test renders. In those renders every costume was
worn on every pose the shotlist pairs it with. I also placed pins on the maps with the director's projection
formulas, checked the orca with `doug_cap` at (+210,-120) x scale, put Doug at the sailboat helm, checked
`cap_off` on `stand`/`wave`, and checked every `*_flat` next to an `on_back` Doug.

## Verdict: PASS (assets APPROVED), with 2 fixes I applied myself and 1 composition fix for the director

## Fixed by the art director (trivial geometry, already in `assets/library/`)
1. **`tern_costume`**: the headband bill sat at y -233..-212 and covered the lower half of the cap brim
   (y -248..-225). I lowered it to y -222..-200 (tip at (196,-210)). The brim is now fully visible, and the bill still starts
   at x +62, clear of Doug's eyes. Verified on `stand`, `float`, `panic1`, `arms_up`.
2. **`crab_costume`**: the right eye stalk curved through the cap brim tip (stalk point at (132,-232)). I lowered both stalk
   roots to y -206 and re-routed them out to x +-150..+-170, so they now pass under the brim tip and rise beside it. The eye
   balls are now at (+-166,-350) and the bbox is x -186..+186. Cap, brim and face are fully visible on `stand`, `walk1`,
   `arms_up`. The flat version is unchanged.
   Verification sheet: `assets/previews/008-art-review-costume-fixes.png`. (`008-item3-*` and `008-item4-*` still show the
   old stalks/bill. They are stale, but nothing needs redoing.)

## For the director (composition, not assets)
3. **s057, s058: `reef_fish_costume` on `pose: "cower"`**. Cower drops Doug's head into the suit, so the suit's top edge
   covers his mouth and chin. That breaks the "head, face and cap fully visible" rule. Use `float` or `stand` with
   `expression: "shock"`, which already reads fine in 15 other shots. Every other costume/pose pairing in the shotlist renders
   on-model.

## Engine request: DONE and verified
- `gear: ["cap_off"]` on non-flat poses omits the cap and draws nothing on the ground. Head and face are unchanged. Tested on `stand`
  and `wave`. The art bible already logs the rule ("Capless upright Doug (from 008)"), and the exception is in `decisions.md`.
  This no longer blocks s313, s314, s318, s319.

## Per-asset notes (all APPROVED)
| Item | Assets | Notes |
|---|---|---|
| 1 Mantis shrimp | `mantis_shrimp`, `mantis_shrimp_strike`, `mantis_arm_spring`, `snail_shell_cracked`, `highspeed_camera`, `speedometer` | Body identical in both shrimp states, so the swap is clean. Staircase size (0.17) still reads. The spring diagram is clear. The shell is honey-amber with a clean zigzag split. The speedometer leaves (0,+60) clear. |
| 2 Moray | `giant_moray`, `moray_xray`, `moray_xray_jaws_forward`, `tape_measure`, `roving_coral_grouper`, `reef_fish_costume`, `_flat` | Moray: teeth are white on a `#7a0d0d` mouth, no blood. The silhouette is long and plain, but the mouth notch identifies it once only the head pokes out of the crack (s058). X-ray pair overlays exactly. The grouper face is neutral, not friendly. On the flat costume the button eye is crossed out. |
| 3 Octopus | `giant_pacific_octopus`, `octopus_arm`, `glass_jar`, `jar_lid`, `crab_costume` (fixed), `crab_costume_flat`, `tennis_ball`, `bathroom_scale` | The octopus spans the full width and stays under 620 tall, with slit eyes and no face beyond them. The jar is outline only. Director: in the illustrator's jar preview Doug's feet poke below the jar base. Keep the brief's "feet 30 above base" in s074-s078 (I will check this at keyframes). |
| 4 Trevally | `giant_trevally`, `sooty_tern`, `tern_costume` (fixed) | Steep forehead, scowl and gold eye. Reads well both rotated and as a silhouette. The tern stays bold at 0.28. The costume wings are suitably oversized and homemade. |
| 5 Goliath grouper | `goliath_grouper`, `goliath_grouper_full`, `shark_costume`, `baby_grand_piano`, `shipwreck` | Mouth: small white teeth in a dark-red mouth, heavy and not cute. The full version has bulging cheeks and a grey felt tail tip, no blood. The shark fin stays left of the head and cap. The wreck stays mid-value and in the background. |
| 6 Tiger shark | `tiger_shark`, `tiger_shark_xray`, `tin_can`, `burlap_sack`, `sea_turtle_costume`, `_flat`, `seagrass`, `albatross_chick`, `australia_map` | Blunt snout and stripes. The silhouette is clean. The x-ray stomach is an empty oval as requested. Map pins with the 28 px/deg formula land on Kennedy River/Princess Charlotte Bay, Shark Bay, Bremer Bay and the Torres Strait gap. |
| 7 Croc | `saltwater_crocodile`, `tide_table` | Feet sit flat on y=0. The silhouette is unmistakable. The booklet has no readable text. |
| 8 Polar bear | `polar_bear`, `polar_bear_lying`, `seal_costume`, `_patched`, `_flat`, `cape_fur_seal`, `beaufort_map`, `finish_banner` | The bear has a clear dark outline, so it will read on ice. The lying bear's head is at the left. Seal whiskers sit beside the cheeks, not over the face, and `fall` rotated -20 (s247) reads. Beaufort pins: Point Barrow and the Yukon coast land on the coastline, and the pack-ice edge is at about 73.5 N. |
| 9 Great white | `great_white_shark`, `seal_island`, `seal_decoy`, `six_story_building`, `south_africa_map` | The building has exactly 6 window rows. The contact sheet crops its top row, but the asset itself is correct. Seal Island and Gansbaai pins land in and just east of the False Bay notch. |
| 10 Sperm whale | `sperm_whale_top` | Box head is on the right with white scar circles. Reads from above. |
| 11 Orca | `orca`, `orca_bent_fin`, `sailboat`, `sailboat_no_rudder`, `rudder`, `life_jacket`, `iberia_map` | Powerful, not plush. `doug_cap` at (+210,-120) x scale sits on the head. Doug at local (-20,-110) at the helm reads, with legs hidden by the hull. The life jacket works on `stand`, `wave`, `thumbs_up`. The Iberia map shows Gibraltar and North Africa. |

## Style bible 7 checks (asset-level)
- Rule 1 (two tiers): every creature, place and prop is in the detailed tier, and every costume leaves crude Doug on-model. PASS.
- Rule 2 (cap always visible): PASS after fixes 1-2. The only capless frames are the logged one-off exception.
- Rule 7 (silhouettes): every SIL asset (moray, roving grouper, trevally, goliath, tiger shark, croc, great white, orca) has a
  clean, recognisable outer shape. PASS.
- Rule 8 (no gore): no blood, wounds or carcasses anywhere. Flat costumes use X eyes only, with no tears. PASS.
- Rules 3-6 and 9 apply at keyframe level and will be checked in round 2.

ASSETS: APPROVED (pending director fix 3 at keyframes)
