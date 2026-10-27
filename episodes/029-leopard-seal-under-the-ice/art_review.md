# 029-leopard-seal-under-the-ice: art review (assets)

## Round 2: APPROVED (art director, 2026-10-27)

## Verdict: PASS. All 37 assets are APPROVED and art is signed off for the assets.

I re-reviewed the six round-2 redraws from `assets/previews/029-leopard-seal-under-the-ice-assets-fixes.png`,
`-seal-mouths.png` and `-jaw-diagram-s161.png`. I also rendered the real keyframes that use them: s021, s079, s080, s105,
s155, s161-s164, s169 and s172-s174.

| Fix | Asset | Round 2 |
|---|---|---|
| 1 | `leopard_seal_gape` | APPROVED. Both jaws are outlined with rounded tips, and the concave mouth edge sits behind them, so the head no longer reads as sliced. In s105 at 1.3 it reads as menacing, not gory |
| 1 | `leopard_seal_open` | APPROVED. Same fix, and it matches `_gape` and the hero design. The small nub teeth stay non-graphic for s135 |
| 2 | `leopard_seal_jaw_diagram` | APPROVED. The back of the skull is closed and rounded, with no cut edge. The canines are clearly the longest teeth (about 1.6x the cheek teeth). The interlock zone is clear, and the s163 ring and s169 arrows still land on the sieve |
| 3 | `leopard_seal_canine` | APPROVED. It is slim and sabre-curved with a plain tan root, so it reads as a fang at 1.4 in s174 |
| 4 | `boat_fender_bitten` | APPROVED. Two diagonal crescent punctures with jagged rims, and no face read at 0.6 (s079) or 1.6 (s080). No red |
| 5 | `explorer_1916_rifle` | APPROVED. Carried across the chest at about 70 degrees with the muzzle above the back shoulder, so it is not aimed. No flash (s021) |

### Shotlist check against the moved canines (canines now at local x +270..+384, tips y -58 / +100)
- **s174**: no change needed. It uses the standalone `leopard_seal_canine` (600, 540, 1.4) plus `leopard_seal`, and does not
  use the jaw diagram, so it has no coordinates tied to the canine position. The FANGS wordart sits clear above the tooth.
- **s162**: I fixed this myself in `shotlist.json`. The dashed leader line from the interlock (978, 544) to the zoom
  circle ran straight through both canines, and the SHARP POINTS wordart (1500, 620) overlapped the upper canine tip and
  the chin. Changes:
  - The line now runs (978, 544) -> (1090, 420) -> (1380, 420), above the lower canine tip.
  - The wordart moved to (1560, 660). Its right edge is about 1800, which is inside the safe area.
  - `validate shotlist` passes and the re-rendered keyframe is clean.
- s155, s161, s163, s164, s169, s172 and s173: no overlays touch the canines, so no change.

### Minor, no action required
- The diagram's upper-canine gum reads a little like a pink cap at 1.1. This is acceptable for a textbook diagram, and the
  illustrator can soften it if there is time.
- The director's note on s064 (`thumbs_up` inside `penguin_costume`) from round 1 still stands.

## Next
The assets are signed off. Keyframe review happens at `art_approved` after the director renders the full contact sheets.

---

## Round 1 (superseded by round 2 above)

Art director, 2026-10-27. Reviewed the 37 new assets in `asset_requests.md` from the three preview sheets
(`assets/previews/029-leopard-seal-under-the-ice-assets-{seal,2,3}.png`). I also rendered three test scenes: the seal family on
ice `#dff4ff` and surface water `#3a9ad9` next to Doug at shot scale, the worn props on Doug (stand / thumbs_up), and
`leopard_seal_jaw_diagram` at its s161 placement (860, 520, 1.1).

## Verdict: FAIL (round 1). 32 APPROVED, 5 need fixes (all to the illustrator)

### Leopard seal design: SIGNED OFF (brief section 7)
The core design is approved and locked for the family. It has a long, slim, snake-like body, a slate `#5f6670` back fading to a
silver `#c9ced4` belly and dark irregular spots that are densest on the throat and shoulders. The head is long, flat and reptilian.
It has a small dark eye under a heavy brow, a grin line that runs back past the eye and no ear flaps. It reads as menacing, never
cute, and nothing about it looks like a kids' mascot. `leopard_seal`, `leopard_seal_hauled_out` and `leopard_seal_head_rising`
are clearly the same animal at every scale I tested (0.7 to 1.1). The fixes below cover only the open-mouth variants and the two
diagram pieces. They do not change the head, palette or spots.

## Per asset

