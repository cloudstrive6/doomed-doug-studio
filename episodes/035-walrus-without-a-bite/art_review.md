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

## Keyframes round 1, 2026-11-02 (s001-s217 + endslate, sheets 01-19)

**Verdict: FAIL. Director, 5 composition fixes. There are no asset fixes, and nothing fails on style or policy.**

### Asset round-2 re-check (illustrator fixes): all 4 APPROVED
- `walrus_cow`: in the s003/s004 silhouette herd the ivory tusks now show on every tile, so it reads as walruses, not seals (checked at 1080p).
- `walrus_bull_rearing`: in the s103 red-rim pair the tusks clear the flipper column. In s104-s107 and s118-s119 there is no tusk contact with Doug.
- `walrus_swimming`: in the s029 and s070 silhouettes the long tusks sit clearly outside the outline. In colour (s030, s035, s041, s128-s135) they read well, and the s133 air sacs are clear.
- `walrus_top_view`: in s167 and s187-s189 the tiles show tusk tips, a neck pinch and side flippers. They read as walruses on gravel and no longer look like grubs.

### Passed checks
- **Style:** the two tiers stay consistent across all 217 shots, with crude Doug and detailed walruses, bears, ships and cows. The caption bar and the DOUG DEATHS / WALRUS COUNT HUD sit in the same position on every frame. The counter steps 274 to 280 on the six death cards (s026, s075, s101, s120, s185, s211). Doug is on-model everywhere. The ghost Doug is white on near-black with the cap kept, and `sunburn` (s141-s143) is approved gear.
- **Zones and colour:** each item keeps its own sky key (ice blue, then cream diagrams, then grey sea, then dusk orange, then purple dusk, then overcast gravel, then the stampede slate). The s173-s176 shelf diagram goes from light shallow blue to navy deep water, which is correct.
- **Policy:** no blood and no wounds. s107 is spoken only, with an arrow and a triangle. The s193 trampling is a dust cloud. s201-s203 are plain, sober text cards. The s025 heart is the hug joke and does not tip into cute. The calf stays plain and nothing is kid-coded.
- **Reveals:** every item title uses the red-rim silhouette (s006, s029, s054, s078, s103) or a full-colour title card.

### Required fixes (route: director)
1. **s018-s024: seven near-identical wide floe frames in a row** (same floe, same camera, walrus left, Doug right). Recompose **s020** (Doug sunbathing) as a push-in or close two-shot on Doug and the towel. Recompose **s022** ("Doug did not agree") as a tight reaction close-up on Doug's face. Keep s023/s024 wide for the roll-over payoff.
2. **s061, s062, s063 reuse the front snout close-up 3 times in a row**, and it has already appeared in s052, s053 and s056. Change the base layout for **s062** (fend off predators): use the bull facing the polar bear, as in s148. Change it for **s063** (settle arguments): use a small `walrus_bull_rearing` pair. s061 can keep the head with the breathing hole.
3. **s137 repeats s136** (the same hanging row, with only the label changed). It also matches s122-s125. Recompose **s137** ("safest thing in this entire video") on the s126 side-view `walrus_hanging_asleep` with the green check, or as a push-in on one hanging head.
4. **s107: the "SOMEBODY HURT" wordart is at y 1000 (size 88)**, which is outside title-safe, over the bulls' flippers, and under a `shake` camera. Move it up to about (560, 260), clear of the caption bar and the HUD.
5. **More than 2 keyword labels on screen at once (rule 7.4):** **s009** has STOMACH SAMPLES + HUNTED + FOUND DEAD. Drop the carried-over STOMACH SAMPLES header. **s011** has LARGE MALES + RINGED + BEARDED. Drop LARGE MALES; the arrow already does that job. **s147** has SIZE + HIDE + TUSKS (+ VS). Drop HIDE, or merge it into one "SIZE, HIDE, TUSKS" list label. Region labels on diagrams (SHALLOW SHELF / DEEP WATER, the s128 pool states) count as annotations and are accepted.

