# 044-shoebill-spare-chick: decisions

## 2026-11-11, creative director: script gate (APPROVED)
- Read: script.md draft 3, facts.md draft 3, script_review.md (draft 3 PASS: facts 0 errors / 16 re-verified, hook 8, structure 7, voice 8,
  TTS PASS, policy PASS, 2,014 words, about 10.3 min).
- Opening: thumbnail A, then sentence 1 gives the height and the spare-chick stake. The payoff promise lands about 0:08, "The Lungfish." at about word 31,
  and "Here's the problem." about 0:28. Would click, would keep watching.
- Escalation (Fish, then Reptiles, then Family) ends on the most extreme item, the parents letting the spare die. That delivers the brief's
  title and alternates ("eats baby crocodiles" is sourced at item 6, "lets its own chick die" at item 9). Counter 336 to 343: 7 deaths, 2 survivals.
- Gore and kids: strikes cut to black, the hatchling is swallowed intact with no blood, siblicide is defined plainly and never shown, and the chick
  costume is grey and deadpan. The honesty line (it does not threaten people) and the conservation context (Vulnerable, pet trade only as a threat) are in.
- Applied screener R1 myself: sentence 1 "raises" changed to "hatches", so the hook no longer contradicts "raise only one" at the boss. The word count
  and the timing to "The Lungfish." are unchanged.
- Screener R2, for the director: in the Water Bucket pour shot the parent's eye and head stay on the eggs or the water, never on Doug.
  This protects the item 2 kicker. A stage comment has been added to script.md.
- Director: the regurgitation diagram at The First Egg stays a plain arrow labelled FOOD, with no visible food or fluid. The Spare shows no pecking and
  no injured chick, and the older chick is only a big grey shape.
- Series bible: the 044 row and the counter total (343) get added at final approval, as for 040-043.
SCRIPT: APPROVED

## 2026-11-11, creative director: thumbnail gate (A REVISE, B REVISE, C APPROVED)
- Read: build/thumbnail.png, thumbnail_b.png, thumbnail_c.png and their `_small` (168x94) versions, the three JSONs, metadata.json
  `packaging.variants`. `python -m studio package 044-shoebill-spare-chick check` prints OK. The visual screener's thumbnail round (post-render)
  has not run yet, so these verdicts are mine only; nothing ships until that round passes too.
- Title pairing: all three add to their title without repeating a word, and the video delivers all three claims (item 9 The Spare, item 6
  baby crocodiles, item 1 the lungfish wait). No gore, no cute chick, no pecking. Policy is clean.
- **Red arrow ruling:** style bible sec 2 "no red arrows" stands for 044 and from here on. The 040 A / 043 C arrows were one-off exceptions and
  are not precedent. In A the arrow also does nothing useful: it stops in empty air about 90 px above Doug's cap, THE SPARE already sits over him,
  and at 168x94 it is a 4 px red tick that competes with the cap (the only red that should be on the image). Remove it; fix the reading with size, not annotation.

**A. THE SPARE + "Why the Shoebill Hatches Two Chicks and Lets One Die" (`thumbnail.json`, also s001): REVISE.**
The parent's stare is the best face on the three images. At 168x94 the nest is mush: the two chicks are one grey blob, the fish is invisible
and Doug is a red dot, so the image sells "big bird" and not "two chicks, one fed, one spare", which is the whole click.
1. Delete the `arrow` element.
2. Give the nest scene more of the frame: move the parent left (x 400 -> about 330, keep scale 1.95; the cropped wing is fine) and scale the nest group
   up about 25%: nest 0.82 -> ~1.0, `shoebill_chick_big` 0.78 -> ~0.95, `silver_fish` 0.42 -> ~0.55, Doug + `shoebill_chick_costume` 0.42 -> ~0.52.
   Keep the big chick clearly bigger than Doug, the fish clearly in the big chick's bill, and a visible empty gap between the chick and Doug.
3. Doug's cap sits directly under the R/E of SPARE (no arrow needed). If the text has to shrink to make room, 125 -> ~110, no smaller.
4. Re-render, check the small version: two separate chick shapes, the fish, and Doug's face + cap must each be readable at 168x94. Re-render s001 from the new A.

**B. EATS BABY CROCS + "Why the Shoebill Is the Creepiest Bird on Earth" (`thumbnail_test_b.json`): REVISE.**
At 168x94 the bird reads as a pigeon (small head, big round body) and the hatchling reads as a stick laid across its bill. The words make a
promise the picture doesn't show.
1. Crop to the head: scale `shoebill_side` up (1.9 -> ~2.4) and shift it down/left so the head, eye and bill fill the left half and the round
   body is mostly out of frame. Make the eye bigger or at least keep it fully in frame; it is the creepy part.
2. Make the hatchling read as a crocodile: darker olive-green body against the orange, a white rim (6 px) instead of the black one, scale ~1.6,
   and rotate so the snout, eye and two legs show clearly above the bill (about -55 to -60 instead of -75). Keep it whole: no blood, no bite marks.
3. Doug, reeds and text are fine; keep them.

**C. IT WAITS + "Every Reason the Shoebill Is the Creepiest Bird Alive" (`thumbnail_test_c.json`): APPROVED as is.**
The best read of the three at 168x94: one eye, one enormous bill, the hook tip hanging over Doug's cap, two big words. I would click it.
No changes. (If the analyst later sees C win Test & compare, the hero-profile-plus-bill layout becomes the default for single-animal episodes.)

Back to the graphic designer for A and B, then `package check`, then the visual screener's thumbnail round. A and B come back to me only if the
fixes change the concept; a cosmetic pass with the screener's PASS is enough.
THUMBNAILS: A REVISE, B REVISE, C APPROVED
- 2026-11-11 showrunner: script 3 rounds (2 FAIL fact/structure), art assets 1 round (+chick redraw), keyframes 2 rounds, thumbnails 2 rounds (A/B revised, red arrow removed per bible). Risks: kid appeal of baby-bird ending, siblicide wording must stay 'let die'; title omits 'Doug' (no-Doug test, exclude from comparison); thumbnail A is also opening image.
