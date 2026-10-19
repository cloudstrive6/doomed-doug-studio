# Visual review: 023-hippo-every-era

## Round 1: pre-render keyframes (2026-10-19)

I checked 26 contact sheets covering all 301 shots, and opened individual keyframes where something looked wrong (s018, s096, s108, s154, s194).

VERDICT: FAIL

Overall the episode is strong. Doug is on-model and readable throughout. The deaths are cartoon only: splashes, a cap left behind, ghosts and a tombstone. There is no gore and no kids-show tone. The HUD (DOUG DEATHS / HIPPO SURVIVED) counts up correctly across all 12 stops, and spelling is clean. The fixes below are mostly mismatches between picture and narration, a few elements that are missing or can't be read, and text sitting on top of drawings. Must-fix items are 1–8. Items 9–16 are polish but should go in the same pass.

### Must fix
1. **s056 (director)**: The label is "CALVES" and the arrow points to the crocodile, but no calf is drawn. Viewers will read the crocodile as "calves". Add a small `hippo` (scale ~0.3) beside the adult and point the arrow at it. Leave the crocodile heading toward the calf.
2. **s124 (director)**: Two problems. The narration says "then past the hippo", but `hippo_submerged` (x 1400) sits under `titanoboa_coil` (x 1500) and can't be seen, and Doug (x 500) is mostly hidden by the coils. Also, s124 is the **only shot with no DOUG DEATHS / HIPPO SURVIVED HUD**. Fix: draw the hippo after the coils, or move it into a gap between coils, so its ears and eyes show. Make sure Doug's head stays clear, and add the three standard HUD elements.
3. **s096 (director)**: All three red arrows miss what they point at. The top arrow ends in open water, the "JAWS" arrow lands on sand past the snout, and the lower-left arrow stops short of the feet. Re-aim them at the snout (~1330,770), the jaws/teeth (~1250,790) and the hind foot (~930,880), and add "BIG FEET" and "LONG SNOUT" labels so each arrow has a meaning.
4. **s154 (illustrator/director)**: For Doug's T-rex death, a large flat dark-brown ellipse with the cap in it doesn't say "stomped". It reads as a pit or a dark pool, which is close to "blood pool" territory at feed size. Replace the ellipse with a clear three-toed T-rex footprint, using the tracks/footprint style from the Morrison stop, with the cap pressed flat in it.
5. **s276 (illustrator)**: The early Earth's "continents" are two flat near-black squares on a blue circle. They read as holes or a render glitch. Redraw them as irregular brown/grey volcanic landmasses, or as small island blobs.
6. **s145 (director)**: A dark parallelogram (`poly` 1350–1960 × 860–980) cuts off at the right frame edge and looks like a stray shape. If it is meant as a looming T-rex shadow, make it a recognisable T-rex silhouette shadow. If not, delete it.
7. **s018 (director)**: The "WARM SPELL" wordart sits on Doug's cap and head. Move the wordart up to about y 470 (between the sun and the thermometer), or move Doug and the hippo down/right.
8. **Variety (director)**: Two runs of near-identical compositions need breaking up.
   - **s002–s004 and s006–s009** both use the same room with the time machine on the left, Doug in the middle and the hippo on the right. Change the framing in at least s003 and s008: a close-up on the hippo's face for "did not agree", and a low wide shot of the hippo dwarfing the door for "does not fit".
   - **s283–s287** use the same Hadean layout five times: moon top-left, Doug left, pool right. Give s284 its own visual (a 0% O2 meter or an empty air tank instead of the small crossed icon over the moon). Shoot s286 ("Here's the twist") as a close-up of the hippo in the pool or a zoom-in.

### Text overlapping drawings / HUD (fix in the same pass)
9. **s042 (director)**: "HALF A BUS" wordart overlaps the bus roof and crowds the HIPPO SURVIVED HUD. Move it to y ≈ 960 under the bus, or shrink the bus to about 0.85.
10. **s115 (director)**: The angry sun (~x 490, y 970 on the sheet) covers the HIPPO SURVIVED HUD badge. Move the sun left of x 1300 or lower than y 330.
11. **s158 and s208 (director)**: The conifer / Archaeopteris tree crown goes behind or over the DOUG DEATHS box. Move the tree left of x 1250, or scale it down so its top stays below y 300.
12. **s162 (director)**: "REDWOOD TALL" runs into the conifer's branches. Move the wordart left (x ≈ 600) or above the tree top.
13. **s174 (director)**: "40 TONNES" wordart sits on the "35 M" label and the sauropod's neck. Separate them, for example "40 TONNES" at y 380 left of the neck and "35 M" over the dashed length line near the body.
14. **s213 (director)**: "5 CM FANGS" covers the Hyneria's eye and upper head. Move it to the upper-right corner above the fish (y ≈ 330) and keep the arrow on the teeth.
15. **s116 and s035 (director)**: "AVERAGE YEARLY" touches the thermometer tube (s116), and "A LONDONER" sits over the dome and cloud (s035). Nudge each so it clears the drawing.

### Advisory (owner/art director call; not blocking alone)
16. **s297 (art director)**: Doug appears without his cap (`gear: cap_off`) because the cap is on the hippo for the "cap survived all twelve" payoff. At this size a capless stick figure on the far right doesn't read as Doug. Either keep this gag and make him bigger with the "DOUG SURVIVED" label pointing at him, or confirm that capless Doug is allowed under the locked design.
- Minor, no change required: s028 (the lion in the reeds is barely visible at the left edge; a visible eye or ear would sell "reeds start to move"); s098 (the "LIKE A CROC" inset croc floats in the sky; a small frame around it would help); s250/s284/s289 (the crossed-out O2 icons are small and the X hides "O2").