| # | Asset | Verdict |
|---|---|---|
| 1 | `leopard_seal` | APPROVED (hero design, see above) |
| 2 | `leopard_seal_head_rising` | APPROVED. The ripple ring reads as emerging, not as a cut neck |
| 3 | `leopard_seal_hauled_out` | APPROVED |
| 4 | `leopard_seal_gape` | **FIX 1** |
| 5 | `leopard_seal_open` | **FIX 1** |
| 6 | `leopard_seal_jaw_diagram` | **FIX 2** |
| 7 | `leopard_seal_canine` | **FIX 3** |
| 8 | `boat_fender_bitten` | **FIX 4** |
| 9 | `explorer_1916_rifle` | **FIX 5** |
| 10 | `adelie_penguin` | APPROVED. The white eye ring is the real field mark, not a cute eye. A row at 0.34 reads |
| 11 | `adelie_penguin_swimming` | APPROVED. Alive and darting. The pink trailing feet read as feet, not as injury |
| 12 | `fur_seal_pup` | APPROVED |
| 13 | `crabeater_seal` | APPROVED. Pale scar stripes, never red |
| 14 | `krill_cloud` | APPROVED |
| 15 | `zodiac_boat` | APPROVED |
| 16 | `zodiac_boat_wrapped` | APPROVED. Reads as armoured |
| 17 | `zodiac_boat_wrecked` | APPROVED |
| 18 | `inflatable_dinghy` | APPROVED |
| 19 | `inflatable_dinghy_swamped` | APPROVED |
| 20 | `music_note` | APPROVED. Reads at 0.3 on blue |
| 21 | `photographer_diver` | APPROVED (`auto_ink`, no cap, camera clear of the head) |
| 22 | `quad_bike_rider` | APPROVED (`auto_ink`, generic, not a likeness) |
| 23 | `explorer_1916` | APPROVED (`auto_ink`, no cap) |
| 24 | `explorer_1916_skis` | APPROVED |
| 25 | `doug_skis` | APPROVED (checked under Doug, thumbs_up) |
| 26 | `penguin_costume` | APPROVED. Head, face and cap fully visible (see the director note) |
| 27 | `penguin_costume_flat` | APPROVED |
| 28 | `marina_pontoon` | APPROVED |
| 29 | `canvas_tent` | APPROVED |
| 30 | `new_zealand_map` | APPROVED |
| 31 | `bowling_lane` | APPROVED |
| 32 | `blubber_stove_pot` | APPROVED. No meat visible |
| 33 | `cinema_seat` | APPROVED |
| 34 | `endurance_wreck` | APPROVED |
| 35 | `selfie_stick_phone` | APPROVED |
| 36 | `pasta_strainer` | APPROVED |
| 37 | `vacuum_cleaner` | APPROVED |

## Required fixes (illustrator)

1. **`leopard_seal_gape` and `leopard_seal_open`: the mouth front edge.** The `#7a0d0d` mouth fill runs straight out to a flat,
   unoutlined edge between the jaw tips. The front of the head reads as sliced off, with a red block where the snout should be.
   On `_gape` the upper jaw tip has no closing outline either. This matters most in s178, where `_open` sits at scale 1.4 with no
   Doug, and in s105, where `_gape` is at 1.3. Fix it like this:
   - Close both jaws with their own black lip outlines, with the upper and lower jaw tips each finished as a rounded snout or chin.
   - Pull the mouth interior back from the tips, so its front boundary is a concave curve with a black line that sits behind the
     line between the tips. The background shows through the gap at the very front.
   - Keep `#7a0d0d`, the pink tongue on `_gape` and the existing tooth count.
   - On `_open` the teeth may stay as they are. The request asked for "a few nubs", so you may trim them to 3-4 per jaw, but this
     is optional.
   - Keep the same bboxes, anchors and mouth centres: `_gape` mouth at (+260, -280), `_open` gap at x +300..+410, y -45..+45.
2. **`leopard_seal_jaw_diagram`: the flat cut edge and the canines.**
   - The back of the head ends in a straight vertical edge with a dashed grey line. At the shotlist placements (860, 520, 1.1 in
     s161-s169, and 0.7 in s155/s172/s173) that edge lands mid-frame at about x 365. It reads as a severed head. This breaks the
     art bible's open-jaw cut-edge rule (from 027). Replace it with a closed, rounded back of the skull or neck outline, so the
     head ends in a curve with no flat edge. Keep the width at about 900.
   - The two canines at about (+310..+378) are no taller than the cheek teeth, so s174 (the canine card) has nothing to point
     back to. Make the upper and lower canines clearly the longest teeth: about 1.6x the cheek-tooth height, curved and pointed.
   - Leave the interlock zone at (+80, +40) clear of other detail, exactly as it is now.
3. **`leopard_seal_canine`: shape.** It is straight, symmetrical and banded, so at 1.4-1.6 it reads as an ice-cream cone or a
   corn kernel, not a fang. Redraw it as a long, slim, **curved** tooth:
   - The crown curves back like a sabre, with the tip at y -150 bent toward one side.
   - Shade `#f4ecd8` with grey on the inside curve.
   - Give the root half a duller tan with no horizontal bands, so nothing looks like a waffle cone. A single faint line at the
     gum line is fine.
   - Keep it about 110 x 300 with a centre anchor.
4. **`boat_fender_bitten`: the holes read as a face.** The two dark chevrons stacked on the white band look like a pair of
   frowning eyebrows, so the fender reads as a face at 0.6 (s079) and at 1.6 (s080). Draw them as clear punctures instead:
   - Two small dark-filled crescent or oval holes **side by side on a slight diagonal**, the spacing of a bite. Do not stack them
     vertically.
   - Give each one a jagged pale rim and a short wrinkle or dent line, so the vinyl reads as punctured and soft.
   - No red.
5. **`explorer_1916_rifle`: the rifle angle.** The rifle is held out in front of the face at about 40 degrees, so it reads as
   aimed forward and up. The brief's policy note asks for it carried *across the chest, muzzle up*. Rotate it to about 70
   degrees, with the butt at the front hip and the muzzle beside the back shoulder, above head height. Keep both hands on it and
   no flash.

## Director notes (no change needed for asset sign-off)
- s064 uses `thumbs_up` with `penguin_costume`. The costume hides the arm, so only a lone thumb pops out next to the hood, which
  reads as odd. Prefer `stand` (or `wave` if the gesture matters) for that shot, or accept the floating thumb knowingly.
- `leopard_seal_jaw_diagram`: keep wordart and the red ring off the canines once fix 2 lands, because s174 calls back to them.

## Next
The illustrator redraws items 4-8 (fixes 1-5), re-runs `python -m studio asset-preview` for those five, and pings me for round 2.
The 32 approved assets need no further review. `_gape` is bottom-anchored and about 390 tall, so the default preview cell
crops its head. Preview it at `--scale 0.6` or on a scene canvas.
