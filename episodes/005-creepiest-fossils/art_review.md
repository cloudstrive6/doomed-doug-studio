# Art review: 005 Creepiest Fossils (new assets)

Reviewer: art director · Date: 2026-10-01 · Scope: the 44 new library assets in `asset_requests.md`

## Verdict: FAIL (REVISE 2 of 44; 42 APPROVED, 1 fixed by the AD)

How I checked: I rendered each asset at scale 1 with its requested box and anchor drawn on top, on its shot background
(night hall `#2c3350`, ocean ramp, near-black `#0b1018`). I zoomed in on every mummy and baby animal to check gore and kid appeal.
I tested the SIL assets with `silhouette: true`, borealopelta at `rotate: 180`, and the foal at -9 degrees. I also diffed both matched pairs.

Preview note: `assets/previews/005-creepiest-fossils-assets-b.png` was overwritten by the section 8-12 sheet, so the
museum-to-sauerkraut sheet listed in asset_requests.md no longer existed. I regenerated it as
`assets/previews/005-creepiest-fossils-assets-a.png` (scale 0.7).

## Gore / kid appeal
- Pass across the set. No blood, wounds or exposed tissue anywhere. The test tubes are a flat cartoon `#8a1a1a` with no splatter, and the stew has no meat detail.
- The baby animals are not cute. `cave_lion_cub` has a grumpy, heavy-lidded stare, `baby_mammoth` has a frowning brow, and the
  mummies are dark and dry with closed slit eyes. None of them uses pastel colours or big shiny eyes.
- `wolf_pup_mummy` passes on gore but fails on recognisability (see the REVISE list).

## squid_costume_flat: APPROVED (worn-prop family)
It is on-model with `squid_costume`: same cardboard `#c89a5e`-family fill, the "SQUID" marker text, tape patches and fins. It is
horizontal, crushed and folded, and the tentacles trail limp. One marker X is drawn over the old scribbled eye and a second X sits beside it.
It is empty, with no hooks and no bite marks, and it reads clearly on twilight blue `#1b4f86`. It is already rock steady (boil/wobble 0).

## Per-asset verdicts
| # | Asset | Verdict | Notes |
|---|---|---|---|
| 1 | dinosaur_skeleton | APPROVE | Reads well on `#2c3350`. Off-white bones with grey outline. |
| 2 | cave_lion_cub_mummy | APPROVE | Dry, matted, whiskers visible, mud patch. |
| 3 | cave_lion_cub | APPROVE | Wary or grumpy, faint spots, not kawaii. |
| 4 | cave_lion (SIL) | APPROVE | Clean silhouette, tail tuft reads. |
| 5 | blue_babe | APPROVE | Vivianite blue with crust patches, claw scratches on the rump, no wounds. |
| 6 | steppe_bison | APPROVE | Optional: the horn could be a little longer and wider for the "longer than a modern bison" beat. |
| 7 | stew_bowl | APPROVE | |
| 8 | lyuba_mummy | APPROVE | |
| 9 | baby_mammoth | APPROVE | |
| 10 | mammoth_scan_head | APPROVE | Rock steady. |
| 11 | mammoth_scan_head_plug | APPROVE | Byte-identical prefix of the head plus 2 plug elements. The plug sits at about (+160..+210, +55..+235). |
| 12 | large_dog | APPROVE | |
| 13 | sauerkraut_jar | APPROVE | |
| 14 | batagaika_crater | APPROVE | The centre is plain brown, so the wordart reads on it. |
| 15 | batagaika_foal_mummy | APPROVE | The muzzle pokes about 30 px past the 400 box on the right. That is harmless on the -9 degree slope. |
| 16 | test_tube_rack | APPROVE | |
| 17 | petri_dish | APPROVE | |
| 18 | wolf_pup_mummy | **REVISE** | See fix 1. |
| 19 | grey_wolf | APPROVE | |
| 20 | salmon | APPROVE | |
| 21 | bread_loaf | APPROVE | |
| 22 | turtle_pair_fossil | APPROVE | Turtles sit at about (-90,0) and (+100,0), and the right one is larger. Dry museum read. |
| 23 | messel_turtle | APPROVE | |
| 24 | dinner_plate | APPROVE | |
| 25 | fighting_dinosaurs_fossil | **REVISE** | See fix 2. |
| 26 | protoceratops | APPROVE | The beak at (+220,-170) and the frill at (+80,-240) match the request. |
| 27 | turkey | APPROVE | |
| 28 | house_key | APPROVE | |
| 29 | borealopelta | APPROVE | Strong two-tone. At 180 degrees the cream belly reads on top. |
| 30 | borealopelta_fossil | APPROVE | |
| 31 | mining_shovel | APPROVE | The top corners are light. The bucket is at about (+370,-77). |
| 32 | horseshoe_crab | APPROVE | |
| 33 | ichthyosaur (SIL) | APPROVE | Countershaded. The silhouette reads with snout, dorsal and crescent tail. |
| 34 | ichthyosaur_fossil | APPROVE | |
| 35 | dolphin | APPROVE | |
| 36 | belemnite | APPROVE | |
| 37 | squid_costume_flat | APPROVE | See above. |
| 38 | gogo_arthrodire | APPROVE | |
| 39 | gogo_nodule | APPROVE | |
| 40 | shark | APPROVE | |
| 41 | stanleycaris (SIL) | APPROVE | Mid-tone fill reads on `#0b1018`. The silhouette shows the eye stalks and claws. |
| 42 | stanleycaris_head | APPROVE (AD fixed) | See "AD edits". |
| 43 | stanleycaris_head_brain | APPROVE (AD fixed) | See "AD edits". |
| 44 | pencil | APPROVE | |

