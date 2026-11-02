# 035-walrus-without-a-bite: art review (art director)

## Asset review, 2026-11-02 (22 new library drawings)

**Verdict: FAIL. 18 APPROVE, 4 need fixes (illustrator).** All four fixes are about the walrus reading as a seal
in silhouette or at crowd size. Nothing is wrong on policy.

How I checked it: I read the previews (`assets/previews/035-walrus-without-a-bite-{assets,context,hug}.png`), re-rendered
every asset at scale 0.55 and 1.0, and rendered real keyframes for s002, s003, s006, s013, s020, s024, s029, s030, s103,
s126, s167 and s183 against the current shotlist.

### Family-wide
- **Style: OK.** These are in the detailed tier: outline 4-6, a darker back, a lighter belly, pale wrinkle and scar lines,
  and spray texture. They contrast clearly with crude Doug. The palette matches the director's proposal (`#b07a5e` / `#8a5a44` /
  `#c99a80`, ivory tusks, underwater tint `#8fa9c4` with a `#1b4f86` outline). There are no pink-cute tones. The drawings read on ice, sea,
  dusk orange, gravel and cream.
- **Not cute: OK.** The eyes are small and dark with no shine. There are no smiles and no moustache gag. The bulls have bosses and scars.
  The calf is small and plain, with a dot eye.
- **No gore: OK.** There is no blood, no wound and no carcass, and no tusk touches anything soft in the shots I rendered. Grease is left to the shotlist.
- Optional, not blocking: the side-view whisker pad is a brown ball with dark dots and only short pale stubs at its edge.
  At 0.3 it reads like a knob or nose. If you are already editing a file, lighten the pad toward `#c99a80` and add a few longer
  `#e8dcc0` bristle strokes (as in `walrus_snout_closeup`) so the "stiff pale bristles" read.

### Per asset
| # | Asset | Verdict | Notes / required fix |
|---|---|---|---|
| 1 | `walrus_bull` | APPROVE | Reads as a walrus at 0.28 in crowds and as a silhouette (s006: the tusks clear the flipper). The boss zone has no stains, so s013/s014 grease works. |
| 2 | `walrus_cow` | **FIX** | Fine in colour. As the plain black crowd tile (s003-s004) the short, thin tusks vanish into the chest and the herd reads as **seals**. Fix: mark both tusks `silhouette_keep` (as on `walrus_head_rising`) and widen them a little (about +4 local) so they still show at 0.3. Do not lengthen them past the bull's. |
| 3 | `walrus_sleeping` | APPROVE | **Overrun to x +344 accepted.** s020: the tusk tip lands at screen x ~978, about 55 px clear of Doug's cap. s121 (facing pair): the tips are at ~726 and ~1234, well apart. The cap positions for s186 and s213 still work. |
| 4 | `walrus_bull_hug` | APPROVE | **Pose deviation accepted.** In s024 the flippers drape over the chest and belly, Doug's face and cap are fully clear, the head is far right, the tusks hang along the walrus's own body, the eyes are half shut and there is no smile. It reads as "flopped onto him", which is the joke. |
| 5 | `walrus_bull_rearing` | **FIX** | Fine in colour. As the s103 red-rim silhouette pair, each tusk overlaps the front-flipper column and merges into it, so the pair reads as hooded sitting shapes. Fix: mark the tusks `silhouette_keep`, and swing the tips about 30 local units forward (right) so the tusk tips clear the flipper column (keep the s119 no-contact gap). |
| 6 | `walrus_cow_calf` | APPROVE | The calf is small and plain with no shine, no mouth and no tusks. The underwater tint is on-palette. |
| 7 | `walrus_swimming` | **FIX** | The tusks are too short and tucked under the chin. As the s029 / s070 silhouette it reads as a **seal**, and in colour it is borderline. Fix: lengthen the tusks to about 110 local from the root, pointing down and slightly back, so they sit clearly outside the body outline. Mark them `silhouette_keep`. Keep the throat at y +80..+98 clear for the air sacs. |
| 8 | `walrus_feeding` | APPROVE | **Overrun of the rear flipper to (-532,-370) accepted.** In s030/s035/s036 it stays on screen (top at y ~560). The snout sits on the mud line and the clam reads. |
| 9 | `walrus_head_rising` | APPROVE | Front view reads at 0.2. The ivory `silhouette_keep` tusks make the s002 silhouette work well. |
| 10 | `walrus_hauling_out` | APPROVE | Tusks in the ice top and a straining look, with the underwater tint. |
| 11 | `walrus_hanging_asleep` | APPROVE | **Overrun of the rear flipper to y +444 accepted.** In s126 the bottom is at screen y ~1044, inside the frame. The tusk rests on the ice top. |
| 12 | `walrus_hanging_front` | APPROVE | Reads as a row of 12 at 0.34. The tusks cross the edge cleanly. |
| 13 | `walrus_snout_closeup` | APPROVE | The 14 bristle rows are countable. The tusks are slim enough for the jam jar shots. |
| 14 | `walrus_mouth_cutaway` | APPROVE | Diagrammatic: a cream interior and a cartoon pink piston tongue (`#e79aa0`, on-bible). Nothing realistic. |
| 15 | `walrus_top_view` | **FIX** | At 0.3 (s167) the tiles read as grubs or sausages: the head isn't separated and the tusks are invisible. Fix: (a) make the tusk tips poke clearly past the snout to about x +185, at least 10 local wide, in ivory with a `#6a5a4a` outline; (b) add a clear neck pinch about 40 local behind the head; (c) make the front flippers a little bigger so they stick out sideways. Re-check as a 0.25 tile on `#8c8a84` and `#6e6a64`. |
| 16 | `walrus_head_icon` | APPROVE | Reads in the 36 px HUD. The cream rim works on near-black. |
| 17 | `clam_empty` | APPROVE | Empty and pale, the same family as `clam`. |
| 18 | `dairy_cow` | APPROVE | Instantly a Holstein. The udder is small. |
| 19 | `navy_ship` | APPROVE | No insignia and no weapons. Hull number 462. |
| 20 | `eye_icon` | APPROVE | Matching disc set. |
| 21 | `ear_icon` | APPROVE | |
| 22 | `nose_icon` | APPROVE | |

### Required fixes (route: illustrator)
1. `walrus_cow`: tusks `silhouette_keep` plus slightly wider. Re-check the s003/s004 silhouette herd at 0.3-0.5.
2. `walrus_bull_rearing`: tusks `silhouette_keep`, tips swung forward clear of the front flipper. Re-check s103 and s119.
3. `walrus_swimming`: longer tusks clear of the body outline, `silhouette_keep`. Re-check s029, s070 and s128.
4. `walrus_top_view`: visible tusk tips, a neck pinch and bigger front flippers. Re-check s167 and s187 at 0.25-0.3.

Keep every anchor and the other extents unchanged, so no re-placement is needed in the shotlist. Re-preview and send back
for a re-check of these four only. Everything else is approved.
