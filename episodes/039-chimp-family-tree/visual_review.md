# Visual review: 039-chimp-family-tree

## Round 1: pre-render keyframes (2026-11-08)

Inputs: `shotlist.json` (208 shots + endslate), `build/contact/sheet_01..18.png` (rendered 20:29, newer than the shotlist), with
full-resolution crops of `build/keyframes/` for s005, s018, s029, s031, s035, s064, s067, s077, s094, s099, s111, s116, s122,
s182, s194 and s196.

VERDICT: FAIL

Most of the episode is clean. Doug is on-model in all 208 shots (red cap, white head), including the bushbaby, colobus, gorilla
and chimp costumes. The HUD counter runs from 301 to 308 with exactly 7 deaths (s024, s072, s095, s135, s154, s177, s203).
Every death is a cap in the dark, with no gore, no blood and nothing realistic. The tone does not read as a kids' show. The
fails below are places where the picture contradicts the narration, labels are cut by drawings, and two runs of shots repeat
the same composition.

### Blocking fixes

1. **s064 (director): the picture contradicts the line.** "THE SMALLEST" sits on the *largest* gorilla silhouette, and both
   gorillas are adult-sized. Add a clearly smaller gorilla (e.g. `silverback_gorilla` at about 0.4, or a juvenile) and move the
   label onto it with a red arrow. Apply the same change to s062, so that the "?" points at the small one.
2. **s077, s078, s079 (director): the tree branches cut through the labels.** The branch lines run through "GORIL|LA",
   "CHI|MP" and "H|UMAN". End each branch about 20 px below its icon and put the label *above* the icon, or shift the labels
   below the branch tips so no line crosses the text.
3. **s196, s197, s198, s204 (director): the trunk cuts through "SAME GROUP".** The red label is centred on the trunk, so the
   trunk splits "SAME" from "GROUP" and runs through the "G". Move it to the left of the trunk's top branch (next to the chimp
   it describes), or give it a white box like the s204 version and put it clear of the trunk. In s204 the boxed version still
   overlaps the trunk.
4. **s099 (director): the text covers drawings and there is no river.** "ACROSS A RIVER" runs over the bushbaby and the base
   of the trunk. Move it to the empty right half (about x 1300, y 750), and draw a blue river band across the ground strip, or
   it is just a phrase.
5. **s005 (director): the title card collides with the tree.** "DISTANT RELATIVES." runs straight across the hollow tree's
   crown on the left. Move the text right/down into open sky (centred about x 1100) or move the tree out of the text band.
6. **s031 (director): the text covers Doug.** "25-30 MILLION YEARS" is drawn over Doug (x≈1500). Move Doug to about x 1750 or
   lift the label to about y 700.
7. **s067 (illustrator, director): the forest elephant reads as smaller than the gorilla.** It is tucked under the gorilla's
   belly, so a viewer reads it as a dog or calf. Scale the elephant up to at least gorilla shoulder height × 1.5 and give it its
   own space to the right of the gorilla.
8. **s194, s195 (director): the KAHAMA group is unreadable.** The KAHAMA chimps render as dark green discs (they do not read as
   chimps), and the KASAKELA `chimp_head_icon`s at 0.32 are near-invisible brown on navy. Raise the icons to about 0.6 with a
   light rim (as on the s069 ridge line). In s195, show the Kahama members fading or crossed out one by one to match "killed or
   vanished one by one". Align the KASAKELA and KAHAMA labels at the same y, and move "THE FOUR-YEAR WAR" up so it does not
   touch the KASAKELA label.
9. **s167 to s172 (director): variety, 6 chalkboard shots in a row** with the same board in the same position and Doug at
   right. Break the run: make s170 ("nobody had ever recorded an exile this long") a 5-year exile timeline (re-use the s163
   calendars with "LONGEST EVER" on them) in place of a repeat of the s168 board, which also fixes a mismatch: the board text is
   about between-group killings, not exile. Make s172 ("competition for mates is fierce") a scene shot of two males facing off.
10. **s042 to s045 (director): variety, 4 near-identical branch shots.** Push in on Doug and the three colobus males for s045
    ("Doug is fine.", Doug centred at about 2x), or reframe s044 low from the chimp's side so the run does not hold one wide
    shot for four lines.

### Non-blocking fixes (do them in the same pass if cheap)

