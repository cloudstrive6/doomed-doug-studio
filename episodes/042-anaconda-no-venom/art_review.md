# 042 art review: new assets (art director, 2026-11-09)

Reviewed: `assets/previews/042-assets-snakes.png`, `042-assets-a.png`, `042-assets-a-diagrams.png`, `042-assets-b.png`,
`042-assets-b2.png` (39 drawings, which matches asset_requests.md). I also ran my own checks: the bounding box of every asset at
scale 1 against the requested anchor and size; Doug at scale 1 inside the wrap pair and the capybara suit (scales 1 and 0.48);
cap placements at the shotlist offsets (caiman s146, lump s128, breeding ball s055, antivenom s075, eye bumps s168); everything
on the near-black night background `#0b1020`; the grey and red-rim silhouettes on `#0d1410`; and the HUD icon at 0.32.

## Verdict: FAIL (1 asset to redraw). 38 approved: 36 as drawn and 2 fixed by me. Fix 1 blocks art_approved.

### Approved as drawn (36)
- **Anacondas:** `green_anaconda` (heavy female, matches the palette, still reads as a snake in silhouette at 0.22-0.3),
  `anaconda_eyes_water` (eye and nostril bumps face right, the ripple ring reads on night water), `anaconda_head_open` (backward
  teeth, no fangs; the `#7a0d0d` mouth is flat colour, not gore), `anaconda_wrap_back`/`_front` (Doug's head, face, cap and
  shoulders are clear above the top loop; the shins show below the bottom loop, which helps readability; the grey stick-man
  silhouette works as the victim too), `anaconda_lump` (smooth bulge, the cap sits on it at (0,-100)), `anaconda_swallowing`,
  `breeding_ball` (writhing, not cute; the cap at (0,-150) lands on a male's head and reads fine), `baby_anaconda`,
  `hanging_scale_sling` (the dial centre is blank for "97.5 KG").
- **Diagrams:** `anaconda_skull_side` (six rows, hooked back, no fangs), `snake_jaw_below` / `_spread` (unfused halves, the pink band
  stretches), `anaconda_eye_closeup` (the clear dome shield and shine read), `snake_throat_cutaway` (the windpipe opening is a small
  dark hole. It reads as an opening, not as blood).
- **Animals:** `capybara` (incisors, calm, not cute), `spectacled_caiman` (slimmer than the library crocs, spectacle ridge, yellow
  eye; the cap at (0,-97) x0.6 sits on its back), `deer_stag_lying` (eyes closed, no wounds, the antlers carry the silhouette).
- **Costume and human:** `capybara_costume` (face and the whole cap are visible at 1 and 0.48, cheap felt, no antlers),
  `bare_foot_step` (crude tier, `auto_ink` true, white on night).
- **Props:** `antivenom_box`, `hunt_stage_post` (boards at -460..-100 as specified. In the preview sheet only the top is cut, because
  the 800x600 tile is too small), `hunt_stage_icon` (at 0.32 it still reads as a post with a red pointer), `south_america_map`,
  `pressure_gauge` (no needle), `heart_monitor` (the screen is empty), `smartwatch`, `lungs_icon`, `bp_cuff_arm` / `_big`,
  `bp_cuff_band`, `fish_hook_cork` (the barb is visible), `garden_hose_knot`, `hose_beach_ball`, `minivan` (no logos),
  `reward_poster`.

### Fixed by the art director (2), now approved
1. **`anaconda_coiled` floated above its anchor.** The lowest coil was at y -28 (bottom-centre anchor, so it hovered in s005-s019,
   s052, s057, s070, s071, s089). I wrapped the drawing in a group at y +30, so the bottom now sits at y +2. The head is now near
   (+200,-220). No shotlist values reference the head position.
2. **`anaconda_constricting_caiman` sank through the ground.** The -10 degree tilt pushed the anaconda's tail tip to y +68
   (bottom-centre anchor). I changed the inner group to rotate -6, y -70, so the bottom now sits at y +2. The caiman still tilts
   nose-up and the struggle reads the same. Check: `assets/previews/042-ad-fix-ground.png`.

### Fixes required
1. **`caiman_holding_snake` (illustrator, blocks s136, s137): the snake does not read as "held in the jaws".** At shot scale
   (0.85) the anaconda lies flat along the ground under the caiman's chin. The short section through the mouth gets lost among
   the teeth, and the X eye is about 6 px, too small to read. Redraw the snake so it hangs crosswise from the closed jaws:
   grip it at about local x +330, y -60, and let one limp U-shaped section drape down each side of the snout, with the
   head end lying on the ground in front. Make the X eye at least 3x bigger, in black with a 4 px line. Keep the anchor
   bottom-centre with the feet on y=0, and keep the width inside about x -400..+520. No blood. Re-preview at 0.85.

### Notes (not blocking)
- `capybara_costume`: the hood flap with two ears behind the head reads a little like a ponytail at 0.48. The illustrator can
  make the ears rounder and more separate if there is time.
- `anaconda_wrap_*`: the coils hide Doug's arms. That is fine for a constriction, but the director should not use a pose that
  depends on the arms (for example `arms_up`) inside the wrap.
