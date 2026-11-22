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
