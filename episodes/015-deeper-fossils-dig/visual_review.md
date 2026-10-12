# Visual review: 015-deeper-fossils-dig

## Round 1: pre-render keyframes (2026-10-12)

Scope: contact sheets 01-25 (s002-s289), with full-res keyframe crops checked for overlaps. s001 skipped (thumbnail pending).

VERDICT: FAIL

What passes: Doug is on-model and readable in every shot (red cap, white head), including the pupa costume (s053-s056), referee (s152-s154), vet (s104-s106), cone costume (s283-s286) and the close-up (s251). All deaths are cartoon only (ghost Doug, cap left behind, X eyes, tombstone), with no blood or gore anywhere. Nothing reads as a kids' show. On-screen spelling checks out (TELEOCERAS, XENOMORPHIA RESURRECTA, PALAEOPYTHON, PSITTACOSAURUS, RHAMPHORHYNCHUS, ASPIDORHYNCHUS, TANYSTROPHEUS, NOTHOSAURUS, INVAVITA PIRATICA, CLOUDINA, TRICHOMONAS). The death counter runs 121 to 130 with no jumps. The depth badge matches each chapter. Picture and narration match almost everywhere.

### Required fixes

1. **s034** (director): the chapter title "WASPS INSIDE FOSSIL FLIES" (two lines) runs under the DOUG DEATHS / DEPTH HUD. The depth badge and shovel icon sit on top of the word "FOSSIL". Make the title smaller or move it down/left so it clears the HUD box (x > ~455 at 640 scale). The other chapter cards (s057, s081, s109, s131, s157, s184, s232, s256) clear the HUD and are fine.
2. **s206** (director): same problem on "THE SHARK'S TAPEWORMS". The final "S" of SHARK'S sits on the depth badge and shovel icon. Make the title smaller or shift it left/down.
3. **s082** (director): Sue's mounted skull sits under the DEPTH badge. Move or scale the skeleton down/left so the skull clears the HUD.
4. **s141** (director): the year label is hidden behind the slab, so only "20" shows. Place "2023" fully outside the slab (for example above it or bottom-left), not behind it.
5. **s240** (director): the "OUTSIDE" label touches and overlaps the bottom of the DEPTH badge. Move it down/left (for example next to the worm on the right, below y ~110).
6. **s281** (director): the dinosaur icon in the top-right of the ring sits under the DOUG DEATHS / DEPTH HUD. Shrink the ring or move that icon so all eight callback creatures are fully visible.
7. **s204** (director): the head of the black Nothosaurus silhouette runs under the DEPTH badge. Scale or move the silhouette down/left so it clears the HUD.
8. **s191** (director/illustrator): the Tanystropheus head disappears into the giraffe's chest, so the two read as one fused creature. Separate them: Tanystropheus on the left, a clear gap, then the giraffe, with the two necks lined up for comparison. Also move the "GIRAFFE" label off the giraffe's head.
9. **s071, s078 food-chain icons** (illustrator): the insect is a plain brown oval and does not read as an insect. Draw a small, simple insect (a beetle-style body, legs, antennae; it can be faded or "too far gone"). Use the same icon in s071 and s078.
10. **s169, s170, s171** (director): the pterosaur wing bone runs across the top of the frame and under the DEPTH badge. Move the jaw and wing group down about 40 px (640 scale) so the bone clears the HUD.
11. **s178, s179, s180, s181** (director): the fishing rod runs off the top of the frame, behind the chapter-title box. Shorten or angle the rod so its tip stays inside the frame, below the title box.
12. **s195-s198** (director): variety. Four near-identical grey-slab compositions in a row (the same slab, same framing, only a "?", an outline or a circle changing). Change at least one: for example s197 as a close-up on the empty space where the body should be, or s198 as a tight close-up on the tooth marks.
13. **s236-s242** (director): variety. Six of seven shots are the same ostracod in the same centred framing (s236, s237, s238, s240, s241, s242). Make at least two clearly different: for example s238 with the worm alone next to a ruler, and s242 as a wide shot of the rock nodule with Doug, or as a time-scale graphic.

### Recommended (non-blocking)

