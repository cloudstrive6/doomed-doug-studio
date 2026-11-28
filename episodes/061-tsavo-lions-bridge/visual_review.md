# 061-tsavo-lions-bridge: Visual review

## Round 1: pre-render keyframes (2026-11-28)

Screened: shotlist.json (174 shots + endslate), contact sheets sheet_01 to sheet_15. Spot-checked full-size keyframes:
s003, s027, s034, s040, s046, s056, s069, s082, s091, s098, s109, s116, s129, s152, s153, s160, s163.
For s109 and s163 I also rendered the mid-shot state (t=0.3), because the keyframes only show the end state.

**VERDICT: FAIL**

### What works
- Real victims are handled with care. s015 (black card, "ABOUT 35 REAL PEOPLE", a tally line) is respectful.
  Ungan Singh's attack (s025-s027) shows only a lion head silhouette in a tent doorway. No victim is ever drawn
  being eaten or hurt. Every joke lands on Doug, never on the workers. s034/s035 (the mattress) is the one played
  for laughs, and that man survived. The workers are anonymous generic stick figures with no caricature.
- No gore anywhere. Doug's deaths are off-screen (cap on a pole, dropped lantern, dental mirror on the ground).
  The lions are hit "again and again" in s154/s155 with no blood. The museum and rug epilogue (s164-s171) is clean.
- Nothing kid-coded. The tone is dry and adult throughout.
- Doug is on-model everywhere he appears: red cap, white head, consistent rig. The dentist coat (s090/s091) and the
  scarf (s068) read well.
- Text is legible and spelled correctly. The HUD never collides with art. Chapter cards are strong.

### Required fixes

1. **s109: Doug is missing from his own death, and half the shot is a blank black frame.** At mid-shot a lion paw
   grabs the "DAYS WITHOUT AN INCIDENT" sign, but Doug (who was standing by that sign with his shovel in s108) is not
   in the scene. Then the full-frame blackout at appear 0.5 leaves a completely empty black screen for the second
   half (`keyframes/s109.png`). **Director:** put Doug (`pose: stand`, shovel, `expression: scared`) at x≈260 in
   front of the sign so the paw reaches *him*. Leave the death residue visible after the blackout, the way
   s039/s072/s092 do: `doug_cap` on the ground at x≈260, y≈900 drawn above the blackout rect, plus the sign reading 0.
2. **s163: the death reads as "a sign fell over".** Doug was up the tree in s159-s162. In s163 the sign falls, "THUD"
   appears, and the eyes stay, but there is no Doug, no cap and no tree. **Director:** keep the `thin_thorn_tree`
   silhouette (dimmed), and drop `doug_cap` on the ground next to "THUD" at x≈700, y≈950 after appear 0.42, so the
   viewer understands Doug fell out of the tree.
3. **s098: the picture contradicts the narration.** The narration says they "threw themselves onto the rails *in front
   of the engine*", but the workers stand behind the wagon at left while the engine faces right. **Director:** move
   the worker row onto the track to the RIGHT of the locomotive (x≈1750-1900), or flip the train so the engine faces
   the workers. Add a short red "STOP" arrow from the workers to the engine.
4. **s143 and s157: the lions' deaths are never shown, so the chapter payoffs land on empty frames.** s143 ("He shot it
   later that night") shows the unchanged platform. s157 ("finally dropped barely five yards from him") shows
   Patterson and a dashed line with no lion. **Director/illustrator:** in s143 add a "BANG" burst (same style as
   s123) and the `tsavo_lion` lying on its side under the platform (cartoon only, no blood). In s157 put the lying
   lion at the far end of the "5 YARDS" dashed line at x≈620, y≈960. Use a closed-eye or plain "lying" pose. No X-eyes
   or wounds, since these are real animals and the chapter is serious.
5. **s152: the charging lion is invisible.** A black silhouette behind dense grass stalks on a near-black night reads
   as a dark smear, not a charge. **Director:** use the tan `tsavo_lion` running pose from s154, drawn IN FRONT of the
   grass layer and larger (scale ≥1.0), with motion lines.
6. **s003 (cold open, second shot on screen): the lion under the tree reads as a gorilla.** The sitting-lion
   silhouette is a black hump. Doug is also small (about 60 px head). This is the hook frame. **Director:** use the
   tan standing/prowling `tsavo_lion` side-on (ears, tail tuft visible) under the tree, or a silhouette with a gray rim
   like s089. Scale Doug up about 1.5x.
