# 056 King Cobra Snake Eater: visual review

## Round 1: pre-render (keyframes + thumbnails), 2026-11-23

Checked: `build/contact/sheet_01..19.png` (s001-s223 + endslate), full-res crops of `build/keyframes/` for suspect
shots, `build/thumbnail{,_b,_c}.png` and the `_small` versions, against `shotlist.json` and `metadata.json`.

**VERDICT: FAIL** (keyframes). Thumbnails pass (minor note 12).

What already works: Doug is on-model (red cap, white head) and readable in every shot he is in. The costume gag reads
(krait / rat snake / cardboard-hood cobra / python / king cobra suits). The death counter runs 408 to 414 with no
gaps (055 ended at 408). There is no gore: deaths are cut-aways, a ghost, the cap left behind, or Doug inside the
coils. Snakes are recognisable and kept distinct (banded krait vs common krait, Indian cobra hood vs king cobra).
Nothing reads as a kids' show. The ending pays off ticket 9 (s217-s219), there is no "???" teaser, and the endslate
is clean.

### Required fixes

1. **s078** (director): the king cobra's head is fully hidden behind the red "THE COBRA" title (checked at full
   res), so the chapter card has a headless snake. Move the title up to about y=300, or move/scale the
   `king_cobra` asset down so the head sits under the title with clear space.
2. **s077** (director): "VENOMOUS." is drawn across the Indian cobra's hood. Move the text to y of about 330, or
   push the cobra down/right so the hood is clear.
3. **s091** (director): "NATIONAL ZOO" text sits on the signboard's top frame and is half hidden by it. Move the
   text down into the board face (about y=640 at this scale), or shrink it to fit inside the board.
4. **s134 and s198** (director): the red SINGAPORE circle (x=760, y=820) is drawn *below* the map frame, on empty
   background, not on Singapore. Move it onto the southern tip of the Malay Peninsula inside the map (about
   x=790, y=740 at the current map scale) and keep the SINGAPORE label just under the map.
5. **s158** (illustrator/director): the "WETLAND RESERVE" newspaper photo shows a **monitor lizard** (the s133
   clipping reused). This beat is the king cobra eating a reticulated python. Swap the photo for a king cobra +
   python drawing (or the s161 photo-frame art at small scale).
6. **s052** (director): narration says "waving goodbye to someone he just met", but Doug is holding up his ticket
   and the bubble says "hi friend?". Use the `wave` pose (ticket in the other hand) and change the bubble to
   "bye friend?" so picture and line agree.
7. **s190** (director): green "NOT A SNAKE" text sits over the green tree canopy and is hard to read. Move it to the
   open sky between the cobra and the HUD (about x=1150, y=560) and drop the arrow start accordingly.
8. **s132** (illustrator/director): the radio-tag icon is a small dark ring floating on the navy night sky. It is
   unreadable and looks like a stray mark. Either attach it to the cobra's neck as a collar with a RADIO TAG label
   (as in s030) or delete it. Do the same in **s030**, where the tag floats above the snake: put it on the neck.
9. **Variety, s109-s118** (director): 10 consecutive shots use the same tree-left + branch-top + flat ground frame,
   and s115/s116/s117 are near-identical (upright cobra under the branch). Break the run. s110: close-up of the
   cobra's head gripping the viper behind its head (no branch). s113 or s116: plain cream info card (stopwatch +
   "10 MIN" / "30 MIN") instead of the forest set. s117: tight two-shot of the frozen cobra and puzzled Doug.
10. **Variety, s122-s125 and s186-s191** (director): s122-s125 are 4 near-identical Doug-with-clipboard-under-branch
    frames, and s186-s191 are 6 near-identical tree + mound + Doug frames. For s124 ("Doug is fine."), cut to a
    close-up of Doug's clipboard/face. For s188 ("Doug freezes"), use a close-up of Doug frozen with the rake
    and the cobra's head looming in from the top edge. For s191 ("Doug is fine."), use a wide shot with Doug
    walking off right, nest small.
11. **s041** (director): the dashed "serious ground" route runs off the west coast into the Arabian Sea. Redraw
    the points inside the Western Ghats (onshore, along the south-west coast strip near the s038 circle).

### Minor (fix if cheap)

12. **Thumbnail B** (graphic designer): at `_small` size the green pit viper on the cobra's head reads as a leaf.
    Scale the viper up about 1.5x and make the bite contact obvious (jaws clearly on the cobra's head, a darker
    outline), or give it a contrasting yellow lip. A, B and C otherwise pass: each has one focal point, Doug and the
    threat are obvious, the text is legible at feed size, they complement their paired titles, and nothing is
    misleading. Thumbnail A also has a stray green sliver at the bottom-right corner (about x=1200-1280, y=700). Crop
    it or extend the tail cleanly.
