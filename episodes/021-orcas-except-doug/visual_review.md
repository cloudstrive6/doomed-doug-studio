# Visual review: 021-orcas-except-doug

## Round 3 (final): pre-render keyframes (22 contact sheets, s001-s259) + thumbnail

VERDICT: PASS

Note on the build: `build/contact/` held only one partial sheet (s082, s087), left over from a `--shots` run. Also, `shotlist.json` (saved 18:12:54) was newer than most keyframes (18:11-18:12:10). I re-ran `python -m studio keyframes 021-orcas-except-doug` and reviewed all 259 fresh keyframes on 22 sheets. `validate shotlist` returns OK.

Twenty-one shots changed since round 2: s006, s010, s013, s014, s023, s036, s037, s052, s060, s068, s071, s082, s084, s085, s087, s100, s145, s174, s219, s234, s255. All were checked, and none of them has a regression.

### Round 2 items: status

| # | Shot(s) | Status |
|---|---|---|
| 1 | s067-s071 navy card run, s068 had no picture | FIXED. s068 is now a seascape: the notched surfboard sits at the waterline, the fin heads away to the right, there is a red arrow, and "HE SURVIVED" is at the top. s071 reuses the seascape with the fin further off and "IT LET GO". The longest navy run is now 2 (s069, s070). No rider, no blood, and the notch is a cartoon notch. |
| 2 | s087 "8x" had no comparison | FIXED. There is now an "ORCA" row with 8 red ticks and a "FISHING GEAR" row with 1 grey tick. The scar strokes on the fin tiles are about 2x thicker. It reads in 1 second (full frame checked). |
| 3 | s255 Doug overlapping the fin | FIXED. Doug is at x1760 and the fin at x1550. The splash ends at about x1680 and Doug's hand starts at about x1720, so they read as two separate shapes (full frame checked). |
| 4 | s145 scissors near the pectoral fin | ACCEPTABLE. Now about 60-70 px diagonally from the fin tip at (1260,790). See note A. |

### Sweep of all 22 sheets
- **Doug:** on-model (red cap, white head) in every shot where he appears.
- **Death counter:** steps 170 -> 171 (s029) -> 172 (s050) -> 173 (s099) -> 174 (s120) -> 175 (s140) -> 176 (s159) -> 177 (s200) -> 178 (s246). It matches the outro line "one hundred and seventy-eight" in s257.
- **Overlaps:** no map frame or label covers the DOUG DEATHS box, and nothing overlaps the title labels.
- **Content:** no gore anywhere. Deaths are X-eyes or a floating cap only, and the s001 jaw interior is dark maroon, not blood.
- **Tone:** no kids-show tone.
- **Variety:** no run of 4 or more near-identical compositions. The longest similar runs are 3: the s235-s238 menu callbacks change their emphasis each time, and the s146-s148 maps change their content.
- **Changed map shots** (s006, s010, s013, s014, s023, s036, s037, s052, s060, s084, s085): each has a clean frame, clears the counter, and has labels inside the safe area.
- **Other changed shots:**
  - s082: five cars under the orca.
  - s100: a 1-in-25 grid.
  - s174: humpbacks chasing orcas, with a "6.5 HOURS" clock.
  - s219: "PARTNERS / NOT PREY".
  - s234: "SAME AS EDEN" with a dashed link.

  All five read clearly.

### Thumbnail (build/thumbnail.png, thumbnail_small.png, plus a 168 px feed simulation)
- **Text:** "NOT ME?" is legible at 320 px and at 168 px. It uses no title or alt-title words.
- **Subjects:** the orca breaching with a great white held side-on is obvious at feed size. The orca is hard-eyed, not cute. Tiny Doug in the rowboat, waving, is identifiable by the red cap even at 168 px.
- **Content:** no blood, wound or red in the jaw; the mouth interior is dark maroon and reads as shadow.
- **Fit with the title:** it complements "Why Orcas Kill Everything in the Ocean Except Doug" (threat plus exception) and is not misleading. The orca kill-list and the Doug exception are both in the video.

### Non-blocking notes (optional polish, do not hold the render)
A. **s145, director.** The car's wheels now end at y1072, only 8 px above the bottom edge, so the car looks like it rests on the frame. The scissors are still fairly close to the shark's pectoral fin. Suggested change: move `car_half` from (1180,1070) to about (1000,1010). That puts the cut line clear of the fin (the fin spans x1260-1400) and leaves about 60 px of bottom margin.

