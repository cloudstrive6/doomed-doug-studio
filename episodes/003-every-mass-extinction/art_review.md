# Art review: 003 Every Mass Extinction (new assets)

Reviewer: art director · 2026-10-01
Scope: every item in `asset_requests.md` (all have a Done line), plus my own `time_machine` and `sunburn` gear.
Checked: all `assets/previews/003-*` sheets, plus 16 in-context keyframes I rendered
(`python -m studio keyframes 003-every-mass-extinction --shots s002,s009,s025,s047,s089,s110,s131,s136,s146,s155,s173,s198,s205,s220,s224,s248`).
Criteria: recognisable; detailed tier vs crude Doug; on palette; bold silhouette; readable small; not gory; not
kid-cute (the brief flags dinosaurs and time machines as kid magnets); anchors land where the director laid out the shots.

## Verdict: PASS (assets)

All 38 illustrator drawings, the `time_machine` and the `sunburn` gear are approved. One asset (`rotten_egg`) had a readability problem; it was a small fix, so I made it
myself (see below). No illustrator work is outstanding.
There are **4 composition fixes for the director** (silhouette glow and one crop). They don't block asset approval,
but they must be fixed before keyframe approval (style bible 7.7 and 7.8).

## Per asset

| # | Asset | Result | Notes |
|---|---|---|---|
| 1 | time_machine (AD) | APPROVE | Teal booth, `TIME` panel, door open on the right with a window grid, dark interior with a dial and lever, base sparkles. Not a TARDIS. Doug fits the doorway with his cap at 0.75 (s002, s009). The flat roof takes the pigeon exactly (s248). |
| 2 | sunburn gear (AD, `studio/doug.py`) | APPROVE | Head fill `#ff8a7a`, the same crescent in a burnt tone, red arm lines, peel flakes at the front of the face. Head, eyes and cap are unchanged (s089). It meets CD note A6. |
| 3 | moss_patch | APPROVE | Harmless low smear, on palette, capsules read. It holds up at 3.0. Optional polish, not required: the 3.0 lobes are a little fat and sausage-like. Flatter, thinner ribbon lobes would read more like a liverwort. |
| 4 | trilobite | APPROVE | It is a textbook trilobite: three lobes, head shield, crescent eyes. It still reads at 0.15 on dark. |
| 5 | brachiopod | APPROVE | It reads as a fan shell with a beak. The plain centre leaves room for the s182-s184 holes. |
| 6 | doormat | APPROVE | Coir texture, border, no text. |
| 7 | ice_block | APPROVE | Outline only, Doug shows through, and the darker rim keeps it visible on pale blue (s025). |
| 8 | gondwana | APPROVE | Flat green with faint internal seams, no labels, on palette. |
| 9 | snorkel_gear | APPROVE | It clears the cap. It reads upright and when rotated -90 with `lie` (s047). |
| 10 | stromatoporoid | APPROVE | Layered dome, mamelons, star pores, no face. |
| 11 | angry_sun | APPROVE | Angry V brow and gritted teeth. It reads as annoyed, not cute. |
| 12 | spore | APPROVE | Trilete mark, even spines. |
| 13 | spore_malformed | APPROVE | Lopsided, with long twisted spines. The contrast with `spore` is clear side by side. |
| 14 | supernova | APPROVE | It reads as a spiky starburst in both colour and silhouette. |
| 15 | campfire | APPROVE | |
| 16 | dunkleosteus | APPROVE | Bony blade jaw, not teeth. Plate seams, small eye. The silhouette is clean and menacing. |
| 17 | dunkleosteus_dead | APPROVE | Belly-up, X eye, bubbles, no blood. |
| 18 | marshmallow_stick | APPROVE | The handle lands in Doug's pointing hand. It reads lying on the ground (s110). |
| 19 | conodont | APPROVE | Large eyes (which is the science), V muscle blocks, fin rays. It looks like a textbook drawing, not a mascot. |
| 20 | hot_tub | APPROVE | Steam only comes off the water. No people. |
| 21 | rubber_ring | APPROVE | It sits at Doug's hips behind the `float` pose (s131). |
| 22 | head_towel | APPROVE | It rests on the cap dome. The brim and the red stay visible. |
| 23 | rotten_egg | **FIXED BY AD** | **Problem:** a speckled egg with a round green dome poking out of the top and the shell cap flying off. In a dinosaur episode that reads as *an egg hatching*, not a rotten egg. **Fix applied in `assets/library/rotten_egg.json`:** I flattened the yolk into a grey-green pool inside the half-shell, removed the 4 speckle dots, added a green drip over the left rim, and laid the shell fragment on the ground at the lower right. Extent is now about x -124..+228. Re-checked in s136: it reads as a broken rotten egg and still sits clear of Doug. |
| 24 | lystrosaurus | APPROVE | Beak, down-pointing tusks, a bored heavy-lidded eye. Blocky silhouette; it still reads as a 0.22 map icon. Good deadpan character. |
| 25 | pangaea_map | APPROVE | No labels, and the NA/Africa seam is a thin dark line where the crack goes. |
| 26 | coelophysis | APPROVE | Slender, not cute, and it stands on the podium (s173). |
| 27 | phytosaur | APPROVE | Long narrow snout, back scutes, and the nostril mound sits by the eye (the defining feature). |
| 28 | volcano | APPROVE | |
| 29 | ammonite | APPROVE | Ribbed, banded shell, annoyed eye, not cute. It reads at 0.25. |
| 30 | ammonite_costume | APPROVE | Zipper language matches 002. Head, face and cap are fully visible. |
| 31 | ammonite_costume_flat | APPROVE | Deflated and slumped. See director fix D4 for the crop in s198. |
| 32 | india_map | APPROVE | Recognisable outline. The Deccan sits at local (-50,-20) as requested. |
| 33 | empire_state_building | APPROVE | Exactly 512 tall. Five stack spire-to-base with no gaps (s205). |
| 34 | fire_extinguisher | APPROVE | The label has no readable text. It reads lying in the death (s220). |
| 35 | asteroid | APPROVE | Plain rock, craters, lit side. The outline stays clean in silhouette. |
| 36 | sauropod | APPROVE | |
| 37 | t_rex | APPROVE | It looks mean, not cute. The tiny arms land the joke. |
| 38 | fern | APPROVE | |
| 39 | feathered_dinosaur | APPROVE | Wider than asked because of the tail (noted by the illustrator). The director should check that s247 still has the tail on screen. |
| 40 | pigeon | APPROVE | Head down, orange eye, wing bars, unimpressed. It sits on the roof in s248. |

