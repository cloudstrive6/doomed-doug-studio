# Visual review: 030-trapped-in-amber

Round 1 (2026-10-28, pre-render keyframes): FAIL. The main problem was variety (about 95 centred-bead shots, with runs
of 4 to 8). There were also point fixes on s004, s012, s065, s046/s047, s172-s174, s134 and s048, plus advisories.
This file replaces the round 1 report.

## Round 2: restaged keyframes and thumbnails (2026-10-28)

I screened all 19 contact sheets (s001 to s216 plus the endslate) again. I checked the restaged and gold-background
shots at full resolution in `build/keyframes/`, and checked all three thumbnails at 1280x720 and at 168x94.

VERDICT: PASS

### Round 1 fixes: status
1. **Variety: fixed.** No run now has more than 3 consecutive shots with the same centred-bead framing. The restages
   work: the tick close-ups and DRACULA plate (s007, s009, s010), the feather cutaway (s011), the forest cutaways for
   the web (s035, s043, s044), the live hell ant with HORN/JAWS labels (s058, s059), the ant piercing the beetle with
   no fluid shown (s068, s069), the vertebrae close-up with "97" (s112), the credit card comparison (s113), the forest
   log (s118), the scan cutaways (s143, s168), the tail close-ups (s185, s186, s189), and the map, mine, journal and
   map sequence (s202 to s205). s161 to s164 is the tightest stretch left (four mid-size Belone beads). Each shot has
   its own prop (card, arrows, nameplate, skylark), so it passes.
2. **s004: fixed.** The trunks have moved left (x about 65 to 515). The whole silhouette is now clear, and the arrow
   lands on the tail end.
3. **s012: fixed.** The "PENNY EDGE" inset shows the tick at about 2/3 of the edge thickness, so the picture now
   matches "shorter than a penny is thick".
4. **s065: fixed.** The ant is clearly shorter than the rice grain, and dashed guides line up the left ends.
5. **s046, s047: fixed.** The adult male now sits inside the bead. Its leg tips and the "?" touch the rim but don't
   read as outside the amber.
6. **s172 to s174: fixed.** Doug stands between the trunks and his body lines read against the orange set.
7. **s134: fixed.** It is now a recognisable thumbs-up hand with a nail, and a true-scale skull on the thumb.
8. **s048: fixed.** It is now a silk sac with clustered eggs.
- Advisories done: the Kachin State region now has a red outline (s202, s205). s210 is still the accepted 1.2 s
  cut-to-black death.

### WordArt contrast on gold
All the lime WordArt has a thick dark outline, which keeps it readable on gold beads and gold sets at full size and
on the contact sheet. I checked: NEVER LANDED (s042), PINNED (s061) and FLIGHT FEATHERS (s159), which overlap bead
rims; and 100 MILLION YEARS, DOUG IS FINE, SPLIT SECOND, PIERCE, DRINK, COCKROACH RELATIVE, DRESSED AS ONE,
SANDY BEACH, SWALLOWED, COLLECTED, THE TIDE, IN A FOREST, DECLINED, READY TO FLY, VULNERABLE and NOT AT A DIG. None
fails. The weakest is 100 MILLION YEARS (s050), where "YEARS" crosses the light trunk. It is still legible, so no
change is required.

### Three items not done (advisory, none blocking)
- **s153, s154 (illustrator), not blocking.** The empty white plate on `old_drawing_card` is a small cosmetic blank
  in a 2-shot gag. Fill it with "1890s" or remove it if there is time.
- **s121, s128 (illustrator), not blocking but the most worth doing.** The big snake silhouette still reads as a black
  rope, especially in s128, where it is the death beat with no narration. The chapter bar, the shed skin and "hi
  friend?" carry the meaning, so a viewer will get it. A pale eye dot and a red forked tongue on the head end would
  make it read as a snake in under a second.
- **s165 to s167 (illustrator), not blocking.** The raw lump still reads as a potato or rock. Raw Burmese amber does
  have a brown crust, the narration says "a piece", and s168's scan resolves it. Still, one amber-gold chipped window
  with a glint, where the claw sticks out, would make the subject obvious.

### New advisories (fix if cheap)
- **s003, s004 (illustrator or director).** The forked, feathered tip of the dinosaur silhouette's tail faces Doug,
  and at a glance it can read as an open jaw. The head is at the far right. Because s004's arrow ends exactly on the
  fork, this could reinforce the misread. Either end the arrow mid-tail (about x 1200, y 590) or close the fork on the
  `feathered_dino` silhouette tail.
- **s086 (director).** The dime is drawn about twice the ammonite's width. True scale is about 18 mm to 12 mm. Shrink
  the dime about 25 % so the ratio is close to 3:2.

### Thumbnails
- **thumbnail.png (A, hero): PASS.** "99 MILLION YEARS" is readable at 168x94. The focal point is clear: Doug in
  shock between a tick in amber and the giant feathered dinosaur jaws. It complements the title without repeating
  any title word, and isn't misleading, because the adult appears in s209. There is no gore and nothing kid-coded.
- **thumbnail_b.png (B, hero): PASS.** "STUCK" is readable at feed size. Doug sinks in a resin pool with a falling
  drop and a giant hell ant. The threat is obvious and nothing is broken. Two notes: Doug is the main subject here,
  not "a small scale figure" (style bible rule 10), and the ant is drawn far larger than real. Both are within the
  cartoon register and the channel's past B tests, so neither is a fault.
