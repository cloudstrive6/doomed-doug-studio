# Visual review: 009-every-prehistoric-ocean

## Round 1: pre-render keyframes (2026-10-08)

Scope: `build/contact/sheet_01..29.png` (s001–s337) checked against `shotlist.json` narration. I zoomed into keyframes for s011, s027, s053, s140, s187, s276, s310 and s334.
s001 is the thumbnail placeholder, which is expected.

**Overall:** The episode is strong. Doug stays on-model (red cap, white head) in every shot. The death counter runs 74 → 84 and matches the script (the s213 "81 (swallowed)" gag is crossed out and the counter correctly stays at 80). There is no gore: mouths are cartoon interiors, deaths use splash, ghost and floating cap, and the s330 black frame is a deliberate gag with the HUD still visible. Nothing reads as a kids' show. Creatures are recognisable, and silhouette reveals are used consistently. Everything below is a local fix.

### Required fixes (blocking)

1. **s024, s025, s026, s027: Doug has no snorkel, but the payoff line is "the one animal wearing a snorkel."** These four shots set `gear: ["mask"]` only and leave out the `snorkel_gear` asset. In s027 the SNORKEL arrow points at a bare head. The snorkel then appears floating away in s028, so it is clearly meant to be there.
   *Director:* add `{"type":"asset","name":"snorkel_gear","x":880,"y":820,"scale":0.55}` (same x/y/scale as the doug element) to s024–s027, following the s310 pattern. In s027, re-aim the arrow so its tip lands on the snorkel tube.
2. **s026: the "ARMORED" label sits next to the Anomalocaris silhouette.** That tells viewers the predator is the armored one, which is the opposite of the segment's point.
   *Director:* move "ARMORED" down to the trilobite row (about y 800, between the trilobites at x 260 and 620) or point an arrow at a trilobite. Keep the silhouette unlabelled.
3. **s310: the "slimmer" comparison does not read.** The great white and the megalodon assets are nearly the same shape. Both "USUAL DRAWING" (y 620) and "SLIMMER" sit beside the bottom shark, and the top shark has no label.
   *Director:* move "USUAL DRAWING" directly above the top shark (y about 230). *Illustrator:* provide a visibly bulkier "usual" megalodon (deeper body, around 1.3× height), or a visibly slimmer one (stretched long, around 0.75× height), so the difference reads in one second.
4. **s276 "tusks don't count": the elephant asset has no tusks.** The red X lands on the trunk.
   *Illustrator:* add two ivory tusks to `elephant`, or make an `elephant_tusks` variant. *Director:* centre the red X on the tusks. Drop the red ornamental saddle blanket if possible, because it reads as circus or toy.
5. **s334: "THE WHOLE NIGHT" (yellow-green) sits on green grass.** The contrast is too low to read at feed size.
   *Director:* move the label into the sky (for example x 1400, y 820, right of the time machine), or put it in a white `label` box.
6. **s187: "TWO-METER HEAD" is drawn over the pliosaur's grey-green flippers.** The letters merge with the drawing.
   *Director:* move the text to the upper right of the water area (about x 1450, y 470), clear of the animal. Alternatively, use a boxed `label` with an arrow to the head.
7. **s140: the SKULL, BACKBONE and FLIPPER labels float over empty mountainside.** Nothing is being dug up.
   *Director:* place small fossil props under the labels (for example `pliosaur_skull` or a skull asset at scale ~0.3, a short row of vertebra circles, and a flipper bone shape) half-buried in the rock. Or swap in the s142 skull plus a dig pit.
8. **Variety: s040–s043 and s045–s048 (Endoceras).** These are eight beige "cone on a plank + Doug standing right" frames, broken only by the s044 truck. That is two runs of four near-identical compositions.
   *Director:* re-stage at least two in each run. Examples: s041 as a museum gallery (plaque, glass case, "HARVARD"); s042 with the scientist sketching the missing tip on a clipboard or in close-up; s046 as a split bar (solid half / dashed half, "ESTIMATE"); s048 with a document or paper prop plus a "GENEROUS?" stamp.
9. **Variety: s228–s232 (Tylosaurus mouth).** Five consecutive frames use the identical front-on mouth with small Doug top-right; only the arrows change.
   *Director:* give s229 or s231 a side-on cutaway (the tylosaurus asset with a roof-of-mouth inset), and push in or crop tighter on s230 (a close-up of the backward-pointing palatal teeth) so the camera moves.

### Advisory (fix if cheap, not blocking)

10. **s011, s012 (compound eye):** the eye on a brown stalk reads as a lollipop or shower head. *Illustrator:* add a small Anomalocaris head behind the stalk, or use a dragonfly-eye texture with hex facets.
11. **s065–s070 (Jaekelopterus claw):** the claw reads somewhat like a toothed jaw or skull. *Illustrator:* separate the two fingers slightly (open pincer) and make the hinge clearer.
12. **s053–s055:** inside the shell, Doug is only a tiny red cap. That works as a hiding gag, but s053 "lies beside him" shows the Endoceras stacked on top of his shell. *Director:* place it alongside, on the seafloor.
13. **s160:** the tilted red "NOPE" stamp overlaps the Liopleurodon's teeth on a blue screen. Give the stamp a white fill.
14. **s327:** the red "NOT PROVEN" stamp on dark navy has low contrast. Give it a white fill.
15. **s260:** the X covers the middle of "SCAVENGING" so the word reads "SCAV…GING". Use a horizontal strike-through like s243 so the word stays legible.
16. **s311:** "STREAMLINED" crosses the shark's belly and pectoral fin. Move it down about 60 px.
17. **s085, s258:** a cartoon goldfish stands in for "most fish have teeth" and for "a large fish". It is acceptable, but a generic large fish asset would sell s258 better.
18. **HUD timer (several shots):** the timer format drifts between "0 h 22 min" (s107 shows "22 min", s154 shows "9 min", s186 shows "4 min") and the seconds variants (s237 shows "1 min 30 s", and the s262–s264 and s289–s292 series). Seconds for deliberate quick-death gags are fine. For minute-level values, standardise on "0 h MM min". When the label is short, the moon icon sits away from the box (s262, s289, s328); anchor the icon to the label's left edge. *Art director / editor.*
19. **s207:** the Xiphactinus tail fin is clipped by the bottom frame edge. Raise it about 60 px.
20. **s141:** "FREEING THE BONES" starts on the scientist's legs. Nudge it right by 80 px.

### Checked and OK
- Doug on-model and readable in all 336 shots. Ink auto-whitens correctly on the dark Livyatan/Megalodon backgrounds (s124, s125, s256).
- Spelling of every creature header and name card is correct (Anomalocaris, Endoceras, Jaekelopterus, Dunkleosteus, Helicoprion, Cymbospondylus, Pliosaurus, Xiphactinus, Tylosaurus, Basilosaurus, Livyatan, Megalodon). Same for the place labels (Dorset, Hays, Kansas, Valley of the Whales, North Carolina, Belgium).
- No text is cropped at the frame edges, and the HUD never collides with headers.
- Deaths (s028, s082, s107, s133, s154, s186, s237, s265, s292, s330) are all cartoon only: splash, ghost, cap. There is no blood.
- The s132 "He picks the tail" circle is on the correct (tail) card.

VERDICT: FAIL
Blocking: fixes 1–9 (director: 1, 2, 3, 5, 6, 7, 8, 9; illustrator: 3, 4). Re-render keyframes for s024–s027, s040–s048, s140, s187, s228–s232, s276, s310 and s334 for round 2.