11. **s029, s051, s085, s086, s103 (director):** the map's top-right corner tucks under the HUD family-tree card. Shrink the map
    by about 8% or shift it down/left so its frame clears the card by at least 20 px.
12. **s046 (director):** a lone `doug_cap` on the empty branch reads as Doug dying, one line after "Doug is fine.", and no death
    is counted. Replace it with the empty branch plus the shrinking graph only, or show Doug still sitting there alone.
13. **s054 (director):** the white tally marks and "2014-2018" sit on the fruit canopy, and the marks are half-lost among the
    fruit. Move the 9 tally marks into open sky to the right of the tree.
14. **s157 (director):** "THE OLD KING" ends against the green tree's crown. Move the tree to about x 560 or nudge the title
    left.
15. **s100, s101, s112 (illustrator, art director):** at contact-sheet size the `bonobo` reads as a chimp. The chapter is about
    them being different. Either add a small "BONOBO" label in s100 and s101, or strengthen the bonobo's distinguishing marks
    (pink lips, middle-parted hair, longer legs) so it reads at 0.6.
16. **s182, s183 (director):** the 200 `chimp_head_icon`s are dark brown on navy and read as noise. Use the light dots from s184
    or give the icons a pale rim.
17. **s009 (director):** "YOUR ARM" floats far from Doug, and his arm is much shorter than the 75 cm ruler. Put Doug's extended
    arm along the ruler and move the label beside it.
18. **s174 (illustrator):** the paper crown in Doug's hand is about 15 px and invisible. Scale it to about 2x so the setup for
    s175 and s176 reads.
19. **s012 (director):** the "?" touches the "B" of "BUSHBABY BED". Shift it up/left about 30 px.

### Carry-over (not a keyframe fail)
- **s001 (graphic designer):** the shot shows "(thumbnail pending)". The thumbnail must exist before the render, because s001
  is the video's opening image. It will be checked in the post-render round along with `thumbnail_b`/`_c` and the `_small`
  versions.

### Checked and fine
- Gore and violence: the deaths (s024, s072, s095, s135, s154, s177, s203) are cap-in-silhouette, and the attackers are
  red-rimmed silhouettes. The baby-mortality (s146) and "17 of the smallest" (s190) cards are text only. Nothing graphic.
- Kid appeal: none. "hi friend?", "cousin?" and the field guide gag are adult-coded deadpan, and the s187 playground is
  abstract dots.
- Costumes: the bushbaby (s022, s023), colobus (s042 to s045), gorilla suit (s068 to s071, s089, s090), empty suit (s091) and
  chimp costume (s111 onward) are all on-model, and the cap and white face read on every background, including the dark
  patrol and night scenes.
- Endslate: the layout is correct, and the placeholders fill at render.

## Round 2: keyframe recheck and thumbnails (2026-11-08)

Inputs: `shotlist.json` (208 shots, commit 5bc987e), `build/keyframes/*.png` (re-rendered 20:42), full-resolution views of every
shot named in round 1 (s001, s005, s009, s012, s029, s031, s042 to s046, s051, s054, s062, s064, s067, s077 to s079, s085, s086,
s099 to s101, s103, s112, s157, s167 to s172, s174, s182, s183, s194 to s198, s204), and `build/thumbnail{,_b,_c}.png` plus
the 168x94 `_small` versions. `metadata.json` title: "Every Reason Chimpanzees Kill Their Own Relatives, Including Doug".

### Part (a): keyframe recheck. VERDICT: PASS

All 10 blocking fixes are done:
1. s062, s064: a clearly smaller gorilla now stands third in line. The "?" (s062) and the "THE SMALLEST" arrow (s064) point at it. Fixed.
2. s077 to s079: the labels sit above the branch tips and no line crosses the text. Fixed.
3. s196 to s198, s204: "SAME GROUP" sits right of the trunk, clear of it (on s204 the gap to the trunk is only about 13 px at 1920; it does not touch, but 30 px would be safer). Fixed.
4. s099: "ACROSS A RIVER" is in the open right half, and a blue river band runs along the bottom. Fixed.
5. s005: "DISTANT RELATIVES." is in open sky, clear of the tree. Fixed.
6. s031: Doug has moved to the far right, clear of "25-30 MILLION YEARS". Fixed.
7. s067: the elephant is now the largest silhouette and stands on its own to the right of the gorilla. Fixed.
8. s194, s195: the icons have pale rims, the Kahama members are crossed out, the KASAKELA and KAHAMA labels share one y, and
   "THE FOUR-YEAR WAR" sits clear of them on the ground strip. Fixed.
