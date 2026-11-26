# 058-pilot-whales-chase-orcas: art review (art director, 2026-11-26)

## Verdict: PASS (assets PASS after art-director fixes; keyframes PASS with notes for the director)

Reviewed `assets/previews/058-pilot-whales-chase-orcas-assets.png`, close-up test renders on white, surface `#3a9ad9`,
twilight `#1b4f86`, abyss `#050a1f`, sky and cream, and all 223 keyframes (`build/contact/sheet_01..19.png`).

## Assets (20)

| # | Asset | Verdict | Notes |
|---|---|---|---|
| 1 | `who_ran_board` | **APPROVE after fix (applied)** | Headers were ~10-12 px tall and thin at 0.55, and couldn't be read on the contact sheets. **Fixed:** WHO RAN 54 to 62, PILOT WHALES 34 to 40, EVERYONE ELSE 32 to 36, all with a 2-unit chalk-colour stroke so they render chunky. The divider now starts at the underline (y -34) instead of y -80, so each header gets the full half-width without hitting it. Cap height is now ~16/14.5 px at 0.55, and the board reads on white, sky, sea and black. Tally zones are unchanged. |
| 2 | `pilot_whale` | APPROVE | Round melon, forward hooked fin and sickle flipper all read. You can tell it from `orca` at a glance (no eye patch). It reads on abyss thanks to the `#4a4f58` highlight, and its silhouette mode works. |
| 3 | `pilot_whale_front` | APPROVE | Calm, blank "wall of heads". It reads in crowds at 0.22-0.4. |
| 4 | `pilot_whale_head` | APPROVE | Deadpan and works beside the rowboat. |
| 5 | `pilot_whale_calf` | **APPROVE after fix (applied)** | Plain, so it meets the CD condition. The fetal-fold bands (`#7a8088`, width 3) read as **ribs** at 0.4-0.6, which looks starved or skeletal. **Fixed:** they are now `#5d626b` at width 2, a faint banding that stays documentary. |
| 6 | `pilot_whale_old` | APPROVE | The pale melon patch, scars and fin nick set her apart. The cap at (+250,-80) sits on her melon correctly (s183-s184). |
| 7 | `orca_costume` | **APPROVE after fix (applied)** | The full-height white front panel made the egg-shaped suit read as a **penguin** at small sizes (s004, s221). **Fixed:** the white is now a lower-belly panel only (y -40..+74) and the hood eye-patch is bigger (rx 15, ry 34). The suit is now mostly black with a low white belly, tall fin and flukes, so it reads as an orca. The face, red cap and zip are still visible, and Doug is on-model. |
| 8 | `orca_costume_swim` | APPROVE | Reads well. A few of Doug's stick limbs poke out under the suit in swim2. This is acceptable because it's crude on purpose. |
| 9 | `orca_costume_flat` | APPROVE | X eye, no tears, no bite marks. The illustrator flagged that the fin reaches y -66, so the shotlist now puts the cap on the **hood end** (see the shotlist changes below). |
| 10 | `oceanic_whitetip` | APPROVE | The paddle fins and mottled white tips are right. Closed mouth, not gory. |
| 11 | `beluga` | APPROVE | |
| 12 | `beaked_whale` | APPROVE | |
| 13 | `owl` | APPROVE | Grumpy-plain, not cute. |
| 14 | `cheetah` | APPROVE | |
| 15 | `iceland_map` | APPROVE | It's on-style and has the Westman Islands at (-78,+223). Breiðafjörður at (-240,-28) is open sea in the bay between Snæfellsnes and the Westfjords, clear of the islets. No dot is baked in, and the shotlist draws one, as intended. |
| 16 | `fisherman_hat` | APPROVE | Perches on the cap in the `sit` pose with the red dome and brim visible. |
| 17 | `longline_hook` | APPROVE | It has no branch line, as flagged. The shotlist now draws one where needed (see below). |
| 18 | `longline_hook_baited` | APPROVE | The `longline()` helper already draws the branch lines. |
| 19 | `pub_front` | APPROVE | No text, logos or drinks. |
| 20 | `dive_mask` | APPROVE | Small but legible on the melon (s045). |

## Shotlist changes made by art (in `build/gen_shotlist.py`, regenerated, validate OK)
1. **Hooks (s078, s079):** the three reeled-in `longline_hook`s floated loose under the rowboat. Added a `HOOK_UP()` helper that draws a 3 px `#2b2b2b` branch line from the waterline to each hook eye.
2. **Flat costume cap (s217-s219):** moved `doug_cap` off the flopped fin and onto the hood end, where Doug's head was. The cap is now at costume local (+150,-42), i.e. (1050, 500), next to the X eye.
3. **Iceland dots (s132, s188):** checked. The Breiðafjörður dot (-240,-28) and Westman dot (-78,+223) both land in the sea at the right places, so no change was needed.
4. **s185:** the orca overlapped the map frame's bottom-right corner. Moved it from (1200,860) to (1290,800).
5. **Boss "ORCAS" on the board (s216-s219, in `lib058.py`):** at size 40 it overflowed the right tally zone into the frame. It is now size 36 in ComicNeue-Bold (chalk font) and keeps its black outline.

## Keyframe review
The style is consistent, Doug is on-model in every pose and gear (costume, squid costume, hat, ghost), and zone colours
follow the bible: surface `#3a9ad9`, twilight `#1b4f86`, midnight/abyss, cream maps. HUD text is legible and inside the
safe area, and no element collides with the board. Nothing gory, and the death frames are clean.