13. **s222 / s223** (illustrator): a red sliver of the ticket dispenser peeks out at the left edge of the "10"
    NOW SERVING box. Move the dispenser fully clear or fully behind the box.
14. **s065** (director): "FOLDED IN HALF" points at nothing. The cobra just has a hump. Show the rat snake bent
    into a U at the cobra's mouth, or attach the label with an arrow to the bulge.
15. **s009** (director): only slot 1 has a snake, and the common krait at scale 0.5 is nearly invisible on the
    #15181a background. Scale it to about 0.8, or put a white label "COMMON KRAIT" beside slot 1.
16. **s116 / s164** (illustrator): the stopwatch has no hand (blank face) next to "30 MIN". Use the stopwatch with
    a hand as in s013/s113.
17. **s209-s213** (director, optional): 5 frames of the same four-cobra row. This is a progressive build, so it is
    acceptable, but s213 "FOUR KINGS" would land harder with tiny crowns on the four heads or a push-in.

Routing summary: director 1-4, 6, 7, 9-11, 14, 15, 17; illustrator 5, 8, 13, 16; graphic designer 12. No art-director
style issues found.

## Round 2: re-check of Round 1 fixes (keyframes + thumbnails), 2026-11-23

Checked at full res in `build/keyframes/`: s009, s030, s041, s052, s065, s077, s078, s091, s108-s125, s132, s134,
s158, s164, s182, s185-s192, s198, s222, s223, plus `build/thumbnail{,_b,_c}.png` and their `_small` versions.

**VERDICT: PASS** (keyframes and thumbnails). Nothing below blocks the render.

Round 1 items, re-checked:
1. s078 fixed. The king cobra's head is fully clear of the title.
2. s077 fixed. VENOMOUS. sits above the cobra and the hood is clear.
3. s091 fixed. NATIONAL ZOO sits inside the board face.
4. s134 and s198 fixed. The circle is on the southern tip of the peninsula, inside the map.
5. s158 fixed. The newspaper photo now shows a cobra with a python, not the monitor lizard.
6. s052 mostly fixed. The bubble reads "bye friend?" and the tear sells it. In the tube suit there is no visible
   waving arm (see minor note a).
7. s190 fixed. NOT A SNAKE sits on open sky and the arrow lands on Doug.
8. s030 and s132 fixed. The radio tag is a collar on the neck with a RADIO TAG label.
9. s109-s118 run broken. s110 is a close-up, s116 is a cream info card with a stopwatch that has a hand, and s117 is
   a tight two-shot.
10. s122-s125 and s186-s191 runs broken. s124 is a Doug/clipboard close-up, s188 is a close-up with the cobra
    looming, s189 is a cream card, and s191 is a wide walk-off.
11. s041 fixed. The route is onshore down the south-west.
12. Thumbnails pass. In B the viper is now larger, white-outlined and clearly biting, and reads as a snake at
    `_small`. The stray sliver in A is gone. A, B and C each have one focal point, legible text at feed size, and
    match their paired titles.
13. s222 and s223 fixed. The dispenser is clear of the NOW SERVING box.
14. s065 fixed. The FOLDED IN HALF arrow points at the bulge.
15. s009 fixed. A COMMON KRAIT label sits beside slot 1.
16. s116 and s164 fixed. The stopwatches have hands.

s182 (newly listed) is fine. Doug is asleep on the house roof and matches the "sleeping on the roof of the nursery"
line. It is not kids-coded.

### Minor (optional, fix if cheap; does not block)

a. **s110** (director/illustrator): the narration is "grabbed them right behind the head", but the cobra is only
   tongue-flicking at the viper and its jaws don't touch it. If cheap, overlap the cobra's closed jaws onto the
   viper's neck, just behind its head, and keep the arrow.
b. **s052** (director): "waving goodbye", but the tube suit shows no arm. If the rig allows it, add one raised arm
   or hand at the suit's shoulder (right side, under the bubble tail).
c. **s188** (director): the rake handle crosses the final "S" of FREEZES. Shift the text about 80 px left, or up
   to about y=1000.
d. **s111-s115** (director): these share the same branch set, and s112, s113 and s115 all have the upright cobra
   in the same spot. The overlays differ (tally, stopwatch, viper on the branch), so this is acceptable. A small
   push-in on s113 would add some motion.

