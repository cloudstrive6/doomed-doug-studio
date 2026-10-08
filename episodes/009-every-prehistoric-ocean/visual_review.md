# Visual review: 009-every-prehistoric-ocean

## Round 2: pre-render keyframes (2026-10-08)

Round 1 result: FAIL with 9 blocking fixes (snorkel s024–s027, ARMORED s026, s310 sharks, s276 tusks, s334 contrast, s187 label, s140 fossils, Endoceras variety, Tylosaurus variety) and 11 advisories.

Scope: I re-checked all 29 re-rendered contact sheets (s001–s337) against `shotlist.json`, and zoomed in on s027, s132, s140, s231, s276, s310 and s334. The "thumbnail pending" tile at s001 is expected.

### Blocking fixes from round 1

1. **s024–s027 snorkel: fixed.** Doug wears mask and snorkel in all four shots. In s027 the SNORKEL arrow tip lands on the snorkel tube. Continuity holds into s028–s029, where the snorkel floats away.
2. **s026 ARMORED: fixed.** The label now sits at lower left beside the trilobite row, well clear of the Anomalocaris silhouette.
3. **s310 sharks: fixed.** "USUAL DRAWING" sits above the top shark. The bottom shark is visibly longer and shallower-bodied, with "SLIMMER" under it, so the comparison reads.
4. **s276 tusks: fixed.** The elephant has ivory tusks and the red X is centred on them. The saddle blanket is gone.
5. **s334 THE WHOLE NIGHT: fixed.** The label is now in the sky at left, outlined, and legible against light blue.
6. **s187 TWO-METER HEAD: fixed.** The text sits in open water at upper right, clear of the pliosaur.
7. **s140 fossils: fixed.** A dig pit now holds a half-buried skull, a vertebra row and a flipper bone between the two scientists, with one "SKULL, BACKBONE, FLIPPER" caption below.
8. **Endoceras variety (s040–s048): fixed.** The run is now broken up: s041 is a Harvard museum case with the missing tip circled, s042 is the scientist with a "MISSING PART?" clipboard and pencil, s044 is the truck, s046 is a close-up cone with a dashed "ESTIMATED" tip, and s048 is the 2025 study on a monitor with "GENEROUS". No run of four near-identical frames is left.
9. **Tylosaurus variety (s228–s232): fixed.** The front-on mouth now alternates with s230 (a tight push-in on the backward palatal teeth with yellow arrows) and s231 (a side-on Tylosaurus with a roof-of-mouth inset, a fish at the jaws and a THROAT arrow).

### Round 1 advisories that also landed
s053 (Endoceras now lies alongside the shell), s141 (FREEING THE BONES nudged clear of the scientist), s160 and s327 (NOPE and NOT PROVEN stamps now have a white fill), s260 (SCAVENGING uses a horizontal strike-through), s262–s264 and s289–s292 (moon icon now anchored to the HUD label), s311 (STREAMLINED moved below the shark) and s207 (tail no longer clipped).

### Regression check
- Doug is on-model (red cap, white head) and readable in every shot, including the dark Livyatan and Megalodon backgrounds.
- The death counter runs 74 → 84 in order. The s213 "81 (swallowed)" gag stays crossed out and the counter holds at 80 until s237.
- The s132 circle is still on the tail card (the middle card).
- I found no new overlaps, cropped text or stray marks.
- There is no gore. Deaths stay cartoon only (splash, ghost, floating cap, and the s330 black frame with the HUD still showing).
- Nothing reads as a kids' show.
- Header and name spellings are unchanged and correct.

### Advisory (non-blocking, fix if cheap)
1. **s231:** the yellow "toward the throat" arrow is drawn across the top of the head, over the eye. *Director:* lower it about 25 px so it runs along the jawline or into the mouth.
2. **s276:** the tusks are small and partly hidden behind the trunk, so the X covers most of them. *Illustrator:* lengthen the tusks about 1.4× so they stick out past the trunk. Or *director:* shift the X about 30 px right onto the exposed tips.
3. **s334:** "THE WHOLE NIGHT" is smaller than the other green callouts. *Director:* bump the size about 1.3× if it still fits left of the time machine.
4. **s011, s012, s065–s070, s085, s258:** the round 1 advisories 10, 11 and 17 (compound eye on a stalk, claw shape, goldfish stand-in) are unchanged. They are acceptable as they are.