9. s170 is now a 5-calendar "THIS LONG" timeline, and s172 is a night scene with a male line-up ("FIERCE"). The chalkboard run
   is broken. Fixed.
10. s045 is a push-in on Doug and the three colobus males. Fixed.

Non-blocking: 11 (maps clear the HUD card), 12 (s046 shows Doug on the branch with no lone cap), 13 (s054 tallies are in the
sky), 14 (s157 title is clear of the tree), 15 (BONOBO labels in s100 and s101; s112 is the intentional name tag), 16 (s182 and
s183 icons are rimmed), 18 (s174 crown is readable) and 19 (s012 "?" is clear) are all done. The s001 carry-over is resolved:
it now shows thumbnail A.

Still open, not blocking:
- **s009 (director):** round-1 item 17 is only half done. "YOUR ARM" is beside Doug now, but his arm is still a short stub
  under the 75 cm ruler, so the comparison does not read. Extend Doug's arm horizontally under the ruler (pose with the arm
  out, about x 650 to 1250) so the arm and the spear line up.
- **s077 (director):** the red "!" floats alone in empty space at about x 1450, y 760. Drop it, or put it next to the
  CHIMP/HUMAN fork.

### Part (b): thumbnails. VERDICT: FAIL (A needs one fix, B passes, C fails as built)

**Thumbnail A (`thumbnail.png`, "HE'S FAMILY"; also s001):** the text is huge and readable at 168x94, and there is one focal
point (the chimp backlit by the sun) with the threat obvious. Doug is small but the red cap reads. The image complements the
title without repeating any of its words. There is no gore and nothing misleading. One blocking defect:
1. **(graphic designer / illustrator) The spear floats.** The stick stands in front of the chimp's chest with no hand on it
   (at 1280x720 it runs from about x 555, y 255 down to x 640, y 720, and the chimp's near arm goes down past it and off frame
   without gripping it). The brief says "holding a stick", and a free-standing spear reads as a drawing error on the video's
   opening image. Fix: give the chimp a closed hand around the shaft at about y 470 to 520, with the arm bent to reach it (as
   in B's left chimp), or tuck the shaft into the existing hand and crop it so the grip shows. Optional while in there: scale
   Doug about 1.25x (he is about 25 px tall in the small version) and keep him at the left third.

**Thumbnail B (`thumbnail_b.png`, "NEXT"): PASS.** It is the strongest of the three at feed size. Doug is centred and the
largest he appears in any variant, the costume and cap read, three chimps hem him in, and the spear points at him. "NEXT"
plus "...Including Doug" pays off in s204 ("it just tells you who's next"), so it is not misleading. The threat is cartoon,
not violence. Minor, non-blocking: the crouching chimp's rump merges with the big male's hand at about x 940 to 1000. Move the
crouching chimp about 40 px left.

**Thumbnail C (`thumbnail_c.png`, 4-tile grid): FAIL.**
2. **(graphic designer / illustrator) The bonobo tile is a black blob at 168x94.** The crouched bonobo on magenta loses its
   face and reads as a gorilla or a shadow. Use the standing or side-on bonobo with the face lit (pink lips, parted hair)
   at a bigger scale, or swap to a lighter tile colour behind it.
3. **(graphic designer) No threat anywhere, so it does not sell the title.** Three of the tiles are calm animals, and in "THE
   SPLIT" Doug and the chimp just stand side by side. Make "THE SPLIT" carry the threat (chimp with hair on end facing Doug,
   spear raised) and enlarge both figures to fill the tile height.
4. **(graphic designer, style) The grid is off-grammar** for the style bible's Archetype A: 4 tiles where the rule is 6 to 12,
   coloured tile fills where the background should be white, and labels above rather than under the tiles. Going to 6 tiles
   (add "THE HUMAN" and "THE OLD KING", the chapter names) would also make it feel like the "Every Reason" list the title
   promises. If there is no time for 2 to 4, drop C from the test and run A against B.

Policy, all three: no gore, no blood, no realistic violence, no kids-show framing, and no title words repeated on the image.
None promise anything the video does not deliver.
