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

## Round 2: keyframe re-check (2026-11-18)

Scope: I re-rendered the keyframes from commit c81c9008 (18:19). I checked these at full resolution: s021-s028, s071, s089, s090, s092, s093, s102, s111, s115, s133, s157-s160, s186, s194, s199, s203 and s206. I also skimmed all 18 contact sheets. s001 still shows "thumbnail pending" and was not judged.

VERDICT: FAIL

### Round 1 items, now resolved
- **s022-s026 run:** fixed. s023 is now a tight close-up of Doug's gritted face through the bars, which breaks the run and lands the joke.
- **s157-s160 run:** fixed. s160 is now a side-on coastline with headlands, tagged sharks swimming right, Doug swimming after them, and an EAST arrow.
- **s206:** fixed. The shark faces right, away from the RIP stone, and the arrow points off to the right, so it reads as "the sharks leave".
- **s027 and s093:** fixed. The splash, ghost and counter tick now play in s026 and s092. The location lines cut straight to the South Africa and Farallones maps, and the ghost carries over, which is a nice touch.
- **s111:** fixed. The "hi friends?" tail now ends on the costume's back next to Doug's head. Doug is in the costume, so it clearly comes from him.
- **s186 (HUD collision):** fixed. The scientist is at x about 1190 and clears the HUD block.
- **Field guide (s021, s071, s115, s133, s199, s203):** fixed. The book is now about 0.5 scale. "GREAT WHITE", "FRIEND?", "NO" and "MAYBE" all read. The s203 sticky note "AFRAID OF ONE THING." is legible at 1080p.
- **s089 and s090 (floating tourists):** fixed. Their feet now sit on the deck behind the rail.
- **s102 (text overflow):** fixed. "NOT A SINGLE SHARK." now sits on one line inside the bubble. But the tail has a new problem; see fix 2.

### Required fixes

1. **s194 (director): the bubble tail is still broken.** The tail now ends at the scientist's head `[560, 615]`. But the bubble is to his right at almost the same height, so the engine draws a long, nearly horizontal sliver. Its root breaks the bubble's bottom outline, and the stray black dot under "EXCITING!" (about 905, 603) is still there.
   - Why: `paint.py` roots the tail at about (x-0.12w, y+0.35h) to (x+0.02w, y+0.42h), so a target level with the bubble always renders like this.
   - Fix: move the bubble up and left so the tail runs mostly downward: speech `x 640, y 470` (w 330, h 100 unchanged), `tail [540, 585]`.
   - Re-render and confirm the tail is a clean wedge with no dot or gap.
2. **s102 (director): the tail stops at the horizon, not at the speaker.** The "NOT A SINGLE SHARK." tail ends at `[1450, 560]`, on the shoreline, about 70 px above and 100 px left of the scientist's head (head at about 1550, 640-720). This is the same fault fixed in s111 last round.
   - Fix: set `tail [1530, 630]` so it touches the top of his head and binoculars.
3. **s159 (director): a broken arrow sits on top of the sharks.** The arrow `from [675, 896] to [668, 857]` with `bend -40` is 40 px long and points up. It renders as a red "Z" squiggle over the third tagged shark, on the line "started heading east". It looks like a coordinate bug.
   - Fix: replace it with an eastward arrow in the sea just right of the sharks, for example `from [720, 866] to [990, 846]`, `bend -15`, width 8, `appear 0.4`.
4. **s090 (director): a fuzzy white static cloud covers the second tourist.** The `spray` at `(420, 290)`, `r 70`, `density 0.5`, `appear 0.3` (presumably the camera flash) sits over his backpack and legs. It reads as a render glitch, not a flash.
   - Fix: move it onto the camera lens at about `(470, 215)` with `r 28`.
   - Or delete it and use a small white star or burst asset at the lens. The red "!" marks already sell "thrilled".

### Recommended (non-blocking)

5. **s186 (director): the tail is a long, thin double-lined sliver.** It runs about 450 px nearly level from the bubble to the scientist. It does reach him, but the root shows two separate outline strokes.
   - Fix: shorten and steepen it by moving the bubble right and down, for example speech `x 960, y 150, w 600`, `tail [1175, 228]`.
   - The bubble must stay below the title card (y > 83) and left of the HUD (x < 1300).
