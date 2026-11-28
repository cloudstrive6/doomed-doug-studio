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

## Round 2: pre-render keyframes re-screen (2026-11-28)

Screened: regenerated contact sheets sheet_01 to sheet_15 (all 174 shots + endslate). Full-size checks: s116, s117,
s121, s124, s127, s161, s162, s163, s113, s055-s057, s046, s082, s147. I rendered mid-shot states (t=0.2-0.9) for
s003, s109, s153 and s163 because their keyframes show only the end state.

**VERDICT: FAIL** (3 required fixes, all small. Everything else from Round 1 is resolved.)

### Round 1 items: status
1. s109: **fixed.** At t=0.3 the paw grabs Doug (stand, shovel, gritted) at the sign. After the blackout the cap is
   on the ground, the sign reads 0, and the ghost floats up. The locomotive now fits inside the frame.
2. s163: **fixed.** Doug lies dead (X-eyes) at the base of the silhouetted tree with his cap beside him, plus THUD and
   the eyes. It reads clearly as "fell out of the tree", with no gore.
3. s098: **fixed.** The worker row is on the rails right of the engine, with a STOP arrow and a HUNDREDS label.
4. s143 and s157: **fixed.** Both have a lying tan lion, closed eyes and no wounds. In s143 the BANG plus the lying
   lion lands the payoff. In s157 the lion sits at the end of the 5 YARDS line.
5. s152: **fixed.** A large tan charging lion with motion lines, in front of the grass. It reads instantly.
6. s003: **fixed.** A tan prowling lion side-on, with ears and tail tuft. Doug at the top of the tree is readable.
7. s091: **fixed.** The "open wide" tail points at Doug and "hi friend?" has been removed.
8. s055-s057 and s069-s071: **fixed.** Doug's body and legs read against the ground strip and in the gate gap.
9. `stick_man_arms_up`: **fixed.** The arms now attach at the shoulders (s046, s147, s148, s153). s082 uses small
   figures on the caravan route, and the tone is fine.
10. s046, s047, s153: **fixed.** The canopy clears the topbar. The s153 climbers are readable, with Patterson's hat
    showing.
11. Rifles: **fixed, and policy compliant.** `rifle_held` rests across each soldier's lap in every trap shot (s116,
    s117, s119-s122, s124-s128). The stock is low-left and the muzzle points up-right, toward the men's-room wall or
    roof. **The rifle never points at the lion, which is always on the left (lion room / outside).** This holds in
    the close-ups s116, s121 and s127 at full size. Keep this orientation in any re-render.
12. s114: **fixed.** The push-in shows a red double-arrow, "3 IN (7.5 CM)", and LION / MEN labels. Legible.
13. The sitting lion in s091/s093 (redrawn `tsavo_lion_sitting`) is **fixed** and now reads as a lion. **s160-s162
    are NOT fixed.** They use `tsavo_lion_looking_up`, which was not redrawn (see fix R2-1).
14. Variety: **fixed.** New close-ups s113 (zoom), s116, s117, s121, s124, s127, s142, s161 and s162 break every run.
    s012 is now an "11 + 24 = ABOUT 35" sum card. No run of 4 or more near-identical frames remains.
15. s001 thumbnail: still "(thumbnail pending)". This is expected at this stage (scene_ref thumbnail, delivered at
    packaging). I will screen it in the post-render round. It does not block this round.

### Required fixes
R2-1. **s161 (and s160, s162): the lion in the new close-up does not read as a lion.** `tsavo_lion_looking_up` at
   scale 2.0 is a tan blob with a dog/bear head pointing straight up. It has no visible ears and no tail, and the
   tail tuft floats as a loose brown ball on the ground at about (820, 875). The right foreleg is a flat outlined slab.
   s161 is the shot where the lion is the only subject. **Illustrator:** redraw `tsavo_lion_looking_up` using the
   Round-3 `tsavo_lion_sitting` construction (rounded ears, lion muzzle and chin, tail running from the rump to a
   dark tuft by the front paws, two proper forelegs), with the head tilted up about 45° rather than vertical.
   Re-key s160, s161 and s162.
R2-2. **s127: the lion is a black silhouette blob at the left edge that reads as a bear's head.** This is the
   "tight on Doug and the lion" beat, and s121/s122 just showed the lion in tan. **Director:** drop
   `silhouette`/`rim` on the `tsavo_lion` in s127 (keep `appear: 0.3`) so it matches s121. The rifles stay as they are.
R2-3. **s117 and s124: a half-sliced soldier sits on the right frame edge.** In s124 a head, rifle stub and body are
   cut at x=1920. In s117 there is a sliver of head at about x=1910. **Director:** shift the group x by about -60
   (s124) and about -40 (s117) so that soldier is fully in frame, or by about +120 so he is fully out. A clean
   inclusion is preferred, since it shows the men are in there.

### Minor (not blocking)
- s162: a tree twig crosses the top of the DOUG DEATHS box at about (1400, 110), a branch runs
  behind the DAYS WITHOUT box, and a detached "V" twig floats at the bottom-left (about 410, 1065). Trim the branch
  ends or shift the group x by +80.
- Carried over from Round 1, still open: the s164 rug is a plain oval (a lion-shaped rug would land the fact), and
  the two lions in the s166/s170/s171 case still overlap into one shape.

Re-screen after fixes: s117, s124, s127, s160-s162. Then post-render: samples, qc.json, s001 and the three thumbnails,
Shorts.

## Round 3: pre-render keyframes re-screen (2026-11-28)

