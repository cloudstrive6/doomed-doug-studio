# 054-cape-buffalo-black-death: visual review

## Round 1: keyframes (2026-11-21, visual screener)

Scope: all 18 contact sheets (`build/contact/sheet_01..18.png`, s001-s209 + endslate) against the narration in
`shotlist.json`. Suspect tiles were rechecked at 1920x1080 in `build/keyframes/` (s001, s010, s013, s029, s056,
s078, s085, s087, s091, s098, s113, s133, s134, s141, s148, s154, s172, s186, s197, s204).

VERDICT: FAIL

The episode is in good shape overall. Doug is on-model and readable in almost every shot. The HUD death counter
steps correctly: 397 at s023, 398 at s091, 399 at s112, 400 at s134, 401 at s178, 402 at s203. Spelling is clean,
and the chapter cards and death cards are consistent. Nothing is gory or kids-show in tone: deaths are shown as a
cap only, a ghost, or X eyes. "DRINKS: BLOOD" (s055) is text only, the s063 "DOUG" juice box is a dry gag, and the
red X over cattle in s126 is a cartoon tally. The red glow behind the silhouettes in s091 and s113 follows the art
bible and stops at the ground line, so it does not read as blood.

Nine fixes block the keyframes. They are listed below.

### Blocking fixes

1. **s010 (director): overlapping text.** The green `BLACK DEATH` caption runs into the book's top-right corner,
   and the `RANKING` label sits on top of the last letters, so it reads "BLACK DEAT". Move `BLACK DEATH` up into
   clear space (y about 200, centred over x 380-1300, above the book). Move `RANKING` down to sit directly above the
   clipboard (about y 420) so that nothing overlaps.
2. **s134 (illustrator + director): Doug is off-model in a death shot.** The lying costume has a cow head with X
   eyes, and the red cap floats in the middle of the body. Doug's own white head is gone, so this reads as "a dead
   cow", not Doug. In s131-s133 his white head and cap show above the costume. Keep that here: Doug's white head
   with X eyes and the cap on his head at the costume's neck end, plus the costume ears. Drop the pink-snout cow
   face. s135 reuses the same body, so update it too.
3. **s078 (director): the label is cut by a reed stem.** A dark reed stem is drawn over `ONE ARM'S LENGTH` and
   splits it into "LE|NGTH". Draw the label after the reed stems (z-order), or move it to a gap between stems.
4. **s141 (illustrator/director): broken composition.** A third lion is hidden behind the buffalo wall, and only its
   legs and tail stick out under the herd (about x 1010-1160, y 800-880). It looks like a glitch. The beat ("lions
   catch one, the herd comes back to drive them off") is also muddled: one lion is pressed into the caught
   buffalo's rear and the other is head-to-head with it. Remove the hidden lion. Put two lions on the caught
   buffalo with a clear gap between them and the herd. Keep the red arrow running from the herd toward the lions.
5. **s148 (director): Doug is buried in the herd.** He is wedged against the right edge of the buffalo wall
   (about x 1790-1840), and a horn tip crosses his cap and face. Shift the herd left about 150 px and place Doug in
   open ground at x about 1800, y about 960, as in s149 and s150.
6. **s154 (director): Doug is hidden on his "Doug is fine" beat.** Only the cap peak and the top of his eyes show
   between the seat back and the windscreen. Raise him so that his whole head and face clear the door line, as in
   s155. The narration is about him being safe, so the viewer has to see him.
7. **s029 (director): the arrow points at the wrong thing.** The red arrow starts on Doug's face (the line crosses
   his head) and ends on the third head's nose or cheek. The narration is about the horn bases meeting in the
   middle, so aim the arrowhead at the fused boss (about x 1480, y 440). Start the arrow beside Doug's raised hand,
   not on his head.
8. **s085 (director): text is hidden behind the red X.** The X strokes cover the middle of both words, so the
   bubbles read "AMBU_ PLAN" and "GR__GE". Viewers need to read the claim before they see it rejected. Shrink the X
   to about 60% and offset it so it covers the bubble's right edge. Better still, replace it with a single red
   strike-through line across each word.
9. **Variety (director): three runs of near-identical frames, 4 or more each.**
   - **s019-s022:** the same wide shot of Doug with a camera and the bull asleep in the mud, four times. Change
     s020 ("Doug did not agree to this") to a close-up of Doug's face with an unhappy or deadpan look, or a tight
     shot of the bull's half-open eye.
   - **s041-s044:** the same tree, the same lying bull and Doug on the branch, four times. Only the calendar and
     the small book change. Make s042 or s043 a close-up, for example Doug and the DAY calendar on the branch in a
     tight shot, or the chewing bull's face from below.
   - **s064-s069:** the same row of resting buffalo, the BUFFALO sign and Doug lying flat, six times. Make s066
     ("checked him from his boots to his cap") a close-up of the oxpecker on Doug's cap, with Doug's eyes turned up
     at it. Make s068 ("Doug is fine") a tighter framing on Doug and the field guide.

### Nits (non-blocking, fix if touching the shot anyway)

- s001: the `BLACK` outline touches the left frame edge (x 0). Nudge the caption block 30-40 px right and down so
  it sits inside the title-safe area.
- s013: the bottom edge of `RETIRED` touches the picture frame. Move it down about 25 px.
- s087: `REEDS HIDE THEM` runs to the right page margin of the open book (there is no padding at x 1072). Drop the
  font 2-3 pt.
- s183 and s186: the green captions sit over the top of the dust cloud. They are still legible thanks to the dark
  outline, but moving them up 40 px would clear the cloud.
- s056-s058: Doug's head touches the base of the left fence post. Move him about 60 px left, into the open ground
  between the cow and the fence.
- s175 and s176: the leftmost buffalo's horn tip touches Doug's face. Shift Doug about 40 px left.
- s197: the rear lion's back legs and tail overlap the edge of the herd, so it looks attached. Move both lions
  about 120 px left.
- s098 and s099: the white dashed "stare" lines are thin and faint against the pale sky. Make them 2 px thicker or
  red, and make sure each one starts at the standing cow.

### Checked and fine

- Doug: red cap, white head, readable against every background, including the dark death cards. The ghost Doug
  (s024, s135, s179, s206-s209) and the cow costume in s131-s133 read clearly.
- The drawings are recognisable: buffalo (side, front and lying), the boss progression, oxpeckers, the cattle and
  Friesian, the lions, the safari vehicle, the maps (Kruger, Lake Manyara, Botswana, KwaZulu-Natal), the upright
  piano and the megaherd with its dust cloud.
- Pacing and the payoff: s198-s206 pay off the s003 promise (a thousand buffalo, the lion runs, Doug does not). The
  endslate is clean and has no "???" teaser card.