VERDICT: PASS

## Round 3: thumbnail at feed size (2026-10-08)

Scope: `build/thumbnail.png` (1280x720), `build/thumbnail_small.png` (320x180), plus a 168x94 mobile downscale. I checked them against the `metadata.json` title and thumbnail_brief and against style bible §2A.

- **Grammar:** this is an Archetype A 3x4 grid on white with thick rounded frames and a single comic-font label per tile, matching the brief. Tiles darken in era order from pale Cambrian blue to near-black navy, and Megalodon sits alone on the darkest tile at bottom right. There is no title text or logo, and no label repeats a title word (Dying/Every/Prehistoric/Ocean/Sea/Like).
- **Readability:** at 320x180 all 12 labels are readable and every tile reads as a sea monster. The teeth on Pliosaurus, Livyatan and Megalodon carry the threat. At 168x94 the labels blur, which is normal for this archetype, and the grid still reads as a table of contents for ocean monsters.
- **Spelling:** all 12 names are spelled correctly and none is cropped.
- **Doug:** zoomed in, he is on-model: red cap, white round head, stick body, shock mouth, mask, snorkel and fins. He is a speck at feed size. That is intended, because the style bible says the stick man is never the hero.
- **Policy and kid appeal:** there is no blood or gore. The Helicoprion whorl is a cartoon. Angry brows and teeth on most predators keep it in nature horror. The grid does not read as a dinosaur picture book or as a kids' show.
- **Misleading:** no. The title promises deaths in prehistoric oceans, and the grid shows the monsters at each stop, all of which are in the video.

### Advisory (non-blocking)
1. **Megalodon tile (bottom right):** YouTube's duration badge will cover the right part of the "Megalodon" label. *Graphic designer:* if cheap, nudge the label about 20 px left within the tile. The shark itself stays clear of the badge.
2. **Anomalocaris tile:** Doug faces right, away from the Anomalocaris, and the dark mask band over his eyes reads slightly like lettering when zoomed in. *Graphic designer:* optionally set `facing: "left"` so his shock is aimed at the threat. This is invisible at feed size, so it is not required.
3. **Silhouette variety:** six tiles are grey right-facing fish shapes (Dunkleosteus, Helicoprion, Cymbospondylus, Xiphactinus, Basilosaurus, Megalodon). They are acceptable because the tile colours and labels separate them, but this is worth noting for the next grid episode.

VERDICT: PASS

## Thumbnail v2 (2026-10-08)

Scope: revised `build/thumbnail.png` (1280x720) and `build/thumbnail_small.png` (320x180), plus a 168x94 mobile downscale and zoomed crops of both Dougs and the bottom row. Title: "What Dying in Every Prehistoric Ocean Would Be Like".

- **Readability:** the 3x4 Archetype A grid is unchanged in structure. At 320x180 all 12 labels are readable, spelled correctly and uncropped. At 168x94 the labels blur, as expected for this archetype, but the grid still reads at once as "a list of sea monsters". The tiles still darken in era order, ending on Megalodon on the darkest tile.
- **Doug (on-model):** both Dougs (Anomalocaris tile and Megalodon tile) have the red cap, white round head, stick body, open shock mouth, blue mask, snorkel and fins. Both now face left, toward their threat, so round 3 advisory 2 is resolved. The eyes show through the mask and no longer read as lettering. In the Megalodon tile Doug is white-on-navy and is the only light speck in the corner, so he reads as "tiny man next to giant teeth" even at 320 px.
- **Creatures:** every tile is recognisable as its animal type. Anomalocaris has frontal appendages and stalked eyes. Endoceras is a striped cone shell with tentacles. Jaekelopterus is a sea scorpion with claws. Dunkleosteus has an armoured head plate. Helicoprion shows the tooth whorl. Cymbospondylus is an ichthyosaur. Pliosaurus is a toothy marine reptile. Xiphactinus is a fanged fish. Tylosaurus is a gaping mouth with eyes in the corners. Basilosaurus is an eel-like whale. Livyatan and Megalodon are giant jaws. The Tylosaurus mouth is the most abstract tile, but its teeth, eyes and palatal tooth rows make it a maw rather than a red blob.
- **Gore and policy:** there is no blood, wound or body part. The dark red on Tylosaurus, Livyatan and Megalodon is gum or mouth interior, drawn flat with no drips or pooling, so it is acceptable. Nothing is cutesy and there is no nursery palette. It reads as nature horror, not a kids' dinosaur book.
- **Misleading:** no. Every creature shown appears in the video, and the grid delivers on "every prehistoric ocean".

