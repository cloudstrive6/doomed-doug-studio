# 025-too-much-oxygen: art review, round 2

Reviewer: art-director, 2026-10-22
Scope: (a) re-check of the 4 redrawn drawings (`assets/previews/025-redraw4*.png`, plus s111, s236, s250, s251, s253 and s254 in context);
(b) all 22 contact sheets and the keyframes they come from (s002-s260 and the endslate). s001 is the thumbnail, which is in progress in
parallel, so it was not reviewed.

## Verdict: FAIL (composition only, route: director)

All 4 redrawn drawings now pass. All 27 new drawings are approved, so the illustrator has nothing blocking (fix 30 is an optional new
icon). The keyframes still have composition faults. The worst are: labels landing on the DOUG FOR SCALE meter (11 shots); a death beat with no cap
in frame (s088); a shot that pans the HUD off screen (s056); Doug standing inside trunks, ferns or the millipede (about 15 shots); and three
runs of 8 near-identical frames. All of them are shotlist edits. Re-render the listed shots and send the new contact sheets back for a quick
round 3.

Good overall: the palette ramp is consistent from item to item; the caption bar, counter and meter are consistent; Doug is on-model
everywhere, including the ghosts, `on_back` dead with X eyes, and `sit`; the death beats keep the cap in frame except s088; the
silhouette-plus-red-glow reveals work (s033, s147, s178, s199, s226); the grey-slab fossil shots read well. The round-1 composition notes
are fixed (s170: log and scorpion side by side; s141: Doug hangs against open sky and the net hoop is visible).

## (a) Redrawn drawings: all PASS

| Drawing | Verdict | Notes |
|---|---|---|
| tree_fern | PASS | Fiddleheads in the crown, long feathery fronds with separate leaflets in both greens, hanging dead brown fronds, and a trunk that widens into a shaggy root skirt. It reads as a Carboniferous tree fern, not a palm (s090, s103, s111). Anchor and height are unchanged. |
| arthropleura_head | PASS | Now front 3/4. The plates are wide, flat and receding, in the same colours as `arthropleura`. The antennae are a matching segmented pair, the eye stalks are small and spread apart with no shine, and the dark mandibles and palps are readable. The s236 arrow now lands on the mouthparts. It holds up at 0.6 in the `crt_tv` (s235). |
| fern_saddle | PASS | Pommel, dipped seat and cantle, frond leaflets along the top and hanging over the sides, a shadow lip, loop stirrups and strap ties. The eye-like curl is gone. It reads as a saddle at 0.6 (s250/s251) and at 0.5 (s253/s254). Green on the dark swamp is low contrast, but the black outline carries it. |
| leaf_hat | PASS | A leafy dome over the cap. The red brim sticks out at the front and the red crown shows through the top. Eyes are clear. Tested in stand, hands_hips, thumbs_up and gritted (s110-s117), and it reads as camouflage. |

## (b) Keyframes: required fixes (route: director, unless marked otherwise)

**Labels on the DOUG FOR SCALE meter** (art bible, "Second meter under the counter": wherever text overlaps x 1300-1860, its glyph tops
must stay at y >= 290, so a label centre needs y >= 340). Re-aim each arrow after moving its label.
1. **s093**: move "PIERCING BEAK" from (1450, 290) to (1450, 360). Aim the arrow at the beak tip (it currently ends just right of the beak).
2. **s094**: move "EXTRA FLAPS" from (1420, 280) to (1420, 360).
3. **s157, s158**: move "SMALL PINCERS" from (1500, 300) to (1500, 360).
4. **s161**: move "BOOK LUNGS" from (1450, 300) to (1450, 360).
5. **s162**: "AIR" at (1550, 260) is half hidden behind the meter label. Move it to (1500, 380) and start the blue arrow from there.
6. **s164**: move "BOOK LUNGS" from (1350, 300) to (1350, 360). Move "GILLS" to (550, 360) as well, so the pair stays level.
7. **s177**: move "2005" from (1350, 280) to (1350, 350), above the journal page.
8. **s211**: "HUGE TEETH" at (1450, 250) is covered by the meter label. Move it to (1450, 360).
9. **s213**: "LARGE EYES" at (1400, 270) is covered by the meter label. Move it to (1400, 360) and aim the arrow into the big eye socket.
10. **s236**: move "CENTIPEDE-LIKE" from (1450, 290) to (1450, 360). Keep the arrow on the mandibles.
11. **s225**: the "LARGEST LAND BUG" wordart (960, 300) runs into the tape icon at its right end. Move it to y 400.
12. **s174**: the two-line red title puts "THAT" against the meter label. Set size 80 so it fits on one line (max_width 1500) at y 360, and move
    "330 MILLION YEARS AGO" to y 470.
13. **s125, s126**: the flashback frame rects (top y 220) run under the meter label. Move both rects to y 300 (h 560 is still fine). In s126,
    move `meganeura` from y 330 to y 430 so its wings sit inside the frame and clear the meter.
14. **s192**: the pink silicone-copy rect (1300, 250) touches the meter label. Move it to (1300, 330). Optionally lay a few print marks on it so it reads
    as a cast of the trackway rather than a blank swatch.
15. **s061** (`bojophlebia` at 1450, 300) and **s140** (`meganeura` at 1250, 330): a wing tip lies on the tape icon. Lower each to y 400.

**Death beats and the HUD**
16. **s088** (death 206): the cap is hidden. `doug_cap` is drawn before the opaque `water_glass_empty`, so the frame has no cap and does not read
    as a death. List `doug_cap` *after* the glass (same x/y) so it reads as trapped inside it. Every death beat must show the cap (art bible,
    "Death images without a body").
