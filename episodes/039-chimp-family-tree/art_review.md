# 039-chimp-family-tree: art review (art director, 2026-11-08)

**Verdict: PASS (assets).** All 24 requested drawings are APPROVED. The 4 the illustrator flagged were fixed by the art director
(engine gear plus small JSON edits). No illustrator changes are required.

Checked: the 4 preview sheets (`assets/previews/039-chimp-family-tree-*.png`), my own test renders on sand / green / olive / dusk /
night / near-black and as red-rim silhouettes, and keyframes s010, s091, s118, s152, s159, s175, re-rendered after the fixes.
Rules from CD brief section 7 hold across the set. Apes are adult, unsmiling and have no eye shine. There are no babies, bananas,
clothes on animals or gore, and no spear tip touches anything. Doug's head, face and cap stay clear and on top in every costume.

## Flagged by the illustrator

| Asset | Verdict | Notes / what I changed |
|---|---|---|
| `chimp_costume` | APPROVED (AD-fixed) | It had no leg sleeves and a narrow vest. With bare stick legs under a fringed fur skirt it read as a log or a grass skirt, not a chimp suit. **Fix 1:** new Doug gear `fur_legs` in `studio/doug.py`. It draws dark fur sleeves along both legs in any upright pose (stand, walk1/2, point, wave, run, sit, crouch), so one costume drawing fits every pose. Its outline is literal black, so it doesn't flip to white at night. **Fix 2:** I widened the vest (back edge -48 to -56, front edge +8..14 to +22..30), widened the tan chest patch and moved the back shading strip to match. The bbox is now about x -136..120. Its description says to pair it with `fur_legs`. **Fix 3:** I added `"gear": ["fur_legs"]` to all 40 Doug elements in `shotlist.json` that wear `chimp_costume`. They were matched on the same x/y/scale, so none were missed. |
| `chimpanzee_old_male` | APPROVED | It reads as older next to `chimpanzee_sitting`: grey chin tuft, grey-white ticks on the lower back, bald tan brow, heavy-lidded tired eye. It isn't pitiful or cute. Its silhouette is clean. The head top sits under the `paper_crown` in s175 exactly (checked in keyframe). No change. |
| `chimpanzee_spear_carry` | APPROVED (AD-fixed) | The folded near arm was one self-intersecting polygon, so it rendered **hollow**: a wire outline with the body showing through. I replaced it with the filled outer hull plus a 3 px fold line from hand to elbow (elements 69, 82, 83). It is now a solid dark arm on all backgrounds, and the silhouette is unchanged. The spear passes just over the crown and points forward, which is acceptable. |
| `gorilla_suit_dark` | APPROVED, plus new `gorilla_suit_dark_empty` | Worn on Doug (`sit`, s068-s071, s089-s090) it is good. It reads dark, never white, and the grey rim holds on olive. Empty at `rotate: -80` (s091), the crest/brow ridge floated loose above the hood, because it only works sitting on Doug's cap dome. I added `assets/library/gorilla_suit_dark_empty.json`, which has the same geometry and colours without the crest (elements 70-76), and switched s091's lying suit to it. It now reads as a slumped empty suit (keyframe checked). |

## All other new assets

| # | Asset | Verdict | Note |
|---|---|---|---|
| 1 | `bushbaby` | APPROVED | Big thin ears, flat stare, no shine. Silhouette reads at 0.32. |
| 2 | `red_colobus` | APPROVED | Red cap, charcoal back, pale limbs and a long tail all distinct. Reads as a monkey, not a chimp. |
| 3 | `bonobo` | APPROVED | Black face, middle-parted hair, slimmer. The pink lip line looks slightly parted at 1.0. It is not a smile, but keep it as a closed line if it is ever redrawn. |
| 4 | `chimp_head_icon` | APPROVED | Same family as `gorilla_icon`. Brow, ears and rim read at 0.3. |
| 5 | `chimpanzee_standing` | APPROVED | Bristling outline gives a clear display silhouette. |
| 6 | `chimpanzee_spear_bite` | APPROVED | Tip between the teeth and eyes down the stick. On model. |
| 7 | `chimpanzee_spear_jab` | APPROVED | Tip ends in clear air. |
| 8 | `chimp_costume_sit` | APPROVED | Name-tag area plain, cap on top. |
| 9 | `bushbaby_costume_sit` | APPROVED | Ears behind the cap, no hood eyes, tail curls in front. |
| 10 | `red_colobus_costume_sit` | APPROVED | Ruff goes round the cap, not over it. Tail to about +400. |
| 11 | `hollow_tree` | APPROVED | Broken top clear of the HUD, lip ledge at -270. |
| 12-14 | `leafy_stick`, `stripped_stick`, `chimp_spear` | APPROVED | Three stages clearly distinct. Tip uncoloured. |
| 15 | `fruit_tree` | APPROVED | Generic round orange fruit, no bananas. Trunk clear below the crown. |
| 16 | `maize_stalk` | APPROVED | |
| 17 | `maize_sack` | APPROVED | |
| 18 | `leaf_nest` | APPROVED | |
| 19 | `chimp_hand_reach` | APPROVED | Grip reads on the sign in s152. |
| 20 | `armwrestle_photo` | APPROVED | Crude Doug with a detailed-tier chimp. Doug losing is readable at 1.8. |

## Notes for the director (no blocking fixes)
1. `shotlist.json` was edited by the art director: 40 x `fur_legs` gear and s091 `gorilla_suit_dark` -> `gorilla_suit_dark_empty`.
   If you regenerate from `build/make_shotlist.py`, add `"gear": ["fur_legs"]` to every Doug that wears `chimp_costume` and keep the
   s091 swap, or these fixes are lost.
2. Keyframe review (contact sheets of the full episode) still to come at the art_approved gate. This review covers assets only.
