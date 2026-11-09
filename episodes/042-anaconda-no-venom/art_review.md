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

---

# 042 art review, round 2: caiman re-approval + keyframes (art director, 2026-11-09)

## Asset re-approval: `caiman_holding_snake` PASS
Checked `assets/previews/042-assets-caiman-fix.png`, `042-caiman-fix-s136-0.85.png`, `042-caiman-fix-zoom.png`, and the rendered
s136/s137 keyframes. The snake now rises in a loop into the closed teeth and drops out the far side, so it reads as gripped, not
lying on the ground. The head lies in front with a big black X eye that reads at shot scale and on the contact sheet. No blood. Feet
are on y=0 and the width stays inside the requested band. It is not the exact "U on each side" pose I asked for, but it does the job,
so it is approved. All 39 assets for 042 are now approved.

## Keyframes: FAIL (4 composition fixes for the director; the rest is approved)
Reviewed all 15 contact sheets (s001-s171 + endslate). s001 is the thumbnail placeholder (the designer has not run yet), so it is not reviewed.
What is good: Doug is on-model everywhere (red cap, white ink on the night scenes, ghost Doug keeps the cap). The counter steps
322 -> 329 on the right shots and the hunt-stage HUD tracks the signpost. Each item has its own palette (pale swamp, ochre dry season,
olive breeding pool, cream diagrams, sunset coils, navy caiman night, near-black final hunt), and the background darkens as the hunt
moves toward "kept". Title cards are red. Silhouette-then-reveal is used (s040 -> s041, s129, s138). Nothing is gory: the X-eye snake,
the red mouth interiors and the throat cutaway are all flat cartoon.

### Fixed by the art director in shotlist.json (re-rendered, verified)
1. **s064**: the two red X's were drawn on top of "NO FOLDING FANGS" / "NO POISON" (unreadable, and a double negative). I moved them
   to the left of the labels (x 1190, scale 0.35).
2. **s096**: the "WHEN TO STOP" wordart overlapped the top of the heart monitor. I moved it to (560, 420), above the coils.
3. **s097**: the red arrow ran through the "ARTIFICIAL HEART" label. I moved the label to (1000, 930) and the arrow to (880,905)->(740,840).
4. **s044**: the "WRITHING" wordart ran into the reeds. I moved it to x 1060.
5. **s046**: "LONGEST 46" had no unit, so I changed it to "LONGEST: 46 DAYS" and moved it to x 1400, clear of the reeds.
6. **s133 / s138 / s141**: text sat on the moon. "OFTEN" is now at x 600, "EAT HIM" at y 290, and "UNDER THE PLANTS" at (1400, 470),
   which also clears the leg.
7. **s144 / s145**: the "CAIMAN" flag text was 22 px and unreadable. It is now 34 px.
8. **Calendars too small to read**: s042 ("DRY SEASON", was 15 px) and s054/s057 ("7 MONTHS") are now at calendar scale 0.9.
   s052 and s140 ("+5 DAYS", calendar lowered to y 470) are now at 0.8, and s166 ("MONTHS", 32 px) at 0.7. The text was scaled
   up with each calendar.
9. **s159 / s160**: these had `topbar: false` and no HUD, so the caption bar was missing mid-item (style bible 7.3 under Art Director).
   The caption bar and the counter/hunt-stage HUD are restored (copied from s158).

### Fixes required (director), these block art_approved
1. **s041-s047: the same composition 7 times in a row.** Breeding ball centre-right, bank lower-left, reeds right, Doug on the
   bank. Only the labels change. Keep s041 (title), s044 and s047. Recompose at least s043 and s045 so they look different.
   For example, s043 could be a close crop of the ball (scale ~1.6, Doug's head peeking in at the edge), and s045 a cream diagram
   with 13 small male snake icons in a row and 3 of them highlighted ("USUALLY 3"). Do the same for s053-s056, which reuse
   the framing again 4 times: put s054 on a cream background (calendar + empty plate + coiled female, like s052, but with a red
   "?" over a male).
2. **s081-s084, s089, s096-s099: the boas are drawn as green anacondas.** In s089 the shot contrasts "BOAS" with "ANACONDAS INCLUDED"
   using the same drawing, so the viewer can't tell them apart, and a commenter will notice. Either (a) ask the illustrator
   for a `boa_constrictor_coiled` (tan/brown with dark saddles and a red-brown tail, the same footprint as `anaconda_coiled`, plus a wrap
   front/back pair if you keep the rat shots), or (b) at minimum, recompose s089 so the difference doesn't depend on the drawing
   (e.g. one coil labelled "BOAS: TESTED" and a bigger one labelled "ANACONDAS: SAME TRICK"). With (b), the rat shots can keep the anaconda wrap
   with their "BOA" label.
3. **s159 / s160: two text-only grey cards in a row** with no drawing and no Doug (his only appearance is s158). Make it a picture:
   anaconda head striking (`anaconda_head_open`) at a stick-figure field assistant (`scientist`, cartoon, no contact shown)
   with the label "2 FIELD ASSISTANTS". Then s160: a red "?" over a small stack of clipboards with "VERY FEW, HARD TO VERIFY"
   and Doug shrugging. Keep at most 2 labels on screen.
4. **s109: there is a stray green flatline** floating at (1350-1700, 560) with no monitor. It reads as a rendering glitch. Either add
   `heart_monitor` (scale ~0.6, right of the reeds, below the counter zone) and draw the flatline on its screen, or delete the line.

### Notes (not blocking)
- s012 -> s013 -> s014 show the same map three times. s012 ("Here's the twist") would hit harder as a Doug shock close-up with a red "!".
- s059-s066 show the skull in 5 of 8 shots. s066 ("that's not what the bite is for") could use the strike head + Doug instead.
- s067-s069 and s072 show `anaconda_head_open` on plain cream, so the neck ends in mid-air. A short water line or a pond edge under it
  would ground it.
- s055/s056/s146 show capless Doug (the cap is on the ball or the caiman, in frame). That is fine as a gag, but don't let it run longer than 2 shots.
- s074/s143 have thought-bubble episode tags ("010", "027") at about 20 px. They are fine as easter eggs, but they don't need to be read.

Note: I re-rendered the full keyframe set (172 frames) after the fixes, so `build/contact/` reflects the current shotlist.
