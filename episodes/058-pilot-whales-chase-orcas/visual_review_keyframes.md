# 058-pilot-whales-chase-orcas: visual review, keyframes (visual screener, 2026-11-26)

## Round 4 (thumbnail re-check after the designer's fixes)

**VERDICT: PASS** for thumbnails A, B and C. All three can run as the A/B/C test (A primary).

Checked the 00:25 re-renders (`build/thumbnail.png`, `thumbnail_b.png`, `thumbnail_c.png`) at 1280x720, and each `_small`
(168x94) blown up 4x with nearest-neighbour scaling, with a simulated "18:42" duration badge drawn at x 132-164, y 79-90.

- **A: WRONG WAY: PASS** (unchanged). The pilot whale wall is the focal point, Doug's red cap reads between the pod and the
  orca tail leaving on the right, and the caption is fully legible. The badge covers only the costume's tail fluke and speed lines.
  The floating sweat drop is still a nit and does not block.
- **B: THEY CHASE: PASS.** Round 3 fix 1 is done. The caption now ends around x 985, and at feed size the badge sits clear to
  the right of CHASE, so it reads in full. The pod of three reads as whales chasing right, Doug in shock in the costume is the
  centre, and the orca leaping off the right edge with the dropped fish reads as fleeing.
- **C: TOO SLOW: PASS.** Round 3 fix 2 is done. Each head now has a hooked dorsal fin, a white eye aimed at Doug, and wake
  lines, so at 168 px the row reads as a pod of whales in the water rather than boulders. Doug is bigger (head about 17-18 px
  wide at 168) and clear of the splash, with the gritted teeth readable. The badge sits on empty dark water. The orcas are still
  longer than any one head.

### Non-blocking nits (graphic designer, only if re-rendering anyway)
1. **C**: the upper orca (x 1170, y 360) has its tail stock tucked behind Doug's chin, so at feed size the pointed end can read
   as an orca nose touching his face. Move it about 60 px right (x ≈ 1230) so the gap between orca and Doug is clear.
2. **A**: lower the sweat drop about 50 px (y ≈ 280) so it touches the orca's back.

No gore and no kid-show tone. All three thumbnails match the title "Why Orcas Give Up Their Kill When Pilot Whales Show Up"
honestly and are not misleading.

## Round 3 (thumbnails at feed size + changed keyframes)

**VERDICT: FAIL** for thumbnails B and C only. Thumbnail A and all eight changed keyframes **PASS**.

Checked `build/thumbnail*.png` at 1280x720, the `_small` files at 168x94 (blown up 3x with nearest-neighbour scaling), and the
168x94 version with a simulated duration badge (bottom-right, about x 132-164, y 79-90). Also checked s006, s068, s095, s122, s123,
s125, s187 and s201 in `build/keyframes/` against their narration in `shotlist.json`.

### Thumbnails
- **A: WRONG WAY: PASS.** At 168 px the wall of pilot whale heads is the clear focal point. Doug (red cap) sits between the pod
  and the orca tail leaving on the right, and WRONG WAY is fully legible. Nothing important sits under the duration badge (only
  speed lines). It works with the title "Why Orcas Give Up Their Kill When Pilot Whales Show Up". Minor and not blocking: the
  sweat drop floats about 60 px above the orca's back and could be mistaken for a bubble.
- **B: THEY CHASE: FAIL.** The CD's round 2 changes landed. The pod is bigger, faces right and reads as whales, and the plain fish
  now reads as dropped prey. But the caption runs into the duration badge: at feed size the badge hides the "E" and half the "S"
  of CHASE, so it reads "THEY CHAS".
- **C: TOO SLOW: FAIL.** The scale inversion is fixed (the orcas are now clearly longer than any one head). But at 168 px the row
  of five `pilot_whale_head` shapes on the waterline reads as black boulders or a rocky shore. No fins, no flukes and no visible
  eyes make them read as animals, so the threat isn't obvious. Doug's head is about 13 px tall and half-merged with the splash.

### Thumbnail fixes (graphic designer)
1. **B (`thumbnail_test_b.json`)**: move the THEY CHASE caption out of the bottom-right badge zone. Either shift it left so it
   ends by x ≈ 960 (centre ≈ 560), or move it to the top-left of the yellow sky (y ≈ 40-150, x ≈ 40-700, clear of the orca's
   fin). Keep the size. Re-check `_small` with a 32x12 px badge at the bottom-right.
2. **C (`thumbnail_test_c.json`)**: make the pod read as whales at 168 px without making them bigger than the orcas. Put a
   pilot whale dorsal fin (broad, hooked, `pilot_whale` fin shape) behind each head. Give each head a visible white eye
   catchlight aimed at Doug. Swap the flat white foam strip under the heads for 2-3 short wake lines per head so they read as
   moving, not beached. Raise Doug's scale about 1.3x (head ≥ 18 px at 168 wide) and nudge him right about 40 px so the splash
   no longer overlaps his face. Keep the red sky, TOO SLOW and the orca sizes.
3. If B or C can't be re-rendered before the package gate, ship A alone (per the CD's 2026-11-26 note). Do not run a failing
   variant.

### Keyframes: all PASS
- **s006**: Fixed. The speaker is at the left with red arcs, four tagged whales face it with red arrows, the 5th is turned away,
  and Doug looks confused. 4 OUT OF 5 reads in one second.
- **s068**: Fixed. Doug's mitten is on the trolley handle and he is clearly pushing while the second man takes the bread.
  GROCERIES is legible.
- **s095**: Picture matches the line: a dog trails Doug and his groceries. TAGS ALONG is legible. The tally is at 3.
- **s122**: Pilot whale next to a low ACTUAL DANGER meter (red in the bulb only) reads as the setup for s123. No masking
  artefact is left on the thermometer.
