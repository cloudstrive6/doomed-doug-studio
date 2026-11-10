# 043 art review: new assets (art director, 2026-11-10)

**Verdict: PASS** (32/32 approved; two trivial fixes applied by the art director, listed below).

Checked: the 9 previews in `assets/previews/043-*`, plus my own test renders. These covered the hanging and flying bats, the colony,
the stalagmite and the virus on cave #3b2a17 and IR green #2a3a2e, next to Doug for scale. I also rendered silhouette-with-glow tests
for fruit_bat_flying, chicken_coop, wooden_shed and brown_dog_sitting, Doug seated in diner_booth with burger_plain on the table, flea
beside sesame_seed at the same scale, broom rotated, the farm animals at 1.3-2x, and the hanging bat downscaled to 168x94.
Both tiers hold: the creatures and props have interior shading, layered fills and bold 4-5 px outlines against crude Doug. All are on
the requested hexes. There is no gore and no symptom imagery, and the germ is faceless.
Per the brief, the carriers look ordinary and calm, not cute: small dark eyes with no shine, no blush, no tongues.

## Fixes applied by the art director
1. **pig**: the mouth curve dipped in the middle and read as a smile, which breaks the "never cute, no smiles" rule. I flattened it to
   a straight, slightly downturned line (element 26). The anchor and footprint are unchanged.
2. **goat**: the horn floated just above the skull at scale (a visible gap). I moved the horn by (+10,+14) so its base tucks under the
   head outline. The anchor and footprint are unchanged.

## Per asset
| # | Asset | Result | Notes |
|---|---|---|---|
| 1 | fruit_bat_hanging | APPROVE | Reads as a bat on both cave and IR. The face is the right way up for an inverted head. The preview sheet crops its head because the cell assumes bottom-centre anchors, but the asset is fine. See thumbnail note T1. |
| 2 | fruit_bat_flying | APPROVE | The silhouette reads clearly as a bat with the red glow. |
| 3 | bat_ceiling_colony | APPROVE | |
| 4 | bat_ceiling_colony_stir | APPROVE | Clearly different from #3: wings flicked. |
| 5 | stalagmite | APPROVE | Flat tip suits the cap. |
| 6 | europe_map | APPROVE | Pin coordinates match the projection. Germany and Serbia are highlighted. |
| 7 | malaysia_map | APPROVE | Frame is off-centre as the request specified. See director note D1. |
| 8 | netherlands_map | APPROVE | Oss at (39,90) checks out. |
| 9 | date_palm_tapped | APPROVE | |
| 10 | clay_sap_pot | APPROVE | The spout rises above the rim. Hang the cap on the rim, not the spout. |
| 11 | sap_cup | APPROVE | |
| 12 | flour_bag | APPROVE | |
| 13 | pig | APPROVE (fixed) | Fix 1. |
| 14 | virus_blob | APPROVE | Still reads at 0.25. |
| 15 | temple_stairs | APPROVE | No symbols and no text. |
| 16 | goat | APPROVE (fixed) | Fix 2. |
| 17 | chicken_coop | APPROVE | The props sheet crops its roof, but the full render is correct and the silhouette reads. |
| 18 | straw_nest_eggs | APPROVE | |
| 19 | burger_plain | APPROVE | |
| 20 | diner_booth | APPROVE | Seat and table heights verified with a seated Doug. |
| 21 | wooden_shed | APPROVE | The silhouette reads. |
| 22 | wooden_shed_open | APPROVE | |
| 23 | deer_mouse | APPROVE | |
| 24 | mouse_nest | APPROVE | |
| 25 | broom | APPROVE | |
| 26 | medieval_town_skyline | APPROVE | The tower has a clock face, with no cross or flags. |
| 27 | ground_squirrel | APPROVE | Upright and intact, fine as the doormat "present". |
| 28 | flea | APPROVE | Matches sesame_seed at the same scale. |
| 29 | brown_dog_sitting | APPROVE | Non-blocking: the forelegs are two stiff rectangles. Illustrator may soften them in a later pass. |
| 30 | brown_dog_sleeping | APPROVE | Consistent with the other two dog poses. |
| 31 | brown_dog_walking | APPROVE | |
| 32 | cardboard_box_open | APPROVE | |

## Notes for the director (composition, not blocking)
- D1. **malaysia_map**: to centre the map in frame, offset placement by (-40,-30). The pin is at (-260,20) relative to the anchor.
- D2. Several animals run up to 20% over their requested boxes (pig, goat, deer_mouse, brown_dog_walking, brown_dog_sitting). Keep
  them clear of the caption bar and the safe area when the keyframes come in.
- D3. On cave #3b2a17 at small scales the bat's dark wings (#4a3c34) merge with the background, though the body and face still read.
  For the colony and other small-bat shots, use the lighter IR green or a light rim if they look muddy in keyframes.

## Note for the graphic designer
- T1. Thumbnail hero (fruit_bat_hanging): at 168x94 on #3b2a17 the wings sink into the background. Use a flatter, lighter background
  (Archetype C), or add `"rim": {"color": "#ffffff", "px": 4}`, so the silhouette pops in the feed.