Screened: freshly re-keyed s117, s120, s124, s127, s160, s161, s162, s164, s166, s170, s171 (contact sheet plus
full size for each; s161 paws/tail cropped at 2x).

**VERDICT: PASS** (pre-render keyframes. The post-render round is still to come.)

### Round 2 items: status
R2-1. s160, s161, s162: **fixed.** The redrawn `tsavo_lion_looking_up` now reads as a maneless lion in 1 second. It
   has a rounded ear, an eye, a cat muzzle with a dark nose, the head tilted up about 45°, and a haunch. The tail runs
   from the rump along the ground to a dark tuft by the front paws, so the tuft is attached and no longer floats. In
   s160 the lion at the base of the tree looks up at Doug, and the beat lands.
R2-2. s127: **fixed.** The lion is tan, not a silhouette. Its ear, eye and muzzle read at the left edge and match
   s121. All three rifles still rest across the men's laps with the muzzles up-right, away from the lion.
R2-3. s117 and s124: **fixed.** The right-hand soldier sits fully in frame at about x=1700-1830, with his rifle
   across his lap. Nothing is sliced at x=1920.

### Minor items
- s162: **fixed.** No twig crosses the DOUG DEATHS or DAYS WITHOUT boxes, and the floating "V" twig is gone.
- s166, s170, s171: **fixed.** The two mounted lions face each other with clear space between them. The cap sits on
  the floor of the case between them.
- s164: the rug is now a fringed rectangular rug, so it reads as "rug", but it does not say "lion". The flying
  calendar pages carry "25+ YEARS". Not blocking, and acceptable as is.
- s120: clean. The tan lion lunges against the bars on the left, the men sit on the right with their rifles across
  their laps, and Doug is outside, horrified.

Next: post-render screening of samples, qc.json, the s001 cold open with thumbnails A/B/C and their `_small`
versions, and the Shorts.

## Round 4: thumbnails A/B/C and the s001 opening frame (2026-11-28)

Screened: `build/thumbnail.png`, `thumbnail_b.png`, `thumbnail_c.png` at 1280x720, their `_small.png` versions at
168x94 (side by side at 1x and 3x nearest-neighbour), and `build/keyframes/s001.png`. Pairings come from
`metadata.json` packaging candidates 1-3.

**VERDICT: FAIL** (A PASS, B FAIL, C PASS). One fix on B, then re-screen B only.

### Per variant
- **A "NO MANES"**, title "Why the Tsavo Lions Kept Killing Rail Workers for 9 Months": **PASS.** The text is
  legible at 168 px, spelled right and not cropped, and it does not touch the drawings. Two tan heads with round
  ears, whiskers and pale muzzles flank the tent, and they read as big cats, without manes, which is the hook. Doug
  is in the lit doorway, and the red cap and white head pop against the dark interior even at feed size. He is
  on-model and clearly scared. The heads are cropped at the frame edges, which is intentional framing. No gore,
  no victim shown, not cutesy. Minor (graphic designer, not blocking): the heavy half-closed lids make the lions
  look bored rather than predatory. Opening the lids slightly and adding a brighter catch-light would sell the threat.
- **B "LAST ONE HERE"**, title "How Two Lions Killed Enough Men to Stop a Railway in 1898": **FAIL.** The text,
  Doug, the shovel and the departing train all read. The threat does not read: the two "lion eye" pairs are plain
  orange ovals with no pupils, and at 168 px they read as orange dots, like fireflies, flowers or lamps. With no
  lion shape anywhere, the picture shows Doug waving at a train, and the "two lions" in the title have nothing to
  land on. The right-hand pair (about x=670-760, y=520-550) also butts against the wagon's left end at x≈760.
- **C "UP A TREE"**, title "How Doug Would Die Guarding the Tsavo Railway Camp in 1898": **PASS.** The text is
  legible and clear of the tree. The sitting maneless lion reads in 1 second, with its head tilted up at Doug. Doug
  is in the fork at the top of the tree with his cap on. The moon balances the frame, there is one clear focal
  relationship, and the picture fits the title. Minor (graphic designer, not blocking): at 168 px Doug's head is
  about 5 px, readable only by the red cap. Scaling Doug and the tree crown up about 1.3x, with the moon kept clear,
  would help. The lion's near foreleg is a straight tube with a rounded top that ends at the chin. It is
  acceptable, but tapering it into the chest would look less like a post.

### s001
The keyframe on disk was a stale white "(thumbnail pending)" placeholder dated 18:41, before the 18:53 thumbnail.
I re-keyed it (`python -m studio keyframes 061-tsavo-lions-bridge --shots s001`) and it now matches thumbnail A
exactly at 1920x1080, with nothing cropped by the upscale. Editor: confirm that the final render's s001 is the
thumbnail art and not the placeholder (check the 0 s frame in the samples).

### Sensitivity, policy
No blood, bodies, remains or attack depicted in any variant. No real victim or real person (Patterson, the workers)
is drawn, and the men on B's train are alive and leaving, which matches the historical exodus. None of the variants
has a nursery tone. None of the variants is misleading against its title.

### Fixes
1. **B** (graphic designer): make the lurking lions unmistakable. Turn each eye into an almond shape with a dark
   vertical slit pupil, about 1.5x the current size. Add a faint darker-tan or dark silhouette of a maneless lion
   head (ears and brow) around each pair, half-hidden in the grass. Move the right-hand pair left and up, to about
   x=560-640, y=470, so it sits clear of the wagon. Check that it still reads as "lion eyes" at 168x94.

Re-screen after the fix: B and B_small. Then the post-render round: samples, qc.json, the s001 0 s frame, Shorts.
