# 060-oarfish-doomsday-fish: art review (art director, 2026-11-27)

## Verdict: FAIL (19/20 assets APPROVED; 1 illustrator redraw; 5 director placement fixes; HUD device APPROVED)

Reviewed `assets/previews/060-oarfish-doomsday-fish-assets.png`, `-ad-review.png`, larger `asset-preview` renders of the crude-tier
figures, and fresh keyframes of every shot that uses a flagged asset: s002 s003 s004 s007 s023 s031 s036 s038 s056 s076 s077 s085 s089
s109 s117 s128 s134 s137 s142 s143 s152 s155 s167 s175.

## Assets (20)

| # | Asset | Verdict | Notes |
|---|---|---|---|
| 1 | `oarfish_stump` | APPROVE | It is the same animal as `giant_oarfish`. The stump is a clean rounded pale cap with a grey seam and no red, so it meets the CD condition. The head top at -440 (not -500) comes from reusing `giant_oarfish`'s head, so **no redraw**. The director already places it by anchor, and it reads at 0.45 on cream and at 0.5 on `#0b2447`. |
| 2 | `oarfish_stump_short` | APPROVE | Calm and not pitiful. The shortened streamers are fine. |
| 3 | `oarfish_tail_piece` | APPROVE | Sealed rounded front end with no flat cut. The tip at +402 sits in Doug's hand in s134. |
| 4 | `oarfish_head_closeup` | APPROVE | The eye is blank, the mouth is a straight line, there are no teeth and it is not cute. |
| 5 | `oarfish_head_open` | APPROVE | It reads as a tunnel entrance (s143). There are no teeth and the eye is round, not an X. |
| 6 | `streamer_fish` | APPROVE | Clearly slimmer and darker, with no crest or oars. The top edge is clean under the s109 zigzag. |
| 7 | `tapeworm_larva` | APPROVE | A plain ribbon with no segments, no hooks and two deadpan dots. It reads on gut pink and as the s004 silhouette. |
| 8 | `krill` | APPROVE | The silhouette keeps its legs and antennae. |
| 9 | `shortfin_mako` | APPROVE | The conical snout, lunate tail and closed mouth all read, so it is clearly not the generic `shark`. |
| 10 | `undersea_palace` | APPROVE | It is respectful, fairy-tale, with no text or symbols. The right edge is clear for the oarfish (s007). |
| 11 | `rooster` | APPROVE | The comb, sickle tail and hackle all read, so it can't be confused with `chicken`. |
| 12 | `bean_tin` | APPROVE | No brand or text. |
| 13 | `spyglass` | APPROVE | It sits correctly in Doug's `point` hand (s023, s031). See director fixes 1-2 for the cook shots. |
| 14 | `ship_cook` | APPROVE | On Doug's tier, with a flat face and `keep_ink` on the face. The hand is at (+110,-140) as specified. The toque rising to -424 is a **placement matter only, so no redraw**. At 0.55-0.6 the toque top sits 233-254 px above the hips, far below the HUD, so the director keeps the current scales. |
| 15 | `stick_man_arms_up` | **REDRAW (illustrator)** | Drawn at 1.45x `stick_man_plain`, so in s056 the crowd is 1.45x Doug's size: off-scale giants, and the size mismatch is obvious beside Doug. It also leaves a library trap, because every later reuse at "normal" scale makes giants. **This needs a redraw, not a shot fix.** Scaling to 0.29 would match sizes but leaves the hands only ~14 px above the heads, so the fish would sit on their heads. Fix 1 below. |
| 16 | `rope_puller` | APPROVE | The x overshoot to +164 is **placement only, so no redraw and no shot change**. At 0.26 with ~52 px spacing in s142/s155, the 15 men overlap slightly and read as one hauling team, which works better. The 8-wide lines are right for 110 px. Gritted teeth are fine. |
| 17 | `cooler_box` | APPROVE | No logos. |
| 18 | `desk_drawer` | APPROVE | The labels are blank. See director fix 4 for s076. |
| 19 | `krill_costume` | APPROVE | The dot eyes, zipper, felt legs and thick outline read as an empty suit on `#1b4f86`. |
| 20 | `park_bench` | APPROVE | No sign baked in. |

## Episode HUD: DISTANCE TO FISH readout: APPROVED

It follows the 049/057 meter pattern: a size-28 label at (1590,238) under the counter, with one `tape_measure` icon per shot (checked all 178
scene shots: every shot has exactly one label and one icon, and s136 has neither, as specified). Red-on-pink `#ffd2cc`/`#e0201b` from s137 is
legible on `#1b4f86`, `#0b2447`, sky, sand and gut pink. The widest value, `0 M (HOLDING)`, ends at about x 1830, inside the 1856 safe
edge. The tape measure reads as a yellow case + tape silhouette at 0.16 with no interior text. Nit (optional, not blocking): the icon's
right edge sits ~50 px left of the label box instead of ~30. Move the icon x +20 per label width if the generator makes it easy.
Added to the art bible.

## Fixes

1. **Illustrator, `stick_man_arms_up`:** redraw it at exactly `stick_man_plain` proportions (line width 5, head top -450, feet at 0)
   with both arms raised clearly *above* the head: shoulders/neck at about -300, elbows out at about (±90,-440), hands at about
   (±55,-600). That leaves the hands ~150 above the head top, so the pose reads as "holding something overhead" and not "hands on
   head". Bounding box x -100..+100, y -600..0. Update the description and `asset_requests.md` with the new hand point.
2. **Director, s056 (after fix 1):** keep the six men at 0.42 (now the same size as Doug at 0.42) and lower `giant_oarfish_beached` so its
   belly rests on the new hand line, y ≈ 900 − 0.42×600 = 648 (about 40-45 px lower than now). Doug's cap top (~706) keeps ~55 px of clearance.
3. **Director, s036 and s038: the spyglass floats above the cook's hand.** The hand is at hips + scale×(+110,-140).
   - s036: cook (250,860) at 0.55, so the hand is at (310,783). Move `spyglass` from (330,700) to **(310,783)**. Also, the deck rail
     (y ≈ 718) currently cuts across the cook's eyes because he is drawn behind it. Draw the cook *after* the rail (he stands on the
     deck in front of it), or move him so the rail passes below his chin.
   - s038: cook (1550,900) at 0.6, so the hand is at (1616,816). Move `spyglass` from (1620,740) to **(1616,816)**.
4. **Director, s076:** the `narrator_hand` covers the sticker, which reads "DOUG DEA". Move the hand right (about x 1180) so that only the
   fingertips pinch the label's right end, and the full "DOUG DEATHS: 428" is readable.
5. **Director, s175: two caps on screen.** `doug_cap` rides the fish, but Doug (right) still wears his cap. Give Doug the `cap_taken` gear.
   Also move the cap from (950,420), where it sits on the red crest and its red merges with the crest, to the fin edge the
   illustrator kept plain: stump (900,640) at 0.5 + local (+60,-300) gives **(930,490)**.
6. **Director, s167: the LARVAE label sits under an oarfish,** so it says the oarfish is the larva. Put `tapeworm_larva` (about 0.4) above
   the LARVAE label as the subject. Either drop the oarfish or keep it small behind with a label such as `HOST`, so the arrow goes
   larva to mako (ADULT).

Re-render s036 s038 s056 s076 s167 s175 after the fixes. I'll re-check those shots and then review the full contact sheets.
