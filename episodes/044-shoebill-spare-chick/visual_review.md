# 044-shoebill-spare-chick: visual review

## Round 2: pre-render keyframes (visual screener, 2026-11-11)

**VERDICT: PASS**

Screened: all 17 sheets in `build/contact/sheet_01..17.png` (s001-s195 plus the endslate), and a full-res crop of `build/keyframes/s188.png`.
s001 still says "thumbnail pending" on purpose. It gets checked in the post-render round.

### Round 1 required fixes: all 10 resolved
1. **shoebill_chick_big bill: fixed.** The bill is now a broad, horizontal clog shape pointing right, in horn-grey with a dark hooked tip,
   with the eye just above its base. At shot scale it reads as a shoebill chick on dusk (s147-s163), on night (s164-s193) and on cream
   (s138, s195). The full-res s188 crop confirms it: no more ear or chimney look.
2. **s002: fixed.** The bird's crown now meets the "UP TO 140 CM" line at the same height as the kid's head, and the "10-YEAR-OLD" tag is there.
3. **s165 / s176: fixed.** A small grey second chick now sits in the right half of the nest, the "peep" ticks come from it, and the orange fish is gone.
4. **s041-s047 variety: fixed.** The run is now wide, Doug close-up (s042), statue close-up (s043), wide with NOT FOOD (s044), Doug
   relieved (s045), eyeline (s046) and a bill close-up (s047).
5. **s133 / s134: fixed.** Both frames show the chicks instead of eggs.
6. **s140: fixed.** The water arc lands on Doug's cap with blue drip ticks, and the grey-green fuzz is gone. s143 now uses drip ticks as well.
7. **s123: fixed.** One shoebill, standing over Doug and waiting. The strike happens on the cut to the s124 aftermath.
8. **s079-s081: fixed.** A Nile monitor hangs from the bill in all three frames, with no blood.
9. **s103: fixed.** Doug stands on the low, tilting end of the mat, which sets up s104.
10. **s118: fixed.** The python silhouette haze is now neutral grey, not red.

Round 1 advisories: the orange banded fish has been replaced with a silver fish everywhere (s030, s035, s054, s055, s143 and the nests).
The s097 pair is still fairly close together but reads as two birds. No other action is needed.

### Fresh checks this round
- Doug is on-model and readable in every shot. The death counter steps 336 to 343 at the right shots (s026, s066, s085, s105, s124, s161, s191).
- Text is spelled correctly and does not collide with the counter or chapter tags. There is no gore: siblicide is only labelled, never
  shown, and the deaths are cartoon collapses, splashes and floating ghosts. Nothing has a kids'-show tone.