7. **s091: both speech-bubble tails point at the tents, not at the speakers.** **Director:** aim the "open wide" tail at
   Doug's head (≈1150, 740). Either drop "hi friend?" (no speaker is obvious) or give it to Doug as a first beat
   and remove it on "open wide".
8. **s055, s056, s057, s069, s070, s071: Doug's black stick body disappears into the brown thorn fence.** Only his head
   floats (`keyframes/s056.png`, `s069.png`). **Director:** in s069-s071 stand Doug in the gate gap between the two
   posts (x≈900-1100) on the dark ground, not against the boma. In s055/s056 either put Doug in front of the fence with
   his feet on the ground strip below it, or **art director:** give the rig an automatic light rim (the `rim`
   option already used on silhouettes) whenever it is drawn over a busy mid-tone.
9. **`stick_man_arms_up` asset (s046, s082, s097, s147, s148, s153): the arms sprout from the top of the head and look
   like antennae.** **Illustrator:** re-attach the arms at the shoulders (neck joint) and raise them from there.
   **s082 specifically:** the narration is "sick and dying porters were sometimes left behind", and arms-up (cheering)
   figures are tonally wrong for that. **Director:** swap them to `stick_man_sitting`, slumped, or remove the figures
   and keep only the grey caravan route.
10. **s046, s047, s153: the tree crown runs behind the chapter label and off the top of the frame.** **Director:** lower
    the tree (y +120) or scale it to 0.85 so the canopy clears the topbar. In s153 the two climbers are tiny
    (scale 0.18) with no visible bodies: raise them to 0.28 and use `stick_man_plain` gripping branches.
11. **s116: "two soldiers with rifles", but there are no rifles.** **Illustrator/director:** give both seated men a rifle
    prop (simple brown/grey line across the lap, angled toward the lion room). Keep the rifles through s117, s119,
    s121, s122, s124, s127.
12. **s114: the "3 IN (7.5 CM)" gap marker is invisible.** It is a few red dashes about 40 px wide inside the cage.
    **Director:** add a circular zoom inset (like s085/s088) showing two iron rails with a red double-arrow labelled
    3 IN, or bring the camera in (push to the centre divider).
13. **Sitting-lion pose (s091, s093, s160, s161, s162) is borderline recognisable at feed size.** It reads as a bear or
    seal, with the head tipped back and no visible ears or tail tuft. **Illustrator:** for the `tsavo_lion` sitting
    variant, add rounded ears, a clearer muzzle and chin, a visible tail with a dark tuft curled at the front paws,
    and longer front legs. In s160-s162 turn the head toward Doug rather than straight up.
14. **Variety: near-identical runs of 4 or more.** **Director:** break each with a camera move, scale change or
    insert:
    - **s112-s117** (6 shots, the same full-width trap at the same framing): s113 push in on the two rooms;
      s114 inset (fix 12); s115 low angle on the men's side; s117 close-up on the door.
    - **s119-s122 and s124-s128** (same framing again): s121 close-up of the two frightened faces; s124 close-up
      of the door bar; s127 tight on Doug and the lion with the divider between.
    - **s139-s143** (5 identical platform wides): s141 top-down circle is already different, so keep it; make s142
      a close-up of Patterson and Doug on the platform edge; s143 per fix 4.
    - **s159-s162** (tree and sitting lion, only the text changes): s161 close-up on the lion looking up; s162 slow
      zoom on Doug's face.
    - **s010-s013** (tan lions on cream; s011 and s012 are the same frame plus a label): merge s011/s012 into one
      shot with "ABOUT 35" appearing, or change s012 to a big tally/sum graphic.
15. **s001: "(thumbnail pending)".** This is not a fault of the keyframes, but the cold-open frame cannot be screened
    until it exists. **Graphic designer:** deliver the thumbnail. I will screen s001 with the thumbnails in the
    post-render round.

### Minor (fix if cheap, not blocking)
- s109 (mid-shot): the locomotive's front buffer beam is cut off at x=1920. Shift the train left by 40 px.
- s164 "FLOOR RUGS": the plain oval rug does not say "lion". A flat lion-shaped rug outline (head and four paws,
  plain tan, no face detail) would land the fact without being grim.
- s166/s170/s171: the two mounted lions overlap into one blob in the case. Separate them by about 60 px.
- s040/s128/s161: the "TSAVO LIONS / FRIEND?" notebook text is about 18 px tall and illegible at 1080p. Only the
  big NO/MAYBE stamps read, which is acceptable.

Re-screen after fixes: s003, s046, s047, s055-s057, s069-s071, s082, s091, s098, s109, s112-s128, s139-s143,
s152, s153, s157, s159-s163, plus the s001 thumbnail.
