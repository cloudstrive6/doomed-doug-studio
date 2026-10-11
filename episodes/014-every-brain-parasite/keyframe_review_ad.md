# 014 keyframe review: art director

Reviewed all 22 contact sheets (s001-s256) and the full-res keyframes where needed, checked against `channel/art_bible.md`, style bible section 7 (rules 1-9) and `shotlist.json`.

## What holds
- **Style and two tiers:** crude Doug and humans (scientist, stick patients) sit against detailed creatures (killifish, heron, carpenter ant, sheep, border collie, rat, horse, mandrill, amoeba). Grey `head_outline` / `body_outline` diagrams are used consistently.
- **Doug on-model:** the red cap is visible in every shot, ghosts included. The worn costumes (killifish, ant, sheep) leave his head, face and cap clear, and are dropped on screen at the band shift (s086/s088). Deaths use `on_back` + `dead` + `cap_off`, never `rotate` (s141, s142, s193, s220, s221, s252). The no-body deaths keep the cap in frame: on the water (s028), on the grass blade (s059), on the ground (s084) and on the flowerpot (s253).
- **Counter:** 114 to 121 ticks only on death beats. The Spirometra 119-and-back gag (s167/s168) reads clearly. The BRAIN meter flips STEERED, then OCCUPIED, then EATEN at the band cards. Nothing intrudes into the counter zone, and the inset frames start at y >= 250 (s141).
- **Colour language:** the backdrop darkens one step per band: cream/salt marsh, then flesh pink, then maroon, then near-black for the boss. Night shots, sunset and day are consistent within each item. I logged it as a reusable ramp in the art bible.
- **Text:** red item title cards, white section headers ("STEERS YOU.", "LIVES IN YOU.", "EATS YOU."), wordart of 1-4 words with at most 2 on screen, and nothing on green ground. Everything is inside the safe area.
- **Reveals:** the heron silhouette (s018) is followed by colour (s019), the worm (s153) by s154, and the mandrill (s223) by s227. No gore. The body diagrams are cartoon grey with pale cysts and no tissue detail.
- **Layout variety:** location scenes, diagrams, maps, scale comparisons, insets and bar charts rotate. No composition repeats 5 times in a row.

## Fixed directly in shotlist.json (re-rendered: s018, s041, s108, s139, s140, s146, s192, s194, s223)
1. **s223:** the mandrill silhouette was invisible. Its glow `spray` was drawn after the black shape, which speckled it out on the near-black backdrop. I moved the spray behind the silhouette and raised its density to 0.55, so the shape now reads.
2. **s018:** same order fix for the heron's glow spray, so the silhouette is solid black.
3. **s139, s140:** the "vegetarian" sign cord crossed Doug's face and the sign covered his chin. The sign now hangs on his chest from the neck point.
4. **s192:** the worm's dashed route crossed Doug's eye. The path is now drawn behind Doug, so his head covers it and the worm sits on the cap.
5. **s194:** the shadow spray speckled over Doug's face. Moved it behind him.
6. **s041:** the thermometer sat on top of the sun. Moved it and the COOL label to x 1400.
7. **s108:** the WEEKS/MONTHS labels spilled over the calendar's bottom edge. They are now stacked below it.
8. **s146:** this was the second of three identical side-head shots (s145-s147). It is now a grey patient body with headache zigzags, plus the `scientist` as the doctor, keeping 2008 / UNITED KINGDOM / ?.

Art bible updated: the parasite/body severity ramp, glow spray goes before the silhouette, neck-hung signs, and paths/sprays near Doug are drawn before him.

## Advisory for the director (non-blocking)
- s118-s126 are 9 grey anatomy diagrams in a row (body, head, body). Each one differs in content and position, but if the editor sees the Pork Tapeworm middle sag, cut one shot to Doug reacting or to a location beat.
- s153-s155 are three top-down heads in a row (silhouette, reveal, removal). It is acceptable as the scan "flipbook", so leave it unless pacing calls for a change.

KEYFRAMES: PASS

Remaining fixes: none blocking.
