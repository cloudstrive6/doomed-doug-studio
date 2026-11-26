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