6. **s089 (director): aim the "GREAT WHITE!" tail at a tourist.** The tip is still at the cabin roof corner (about 470, 280). Set `tail [445, 235]` so it ends at the nearer tourist's camera or head.
7. **s199 and s203 (illustrator or director): the eraser smudge spills past the book.** The smudge under "NO" (where "MAYBE" was erased) runs about 15 px below the book's bottom edge onto the water. Clip it to the page, or shrink the spray radius.
8. **s175-s178 (director): carried over from round 1, item 9.** There are still 4 shots with the same road, beach and car framing. s178 ("Doug is fine.") would land harder as a medium close-up.

### Skim of the contact sheets
I found no new issues beyond the above.
- Doug is on-model throughout, in the cap, shark costume and seal costume.
- The HUD is consistent: the counter runs 380 to 386 and ticks only on death beats. The SHARKS GONE label escalates from minutes to years.
- The chapter cards are correct.
- There is no gore. The bull elephant seal's pink chest shield in s113-s115 reads as anatomy, not a wound. The missing-liver beats are still X marks and diagrams.
- I found no kids'-show tone.

Re-check for round 3: re-render s090, s102, s159 and s194, plus s089, s186, s199 and s203 if items 5-7 are taken. Round 3 only covers these shots.

## Round 3: keyframe re-check (2026-11-18)

Scope: I re-rendered all 14 shots from the current working-tree shotlist (it was modified after some of the older keyframes) and checked s055-s057, s068, s089, s090, s102, s159, s166, s178, s186, s194, s199 and s203 at full resolution.

VERDICT: PASS

### Round 2 required fixes, now resolved
1. **s194:** fixed. The bubble now sits up and right of the scientist, and the tail is a clean downward wedge ending at his binoculars. The bubble outline is unbroken and the stray dot is gone.
2. **s102:** fixed. The "NOT A SINGLE SHARK." tail now ends on the scientist's head and binoculars, not on the shoreline.
3. **s159:** fixed. The red "Z" squiggle is gone. A clean eastward arrow runs from the tagged sharks to the EAST label, in open sea.
4. **s090:** fixed. The static cloud has gone. A small flash sparkle now sits on the second tourist's lens and reads as a camera flash.

### Round 2 recommended items
5. **s186:** the tail reaches the scientist's head and the bubble stays clear of the title card and HUD. It is still a long, thin sliver, but that is acceptable.
6. **s089:** the "GREAT WHITE!" tail now ends at the nearer tourist's camera. Accepted.
7. **s199 and s203:** the eraser smudge now stays on the page. "AFRAID OF ONE THING." and "NO" are both legible.
8. **s178:** now a medium close-up of Doug at the roadside giving a deadpan thumbs-up. It lands "Doug is fine." and breaks the s175-s178 run.

### Art-director touch-ups, checked for screening
- **s055-s057:** the diver and Doug are centred in the gap between the kelp stipes and clear of the tuft. The cap and mask read clearly. The 1 HOUR stopwatch in s056 is legible.
- **s068:** Doug in the sevengill costume, among the school, reads as "joined the crowd".
- **s166:** the arrow now stops short of the first tagged-shark icon, and the orcas-at-Gansbaai-to-sharks-east logic reads.

### Non-blocking note
- **s057 (director):** the top of the "LARGEST ON EARTH" caption touches the lowest sevengill's belly and fins (about 600-820, 925). The caption is still fully legible. If someone touches this shot again, nudge that shark up about 30 px or move it right of the caption.

No gore, no kids'-show tone, and Doug is on-model in every shot checked. Visual screening for art_approved is passed.

## Round 4: thumbnail screen, variants A/B/C (2026-11-18)

Scope: `build/thumbnail.png`, `thumbnail_b.png`, `thumbnail_c.png` at 1280x720 and their `_small` versions at 168x94 (viewed at 1x and at 3x nearest-neighbour), checked against the top 3 packaging candidates in `metadata.json`. Thumb-text claims were checked in `facts.md`. "IN MINUTES" is the Farallones "within minutes" finding (MBA release). "ZERO IN 2019" comes from the Shark Spotters 2019 annual report. "GONE ALL SEASON" fits the "up to a year" and Months band.

VERDICT: FAIL (B blocks; A has one cheap fix; C passes)