B. **s067, director, optional.** This is still a text-only dateline card ("POINT SUR, CALIFORNIA, 1972" on navy). It is accepted as a dateline beat now that s068 carries the picture.

### Routing summary
- Director: optional A, B
- Illustrator: no action
- Art director: no style violations; no action
- Graphic designer: thumbnail passes; no action

Cleared for narration/render. Post-render screen still due: build/samples, qc.json, and the Shorts.

---

## Post-render screen (final.mp4, thumbnail, Shorts)

**What I checked:** build/samples f_001-f_032 (one frame every 30 s of the 951.8 s render), build/qc.json, build/thumbnail.png and thumbnail_small.png against metadata.json, and the three Shorts. For each Short I viewed the preview and pulled ffmpeg frames at 1/8/16/24/32 s plus the last 9, 6, 3.5, 1.5 and 0.3 s.

### Main video
- **QC:** qc.json reports `problems: []`. There are no black, blank or glitched frames in the 32 samples.
- **Frames:**
  - Every sample has the zone header and the death counter (it rises from 170 to 178 in order). Doug is on-model (red cap, white head) wherever he appears.
  - Text is legible and uncropped.
  - Each chapter has a different background colour or zone, so no stretch looks frozen.
- **Pictures:** every drawing is recognisable: salmon, otter, seal, dolphin and porpoise, stingray, moose, the South Africa map, gray whale, whale shark, the Eden whalers and Old Tom, blue whale, and the rowboat ending.
- **Content:** no gore. Deaths are costume gags (the otter float, the whale-shark mouth, the moose costume).
- **f_012 (dolphin, "1 IN 25"):** Doug is caught mid-fade or sinking at the death beat. That is acceptable as a transition frame.
- **f_014 (stingray zone):** an empty beach with Doug on the bank is a scene beat, not a missing asset.

### Thumbnail
- **thumbnail.png:** "NOT ME?" is legible. The breaching orca holds a whole great white with no blood. Tiny waving Doug in the rowboat is clear.
- **thumbnail_small.png (320 px):** the text, the orca with the shark, and Doug's red cap all still read.
- **Fit with the title:** it complements "Why Orcas Kill Everything in the Ocean Except Doug" (threat plus exception) and is not misleading. Unchanged from the keyframe-round pass.

VERDICT (main): PASS

### Shorts (1080x1920)
- **short01, "One Orca Killed a Great White Shark in Two Minutes" (49.4 s)**
  - Title is readable and not cropped. Captions are legible.
  - It pays off the title with "1 ORCA" and the 2:00 stopwatch.
  - End card: the orca silhouette (dorsal fin, tail flukes) is recognisable in red outline with "???". "WHAT DID THE ORCA DO TO DOUG?" matches the outro ("Doug in the shark costume ... did not last two minutes"). The outro implies the outcome but not what happened, so the question stays open. The arrow points down.
- **short02, "Orcas Have Been Caught Killing Swimming Moose" (48.2 s)**
  - The hook scene and the Icy Strait 1993 map pay off the title.
  - End card: the moose-costume silhouette (antlers over a swimming body at the waterline) is recognisable as the moose costume. It matches "HOW DID DOUG THE MOOSE END UP?". The outro does not answer it, and the arrow points down.
- **short03, "Orcas Hunt the Largest Animal That Has Ever Lived" (45.8 s)**
  - The blue whale, the "150 TONNES" label, the Australia map, the hunt formation with "FEMALES LEAD", and the fin-ID grid pay off the title.
  - End card: the orca silhouette is clear, with "WHAT DID THE ORCA DO FOR DOUG?". It is a specific tease of the 34-case prey-offering finding and is not answered in the clip. The arrow points down.
- **All three:** the watermark is present. Titles and subtitles sit in the safe areas. The preview stills catch captions mid-word (word-by-word reveal), which is normal in motion.

VERDICT (shorts): PASS

### Non-blocking notes (optional; do not hold upload)
C. **s224-s226, director, optional.** At `blue_whale` scale 2.4 the whale overruns both frame edges in the landscape and Shorts frames. This is intended to show the "too big to fit" scale, and the head and eye stay in frame. In s226 the menu card group at (60,290) also covers the whale's tail section. If these shots are ever re-cut, shift the card to y≈560 below the whale, or drop the whale to scale 2.0.
D. **short01 outro, director, optional.** "He did not last two minutes" leans toward answering the question. A softer line next time would be "Next, an orca found Doug in the shark costume. Full video below."

### Routing summary
- Director: optional C, D
- Illustrator, art director, graphic designer: no action

Cleared for upload.
