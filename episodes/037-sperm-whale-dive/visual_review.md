# Visual review: 037-sperm-whale-dive

## Overall (2026-11-04, final thumbnail pass)

VERDICT: PASS

- **Keyframes**: PASS (Rounds 1-2). All Round 1 items (s001, s159, s024, s043, s044-s047, s166-s168, s208, s006, s161, s138,
  field guide s031/s054/s078/s124/s174/s200, s216) were fixed. No gore, no kids-show framing, Doug on-model, HUD and death
  counter consistent. Advisory only: s004 Doug scale (about 0.3), field-guide MAYBE continuity.
- **A, thumbnail.png (2 KM DOWN)**: PASS (Round 3, unchanged). One focal point (the scarred head), Doug and his beam read at
  168x94, and the text is the biggest element. It pays off "deeper".
- **B, thumbnail_b.png (IT HEARD YOU)**: PASS (Round 3, unchanged). The jaw is the focal point, Doug is lit between the teeth and
  the head, and the text is legible at feed size.
- **C, thumbnail_c.png (2x3 chapter grid)**: PASS.
  - DEEP: the red spray and red outline are gone. The whale is now a dark navy silhouette with a pale rim, angled nose-down
    toward the bottom-right, and Doug's beam lands on the head. The blood/gore read is fixed.
  - Bottle question, judged at 168x94 (smalls.png, c_small_x3.png): taken alone, the shape is ambiguous. The fluke end is thin,
    the head end is rounded, and the tan lit patch can look like a bottle base or cork. In the grid it still reads as a whale,
    because five tiles in a row show the same whale and the DEEP label explains it. Each tile is only about 55 px wide, so the
    labels carry the meaning in every tile. This is not blocking.
  - CABLE: the cable now runs off the tile edges and no longer ends in Doug's hand, so the "Doug lassoing it" read is gone.
    Doug is on-model in all six tiles, and all labels are legible at feed size.

Order: A is primary, B and C are test variants (per the CD).

### Advisory (not blocking, optional polish for C/DEEP, graphic designer)

1. **thumbnail_c, DEEP tile**: to remove any bottle read, square off the head end so it is flat and blunt like the other five
   tiles. Add the small eye and a short light-grey lower-jaw line with 3-4 teeth inside the beam. Make the flukes about 1.5x
   larger so the tail end reads as a tail and not a bottle neck. Keep everything else.
2. **s004 (director)**: carried over. Scale Doug up to about 0.3.

## Post-render (2026-11-04)

Checked: build/samples f_001-f_024 (mapped to shots via timing.json, one every 30 s from 0:15), final.mp4 frames at
0.5 s / 4 s / 8 s / 711.5 s, build/qc.json (duration 712.3 s, problems: none), thumbnail.png / _b / _c and their `_small`
versions (re-rendered at 18:39, same as the Round 3 pass), metadata.json, and build/shorts short01-03 (previews plus 10
frames each, including the last 2.5 s).

VERDICT (main): PASS
VERDICT (shorts): PASS

### Main video
- No black, blank, glitched or frozen frames. Every sample matches its narration (s007 ships sunk, s018 Essex, s026
  hypothesis, s037 drifting, s047 boat bump, s058 THE CLICK, s066 60 km, s076 listen, s096 STUN?, s108 jaw, s116 1891
  clipping, s126 jaw, s136 20 CM?, s143 whole record, s155 1957 clipboard, s163, s173 CABLE: FINE + cap on seabed,
  s184 150 ATM column, s192 bones worse with age, s205 2,000 m line, s213, s223 whale rises, endslate).
- HUD is consistent: the death counter goes up monotonically 287 to 293 on screen (294 is spoken at s229), and depth
  goes 0 to 15 to 200 to 500 to 700 to 900 to 1,134 to 1,500 to more than 2,000 m. Chapter tabs match the chapters.
- Doug is on-model in every frame. No gore: the bones are clean museum skeletons, and the s173 death is a cap on the seabed.
  No kids-show tone.
- The opening frame (0.5 s) is the A thumbnail, as intended. The endslate is clean, with the end-screen
  placeholders and SUBSCRIBE. The video pays off its title: it ends at 2,000 m and more with the whale going back up.
- Thumbnails A/B/C: unchanged since the Round 3 PASS and still readable at 168x94. "2 KM DOWN" fits the title.

### Shorts
- short01 (36.7 s), short02 (38.7 s) and short03 (49.2 s) are all 1080x1920. Titles are fully readable in 3 lines with no
  cropping. The 16:9 art is letterboxed at full width, so nothing is cut at the sides. The jaw bleeding off the left edge in short02/03 is
  the original s126/s160 composition, not a crop. Subtitles are large, white with an outline, and sit clear of the art.
  The end card "FULL VIDEO: TAP BELOW" has a red arrow that points straight down. Each Short ends cleanly with no "???"
  card.
- Payoffs: short01 shows 236 dB, explains why water is not air, and shows 60 km and 1.5 marathons. short02 shows the 1891
  clipping, then "not one word of truth", then OTHER VERSION. short03 shows 1,134 m against the tallest building, then the
  cable around the jaw and tail. "Doug dies seven times" matches the on-screen counter (287 to 294).

### Advisory (not blocking)
1. **s085 (director)**: "eighteen supermarket trips" is a single tiny cart (about 30 px at 640 w) in the top-left of an
   otherwise empty dark frame, so the subject is not obvious in 1 s. Scale the cart about 3x and centre it, or show a row
   of carts.
2. **s004 (director)**: carried over. Doug is tiny in the 2,000 m hook frame, so scale him up to about 0.3.
3. **Shorts (editor)**: Doug and the HUD are small inside the letterboxed 16:9 art on a phone. If the Shorts template
   gets a revision, crop in about 1.3x on the action. Not needed for this episode.