### Checked and OK
Doug is on-model in every live shot. Ghost and float poses are used only after deaths: s029, s055, s084, s103, s154, s201, s223, s266, s294. Every stop has a clear title card, era label and verdict chalkboard. Silhouettes (croc, Purussaurus, Titanoboa, T-rex, Allosaurus, sauropod, gorgonopsian, Hyneria) all read. Maps, scales and comparisons are legible. The end card arrow (s301) points down to the comments.

## Round 2: verify Round 1 fixes (2026-10-19)

The keyframes were stale (the contact folder held 1 sheet, and the shotlist had changed after the last render). I re-ran `python -m studio keyframes 023-hippo-every-era` for all 301 shots. A second full run came after the art director's 17:27 `glow_r: 0` edit to s145, so these findings match the current shotlist (31 changed shots). I opened every Round 1 shot full-size, and checked every changed shot plus its neighbours on the contact sheets.

VERDICT: PASS

### Round 1 items
1. **s056: fixed.** A calf hippo stands between the adult and the croc, and the CALVES arrow lands on the calf.
2. **s124: fixed.** Static frame. Doug's head and cap are clear on the left bank, the hippo shows between the coils with ears and eyes up, and all three HUD elements are back. The underwater body cutaway matches s125.
3. **s096: fixed.** LONG SNOUT lands on the snout tip, JAWS on the tooth row, and BIG FEET on the hind foot.
4. **s154: fixed.** A three-toed sand-rimmed footprint with the cap pressed flat. It reads as "stomped", not as a pool.
5. **s276: fixed.** Irregular brown landmasses. They no longer read as holes.
6. **s145: fixed.** The stray parallelogram is gone. A small T-rex silhouette stands on the horizon. After the second render the red speckle at its feet is gone. In the first render it read as blood mist, so keep `glow_r: 0`.
7. **s018: fixed.** WARM SPELL sits between the sun and the thermometer, well clear of Doug.
8. **Variety: fixed.** s003 is a close-up on the hippo's face and s008 shows the hippo wedged in the time machine, so the room run is broken. s284 has its own O2 0% gauge. s286 is a close-up on the hippo in the pool. The Hadean run s283-s287 now alternates.
9. **s042: fixed.** HALF A BUS is above the roof and clear of the HUD.
10. **s115: fixed.** The angry sun is out of the counter zone.
11. **s158 / s208: fixed.** Both tree crowns are below and left of the counter boxes.
12. **s162: fixed.** REDWOOD TALL is clear of the crown.
13. **s174: fixed.** 40 TONNES and 35 M are separated.
14. **s213: fixed.** 5 CM FANGS sits lower-right and the arrow lands on the teeth. The eye is clear.
15. **s116: fixed. s035: partly fixed.** A LONDONER is now clear of the dome but still runs over the right-hand cloud. It stays legible (see polish item P1).
16. **s297: fixed.** Capless Doug is bigger, and the DOUG SURVIVED: 3 / 12 arrow points straight at him, so the cap gag reads.

Also checked: s176 (a sliver of the cap shows behind the cycad, which is the "hides" joke and is acceptable) and s182 (the foot clears the caption bar). s108, s113, s205, s214, s249 and s268 all look clean. No gore, Doug is on-model in every live shot, and there is no kids-show tone.

### Optional polish (not blocking; do it if anyone is already touching the shotlist)
- P1. **s035 (director):** Move the right cloud (about x 1660, y 360) off A LONDONER, or move the wordart down to about y 440.
- P2. **s298 (director):** ALL TWELVE sits over the dome's base and touches the right cloud. Shift it right/down to about (1250, 460), or remove that cloud.
- P3. **s174 (director):** The sauropod's head ends about 30 px under the HIPPO SURVIVED badge. Scale the silhouette to about 0.95 or move it left about 80 px so the head has some air.
- P4. **s008 / s010 (director, advisory):** Both now use the same "hippo rear wedged in the doorway" picture for "does not fit" and then "it gets in". It's fine as a callback. If you want s010 to pay off, show the door shut with the hippo's face behind the glass (as in s011).

### Thumbnail: A (`thumbnail.png`) vs B (`thumbnail_b.png`)
**A is stronger. Ship A.**
- **A (archetype C hero, "BAD TIMING"):** At 320x180 it reads instantly: one huge hippo nose to nose with a T-rex head, plus a tiny red-capped Doug on its back as the scale figure. That gives two subjects, two words, a flat orange field and high contrast. It complements the title without repeating any title word, isn't misleading (the T-rex stop is a real chapter), and matches the s001 opening frame. Small nit for the graphic designer, not blocking: the T-rex teeth zigzag into hourglass/bow-tie shapes at full size. Plain downward triangles on the top row would read more cleanly.
- **B (3x3 verdict grid):** At 320x180 the tiles are recognisable but the labels are already tiny. At 168x94 they are close to unreadable, and the same grey hippo repeated nine times flattens the grid. More importantly, **the check/X badges give away the episode's payoff**: the title asks whether the hippo survives, and the thumbnail answers it for 9 eras. B also has no Doug, and it leaves out 3 of the 12 stops (Hyneria, Bare Land, Archean). If B is ever A/B-tested, drop the badges (or replace them all with "?") and add a small Doug to one tile.
