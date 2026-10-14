# Visual review: 018-every-cassowary-reason

## Round 1: pre-render keyframes + thumbnail (2026-10-14)

Scope: contact sheets `build/contact/sheet_01..23.png` (s001-s265), spot-checked full keyframes s021, s084, s101,
s122, s135; `build/thumbnail.png`, `build/thumbnail_small.png`; alt B (`thumbnail_b.json`) at `/tmp/th/b.png` and
`/tmp/th/b_small.png`.

VERDICT: FAIL

Most of the episode reads well. Pictures match the narration, chapter bars and the death counter are consistent
(147 -> 154, and they step up on the right shots), text is spelled correctly and not cropped, and the drawings are
recognisable. The fixes below are small and specific.

### Required fixes

1. **s135 (art director / engine): Doug is off-model.** His body and limbs render white instead of black ink, and
   only on this shot. s133, s015 and s182 use the same pose/expression and render correctly. The shot JSON sets no
   `ink`, so this looks like an engine or rig bug. Fix it so Doug is drawn in normal black ink, then re-key s135.
2. **s122 (director): the three "male" cassowary icons float in mid-air** at y=560, well above the ground line
   (y~900), next to the right-hand tree. Either put them on the ground (y about 890, scale about 1.0, x 1400/1520/1640)
   or put them inside a thought bubble coming off the female, the way s118 does it.
3. **s101 (director): the "NO HOOKS" label touches the DOUG DEATHS counter box.** The label spans y 197-264 and the
   counter ends at y 196, with overlapping x. Move "NO HOOKS" down to y about 290 (or left to x about 1250 with the
   feather), so there is at least 30 px of clear space.
4. **s084 (director): the empty white disc reads as a blank or broken element** for the whole line. It is a pie
   that only gets filled in s085. Either fill it light grey with "110" centred in it (size 90, bold), or start s085's
   55% red wedge sweeping in at appear 0.8 of s084.
5. **s246-s253 (director): run of near-identical compositions.** s246, s247, s248, s250, s251, s252 and s253 are
   all "cassowary under a spotlight cone, centre-right", with only the label changing (s249 is the only break).
   s250-s253 are 4 in a row that are practically the same frame. Required changes:
   - s251 "the person had come to the bird": cut to a tight push-in on the bird's head/eye (camera zoom about 1.8
     on the head) with the two arrows. No people drawn; keep it sober.
   - s253 "Once to keep it": switch to a wide shot without the spotlight (a plain night forest), with the bird
     small and off-centre right, so s254's Doug + field guide lands on a new frame.
6. **s003-s007 (director): the hook opens with 5 almost identical wides** (Doug left, cassowary right, same trees,
   with the word changing). Keep s004 and s005. Change the other two:
   - s006: crop in tight on the fern with only the casque and eye showing over it.
   - s007: push in on Doug's confused face with the white sound arcs coming in from frame right, and the bird
     off-frame.
7. **Thumbnail A, also shot s001 (graphic designer): the foot reads as a severed leg**, a disembodied shin with a
   jagged black stump on the left edge. That is a mild gore read at feed size, and the "SAME TOE" claw is not
   singled out.
   - Extend the leg so it runs off the top-left edge of the frame (no visible feather "cut").
   - Add one thick red circle (width 8 or more) around the long inner-toe claw, so "SAME TOE" has an obvious
     referent.
   - Mirror the same change in s001 so the opening image still matches the thumbnail.

### Advisory (not blocking)

- s173: the "ROOTS" label points at bare ground. Either add a couple of root curves by the log or drop the label.
- s143: the scale is balanced while the right pan is empty. Tilt the beam toward the bird until s144 adds the rice.
- s255 -> s257/s263: a second "NO" appears on the left page of the field guide that wasn't there in s255. It works
  as the "still says no" payoff, but the change is abrupt. Consider having it appear on s263 (appear 0.5) instead
  of already being there in s257.
