# 047 Wolverine Snow Climb: Visual Review

## Round 7: post-render (final.mp4, thumbnails, Shorts) (2026-11-14)

Scope: all 24 `build/samples/f_*.png` (every 30 s, 707 s total), `build/qc.json` (no problems), thumbnails A/B/C and
their `_small` versions, `metadata.json` (title "Why a 16 kg Wolverine Can Kill a Reindeer Six Times Heavier"), the
three `build/shorts/*_preview.png`, and 6-10 frames extracted from each short (1080x1920; 48.4 s / 45.4 s / 36.7 s).
Nothing was rendered.

### Main video
- No black, blank, frozen or glitched frames in the samples. Each frame has a different composition, and the chapter
  tag steps through REINDEER, GLUTTON, FRIDGE, TRAPLINE, NOSE, RANGE, SNOWSHOES, SNOW DEN and CLIMB in order.
- The HUD counter climbs 356 -> 362, and altitude goes FOREST -> TREELINE -> SNOW -> SUMMIT. Both are always legible.
- Doug is on-model wherever he appears (red cap, white head), and that includes the reindeer costume (f_003). The
  wolverine reads at once in every frame. Carcasses are pale cartoon shapes with no blood. There is no gore and nothing
  looks like a kids' show.
- The end screen (f_024) has the standard blank end-screen slots, the SUBSCRIBE circle and "DOUG'S NEXT DEATH". It ends
  cleanly.
- The Round 2 advisory A4 is still visible in the render: in f_019, the altitude stake sits on the den entrance. This
  is cosmetic and does not block.

