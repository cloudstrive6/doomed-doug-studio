# 038 visual review (visual screener)

## Round 1: keyframes + thumbnails (2026-11-05)

Checked: contact sheets 01-16 (all 184 shots + endslate). I reviewed them after the 18:20 keyframe re-render, so the
redrawn deer are included. I also checked full-size crops of s089, s099 and s111, plus thumbnail.png, thumbnail_b.png and
thumbnail_c.png and their 168x94 `_small` versions.

| Item | Verdict |
|---|---|
| Keyframes | **FAIL** (3 required fixes, all small) |
| Thumb A (`thumbnail.png`, hero) | **PASS** (advisories) |
| Thumb B (`thumbnail_b.png`, Doug in peril) | **PASS** (advisories) |
| Thumb C (`thumbnail_c.png`, grid) | **FAIL** (1 required fix) |

**VERDICT: FAIL** (keyframes fixes 1-3 and thumbnail C fix 4. No gore, kid-appeal or off-model problems anywhere.)

### What passes
- **Gore/violence:** none. Every death is the field-guide card plus ghost Doug with X eyes (s026, s069, s092, s114, s133,
  s156, s180) or the floating cap gag (s070, s182-s184). The predators never touch prey on screen. The sunburn beat (s024-s028) is cartoon only.
- **Doug:** on-model in every shot. The red cap is always visible, the head is white, the ink is white on dark swamp/night/death cards,
  and he stays readable inside all the costumes (gorilla, whale, deer, squirrel, bird, turtle, hatchling).
- **Deer (AD fix 1):** the re-rendered s072-s093 deer now have sideways ears and a longer head. They read as deer/does, not rabbits.
- **Text:** the caption bar, DOUG DEATHS counter (294 → 301) and TIME LEFT tag are present, spelled right and inside the frame on every
  segment shot. I found no cropped wordart.
- **Kid-appeal:** acceptable. The cute animals (squirrel, songbird, hatchlings) sit inside adult framing (inbreeding, "hi friend?",
  deaths). There is no nursery tone.
- **Opening (s001-s012):** the hook pictures match the narration. s003/s004 now read clearly (bigger Doug + glow).

### Required fixes: keyframes
1. **s099, text overlapping a drawing (director).** The "ON PURPOSE" label box covers the left slope of the right-hand house roof
   (frame px ~1150-1300, y ~400-470). Move the label left so it clears the roof by at least 30 px (e.g. centre it
   at x ~1300 → ~1080, or put it under "$750" at y ~620 in the sky gap). Keep it off the car.
2. **s137-s141, run of 5 near-identical compositions (director).** Five consecutive shots use the same night beach, the same centred
   white hatchling in the nest and the same moon, with only a small overlay changing each time (arrow, dashed lines, volunteer, calendar). s148
   repeats it again. Break the run:
   - s139: push in on the nest (camera zoom ~1.8x on the hatchling) with the siblings' tracks leading to the water.
   - s140: make the volunteer the subject, kneeling large in the left third and looking into the nest, with the hatchling in the foreground.
   - s141: a calendar close-up, with "-2 DAYS" big (size ≥ 60) as the key subject and the hatchling small beside it.
3. **s037, the key subject doesn't read (illustrator/director).** "THE CALVES" points at a solid black whale shape with a blue glow.
   At a glance this reads as an orca, or as the attacker, not as a humpback calf. Draw the calf as a small humpback (same
   white_humpback shape at ~0.35 scale, or a grey-toned calf), tuck it under the adult's flipper, and aim the arrow at it. Keep the two
   orca fins on the surface as the threat.

### Advisory: keyframes (non-blocking)
- s089-s091 deer costume: the ears are fixed, but the hood still has no deer-only cue, so the white hood with big ears is still a little bunny-ish.
  Two short antler nubs or a dark nose tip on the hood would settle it (illustrator).
- s042: the "5 PITCHES" icon is an American football, but the narration and the Australian setting mean soccer pitches. Use a soccer ball or a
  small pitch rectangle (illustrator/director).
- s113: the long lead runs off to the bottom edge and doesn't reach Doug, so the "very long lead" gag doesn't land. Run the lead from the cat to
  Doug's ankle (director).
- s172: the crossed-out dark ellipse ("OUTSIDE A ZOO") doesn't say what it is. Use the s173 glass tank icon with an X, or a small grown-alligator
  silhouette with an X (director).
- s176-s179: the broken eggshell reads like a paper crown/boat at a glance. A yellowed shell edge or one shell fragment on the bank would help
  (illustrator).
- s145: the "FISH" are dark ovals that read as shadows. Use the s163 fish asset (director).
- s120: the label "39% THICKER" vs the spoken "about forty percent". The match is fine, but "~40% THICKER" mirrors the voice.

### Thumb A (`thumbnail.png`): PASS
At 168x94 there is one clear focal point (the white alligator jaw with its pink eye), and Doug in his hatchling costume with the red cap is readable bottom-left.
"NO HIDING" is legible, and the black-green swamp gives strong contrast. It fits the title ("...Kills Albino Animals First, Then Doug").
Advisories (graphic designer):
- The heron in the top-left corner is cropped to a black and red hook. At feed size it reads as an abstract claw/blade, not a heron. Either
  show more of the head and beak (move it ~80 px down and right so the eye and beak tip are clearly a bird's), or drop it.
  The alligator already carries the threat.
- "NO HIDING" sits ~10 px from the bottom edge (baseline y 662, size 104), where the watched-progress bar draws.
  Raise it to y ~630.

### Thumb B (`thumbnail_b.png`): PASS
This is the strongest feed read. "SPOTTED" is big and clear, the heron beak points straight at Doug, Doug is large, shocked and in his cap, and the
ripples and glow isolate him. There is one focal story at 168x94.
Advisories (graphic designer):
- At 168x94 the dark hatchling at right (alligator_hatchling, x 980) reads as a striped caterpillar/bee. Either scale it up ~1.4x and
  put it partly in the water, or remove it. The point "the white one is the one that gets seen" still lands through the glow.

### Thumb C (`thumbnail_c.png`): FAIL
4. **Top-right panel reads as a polar bear (graphic designer).** The white_lioness_face bust has round ears, a blunt muzzle and no mane, on a
   flat red field. At 168x94 it is a white bear. A polar bear is a naturally white animal, so in an "albino animals"
   grid it undercuts the premise and mis-signals the topic. Replace it with the full-body white_lioness on a savanna gold
   ground (as in s049), or swap in a clearer subject (white_humpback breaching on blue, or the white deer). Also scale Doug up in
   the bottom-right panel (currently ~12 px tall at feed size) so the cap is a clear red dot. Push him to ~1.3x his current scale and crop the
   jaw rather than Doug.
Everything else in C is fine. The gorilla, squirrel (the tail reads as a squirrel) and gator+Doug panels are clear, the colour fields
separate the panels, and the grid has no text, as the brief asks.