- s046: the "knock knock?" bubble tail is a long stray line. Shorten it so it ends at Doug's head.
- Thumbnail B (Archetype A 2x2): it is readable at 320 px, but the labels are a regular-weight font, while the style
  bible calls for bold comic labels. Make them bold. The bottom-right foot has the same "cut stump" look as item 7,
  so crop the leg at the tile's top edge. B has no Doug, which the archetype allows. B is a valid alternative once
  this is fixed.

### Policy check: PASS

- **Sober cards s240-s245:** plain black cards with white or grey text, no counter, no Doug, no drawings of the
  victims or the incidents ("HE STRUCK THE BIRD.", "HE HAD FALLEN."). They are respectful and contain no depicted
  violence. The return to the chapter on s246 is clean. OK.
- **Chicks (s128-s139, s194-s195, s205-s206, s248):** small, naturalistic striped chicks with no faces, no hearts
  and no baby-style framing. s205 ("hi friend?", Doug holding a chick) reads as the setup for the s208 death, not
  as cute. OK, not kid-coded.
- **Swallowed cap (s258-s262):** only the empty cap is picked up and swallowed. Doug is already a ghost, and there
  is no body, blood or innards. The cap-flower "PLANTED" payoff is a dark-humour dung joke, not nursery whimsy. OK.
- **Deaths (s070, s139, s159, s183-s184, s208, s230, s257):** all dust clouds, X-eyes and ghosts. There is no gore
  anywhere. The s217 paring knife is a size reference only, not pointed at anyone. OK.
- **Kid appeal:** palette, captions and humour are adult-coded throughout. OK.

### Thumbnail readability (feed size, 320x180)

- A: "SAME TOE" is crisp. The cassowary head (casque, blue, wattles) is instantly identifiable, and tiny Doug with
  his red cap is visible for scale. It complements the title without repeating any title word. The only problem is
  item 7 (the severed-leg read and no claw callout).
- B: all 4 labels are legible and the subjects are recognisable. The "RADIATOR" thermal bird is the weakest tile but
  still reads as a bird.

Re-screen needed for: s001, s006, s007, s084, s101, s122, s135, s251, s253, thumbnail A (and B if it is used).

## Round 2: re-screen of round-1 fixes (2026-10-14)

VERDICT: PASS

Re-checked the keyframes s001, s006, s007, s084, s101, s122, s135, s251 and s253 (plus s252 and s254 for the run
context), thumbnail A and thumbnail B at full size and at 320x180.

1. s135: fixed. Doug is drawn in normal black ink and is on-model (red cap, white head), with the same look as s133.
2. s122: fixed. The three males stand on the ground line at the right, so nothing floats.
3. s101: fixed. "NO HOOKS" sits about 70 px below the counter, so it is clear of the counter and of the feather.
4. s084: fixed. The disc is light grey with a bold "110" in it, so it reads as a total and not as a blank element.
5. s251 and s253: fixed. s251 is a tight shot of the head and eye with the two arrows, and no people are drawn.
   s253 is a wide night forest with no spotlight and a small bird off-centre right. The spotlight run is broken,
   and s254 lands on a new frame.
6. s006 and s007: fixed. s006 is a tight shot of the fern with only the casque and eye showing over it. s007 is a
   push-in on Doug's confused face with white sound arcs coming in from the right. The hook no longer has 5
   identical wides.
7. Thumbnail A and s001: fixed. The leg runs off the top edge, so there is no stump or severed read. A thick red
   ring marks the inner-toe claw, so "SAME TOE" has an obvious referent. s001 matches the thumbnail. At 320 px the
   text, the bird head, the ringed claw and tiny Doug in his red cap all read.
   Thumbnail B: fixed. The labels are bold, and the foot tile crops the leg at the tile's top edge, with the claw
   ringed. All 4 tiles read at 320 px. Either thumbnail is OK to use.

### Advisory (not blocking)

- s251: the "CAME TO THE BIRD" caption crosses the bird's neck and wattle. It is legible thanks to its outline, but
  it would be cleaner moved up to y about 200 in the empty dark area at upper left (director).