### Thumbnails
- **A** (live, IT DOESN'T SINK): the caption is readable at 168 px, the wolverine stands on the crust and the reindeer is
  sunk. It explains the title (why the small animal wins) and is not misleading. Advisory: at feed size the sunk Doug is
  only a red dot, and the reindeer is bigger than the wolverine, so it pulls the eye. If the designer revisits this,
  scale the wolverine up about 15%.
- **B** (IT CLIMBS): the strongest at feed size. It has one focal point, a terrified Doug, and an obvious threat.
- **C** (200,000 / PER LITTER): readable at 168 px and fits alt title 3. Doug in the costume is small but recognisable.

### Shorts
- In all three, the title (red, 3 lines) is fully inside the frame. Subtitles are large and high-contrast, and the
  @DoomedDoug tag is clear. Drawings are not cut at the sides (side labels such as FOUR and DIDN'T STOP sit at about
  x 20 px or more, which is safe).
- **short01**: pays off its title on screen (90 MINUTES stopwatch, 4x stacked towers for 1,500 m, the wolverine over the
  summit, DIDN'T STOP).
- **short02**: has the 800 KM map, the I-80 crossing, a NEW YORK TO DETROIT comparison and Doug with the snacks.
- **short03**: has the carcass buried under snow, the wolverine on the surface, and a dashed line showing it digging
  straight down to the carcass. The payoff is shown, not withheld.
- In all three, the end card reads FULL VIDEO: TAP BELOW and the red arrow points straight down. Doug is on-model and
  there is no "???" teaser.
- Advisory (editor): subtitles reveal letter by letter, so a paused frame can show half a word (the short02 preview
  reads "one of the bu"). That is fine in motion. Advisory (director, later episodes): the 16:9 artwork band makes Doug
  very small in the 9:16 frame (about 40 px tall in short02/short03). A tighter crop on Doug-centred shots would help
  retention.

No required fixes.

VERDICT (main): PASS
VERDICT (shorts): PASS

---

## Round 6: thumbnail C re-screen after the Round 5 fix (2026-11-14)

Scope: `build/thumbnail_c.png` and `thumbnail_c_small.png` (PNG 18:21:58Z, newer than `thumbnail_test_c.json` at
18:21:57Z) at 1x and at 4x nearest-neighbour from 168 px, plus a check that A and B were regenerated. The A and B PNGs
are dated 18:21:58Z, and their JSONs have not changed since 18:20:02Z. Both look the same as the Round 5 PASS.

VERDICT: FAIL. A: PASS (unchanged), B: PASS (unchanged), C: FAIL (one geometric fix).

### C: "200,000 PER LITTER": FAIL
Round 5 fix 1 (size): DONE. At `size: 96` the digits are about 70 px tall, and the number is now the second read
after the wolverine. The wolverine is at 1.15 and the jaw string is still attached. The tag clears Doug by about
93 px and the snow line by 20 px. No gore, not kids-show tone, Doug on-model.

1. (graphic designer, `thumbnail_test_c.json`) The number no longer fits inside the tag. Measured:
   - The text spans x 663-1003. The tag's right outline sits at x 986-1000, so the last "0" runs into the outline.
     At 168 px the number reads "200,00|", which reads as if it were cut off.
   - The grommet ends at about x 665, so it touches the "2" (text starts at x 663).

   Change (I test-rendered this to /tmp and it is verified):
   - `price_tag`: `x 815, y 412, scale 4.0` (was 800 / 420 / 3.4).
   - "200,000": `x 858, y 416, size 92` (was 834 / 424 / 96).
   - Jaw-string curve: shift all three points by `y -8`, giving (640,402), (620.4,382), (650.4,412). The wolverine
     stays as it is.

   Measured result:
   - The text spans x 695-1020. That leaves about 25 px to the grommet and 15 px to the outline's inner edge
     (x 1035).
   - The tag spans y 302-527, which is 18 px above the snow line at 545.
   - The tag's outer edge is at x 1054, 43 px from Doug's cuff at x 1097. No tangents.
   - The tag tip still sits in the wolverine's jaw.
   - Digit height is about 67 px, and "200,000" reads in full at 168 px.

Advisory C1 (the stray red stroke behind the left antler at about x 1100-1110, y 335-345) is still present. It does
not block.

---

## Round 5: thumbnails A/B/C re-screen after creative-director revision (2026-11-14)

Scope: `build/thumbnail.png`, `thumbnail_b.png`, `thumbnail_c.png` (1280x720) and `_small` (168x94), viewed at
1x and 4x nearest-neighbour. The PNGs (18:20:23Z) are newer than `thumbnail.json`, `thumbnail_test_b.json` and
`thumbnail_test_c.json`, so they are current and I did not regenerate them. Thumb texts match `metadata.json`
`packaging.candidates` top 3. No gore, no kids-show tone, spelling correct, Doug on-model (red cap, white head) in all three.

VERDICT: FAIL. A: PASS, B: PASS, C: FAIL (one fix).

### A: "IT DOESN'T SINK": PASS
Unchanged from the Round 4 PASS. Wolverine on the crust, reindeer and Doug sunk, and it all reads at 168 px.
Advisories A1 (white costume rump blob at about x 640-700, y 340-420) and A2 ("K" of SINK ends at about x 1150,
y 665, close to the duration badge) still apply. They do not block.

### B: "IT CLIMBS": PASS
Doug is on the slope face, readable at 168 px (red cap plus screaming face under the wolverine), and nothing is
cut by an edge. One focal point: the wolverine on the summit. Advisory B1 (a climbing pose would sell "climbs"
better than the arms-up scream) still applies. It does not block.

### C: "200,000 PER LITTER": FAIL
Round 4 fixes:
- Fix 1, text "200,000" plus "PER LITTER": DONE in wording. "KR" is gone and the caption reads correctly with
  the "Sweden Pays" title. NOT DONE on size, see fix 1 below.
- Fix 2, tangents: FIXED. The tag's right outline (x 1042) is now 42 px from Doug's left cuff (x 1084). The tag's
  bottom (y 525) is 20 px above the snow line (y 545).

1. (graphic designer, `thumbnail_test_c.json`) "200,000" is too small. It is set at `size: 64`, which gives a
   measured cap height of about 46 px (digits y 419-465). Round 4 set a floor of about 70 px. At 168 px the number
   is about 6 px tall: barely legible at 1x and smaller than Doug's head. The number is the whole joke, so it has
   to be the second thing the eye reads after the wolverine. Change: raise the text to about `size: 96` (cap height
   about 70 px, which needs about 345 px of text width). Make room by shrinking the wolverine (`scale` 1.35 to about
   1.15, keeping the jaw string attached) and moving the tag left with it, then scale `price_tag` from 3.0 to about
   3.4 so the white area holds the number with at least 20 px padding. Keep the 30 px or more gap to Doug (x 1084)
   and keep the tag clear of the snow line.

Advisory (does not block):
- C1. (graphic designer) A small stray red stroke sits above and left of Doug's cap, behind the left antler (about
  x 1095-1105, y 333-342). It looks like a cap or hood artifact. Remove it if it is easy.

Re-screen C's full-size and `_small` files after fix 1. A and B are locked.

---

## Round 5: thumbnails C (and A caption) re-screen (2026-11-14)

Scope: re-rendered `build/thumbnail_c.png` and `thumbnail_c_small.png`, plus `thumbnail.png` and
`thumbnail_small.png` after the caption nudge. Both were viewed at full size and at 4x nearest-neighbour from 168 px.
B is unchanged and stays PASS.

VERDICT: PASS. A: PASS, B: PASS (unchanged), C: PASS.

### C: "200,000 PER LITTER": PASS
- Round 4 fix 1: FIXED. The tag reads "200,000" in bold black and is fully legible at full size. At 168 px it is
  small but readable. With "PER LITTER" and the title "Why Sweden Pays...", the price joke now lands, and it
  matches facts.md (SEK 200,000 per documented reproduction). It is not misleading.
- Round 4 fix 2: FIXED. The tag clears Doug's cuff by about 45 px and sits clearly above the snow line. There are
  no tangents left.
- Focal order (wolverine, then tag, then Doug) holds. Doug is on-model and fully in frame, with his antlers inside
  the right edge. There is no gore and no kid-appeal.
- Advisory C1 (graphic designer, optional): the string loop and the tag's point now cover most of the wolverine's
  face (no clear eye or nose), so at feed size the head is a dark mass. The striped body still identifies it.
  Pulling the loop down to the lower jaw, so the eye and nose show, would add menace.
- Advisory C2 (graphic designer, optional): the tail tip is about 10 px from the left edge. Shifting the whole
  wolverine about 20 px right would give it some air.

### A: caption nudge: PASS
The caption (now centred at about x 615, y 605) ends at about x 1145, y 660, which keeps it out of the duration
badge corner. It is still clean at 168 px. Nothing else changed, and Round 4 advisory A2 is resolved.

---

## Round 4: thumbnails A/B/C re-screen (2026-11-14)

Scope: `build/thumbnail.png`, `thumbnail_b.png`, `thumbnail_c.png` (1280x720) and their `_small` (168x94)
versions (also viewed at 4x nearest-neighbour), against `metadata.json` `packaging.candidates` top 3. No gore and no
kids-show tone in any of them. All text is spelled right and legible at 168 px. Doug is on-model in all three.

VERDICT: FAIL. A: PASS, B: PASS, C: FAIL (one fix).

### Round 3 fixes: status
1. A, reindeer scale: FIXED. The reindeer is now clearly bigger than the wolverine (its body is about 1.5x the
   wolverine's height), so "six times heavier" reads correctly.
2. A, reindeer cropped: FIXED. The head and antlers are fully in frame. The nose reaches about x 1245, not the
   x 1150 or less I asked for, but nothing is cut and it does not touch the edge, so I accept it.
3. A, sink contrast: FIXED. A white snow lip with grey crack lines now covers the reindeer's belly and Doug's chin.
   The blue puddle ellipses are gone, and the wolverine stands on the crust with a faint shadow under its paws. The
   on-top versus sunk contrast reads at 168 px.
4. A, antler tangle: FIXED. Doug's left costume antler tip (about x 620, y 250) is well clear of the snout (about
   x 565, y 350).
5. B, Doug position: FIXED in substance. Doug is on the slope face (head at about x 260, y 420, feet at about
   y 670), scaled up, and not cut by any edge. At 168 px the red cap and stick body read under the wolverine, so
   "Doug + threat" now works at feed size. He uses an arms-up scream pose, not the climbing grip I asked for (see
   advisory B1).
6. C, price on tag: NOT FIXED. The tag now reads only "KR", which is a currency code with no amount. Most viewers
   in the feed will not know what "KR" means, and with no number there is still no price joke. "KR PER LITTER"
   reads as a riddle, not a price. The 3-word cap does not force this: `thumb_word_count` counts "200,000" as one
   word, so "200,000" plus "PER LITTER" is exactly 3 words (see fix 1 below).
7. C, US-looking banknote: FIXED. It has been removed.
8. C, focal order: FIXED. The white tag is now the brightest thing in frame and Doug is smaller at the far right,
   so the eye goes wolverine, then tag, then Doug.

### C: "KR PER LITTER" / "Why Sweden Pays for the Wolverines That Kill Its Reindeer": FAIL
1. (graphic designer, via `python -m studio package 047-wolverine-snow-climb rank`) Change the thumbnail text to
   "200,000 PER LITTER": tag "200,000", caption "PER LITTER". That is 3 words and passes the gate. The title
   already says "Sweden Pays", so the number does not need "KR" to read as a payout (facts.md: SEK 200,000 per
   documented reproduction). Fit "200,000" on the tag in bold black at the current cap height or larger, shrinking
   the font or widening the tag a little if needed. Do not let it drop below about 70 px cap height at full size.
2. (graphic designer) Fix two tangents while the tag is being redrawn. The tag's right edge (about x 1060) touches
   Doug's left cuff (about x 1065), so leave at least 30 px between them, for example by moving Doug about 40 px
   right while keeping his right antler tip inside x 1250. The tag's bottom edge also sits right on the snow line
   (y about 545), so lift the tag about 20 px or let it clearly overlap the snow.

### Advisories (do not block)
- A1. A (graphic designer): the white rounded shape with the beige ear to the left of Doug's head (about x
  640-700, y 330-420) is the costume's rump or hood, but it reads as a stray white blob. Shade it brown like the
  costume, or tuck it behind the snow lip.
