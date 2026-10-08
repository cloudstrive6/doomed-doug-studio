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
