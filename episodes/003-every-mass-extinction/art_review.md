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

---

# Keyframe review: 003 Every Mass Extinction

Reviewer: art director · 2026-10-01
Scope: all 249 keyframes in `build/contact/sheet_01..21.png`, plus a re-check of the 4 director fixes from the asset review.
Cropped and zoomed: s047, s110, s130, s135, s146, s169, s196, s201. Test renders of my proposed fixes for s130, s146
and s196 were made with `python -m studio art` (not committed).

## Verdict: FAIL (keyframes)

The style is consistent. Doug is on-model in 245 of 249 shots: the red cap is always there, ink auto-whitens on dark
backgrounds, and the sunburn (s089-s091), ghost and `lie` death poses are all correct. Each item keeps its own zone
colour all the way through (Ordovician pale blue/grey, Devonian teal, Siberian maroon/lava, hot-tub rust, purple
oceans, Triassic yellow-green, Deccan grey, Chicxulub sky blue). Captions and the death counter (18 → 27) are legible and
inside the safe area.
The episode still fails, for three reasons: s146 still reads as a blood puddle, two Doug design breaks, and four runs of 5-6 near-identical compositions.

## Re-check of the earlier director fixes
| Fix | Shot | Result |
|---|---|---|
| D1 | s224 asteroid, s085 dunkleosteus | **Fixed.** The red glow reads clearly around both silhouettes. |
| D1 | s201 asteroid (scale 0.4) | **Weak.** `glow_r` 280 x 0.4 = 112 px leaves only a hairline ring. See fix 9. |
| D2 | s080 supernova | **Fixed.** |
| D3 | s146 lystrosaurus | **Still FAIL.** See fix 1. The colour reveal was removed (good), but the red pool under the belly is still there. |
| D4 | s198 ammonite costume death | **Fixed.** The shell is fully in frame. |
| minor | s025 moss over the ice block edge | Unchanged. Still optional (fix 10). |

## Blocking fixes (director)

1. **s146: gore read, root cause found.** The puddle doesn't come from your body spray. It comes from the engine's
   **default glow**. Every `silhouette: true` gets a red glow (`glow_r` 260) at the anchor even when `glow` is left out,
   and lystrosaurus is anchored at the feet, so the disc lands on the ground. Re-ordering elements doesn't help either,
   because the ground poly's bucket fill skips spray speckles. I tested this exact recipe and it is clean: a halo
   above the ground line only, and nothing on the ground.
   - On the `lystrosaurus` silhouette element, add `"glow_r": 0`.
   - Keep the `#e0201b` spray, but use `x 1100, y 600, r 360, density 0.25`.
   - Directly after that spray, before the silhouette, add
     `{"type":"rect","x":0,"y":768,"w":1920,"h":312,"fill":"#7a6248","width":0,"outline":false}`, and then re-add the
     ground texture `{"type":"spray","x":960,"y":940,"r":700,"color":"#5a4632","density":0.04}`.
   (I added this engine behaviour to `channel/art_bible.md`, Silhouette glow sizing.)
2. **s130, s131: the head towel is across Doug's mouth (off-model).** Doug was raised to y 508, but `head_towel` stayed
   at y 630, so it now covers his face. Set Doug to **y 630** in both shots, to match s132. That puts the ring at his
   hips (as approved) and the towel back on the cap dome. Tested.
3. **s196, s197: the wordart covers Doug's cap** ("BLEND IN" / "VERY SERIOUSLY" at 860,250 sits on top of the cap and brim).
   Style bible 7.2 requires the cap to be visible at all times. Move both wordarts to **x 1400, y 300** (the empty sky on the right). Tested.
4. **s049-s054: six identical reef compositions in a row.** Only the labels change. Re-lay two of them:
   - **s051** ("largest development of animal-built reefs"): use a globe or map with the reef belt highlighted, or a
     scale comparison. Do not use the reef strip.
   - **s053** ("two pulses of ocean anoxia"): use dark water with no reef, plus an O2 gauge or two pulse blocks on a line,
     to set up s055. The reef can come back in s054 and s056.
5. **s005-s009: five shots of booth-left / ground / water-right.** s006 is almost a duplicate of s005. Re-lay **s006**
   ("animals had barely set foot on land") without the booth: a wide bare-rock panorama with tiny Doug and the
   "443 MILLION YEARS AGO" label, or a split land/sea panel with all the life on the sea side.
6. **s036-s040: five shallow-basin shots in a row.** Re-lay **s037** ("many species lived nowhere else") as a close-up
   inside the basin water (trilobite and brachiopod large, with the "NOWHERE ELSE" label), with no cross-section.
7. **s057-s061: five rock-column shots in a row.** Re-lay **s061** ("half a centimeter every thousand years") as a tight
   zoom on one layer with a ruler or fingernail for scale. Do not show the full column. s062 (coins) then follows naturally.

## Non-blocking (fix if touching the shot anyway)
8. **s233:** the thermometer (1600,480) sits on the sauropod's head and neck. Move it to about **x 1780, y 400**.
9. **s201:** raise the asteroid `glow_r` to **450**, so the ring is about 180 px at scale 0.4.
10. **s025:** nudge `moss_patch` right by about 60 px so it clears the ice block outline (carried over).

No asset fixes for the illustrator.

## Changed files
- `channel/art_bible.md`: silhouettes always get a default glow (use `glow_r: 0` to suppress it); spray isn't covered by a
  later ground poly; small scales need a bigger `glow_r`.
