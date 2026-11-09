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

---

## Keyframe review (art director, 2026-11-08): FAIL, 5 composition fixes (director)

Reviewed: `build/contact/sheet_01.png` to `sheet_17.png` (s002-s202 and the endslate; s001 waits for the thumbnail).

Doug is on-model in almost every shot, including the hard hat (s021), the amoeba and mammoth costumes (s144, s167-s168) and the
ghost beats. The approved assets read cleanly in context. The counter and TIME TRAPPED furniture is consistent, and the timer turns red
from s173. The death count runs 308 to 315, which matches the tally on s196. Reveals use silhouettes with a red glow (s087-s089,
s126, s147). The sober place-and-date cards with no Doug counter (s024-s029, s082-s083) follow the brief and are approved as a
deliberate exception. Nothing is gory. The remains are never drawn.

### Required fixes (director)
1. **s022: Doug has no red cap on screen** (style bible 7.2). Only the two boots stick out of the hole. Put the `doug_cap` asset at
   the passage mouth, as in s023 and the brief ("the cap is left at the passage mouth").
2. **s200-s202: two caps on screen.** Doug stands with his cap on, and a second `doug_cap` lies beside the suitcase. Follow the brief
   ("end on the full suitcase and the cap"): either drop Doug from these three shots, or keep him and give him gear `cap_off`. Do
   not show both.
3. **Item titles cross scenery** (art bible, Text). s006 runs over the cave passage, s031 over the ridge and trees, s054 over the
   mountain ridges, s127 over the lake and borehole, and s149 over the fossil grid. Move each title into clear sky or onto a plain
   band (y about 340-360, clear of the counter zone), or shrink the scenery under it.
4. **Repeated composition, s007 and s009-s014.** The same full cave cross-section appears in 7 of 8 consecutive shots, and only the
   arrows change. Reframe at least two of them. For example, push in on the downward crack with Doug head-down in it for s011
   ("Here's the problem") and s013 ("pushing uphill, head-down"), so the squeeze reads at close range.
5. **s197: the T. rex silhouette has a purple halo, not a red glow** (style bible 7.7). Use the red spray (`#ff2a1a`) as in s178,
   or set `glow_r`.

### Minor (non-blocking)
- s081: the red arrow points at an empty pit floor while the narration says "found a skeleton". Since remains are never drawn, end
  the arrow on a small red-glow spray spot, or drop the arrow.
- s121: the small blue circle with a red X next to the worm is unreadable at size. Make it bigger or remove it.
- s130-s145: 16 shots of the same lavender lab layout with Doug at right. s138/s139 and s142/s143 are near-twins. If time allows,
  add one close-up or a split framing in the middle of the run.

Re-render s006, s007, s009-s014, s022, s031, s054, s127, s149, s197 and s200-s202 as keyframes, then send them back for re-review.

---

## Keyframe re-review, round 2 (art director, 2026-11-09): FAIL, 1 composition fix (director), s022 only

Reviewed: `build/contact/sheet_01.png` to `sheet_04.png` (the 39 re-rendered keyframes listed in decisions.md), plus full-size
checks of s006, s013, s022, s088, s164, s191 and s197. The shots that were not re-rendered are unchanged from round 1 and were
approved then, so I did not need to run any extra keyframes.

### Round 1 required fixes
1. s022 cap: fixed. A `doug_cap` lies at the passage mouth next to the suitcase.
2. s200-s202 two caps: fixed. Doug is `cap_off` and there is one cap beside the suitcase. Ending on the full suitcase and the cap matches the brief.
3. Item titles over scenery: fixed. s006, s031 and s054 now sit in clear sky, s127 sits above the lake in the sky band, and s149 sits above the dig frame.
4. s006-s014 repetition: fixed. s011 and s013 are tight push-ins on the crack, so the run now alternates wide, close, wide, close.
   No figure appears in the real case, which is correct.
5. s197 glow: fixed. The red spray reads clearly behind the black T. rex, with no purple.

### Round 1 minor items and the visual review changes: all good
s081 ends on a red glow spot. s121 is now a curled worm with DRY FIRST and reads well. s036 has a larger crossed plate. s057 places
5,300 YEARS clear of RECENT?. s164 shows one large pelvis with a PELVIS label, and it reads as a bone. s147 has no topbar. s050 shows
the hand with the sticker. In s051 Doug walks out with the suitcase. s118 and s120 are a worm close-up and a family tree of dishes.
s189 and s191 are a feeding close-up and Doug's shocked close-up, which is on-model with the cap, crescent and oval eyes.
s088/s089 now show the sabre fangs on the cat, which has legs and so cannot be a walrus, and the upright clawed sloth, which has no trunk.
s145 shows the red cap on the amoeba. s201 has one room box. The run variety is now good across s117-s121 and s188-s192.

### Required fix (director)
1. **s022: there are stray red marks on the clipboard that read as blood drips.** The clipboard asset's red marks show outside
   the white cover rect, at about (545, 665) and (495, 725), as red drops under ONE MORE PASSAGE. This is a death beat next to
   a real fatality, so it must not carry anything that looks like blood (no gore). Enlarge the white cover rect so it covers the
   whole paper (about `x 288, y 465, w 272, h 295`) or use a clipboard without the red checks. Then re-render s022 only.

The rest of the episode is approved. Once s022 is re-rendered without the red marks, art is approved, and no further art director
pass is needed beyond a glance at that one frame.

---

## Round 3 spot check (visual screener on behalf of the art director, 2026-11-09): PASS

Open item from round 2. **s022: stray red marks on the clipboard: RESOLVED.** In the re-rendered `build/keyframes/s022.png`
the clipboard paper is solid white from the clip to the bottom edge, and the only red is the ONE MORE PASSAGE text. Nothing
reads as drips or blood. The `doug_cap` at the passage mouth, the boots and the suitcase are unchanged.

Also checked: s087-s089 `smilodon_body` is redrawn with cat ears, a muzzle and an open-jaw notch, upper-jaw sabres and slimmer
stalking legs. It reads as a sabre-toothed cat, not a walrus, and stays on-style (black silhouette with a red rim).

No open art items remain. Art is approved for the episode.
