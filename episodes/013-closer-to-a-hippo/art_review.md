# Art review: 013 closer-to-a-hippo, library assets (18)

Reviewer: art director. Previews: `assets/previews/013-closer-to-a-hippo-assets-a*.png`, `-b*.png`
(`-b-context.png` re-rendered after the fixes below).

**Verdict: PASS** (3 small REVISE items fixed by the art director in `/tmp/hipgen/gen.py`, re-generated and re-previewed).

## Hippo set (illustrator A, `/tmp/hippo_gen/gen.py`)
One animal across all poses: same palette, head, eye/ear/nostril layout. Detailed tier (outline, flat fills, darker
back, paler belly, spray) against crude Doug. Small eyes with heavy brows, no smile, no blush, short thick legs: reads
dangerous, not cuddly. Bold silhouettes hold at the 0.33 scale.

| # | Asset | Verdict | Notes |
|---|---|---|---|
| 1 | `hippo` | APPROVED | Barrel body, level back, lower canine at the lip corner. Points match the request. |
| 2 | `hippo_yawn` | APPROVED | Clear 150-degree gape, flat pink interior, no tongue/saliva/gums, tusks read. Canine tip 17 units off the request (noted by illustrator) is fine. |
| 3 | `hippo_waterline` | APPROVED | Ears/eye/nostrils read at 2.4x and at map scale; covers `hippo_rock`. |
| 4 | `hippo_rock` | APPROVED | Reads as a plain river rock; 300x64 accepted (fits inside waterline). |
| 5 | `hippo_grazing` | APPROVED | Mouth on the grass tuft at the requested point. |
| 6 | `hippo_red_sweat` | APPROVED | Orange `#e8662a`/`#f0902a` with white gloss reads as wet coating, not blood. Director: keep the "NOT BLOOD" label on screen in s094-s097 as planned. |
| 7 | `hippo_trot` | APPROVED | All four feet off the ground, clear gap for the s087 arrow, shadow on y=0. |
| 8 | `hippo_underwater` | APPROVED | Mid-tone body reads on murky `#5d6b45` and on black. |
| 9 | `hippo_sleeping` | APPROVED | Eyes shut, calm pose; works for the three-up diagram. |

## Batch B (`/tmp/hipgen/gen.py`)
| # | Asset | Verdict | Notes / fixes |
|---|---|---|---|
| 10 | `hippo_submerged` | REVISE -> FIXED | (a) The mouth line curved up into a corner with a pink dot, which read as a **smile** (kid-appeal rule). Fixed: the mouth line now runs flat and turns down (`(372,70)->(330,78)->(290,92)`), and the pink corner is a small 5x4 flesh spot with no outline. (b) The belly spray under the jaw spilled outside the outline as grey fuzz. Fixed: moved to (310,96), r 22. |
| 11 | `hippo_mouth_front` | REVISE -> FIXED | Spray spilled outside the outline (grey fuzz above the head and beside the cheeks on the orange background). Fixed: back spray now (0,-880) r 80, cheek sprays (+-425,-500) r 30. The silhouette reads as a gaping mouth. The red speckle in the silhouette tile is the engine's intended glow, not the asset. The chin centre stays light, so Doug's black ink reads. |
| 12 | `hippo_canine` | APPROVED | Wear facet at the tip, yellow root, at ruler scale. |
| 13 | `lettuce` | APPROVED | Reads at 0.32 on dark pink-red. |
| 14 | `tent` | REVISE -> FIXED | The light-green spray at the top right bled past the dome outline. Fixed: (80,-160) r 35. Mid-tone fills read on the night ground. |
| 15 | `sticking_plaster` | APPROVED | |
| 16 | `dung_cloud` | APPROVED | Flat, abstract scribble with no lumps. Gross but not gross-out. Use in one shot only. |
| 17 | `africa_map` | APPROVED | Matches the `world_map` style, with rivers, lakes, Madagascar and the Arabian edge. Director: check the icon positions on the s232 keyframe. |
| 18 | `astronaut` | APPROVED | Crude tier, no cap, auto_ink works on black and on white. |

