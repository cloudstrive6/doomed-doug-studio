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

## Round 2: keyframes (2026-11-09)
Scope: 4 contact sheets of the 39 re-rendered keyframes (s006-s014, s022, s031, s036, s050, s051, s054, s057, s081,
s087-s089, s117-s121, s127, s145-s147, s149, s164, s188-s192, s197, s200-s202), checked against round 1 fixes.

VERDICT: FAIL (one illustrator fix left; everything else passes)

Round 1 fixes checked:
1. s050: fixed. Suitcase with an empty "?" slot, an arrow to the SNOWBOUND CAR sticker with a red X, and the narrator hand. Reads in 1 s.
2. s051: fixed. Doug (cap on, smiling) walks out of the drift with the suitcase, footprints behind him. No lone cap.
3. s117-s120: fixed. s118 is a full-frame worm close-up and s120 a dish family tree labelled "100+ GENERATIONS". s121 (fridge -80°C, curled worm, DRY FIRST) is clear too.
4. s188-s192: fixed. s189 is the food-falling close-up and s191 a big shocked-Doug close-up with NOT over a struck-through DEAD. The run now alternates.
5. s006-s014: fixed. The s011 and s013 push-ins (DEAD END / HEAD-DOWN + UPHILL) break up the cross-section run.
6. s006/s149 titles (plus s031, s054, s127): fixed. Titles now sit in the sky band or above the drawing and are fully legible.
7. s088/s089: partly fixed. The ground sloth now reads (upright, hooked claws, no trunk) and the gomphothere reads as an
   elephant relative. **The sabre-toothed cat still reads as a walrus** (see below).
8. s145: fixed. The red cap is on the amoeba in the eyepiece and SPECIMEN 313 is legible. s146 matches.
9. s201: fixed. There is one red box only, in the empty space right of the gyre sticker.

Advisories from round 1: s036 plate enlarged (OK), s057 "5,300 YEARS" clear of RECENT? (OK), s164 single pelvis + PELVIS label
(OK), s081 arrow ends on a red glow spot with no skeleton drawn (sober, OK), s147 topbar dropped (OK). s197 T. rex silhouette
now reads against the red glow; ghost Doug and the fallen cap are clear. s022 upturned boots + cap at the passage mouth is a clean cartoon death.
No gore and no kids-show tone. HUD and labels are legible and spelled right throughout.

### Required fixes
1. **s087, s088, s089: `smilodon_body`** (illustrator): the head is a blunt rounded dome with no muzzle and no visible ears.
   The two fangs hang straight down from the front of it, which is the walrus-tusk silhouette. s087 ("She wasn't
   alone") shows it alone with no narration naming it, so viewers will read "walrus". Change: add two clear pointed
   cat ears on top of the skull, and give it a longer, lower cat muzzle with an open-jaw notch so the sabres come out of the
   upper jaw behind the nose tip. Make the legs slimmer, with the front legs slightly forward (stalking stance). Keep the bobtail and the red rim.
   Re-render s087-s089 only.

### Advisory (non-blocking)
- s011/s013: the zoomed cave branch runs behind the TIME TRAPPED label and the chapter tag (s013). Both are in white boxes and
  still legible, so this is fine as is.
- s200-s202: Doug is `cap_off` with the cap beside the suitcase, as the art review asked. That's OK for the final death-count beat. He is
  still recognisable from the red cap in frame.
- The contact-sheet caption still drops the "Ö" in "Ötzi" (s054). The editor should confirm that subtitles and Shorts captions render Ö.

---

## Round 3 spot check (visual screener, 2026-11-09): VERDICT: PASS

Viewed at full size: `build/keyframes/s022.png`, `s087.png`, `s088.png`, `s089.png`. I also looked at a 3x crop of the s087 head and a 320 px feed-size version.

1. s087-s089 `smilodon_body`: fixed. It now has two pointed cat ears, a lower muzzle with a red open-jaw notch, and the sabres
   come out of the upper jaw behind the nose. It has a long, low body with four separate legs in a stalking stance and a bobtail.
   The walrus read is gone, and at 320 px it still reads as a fanged cat. s087 ("She wasn't alone") works without a label. In s088
   and s089 the cat, the upright clawed sloth and the gomphothere are three distinct silhouettes. "26+ ANIMALS" in s089 is legible and
   does not overlap any drawing. Doug is on-model (red cap, white head) in all three shots.
2. s022: clean. The clipboard paper is fully white with the wavy line and ONE MORE PASSAGE, and there are no red drops or marks
   outside the text. The upturned boots, the cap at the passage mouth and the suitcase make a clean cartoon death with no gore.
   The HUD and title are legible.

Advisory (non-blocking): the smilodon's muzzle tip is still a little blunt. The ears and legs carry the read, so no change is needed.
