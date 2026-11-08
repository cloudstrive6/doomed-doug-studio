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
