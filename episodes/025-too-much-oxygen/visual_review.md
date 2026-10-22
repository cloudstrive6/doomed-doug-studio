# Visual review: 025-too-much-oxygen

## Round 2: re-rendered keyframes + thumbnails (2026-10-22)

Scope: the 80 re-rendered keyframes (contact sheets 01–07: s002–s005, s013–s014, s025–s030, s043–s044, s048, s056,
s061, s065, s069, s075–s076, s088–s090, s093–s094, s103, s107–s109, s113, s116, s120, s124–s126, s138, s140–s142,
s157–s158, s161–s162, s164, s172, s174, s177, s185, s192, s198, s210–s213, s215–s217, s222, s225–s226, s228–s229,
s231, s234, s236–s238, s247–s257, s259), checked against the round-1 fixes and for regressions. I also screened all
three thumbnails at full size, in `smalls.png` and at feed size (`feed168.png`, 168x94).

**VERDICT: PASS**

All seven round-1 blockers are fixed, and I found no new blocking problems.

### Round-1 blockers: status
1. s030: fixed. The ghost Doug now floats in open sky with his full body visible, and the only other cap is the one on the fern. The dismemberment read is gone.
2. s211: fixed. "HUGE TEETH" sits clear of the meter.
3. s213: fixed. "LARGE EYES" is clear of the meter.
4. s162: fixed. "AIR" reads clearly and the blue arrow hits the plates.
5. s093: fixed. "PIERCING BEAK" is clear of the meter box.
6. s094: fixed. "EXTRA FLAPS" is clear and the arrow is aimed at the front flap.
7. s090: fixed. "309 MILLION YEARS AGO" is fully visible.

### Round-1 should-fix and variety items: status
Fixed: s061 and s140 (meter clear), s125 and s126 (frame clear of the meter), s069, s177, s157, s158, s236, s229 (stale bracket removed),
s210 (the 1.6 M marker is gone and the 2–3 M bracket stays), s259, s013, s014, s198, s215, s228, s231, s044, s120, s027, s141, s142,
s056 (Sumatra label added, dashed line now starts below the tag, and a Doug stack gives scale), s043 (now a winged mayfly), s075 and s076 (rope
barrier with posts), s138 (wings-spread bat), s109 (fern-and-insect scene breaks the cross-section run),
s113 (close-up), s116 (larger hand). The meter is now hidden in the cold open (s002–s005).

### Non-blocking notes (fix if touched again)
- **s002 (director):** the right-hand "O2" (about x 1150, y 420) now sits on the branches of the right tree crown. Move it about 120 px up into open sky.
- **s140 (illustrator/director):** the net handle ends at Doug's cap brim, about 50 px above his raised hand. Snap the handle end to the hand.
- **s250 (director):** the fern saddle floats beside Doug's outstretched hand rather than in it. Move it about 60 px left and down onto the hand.
- **s056 (director):** the top Doug in the depth stack is cropped at the frame edge. This is acceptable as "keeps going", but one fewer Doug, or a small "x9" label, would make it read more clearly.
- **Size meter (art director, carried over from round 1, item 31):** the tape icon is still unreadably small at scale 0.16.

### Thumbnails

**A: `thumbnail.png` ("AIR DID THIS?", Arthropleura head-on + Meganeura, Doug): PASS (recommended lead).**
At 168x94 it has one clear focal point: the giant segmented bug fills the right half and Doug's red cap stands out against the lime background.
The text is fully legible at feed size and repeats no title word. It complements the title well: the title gives the oxygen cause and the image
shows the giant bugs blamed on it. There is no gore and it does not look like a kids' show. Minor issue: the Meganeura shrinks to a thin blue stroke
at feed size, so it adds little but does no harm.

**B: `thumbnail_b.png` ("GULP", Crassigyrinus jaws below the waterline, Doug above): PASS (weakest of the three).**
It is readable at feed size with one focal point, the teeth and eye. There is no gore; the teeth are cartoon. It is not misleading,
because Crassigyrinus is a full chapter. However, the title promises **bugs**, and this shows an amphibian that reads at 168 px as a crocodile or frog, so the
title and image pull in different directions, and "GULP" does not connect to oxygen. I expect the lowest CTR of the three. Keep it in the test only as the
contrast arm (graphic designer, optional).