### Advisory (non-blocking)
1. **Megalodon tile label:** this is carried over from round 3 advisory 1. The label is still centred, so YouTube's duration badge (bottom right, about 80x40 px at full scale) may clip the final "n". *Graphic designer:* if cheap, shift the "Megalodon" label about 20 px left. Do not move the shark or Doug.
2. **Silhouette variety:** the grey right-facing fish shapes are unchanged. They are acceptable for this episode, and this note is kept for the next grid.

VERDICT: PASS

## Round 4: thumbnail v2 (2026-10-08)

Scope: `build/thumbnail.png` (1280x720) and `build/thumbnail_small.png` (320x180), a 168x94 downscale, and a simulated YouTube duration badge (desktop feed: about 44x20 px at 8 px inset on a 360 px card, which is roughly x 1095-1251, y 620-691 at full res; the mobile badge is similar). This round supersedes the unnumbered "Thumbnail v2" section above, which did not test the badge position.

- **CD changes applied:** Endoceras, Pliosaurus and Basilosaurus are flipped. Crops now vary across the grid (full body: Endoceras, Helicoprion, Cymbospondylus, Pliosaurus, Basilosaurus; mid: Anomalocaris, Jaekelopterus, Dunkleosteus; tight: Xiphactinus, Tylosaurus, Livyatan, Megalodon). Basilosaurus is a long eel-whale across the tile. Tylosaurus is a front-on gaping maw. Megalodon is a tight jaw crop of more than 40% of the tile with a tiny Doug. The palette gradient, labels, frames and order are unchanged. The "stamp sheet" problem from v1 is fixed.
- **Legibility:** at 320x180 all 12 labels are readable. At 168x94 they blur, as expected for Archetype A, but the grid still reads as a set of sea monsters. Spelling is correct and nothing is cropped by the frames.
- **Bottom row at 320x180:** Tylosaurus, Livyatan and Megalodon read as three distinct animals. Tylosaurus is a front-on red-and-green maw. Livyatan is a brown-grey side-on whale head with a brow and an eye. Megalodon is a pale grey and white three-quarter jaw on navy. They differ in colour, angle and shape, and Basilosaurus breaks up the run. The only overlap is that Livyatan and Megalodon share the same zigzag tooth row with red gums. That is acceptable.
- **Doug:** both Dougs are on-model, with red cap, white head, stick body, shock mouth, mask, snorkel and fins, and both face their threat. The Megalodon-tile Doug is the only light speck on navy and sells the scale at 320 px.
- **Policy:** there is no gore. The mouth interiors are flat dark red with no drips or pools. The tone is nature horror, not a kids' picture book.
- **Misleading:** no. Every creature shown is in the video.
- **Duration badge (blocking):** with the badge simulated, it covers **Doug's legs and fins in the Megalodon tile**, from his waist down (his body runs y about 575-645 and the badge starts at y about 620). Only a floating head and cap remain, so the one human-scale cue the CD asked for is half hidden. The badge also covers "odon" of the label, which then reads "Megal…".

### Fixes
1. **Megalodon tile Doug (graphic designer, blocking):** move Doug up so that his whole figure, fins included, sits above y ≈ 610 at full res and stays on the navy gap right of the jaw. That is about 40-50 px up. If that pushes him into the white jaw edge, nudge the shark about 30 px left or down instead of shrinking Doug below scale 0.12. Do not move him left over the teeth, because white on white disappears.
2. **"Megalodon" label (graphic designer, recommended, not blocking):** this has been flagged for the third round. The label's right edge sits under the badge. Shift it left so it ends before x ≈ 1085, or accept "Megal…" in feed. The jaws carry the tile without the label.
3. **Livyatan (advisory):** the jaw is wider than in v1 and the teeth read at 168 px, but it is still a narrow band. If the designer is re-rendering anyway, opening it about 20% more would separate it further from Megalodon.

VERDICT: FAIL