- A2. A (graphic designer): the "K" of "SINK" (about x 1080-1170, y 560-665) slightly enters YouTube's bottom-right
  duration badge area. Consider nudging the caption about 30 px left or up.
- B1. B (graphic designer): a climbing pose (one hand gripping the rock, feet braced on the slope) would sell
  "IT CLIMBS" better than the standing scream and remove the slight "standing in front of the mountain" look.
  Optional.

Re-screen C's full-size and `_small` files after fix 1 and fix 2. A and B can be locked.

---

## Round 3: thumbnails A/B/C at feed size (2026-11-14)

Scope: `build/thumbnail.png`, `thumbnail_b.png`, `thumbnail_c.png` (1280x720) and their `_small` (168x94)
versions, against the paired titles in `metadata.json` `packaging.variants`. No gore, no kids-show tone in any of
the three; text is spelled right and legible at 168 px in all three.

VERDICT: FAIL. A: FAIL, B: FAIL (one fix, closest to passing), C: FAIL.

### A: "IT DOESN'T SINK" / "Why a 16 kg Wolverine Can Kill a Reindeer Six Times Heavier": FAIL
The wolverine reads at feed size and the text is strong, but the picture contradicts the title.
1. (graphic designer) The reindeer is drawn about half the size of the wolverine, so the "six times heavier"
   claim is visually reversed (misleading). Scale the reindeer up so it is clearly bigger than the wolverine
   (body at least 1.5x the wolverine's height) and scale the wolverine down so both fit.
2. (graphic designer) The reindeer's head and antlers are cut off by the right edge. Bring it fully into frame
   (head at x 1150 or less).
3. (graphic designer) The sink contrast does not read: the reindeer and Doug sit on the snow line as if lying
   down, and the pale-blue ellipses read as water puddles or ice holes. Draw a white snow lip in front of the
   reindeer's belly and Doug's chest (snow overlapping their bodies), replace the blue ellipses with white snow
   rims with grey crack lines, and keep the wolverine's paws visibly on top of the crust (a little shadow under
   the paws only).
