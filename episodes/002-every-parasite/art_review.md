# Art review: 002 Every Parasite (assets)

Reviewer: art director. Scope: the 53 new library drawings in `asset_requests.md` (commit 7a9ad3b, plus the
uncommitted `lilo`). Keyframes are **not** reviewed here yet.
Checked against: `channel/art_bible.md`, style bible section 7 (Art Director rules 1, 7, 8), brief section 8 (gore
watch, kid-appeal), and the anchors/sizes in the requests. Previews used: `assets/previews/002-every-parasite-*.png`,
plus my own re-renders at scale 1-2 on white, on the actual shotlist backgrounds (`#1b2a4a`, `#4a1a28`, `#b9503a`,
`#7a2a33`, `#3d0f18`, `#cfe9a8`, `#dfe8ee`), silhouette + red-glow tests for every SIL asset, the mosquito at scale
0.2, and a bounding-box pass for every anchor.

## Verdict: FAIL (5 assets need fixes, 48 approved)

Gore watch is clean across the whole set: nothing enters, leaves or grows inside a body; `body_outline` and
`head_outline` have no organs or brain; `horsehair_worm` is a lone tangle; `naegleria_amoeba` has no face or teeth;
`fungus_stalk` stands alone; the single cells and `cercaria` are pale textbook diagrams. No cute eyes or smiles on
creatures, no pastel nursery palette. The two-tier contrast holds (crude Doug and `toddler` vs detailed creatures).

## Fixes required (route to the illustrator)

1. **field_cricket (A, also SIL in s050)**: the cricket giveaway is missing. The hind leg is a thin line hidden under
   the body and the silhouette reads as a generic bug with a raised flap. Fix: draw the **big jumping hind leg** on
   the near side: a fat, slightly striped femur angled up and back from the rear of the thorax so it rises above the
   back line, then a thin spiny tibia folding sharply down and back to the ground (the classic inverted "V").
   Lower the lifted wing flap so it lies flat along the back ("wings folded flat"). Re-check the SIL at scale 2.0.
2. **cricket_costume (A)**: (a) the hind legs read as two leaves with ski poles: the fat femur blobs sit upright at
   the shoulders and the tibias are straight black poles. Redraw each side as the same inverted-"V" jumping leg as
   item 1 (femur angled up/back from the hip area, tibia folding down to the ground). (b) Night readability for
   s064/s065 on `#1b2a4a`: the black tibia poles and black body outline nearly vanish. Draw the tibias in
   `#5a4632` with lighter spine ticks, and strengthen the rim highlight (`#7a6446`-ish, 4-5 px) down the whole
   left and right edges of the suit and along the wing cape, not just a faint streak on one side.
3. **raccoon (A, 13 shots)**: the four legs are straight grey rectangles with black blocks, which reads as a table
   and is below the detailed tier of the rest of the animal. Taper each leg, give the hind legs a visible heel/knee
   bend, and make the paws small dark rounded mitts (raccoon "hands") instead of flat blocks. Keep the body, mask,
   tail and the head-top position (about (+150,-200)) exactly as they are: the cap in s191 depends on it.
4. **blood_flukes (A, used at scale 2.0 in s119)**: the request asks for a male **curved into a C**; the drawing
   is a shallow arch (~120 degrees) that reads as an eyebrow or a rainbow at small sizes. Curl it to roughly a
   200-220 degree C (ends turning inward), keep the thinner darker female lying in the groove with her ends
   showing, and keep the two small suckers at the male's front end. Keep the fills pale; the red-brown surface dots
   are fine but do not add more (they start to read as blotchy skin).
