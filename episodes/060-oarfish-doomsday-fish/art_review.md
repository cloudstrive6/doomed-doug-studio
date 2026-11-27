# 060-oarfish-doomsday-fish: art review (art director, 2026-11-27)

## Re-check 3 (changed shots, build/keyframes): PASS

I re-checked s003 s004 s012 s072 s073 s084 s091 s114 s130 s151 s152 s153 s158 s159 s160 s169 s171 s172 s175 s176 s177, and their
neighbours for variety (s002, s005, s011, s013, s071, s074, s083, s085, s090, s113, s129, s150, s154, s157, s161, s168, s170, s173, s174).
My round-2 fixes and the visual-screener round-1 fixes are all in.

| Shot | Result |
|---|---|
| s003 | PASS. The ITS OWN BODY keyword ends at about x 1310 and clears the crest (about x 1415). Doug now holds the dropped tail piece, so the teaser reads. |
| s004 | PASS. Gut corridor with Doug, torch and three tapeworms in the beam. NOT ALONE now matches the line. |
| s012 | PASS. Accepted as a build: the dashed match line plus A MATCH?. The punch-in was advisory. |
| s072, s073 | PASS. The arrow leaves PASSENGER from the left and no longer crosses the "P". The isopod is bigger and easy to find, and the fish sits clear of the chapter tag. Nit: the arrow tip stops about 100 px short of the isopod. Extend `to` about 80 px left if it is a one-line change. |
| s084 | PASS. NO TEETH sits in open water, off the belly and fin. |
| s091 | PASS. NO WAY TO HURT clears the pelvic streamers. |
| s114 | PASS. The MOST OF IT arrow goes around Doug's head to the fish body. |
| s130 | PASS. "8 M" sits completely on the page. |
| s151 | PASS. The worms-in-beam close-up is a new layout. The torch is held from off-frame, which works for an insert. |
| s152 | PASS. Wide shot with Doug small. Clearly different from s151 and s153. |
| s153 | PASS. FURTHER DOWN is above the cone and Doug's legs are clear. |
| s158 | PASS. **New thorny-headed worm (shapes):** a `worm_icon` body with a pale round proboscis ringed by short maroon spikes. It reads as a different worm from the two roundworms, is on the detailed tier at this size and on-palette (`#f2b8b8`/`#8a3e3e`), is not gory, and isn't cute. The three-column specimen card is a clear layout break inside the gut run, and the labels sit inside the safe area. Nit (optional): make it `~24 TAPEWORMS` so the column labels match ("2 ...", "1 ...") and TWO DOZEN clearly refers to the tapeworms. If the worm comes back in a later episode, the illustrator should save it as a library asset (`thorny_headed_worm`) and not rebuild it from loose shapes. |
| s159 | PASS. The arrow and the 15 cm bracket are on the central hanging worm. |
| s160 | PASS. Doug's face close-up is on-model: round head, grey crescent, vertical oval eyes, red cap and goggles. |
| s169 | PASS. ADULT label restored, so it matches s167/s168. |
| s171 | PASS. Doug sits with the worms. A new pose in the same plate is fine. |
| s172 | PASS. Doug's two eyes in the dark set up the "torch ran out" beat and keep it distinct from s173. |
| s175, s176, s177 | PASS. Ghost Doug keeps his cap. The real cap rides the fin (s175), sits on the seabed (s176) and sits on the gravestone (s177). That makes one real cap per frame. |

Variety: the s150-s160 gut run now goes corridor, close-up, wide, medium, corridor, specimen card, measured worm, face close-up, so
no 4-in-a-row repeats are left. Style, zone colours (gut pink, `#1b4f86`, cream diagram, dark TV room), the HUD and the safe area are
consistent. There are no gore or kid-appeal flags.

**Verdict: PASS (art approved). Waiting on the visual-screener pass before staging `art_approved`.**

## Re-check 2 (keyframes + all 15 contact sheets): FAIL, 4 small director fixes

The previous fixes are all in: `stick_man_arms_up` redraw, s036, s038, s056, s076, s167. All 20 assets are now APPROVED.

