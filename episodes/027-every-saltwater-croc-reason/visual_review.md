# Visual review: 027-every-saltwater-croc-reason

## Round 1: pre-render keyframes (2026-10-26)

Scope: all 28 contact sheets (s001 to s330 plus the endslate). I zoomed into these full keyframes: s030, s054, s107, s195, s201, s235, s292. The thumbnail (s001) is still pending, so it was not reviewed.

**VERDICT: FAIL**

### What passes
- Doug is on-model (red cap, white head) in every shot he appears in, and readable on every background, night scenes included. The ghost Doug and floating-cap death beats are consistent, and the death counter climbs correctly from 218 to 226, one step per on-screen death.
- No gore anywhere. Every death is a splash plus a ghost. The Ramree chapter (s240-s261) covers real human deaths using only documents, maps and text, with no Doug and no counter. That register is appropriately sober. Nothing reads as a kids' show.
- Leap check: s201 is the only lunge out of the water. The croc clears roughly half its body (snout about 255 px above the waterline on a body about 600 px long), so **no croc leaps its body length**. Fix 2 still asks for the lunge to be lowered so it matches the "kitchen counter" scale. s118 (head and neck out of a pool) and s191/s192 (gallop, low bound) are fine.
- Text is spelled correctly and nothing is cropped. Earlier fixes are confirmed: the art-review round-2 asset fixes (the jaw-closeup neck runs off frame, the bathtub croc has a sloped neck, the held shape is clamped across the jaw) all hold.

### Required fixes
1. **s107 (director): layering bug.** The "FLOODS" water is a flat full-width rectangle drawn over the foreground. It cuts the nest mound off flat and hides Doug except for the top of his cap. Doug is alive (counter 220), so he must not vanish. Either raise the flood as a semi-transparent band behind Doug, with the waterline below his knees, or move Doug to higher ground to the left and keep the mound's top half above the water. No hard rectangle edge across the middle of the frame.
2. **s195-s212 (director, with illustrator for the counter prop): scale is wrong.** The narration says the branch is "about as high as a kitchen counter" (about 0.9 m). In s195 the counter is about 190 px tall against Doug's 150 px, so it is taller than Doug, and the branch sits a full Doug-height above the water. Make the counter about half Doug's height, and lower the branch to match (about 75-80 px above the waterline at full resolution) in s195-s212. Then in s201 the croc only needs its head and shoulders out to reach the branch. Keep the out-of-water part well under half the body.
3. **s235 (director/illustrator): death beat is unreadable.** The flat grey inverted triangle with ripple rings does not read as a croc, a roll or a splash. Use the standard death composition: the splash asset at the spot Doug fell, with the croc's back and tail just rolling under (or the existing roll motion arcs), cap on the bank, ghost Doug. Drop the grey cone, or replace it with the red-and-yellow spinning top from s232 if the "dance" callback is wanted.
4. **s292 (director): effect looks like a glitch.** The death effect is a large grey static-noise disc over the end of the jetty and reads as TV static or a render error. Replace it with the standard splash (as in s062/s182/s323) at the end of the jetty, with the cap on the boards as now.
5. **s227 (director): picture contradicts the narration.** The narration says "all but one species rolled", but all five crocs have green ticks. Change the last one (or the thin-snouted one) to a red X so the frame shows "all but one".
6. **s054, s055, s105 (director): floating cut-off head.** `croc_open_mouth` has a flat, outlined bottom edge. On the plain background (s054, s055) and on the mud beside the nest (s105), it reads as a disembodied or severed head. Either put a waterline across the base (as s065-s070 already do), so the head is clearly emerging from water, or swap in the full-body croc. In s105 the mother should be beside the nest as a whole animal.
7. **s054 (illustrator/director): stray mark.** There is a lone black dash at about (1760-1840, 800) behind the fish. Remove it, or make it 2-3 obvious speed lines.
8. **s030 (director): narration says he "wades in up to his knees".** Doug is standing on top of the water with his whole legs showing. Mask his lower legs below the waterline, or add a ripple ring around his knees.
9. **Variety (director): runs of 4 or more near-identical compositions.** Break each run with at least one reframe (close-up, cutaway, insert or new angle):
   - s011-s017 (7 shots): the same underwater cross-section, with the bank on the left, the croc at the bottom and Doug top-left. Cut in a close-up for s015 (stopwatch "11.5 HOURS") and s017 (a heart close-up for "2 to 3 beats a minute").
   - s129-s140 (12 shots): the same framed croc picture on orange, Lolong then Cassius. Give s134-s136 a full-frame map of the Cairns/NT move, and s139 a Doug-vs-Cassius age gag instead of the frame.
   - s160-s172 (11 of 13 shots): the same Cape York map. Give s166-s167 more road shots (these are fine) and turn s169 or s171 into a wider shot of the croc near the release point.
   - s217-s224 (7 of 8 shots): the same curved top-down croc. Show s218 (already different) and change s221 or s224 to a side view of the spin.
   - s279-s283 (5 shots): the same Indonesia map. Make s282 (coin flip) a full-frame coin and s283 a fishing-boat scene.
   - s243-s246 (4 shots): the same Ramree map. This one is minor: make s245 ("very few came out") text-only on black.
10. **s041, s042 (director): missing label.** The narration says the study counted "on an alligator". The dark croc has no label, while s043 labels "NILE CROCODILE" and s072 uses the same asset as "ALLIGATOR". Add an "ALLIGATOR" label under it in s041 and s042, so the 4,000 vs 9,000 comparison reads.
11. **s154 (director): text collision.** The "Y" of "FAR AWAY" runs into the slung croc crate. Move the text left or up, clear of the sling.

### Minor (optional)
- s008, s097, s098, s123, s143: big captions sit on top of the mangrove trees. They are still legible thanks to the outline, but they would be cleaner moved 40-60 px up into clear sky.
- s116, s121: the hatchlings are tiny brown specks. Scale them up about 1.5x so "babies reach the water unharmed" is visible.
- s142: the small object under the 1914 calendar can't be identified. Remove it, or make a hatchling clearly peek out.
- s276/s277: Nile and saltwater use the identical drawing. That is acceptable since the labels carry it.

Re-render the keyframes for s030, s041, s042, s054, s055, s105, s107, s154, s195-s212, s227, s235 and s292, plus the reframed variety shots, for round 2.