- **thumbnail_c.png (C, grid): PASS with advisory (graphic designer).** It is readable at 168x94, the four specimens
  are recognisable, and the labels avoid all title words. Its kid-appeal risk is the highest of the three (4 big
  candy-coloured tiles and comic type), but it follows the replicated archetype A grammar and has a shocked Doug in
  the tail tile, so I don't consider it nursery-toned. Advisory: archetype A asks for 6 to 12 tiles, and the brief
  asks for a size ladder. All four beads are about the same size. Adding HATCHLING and WRONG DINOSAUR tiles (2x3), and
  stepping the bead size up from Tick to Dinosaur Tail, would deliver the "size ladder" promise and dilute the
  flashcard look.
- None of the three has spelling errors, crops, stray marks or gore.

## Round 3: post-render (final.mp4, thumbnails, Shorts), 2026-10-28

Inputs checked: `build/qc.json` (655.49 s, `problems: []`, written 17:41 after the 17:35 final render), all 22 samples
`build/samples/f_001-f_022.png` (each mapped to its shot via timing.json; every frame matches its narration), `thumbnail.png` / `_b` / `_c`
and their `_small` (168x94) versions, `metadata.json`, and the three `build/shorts/*_preview.png`. From each Short (1080x1920,
46.1 s / 40.2 s / 46.9 s) I pulled frames every 6 s, frames every 1.5 s over the last 9 s, and the final frame. Title: "The Creepiest
Things Scientists Have Found Trapped in Amber".

VERDICT (main): PASS
VERDICT (shorts): PASS

### Main video + thumbnail: PASS
- No sample is black, blank, frozen or glitched. f_022 (endslate, sky/grass, DOUG'S NEXT DEATH + dark end-screen box) is intended.
- The chapter tags step in order: Tick, Web, Hell Ant, Ammonite, Snake, Wrong Dinosaur, Hatchling, Tail. The counter also steps
  in order, from 240 to 245.
- Each picture matches its line. Examples: f_002 "158 MOA BONES" over "...a hundred and fifty-eight bones of moa", f_008 Doug in
  the cockroach costume over "young cockroach relative", f_014 skull vs BEE HUMMINGBIRD, f_019 "3.5 CM" tail, f_021 the
  map with the red outline, "2021" and STRICTER STOP.
- Doug is on-model everywhere (red cap, white head), including the cockroach costume. The specimens are recognisable: the tick,
  the spider and the fly in the web, the hell ant, the ammonite, the snake skin, the Oculudentavis skull, the hatchling and the
  feathered tail. Text is legible and spelled right. There is no gore: the swollen tick and the "iron from blood" beat have no
  blood read. Nothing looks like a kids' show.
- The thumbnails are unchanged from the Round 2 PASS. Each is readable at 168x94, with Doug and the threat obvious. None is
  misleading against the title.
- Advisory (director, not blocking): f_021 / s205 has no Doug and no death counter. It is a map beat, so this is acceptable.

### Shorts: PASS
- short01 (Lizard): The title pays off ("A LIZARD", scan). The outro opens the nest question without answering it. The end card
  shows a red-outlined toothed bird silhouette (enantiornithine, s178) with "???" and "WHAT LANDED BEHIND DOUG AT THE NEST?".
  The question matches the silhouette.
- short02 (Hell Ant): The title pays off ("PINNED", the cockroach relative held under the horn). The outro sets up the costume.
  The end card shows a hell-ant silhouette with scythe jaws and "DID THE HELL ANT FALL FOR IT?". It is not answered in the clip.
- short03 (Tail): The title pays off (bones, skin, 3D feathers, iron). The end card shows the looming toothed dinosaur head with
  "WHAT CAME WITH THE YOUNG ONE?". It is not answered in the clip.
- In all three, the title is readable, the subtitles are legible, nothing is cut off at the sides, and the red arrow points down
  to the link. The subtitle in short02_preview ("related to cockro") is a mid-word progressive reveal, not truncation. The next
  frames complete the word.
- Advisories (director, not blocking): (1) short03 `tease_asset` feathered_dino_looming shows only a head wedge cropped at the
  right edge, and "???" sits over its eye. It still reads as a toothed dinosaur head, but a full-body adult silhouette would read
  faster. (2) In all three end cards "???" overlaps the silhouette's centre. Nudging the "???" above the silhouette would
  improve recognition. (3) Doug sits very close to the left frame edge in several Short frames (about 20-60 px). He is not
  cropped.

### Technical notes for the showrunner
- QC exit status 1 vs a clean qc.json: `cmd_qc` writes qc.json and then exits with `1 if problems else 0`. A qc.json with
  `problems: []` written at 17:41:14 (the samples are the same timestamp) therefore comes from a run that exited 0. The reported
  exit 1 most likely came from a different step. My best guess is `gate`, which exits 1 while the newest visual-review verdict is
  missing or not a PASS. That was the case before this round. The other possibility is an earlier QC attempt whose output was
  overwritten. Re-run `python -m studio qc 030-trapped-in-amber` and `gate` to confirm. Nothing in the render itself is wrong.
- Duration 655.49 s (10.9 min) is not suspicious. It matches narration.wav (655.56 s, 1,986 words, 199.6 wpm speech /
  181.8 wpm overall with pauses). It is inside `target_minutes: [10, 12]`. The CD's "~10:07" was a word-count estimate made
  before the pauses were added. The video is 1920x1080 with audio and video streams. There are 217 timed shots.
