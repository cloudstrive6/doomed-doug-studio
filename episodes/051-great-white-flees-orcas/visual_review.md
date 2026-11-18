# 051 Visual review

## Round 1: pre-render keyframes (2026-11-18)

Scope: 18 contact sheets plus the full-res keyframes for s001-s207 and the endslate. s001 shows a placeholder because the thumbnail hasn't been made yet, so it was not judged.

VERDICT: FAIL

The episode is in good shape overall. Doug is on-model and readable in every shot he's in, including the shark, seal and helmet costumes and the ghost and dead beats. The HUD (death counter and SHARKS GONE timer) is legible and never cropped. All the creatures are recognisable: great white, orca with bent fin, sevengill, bronze whaler, elephant seal bull. The deaths are cartoon only: black card plus cap, ghost, and the flattened seal costume. The "missing liver" beats use red X marks and a diagram-style cutaway, not anatomy, so there is no gore. I found no nursery or kids'-show tone. The failures are all text, speech-bubble and variety problems.

### Required fixes

1. **s102 (director): text overflows the speech bubble.** "SHARK." wraps onto a second line that sits on the bubble's bottom outline and the tail joint. Make the bubble `w` 640 (one line) or `h` 150 so both lines sit inside.
2. **s186 (director): the speaker collides with the HUD and the tail misses him.** The scientist on the boat has his head directly under the "SHARKS GONE: YEARS" label, about (1440, 260). The bubble tail `[1380, 250]` ends on the HUD stopwatch, not on him.
   - Move the boat left so the scientist sits at x ≤ 1250 and clears the HUD block (x 1300-1900, y 0-280).
   - Re-aim the tail at his head.
3. **s194 (director): the bubble tail is broken.** The tail `[650, 560]` is horizontal at the same y as the bubble. It renders as a thin wedge that cuts across the bubble outline and ends in empty sand, with a stray dot under the text. Aim it down-left at the scientist's head, about `[560, 615]`.
4. **s111 (director): the tail stops at the horizon.** The "hi friends?" tail ends at y 560 on the shoreline, about 120 px above Doug's head (Doug is at y 720, lying on his back). Extend the tail to about `[790, 650]` so it clearly comes from Doug.
5. **s206 (director): the picture contradicts the line.** The narration is "Unlike the sharks, this number never leaves", but the shark faces the RIP stone and the arrow runs from the shark to the grave (1050 to 500), so it reads as the shark arriving. Unflip the shark and point the arrow away to the right, for example from (1350, 800) to (1850, 780), so the shark is the thing leaving.
6. **s022-s026 (director): a run of 5 near-identical compositions.** Every shot uses the same tour boat, cable, cage, Doug in the seal costume and BAIT tag, with only small props changing. Change at least one:
   - Preferred: make s023 ("Doug did not agree to this.") a tight push-in on Doug's gritted face through the cage bars, scale about 1.0.
   - Or frame s026 as a close-up of the flippers being done up.
7. **s157-s160 (director): a run of 4 South Africa map shots** with the same map frame on the left and Doug on the right, and s158 adds the chapter title over the same map. Re-stage s160 ("along South Africa's southern coast") as a side-on coastline view instead: a line of tagged sharks swimming right past headlands. That breaks the run before s161.

### Recommended (non-blocking)

8. **s089 and s090 (director): the tourists float.** The two `tourist_camera` figures have their feet about 30-50 px above the boat's rail and deck. Lower them (y about 345) so they stand on the deck. In s089 the "GREAT WHITE!" tail also points at the cabin roof between them. Aim it at the nearer tourist's head.
9. **s175-s178 (director): 4 shots with the same road, beach and car framing.** The gag progresses, so this is acceptable. s178 ("Doug is fine.") would land harder as a medium close-up of Doug at the roadside.
10. **s027 and s093 (director): the death beats land on location-change lines.** The splash or ghost and the counter tick play over "Off South Africa," (s027) and "Meanwhile, back at the Farallones," (s093), while the frame still shows the cage. Consider moving the splash, ghost and counter tick earlier, into the tail of s026 and s092 (`appear` about 0.7). The location line would then cut to the new place. Note that s028 currently doesn't show South Africa until 0.7.
11. **Running field-guide gag (illustrator, optional): the in-book text is unreadable at small scale.** In s021, s071, s115, s133, s199 and s203 the book is shown at about 0.3 scale, so "GREAT WHITE / FRIEND?" and the s203 sticky note ("AFRAID OF ONE THING.") can't be read at 1080p playback. Only "NO" reads. Raise the scale to at least 0.5 where the joke depends on the sticky note (s203 especially), or accept that "NO" carries it.

Re-check for round 2: re-render keyframes for s022-s026, s089, s102, s111, s157-s160, s186, s194 and s206, plus any shots touched by fixes 8-11. Round 2 only covers these items.