4. (graphic designer) Doug's left antler crosses into the wolverine's open mouth (about x 760, y 260), which
   makes a tangle at the focal point. Leave at least 40 px between Doug's antler tips and the snout.

### B: "IT CLIMBS" / "Why the Wolverine Is the Scariest Small Predator Alive": FAIL (one fix)
Best of the three: one clear focal point (wolverine on summit, teeth showing), bold orange, text clean at 168 px.
5. (graphic designer) Doug is jammed against the left edge (body about x 80-170, arms cut by the frame) and
   floats beside the slope rather than on it; at 168 px he is only a red speck, so "Doug + threat" fails at feed
   size. Move Doug onto the slope face at about x 260, y 540, scale him about 1.4x, use a climbing pose gripping
   the rock with feet on the slope, still looking up at the wolverine. Keep him clear of the bottom-right
   timestamp area (he is already well away from it).

### C: "PER LITTER" / "Why Sweden Pays for the Wolverines That Kill Its Reindeer": FAIL
6. (graphic designer) The price tag on the wolverine is blank, so the joke the whole concept rests on is missing
   and "PER LITTER" has nothing to attach to. Write the price on the tag in bold black, e.g. "200,000 KR"
   (facts.md: SEK 200,000 per documented reproduction), large enough to read at full size; rotate the tag
   less (about 20-30 deg) so the text is upright enough to read.
7. (graphic designer) The `banknote` reads as a US dollar bill (green, guilloche portrait), which is off-topic for
   Sweden. Give it a plain generic note with "KR" on it, or swap it for a cheque labelled "KR".