### Variant A: "IN MINUTES" / "Why the Deadliest Shark Flees Orcas for Up to a Year" — PASS after fix 1
At feed size the great white reads instantly, and it is fleeing left, away from the orcas, with speed lines. Doug is on-model (red cap, white head, shock face, shark costume) and readable against the blue water. The text is legible and spelled right. No gore or kid tone, and it fits the title.
1. **(graphic designer) thumbnail.json:** the tip of the left orca fin's hooked top runs into the black outline of the final "S" (about x 975-1060, y 105-145). At 168x94 the first fin merges into the letter, so the threat stops reading as a separate shape. Move both orca fins down about 40 px and right about 30 px (or shift the text block about 40 px left) so there is a clear gap of at least 20 px between the fin and the outline.

### Variant B: "GONE ALL SEASON" / "Why Great White Sharks Flee the One Animal That Kills Them" — FAIL
2. **(graphic designer) thumbnail_test_b.json, gore risk:** the orca is drawn as a silhouette with an 8 px red rim. Its dither texture comes out as a red speckle spray drifting off the body into the water (about x 80-600, y 540-720). Against blue water, a red mist around a black predator reads as blood in the water. That breaks the no-gore rule and is an advertiser-friendliness risk. Remove the red rim and red texture completely. Outline in black or white only (for example a 6 px white rim), with no red particles anywhere in the water.
3. **(graphic designer) thumbnail_test_b.json, unreadable threat:** with `silhouette: true` and `rotate: -30`, the orca is a featureless black hump with a stub fin cut off at the bottom of the frame. There is no white eye patch, saddle or tall dorsal fin, so at 168x94 it reads as a rock or blob. The title's "One Animal That Kills Them" therefore has no visible animal. Draw the normal orca asset (not a silhouette), unrotated or tilted no more than 10 degrees, large enough that the white eye patch and dorsal fin are on-frame (keep the dorsal fin above y 600). Keep Doug riding it in shock.
4. **(graphic designer, optional):** the brief's concept for B was the three-panel grid (full bay, orcas arrive, empty bay with Doug's floating cap). That is a valid alternative to fixes 2-3, and it would make "GONE ALL SEASON" literal. If you use it, keep the panels to 3 and the cap at least 25 px tall at feed size.
Doug in B is on-model and the text is legible. Those parts can stay.

### Variant C: "ZERO IN 2019" / "Why the Scariest Sharks Gave Up False Bay to Orcas" — PASS
The crossed-out great white fin is the clear focal point and reads at feed size. The two bent orca fins on the horizon and Doug (on-model, gritted teeth, shark costume) between them read as threat and victim. The text is legible and the claim is sourced. No gore or kid tone.
- Non-blocking: the fin tip tucks behind "ZERO". It still reads as a fin, but dropping the fin about 25 px would give it a clean silhouette. The orca fins are small at 168x94 (about 12 px). They still read, but scaling them about 1.2x would help.

Re-check for round 5: re-render `thumbnail.png` and `thumbnail_b.png` and their smalls. C needs no re-check unless it is touched.

## Round 5: thumbnail re-screen, variants A/B/C (2026-11-18)

Scope: `build/thumbnail.png`, `thumbnail_b.png`, `thumbnail_c.png` at 1280x720 and their `_small` versions at 168x94 (viewed at 1x and at 3x nearest-neighbour). The renders are current: they share an 18:30 timestamp with `thumbnail.json`, `thumbnail_test_b.json` and `thumbnail_test_c.json`. I compared each against its top-3 title in `metadata.json`.

VERDICT: PASS (A PASS, B PASS, C PASS)

### Variant A: "IN MINUTES" / "Why the Deadliest Shark Flees Orcas for Up to a Year" — PASS
- Round 4 fix 1 is resolved. Both orca fins sit lower and further right. The nearest fin edge is about 25-35 px from the final "S" outline, and at 168x94 the two fins read as separate shapes from the text.
- The new worried brow and the two sweat drops on the great white read as "scared shark" at full size. At feed size the shark still reads as fleeing left, helped by the speed lines on the tail side.
- Doug is on-model: red cap, white head, shocked mouth, shark costume. The text is legible and there is no gore.

### Variant B: "GONE ALL SEASON" / "Why Great White Sharks Flee the One Animal That Kills Them" — PASS
- Round 4 fix 2 (gore risk) is resolved. The red rim and red speckle are gone, and there is no red anywhere in the water.
- Round 4 fix 3 (unreadable threat) is resolved. The orca is now the full asset, only slightly tilted. Its white eye patch, saddle, belly and tall dorsal fin are all on-frame, and it reads as an orca immediately at 168x94. The title's "One Animal" is now visible.
- Three shark fins with speed lines leave along the horizon, which makes "GONE" literal.
- The new yellow "!" (black outline) is legible at full size and still visible at feed size. It sits clear of Doug's head and just above his costume fin tip, without touching it. Doug is on-model and in shock, standing on the orca's back. The white text on orange is crisp.
- Non-blocking (graphic designer): the white splash ellipse behind the orca is a large flat disc. At feed size it reads a little like an ice floe or plate. Thinning it to a ring or shrinking it about 30% would make it read as wake. Not required.

