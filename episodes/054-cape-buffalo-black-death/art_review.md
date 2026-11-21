# 054-cape-buffalo-black-death: art review (art director, 2026-11-21)

## Verdict: FAIL (REVISE 4 of 32 drawings; 3 shotlist fixes for the director). Board and red-X cows signed off.

What I checked: all four preview sheets (`assets/previews/054-assets-a.png`, `-a2`, `-b`, `-c`). Every buffalo re-rendered large on the dusk
orange (`#e88a4a`) and on the episode's own backgrounds. Silhouettes rendered at the shotlist scales. The icon checked at 0.3 on cream and on
near-black. Doug in `cow_costume` (both facings). Oxpeckers placed on the bull's back line. Calendar blanking rect + AGE text. Juice box
with DOUG. `parasite_blob` next to `virus_blob`. Map polygon checked against its projection. Keyframes rendered for s002-s206 (38 shots,
in context). Local bounding boxes measured against each footprint.

Tone and safety pass on all 32: no wounds, blood or downed animals; the calf is not cute (adult proportions, small eyes); the
oxpeckers' hide is clean; no trophy look; `cow_costume_flat` reads as a suit (zipper, printed X eyes). Palette: buffalo match the
requested hex values and read on every ramp step. Tiers are correct: animals, places and diagrams are detailed, `cleaner_human` is crude.

## 1. Drawings