8. (graphic designer, advisory) Two focal points of equal weight (wolverine left, Doug right) split the eye at
   feed size. Once the tag has a price, make the tag the brightest thing in frame and let Doug sit a little
   smaller or further right so the eye goes wolverine -> tag -> Doug.

Pairing note: A-to-title fit improves most from fixes 1 and 3; B and C are on-concept once fixed. Re-screen all
three `_small` files after the changes.

---

## Round 2: pre-render keyframes re-screen (2026-11-14)

Scope: refreshed `build/contact/sheet_*.png` and the full-size `build/keyframes/` for the changed shots s006, s015,
s019, s040, s126, s127, s130, s131, s145, s146, s162, s175, s177, plus the neighbouring runs (s142-s147,
s169-s178). s001 skipped (thumbnail pending). I rendered s162's full 1920x2160 pan canvas and s175 without the
blackout (elements with appear < 0.6) to check the pan start and the pre-cut state.

**VERDICT: PASS**

### Round 1 required fixes: status
1. **s015**: FIXED. "200,000 KR" is fully legible and the string attaches at the tag's eyelet, clear of the text.
   A kit is now on the den pad with the tag tied to it (see advisory A1).
2. **s006**: FIXED. The wolverine (bottom centre-right) and Doug (far right) no longer touch.
3. **s040**: FIXED. "WIDE ENOUGH" sits in open sky, clear of both pine crowns.
4. **s162**: FIXED. On the pan start, `wolverine_climbing` sits on the left face and is unobstructed. The red
   arrow starts beside it and runs up the face to the snowcap. "STRAIGHT UP" is on the right in open sky.
5. **s143-s146 variety**: FIXED. s145 is now a close-up of the den chamber (WARM thermometer inside, Doug + COLD
   on the surface, COLD GROUND below). s146 is a surface view with the FEB - MAY calendar. Only s143/s144 share
   the same section, which is within the limit.
6. **s131**: FIXED. The divider starts below the "THE SNOWSHOES" tag.
7. **s019**: FIXED. The coloured wolverine with the pale side-stripe is used, so the threat reads at once.

Round 1 advisories also resolved: s126/s127/s130 reindeer are now sunk into the crust (with snow-clump rims in
s126/s127). s175 shows the wolverine going over the summit with the paw-print trail, a "OVER" arrow and Doug on
the face, and no cap on the summit. s177 is re-framed closer (big mountain, "363", cap + arrow, ghost Doug), which
breaks up the s176-s178 run.

No new blocking issues. Doug is on-model, the counter steps 362 -> 363 across the s175 cut, there is no gore, and
the tone is not a kids' show.

### Advisory (does not block; fix if time allows)
- A1. **s015** (illustrator): the kit is a solid black silhouette with a tail (ellipses at about 982,952 /
  1040,952), so at a glance it reads as a rat or a shadow, not a wolverine kit. If time allows, draw a pale
  grey-fluffy kit with shut-eye lines, or reuse `wolverine` at scale about 0.18 with closed eyes.
- A2. **s015** (director): the big red `question_mark` at 1660,600 sits on top of the right-hand pine, and Doug
  already has his own small "?". Drop it or move it into open sky above Doug (for example 1560,700).
- A3. **s130** (director): the two break-through crack marks still read as stray "< >" chevrons under the
  reindeer. Replace them with a snow splash or delete them. The sunk reindeer and the SINKS arrow carry the beat
  without them.
- A4. **s145** (director): the `altitude_stake` HUD tip lands right on the den's surface entrance (about x 1405),
  which clutters that spot. Consider moving the cutaway entrance a little left. A small grey triangle (distant
  peak) also pokes above the surface at about x 1000-1150 and looks like a stray shape.
- A5. **s177** (director): the line is "The cap made the summit", but the cap sits about a third of the way down the
  far slope. Moving `doug_cap` up to just over the peak (for example about 760,140, with the arrow re-aimed) would
  make the payoff literal.
- A6. **s162** (editor, check in render): the HUD (deaths label/stake) is in canvas coordinates at the top of
  the 2160 canvas, so it scrolls in during the pan-up rather than staying fixed. Make sure this looks
  intentional in the draft render.
- Round 1 advisories that were not touched (s012, s043/s053, s055, s008, s088) still apply as nice-to-haves.

---

## Round 1: pre-render keyframes (2026-11-14)

VERDICT: FAIL. 7 required fixes (s015, s006, s040, s162, s143-s146 variety, s131, s019) plus advisories. All
were addressed in round 2 (see above).