### Variant C: "ZERO IN 2019" / "Why the Scariest Sharks Gave Up False Bay to Orcas" — PASS
- C is unchanged from round 4 and still passes. The crossed-out fin is the focal point, the orca fins and Doug read, and there is no gore.
- The round 4 non-blocking notes still apply and remain optional: drop the fin tip clear of "ZERO", and scale the orca fins about 1.2x.

No required fixes. All three variants are cleared for the packaging gate.

## Round 6: post-render screen of final.mp4, thumbnails and Shorts (2026-11-18)

Scope: `build/samples/f_001..f_023.png` (every 30 s of `final.mp4`, 697.9 s), `build/qc.json` (no problems), `build/thumbnail*.png` and their `_small` versions, `metadata.json`, `build/shorts/short01..03_preview.png`, and ffmpeg frames from each `short0N.mp4` at 0, 1, 3, 5, 7, 10, 20 and 30 s and at end-3 s and end-0.5 s (all 1080x1920). Nothing was rendered.

VERDICT (main): PASS
VERDICT (shorts): PASS

### Main video
- All 23 samples are clean. There are no black, blank or frozen frames and no glitches. The chapter tag, the DOUG DEATHS counter (380 to 386) and the SHARKS GONE tracker are legible on every frame and never overlap the drawings.
- Doug is on-model wherever he appears: red cap, white head, readable on every background. The shark-costume variant (f_005) matches the thumbnails.
- The pictures match their beats: Farallon map, beached shark ("HOURS."), 2009 map, sevengill cousins, empty cage-diving boats, seal colony, the four-season wheel, the Año Nuevo move, the 300+ vs 4 bar chart, and the RIP DOUG end. The BAKERY sign (s081) is the narrated "bakery running out of bread" analogy, and the red car (s175-s177) is the "Doug followed the sharks east" beat. Both are on-script.
- There is no gore. The beached shark has X eyes and no blood, and the removed liver is a plain yellow bean with no red. The tone is not kid-coded.
- The episode ends cleanly on the death-counter tombstone. There is no "???" teaser card.

### Thumbnails (A/B/C)
The renders are unchanged from the round 5 PASS (same 18:41 build). All three read at 168x94 and have one focal point. Doug and the threat are obvious in each, and each matches its paired title in `metadata.json`. No new issues.

### Shorts
- The titles are legible in red with a black outline, and no drawing is clipped at the sides. Doug stays inside the frame. In short01 he enters from the left edge at t=0 and is fully in frame by 3 s.
- The burned-in subtitles in the mp4s are whole words and legible. The cut-off text in the `_preview.png` files ("one org", "hunting s") comes from the preview builder, which truncates to 40 characters (`studio/shorts.py`, `mid[4][:40]`). It is not in the videos.
- Each Short pays off its title. short01 reaches THE LIVER (the x-ray liver plus beached sharks), short02 reaches the season calendar and the Año Nuevo move, and short03 reaches the sightings line crashing to zero. The end card on each reads "FULL VIDEO: TAP BELOW" with a red arrow pointing straight down. There is no teaser card.
- There is no gore. The liver x-ray is a flat yellow organ silhouette.

### Non-blocking notes (optional)
1. Director, Shorts: the in-frame HUD (DOUG DEATHS / SHARKS GONE) is very small in the 9:16 crop and sits within about 10 px of the right edge in short01 at about 7 s. Hiding the HUD in Shorts shots, or moving it about 40 px inward, would tidy this.
2. Director, short01: the chapter tag "THE LIVER" and the big red "THE LIVER" caption appear together (0-3 s). Dropping one would reduce clutter.
3. Director, short01 end card: the outro says "Then Doug dressed as a great white", but the end card shows plain Doug. Using the shark-costume Doug on that end card would land the line.
4. Engine (not a shot fix): the preview still truncates the subtitle at 40 characters mid-word. This affects only the screener's preview.

No required fixes.