Routing: director a-d, illustrator a. No graphic-designer or art-director issues.

## Round 3: thumbnail B (render 18:28 UTC)

VERDICT: PASS

Screened `build/thumbnail_b.png` and `build/thumbnail_b_small.png` against "Why One King Cobra Killed and Ate Over
Two Dozen Pit Vipers" / THEY BITE BACK. This replaces the Round 2 note on B, which described the older render.

- Feed size: at `_small` the bright green viper with its triangular head reads as a snake against the olive cobra
  and the yellow background. The bite on the cobra's crown is the one clear focal point. THEY BITE BACK is legible.
- Cropping: nothing is cut off. The viper's tail clears the top edge. The cobra's tail runs off the left edge on
  purpose. The cobra's body passes below the text block and does not overlap it.
- Doug: on-model (red cap, white round head, stick body), out of costume, scared face with a sweat drop, holding a
  clipboard. He is small but you can still pick him out at `_small` by the red cap.
- Tally: 5 groups of 5 plus 1 makes 26, which matches "over two dozen".
- Gore and kids: no blood or wounds, only red cartoon impact ticks. Adult-coded, nothing nursery-like.
- Misleading check: no. The script says "pit vipers bite back, and in nine of those hunts, the cobra appeared to get
  bitten" (script.md:134), and the cobra still wins per the title. The text and image complement the title without
  repeating it.

Optional (graphic designer, does not block): Doug is about 6% of frame width. If cheap, scale him up about 15% to
make him easier to see on mobile.

## Round 4: post-render (final.mp4 705.9 s, Shorts x3)

VERDICT (main): PASS
VERDICT (shorts): PASS

Main video
- I viewed all 24 samples (`build/samples/f_001..f_024`, taken at t = 15 s + 30 s·n) and matched them to `timing.json`. In every frame the picture fits the line being narrated: krait/QUIETLY (s007), 4 SECONDS (s024), 35 km+ / 6 MONTHS (s042), up a tree "bye friend?" (s052), the jaw diagram (s062), BLACK MAMBA (s092), the tally on the branch (s104), FINE (s124), THING WITH LEGS (s142), SQUEEZES (s160), the coil death with the cap showing (s168), the 55 cm / 1.5 m nest (s178), GUARDING/HUNTING (s189), STILL ALIVE (s199), 2024 (s208), the bell for "number called" (s218) and the end slate.
- qc.json lists no problems. My own ffmpeg blackdetect (0.5 s) and freezedetect (8 s) pass over final.mp4 found no black or frozen stretches.
- Contact sheet (s030, s116, s132, s158, s164, s222, s223): all readable and on-model. The counter runs 408 to 414 without skipping. There is no gore: the deaths are a coil and a gravestone. The ending pays off the title with the deli counter, NOW SERVING 10 and TAKE A TICKET. There is no "???" teaser.
- Thumbnails A/B/C and their _small versions: each has one focal point at 168x94. A shows the krait tail in the cobra's mouth with Doug in a krait suit holding ticket 9 (NEXT IN LINE). B shows the viper biting the cobra's crown with a 26 tally (THEY BITE BACK). C shows the gaping cobra and Doug in a cobra suit (NOW SERVING 9). All three fit their paired titles. None is misleading, and none has blood.

Shorts (short01 52.8 s, short02 39.2 s, short03 43.8 s; 1080x1920)
- The titles are legible on all three backgrounds. On the navy background of short03 the red title is a little lower contrast but still reads clearly. The subtitles are large and stay clear of the drawing. The words that look cut off in the previews ("ap", "ov") are just the word-by-word reveal caught mid-animation. The main subjects stay inside the frame. Only background trees are clipped at the edges.
- Each end card reads FULL VIDEO: TAP BELOW with a red arrow pointing straight down. Doug is on-model and the frame ends cleanly. Each short pays off its title: 26 vipers with the 9-hunts tally; dead within 30 min; filmed swallowing another king cobra alive. There are no teaser cards.

Optional nits (do not block)
a. s034 (director): "tracked one trail back and forth across a fast stream three times". At the sampled moment only Doug and the stream are on screen. If cheap, add a dashed zig-zag path over the stream like the one in s042.
b. s134 (director): "In Singapore...". The map has no marker. Add the red circle on Singapore that short03's map already uses.
c. s114 (director): "then he went back and ate". At the sampled moment Doug stands alone. If cheap, keep the cobra in frame.

Routing: director a-c. No issues for the illustrator, graphic designer or art director.