- **s123**: Thermometer fixed: the red column runs unbroken into the bulb. The two meters with labels read clearly.
  *Nit (director, optional):* the red "!" at x ≈ 1360 points at nothing. Move it to just above the SPERM WHALE REACTION
  column (x ≈ 1150, y ≈ 370) or remove it.
- **s125**: Fixed. The top arrow now arcs about 120 px over Doug's cap. Doug, the dinghy, the pilot fins and the sperm whales
  below all read clearly.
- **s187**: Now the surface chase as specced: four pilot fins on the left, the orca fin escaping right with a splash, and the
  tally at 7. The THE CHASE title card repeats the chapter tab, which is fine for a section opener.
- **s201**: Orca and pilot whale side by side at plausible relative length, with 10 TONNES / 2.25 TONNES matching the narration
  (s200/s201). Doug reacts at the right and everything is legible.
- Across these shots there is no gore or kid-show tone, Doug is on-model wherever he appears, and nothing collides with the HUD.

### Next step
Keyframes stay cleared for the render. Re-render thumbnails B and C with fixes 1-2 and send them back for a feed-size re-check,
or drop them and ship A.

## Round 2

**VERDICT: PASS**

### What I reviewed
- A fresh full render: `build/contact/sheet_01..19.png` (written 00:15:56-00:16:07, after `shotlist.json` at 00:15:34), covering
  222 shots plus the endslate. I viewed all 19 sheets and zoomed to full resolution on s068, s104, s139 and s217 and on the board.
  I did not edit the shotlist or re-run keyframes.

### Round 1 blocking fixes: all 8 verified
1. **WHO RAN board.** Fixed. Every tick is now in EVERYONE ELSE from s031 on, and PILOT WHALES stays empty all episode.
   The red ORCAS stamp sits on its own line under the ticks, in the same column (s216-s219), and is legible at full res.
   The board now reads consistently.
2. **s133-s145 (orca + calf).** Fixed. s134 is small and far, s137 is the surface boat with the 21 MINUTES clock, s139 is the
   flank close-up with the slipstream, and s140 is a surface shot. There is no longer a run of 4.
3. **s124-s127 (dinghy).** Fixed. s126 is a tight Doug-in-dinghy thumbs-up shot and s127 is the white card with NO PARTY.
4. **s177-s180 (orca + pod).** Fixed. s177 is the orca face close-up with a sweat drop and ⚠, and s179 is the labelled
   GRANDMOTHERS / AUNTS / COUSINS / SONS row with a small orca in the corner.
5. **s068 (groceries).** Fixed. The trolley is loaded with bread, fish and a bottle, and the second man walks beside it eating bread.
   s095 has groceries too.
6. **s058 / s215 (black blob).** Fixed. s058 is the side-view pilot whale silhouette with a cyan rim, and it now reads as a whale.
   s215 has five non-silhouette `pilot_whale_front` heads coming in from the left.
7. **s123 thermometer.** Fixed. The red column runs unbroken into the bulb.
8. **s147 calves on the coastline.** Fixed. Both orca + calf pairs sit in open sea.

The round 1 recommendations for s088 (the diver now has a blue mask), s157 (tight POLITEST close-up), s074/s178 (strike-through
lines, labels readable) and s186 (spacing) were also applied.

### Re-checked this round
- Doug is on-model everywhere: cap, white head, orca costume, squid costume, fisherman hat and ghost. He reads on every background.
- Deaths stay clean. s031, s059, s104, s183 and s216 cut away or go to black. In s104 the red inside the splash is the cap, not blood.
- No gore and no nursery tone. All text is spelled right (SÆDÍS, PORPOISING, 24 OUT OF 34, 2.25 TONNES and so on), and nothing is
  cropped or overlapping the HUD.
- Variety: no run of 4 or more near-identical shots anywhere. The longest runs are 3: s111-s113 and s199-s201.

### Recommended (not blocking; fix if time allows before render)
1. **s006 "4 OUT OF 5"** *(director)*: still five identical tagged whales with no speaker in frame. Add the speaker at the right
   with red arcs, draw red arrows from 4 of the whales toward it, and grey out or turn away the 5th.
2. **s202 "a whole pub emptying out"** *(director)*: the four stick men still just stand beside the pub. Put 3-4 of them running out
   to the right with speed lines, and a pilot whale (or a capless family group) at the door.
3. **s064 / s067 / s075 / s081** *(illustrator or director)*: the bitten tuna head is still a small white jagged blob at scale <0.4.
   Use scale ≥0.5 in s064 and s067.
4. **s111-s121** *(director)*: the big sperm whale over the small pilot whale still appears in s111, s112, s113, s115, s118 and s120.
   Flip s115 or frame it from below.
5. **s125** *(director)*: the red "nobody notices" arrow arcs straight through Doug and the dinghy. Raise the top arc about 60 px
   so it passes over him.
6. **s068** *(director, minor)*: Doug's hand stops just short of the trolley handle. Move him about 30 px right so he is clearly pushing.

### Not a visual blocker
- `decisions.md` still asks the CD to confirm the new board logic, where every tick counts someone else backing off, Doug included.
  It reads correctly on screen; this is only a sign-off.

### Next step
Keyframes are cleared for art approval and the render. Post-render screening (samples, qc.json, thumbnails, shorts) comes later.

## Round 1 (summary)
**VERDICT: FAIL.** Eight blocking fixes: the WHO RAN board logic; the variety runs at s136-s139, s124-s127 and s177-s180; the
s068 groceries gag; the s058/s215 silhouette blobs; the broken s123 thermometer; and the s147 calves sitting on the coast. All
eight are verified fixed in round 2 above.
