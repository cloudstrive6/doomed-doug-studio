# Decisions: 042-anaconda-no-venom

## 2026-11-09: script gate (draft 3): APPROVED
Creative director. Read script.md (draft 3), script_review.md (draft 3 PASS) and facts.md against brief.md.
- Opening meets the retention rules: sentence 1 has a number, a stake and the title promise ("kills without venom"). The payoff promise lands by about 0:10, "The Female." comes at words 34-35, and the twist arrives at word 133.
- Axis and bands (Watched/Bitten/Squeezed/Swallowed/Kept) match the brief. Nine items, boss last, deaths 322 to 329, survivals at 3 and 8. Every gag is used once. The 010 and 027 callbacks are one line each, and nothing on the used-once list is reused.
- Title honesty: every item is a way the snake finds, holds, kills, swallows or outlasts prey without venom. The human-fatality line and card now match the sources ("very few, hard to verify"). Myths are debunked (jaw dislocation, suffocation). Boa studies are framed as "a close relative".
- Accepted deviations: jaguar and Fawcett lines cut as unsourced; the 2024 split framed as disputed (Reptile Database). Both are correct calls.
- Length is 2,072 words, about 10.6 min. No gore and no safety advice. The capybara is deadpan, and the tone is adult-coded.
- Notes passed to the director: make deaths 326 and 327 visually distinct (puffed cheeks plus thumbs-up, against eyes closed with a slow heart); keep The Breeding Ball and The Caiman under about 1:20 each; reuse the line-16 night-swamp frame at item 9; draw the 5.21 m van at about half the 9 m tape. The kicker "She has standards." lightly echoes 008's "some standards". That's acceptable, but retire the "standards" closer after this episode.

## 2026-11-09: package gate (thumbnails A/B/C + ranked titles) and art go-ahead
Creative director. Viewed build/thumbnail.png, thumbnail_b.png, thumbnail_c.png at full size and at feed size (320x180),
each with its paired title in metadata.json `packaging.variants`. No visual-screener report on the thumbnails exists yet.

### A: "Every Reason a 97.5 kg Anaconda Doesn't Need Venom to Kill" + NOT A LOG: CHANGES REQUIRED (would not click as is)
The idea is right and the text is good, but the drawing doesn't deliver it.
1. **Doug's hand reads as a raised middle finger.** At scale 0.6 the `thumbs_up` pose renders as one upright stroke on a
   fist, and at feed size it reads as flipping the bird. That's a brand and advertiser risk, so this blocks. Change the pose to
   something that can't be misread: hands on hips, or pointing down at the "log" with the arm angled 45 degrees. Or
   scale Doug to about 0.9 so the thumb is clearly sideways. Keep `hopeful`.
2. **The body reads as stacked crocodile backs or a layer cake, not one snake.** `anaconda_wrap_front` at 2.9 shows two
   parallel slabs, and the cut-off right end (about x 920-1050, y 230-300) has two dark blobs that read as a croc's eye
   bumps. After 027 (saltwater croc) the viewer will think "crocodile". Replace it with one long, low, slightly curved body
   (e.g. `green_anaconda` or `anaconda_coiled` scaled up so a single body arc spans about x 0-1000), with no dark blobs at its
   end.
3. **Put the body half-submerged.** Right now it sits on top of the water like a bench. Raise the waterline to about y 470 so
   the water cuts the body along its length. That's what makes "log" believable. Doug stays standing on the exposed back.
4. **The head reads as a frog with an orange beak.** At 2.8 the orange mouth plank and heavy-lidded eyes of
   `anaconda_eyes_water` make it a frog. Scale it to about 1.5, delete or darken the orange mouth line to olive/black, and
   make the eyes small with no lids or brows. The head must sit where the body enters the water (same snake), not as a
   separate animal in the corner.
Keep the orange background, the NOT A LOG text (size and position) and the red cap.

### B: "Why a 97.5 kg Green Anaconda Doesn't Need Venom to Kill" + IT SQUEEZES: APPROVED (yes, I'd click)
This is the strongest of the three. It reads instantly at feed size: snake, Doug in peril, crossed-out bottle, a two-word
claim, and no gore. The title gives the weight and "no venom", and the image gives the squeeze, so the two don't repeat each
other. No changes. If A is not fixed in time, promote B to primary (thumbnail.png / s001 opening image) and run A as a test
slot once fixed.

### C: "Every Reason the Green Anaconda Doesn't Need Venom to Kill" + TWO BUMPS: CHANGES REQUIRED (would not click as is)
1. **The creature reads as a cartoon frog and close to the Pepe-the-Frog meme face** (green dome head, heavy lids, wide
   orange "lip"). That's an advertiser and brand risk, and it breaks the brief's "no big cute snake eyes" rule. This blocks.
2. **The text contradicts the image.** "TWO BUMPS" works because only two bumps show, but the image shows a whole face.
   Show only two small eye bumps and two nostril bumps breaking the surface (each about 40-60 px), with small yellow eye
   glints and no brows, lids or mouth. Add a faint, long, dark-green silhouette under the water behind them, running off
   the right edge, so the size is the "second shock".
3. **Doug is walking on the water's surface.** The concept is barefoot wading. Lower him so the waterline cuts at his
   knees, and add a ripple ring at his legs. Keep the moon backlight, his `scared` face and the sweat drop.
Keep the TWO BUMPS text and the night palette.

### Titles
The ranked titles are fine. All three are honest to the script (no venom, the squeeze/circulatory arrest, the swallow). The
97.5 kg figure is sourced (Rivas 2000). No changes.

### Art overall: GO-AHEAD, CONDITIONAL (art_approved not recorded yet)
- Art director round 3 is PASS (all 43 assets, all round-2 keyframe fixes).
- The only blocking item from visual-screener keyframes round 2 was s068. I checked the re-render after 06a2ec8: it now
  reads as one snake (strike head from the splash, body trailing underwater to the bank). That's fine from my side.
- The screener has not re-screened s068 or screened any thumbnail. Under the gate rule I can't approve without a screener
  PASS. **Required before art_approved:** (1) fix A and C as above (or ship B as primary and drop or replace C);
  (2) visual-screener re-screen covering s068, s001 (the primary thumbnail as opening image) and all three thumbnails
  at feed size; on PASS, art is approved without another CD pass unless the screener raises new issues.
- Before the final render (editor): confirm the subtitle font draws "ú" in "Jesús" (s007, screener carry-over #8). It
  would be nice, but not required, to close the s066/s067/s069 jaw-to-capybara gap.