| # | Asset | Verdict | Notes |
|---|---|---|---|
| 1 | `cape_buffalo_bull` | APPROVE | Boss, drooping horns that curl up, ears below the horns, mud plates, straight back. The back line is clean: oxpeckers and the cap sit on it in s048/s205/s206. Box x -358..406 (muzzle 16 past the footprint); no clash in the shots I rendered. |
| 2 | `cape_buffalo_bull_front` | APPROVE | Hard stare works. Horn tips land on the s031 dotted line. Nit, next time it's reused: the two shoulder lobes have full outlines, so they read a little like panels hinged on the head. |
| 3 | `cape_buffalo_wallowing` | **REVISE** | See fix 1. |
| 4 | `cape_buffalo_lying` | APPROVE | Chewing marks land at the muzzle (s041). |
| 5 | `cape_buffalo_head_boss` | **REVISE** | See fix 2. |
| 6-8 | `boss_stage_1/2/3` | APPROVE | Same head in all three. The gap closes clearly, and stage 3 is one ridged shield. This is the boss texture I want on the head_boss too. |
| 9 | `cape_buffalo_cow` | APPROVE | Browner, no boss, no mud, separate horn bases. |
| 10 | `cape_buffalo_cow_lying` | APPROVE | |
| 11 | `cape_buffalo_charging` | APPROVE | Reads as a charge at shot scale. The dust puffs are tan, with no stars. |
| 12 | `cape_buffalo_calf` | APPROVE | Not cute, unhurt. Height is 166 against the 250 footprint (smaller than the box); fine at s132/s146. |
| 13 | `buffalo_herd_wall` | APPROVE | The silhouette (s113) reads as a horned wall. Box x ±754 (54 past the footprint each side, horn tips); director, check s111/s135-s139 against the HUD. |
| 14 | `buffalo_herd_resting` | **REVISE** | See fix 3. |
| 15 | `buffalo_megaherd` | **REVISE** | See fix 4 (illustrator's own flag confirmed). |
| 16 | `buffalo_head_icon` | APPROVE | Boss and horns read at 0.3 (48 px) on cream. It vanishes on dark grounds: HUD fix B below (placement, not the drawing). |
| 17 | `oxpecker` | APPROVE | Red bill, yellow eye-ring, tail prop, feet on the anchor. |
| 18 | `oxpecker_yellow` | APPROVE | The bill difference is obvious at 2.4 (s049). |
| 19 | `oxpecker_flying` | APPROVE | |
| 20 | `acacia_tree_day` | APPROVE | Flat branch at y -330; Doug and the calendar sit on it in s041. Box x to +429 (branch tip, 49 past the footprint); clear in s040-s046. |
| 21 | `page_a_day_calendar` | APPROVE | Blank zone fits the white rect and the AGE/DAY text. Not the 034 wall calendar. |
| 22 | `calendar_page_flying` | APPROVE | |
| 23 | `garden_fence` | APPROVE | Hides the bull's legs (s017/s039). |
| 24 | `cleaner_human` | APPROVE | Crude tier, crescent head, free front hand holds the juice box (s063). |
| 25 | `juice_box` | APPROVE | Reads as a juice box, not medical. DOUG is legible. |
| 26 | `car_wash_brush` | APPROVE | |
| 27 | `crash_helmet` | APPROVE | |
| 28 | `cow_costume` | APPROVE | Face and cap fully visible in both facings; reads as a cow onesie (s131-s133). Nit: the hood C is a thin dark arc. A white hood with one patch would read better if this is reused. |
| 29 | `cow_costume_flat` | APPROVE | Zipper + printed X eyes + hoof boots read as a suit, never a dead cow. |
| 30 | `botswana_map` | APPROVE | The projection is exact: the border runs along 21 E north of 22 S and 20 E south of it, and Mababe sits at (24.4 E, 18.75 S). The fence error is in the shotlist (fix C). |
| 31 | `globe_earth` | APPROVE | |
| 32 | `parasite_blob` | APPROVE | Faceless, peach, nothing like `virus_blob` at 0.6. |

### Required fixes (illustrator)
1. **`cape_buffalo_wallowing`**: the mud streaks are full-height vertical bands evenly spaced along the body, so the bull reads as a
   segmented grub or caterpillar (s004 title card, s005). Replace them with short irregular drips hanging from the back line (3-5,
   different lengths, some diagonal). Give the back a shoulder rise behind the head and a rounded rump, so it reads as the top of a
   bull. Keep the mud lip, the footprint and the boss at (+200,-170).
2. **`cape_buffalo_head_boss`**:
   a. The boss texture is a crosshatch grid. It reads as a tweed flat cap, which competes with Doug's cap gag and kills the "helmet" read.
      Redraw it as curved transverse ridges and wavy grooves following the dome, with a darker edge where it meets the hair, the
      way `boss_stage_3` already does at small size.
   b. The neck/shoulder block ends in a flat cut at local y +262. In s026 (y 740, scale 0.95) and s027/s030 (y 640, scale 1.2) the
      cut sits mid-frame at y 989 / 954 on the cream card: severed-head rule (art bible, 027). Extend the shoulders down to local y
      **+380** (bottom at y 1101 / 1096, off-frame at the current placements). Nothing above y +200 moves. New footprint y -260..+380:
      please tell the director.
3. **`buffalo_herd_resting`**: the heads are small and only 2-3 clear the backs, so the row reads as overlapping logs. The
   s091 "The herd." reveal silhouette is a single black log with two bumps. Use 8 animals with every head visible and clear air round each
   pair of horns. Heads about 1.3x their current size. Stagger the back heights by at least 25 units, leave small gaps between rumps,
   and keep a mix of bigger bull horns and thin cow horns. Keep the footprint.
4. **`buffalo_megaherd`** (your flag, confirmed): it renders as a flat rectangular bar. The top edge is a straight fuzzy line, the left and
   right ends are straight vertical cuts, and the silhouette is a black rectangle. In s003 it reads as a brick wall beside the lion.
   a. Broken skyline: let the back rows' horns and boss bumps punch above the dust line, so the top edge is a row of horn shapes.
   b. Ragged ends: stagger the rows so each end steps down and out (smaller heads, a gap, one lone animal), with no vertical cut.
   c. Stronger perspective: front row 1.0, then about 0.7, 0.5, 0.35 and 0.25, with each row's heads overlapping the bodies of the row in
      front. Two rows of big heads plus a texture band is not enough for "a thousand".
   d. Dust (`#c8b58a` / `#e2d3b0`) stays behind and between the far rows and never covers the horn line. Keep the flat-bottom
      anchor and the footprint. Check it as `silhouette: true, glow_r: 0` at 0.33: it must read as horns, not a bar.

## 2. HEAD COUNT board: SIGNED OFF, with fix B
Design approved as specified: a cream board under the counter; values 1 → DOZENS (s092) → HUNDREDS (s185) → 1,000+ (s199), only going up;
red-on-pink `#ffd2cc` / `#e0201b` from the s203 boss death with the big red 1,000+ stamp, staying red to the end; staging only. The
"ABOUT 5,000" label beside the herd in s193 is the right call (the board never goes down). Now in the art bible (Recurring layouts).
Required (director, every shot s004-s207):
- **B1.** Put a cream `#e8dcc0` circle r 30 with a 4 px `#5a3a1e` rim behind the icon, listed before the icon. Without it, the charcoal
  icon disappears on the death beats (s023, s091, s112, s178, s203: invisible in the keyframes), the honesty cards `#4a4f5e` and the outro `#2a2030`.
- **B2.** Widen the board to x **1370-1810** (w 440). "BUFFALO VS DOUG: HUNDREDS" is 397 px at size 25 and leaves 6 px inside the
  420 board. Move the icon and disc to **(1330, 239)**. Text stays centred at (1590, 239), size 25.

## 3. s126 red-X cows: SIGNED OFF (keep red Xs)
The red X is standard channel screen furniture. The cows stay upright, unhurt and in full colour; there are no bodies, no X eyes and no
lying cows; and "ABOUT 8 IN 10" is the label. Greying them out would read as "dead" more than an X does. Keep it exactly as staged.

## 4. Buffalo palette: CONFIRMED. Colour ramp: SIGNED OFF, with fix A
The hide values are confirmed as requested and now in the art bible ("Cape buffalo hide"). The ramp is in the art bible as the
"Savanna midday-to-dusk ramp" with one change:
- **A. The Vote (s092-s111): drop the purple-over-orange dusk bands (`#8a6a8a` / `#e59a5e`) and use a single late-afternoon sky
  `#f6d07a`** on ground `#b8913a`. Purple dusk at item 5, followed by bright amber at item 6 (Carrier) and 7 (Bodyguards), runs the
  ramp backwards and spends dusk four items early (s093 → s118 in the keyframes). The "hour before the evening feed" is still daylight,
  so a low sun is fine if you want one (keep it out of the HUD zone).

Final ramp (sky / ground): 1 Dagga Boy `#fff3c0` / `#c9a24a` (mud `#8a6a4a`) · 2 Boss `#cfe9ff` / `#d9b45a` (lawn `#7cc25a`) ·
3 Hitchhikers `#8fd3ff` / `#c9a24a` · 4 Thicket `#f6dcae` / `#b8913a` · **5 Vote `#f6d07a` / `#b8913a`** · 6 Carrier `#f6c45a` / `#b8913a` ·
7 Bodyguards `#f2a24a` over `#f6c45a` / `#9a7a4a` · 8 Lion Killer `#b8573a` over `#e88a4a` / `#8a6a3a` · 9 Megaherd `#9a4a32` over
`#c9663a` / `#7a5a3a` · closing `#c9663a` over `#e59a5e` / `#8a6a4a`. Death beats `#0b0f14` / `#141a14`, cards `#f4f1dc`, honesty
`#4a4f5e`, outro `#2a2030`.

## 5. Other shotlist fixes (director)
- **C. s115 and s116, Namibia border fence** (illustrator's flag, confirmed): the line runs along 20 E from 18.3 S to 22 S (x 378), but the
  border there is 21 E, so the fence floats in Namibia, outside the green land. Use points
  `[[454,320],[454,601],[378,601],[378,810]]` (21 E from 18.3 S to 22 S, west along 22 S, then 20 E to 24.75 S). The Kuke fence line
  starts at x 378 (20 E) at 21.3 S, also outside: start it at `[454,548]`. Map at (720,620) s0.95: x = 720 + (lon-24.5)x76,
  y = 620 + (lat S - 22.25)x76.
- **D. s075, s079, s082 lying-bull silhouette glow**: the red glow can stay (neutral sand and reeds), but the speckle must not reach
  the ground under the lying bull. In s075 it pools below the body and reads as blood under a downed animal. Clip it at the ground
  line (ground-colour rect after the spray, then the texture spray again), or switch to purple `#5e4670`. Rule now in the art bible.
- **E. (after fix 3/4, keyframe gate)** s091 and s113 silhouettes sit black on `#0b0f14`/`#141a14` with no glow and barely separate
  from the night. Add a body-centre spray (density ~0.55) before the silhouette, per the art bible.

## Routing
- Illustrator: fixes 1-4, then re-preview (`python -m studio asset-preview cape_buffalo_wallowing cape_buffalo_head_boss buffalo_herd_resting buffalo_megaherd`).
- Director: A, B1, B2, C, D, E, then re-render keyframes. I review the full contact sheet at the keyframe gate.

## Art bible updates I made (channel/art_bible.md)
Cape buffalo hide; Savanna midday-to-dusk ramp; crowd and herd asset rules (broken skyline, ragged ends); no red glow on the ground under
a lying-animal silhouette; HEAD COUNT board layout (with icon disc).

---

# Round 2: redrawn assets + keyframe gate (art director, 2026-11-21)

## Verdict: FAIL (assets PASS; keyframes need 8 composition fixes from the director, then a spot re-check)

What I checked: the re-preview (`python -m studio asset-preview cape_buffalo_wallowing cape_buffalo_head_boss buffalo_herd_resting buffalo_megaherd`,
plus `assets/previews/054-assets-r1.png`), each asset again in context at full 1080p (s004, s026/s027/s030, s091/s092, s180/s185/s193/s202),
and all 18 contact sheets (210 keyframes incl. endslate). I checked round-1 fixes A-E in the keyframes as well.

## 1. Redrawn assets: all 4 PASS
| Asset | Verdict | Notes |
|---|---|---|
| `cape_buffalo_wallowing` | **PASS** | The streaks are now 5 short, uneven drips off the back line, and some of them slant. The shoulder hump rises behind the head and the rump is rounded, so it reads as the top of a bull and no longer as a grub (s004-s008, s019-s022). The mud lip is soft. |
| `cape_buffalo_head_boss` | **PASS** | The boss now has wavy transverse ridges with a darker rim, with no grid and no flat cap, and reads as a helmet (s027 "HELMET"). The shoulders run off-frame in s026/s027/s030, so no cut edge shows anywhere. |
| `buffalo_herd_resting` | **PASS** | There are 8 animals with every head up, clear air round the horns, staggered backs, and a mix of bull and cow horns (s092 at full size). As a silhouette at 0.52 it still reads as a low row, though the horns are faint (see K3, which is about staging and not the drawing). |
| `buffalo_megaherd` | **PASS** | It has a broken horn skyline, ends that step down, five perspective rows, and dust only behind the far rows. In s193 it reads as "thousands", and in s185/s186/s199 as a herd mound, not a bar. |

## 2. Round-1 shotlist fixes
- A (Vote sky `#f6d07a` / `#b8913a`, s092-s111): **done**. The ramp now runs forward without breaks from item 1 to the closing shot.
- B1/B2 (icon disc, board 1370-1810, icon at 1330,239): **done** on every shot, and the icon now reads on the death beats, the honesty cards and the outro.
- C (s115/s116 fence on 21 E / 22 S): **done**.
- D (s075/s079/s082 glow): **done**. No speckle reaches the ground under the lying bull.
- E (s091/s113 body-centre glow): s113 **done**. s091 is **not done**: see K3.

## 3. Consistency pass: what's good
Doug is on-model in all 210 frames: crescent head, red cap always visible (including the ghost and the cow suit), and auto-white on dark grounds.
The crude tier vs. the detailed tier holds throughout. The caption bar, counter and HEAD COUNT board stay in the same position on every segment
frame, and the board's values only go up (1 → DOZENS → HUNDREDS → 1,000+, red from s203). Death beats are cartoon (cap left
behind, ghost, suit flat with printed X eyes). There's no gore anywhere. The lion kills are silhouettes (s146/s147) or off-screen. The text is legible
and inside the safe area.

## 4. Fixes I made myself (trivial, re-rendered and verified)
- **s010**: the "BLACK DEATH" wordart collided with the "RANKING" label and sat on the book's edge. I moved RANKING under the clipboard (y 380 → 790) and moved the
  wordart to x 1020.
- **s177**: Doug (x 700) stood inside the herd wall's left edge, so his body flipped to white ink over the buffalo and a horn appeared to grow
  from his head. I moved Doug and his INTERN badge 170 px left (Doug x 530). He's now clear of the wall.

## 5. Required fixes (director), by shot id
Composition variety. The rule is that no layout repeats 5 or more times in a row and each shot must differ visibly from the previous one:
- **K1. s040-s046** (7 shots of the same full-width acacia, tree centre-left, Doug on the branch). Re-frame at least two of them:
  **s042** as a tight shot of Doug + the DAY 2 calendar on the branch (scale ~1.6, bull's horns just entering the bottom), and **s044** as a
  low shot of the lying bull filling the lower frame, with the branch and Doug's legs dangling at the top. s045/s046 may stay wide.
- **K2. s064-s069** (6 identical shots of the herd row + BUFFALO sign + prone Doug). Re-frame **s066** as a close-up of Doug's face and cap with
  the oxpecker standing on the cap (scale ~1.8, herd out of frame), and **s068** ("Doug is fine.") with the herd at right and Doug + the field
  guide at centre-left, or push in.
- **K3. s091** (Doug's death 398). (a) The glow is six equal sprays at y 830, which makes a flat-topped red fog block with square ends. It
  isn't a glow around the animals. Put one spray per animal, centred on each body (about y 870, r 110, density ~0.5), so the glow follows the
  head bumps, and raise the silhouette to scale ~0.62 so the horns read. (b) The cap on a lone green stem reads as a red tulip.
  Either make the stem an obvious reed (thin, cattail head, 2-3 more reeds beside it) or drop the cap on the trampled ground like s112/s203.
- **K4. s092 → s093**: back-to-back title cards with the same centred herd row. Re-stage **s093 "The Vote"**: 2-3 standing cows at scale ~1.2 with
  their heads up, staring left, and Doug small at right (or the herd at the right third with the title at left).
- **K5. Item 5 herd repeats (s097-s101, s104, s107, s108)**: the same mid-distance herd composition appears 8 times. Re-frame **s098** as a
  close-up of one standing cow's head (cow asset at scale ~2, cropped at the shoulders) with the white dashed gaze line, and **s104** ("Here's the
  uncomfortable part.") as a tight shot of Doug standing among the lying cows, low camera, with the herd's horns towering behind him.
- **K6. s172-s174** (3 identical intern line-ups). Re-frame **s173** as a close-up of Doug's head + INTERN badge, with the sitting lioness's
  head entering frame left.
- **K7. s199 → s200**: identical frames (only the arrow changes). Re-frame **s200** tighter on Doug + the badge, with the megaherd's front
  row looming larger behind (scale it up or move it nearer), so that "then at the small man" lands visibly.
- **K8. s137 → s138**: same frame with the herd wall and the crouching lioness. Shift **s138** so the herd wall dominates (scale ~1.1, lioness
  smaller at the far left).

Nits (optional): s034/s035 and s154/s155 are near-duplicate pairs, so a small push-in on the second shot of each would help. The dust cloud is
the subject in s181-s183 and s190-s192. That's acceptable as the megaherd motif, but s191 could include Doug's tiny silhouette for scale.

## Routing
- Director: K1-K8, then `python -m studio keyframes 054-cape-buffalo-black-death --shots s042,s044,s066,s068,s091,s093,s098,s104,s138,s173,s200`
  and rebuild the full contact sheets. I re-check only those shots. Everything else is signed off.
- Illustrator: nothing outstanding.