- No new runs of 4 or more near-identical compositions. The s171-s174 night-nest run changes from shot to shot (calendar cards, Doug,
  then the parent's entrance), which is acceptable.

### Next
The thumbnail (s001), sample frames, QC, the A/B/C thumbnails and the Shorts get screened in the post-render round.

## Thumbnails round 1 (2026-11-11)
I screened `build/thumbnail.png`, `thumbnail_b.png` and `thumbnail_c.png` at 1280x720, and their `_small` versions at 168x94
(also viewed at 4x nearest-neighbour). I also checked a full-res crop of Doug in A.
All three are free of gore (no blood, no injured animals, the croc hatchling in B is intact) and none of them has a kids'-show tone.
Doug is on-model in all three: red cap, white head, cartoon expressions in our own lines. The text is spelled correctly, is not cropped,
and does not repeat any word from its paired title.

VERDICT: FAIL (A FAIL, B FAIL, C PASS)

### A: "THE SPARE" / "Why the Shoebill Hatches Two Chicks and Lets One Die": FAIL
1. **Graphic designer:** delete the red `arrow` element in `thumbnail.json` (from [1180,250] to [1170,365]). Style bible §2 grammar
   says "no red arrows, no circles" on thumbnails. Arrows belong inside the video.
2. **Graphic designer:** once the arrow is gone, Doug must work as the second focal point on his own. At 168x94 he is about 10 px tall,
   grey costume on a grey/tan nest. Raise `shoebill_chick_costume` scale from 0.42 to about 0.60 and keep him alone in the right
   half of the nest (about x 1130, feet on the nest rim). The red cap and white head then read at feed size without help. The empty gap
   between him and the big chick is the story, so keep it.
- Advisory (no change required): the front-on bill reads more like a tan mask than a shoe at feed size. The pale stare still sells it.
  A three-quarter turn showing the bill's length would read faster. The big chick is fine.

### B: "EATS BABY CROCS" / "Why the Shoebill Is the Creepiest Bird on Earth": FAIL
3. **Graphic designer / illustrator:** the croc hatchling is the hook of this variant, but at 168x94 it reads as a brown twig or fern frond
   crossing the bill. Fixes: (a) give it a clear crocodile silhouette, meaning a long snout with a visible tooth row, four splayed legs
   and a tapering tail, in a greener olive (around #6b7a2e) that separates from the tan bill; (b) scale it up about 1.3x and angle it
   about 30 degrees off vertical so the snout end clearly points down and out of the bill. Keep it intact, with no blood.
- Advisory: the body is a round, pigeon-like oval. A taller, more upright stance with the neck showing would read more as a shoebill.
  The orange field, the text and Doug in the reeds all read well at feed size. The cattail tops behind "BABY"/"CROCS" are acceptable
  because the outlined text stays legible.

### C: "IT WAITS" / "Every Reason the Shoebill Is the Creepiest Bird Alive": PASS
The strongest of the three. The profile head and huge bill make the subject obvious in under a second at 168x94, and the bill tip hanging
just over Doug's cap is the threat. His gritted-teeth face reads, and the text is large and clean. It is not misleading: the shoebill's
motionless wait-and-strike hunting is in the script. Advisory only: the lungfish costume reads as a brown lump at feed size. That is fine
because Doug's head carries the moment.

### Advisories for all three (art director, no change required this round)
- Speckle/dither shading on the bird bodies is visible at full size. The style bible says thumbnails should look clean, and at feed size
  it disappears, so this is not blocking.
- Yellow (A, C) and white (B) outlined text differs from the style bible's "black on white / white on flat". This is accepted
  channel practice and reads well.

### Re-check needed
A after fixes 1-2 and B after fix 3: re-render with `python -m studio thumbnail 044-shoebill-spare-chick` and re-screen the full-size and `_small` files.

## Thumbnails round 2 (2026-11-11)
I re-screened `build/thumbnail.png` and `thumbnail_b.png` (rendered 18:21) at 1280x720, their `_small` versions at 168x94 (also at
4x nearest-neighbour), and a full-res crop of B's croc. C is unchanged and its small version still reads, so its round-1 PASS stands.
There is still no gore and no kids'-show tone, the text is spelled correctly and not cropped, and Doug is on-model in all three.

VERDICT: PASS (A PASS, B PASS, C PASS)

### A: "THE SPARE": PASS
1. **Fix 1 is done.** `thumbnail.json` has no `arrow` element, and there are no arrows or circles anywhere in the frame.
2. **Fix 2 is done.** Doug is now about 2x larger, alone on the right end of the nest with his feet on the rim. At 168x94 the red cap
   and white head stand out against the teal sky. The empty gap between him and the big chick (which has the fish in its bill)
   tells the "spare" story without help. There are two clear focal points, the adult's pale stare and Doug, and nothing collides with
   the text.

### B: "EATS BABY CROCS": PASS
3. **Fix 3 is done.** The hatchling now has a clear crocodile silhouette: an olive body (separate from the tan bill), dark bands,
   splayed legs, a long snout and a tapering tail, plus a white rim. At 168x94 it reads as a croc in under a second. It is intact
   and there is no blood. It crosses the closed bill, so it reads as prey held crosswise, which matches the text.
- Advisory (not blocking): the snout points up and out rather than down as suggested, and only two legs show. Neither hurts readability.
  The round-1 advisory about the round, pigeon-like body still applies.

### C: "IT WAITS": PASS (unchanged from round 1)

All three variants are cleared for the packaging gate.
