# 058-pilot-whales-chase-orcas: visual review, keyframes (visual screener, 2026-11-26)

## Round 1

**VERDICT: FAIL**

### What I reviewed
- On disk, `build/contact/` held only `sheet_01.png`, and it was a 3-tile partial re-render (s185, s216, s217) left by the
  art director's `--shots` pass. That pass overwrites `sheet_01` and leaves no sheets 02 to 19. The keyframes on disk also
  predated the last shotlist edit (keyframes 00:04-00:05, shotlist 00:06:13).
- I re-ran `python -m studio keyframes 058-pilot-whales-chase-orcas`. It writes only to `build/`; I did not touch the shotlist.
  That produced 223 keyframes and `sheet_01..19.png`. I viewed all 19 sheets, zoomed full-res on suspect shots
  (s053, s058, s064, s074, s088, s116, s123, s147, s186, s215, the board) and rendered s216's frame before the blackout.
- **Note for whoever re-runs a subset:** `keyframes --shots` overwrites `sheet_01.png` with only those shots. Run the full
  set again before the next screen.

### What passes
- Doug is on-model everywhere he appears: red cap and white head, plus the orca costume, squid costume, fisherman hat and ghost.
  He reads against surface, twilight, abyss, sky and cream.
- No gore. All five deaths cut away or go to black (s031, s059, s104, s183, s216). The calf is plain, not cute. No nursery tone.
  The lamb/wolf (s142-143), dog (s095) and owl (s027) gags stay deadpan.
- All on-screen text is spelled right, including SÆDÍS, PORPOISING, CHEETAHS OF THE DEEP, SCIENCE, 1993 and 24 / 34. Nothing is
  cropped. HUD and board stay inside the safe area.
- Most pictures match the narration. The map dots are in the right places: Vestfjord, Canary Islands, Ecuador, Breiðafjörður,
  Westman, Gulf of Mexico. The s116 sperm-whale rosette is correct, heads in and tails out.
- Since the art director's pass, the s078/s079 hook branch lines, the s185 orca position and the s217-219 cap position are all fixed.

### Required fixes (blocking)

1. **WHO RAN board logic is backwards, every shot s002-s219.** *Art director (device) + director, needs CD sign-off.*
   The board says "WHO RAN" and ticks pile up under **PILOT WHALES** (7 by the end). A viewer reads that as "pilot whales ran
   7 times", which is the opposite of the episode's thesis. Then "ORCAS" is stamped under EVERYONE ELSE, which uses the
   header the right way. So the board contradicts itself.
   Fix: in `lib058.py`, move the tally ticks to the **EVERYONE ELSE** column. The tick x-coordinates are 1458/1476/1494/1512,
   the slash 1449-1523, and 1544/1562; shift each by about +165 so they sit in the right column.
   The PILOT WHALES column stays **empty all episode**: they never ran, and that is the joke.
   At the boss (s216 at 0.88 onward, and s217-s219), stamp the red "ORCAS" over or under the ticks in the same column.
   Option: put it on a second line at y ≈ 372, or drop the ticks to y 316-360.
   Alternative if the CD wants to keep the ticks on the left: rename the header to "WHO BACKED OFF?" and the left
   column to "NOT PILOT WHALES". This is weaker; I prefer moving the ticks.

2. **s136-s139: run of 4 near-identical compositions.** *Director.*
   All four show the orca at about (860,560) at the same scale with the calf under her, and s133/s134 repeat the same layout too.
   The orca and calf frame appears 7 times in s131-s145.
   - s137 ("watched the pair for twenty-one minutes"): switch to a surface shot. Use the whale-watching boat from s135 with
     two fins (orca plus calf fin) and the clock/21 MINUTES label.
   - s139 ("saves energy and stays sheltered"): use a close-up. Calf at scale ~0.9 tucked against the orca's flank, with only
     the orca's belly/flipper in frame, and a white slipstream curve.
   - s134: flip the shot (`flip: true`) and place it small and far (orca scale 0.3 at right) so it isn't a copy of s133.

3. **s124-s127: run of 4 near-identical compositions.** *Director.*
   Each shot has the dinghy at the same spot, two fins on the right and two sperm whales on the left. Keep s124 and s125.
   - s126 ("Doug survives."): use a tight shot of Doug alone in the dinghy, scale ~1.0, thumbs-up, no whales.
   - s127 ("Nobody is more surprised than the narrator… less pleased"): use a plain white card with a small Doug
     shrugging and a deflated party balloon or an unpopped confetti cannon. Keep LESS PLEASED.

