# 061 decisions

## 2026-11-28: script draft 2, APPROVED (creative director)
- Screener PASS (hook 8, structure 8, voice 7; 2,047 words, about 10.5 min). E1 (toothache line moved next to the injury sentence) and E2 (new outro CTA "Subscribe before it hits four thirty-six.", not a 048-060 line) are applied in the working copy.
- Brief deviations accepted: band "Week three." instead of "Week one." (Ungan Singh is about three weeks in, Patterson ch. 2); Walkout (1 Dec) now before Trap (3 Dec) so the axis is monotonic; the trap survival keeps "Doug did not agree to this." and the only quiet disappointment; deaths 431-435 at 2, 4, 5, 6, 9 as briefed in count.
- Real-victim handling meets the brief: 135 attributed and called "killed", Yeakel's ~35 framed as eaten, one straight "real people" line, Ungan Singh named once and never joked about, no cave of bones, no lion death shown.
- CD edit in place: closing kicker "nobody is checking its teeth" -> "their teeth" (the lions', not the cap's).
- Notes for the director: the trap's off-screen BANG text must never sit over a lion; Patterson is a plain stick figure with a hat and no visible rifle; lions lean and blank-eyed (Lion King risk); the sale price $5,000 is secondary-sourced (flagged in facts.md), keep it off the thumbnail and title.

## 2026-11-28: thumbnails A/B/C, A APPROVED, B and C REVISE (creative director)
Checked the full-size and `_small` versions of `build/thumbnail.png`, `thumbnail_b.png` and `thumbnail_c.png` against the ranked titles in metadata.json.

**A: "Why the Tsavo Lions Kept Killing Rail Workers for 9 Months" + NO MANES: APPROVED.** I would click it. The two lean heads framing the
lit tent door, with tiny Doug in bed between them, reads instantly at 168 px (yellow text, two tan heads, a white and blue centre).
NO MANES adds a twist the title doesn't spell out, and the heads look maneless, so the image backs it up. Lions are blank, mouths are closed, not cute; no blood, no rifles.
No changes are required. Optional nit only: the inner lantern glow could be ~20% brighter so the tent interior pops more at small size.

**B: "How Two Lions Killed Enough Men to Stop a Railway in 1898" + LAST ONE HERE: REVISE.** The story (train leaves, Doug left behind) reads,
but the threat doesn't. The lions are the whole joke, and right now they're invisible.
1. Eyes: the `lit_eye` ovals are plain orange blobs with no pupil, and at `_small` they read as fireflies or flowers. Redraw them as almond eyes
   (rx ~22, ry ~9, fill `#ffd23a`) with a black vertical slit pupil and a short flat black brow stroke above each pair. Make the glow
   stronger (spray r ~70, density ~0.18) and put a darker patch (`#14110c`) in the grass behind each pair for contrast.
2. Move the right pair (x 690/748). It sits against the rail truck and reads as lamps on the train. Put both pairs on Doug's side, away from the
   departing train: e.g. (90,515)/(150,515) and (245,545)/(300,545). Then the frame reads as "the train is leaving right and the lions are waiting
   left, behind Doug".
3. Re-check `_small`: both pairs must read as eyes at 168 px. If they don't, scale them up again.

**C: "How Doug Would Die Guarding the Tsavo Railway Camp in 1898" + UP A TREE: REVISE.** The concept is the best payoff image in the episode,
but the execution isn't clickable yet.
1. The lion's eye is a tiny dark dot. The thumbnail concept says "eyes lit". Add the same lit almond eye as B fix 1 on the upturned face.
2. The lion doesn't read as a lion. The head is small for the body, and the front leg is a detached plank in front of the chest, so at `_small` it reads as
   a bear or dog. Preferred fix: render it as a dark navy silhouette (`silhouette: true` with a thin moon-side rim) with the lit eye. That's creepier, it hides the
   anatomy, and it keeps the Lion King risk at zero. Alternatively, scale the head ~1.3x and use the art-approved `tsavo_lion_sitting` leg
   geometry.
3. Doug is a red dot at `_small` and stands in the fork instead of clinging. Make him ~1.6x larger, clinging to the trunk near the top (arms
   around it, or arms up gripping branches). Lower the tree top so the gap between Doug and the lion's face is about one lion-head tall (the tension
   is "patient, just out of reach"). Move the moon so it sits behind Doug's head and backlights him.
4. Keep everything else: UP A TREE text, bare tree, no rifle, no platform shooter, no blood.

Once B and C are fixed, re-run the visual screener on all three plus `_small`, then return them for a re-approval. A can go to the s001 cold open now.

**Rifles in laps: CONFIRMED ACCEPTABLE** (owner rule "rifles only resting in soldiers' laps"). Verified in shotlist.json: `rifle_held` appears
only in s116, s117, s119-s122 and s124-s128 (two per shot, `rotate` -25/-35, never flipped). The muzzles point up and right, away from the lion at frame left
(checked s121 and s127). No flash or smoke, and no rifle is held by Doug or Patterson. It's historically grounded: Patterson's account puts armed
men inside the trap who were too frightened to shoot straight. There are no rifles in thumbnails A/B/C or in gen_thumbs.py. Standing conditions:
never `flip: true` without `rotate: +25`; never aim at or overlap a lion; BANG text never over a lion; no rifle in any thumbnail, Short cover
or the s001 cold open; Doug never holds one. A rifle in any other shot needs CD sign-off.

## 2026-11-28: thumbnails B/C re-review, B and C APPROVED (creative), pending visual re-screen (creative director)
Checked revised `build/thumbnail_b.png`, `thumbnail_c.png` and both `_small` files (rendered 18:57, commit 2f78a127) against the fix list above.

**B "LAST ONE HERE": APPROVED.** I'd click it. Fix 1 is done: almond `#ffd23a` eyes with slit pupils, a sprayed glow and dark head patches behind them. At 168 px
both pairs now read as eyes in the grass, not fireflies. Fix 2 is done differently: the right pair moved to about x 600-700, clear of the wagon (it starts at about x 760). It sits
between Doug and the train instead of behind him, but two lions flanking a stranded Doug reads just as well, so I accept it. Fix 3 passes. Non-blocking nit: the faint head shapes,
with round ears on a round dome, lean bear or teddy at full size. If there's a respin, flatten the crown and narrow the ears so they match A's lion heads.

**C "UP A TREE": APPROVED.** I'd click it, and it's the strongest of the three. Fix 1 is done: a lit slit eye on the upturned face. Fix 2 is done: a black silhouette (not navy, which is fine) with a cream rim, and
at 168 px it reads as a big cat staring up at Doug. The tail tuft sells "lion" over "panther". Fix 3: Doug is much larger and the moon backlights his head. The rig
has no hugging pose, so "panicking at the treetop" with his arms up is accepted. It reads. The gap between him and the lion is short and tense. Fix 4 holds: no rifle, no blood, no platform shooter.
Non-blocking nit: the rim lines between the forelegs form a small "4" or triangle shape that shows at `_small`. Drop that inner rim segment on a respin.

**Condition:** visual_review.md has no screener pass yet on the revised B/C (round 4 failed B). Run the visual screener on B, C and both `_small` files before packaging.
If it PASSes, all three are approved for the A/B/C test with no further CD round. If it FAILs on anything beyond the nits above, send it back to me.