### Notes (not blocking)
- s013: the BLUBBER wordart sits over the bull's head and whisker pad. If you are already editing, nudge it up into the sky band.
- s068 and s071 use the same framing. A slow push-in on s071 would give the s072 tusk reveal a fresher frame.
- s001 is still "thumbnail pending". That belongs to the graphic designer, not the keyframes.

Re-render only the shots above (`python -m studio keyframes 035-walrus-without-a-bite --shots s009,s011,s020,s022,s062,s063,s107,s137,s147`) and send them back for a round-2 check.

## Keyframes round 2, 2026-11-02 (re-rendered: s009, s011, s013, s020, s022, s052, s062, s063, s106, s107, s124, s127, s137, s147, s154, s169, s207-s210)

**Verdict: FAIL. Director, 2 small composition fixes (both are counter-zone collisions in re-rendered shots). There are no asset fixes, and nothing fails on style or policy. All 5 round-1 fixes are resolved.**

I opened every re-rendered keyframe at full size and checked the neighbours on a strip (s018-s024, s060-s064, s121-s127, s134-s140, s147/s148).

### Round-1 fixes: all resolved
1. **s018-s024 run:** s020 is now a low push-in on Doug and the towel with the sun. s022 is a tight reaction close-up (flat mouth, side-eye), with only the snout and tusk edging in. s023/s024 stay wide for the payoff. The run now reads wide, push, wide, close, wide. Doug is on-model at close-up scale (the shading crescent, the cap and the ink weight all scale correctly).
2. **s061-s063:** s062 is the bull facing the polar bear on the floe with a red arrow. s063 is a facing `walrus_bull_rearing` pair on cream with a red !. The three shots now use three different layouts.
3. **s137:** it uses the s126 side-view `walrus_hanging_asleep` with the green check, SAFEST, and Doug sitting on the floe. It no longer repeats s136/s138.
4. **s107:** SOMEBODY HURT is now at the top left (about x 170-950, y 150-220), in the sky, clear of the HUD and the bulls, and inside safe even under `shake`. The arrow and the warning triangle carry the beat, and there is still no wound.
5. **Label count (7.4):** s009 now shows HUNTED + FOUND DEAD only, outside the paper, with no stray tick. s011 shows RINGED + BEARDED only. s147 shows SIZE + TUSKS + VS.
- Notes: s013 BLUBBER now sits in the sky with a red arrow to the stained patch. The visual-screener items (s052 TEETH, s106, s127, s154, s207-s210 QUIET PLEASE sign with the post on Doug's hand side and his face clear) all read correctly.

### Required fixes (route: director)
1. **s169: the AERIAL SURVEY label collides with the WALRUS COUNT HUD.** The label is at (1160, 250) and runs to about x 1335, touching the walrus head icon at x ~1340 inside the reserved counter zone (art bible, Recurring layouts). Move it to the left of the plane, for example (300, 250). The plane's left edge is at about x 530, and the dashed sight lines stay clear.
2. **s124: THE SLEEP title (size 130, centred at x 960) runs to about x 1325 at y 180-280.** That is inside the counter zone and about 40 px from the HUD icon. Shift it left and/or shrink it so the right edge is at or below x 1280 (for example x 860, size 115). Keep it clear of the centre head (top at about y 410).

### Notes (not blocking)
- s154: the FEMALES AND YOUNG box bottom is at about y 1036, right at the safe edge. If you are already editing, raise it about 20 px.
- s126/s127 share the side cutaway framing back to back (HOOKED ON, then HEAD UP / BODY BELOW). The labels change the beat, so I accept it.

Re-render only s124 and s169 (`python -m studio keyframes 035-walrus-without-a-bite --shots s124,s169`). Once those two are clean, the art is approved with no further full review needed.