## Required fixes (illustrator)
1. **wolf_pup_mummy**: it reads as a sleeping cat. The head is a round dome with a pointed cat ear and no muzzle, and the
   closed eye is an upturned "content" arc. Add a short, clearly protruding wolf muzzle with a dark nose. Put the slightly
   drawn-back lip and the tiny teeth on that muzzle, so the "teeth still there" detail sits where a viewer looks. Make the ear small and
   folded back, not a pricked triangle, and draw the closed eye as a flat or slightly downturned slit. Keep everything else (fur `#7a6f62`,
   curl, size 300x140 `bc`, calm and respectful). This asset is A priority: 10 shots in a sombre item.
2. **fighting_dinosaurs_fossil**: it does not read as "Velociraptor vs Protoceratops". This asset is A priority: 8 shots plus the s114 arrows.
   a. **Protoceratops skull**: right now it is a bean-shaped blob with two holes. Give it a distinct **neck frill** (a fan behind the skull, which can keep the
      window hole) and a **hooked parrot beak** at the front, facing left toward the raptor. The beak must visibly close on the
      raptor's hand at about (+84,-262).
   b. **Raptor's kicking leg**: right now it is one long straight bar from the hip to the throat, so it reads as a spear. Draw it as a bent leg (thigh and
      shin), with a foot and a clearly hooked **sickle claw** pressed into the Protoceratops' throat (about +135,-212).
   c. The raptor skull floats high above the action. Bring the head and neck down and forward so the two animals read as locked
      together, and make the raptor's ribcage read as attached to its spine.
   d. The upper grain line pokes outside the slab outline at the top-right corner (about +330,-380 local). Clip it to the slab.
   Keep the size, anchor, sandstone `#e8c48a` and the bone colours. Report the final claw and hand coordinates for the director.

## AD edits (done)
- `stanleycaris_head.json` and `stanleycaris_head_brain.json`: I added `boil: 0, wobble: 0` to every element (94 and 119 elements), as the
  mammoth scan pair already has. The engine seeds the jitter by the shot element index and the asset name. Without this, the
  `_brain` pop-in in s199 would land on a differently wobbled copy of the plain head and show doubled outlines. The `_brain` file is still
  an exact element prefix of `_head`. I re-rendered the pair to verify: `assets/previews/005-art-review-stanleycaris-pair.png`.

## Composition notes for the director (not asset faults)
- s114: the CLAW arrow ends at (860,560), which is local (-71,-214). The real claw is at local (+135,-212), so aim it at about **(1150,563)**.
  The ARM arrow should end at about **(1078,493)**, not (1080,560). Re-check both after fix 2 using the coordinates the illustrator reports.
- s180: the shark's heart_icon at x=1250 sits on the tail. Move it to about **(1545,552)**, under the gills.
- s049: the MUD arrow tip (1000,760) stops just left of the plug. (1040,740) lands on it.
