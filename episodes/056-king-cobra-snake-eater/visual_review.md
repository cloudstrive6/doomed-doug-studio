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
