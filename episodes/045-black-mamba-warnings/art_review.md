# 045 art review: new assets (art director, 2026-11-12)

**Verdict: FAIL** (17/22 approved). There are 5 required asset fixes, all routed to the **illustrator**. No director fixes. Re-preview only
the 5 drawings listed below. The rest are approved as drawn.

What I checked: the 6 previews `assets/previews/045-black-mamba-warnings-*` (props, snakes, creatures, 168x94 thumbs, in-context, costume
and horse on Doug). The sheet previews crop the tall drawings at the top of the cell, so I also rendered a close-up scene (`studio art`) of the reared/hood/gape
heads, cobra, perched eagle, combat pair, mongoose and costume_off at 1.1-1.6 scale. I also checked the s066-s069 shotlist placement: the
costume is only ever used with `pose: stand`, `cap_off`, and `doug_cap` at the hood top.

Overall the tiers hold. The detailed drawings have bold outlines, interior shading and scute/feather texture, and they sit against crude Doug. The mamba palette
matches the library (olive-grey, cream belly, `#0b0f2a` lining only when the mouth is open). There is no gore and no drool anywhere, and the eagle
carrying the mamba is bloodless.

## Illustrator's concerns: rulings
- **Eagle eyes**: the yellow is right and the brows keep it stern rather than cute. The problem is placement. In a side-on head, the far eye is the same size as the near
  eye and sits on the bill base, so the pair reads as googly owl eyes. **Fix 1.**
- **Mongoose**: does not pass. The legs are four flat rectangular posts with no paws, so it reads as a stool or a rat. **Fix 2.**
- **costume_off**: does not pass. The tabard reads as a brick and the bent wing reads as a rock shard. The three pieces sit apart in a row, so it reads as
  rubble rather than "a costume someone just took off". The hood is good. **Fix 3.**

## Required fixes (illustrator)
1. **brown_snake_eagle** (and the same head in `_glide` / `_carrying_mamba`): keep the near eye large, yellow, with its dark pupil and brow.
   Shrink the far eye to about 60% and move it so it peeks just over the top of the bill base, partly hidden behind the head outline (3/4 view). Do not
   let it overlap the bill. Keep the costume hood as it is: googly eyes suit a homemade cardboard prop.
2. **mongoose**: replace the block legs with four slim tapered legs that have a visible elbow/hock bend and small dark paws. The hind legs angle back a little.
   Keep the body, head, ears and the dark tail tip. Keep the anchor and bbox (~380 x 150) unchanged.
3. **snake_eagle_costume_off**: make it one overlapping heap, not three items in a row. The tabard should be slumped and folded over, with its scalloped
   feather rows and a visible neck hole or strap. One cardboard wing should be clearly a wing: a feathered scalloped trailing edge, a
   crease where it is bent, and an arm strap dangling. Lay it across the tabard. The hood lies on its side against the pile with one yellow eye up (as now).
   Keep the anchor and bbox (~360 x 120) unchanged.
4. **cobra_hooded**: the head is a small tile perched on the hood rim like a hat, and it does not read as facing left. Make the head about 1/3 of the hood
   width. Place it at the top centre in front of the hood, with the snout and eye clearly pointing left and a straight closed mouth line. Keep the wide hood (~200),
   the colours and the anchor.
5. **mamba_combat_pair**: the twist is good, but the two necks splay apart into a Y with the heads facing away from each other. Together with the
   symmetric braid, this reads as a caduceus (the medical symbol), not as wrestling. Bring the raised necks together so they press against each other and lean
   inward. One head should push over the other's neck, both rigid with mouths closed, and the heads stay at about y -380. It must not read as a heart or a hug.

## Approved as drawn
termite_mound (a minor note, not required: it has one turret and the top slopes. The coiled mamba and cap still sit well on it in context),
house_cross_section, bicycle_flat_tyre (reads in the thumbs), nerve_doorbell_diagram, fire_alarm_kit, umbrella_open, umbrella_folded,
black_mamba_reared (the silhouette reads), black_mamba_hood (a narrow flap, clearly not a cobra), black_mamba_hood_gape (the same geometry, lining and fangs are right),
black_mamba_coiled, green_mamba, brown_snake_eagle_glide and brown_snake_eagle_carrying_mamba (pending the eye change in fix 1), honey_badger
(an optional polish: show the heavy front claws more clearly), snake_eagle_costume (Doug's face is fully visible, one cap per frame, on-model), horse_gallop
(Doug `sit` lands in the saddle, neutral expression).

After the fixes: re-run `python -m studio asset-preview` for the 5 drawings plus a close-up `studio art` render, then return them for a quick re-check.

## Re-check (art director, 2026-11-12): **PASS** (22/22 approved)
I checked `assets/previews/045-black-mamba-warnings-fixes-closeup.png` with zoomed crops. The anchors and bboxes are unchanged in the diffs.
1. **brown_snake_eagle** (+ glide, carrying_mamba): fixed. The far eye is small and peeks behind the head outline above the bill base. It reads as a stern 3/4 view, not owl eyes.
2. **mongoose**: fixed. The legs are slim and tapered with bends and dark paws, and the hind legs angle back. It reads as a mongoose.
3. **snake_eagle_costume_off**: fixed. It is now one overlapping heap: a slumped tabard with a neck hole and strap, a scalloped cardboard wing bent at a crease across it with an arm strap, and the hood on its side with the eye up.
   An optional polish, not required: close the small gap at the wing crease so it reads as folded cardboard rather than two pieces.
4. **cobra_hooded**: fixed. The head is about 1/3 of the hood width, sits top centre in front of the hood, faces left and has a straight closed mouth.
5. **mamba_combat_pair**: fixed. The heads press together, one head over the other's neck, and the mouths are closed. It no longer reads as a caduceus, a heart or a hug.

All 045 assets are approved. Next: the keyframe review after shotlist build.
