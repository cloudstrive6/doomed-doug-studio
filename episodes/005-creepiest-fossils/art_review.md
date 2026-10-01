# Art review: 005 Creepiest Fossils (new assets)

Reviewer: art director · Date: 2026-10-01 · Scope: the 44 new library assets in `asset_requests.md`

## Verdict: PASS (round 2, 2026-10-01: all 44 approved. Round 1 was FAIL with 2 REVISE.)

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
| 18 | wolf_pup_mummy | APPROVE (round 2) | Fix 1 done: the protruding muzzle, dark nose, drawn-back lip with tiny teeth, folded ear and flat eye slit now read as a canine pup, not a cat. Calm and respectful. |
| 19 | grey_wolf | APPROVE | |
| 20 | salmon | APPROVE | |
| 21 | bread_loaf | APPROVE | |
| 22 | turtle_pair_fossil | APPROVE | Turtles sit at about (-90,0) and (+100,0), and the right one is larger. Dry museum read. |
| 23 | messel_turtle | APPROVE | |
| 24 | dinner_plate | APPROVE | |
| 25 | fighting_dinosaurs_fossil | APPROVE (round 2) | Fixes 2a to 2d done. The frill fan and hooked beak face the raptor's hand. The bent kicking leg ends in a sickle claw at the throat. The raptor's head and neck are locked in, and the grain line is clipped. It reads as Velociraptor vs Protoceratops at s104 and s114 size. The red dots in the preview are only coordinate markers, not part of the asset. |
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

---

# Keyframe review: 005 (all 211 shots, sheets 01-18), 2026-10-01

## Verdict: FAIL (4 small composition fixes for the director; no asset faults)
Style is consistent across all 18 sheets. Doug is on-model everywhere except the snorkel shots below, and the cap is always red.
Zone colours hold per item: ice-age pale blue/permafrost brown, Messel grey shale, Gobi sand, Borealopelta museum/green,
Solnhofen limestone, ichthyosaur navy, Gogo reef blue/Kimberley red, Cambrian near-black. Title cards, the
"DOUG DEATHS" counter (36 to 46, steps correct) and the time-machine layout are consistent. Text is legible and inside the safe area,
and the layouts vary. Nothing is gory. Both redrawn assets look right in context (s104, s105, s107, s109, s114, s115, s119, plus every wolf-pup shot).

## Director's leftover list
- **s006 / s007 small Doug**: OK, no fix required. He is fully visible and readable at 0.45. Optional: move him to x=900 so
  the divider line does not run through his body.
- **s015 cub cut**: FIX (see 1).
- **s143 crab cut**: OK. The crab is fully in frame and only overlaps the slab outline. Optional: crab x -40.
- **s151 / s181 floating snorkel and flippers**: FIX (see 2). The same bug is also in **s182**.
- **s211 cap near edge**: OK. The ghost's cap top sits at about y=110, inside the safe area.

## Required fixes (director)
1. **s015**: the right cub at (1820,900) is cut off by the frame, and the arrow ends at (1900,600), in empty sky, not on it. Move
   the cub to about **(1640,640)**, level with the left cub, and end the arrow at about **(1470,600)**, short of its nose. Keep Doug where he is.
2. **s151, s181, s182 (snorkel_gear)**: the prop is drawn for the standing skeleton (or lie + rotate -90). With `walk1/2` and `swim1/2`
   the tube floats beside or above the head and the flippers hover away from the feet, so Doug looks off-model. Drop the
   `snorkel_gear` asset in these three shots and keep the rig's `mask` gear. That still reads as "Doug went swimming". If the
   flippers are wanted, I will add native `snorkel` and `flippers` rig gear in `studio/doug.py` on request.
3. **s139** (minor): the horseshoe_crab icon sits over Africa while the circle marks Bavaria. Move the icon to sit beside
   the circle (about +60 px to the right of it, not below it).
4. **s063 / s064** (minor variety): these are back-to-back shots of the same foal-in-mud composition. In s064, push in (scale up the foal)
   or reframe so it is not a repeat.

Optional: s060 has a stray white chevron on the slope (about (1230,780) in the frame). Remove it if it is unintended.

---

# Keyframe review round 2: 005, 2026-10-01

Scope: the re-rendered s013-s015, s019, s020, s030, s039, s060, s064, s081, s101, s120, s134, s139, s145, s149, s151,
s156, s181, s182, s205, s207 (each checked full size), plus a general pass over contact sheets 01-18.

## Verdict: FAIL (1 blocking fix and 1 small fix for the director; rig support added by the AD)

Fixed and approved: s014 (timeline layout, which breaks the cross-section run), s015 (both cubs in frame, the arrow ends at the nose),
s019 (kneel), s030 (blue ox), s039, s060 (chevron gone), s063 to s064 (push-in, no longer a repeat), s081 (a real burrow with a tunnel,
a caving roof and the pup clearly visible, no longer a frying pan), s120 and s205 (the sign text fits the plate), s139 and s156 (the icon is next to the circle),
s145 (no X), s149 (ERRATIC is clear of the prints), s151, s181 and s182 (snorkel prop dropped, so Doug is on-model with the `mask` gear), and s207 (the mudflow wave,
the lone cap and an eye stalk read well, and it no longer looks like a blank frame). Style, zone colours, the counter and title cards are still consistent across all 18 sheets. Nothing is gory.

## AD edits (done)
- `studio/doug.py`: added the poses **`thumbs_up`** and **`sit_thumbs_up`**. They draw a small round fist with a stubby thumb, held
  in front of the face and clear of the head and brim. Doug's core look is unchanged, and the other poses are untouched. Test render:
  `assets/previews/005-art-review-thumbs-up.png`. The art bible (Doug section) and `docs/SCENE_SCHEMA.md` are updated.

## Required fixes (director)
1. **s134 (blocking)**: Doug floats in mid-air about 150 px above the belly-up Borealopelta, and he has no thumb, so the
   THUMBS UP arrow points at nothing. Change the doug element to `"x": 980, "y": 495, "scale": 0.7, "pose": "sit_thumbs_up"`
   so he sits on the cream belly between the up-turned feet. Then end the arrow at about **(1095, 395)**, next to the thumb.
   A verified mock render is at `assets/previews/005-art-review-s134-mock.png`.
2. **s013 (small)**: the "THE TWIST" wordart at (1500,960) runs through Doug's raised right arm. Move it to about
   **(1450, 300)** in the empty yellow space at the top right, or lower the arm by setting Doug's `y` higher. Keep the "!".

## Optional (not blocking)
- s101: the "sorry" bubble tail ends on Doug's cap brim (860,540). End it at about (900,470), above his head.
- s019 to s020: these use the same framing back to back. A slow `zoom_in` on Doug and the cub in s020 would keep the beat fresh.
- s021: the mother silhouette is still a blob (round-1 visual note 8). The illustrator could silhouette the `cave_lion` asset if time allows.