**C: `thumbnail_c.png` (2x3 labelled grid: Griffinfly, Spider, Scorpion, Tadpole, Beak, Millipede): PASS.**
This is the house archetype A. All six labels are legible at 168x94 and there are fewer than 12 tiles. Each creature is recognisable in its tile except Tadpole,
which reads as a croc-like head at feed size; that is acceptable with the label. There is no gore. "Spider" is the chapter name and the
misconception the video unpacks, so it is not misleading. Minor issues: the pastel pink and purple tiles combined with the rounded Comic font are the closest of the three to a
kids-show look, and the six repeated Dougs add clutter. Optional (graphic designer): drop Doug from the tiles or keep him in only one.

No gore or policy risk in any variant. None of them copies competitor drawings or wording.

## Thumbnail re-screen (revised set, 2026-10-22)
Checked at full size and at feed size (`build/feed168.png`, rebuilt after the thumbnails). **VERDICT: PASS (A, B, C).**

- **A ("AIR DID THIS?", Arthropleura + Meganeura, Doug): PASS, still the recommended lead.** It has one focal point, and the text and Doug's red cap read at 168 px. The Meganeura now perches on the millipede's back, so it reads at feed size as one threat instead of a stray blue stroke. It shows no gore and doesn't look like a kids' show. It complements the title and repeats no title word.
- **B ("THIS FLEW", Meganeura wings spread, Doug grimacing): PASS.** This is a clear improvement on "GULP". It now shows a bug, which matches the title's promise, and "THIS FLEW" is legible at feed size. It has one focal point and no gore. Non-blocking: the wingspan is drawn at about 4-5 times Doug's height, while the video's tape measure says "ABOUT 70 CM". The body overlapping the foreground strip makes this read as forced perspective, which is normal genre exaggeration, so it isn't misleading packaging. It is the least threatening of the three, so I expect it to have the lowest CTR (graphic designer, optional: open Meganeura's jaws or angle it toward Doug).
- **C (2x3 labelled grid): PASS.** All six labels are legible at 168 px. Doug now appears only in the Millipede tile, which removes the clutter flagged in round 1. Its creatures stay recognisable, and Tadpole is carried by its label. It shows no gore. The rounded font and pastel tiles remain the closest of the three to a kids-show look, but this is acceptable.

None of the variants has a policy risk or misleading claim, and none copies competitor wording or drawings.

## Post-render screen (final.mp4, thumbnails, Shorts), 2026-10-22
I checked all 32 samples in `build/samples/` against the shots they land in (ffmpeg samples at t = 15 s, 45 s, ... so f_n is (n-1)*30+15 s), all three thumbnails at full size and at 168x94, the four Shorts previews, and frames from each Short (0.5, 3, 15 and 25 s, then six frames across the last 9 s).

VERDICT (main): PASS
VERDICT (shorts): PASS

### Main video
- I found no black or blank frames, glitches, frozen shots or garbled drawings. The death counter runs 203 to 210 in order, and the size meter steps from "SMALLER THAN A DOT" to "40 CM", "54/55 CM", "ABOUT 70 CM", "1.6 M", "DOUG-SIZED", "ABOUT 2.6 M" and "DOUG" in step with the chapters. Doug is on-model (red cap, white head) and readable in every frame. Chapter headers are spelled correctly and not cropped.
- Pictures match the narration: f_011 PALAEODICTYOPTERA label (s092), f_018 sea scorpion vs cat vs Doug-for-scale, f_021 Fife map, f_024 "CHECKED: 1" (s196), f_028 split sandstone block, f_030 oxygen curve with PEAK (s242), f_031 millipede vs car, f_032 time booth with the comments CTA (s260).
- Some frames look empty because their labels pop in later in the shot: f_014 "FINE", f_015 "TODAY: ABOUT 19 CM", f_020 "SMALL OPENINGS", f_023 "WET GILLS", f_030 "NOT ONLY OXYGEN", f_032 "TELL US IN THE COMMENTS". This is expected.
- No gore or kids-show tone. Death 205 (s087, f_011 area) is a cartoon splash.

Non-blocking (fix only if touched again):
1. **s123 (director):** the "65 TO 75 CM" label sits on the end of the griffinfly's abdomen (f_015, about x 270-480, y 480-530 at 1080p). Move the label about 80 px down, or right, clear of the body.
2. **s165 (director/illustrator):** before "SMALL OPENINGS" pops in, the book-gill covering plate reads as a plain brown box with a black slot (f_020). Bring the label in at appear 0.0-0.2, or add a faint outline of the scorpion's body around the plate.
3. **Size-meter tape icon (art director, carried over):** still unreadably small. Every frame shows a smudge at about x 900, y 160.

### Thumbnails
These are the same files as the 18:36 re-screen (A/B/C regenerated with the render; no visual change). **A: PASS** (lead). One focal point; "AIR DID THIS?" and Doug's red cap read at 168 px. **B: PASS. C: PASS.** None is misleading, and none repeats a title word against `metadata.json`'s title "When Earth Had So Much Oxygen That Bugs Could Kill Doug".

### Shorts
- **short01** "The Largest Spider Fossil Ever Found Wasn't a Spider" (45.3 s): pays off its title (museum spider, then "FRESH WATER" sea scorpion with BLADES). The outro leaves Doug in the splash. End card: "WHERE DID THE RIVER TAKE DOUG?", red-outlined eurypterid silhouette with "???" (recognisable: plated body, bladed limbs), and the arrow points down. Unanswered. PASS.
- **short02** "A Fallen Cliff Revealed a Millipede as Big as a Car" (40.3 s): cliff fall, then sandstone block, then Arthropleura vs car (pays off). End card: "DID DOUG GET HIS RIDE?" with a long, segmented, leg-fringed millipede silhouette. Recognisable at full size, though thin. Unanswered. PASS. Optional (director): scale `tease_asset` arthropleura up about 1.3x so the "???" covers less of the body.
- **short03** "Six Meters of Sea Scorpion Footprints Were Found on Land" (47.0 s): trackway with "6 M OF FOOTPRINTS", then Hibbertopterus walking out of the water (pays off). End card: "DID IT WALK OVER DOUG?" with a Hibbertopterus silhouette. Unanswered. PASS.
- **short04** "This Giant Dragonfly Ruled a Sky With No Birds in It" (35.4 s): wingspan vs wheel vs Doug, then "NO BIRDS YET" (pays off). The clip ends at the tree top. End card: "HOW FAR DID DOUG FALL?" with a clear red dragonfly silhouette. Unanswered. PASS. Minor: at 25 s Doug in the scale-tree crown (s143 area) is a few pixels of red among the fronds on a phone; acceptable.
- In all four, title text is legible, burned-in subtitles are white with a dark outline and readable, the 16:9 art band is not cut at the sides, and the end-card arrow points down to the link.

### Technical notes on the QC exit 1
`build/qc.json` (written 18:41:37, after `final.mp4` at 18:36:23 and all 32 samples) lists `problems: []`. `cmd_qc` only calls `sys.exit(1)` when `problems` is non-empty, so **this run's qc.json cannot come from a process that exited 1 through the QC checks.** I re-verified every check independently:
- Duration 964.5 s = 16.1 min (target 15-18, accepted window 12-27): OK.
- 1920x1080 @ 60/1 fps (config fps 60), video + audio streams: OK.
- timing.json: real_voice true, wpm_speech 197.6 (185-215 allowed): OK.
- `thumbnail.png` and `captions.srt` present: OK.
- Integrated loudness -14.3 LUFS, LRA 2.7 LU (target -14; qc doesn't check loudness): OK.
- Shorts: all four are 1080x1920 with audio, 35-47 s.

Likely explanations: (a) an earlier `qc` invocation failed (for example, while `final.mp4` was being written, or before the Shorts render freed the disk) and its qc.json was overwritten by this clean re-run; (b) the exit status belonged to a chained step, e.g. `studio gate`, which exits 1 when there is no post-render screener verdict yet (true until this section was appended); or (c) the qc output was piped (`| head`) and the final `print` raised BrokenPipeError after qc.json was written. Re-running `python -m studio qc 025-too-much-oxygen` (no render needed) should exit 0. If it does not, capture stderr.