14. **s086** (illustrator): the narration says "a red cap. His." but the fossil cap is grey. Give it a faded red tint so it reads as Doug's cap within a second. The "003" tag is meaningless to new viewers. Consider replacing it with a short label such as "HIS".
15. **s107** (director): the death beat (counter goes to 124) shows a hole with dust and a floating cap. Nothing links it to Sue, so the death has no visible cause. Consider showing Sue's open jaws or Sue's silhouette over the hole.
16. **s287** (illustrator/director): the two caps on the shovel are tiny (about 30 px). Scale up the shovel and caps so "TWO CAPS" is readable at phone size. Also move the "TWO CAPS" text left so its "S" does not overlap the dark shaft.
17. **s176** (director): the right-hand top slab touches the bottom edge of the DEPTH badge. Nudge the slab grid down a little.
18. **s070** (illustrator): the "RUSSIAN DOLLS" text sits on the large doll's head. Move the text above the dolls.

## Round 2: keyframes after round 1 fixes (2026-10-12)

Scope: I checked the 13 required and 5 recommended round 1 items at full resolution. I also reviewed all 61 shots that changed in fd02d1c against their narration, plus s001 (the thumbnail opening).

VERDICT: FAIL (one blocking item)

Round 1 items resolved:
- Required 1-13: all fixed. s034, s206, s082, s141 ("2023" is now fully outside the slab), s240, s204, s169-s171 and s178-s181 all clear the HUD. In s191 the Tanystropheus and giraffe are separated, and the label sits above the giraffe. s071 and s078 use the same readable beetle icon. In s195-s198 variety is fixed (s197 is now a close-up of the missing body). In s236-s242 variety is fixed (s238 has a ruler, s239 a rice comparison, s242 a timeline).
- Recommended 14-18: all addressed. s086 has a faded red cap and a "HIS" label. s107 shows Sue's silhouette as the cause. In s287 the caps are larger and "TWO CAPS" clears the shaft. s176 and s070 are fine.

New shots: the changed shots match their narration. Doug is on-model and there is no gore. The death counter and depth badges are consistent.

### Required fixes

1. **s180** (director/art director): the threat glow behind the Aspidorhynchus and pterosaur silhouette is a red speckle cloud in the water, centred on the bite. At a glance it reads as a blood cloud. The red dots also spill over the black fish body, which looks like a render glitch, and there is a row of stray red tick marks along the bottom edge of the frame (x ~1360-1700, y ~1075). Change the glow to a neutral or dark tone (as in s186), keep it behind the silhouette only, and remove the bottom-edge ticks.

### Recommended (non-blocking)

2. **s166, s199** (director): these use the same red underwater glow, more faintly. In s199 it sits next to "caught by the neck". Use the same neutral glow as the s180 fix so nothing in the water reads as blood.
3. **s281** (director): the HUD shovel icon tip touches the T. rex icon's head. Nudge the T. rex icon down or left by about 15 px.

## Thumbnail candidates (round 2)

Checked at 1280x720 and at feed size (about 246x138).

- **Option A (`build/thumbnail.png` = `thumb_a.png`, `thumbnail_small.png`): PASS. Recommended.** The strata cross-section darkens band by band, which sells "the deeper... the scarier" and complements the title without repeating its words. All six finds are recognisable at feed size (the rhino skeleton least so). The labels read at feed size and use no title words. It is not misleading, since every find is in the episode. Non-blocking notes for the graphic designer: (a) Doug is about 50 px tall and his cap touches the top edge, so at feed size he is a speck. Scale him up about 1.5x and drop him a little so the cap clears the edge. (b) The column uses only the middle ~40% of the width. Widen the bands or enlarge the finds so the threats carry more of the frame. (c) "Tanystropheus" is set smaller than the other labels; match the sizes, or shorten it if needed.
- **Option B (`build/thumb_b.png`, `thumb_b_small.png`): FAIL (do not use).** The 2x3 grid of panels loses the depth gradient, so it no longer complements a "deeper = scarier" title and reads like a generic fossil collage. Doug appears only as a tiny figure in one panel, and there is no sense of descent or threat to him. "Held On" and "Wasp Flies" are cryptic without the stacked layers for context.