17. **s056** (`pan_down`): the shot ends on plain brown. The counter, the meter, Doug and "SUMATRA, TODAY" have all scrolled off, and it is the only frame in the
    episode without the HUD. Repeat `DOUG DEATHS: 204` at (1590, 1242), the tape icon at (1372, 1318) and "40 CM" at (1600, 1318) so the HUD
    is on screen at the end of the pan. Also stop the white dashed line at y 100 so it does not cut through the caption bar.
18. **s253, s254**: `fern_saddle` (760, 870) sits on the middle `scale_tree` trunk, and its stirrups dip below the ground line. Move it to
    **(600, 840)** in both shots so the saddle stays where it fell. The scale-0.5 bbox bottom then lands on the ground at about y 885, clear of the trunk.

**Doug inside props** (art bible: keep Doug at least 40 px off trunk edges and off busy bushes)
19. **s198, s215, s217**: Doug (1700) is standing inside the `fern` (1700). Move him to x 1500.
20. **s216**: Doug (200) is on the left trunk (150). Move him to x 300.
21. **Millipede swamp set** (s228, s231, s234, s237, s238, s247, s248, s249): Doug (x 200-250) overlaps the left `scale_tree` (120), and in s228
    and s231 he is also half hidden by Arthropleura's tail. Move that left `scale_tree` to x 40 in every shot of the set (s222-s254), so the set
    stays consistent. Then check that the tail clears Doug by at least 40 px, and nudge `arthropleura` +60 x where it does not (s228, s231 at scale 1.9).
22. **s251**: Doug is drawn over Arthropleura's head and antennae, so his lines merge with them. Move `arthropleura` from x 1000 to x 1080.
    In **s250**, the saddle (540, 760) lies over the antenna. Move `fern_saddle` to (520, 700), held up against the open sky.
23. **s048**: the "PEAT SWAMP" label (700, 620) covers Doug's head and cap. Move it to (900, 520).
24. **s030**: the ghost Doug (760, 520) is inside the middle tree crown. Move him to (1000, 430), into open sky. Do the same on a smaller scale in
    **s172**: move the ghost from x 1000 to x 850.
25. **s185**: tiny Doug sits on the busy footprint band at the right edge. Put him on the plain sand above the trackway.

**Readability and gags**
26. **s090**: `mazothairos` (1250, 520) covers the end of "309 MILLION YEARS AGO". Move it clear, for example to (1550, 700) on the right tree-fern
    crown.
27. **s249**: the car is wedged under Arthropleura's legs, so the "size of a car" comparison doesn't read. Put the two side by side on the same ground
    line with a gap, for example `arthropleura` at (760, 800) and `small_car` at (1640, 890).
28. **s231**: the `paper_crown` sits on the ground by the fern (1700, 1060). Put it on Arthropleura's head (about (1800, 690); check against the
    head outline) so the "biggest bug" gag lands.
29. **s259**: "BUGS THAT NOTICED HIM: ALMOST NONE" (960, 480) runs over the booth roof and sign. Move it to (960, 300). Move `meganeura` from
    (1450, 330) to (1500, 520) so it clears the label.
30. **s043**: the "MAYFLIES" icon is `insect`, which is a brown beetle, so the family tree shows a beetle as a mayfly. Either ask the illustrator for
    a small `mayfly` icon (slim body, upright wings, 2-3 long tail filaments; optional new asset), or drop both icons and keep the labels only.
31. **s065**: the Megarachne reveal is a plain black silhouette. Style bible 7.7 calls for the red glow, as in s033, s147, s178 and s226. Add the same red
    `spray` glow behind it.
32. **s255-s257**: the 2026 outro still shows the "THE MILLIPEDE" caption bar, but s258-s260 don't. Set `topbar: false` on s255-s257.
33. **s044**: "LONELY BRANCH" (1300, 800) starts on the main trunk line. Move it to x 1450.
34. **s124**: the "SPINY LEGS" arrow ends on the prey insect. Aim it at Meganeura's legs.
35. **s103**: the two right tree ferns (trunks merged into one blob). Spread them at least 150 px apart.
36. **s002**: the third "O2" (760, 470) is hidden in the middle tree crown. Move it to (1000, 520).

**Same composition repeated** (keyframe rule: not the same composition 5+ times in a row). Each of these runs is 8 locked-off frames of one set.
Break each one up with 2 framed close-ups, using a custom camera so the keyframe shows the framing (`{"from": [cx, cy, z], "to": [cx, cy, z+0.05]}`).
37. **s024-s031** (cupcake): s025 a 2-shot of Doug and the cupcake (zoom about 1.7 on them); s029 a tight shot on the surviving cupcake (zoom about 2.0).
38. **s110-s117** (leaf hat): s113 a tight shot on Doug's head and the hovering Mazothairos (zoom about 1.8); s116 or s117 a wide shot with the narrator
    hand only, or a close-up on the "insulted" hat.
39. **s247-s254** (millipede): s250 a 2-shot of Doug, the saddle and the head (zoom about 1.5); s253 a low close-up on dead Doug and the crushed saddle (zoom about 1.6).

## Not blocking

- The tape icon at 0.16 is a small yellow smudge at phone size. It is consistent with earlier meters, so leave it, but 0.2 would read better next time.
- s152 shows `hynerpeton` in full colour on the fossil slab. A grey wash would match the other fossil shots.
- s199 and s205: the water cross-section leaves Doug and the "NOT A BUG" wordart squeezed into a 100 px sky strip at HUD height. Dropping the waterline
  to about y 420 would give them room.