## Routing
- No outstanding asset fixes for the illustrator.
- Director: follow the notes on #6 and #17 when you check the keyframes.

---

# Keyframes review (contact sheets `build/contact/sheet_01..22.png`, 253 shots)

Reviewer: art director, 2026-10-09. I checked crowded spots against the full-size frames in `build/keyframes/`.

**Verdict: FAIL.** 12 blocking fixes, all composition fixes for the **director**. Fixes 13-20 are non-blocking and should go in the
same pass. The illustrator has no asset fixes.

## What passes
- **Doug is on-model in every shot:** crude tier, red cap on every live Doug and every ghost, white auto-ink on the night shots.
  Waders and swimmers follow the hip-at-surface rule (s144, s146, s158, s196...), with the water rect starting at the hip. Death images:
  s092 uses `on_back` + `dead` with no `rotate`. s066, s141, s166, s193 and s217 show the ghost plus the cap. The gravestone cap gag in
  s069, s093, s142 and s252 is fine.
- **Counter and meter:** the counter goes 107 -> 114 and ticks once on each of the 7 deaths. The distance meter steps down
  11,000 km -> 1 km -> 300 m -> 50 m -> 10 m -> 5 m -> 2 m -> 1 m -> 0.5 m -> 0 m, and its label stays below the counter on every shot.