| Shot | Result |
|---|---|
| s036 | PASS. The spyglass sits in the cook's hand and he stands in front of the rail with his face clear. |
| s038 | PASS. The spyglass is in his hand. |
| s056 | PASS. The six men are Doug-sized, the fish rests on the raised hands and Doug's cap is clear. |
| s076 | PASS. "DOUG DEATHS: 428" is fully readable and the fingertips only touch the label's right end. |
| s167 | PASS. The larva is the subject, the arrow runs larva to mako (ADULT), and no oarfish is mislabelled. |
| s168 | PASS. Accepted as is. The narration names the oarfish as the host the worms are leaving. The ten shots before (s145-s166) put us inside that oarfish, so the host is implied. The card's job is "not staying": NOT STAYING over the larva plus the arrow out to the mako says that. Adding an oarfish would bring back the s167 mislabel risk. |
| s169 | PASS. Nit (optional): it drops the ADULT label that s167/s168 had. Keep it for continuity if it is a one-line change. |
| s175, s176, s177 | **FAIL: my fix 5 was wrong.** Art bible "One cap per frame": "A ghost Doug keeps his cap as always (the ghost cap is death grammar, not a second real cap)." Style bible §7 rule 2 says the same. `cap_taken` is only for `on_back` bodies. The cap move to the fin edge (930,490) is correct, so keep it. |

### Fixes (director)
1. **s175, s176, s177:** remove `gear: ["cap_taken"]` from the ghost Doug, so the ghost wears his cap as in s174. Keep `doug_cap` on the fin
   (s175), on the seabed (s176) and on the gravestone (s177). This is my error from the last review, not the director's.
2. **s072:** the arrow tail starts inside the PASSENGER label and cuts through the "P". Change `from` [1250,600] to **[1145,640]** (just left of
   the label's left edge), keeping `to` [990,630] and a gentle bend, so the arrow leaves the label instead of crossing it.
3. **s130:** the "M" of "8 M" (x 1036, size 70) runs onto the book's right cover. Move it to **x 990** so the whole text sits on the page.
4. **s003:** the "BODY" of the ITS OWN BODY keyword overlaps the oarfish crest (crest top at about (1415,340)). Shift the keyword about 80 px left
   (right edge ≤ 1380) or up 40 px so it clears the crest.

Re-render s003 s072 s130 s175 s176 s177. Everything else on sheets 01-15 passes. Style is consistent across shots, Doug is on-model, zone colours
are consistent (cream diagram, `#1b4f86` midwater, `#0b2447` deep, gut pink, sand/sky beach), text sits in the safe area, the HUD is consistent,
and there are no gore or kid-appeal flags. Layouts vary enough. The near-repeats (s010-s013 chart, s028-s030 annotations on one fish,
s167-s169 life-cycle card) are deliberate builds where each shot adds a new annotation. s001 is the thumbnail placeholder (graphic designer).

---

## Previous round: FAIL (19/20 assets APPROVED; 1 illustrator redraw; 5 director placement fixes; HUD device APPROVED)

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
5. *(Superseded in re-check 2: the `cap_taken` half of this fix was wrong, because ghost Doug keeps his cap. The cap move stands.)* **Director, s175: two caps on screen.** `doug_cap` rides the fish, but Doug (right) still wears his cap. Give Doug the `cap_taken` gear.
   Also move the cap from (950,420), where it sits on the red crest and its red merges with the crest, to the fin edge the
   illustrator kept plain: stump (900,640) at 0.5 + local (+60,-300) gives **(930,490)**.
6. **Director, s167: the LARVAE label sits under an oarfish,** so it says the oarfish is the larva. Put `tapeworm_larva` (about 0.4) above
   the LARVAE label as the subject. Either drop the oarfish or keep it small behind with a label such as `HOST`, so the arrow goes
   larva to mako (ADULT).

Re-render s036 s038 s056 s076 s167 s175 after the fixes. I'll re-check those shots and then review the full contact sheets.