4. **s177-s180: run of 4 near-identical compositions.** *Director.*
   Each shot has the orca on the left and the pod on the right on surface blue. Keep s178 and s180.
   - s177 ("the unsettling part"): use a close-up of the orca's face, scale ~1.0, with a sweat drop and the ⚠ sign.
   - s179 (grandmothers/aunts/cousins/sons): use a family-portrait row. Labelled pilot whales lined up facing the camera
     (`pilot_whale_front`), with the orca small in the corner.

5. **s068 ("someone eating your groceries out of the cart while you're still pushing it"): the picture doesn't show
   the gag.** *Director.*
   The trolley is empty and the second stick man just stands there.
   Fix: put groceries in the trolley (bread, bottle, fish; a small `fish` asset is enough). Doug pushes the trolley (walk
   pose, hands on the handle at ~(640,760)). The stick man walks beside the trolley with one item raised to his mouth.
   s095 reuses the trolley: add the same groceries there as well.

6. **s058 and s215: pilot whale drawn as an unreadable black blob.** *Director (s058, s215); illustrator if a new pose is needed.*
   Both use `pilot_whale_front` with `silhouette: true` at scale 0.3-0.4. At that size it reads as a sea mine or ink blot,
   not a whale.
   - s058: replace it with the side-view `pilot_whale` as a silhouette with a cyan rim (as in s034), scale ~0.5, heading
     at Doug from the right edge.
   - s215: drop the silhouette. Use 4-5 `pilot_whale_front` (non-silhouette, scale 0.3, as in s216) entering from the left
     edge, so "the wall of black heads turns to him" lands.

7. **s123: broken drawing.** *Director.*
   The right thermometer's red fill stops short. Rect y 410, h 107.4 leaves a white gap above the bulb, which reads as a
   cracked thermometer. Change it to `h: 300` (bottom at y 710, matching s122's fill bottom) so the column is continuous.

8. **s147: both calves sit on Iceland's coastline.** *Director.*
   The calf at (400,300) straddles the Westfjords and the calf at (1000,700) straddles the east coast.
   Move them into open sea: the first to (380,620) and the second to (980,830).
   The narration is "other orca groups… with other pilot whale calves", so put a small `orca` (scale 0.18) beside each calf.

### Recommended (not blocking)
9. **s006 "4 OUT OF 5"** *(director)*: five identical tagged whales and no speaker in frame. Add the speaker at the right
   with red sound arcs. Draw red arrows from 4 whales toward it, and grey out or turn away the 5th.
10. **s202 "a whole pub emptying out"** *(director)*: the four stick figures just stand beside the pub. Make it one family
    (a pilot whale or a cap-less family group) entering the door, with 3-4 stick men running out the far side with speed lines.
11. **s186** *(director)*: "THE ONES WHO LEAVE" ends ~25 px from the WHO RAN board. Shift it left by 80, or move it
    to y ≈ 960. The leftmost pod whale is also cut by the frame edge; move the pod right by 60.
12. **s074 / s178** *(director)*: the red X covers key letters ("DEE_ DIVE", "SP__NT", "A FEW _HALES?"). Use a single red
    strike-through line across the label, or shrink the X to 70% and centre it so the word stays readable.
13. **s111-s113, s115, s118, s120** *(director)*: the big sperm whale above the small pilot whale repeats 6 times in 10 shots.
    There are never 4 in a row, but the block feels static. Flip s115 and frame it from below.
14. **s155-s158** *(director)*: Doug, fish and calf appear 3 times in a row, then Doug alone in the same spot. On s157
    "POLITEST", cut tighter on Doug's face, holding the fish out, at scale ~1.0.
15. **s064 / s067 / s075 / s081** *(illustrator)*: the bitten tuna head on the hook reads as a white jagged blob at
    scale <0.4. Use scale ≥0.5 where it's the subject (s064, s067), or show a whole tuna missing a bite.
16. **s088** *(director)*: the `diver` asset (white round head, no cap) reads as a capless Doug at a glance. Give the diver a
    visibly different head, e.g. a dark hood or a yellow mask strap.

### Next step
Fix items 1-8. Then re-run the **full** `keyframes` (not `--shots`) so all 19 sheets are fresh, and send back for round 2.
