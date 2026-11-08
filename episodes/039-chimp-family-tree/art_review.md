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

---

# 039-chimp-family-tree: keyframe review (art director, 2026-11-08)

**Verdict: FAIL (keyframes).** 6 blocking fixes across 34 shots, all composition, all routed to the **director**. No asset
fixes are needed. The style holds well overall. Every chapter has its own ground colour, and they darken in order: sand,
sky/green, sage/olive, orange, peach, rust/maroon, dusk purple, navy night, near-black. The two tiers stay apart (crude Doug,
detailed apes). Doug is on-model with his cap visible in every shot, costumes included. The death beats are consistent
(silhouette plus a lone cap), and the counter steps once per death, 301 to 308 (s024, s072, s095, s135, s154, s177, s203).
The family-tree HUD and the SPLIT tag update per chapter. There is no gore, and every reveal uses a silhouette before the
colour shot.

Checked: all 18 contact sheets (s001-s208 plus the endslate), and 1080p crops of s003, s029, s051, s077, s086, s111, s112,
s118, s122, s131, s160, s174, s180, s183 and s200. Coordinates below are at 1080p. The HUD tree panel is the rect at
x 1090-1228, y 98-266.

## Blocking fixes (director)

1. **The split line runs through Doug's body: s003, s004, s122, s200, s201, s202.** The full-height white or black line is drawn
   through his head, torso and legs. In the spear episode it reads as Doug skewered on a pole. Stop the line at the ground line under
   his feet, or leave a gap at least 40 px wide around his whole figure (cap top to feet), and draw it before Doug. In s122, also
   raise Doug so his feet are at y ≤ 1000. Right now they are at about y 1060, outside the safe area. The cap-on-the-line shots
   s203, s205, s207 and s208 are fine as they are.
2. **The BONOBO name tag covers Doug's face: s111, s112, s113.** The label at (975, 930.6) sits across his eyes. The art bible
   says nothing crosses his face. Move it to his chest, at y about 985 below the chin, or beside him with a short tie line. In s111
   (the shot that introduces the gag), raise Doug and the `chimp_costume_sit` to scale about 0.6 so the tag reads. End the red
   arrow on the tag; at the moment it points at empty grass.
3. **Map frames run under the HUD tree panel: s029, s051, s085, s086, s103.** The `africa_map` right edge is at about x 1105, under
   the panel (art bible, Recurring layouts: map assets count as inset frames). Shrink the map to about 0.8 and shift it left so the
   frame's right edge is ≤ x 1060, or start it at y ≥ 290. Check the rendered frame line in pixels.
4. **Text touches the HUD tree panel: s131, s145, s160, s162, s174, s183.** The wordart "THE SAFE OPTION" (s131), "WELCOME HOME"
   (s174) and "EXILED" (s162), the labels "FOUDOUKO" (s160) and "SINCE 2018" (s183), and the bar value "37" (s145) all butt
   against or overlap the panel's bottom edge. Keep glyph or box tops at y ≥ 290 wherever they overlap x 1070-1250. In s145, either
   shorten the red bar and put "37" at y about 340, or move the chart left so the bar ends at x ≤ 1060.
5. **Six chalkboards in a row: s167-s172.** This breaks the variety rule (never the same composition 5 times running). s169 adds one
   line to s168, s170 adds only a wordart, and s172 adds a wordart and a "!". Keep s168 and s171 as boards. Re-stage s170 ("nobody
   had ever recorded an exile this long") as Foudouko alone at the edge of the night ridge with the 5 year-calendars, or as a timeline.
   Re-stage s172 ("competition for mates is fierce") on the night set with the younger males facing the old male. Either s169 or
   s170 can then drop its board entirely.
6. **Text crosses props or labels are cut by lines: s005, s157, s077, s078, s079, s196, s197, s198.** "DISTANT RELATIVES." (s005)
   runs over the hollow tree's broken top. The "THE OLD KING" title (s157) runs into the tree crown. Move both into clear sky.
   On the gorilla/chimp/human fork diagram (s077-s079), the branch lines cut through GORILLA, CHIMP and HUMAN. On the tree
   (s196-s198), the trunk cuts through "SAME GROUP". Put each label beside its branch tip, or give it a cream `label` box as
   s204 already does. s204 is the model for this fix.

## Should fix (director, non-blocking)

7. s046: a lone cap on the branch is our death symbol, but the counter stays at 302 ("Doug is fine" was the beat before). Either
   show Doug on the branch, or remove the cap.
8. s184-s186: the Ngogo community is drawn as tan dots, while s180, s182 and s183 use chimp-head icons for the same 200 animals.
   Use the head icon here too (dots are fine for the playground kids in s187-s188).
9. s042 "SAFEST SPOT" sits over the left canopy, s132 "WRONG SIDE" overlaps the left tree crown, and s054 has "2014-2018" with
   tally marks on the fruit canopy. Move each into clear sky (art bible: no wordart on leaves).
10. s087 shows 3 keyword labels (ROADS, PATHS, FIELDS); the maximum is 2. Drop PATHS, since the path is visible in the shot.
11. s041 is nearly a copy of s038 (same clipboard and chart). Swap in a different layout, for example Doug holding a "FIRST" sign or
    the colobus row with red Xs, to break the 4-of-5 chart run from s037 to s041.
12. s199 (the endangered card) has no caption bar or HUD, although it sits inside THE SPLIT. If the sombre bare card is deliberate,
    keep it. Otherwise add the caption bar (style bible 7.3).
13. s018: Doug is tiny and wedged against the sitting chimp's feet. Give him clear space (x about 1200) at his usual scale of about 0.36.

## Notes
- The bonobo lip (asset note 3) reads as a neutral closed mouth at s100-s104 scale. No change.
- Doug in the chimp costume on the dark brown patrol ground (s118, s119, s121, s128) reads through the tan chest patch and the
  white head. Acceptable.
- After fixes, re-render only the affected shots (`keyframes 039-chimp-family-tree --shots ...`) and send the sheets back for a
  quick recheck. The shot ids to re-render are s003, s004, s005, s029, s051, s077, s078, s079, s085, s086, s103, s111, s112,
  s113, s122, s131, s145, s157, s160, s162, s167-s172, s174, s183, s196, s197, s198, s200, s201 and s202, plus any of 7-13 that are taken.
