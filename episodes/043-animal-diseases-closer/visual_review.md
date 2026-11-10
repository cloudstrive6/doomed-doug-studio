# 043 Visual review

## Round 1: keyframes + thumbnails (2026-11-10)

I checked all 15 contact sheets (s001 to s178 plus the endslate) and the three thumbnails at full size and at 168x94.

**VERDICT: FAIL**

Safe for policy: no gore, every death is a cartoon (x-eyes, ghost, cap left behind), carriers are never shown sick or
monstrous, and nothing looks like a kids' show. Doug is on-model in almost every shot. Text is spelled correctly. The
HUD (chapter tag, DOUG DEATHS, HOW CLOSE) is consistent, and the counter runs 329 to 336 as the series bible says.
Counted displays are correct: s048 has 21/50 greyed, s053 has 50/72 seats, s086 has about 48/100, s092 has 9 pins,
and s093 has 8 Dougs. The fixes below are the blocking ones, followed by a short list of advisories.

### Blocking fixes

1. **s098 (director)**: the narration is "The cow is not safer." but the death frame has the cap on a **straw nest of
   eggs** and no cow. Replace `straw_nest_eggs` with the milking-stall set from s097 (fence + `holstein_cow`), with the
   cap left by the milk pail or under the cow. Doug's body and ghost stay as they are.
2. **s171 (director)**: the narration is "Doug has died." but the frame shows Doug **alive** on the couch at WEEK 4, and
   the counter still reads 335. Show the death on the line that announces it. Either move the WEEK 1-4 calendar flip to
   s170's tail and give s171 the death frame with the counter ticking to 336, or swap the two pictures so s171 is the
   death and s172 ("Again.") is the dark couch with the ghost.
3. **s022, s023, s024 (illustrator + director)**: the "torch" floats beside Doug's hand, points up, has no beam, and
   reads as a **microphone**. Put it in Doug's hand (as in the thumbnail) and add the pale-yellow beam cone pointing at
   the ceiling colony. On s023 ("forty thousand bats moved at once"), the colony is identical to s022 and nothing moves.
   Add movement on s023: a scatter of 15-20 flying-bat sprites and motion ticks under the colony. Right now s022 and
   s023 are the same picture.
4. **s080, s081, s082 (art director)**: the `sunburn` gear turns Doug's whole head red. Under "Doug is fine" and "no
   symptoms or only mild ones" this reads as a **fevered, sick face**, which breaks the 043 disease rule (no symptom
   imagery). With the cap off it also makes Doug hard to recognise (no red cap, no white head). Remove `sunburn` and keep
   the white head. There is also a cap continuity break: s080 and s082 have the cap on the ground (`cap_off`), but in
   s081 Doug wears it. Make s081 `cap_off` too, or put the cap back on in all three.
5. **s069 and s068 (illustrator)**: the dust that carries the bacterium "a long way" is drawn as almost transparent pale
   circles on a pale-blue sky, so the key subject is invisible. Make the dust plume visible: tan/khaki stipple at
   about 60% opacity, a clear trail from the barn door to the house, and the green bacteria specks from s064 inside it.
   s079 has the same problem behind Doug and needs the same fix.
6. **s130 (illustrator)**: the South America map only shows the northern half of the continent. The ANDES VIRUS pin
   sits around Peru/Bolivia, and the "!" hangs outside the map frame. Andes virus is the southern cone (Argentina/Chile).
   Show the whole continent, put the pin in southern Argentina/Chile, and keep the "!" inside the frame.
7. **s055 to s060 (director)**: there are **six near-identical temple wide shots in a row** (the same stairs, wall,
   monkey on the left, Doug centre-right), and s051 and s054 use the same plate. Vary them:
   - s056: tighter shot of Doug holding up the selfie stick with the monkey looking into the phone.
   - s057 ("and he was bitten"): close two-shot with the monkey at Doug's raised hand. Use the `bandage` survival gear,
     never red and never a wound. Right now no bite is shown at all.
   - s058-s059: keep the narrator's hand and chart, but go in close on the chart.
8. **s102 (director)**: the frame has a "UK, 1989" calendar under "proteins ... fold into the wrong shape". The date
   belongs to s105 and doesn't match the line. Remove the calendar. The diner booth plus the PRION label carry the shot.
9. **s018 (illustrator)**: "UPSIDE DOWN" sits over a stadium drawn the right way up, and there is a stray stipple
   blotch under the stadium entrance. Flip the stadium 180 degrees (or hang bats from its rim) and delete the stipple.
10. **Thumbnail C, `thumbnail_c.png` (graphic designer)**: the bat tile is dark brown on dark green, and at 168x94 it
    reads as an **empty black square**. That loses the first noun of the title ("a Bat, a Cat or a Dog"). Lighten the
    tile background (mid-green or the purple of thumbnail A) and scale the bat to about 85% of the tile height.

### Advisories (fix if cheap)

- s006 (director): the "GERMANY" text overlaps the top-right corner of the Europe map. Move it down and left, below the
  HUD.
- s013 (director): the end of "UGANDA" runs into Doug's head. Shift the text left about 60 px or move Doug right.
- s003 (director): the red "?" sits on the sleeping dog's back. Lift it about 80 px so the dog reads cleanly.
- s054 (director): "ALMOST NEVER" overlaps the temple roof. Raise it about 50 px.
- s127 (illustrator): the large brown wedge on the left is unreadable (door? beam of light?), and the droplets are faint.
  Either label it or remove it, and darken the airborne droplets.
- s145 (illustrator): the grey droplet puffs are faint on cream. Use the darker virus-blob grey.
- s138 (illustrator): GROUND SQUIRREL and PRAIRIE DOG are the same sprite. If cheap, make the prairie dog stockier and
  tan with a short tail.
- s042 (director): the cap-wearing monkey silhouette appears next to a Doug who also still wears his cap, so there are
  two caps. Use `cap_off` on Doug, or have the monkey hold the cap rather than wear it.

### Thumbnails

- **A (`thumbnail.png`, "UP TO 88%")**: PASS. It has one focal point, "UP TO 88%" is readable at 168 px, and Doug is
  obvious with his cap and torch beam. The bat reads as a large upside-down bat at full size. At feed size it is closer
  to a "brown pod with a face", but the number and the title ("Bats, Cats and Dogs") carry it. Optional for the graphic
  designer: open a sliver of wing membrane or show one ear tip so the bat silhouette is clearer at 168 px.
- **B (`thumbnail_b.png`, "ON THE COUCH")**: PASS. It is clear and adult in tone: a plain dog asleep, a warning
  triangle, and gritted-teeth Doug. It pairs well with the rabies title and isn't misleading. Minor: the dog's stacked
  front paws read as a flat tan board under its chin. If the illustrator touches `brown_dog_sleeping`, separate the two
  paws with a line.
- **C (`thumbnail_c.png`, "HOW CLOSE?")**: FAIL on the bat tile (fix 10). Otherwise it reads well: the escalating tile
  sizes, the arrow, and Doug at the red dog tile.

Next round: after the fixes, re-run `python -m studio keyframes 043-animal-diseases-closer --shots
s018,s022,s023,s024,s055,s056,s057,s058,s059,s068,s069,s079,s080,s081,s082,s098,s102,s130,s171,s172` and
`python -m studio thumbnail 043-animal-diseases-closer`, and send the screener the new sheets and thumbnail C.
