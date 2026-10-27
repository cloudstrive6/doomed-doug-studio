# 028-megalodon-every-era: art review (new assets)

Reviewer: art director, 2026-10-27
Scope: the 24 new library drawings in `asset_requests.md` (previews `assets/previews/028-megalodon-every-era-assets-*`).
Checked against `channel/art_bible.md`, style bible section 7 (Art Director rules 1-9) and Doug's locked design.
Extra checks rendered with `python -m studio art`: the new creatures side by side with the library `megalodon`,
`tylosaurus` and `ichthyosaur` on `#2a6aa6`; the two humans next to Doug at large scale; `mosasaurus` flat and tilted
-50 degrees on near-black; both Panama maps at 0.62. Local extents of all 24 JSONs checked against the requested
anchors.

## Verdict: PASS (all 24 APPROVE; 3 small direct fixes applied, no illustrator rework needed)

| # | Asset | Verdict | Notes |
|---|---|---|---|
| 1 | `shark_cage` | APPROVE | Bars only, Doug clearly visible through them; cap on the roof and Doug seated on the roof both work. Reads on cyan, olive, mid-blue and `#050a1f`. Shackle at (0,-470), extent -162..156 x -470..0. |
| 2 | `megalodon_pup` | APPROVE | Same family as `megalodon` (slate back, countershading, pale belly), mouth closed, hard eye with a brow: menacing, not cute. The black silhouette with a white rim still reads as a shark. |
| 3 | `mosasaurus` | APPROVE (fixed) | Blunt deep skull, no rostrum, so it clearly differs from `tylosaurus`. Reads when tilted and as a red-rim silhouette. **Fixed:** the two far-side flippers sat directly behind the near ones, so only 2 of 4 showed. I moved them 48 units toward the tail so all four paddles read. **Fixed:** three back spray patches spilled dots outside the outline, visible on light water. I moved them down 22 units and set r 44 to 34. Extents unchanged. |
| 4 | `mosasaurus_skull` | APPROVE | Museum fossil on a limestone block, cream bone, not gory. The engraving hatch is light; this is fine at the s039-s045 sizes. |
| 5 | `ichthyotitan` | APPROVE | Bulkier and longer than `ichthyosaur`, with a small eye as requested. Reads as a ceiling at 1.6 and as a silhouette. |
| 6 | `ichthyotitan_jaw` | APPROVE | Long curved bone with glue-crack lines, no teeth. Reads on mid-blue and navy. |
| 7 | `fossil_hunter_girl` | APPROVE | Crude tier with Doug's head, crescent and oval eyes; ponytail, bone in hand. Plain and not kids-show. Her silhouette reads as a child. |
| 8 | `fossil_hunter_dad` | APPROVE | Crude tier, short hair, jacket, hammer. On-model next to Doug. |
| 9 | `sun_hat` | APPROVE | Sits above the cap, and the red dome and brim stay visible (rule 2). Works with `doug_sunglasses`. |
| 10 | `livyatan_skull` | APPROVE | Massive toothy skull in sand with cream teeth in both jaws. Not gory. |
| 11 | `orca_tooth` | APPROVE | Clean cartoon tooth with a crown/root split. |
| 12 | `orca_tooth_worn` | APPROVE | Flat worn top with a pink gum band. Not medical. The gum runs to y +130 (asked 120), which does no harm. |
| 13 | `toothbrush` | APPROVE | Bristles are small, but the shape reads as a toothbrush down to scale 0.4. |
| 14 | `rubber_duck` | APPROVE | Classic shape, bold silhouette. |
| 15 | `statue_of_liberty` | APPROVE | Instantly recognisable. Copper green with a shaded side, torch tip at -620 (the glow reaches -640). |
| 16 | `beringia_map` | APPROVE | `world_map` style, tan bridge in the centre, dashed modern coast. |
| 17 | `panama_seaway_map` | APPROVE (fixed) | Open gap at the centre, with Pacific bottom-left and Caribbean top-right. **Fixed:** a land spray at (-560,-330) r110 leaked green dots above the black frame (y -440). I changed it to (-560,-300) r100. |
| 18 | `panama_isthmus_map` | APPROVE (fixed) | Matches the seaway map, and the canal and lake read. Same frame-leak spray fix as #17. |
| 19 | `container_ship` | APPROVE | Containers, red bottom and stern bridge all read at small size. |
| 20 | `hms_challenger` | APPROVE | A period corvette (white band, gun ports, three masts, funnel) that is clearly not `research_ship`. |
| 21 | `manganese_tooth_nodule` | APPROVE | Rings around a pale tooth, and the pale rim reads on dark water. |
| 22 | `megalodon_vertebra` | APPROVE | End-on disc with strong growth rings. |
| 23 | `stone_tool` | APPROVE | Faceted flake scars and a pale working edge. It reads as a "rock", which is right for a Lomekwi core. The narration and label carry the rest. |
| 24 | `sea_turtle` | APPROVE | Shell scutes, four flippers, bold silhouette. |

## Style consistency
- Two-tier rule (section 7.1) holds. All creatures, props and places are in the detailed tier. Both humans are crude stick figures with the same head, crescent and eye language as Doug. Doug's locked design was not touched.
- Gore (7.8): none. Mouths are dark red interiors, with no blood anywhere.
- Silhouette and rim use (7.7): `megalodon_pup`, `mosasaurus` and `ichthyotitan` all keep a readable outline when blacked out.

## Fixes applied directly (for the record)
1. `assets/library/mosasaurus.json`: shifted far-side flippers (elements 0, 1) by -48 x. Moved back sprays 35-37 down 22 units with r 34.
2. `assets/library/panama_seaway_map.json`, `assets/library/panama_isthmus_map.json`: moved the top-left land spray inside the frame.

## Open items
- None for the illustrator.
- Director: the shotlist validator currently flags `s001: scene_ref 'thumbnail' file missing`. This is expected until the graphic designer delivers `thumbnail.json`, and it is not an art issue.
- Keyframe review (contact sheets) is still to come after `python -m studio keyframes`.
