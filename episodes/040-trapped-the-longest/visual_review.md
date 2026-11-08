# Visual review: 040-trapped-the-longest

## Round 1: keyframes (2026-11-08)
Scope: 17 contact sheets, s001-s202 + endslate. s001 skipped (thumbnail pending).

VERDICT: FAIL

Overall: strong episode. Doug on-model throughout (red cap, white head, readable on every background,
hard-hat and mammoth/amoeba costumes keep the cap). Real deaths are handled soberly: Nutty Putty is shown
only as a cave diagram and plain title cards, Ötzi's and Hoyo Negro's remains are never drawn (no human
skull/skeleton anywhere), no gore. Cartoon Doug deaths only. Tone is adult, not kids-show. HUD, chapter
tags and labels legible and spelled right; nothing cropped. Fixes below are clarity and variety issues.

### Required fixes
1. **s050** (director + illustrator): the picture doesn't match "the suitcase stays empty". It reads as a
   gloved hand over a wooden drawer holding a tape roll. Change: show the suitcase lid open/side with an
   empty sticker slot, and the narrator hand putting the "SNOWBOUND CAR" sticker back (or a sticker with a red X).
   The idea should be clear in 1 second.
2. **s051** (director): "walked out" shows only a floating cap above the drift, which reads like
   Doug died, the opposite of the beat. Change: draw Doug (walk pose, cap on) striding out of the drift
   toward the right with the suitcase. Remove the lone cap.
3. **s117-s120** (director): 4 consecutive near-identical shots (petri dish centre, Doug right,
   one label). Change: recompose at least s118 and s120. Suggested: s118 close-up of the worm in the dish
   filling the frame; s120 a family-tree/stack of dishes labelled "100+ GENERATIONS".
4. **s188-s192** (director): 5 consecutive near-identical dark dish shots (also follows s173-s175).
   Change: recompose s189 (close-up of food falling onto microbes) and s191 ("NOT DEAD": e.g. Doug's
   shocked close-up or a crossed-out tombstone-free "DEAD" stamp). Keep s190/s192 as is.
5. **s006-s014** (director): same cave cross-section 8 times in 9 shots. Change: make s011 ("Here's the
   problem") a tight zoom on the downward crack, and s008-style cutaway for s013 (squeeze close-up showing
   uphill/head-down, still no figure), so the run breaks up.
6. **s006 and s149** (director): the red chapter wordart sits on top of the drawing (cave branches on s006,
   the bone-grid on s149) and is harder to read than other title cards. Change: move the title up into the
   sky band (s006 y≈170) / above the dig frame (s149 y≈300), or shrink the drawing.
7. **s088/s089** (illustrator): the silhouettes don't read as the narration. The left one reads as an
   elephant/walrus, not a ground sloth; the middle one reads as a tortoise, not a sabre-toothed cat. Change:
   give the cat visible sabre fangs + long tail + cat ears, and give the sloth an upright/claws posture with no trunk.
8. **s145** (illustrator/art director): "Specimen 313" Doug-amoeba has no red cap, so Doug isn't
   readable in the death beat. Change: add the red cap to `amoeba_costume_flat` (as in s144).
9. **s201** (director): the red "room" highlight box overlaps the SOUTH PACIFIC GYRE sticker. Change: draw
   one box only around the empty space to the right of the gyre sticker (drop the rect at x=865).

### Advisory (non-blocking)
- s164: four `mammoth_pelvis` drawings at small scale read a bit like horned animal skulls. Consider a
  small "PELVIS" label or scaling one up.
- s057: "5,300 YEARS" touches the struck-through "RECENT?"; nudge down ~30 px.
- s036: the crossed plate ("no food") is small and ambiguous; enlarge or add "NO FOOD".
- s147: chapter tag still reads THE PERMAFROST VIRUS over a mammoth image (transition shot); OK if intended.
- Contact-sheet captions drop the "Ö" in "Ötzi" (s054, s187). On-screen art is fine; editor should confirm
  the subtitle/Shorts caption font renders Ö.
