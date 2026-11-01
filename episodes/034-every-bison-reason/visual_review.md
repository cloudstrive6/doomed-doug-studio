# 034 Every Bison Reason: visual review

## Round 1: pre-render keyframes (visual screener, 2026-11-01)

**Note on inputs.** `build/contact/` held only `sheet_01.png`, because a partial `keyframes --shots` run wipes every sheet and
rebuilds only the shots it rendered. The shotlist had also been edited (s207 icon discs) after the last full render. So I
re-ran `python -m studio keyframes 034-every-bison-reason` on the current shotlist: 209 keyframes, sheets 01-18. Every tile was
viewed, and the suspect shots were checked at full size.

### What works
- Doug is on-model in every shot (red cap, white head): the wolf costume (s020-s024) and referee shirt (s003, s195-s200) keep
  the cap and face readable. He reads on snow, grass, dusk orange and the death-beat black.
- Death counter: 267 -> 274. That is seven deaths (s025, s071, s092, s111, s131, s153, s201) and it matches the seven icons in s207.
  The new cream discs behind the s207 icons fix the art director's note B. The icons now read on the dark slate.
- Text: no misspellings, nothing cropped, no labels on top of drawings. Calendar months follow the ramp.
- Chalkboard tallies in s140 come to 25. The dot grid in s062 shows 12 of 25. The fortnight grid in s144 is correct.
- Gore and policy: all deaths are cartoon (cap on the ground, ghost Doug). There is no blood. The real calf death (s085-s086) is
  a plain grey silhouette card with no figures. The hump cutaway (s032-s033) is a clean textbook diagram (pink band, ivory
  spines, no blood), so it is acceptable. Nothing reads as a kids' show: the calf is never cute or close-up (decision 5c is followed).
- Planned beats that look deliberate and are fine: the empty riverbank in s087-s088, the calf silhouette on the scale in s080, and
  the sober card in s124-s127.
- Variety is good overall, with many locations and diagram cards. The only run of 4 or more near-identical frames is the sober card,
  which is deliberate (see fix 4).

### Required fixes
1. **s105: broken clock (director).** The three `clock` assets are rotated 0/120/240 to show time passing. Rotating the whole
   asset also rotates the numerals, so the final frame shows 3 at the top, 6 on the right, 12 on the left and 9 at the bottom.
   Change: set `rotate: 0` on all three clock elements (or keep one clock) and show the passing time with the hand only, for
   example a red `arrow`/`line` hand from (480,470) that pops in at three angles with `appear` 0, 0.3 and 0.55. Do not rotate the face.
2. **s113, s116, s117, s194: "visitors" read as lollipops or cotton buds (director).** Each visitor is a white circle on a single line,
   with no arms or legs. In s113 the narration subject is "the visitors", and at 1080p they read as a row of lollipops, not people.
   Change: swap each circle+line pair for the library `stick_man_plain` at about 0.3 scale, keeping the same x positions. Use about 8-10
   figures instead of 17 so they don't merge into a fence. Keep `appear` 0.3 in s113.

### Minor fixes (do these in the same pass)
3. **s061: the TOSS panel is just an arrow (director).** BUTT and HOOK both show the bison head, but TOSS has no bison and nothing
   being tossed, while the narration says "throws the person into the air". Change: add `bison_head_icon` at (1340,690) scale 1.0,
   plus a tiny `stick_man_plain` (about 0.18, rotated about 30) at the arrow tip near (1380,500).
4. **s127: the card line doesn't match the narration (director).** The narration is "The bison did not come to them", but the new line
   is "PARK RULE: 23 M". Change: make the new line `THE BISON DID NOT MOVE`, or move "PARK RULE: 23 M" to the next shot that mentions
   the rule. This also gives the 4-shot card a fresh reason to change on its last beat.
5. **s203: the push-in is too weak to show the sticky note (director).** The keyframe matches s202. Change: camera `zoom_in`
   to the PLANT EATER note at about (800,560), with `zoom` 1.8 (it is 1.1 now), so "all it says is plant eater" lands on the note.
6. **s032 (and s033): arrow tails start inside the label boxes (director).** The MUSCLE arrow starts on the "E" and the LONG BONES
   arrow starts on the "S". Change: start each arrow at the label's lower edge (MUSCLE from about (720,425), LONG BONES from about
   (1440,355) in frame coordinates) so no letters are crossed.

### Optional (non-blocking)
- s166 (illustrator): the dog on the rug has pointed ears and a closed-eye smile, so it reads a little like a cat. A longer snout
  or floppier ear would make "picture a dog" instant.
- s156 / s177 (director): "THE RUT." is used as the season card at s156, then chapter "THE WALLOW" follows, then chapter "THE RUT" at
  s177. This is fine because the narration says it, but the topbar jump RUT -> WALLOW -> RUT is a little confusing on a scrub.

### Still pending (not part of this verdict)
- s001 shows "(thumbnail pending)". The thumbnail is also the opening image, so screen s001 and the three thumbnails in the
  post-render round once the graphic designer delivers them.

VERDICT: FAIL
Required: fix 1 (s105 clock) and fix 2 (visitor figures in s113/s116/s117/s194). Fixes 3-6 are minor and should go in the same pass.
After the changes, run the full `python -m studio keyframes 034-every-bison-reason`, not `--shots`, which deletes the other sheets.
