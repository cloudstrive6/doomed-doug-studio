# 040 art review: new assets (art director, 2026-11-08)

Reviewed: `assets/previews/040-props-1/2/3.png`, `040-micro-final.png`, `040-micro-1s.png`, `040-micro-3.png`,
`040-mega-full/sil/dark.png`, `040-costume-test.png`, `040-costume-assets.png`.

## Verdict: FAIL (24 of 29 approved; 5 fixes, all for the illustrator)

### Approved (24)
- Stickers: `sticker_nutty_putty`, `sticker_otztal_alps` (Ö legible), `sticker_hoyo_negro`, `sticker_kolyma`,
  `sticker_yukechi`, `sticker_hot_springs`. One family, on-brief colours, peeling corner, legible at 0.8x.
- Props: `sticker_roll`, `ice_pick`, `pneumatic_drill`, `longbow_broken`, `trophy_cup` (the top crop is only the preview cell),
  `snowmobile`, `sleeping_bag`.
- Micro: `permafrost_nematode` (the C-coil and the small z's read as dormant, clearly a different pose from `devil_worm`),
  `permafrost_nematode_active`, `acanthamoeba`, `pandoravirus` (a touch more saturated than #c8a0d8 but reads well, no spikes, no face).
- Places: `mammoth_dig_layout`. A clean museum grid with animal bones only and a walkway. It reads at 1.0.
- Megafauna: `giant_ground_sloth`, `gomphothere`. Both are silhouette-only uses, and the red-rim silhouettes read clearly.
- People/costumes: `neanderthal` (the brow, hair and fur wrap stop it reading as Doug; auto_ink works on dark), `mammoth_costume`
  (head, flat face and cap visible, deadpan, trunk loop present), `amoeba_costume`, `amoeba_costume_flat`.

### Required fixes (illustrator)
1. **`mammoth_pelvis`: it reads as a skull or face.** The two dark round openings look like eye sockets, the sacrum looks like a nose
   and the small acetabula look like eyes. The brief bans skulls, and four of these in a row (s164) will read as faces. Make the
   obturator openings paler, taller and slanted (an oval or teardrop in a mid-tan, not near-black). Move the acetabula to the outer
   side edges as side-facing cups, and widen and flatten the iliac wings so it reads as a hip girdle. Check it at 0.3x.
2. **`short_faced_bear`: the ears read as spectacles.** The two small ringed circles sit on the brow. Redraw them as two rounded
   bumps on the head's top silhouette. Also remove the head ellipse outline that crosses the shoulder (it shows as a stray seam).
3. **`columbian_mammoth`: stray overlapping outlines on the head.** The ear and head ellipses draw double lines across the face and
   neck. Clip or remove the hidden outline parts. This asset is used full in 4 shots (s151, s156, s165, s166), so it must be clean.
4. **`woolly_mammoth`: same seam issue as fix 3** (the ear ring and neck line show through). A small cleanup.
5. **`sticker_south_pacific_gyre`: the text is too small at suitcase scale.** At 0.3-0.5 the two-line caption is the least legible
   of the set. Shrink the swirl icon and enlarge "SOUTH PACIFIC / GYRE" to match the cap height of the other stickers (stay at about 130 wide).

Optional (non-blocking): `gomphothere` tusks are drawn as two broken prongs. One clean, slightly upturned tusk pair would be
neater if the illustrator is already in the file.

Re-preview fixes 1-5 as `assets/previews/040-fixes.png`, with fix 1 and fix 5 also shown at 0.3x, then send back for re-review.

---

## Re-review (art director, 2026-11-08): PASS, 29 of 29 approved

Reviewed: `assets/previews/040-fixes.png`.

1. `mammoth_pelvis`: fixed. The wide, flattened iliac wings read as a hip girdle. The obturator openings are now pale tan
   slanted teardrops, not dark sockets, and the acetabula sit on the outer edges as side cups. At 0.3x it reads as a bone,
   not a skull or face.
2. `short_faced_bear`: fixed. The ears are rounded bumps on the top silhouette, with no spectacle read, and the shoulder
   seam is gone.
3. `columbian_mammoth`: fixed. There are no double lines on the face or neck. It is clean on both white and dark grounds.
4. `woolly_mammoth`: fixed. The ear ring and neck line no longer show through.
5. `sticker_south_pacific_gyre`: fixed. The caption is enlarged and the swirl is smaller. At 0.3x "GYRE" reads clearly, and
   "SOUTH PACIFIC" is as legible as the `sticker_kolyma` reference at the same scale.

Optional `gomphothere`: done. The tusks are clean and upturned, which is also accurate for a four-tusked gomphothere.

Note for the director: the tusks of both mammoths and the gomphothere reach the right edge of the preview cells. Keep them
inside the frame when you place them.

Asset gate cleared. Ready for keyframes.
