# 055 art review: new assets (art director, 2026-11-22)

**Verdict: PASS** (assets). Two composition fixes go to the director before keyframes.

Reviewed: `assets/previews/055-sperm-whale-circle-assets.png`, `-assets-wide.png`, `-costume-context.png`, `-kayak-context.png`.

## Assets
1. `sperm_whale_calf_costume`: **PASS, including the non-cute kid-appeal check.** It reads as a grey block-headed sperm whale at 0.8 and at 0.3.
   The hood has a flat box face, wrinkles, scar rings and an S-blowhole. It has no eye, no smile, no teeth, no blush and no pastel, and the
   felt is wrinkled, not plush. Doug's face and the whole red cap stay clear at every scale and when flipped. The black outline holds on
   `#8fd3ff`, `#2a6aa6` and `#14365e`. It is the detailed tier against crude Doug, so it is on-bible.
2. `sperm_whale_calf`: PASS. Slate grey, with a short box head and a small slit eye. Not cute, no wounds.
3. `big_headphones`: PASS. The band clears the hood, the cups sit beside the face and the cap is clear.
4. `sea_kayak`: PASS. The yellow hull reads on the ice sky and on `#3a9ad9`.
5. `cap_snow`: PASS on the `sit` pose. The `point` pose needs a placement fix (see Composition 1).
6. `doug_frozen_kayak`: PASS. Doug is frost-white with X eyes, there is no ice block (so it is not the 007 return), and the cap still reads red.
   Not gory.
7. `shift_rota_clipboard`: PASS. It looks like office paperwork and is blank. Note: the ruled rows sit between y -130 and +190, not at the
   requested -80/-20/+40.
8. `bunker_cutaway`: PASS. The ladder-stair is steep enough to land the joke.
9. `castle_wall_cannons`: PASS. The fuses are unlit and the top is at -400, under the HUD.
10. `hand_bell`: PASS.
11. `pilot_whale_fin`: PASS. Low, broad and hooked, and clearly different from `false_killer_whale_fin` and `orca_fin` side by side.

## Composition fixes (to director)
1. s061 (`point` in the kayak): set `cap_snow` y = Doug y - 42 (scale 0.6) so the snow sits on the cap, not the face. Move Doug to y 432
   (cap_snow 390) so his legs stay inside the hull. Right now they hang about 50 px below the keel.
2. `shift_rota_clipboard` text overlays (s035, s039, s040): put the "08:00 GRAN" / "09:00 AUNT" / Doug rows on the drawn ruled lines
   (between y -130 and +190 local), not at -80/-20/+40. I will check this at keyframes.

## Ruling: costume in 7 of 9 items
**Approved as shotlisted (items 1, 2, 4-9; off only for the item 3 kayak run).** The art bible's costume-continuity rule (049) applies: once
Doug is in a costume for a run of items, every Doug in that run wears it, and it only comes off on a scripted beat. The approved script keeps
him in it, and item 3's kayak trip is the scripted break. Taking it off and putting it back on just to hit a count of 4 would break
continuity and read as a mistake. I read the brief's "max 4" as a cap on the featured costume beats (thumbnail, item 1, item 5, boss),
not on how many items he wears it in. The costume passes the kid-appeal check above, so wearing it longer adds no policy risk.
Conditions for keyframes:
- Vary the framing. Not every costume shot should be a mid close-up of Doug. Use the 0.3 top-down rings, cards without Doug, the headphone
  shots and the item 3 break.
- No costume-only gags in items 2, 4, 6 and 7. The costume is the setting there, and the joke stays on the science or the shift rota.
- The creative director should log the deviation from the brief in `decisions.md`.

---

# Keyframe review (2026-11-22)

**Verdict: FAIL.** Style, Doug, palette and policy all pass. The fail is on composition variety: six runs of 5 to 11 near-identical
shots, plus two small text fixes. All fixes go to the director. No asset fixes.

Reviewed: all 203 keyframes plus the endslate in `build/keyframes/`. `build/contact/sheet_01.png` only holds s152 because the last
partial `--shots` run overwrote it. Re-run the full `keyframes` (no `--shots`) before resubmitting, so the contact sheet covers every shot.

## Passes
- Doug is on-model in every shot: costume hood, the red cap always visible (including ghost Doug s201-s203), expressions from the fixed set.
  The kayak run uses the bare rig, and the costume comes off only for item 3, as ruled.
- Asset-stage fixes are verified. s061: the snow sits on the cap and the legs are inside the hull. s035/s039/s040: the rota rows sit on the ruled lines.
- The colour ramp matches `decisions.md` per item (sky greys toward the attack, water darkens, first light in item 9, cream cards, black death beats).
- No gore. Deaths are told with the cap, gaps and a cut to black, and no orca touches a whale or Doug. The silhouette-with-red-glow reveal is used (s046, s067).
- The caption bar, counter (402 to 408, red-on-pink from 408) and annotations are present. Text is inside the safe area.

## Fixes (to director)
Rule for all of these: **at most 4 consecutive shots with the same framing** (same top-down rosette scale, same horizon line-up).
Break each run by changing the camera, not just the label.
1. **s099-s109 (11 top-down rosettes in a row).** Re-frame at least three of them:
   - s101 BADLY HURT: underwater side view of the ring, heads in and tails out, with the hurt whale pushed into the middle.
   - s104: a mid close-up of Doug squeezing between two heads at the rim (whales at about 0.8 scale, cropped by the frame edge).
   - s108: a surface-level view of the ring of backs on the horizon, with Doug's hood in the gap.
   - Keep s107, the big close-up.
2. **s087-s093 (7 top-down).** Make s091 HEADS a cropped close-up of the heads meeting in the centre (whales at about 0.9, no full ring in frame).
3. **s157-s160 (same ring-left / orcas-right / Doug-bottom-left layout 4 times, inside a 7-shot run).**
   - s158 ALONGSIDE: a side view at the surface (water `#18497e`, sky `#6a7686`), with a whale swimming beside the fins.
   - s160 LEADING THE WAY: a close-up on the lead whale and its arrow.
4. **s164-s170 (7 top-down).**
   - s166 NEVER: change it to a cream `#f4f1dc` card or to a close-up of a single orca fin at the ring's edge.
   - s168: a close-up of Doug being shoved back into the middle.
5. **s186-s191 (6 top-down).**
   - s187: a side view below the surface, with the ring above and the dashed gap.
   - s190 (11:00): a cream card with the clock, in the same layout as s123/s171.
6. **s059-s066 kayak run (s061-s064 are the same frame 4 times).**
   - s062 LIVES ALONE: an extreme wide shot with a tiny kayak and a lone whale in a big ice-sky frame.
   - s063: a close-up of Doug's snow-capped head with the whale's eye beside him.
7. **s041-s046 (6 horizon line-ups in a row).** Make s043 (900 KG) a cream comparison card, with the calf against a familiar object as in s026.
8. **s098:** "NOSE TO NOSE" overlaps the bottom-right bus. Move the label about 60 px down and right, or move the bus up, so they don't touch.
9. **THE RING map tile (item 7, s133-s152):** the white "THE RING" title is illegible on the light map. In the fin-count tiles (s180-s191),
   fins cover the title. Put a `#14365e` strip across the top 22 px of the tile, behind the title, on every shot, and keep the fins and map below it.

Items 1-7 are re-framings only. Keep the narration splits, labels and timings. Resubmit the full contact sheet for re-review.