## Director: composition fixes (needed before keyframe approval)

The engine draws a silhouette's glow as a spray disc **at the asset's anchor**, radius `glow_r x scale`, *behind* the
black shape. Every silhouette in this shotlist uses a radius smaller than the drawing, so the glow is invisible. In
s146 it does the opposite: it leaks out as a red smear under the colour reveal. I added the sizing rule to
`channel/art_bible.md` (Screen furniture).

1. **s224 asteroid (1.6), s201 asteroid (0.4), s085 dunkleosteus (1.4):** the glow is fully hidden. Raise `glow_r` to
   about 0.7 x the asset width: asteroid **280**, dunkleosteus **420**. Style bible 7.7 requires the red glow.
2. **s080 supernova:** same problem. Raise `glow_r` to about **350**. Keeping the colour reveal in the same shot is OK
   here, because red glow leftover around an explosion is on-theme.
3. **s146 lystrosaurus (blocking, gore read):** the glow is centred at the feet (bottom anchor), and the colour reveal
   at 0.92 is drawn on top of it. What remains is a red spray puddle under the belly that reads as **blood**. Remove the colour
   `lystrosaurus` element from s146 (s147 already shows it in colour, one beat later), and replace `glow` with a
   `spray` of `#e0201b` at the body centre (about x 1100, y 640, r 380, density about 0.16), placed before the silhouette.
4. **s198 Doug's death in the ammonite costume:** with `lie` rotated -90, the costume's shell points down and is cut off at the bottom of the
   frame. The shell is the one part that says "ammonite". Raise Doug and the flat costume by about 120 px (keep them on the
   dark seabed band).

Minor, not blocking: in s025 the large moss patch overlaps the right edge of the ice block. Nudge the moss right
by about 60 px so the block's outline reads cleanly.

## Changed files
- `assets/library/rotten_egg.json` (fix #23)
- `channel/art_bible.md`: silhouette glow sizing rule. Worn props may now go on a `lie` Doug rotated -90 for death beats
  (this episode does it twice); keep back-mounted parts in frame.