## Notes for the director (recommended, not blocking)
1. **Sædís block, s133-s145:** the same orca and calf composition (orca at ~(860,560), same scale) appears in s133, s134, s136, s139 and s145, with s138 and s141 near-identical. It never reaches 5 in a row, but the section feels static. Flip her or change the scale or framing on two of them (e.g. s139 close-up on the calf's flank, s145 small and far).
2. **Sperm-whale block, s111-s115 and s121:** the same big sperm whale and small pilot whale layout repeats 4 times in six shots. Vary one (e.g. s115 from below or flipped).
3. **Speaker block, s005-s012:** several shots use the same "speaker on a rope + Doug + one whale" layout. Consider one wide shot or one map beat.
4. **s147:** the left calf on the Iceland map straddles the map frame and the coast. Move it from screen (400,300) into the open sea south of Snæfellsnes, e.g. screen (380,620), which is map local about (-272,+80).

No illustrator fixes outstanding. Assets are approved for keyframes and packaging.

---

## Round 2: keyframes (art director, 2026-11-26)

### Verdict: FAIL (3 small composition fixes for the director; each one is test-rendered below)

Reviewed: fresh full render, `build/contact/sheet_01..19.png` (00:15-00:16, newer than `shotlist.json` 00:15:34), 223 keyframes.
I checked every changed shot at full res in `build/keyframes/`.

**Verified fixed:**
- **WHO RAN board, s002-s219:** every tick is in EVERYONE ELSE and PILOT WHALES stays empty. 7 ticks by the end. The red ORCAS
  stamp (s216 end, s217-s219) sits on its own line under the ticks, inside the chalk area. It reads correctly at full size and on
  the sheets. ON-MODEL.
- **s058:** the side-view pilot whale is a black silhouette with a cyan rim, heading at Doug. It reads as a whale.
- **s123:** the right thermometer column is continuous down into the bulb.
- **s126:** Doug is alone in the dinghy, close up, thumbs up. **s127:** white card, NO PARTY balloon. This breaks the s124-s127 run.
- **s134** (small and far), **s137** (surface boat, clock and 21 MINUTES), **s139** (calf close-up under the orca's belly with a
  slipstream). This breaks the Sædís run. In s139 the calf's faint fold bands read as documentary at 0.9, not as ribs. OK.
- **s147:** both pairs are in open sea, each orca beside its calf, off the coast.
- **s157:** tight on Doug holding out the fish. The dive mask is consistent with s155-s158.
- **s177** (orca face close-up, sweat drop, ⚠) and **s179** (family-portrait row with labels, small orca in the corner).
- **s186:** text clears the board and the pod is fully in frame. **s215:** five non-silhouette `pilot_whale_front` heads from the
  left. **s074/s178:** strike-through lines keep the words readable. **s088:** the diver no longer reads as capless Doug.
- Style is consistent, zone colours follow the bible, HUD and text are legible and inside the safe area, nothing is gory, and every
  death frame is clean.

### Required fixes (director, in `build/gen_shotlist.py`)

1. **s187 is a near-copy of s186** (back-to-back: pod on the left, white speed lines, orca on the right, same scale). Rule: each shot
   must look different from the one before it. Keep the THE CHASE title and the sky/sea split, and make s187 a **surface fin shot**.
   Remove the pod, the `orca` and the 3 speed lines, then add:
   `pilot_whale_fin` ×4 at y 524, scale 0.5, x 180/380/580/780 · `orca_fin` at (1300, 524) scale 0.6 · two white wake lines,
   width 5, from x 1210 to 1050 at y 500 and y 530 · `water_splash_small` at (1360, 520) scale 0.5.
   I test-rendered this layout at orca x 1380 and it reads well. Moving the orca to 1300 gives the board more room.
   s192 also uses fins but comes 5 shots later and has Doug and the sun, so that's fine.

2. **s068 / s095: Doug floats ~25 px above the floor and his hand misses the trolley grip** (50-90 px gap). The gag is "pushing it
   round the store", so he has to be pushing. **I added the pose `push1`/`push2` to `studio/doug.py`** (both arms forward at
   shoulder height). The art bible's Poses section has the placement formula. Use it with Doug and trolley at the same scale:
   - s068: doug (560, 801) scale 0.55 pose `["push1","push2"]` · `shopping_trolley` (715, 814) scale 0.55 · `bread_loaf` (687, 751)
     0.29 · `soda_bottle` (749, 725) 0.21 · `silver_fish` (708, 732) 0.22 · shift the second stick man, his arm line and his bread
     150 px left (man x 930) so he walks right beside the trolley.
   - s095: doug (1100, 801) 0.55 `["push1","push2"]` · trolley (1255, 814) 0.55 · bread (1227, 751) · bottle (1289, 725) · fish (1248, 732),
     same scales as s068.
   I test-rendered both: feet on the floor line, both hands on the red grip, groceries in the basket.

3. **s122 / s123: stray red slivers in the left (ACTUAL DANGER) thermometer.** The white mask rect is narrower than the boiled red
   column, so two thin red lines show inside the tube. Widen the mask in both shots from `x 542.4, y 550, w 35.2, h 160` to
   `x 532, y 545, w 56, h 168`. Test-rendered: the tube is clean and the outline is untouched.

### Recommended (not blocking)
- s199-s201: the same big orca, Doug and pilot whale frame three times in a row. On s201, cut to the two weight labels side by side
  with both animals at true relative scale, or flip it.
- I agree with the screener's recommended items (s006, s202, s064/s067 tuna scale, s115 flip, s125 arrow).

### Re-check
Change only s068, s095, s122, s123 and s187, then re-run the **full** `keyframes` (`--shots` overwrites `sheet_01`). I'll
spot-check just those five frames in `build/keyframes/`. If they match the specs above, this is a PASS with no further full review.
