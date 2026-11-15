# Visual review: 048-false-killer-whale-offer

## Round 1 (2026-11-15): keyframes + thumbnails (pre-render)

Looked at: `build/contact/sheet_01..16.png` (s001-s186 + endslate), full-res crops of s041, s043, s080, s129, s178,
`build/thumbnail.png`, `thumbnail_b.png`, `thumbnail_c.png` and the three `*_small.png` (168x94).

Overall the episode is in good shape. Doug is on-model all the way through (red cap, white head). The deliberate
cap-off in The Beach is fine. HUD continuity holds (deaths 362 -> 368, distance 1 KM -> 0 M), and the narrator's arm,
the FRIEND? notebook and the plate HUD gags all land. Every death is cartoon: X-eyes, a floating cap, a ghost Doug.
There is no blood and no gore. The hooked/tangled whale in s083-s084 is handled cleanly. The costumes and the office
party scene read as adult-coded comedy, not as a kids' show. No spelling errors found.

### Keyframes: VERDICT: FAIL

These are small, targeted fixes. Re-run `keyframes --shots` for the affected ids only.

1. **s170-s174: five near-identical shots in a row** (director, composition). All five have a navy background, the
   whale on the left at x=560, the tuna in the middle and the diver on the right at x=1560, at the same scale. This
   breaks the rule against runs of 4 or more. Change at least two of them:
   - **s171:** make it a close-up of the whale's open mouth and the released tuna, with the whale at scale ~1.1 and
     cropped at the left edge. Keep the "A COUPLE OF METERS" dimension line.
   - **s173:** change it to a reaction beat. Use a cream background with the diver/McSweeney large (scale ~0.9) and
     centred, and a red "!" above him. Leave the whale out of this shot.
2. **s178: Doug is drawn on top of the white split-screen divider** (director). His body disappears into the 8 px white
   line, so he looks impaled. Move Doug to x=1560 or x=1600, y=900 on the right panel, next to `stick_man_plain`. That
   panel is "one of us", so Doug belongs on that side. Alternatively, drop Doug from this shot.
3. **s041: same divider problem** (director). Doug is at x=960 on the divider line. Move him to x=1100 on the
   Cocos side, or to x=820 on the NZ side, and keep the shrug.
4. **s129: stray brown curve on the sand** (director). The element is `curve` with points
   [[200,760],[600,740],[1000,770]], colour `#8a6a3a`, `appear 0.5`. It reads as a glitch line. Delete it.
5. **s042, s043, s044: the "COCOS ISLAND" text runs past the signboard** (illustrator). "ISLAND" crosses the bottom
   edge of the board. Fix the `signboard` asset (or its text) so both lines sit inside the board. Make the board
   taller, or set the text one size smaller.
6. **s131 and s133: the key subject is missing** (director). The narration is "largest mass stranding" and "835
   animals ... 4 km along the shore", but the beach shown is empty apart from Doug. A viewer can't tell what
   happened. Add a long row of small false-killer-whale silhouettes lying on the sand at the waterline, at scale ~0.12
   in dark grey. Show them as clean, intact cartoon bodies with no damage, injury or gore. In s133, run them along
   the dashed 4 KM line.
7. **s158: the "1 INCH" label** (director). It is the only imperial unit in a metric episode, and the narration does
   not say it. Change it to "1 SECOND", which matches "hesitated for exactly as long as...".

Advisory (not blocking):
- s092 and s093 are nearly the same frame. They are acceptable because the second one adds the payoff word, but
  nudge the camera if editing allows.
- s128, s129, s138, s142 and s143 reuse the same sunset beach with Doug in the same spot. Fixes 4 and 6 add enough
  difference.

### Thumbnails: VERDICT: PASS

All three work at feed size (168x94). Each has one clear focal point, and Doug plus the whale and tuna read
instantly. All three match the title "False Killer Whales Hunt Like Orcas, Then Hand Us Their Kill" and the
McSweeney payoff in s171-s182, so none of them is misleading. There is no blood: the dark-red mouth interior in B
reads as a mouth, not a wound.

- **A ("IT'S A GIFT", primary):** strong. The whale holds the tuna out toward Doug, who is treading water. The text is
  bold and legible. At small size the word spacing tightens to "IT'SAGIFT", but it still reads.
- **B ("FOR ME?"):** works. Optional polish for the graphic designer: the whale's tail is cut at the right edge and
  leaves a blunt black stub (x~1270, y~390). Either shift the whale left by ~60 px so the flukes are in frame, or
  crop mid-body so the cut reads as intentional.
- **C ("30+ KG TUNA"):** the clearest at feed size. The tag is legible, the tuna dominates, and Doug is shocked.
  The claim "30+ KG" is accurate (34-45 kg per the sources).

Recommended A/B/C order is unchanged: A first.