- **Zone colours hold within each item:** savanna/Magdalena day, Honk sunset, Night Walk navy, Charge/Red Sweat/Yawn mud bank,
  Shallows murky olive cross-sections, Canoe sunset, Bull Territory overcast sage, Mouth maroon/sunset. The diagram beats all use the
  cream backdrop. The item title cards are red, at y 330-360. The white section headers (s004 "FAR AWAY.", s048 "ON LAND.", s143 "IN THE
  WATER.") are consistent with each other. I have logged them in the art bible as a separate card type.
- **Assets:** they read at every scale. The red sweat is orange with "NOT BLOOD" on s094-s097, as the asset notes asked. `dung_cloud`
  is used once (s044). The s232-s234 map icons are plausible (question marks over West/Central/East Africa, hippo icons in the south).
  The field guide in s251 follows the 010 layout. There is no gore, and no tooth touches Doug.
- s001 is "(thumbnail pending)". That belongs to the graphic designer's package stage and does not block this gate. Re-check it at packaging.

## Blocking fixes (director)
1. **s003:** the "AS FAR AS HE COULD" wordart sits on the map's ice band and crosses the bottom frame line (art bible, Text). Shrink
   `world_map` to about 0.8 and raise it, then put the wordart in the freed strip under the frame. Keep it inside y 1040.
2. **s150:** the right edge of "NEVER LEARNED" (960, 220) butts against the DOUG DEATHS box, inside the reserved counter zone. Move it to about
   (900, 320) at size 80, clear of the whale and the dolphin.
3. **s163:** "DOUG CAN" (1420, 320) sits about 10 px under the DISTANCE label. Move both wordarts to y about 390 (the sky runs to y 455).
4. **s195 and s219:** the title card glyph tops are at about y 264, right under the DISTANCE label (s219's "H" touches its corner).
   This episode's meter extends the counter zone down to y 258, so use y 360 as the other title cards do. In s195 use size 130 so the
   title clears the yawn tips.
5. **s194:** ghost Doug at (1300, 330) is inside the counter zone, with his cap against the DISTANCE label. Move him to about (1050, 360).
6. **s061:** the bottom-anchored hippo silhouette puts its red glow on the path under its feet. The speckle reads as a blood puddle
   (art bible, Silhouette glow sizing). Set `glow_r: 0` and add a red `spray` at the body centre (about 420, 590). Then follow the 003 s146
   recipe: a ground-colour rect from the horizon down under the glow, with the path redrawn on top.
7. **s118:** the title card shows the full-colour `hippo_yawn` one beat before the s119 silhouette, which spoils the reveal (style
   bible 7.7). Use `hippo` (closed mouth) or `hippo_waterline` here, so the yawn appears first as the s119 silhouette and then in colour in s120.
8. **s250:** this is a death beat with no cap in frame. The counter ticks to 114 on a black screen (art bible, eaten-whole rule: never a death beat
   with no cap). Draw `doug_cap` (about 0.5) after the black rect, low and centred, appearing with the counter. Or keep 113 here and tick on s251,
   where the cap floats out.
9. **s135-s139:** 5 consecutive shots have the same composition (Doug left, yawning hippo right, same mud bank). Re-lay **s137** as a
   close-up: `hippo_yawn` at about 1.3, head and jaw filling the right two-thirds, the 150-degree arc on the jaw, and Doug small at the left edge.
10. **s211-s215:** 5 consecutive shots of bull / Doug / bull with the same framing (s196-s197 use the same frame too). Re-lay **s212**
    as a cream top-down river-strip diagram: two 50 m territories (two coloured bands with a waterline hippo icon each) meeting at a tiny Doug,
    with the "50 M" label on one band. This also matches the narration.
11. **s013-s017:** 5 consecutive shots on the same savanna-river composition. The backdrop runs from s004 to s017, broken only by
    s006's inset. Re-lay **s015** as a cream count card in the s021 style: "2023" plus "169", with a short row of hippo head icons.
12. **s035, s036:** 3 keyword labels on screen (OWN GROUP, NEIGHBOR, STRANGER), against a max of 2 (style bible 7.4, 011 s083 precedent).
    s034 already named the first panel in the same position, so drop the OWN GROUP label in s035 and s036.

## Non-blocking (fix in the same pass)
13. **s087:** the red arrow ends inside the letters of "FEET". Start it at the wordart's top edge (about y 900).
14. **s026, s030:** "MOZAMBIQUE" and "1 KM" (s026) and "1.6 KM" (s030) sit on the acacia crown and trunk. Move them into clear sky
    between the tree and the counter (about x 1150-1350, y 330-420), and keep the dashed line off the trunk.
15. **s033:** Doug's head sits on the right lake's outline. Move him about 120 px left onto clear ground.
16. **s213, s214:** the red dashed border runs through Doug's face and torso, which reads as a skewer. Break it about 30 px above the cap and
    resume it below the feet. s216 can keep the full line.
17. **s222, s236, s225:** the wordart sits 20-30 px under the DISTANCE label (s222 THE LARGEST, s236 ONE OF THE DEADLIEST) or level with
    the counter row (s225 NO INTEREST). Lower s222 and s236 to y ≥ 330. For s225, use size 80 at about (860, 160) so it ends before x 1200.
18. **s065:** the two floating eyes beside the tent read as a capless Doug in the dark. Make them clearly the hippo's (a silhouette head edge with
    red glow peeking past the tent) or drop them.
19. **s191:** this is the same moment as s190/s192 (sunset) but has the day-blue sky. Use the Canoe sunset bands (`#e88a4a` over `#f2a24a`).
    Optional: do the same for the s172 and s175-s177 cutaway skies, so the item never flips to daytime.
20. **s164:** the underwater red glow spreads into the water and the riverbed around the body. A red cloud in water is the blood-in-water
    image. Shrink `glow_r` so the ring stays about 60 px outside the body, and cover the riverbed with a riverbed-colour rect after the spray.

## Re-check
After the fixes, re-render only the touched shots (`python -m studio keyframes 013-closer-to-a-hippo --shots s003,s013,s015,s026,s030,s033,s035,s036,s061,s065,s087,s118,s137,s150,s163,s164,s191,s194,s195,s212,s213,s214,s219,s222,s225,s236,s250`)
and send the sheet back to the art director.

**Keyframes verdict: FAIL** (12 blocking fixes for the director: 1-12. No asset fixes.)