5. **rat_costume (A)**: the "pink forepaws at the chest" are two plain pink ovals on the side of the belly and read
   as spots or sores. Either give them clear paw shapes (small pink mittens with 3 toe ticks, outlined, placed at
   the ends of short sleeve cuffs at the suit's sides around y=-40) or remove them. Optional: thicken the hood so
   it visibly wraps both sides of the face instead of a single grey band behind the head (it currently reads a bit
   like a headphone band).

## Approved

| Asset | Tier | Notes |
|---|---|---|
| cockroach_costume | A | APPROVE. Reads upright and rotated -90; antennae behind the cap; face and cap clear. |
| ant_costume | A | APPROVE. Gaster bulb, elbowed antennae, reads on `#2e8b3a` and `#cfe9a8`. |
| snail_costume | A | APPROVE. Broodsac stalks from behind the cap, no eyes on tips; shell backpack reads sideways. |
| doug_sunglasses | C | APPROVE. Sits on Doug's eyes, arm to head edge. |
| jewel_wasp | A | APPROVE. Metallic green, red thighs, strong SIL. |
| cockroach | A | APPROVE. Head, pronotum and antennae where requested; clean at 2.2. |
| burrow | B | APPROVE. |
| carpenter_ant | A | APPROVE. Legs root on the thorax, mandibles and elbowed antennae read; SIL clean at 2.0. |
| leaf | A | APPROVE. |
| small_plant | A | APPROVE. Top leaf flat at y about -540. |
| rainforest_tree | B | APPROVE. |
| fungus_stalk | B | APPROVE. Stands alone, no host. |
| clock | B | APPROVE. |
| horsehair_worm | A | APPROVE. Lone tangle, no face or segments. Loops rather than a true knot; acceptable. |
| matchbox_charger | C | APPROVE. Note for director: bounding box is y -91..+190 (the plug hangs down), so the box sits about 50 above the anchor. |
| swimming_pool | B | APPROVE. |
| sun_lounger | B | APPROVE (confirm seat height in s064 keyframes). |
| amber_snail | B | APPROVE. |
| broodsac_snail | A | APPROVE. Striped swollen stalks, clean, no gore. |
| songbird | A | APPROVE. Robin reads; SIL strong. |
| caterpillar | C | APPROVE. No face, no smile. |
| toxoplasma_cell | A | APPROVE. Diagram look, pointed cap end. |
| rat | A | APPROVE. |
| cat | A | APPROVE. Unimpressed predator, not cute; faces right. |
| freshwater_snail | C | APPROVE. |
| cercaria | B | APPROVE. Forked tail, diagram. |
| body_outline | A | APPROVE. No face, no organs. |
| head_outline | A | APPROVE. No interior; nose tip about +235. |
| kissing_bug | A | APPROVE. Drawn top-down (dorsal) facing right rather than side view: this is the better choice because it shows the orange edge stripes; reads on `#4a1a28` at 0.45 too. |
| trypanosome | A | APPROVE. Undulating fin, flagellum; SIL reads. |
| bed | B | APPROVE. |
| calendar | A | APPROVE. Centre left blank for labels. |
| heart_icon | B | APPROVE. |
| library_book | C | APPROVE. "DATE DUE 1987" + cobweb sells the joke. |
| mosquito | A | APPROVE. Spotted wing, tilted abdomen. At 0.2 it is a speck (see director notes). |
| fly_swatter | C | APPROVE. |
| red_blood_cell | A | APPROVE. Textbook disc, not blood. |
| hammock | B | APPROVE. |
| house | B | APPROVE. |
| tsetse_fly | A | APPROVE. Scissor wings, proboscis, striped abdomen. |
| lab_mouse | C | APPROVE. |
| podium | B | APPROVE. |
| airplane | C | APPROVE. |
| naegleria_amoeba | A | APPROVE. Lumpy cell, no face or teeth. |
| jetty | B | APPROVE. |
| usa_map | B | APPROVE. |
| toddler | C | APPROVE. Crude tier, faces left, no cap. |
| lilo | B | APPROVE. Commit it with the fixes (currently untracked). |

## Notes for the director (composition, checked at keyframe review)
- **s216/s218**: the `naegleria_amoeba` silhouette on `#3d0f18` gets a red glow that is almost invisible on that
  background; the black blob barely separates. Use a brighter glow (e.g. `#ff3b2f` at higher density) or lift the
  background a step for those two shots (rule 7: silhouette + red glow must read).
- **s168/s169**: `mosquito` at 0.2-0.25 is a 70 px speck on `#b9503a`. Either go to about 0.3 or point at it with a
  red arrow so the beat reads.
- **s064/s065**: re-check the cricket costume on night navy after fix 2.

After the illustrator's fixes, re-render `asset-preview` for the five assets and send them back to me for a quick
re-check; the approved 48 do not need another pass.
