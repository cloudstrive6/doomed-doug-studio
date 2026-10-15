# Decisions: 019 The Scariest Prehistoric Animals Scientists Drew Completely Wrong

## 2026-10-15: script (draft 2): APPROVED (creative director)
Screener: PASS (hook 8, structure 8, voice 8; 0 fact fails; 3,155 words, about 16:11). I read it against the brief:
- Opening meets 3.2: "Brontosaurus." at spoken word 24, missing-head beat about 0:25, "wearing somebody else's head" about 0:35.
  Thumbnail grid is the opening image.
- The axis is the brief's (Wrong part. / Wrong body. / Wrong animal. / Still wrong.). 11 items, using the Megalosaurus option as a
  survival as allowed. Deaths 155-161; 160 is flat. Boss: Spinosaurus with four cards and a blank fifth.
- All writer corrections to the brief are accepted and sourced: 1932 card instead of 1883, 47 years not "about 70", water plants not
  seaweed, Japanese not Chinese giant salamander, no Dollo credit, Ramskold 1992 reversal, no Brontosaurus mass.
- Overlaps respected: no Velociraptor, Tanystropheus or Megalodon; Anomalocaris is one clause; no Deinonychus toe.
- Policy: every death cuts away, the Allosaurus wound is "a piece missing", no mockery of Scheuchzer, adult tone. The Dimetrodon
  card is a gift-shop shelf.
- Would I click and keep watching: yes. Every item flips a picture the viewer already holds, and the stack of four Spinosaurus
  cards is a strong boss.

Notes for the next stages (not blocking):
1. Director: ping-pong tables are the scale object twice (Megalosaurus L176, salamander L346). Draw them clearly differently
   (two tables end to end vs. one table seen from the end), or swap one visual only.
2. Director: before drawing the Iguanodon closing shot, check the 2026 Crystal Palace renovation status (screener rec. 3).
3. Writer/editor may optionally improve L188, "Being too strange to eat turns out to be a survival strategy." It doesn't follow the
   ladder beat; "out of reach" would. This is optional polish only, so don't re-screen for it alone.
4. Titler: the screener prefers "Creepiest" over "Scariest" (worm, salamander). It's your call. Keep "Dinosaur" out of the title and the
   thumbnail labels. The banned list in brief section 1 applies.
5. Shorts: Brontosaurus Short uses **47 years** (Carnegie 1932-1979), not 70.
6. Art: the OLD DRAWING cards are our own redraws. Public-domain plates (L3) only after the director checks the licence.

## 2026-10-15: shotlist (director)
293 shots, narration matches the approved script word for word (3,155 words, ~16:25), Doug in 97% of shots, max 22 words a shot,
no planned static stretch over ~4.6 s. 68 new drawings requested in `asset_requests.md`; shots are laid out to the sizes given there
(checked with placeholder boxes).
- **Crystal Palace check (note 2):** the park's restoration was finished in July 2026. Historic England took the sculptures off the
  Heritage at Risk Register, and they were repainted "using colours based on their original Victorian appearance" (ianVisits,
  16 Jul 2026; Time Out; Inside Croydon). No source says the horns were removed or changed, and a Victorian-appearance restoration
  keeps them, so L86 "still there today" is not contradicted. The closing shots s059-s060 show both statues with nose horns. If the
  horns ever change, the line needs a date.
- **Ping-pong tables (note 1):** `ping_pong_table` is a side view of the LENGTH (s126: two end to end under the Megalosaurus, at
  150 px/m) and `ping_pong_table_end` is an end view of the WIDTH (s255: the salamander lying across it). They are separate drawings.
- **Severity backdrop ramp:** the OLD DRAWING card wall darkens one step per spoken band, and luminance falls every step: Wrong part
  `#f4f1dc`, Wrong body `#e8dcc0`, Wrong animal `#d9c49a`, Still wrong `#4a3a34`. Time-machine scenes use the art-bible
  environments (surface sea `#3a9ad9`, Cambrian `#7cc6e6`). The section headers are white cards in the night museum hall.
- **Persistent counter** "DOUG DEATHS: N" is on every shot from s002, starting at 154. Each death shot shows the new number popping in
  at the impact (155 s032, 156 s085, 157 s109, 158 s185, 159 s208, 160 s237 flat, 161 s289). Every death keeps the cap in frame.
  Survivals hold the counter.
- **Alive on_back** (art bible, from 010): Doug lies on his back alive in s182-s184 ("the 1977 way") and s256-s257 (next to the slab).
  The counter does not tick there.
- **Elasmosaurus (s082-s084):** the stage direction says the head rises "far behind him". Logically he swims toward the long end, which
  is where the head is, so the body sits behind him (left) and the neck runs under him to the head rising ahead (right). Silhouette
  with red rim in s083, then the full reveal in s084.
- **Spinosaurus mystery:** `spinosaurus_mystery` stays a red-rimmed silhouette (s286, s288) and is never revealed in colour. That is
  the joke ("the version nobody has drawn yet"), and it is a deliberate exception to the silhouette-then-reveal rule.
- **Gary Larson / Far Side (s099-s100):** we never draw the panel or a caveman. It's a blank chalkboard, the year, a pencil and then
  THAGOMIZER in chalk.
- **Public-domain plates (note 6):** none are used. Every OLD DRAWING is our own sepia redraw (`old_*` assets).
- **Shorts:** short01 Brontosaurus s010-s024 (the 47-year Carnegie skull, per note 5), loop = Doug's fate (s032). short02
  Dimetrodon s195-s207 ("further from T. rex than T. rex is from you", then "it's family"), loop = where his cap ends up (s208).
  short03 Spinosaurus s276-s287 with a 15 m hook, loop = the shape that matches none of the cards (s288). Titles are left for the
  youtube-titler.

## 2026-10-15: thumbnail A vs B: KEEP A (grid) (creative director)
- **Chosen:** `thumbnail.json` (Archetype A, 11-tile grid of crossed-out OLD drawings). `thumbnail_b.json` (FAKE HEAD card) stays
  on file as the alternate for a later Test & Compare. Nothing was copied.
- **Why A:** (1) It passed visual screening, and style bible 3.2 requires the grid to be the opening image, so the click carries
  straight into the first frame. B does not match the opening. (2) It delivers what the title promises, "Prehistoric Animals"
  plural: eleven wrong drawings, eleven red X's and a '?' on Spinosaurus that teases the finale. B sells only item 1 (Brontosaurus,
  about 2 of 16 minutes), so it under-promises the list and risks a viewer who came for that one item leaving after the reveal.
  (3) A uses the proven ranking/list formula for this stage of the channel. B is the weaker archetype C.
- **B's strengths noted:** it reads better at feed size (2 huge words, one subject) and has Doug for scale. It's the first
  candidate to try if A's CTR comes in below the channel median after 48 h.
2026-10-15: 019 packaged. Script 2 rounds (7 small fixes), assets 1 round (68 approved), keyframes 2 rounds. Risks: ö/Ö font glyphs and pronunciations unverified in narration.wav (Ramsköld, Öhningen, Scheuchzer, Rozhdestvensky); Crystal Palace horn claim depends on post-2026 restoration.

## 2026-10-15: final package (creative director)
Reviewed: `metadata.json` (title, alts, description, tags, playlist), `build/thumbnail.png` + `thumbnail_small.png`,
`build/chapters.txt`, script L1-60, samples f_001-f_003 (15/45/75 s), `reviews/visual_review_postrender.md`, `build/qc.json`
(985 s, no problems). `validate metadata`: OK. `{{CHAPTERS}}` is filled by `studio/youtube.py` at upload.

**Package: APPROVED on its merits.**
- **Title kept:** "The Creepiest Prehistoric Animals Scientists Drew All Wrong" (59 chars, T4). No alt is clearly stronger:
  "Scariest...Completely Wrong" is the same promise at the 65-char limit (truncation risk on mobile), "How Every...Would Kill Doug"
  over-promises deaths (4 of 11 are survivals), "Each Museum" is narrower than the content, and "Fossils" repeats 005/015.
  Different clause from 017's T4 and not back-to-back with 018's T8. No "Dinosaur", nothing banned by the brief.
- **Honesty:** delivers 11 old drawings, each flipped to the real animal, ending on the one still being redrawn. The softest fit is
  Dimetrodon (the popular "dinosaur" label rather than a scientist's drawing), but the 1878 card and the "Wrong animal." band
  frame it fairly, so it is not a broken promise.
- **Thumbnail:** the 11-tile grid with red X's and a '?' on Spinosaurus reads at 320 px. Labels are chapter names only, with no title
  words, and it is the opening image (style bible 3.2). Screener PASS. Kept over B (see the earlier entry).
- **Opening:** "Brontosaurus" is the 25th spoken word, and it is on screen with the OLD DRAWING card by 15 s. The twist (borrowed head)
  lands well inside 45 s. f_002/f_003 show the 1903 rename and the 1979 head swap with the counter visible, which keeps the pace. I
  would click and keep watching.
- **Description:** the first two lines sell four concrete twists plus the unsolved boss with no spoilers. The comment prompt,
  sources (Carnegie, NHM, ROM, NatGeo x2, Field Museum), cartoon-death disclaimer and AI-use disclosure are all present. Hashtags
  and tags are adult/science-coded. Chapters are 11, start at 0:00 and match the items.
- **Policy:** cartoon deaths that cut away, no gore, no medical/safety content, nothing kid-targeted.

**Not approved yet: the render.** The post-render visual screener FAILed the main video (DOUG DEATHS counter clipped by zoom in
s092/s098/s108/s139/s143/s250, label border shaved in s007/s015/s043) and short03 (Spinosaurus end-card silhouette unreadable).
Fixes are in shotlist.json/shorts.json and a re-render is queued. Before upload, the re-rendered final.mp4 and short01-03 need a
visual-screener PASS that confirms: (1) the counter's full digits in the last frames of those 9 shots, (2) a recognisable short03
end card, (3) qc.json clean. After that the episode can go to upload with this package unchanged; no further CD review is needed
unless the screener finds something new.
Open editor risk carried from packaging: confirm ö/Ö glyphs and the pronunciations of Ramsköld/Öhningen/Scheuchzer/Rozhdestvensky
in narration.wav.

FINAL: REJECTED pending re-render verification

2026-10-15 final review round 1: visual screener FAIL (main: death counter clipped in s007/s015/s043/s092/s098/s108/s139/s143/s250; shorts: short03 end-card silhouette). Fixed via camera.x=960 and tease_asset spinosaurus_mystery_tease; .rerender requested (final, shorts). Stage left at packaged.
FINAL: REJECTED pending re-render verification

2026-10-15 visual screener post-render round 2 (re-render verified from final.mp4 and short01-03):
VERDICT (main): PASS - DOUG DEATHS counter fully visible with all digits and intact borders in the last frames of s007/s015/s043/s092/s098/s108/s139/s143/s250; 33 samples have no black, frozen or glitched frames; qc.json clean; thumbnail unchanged and readable.
VERDICT (shorts): PASS - short01-03 titles, subtitles and down arrows are legible and nothing is cropped; the short03 end card is a recognisable Spinosaurus silhouette (croc snout, long neck, spined sail, waterline) that matches "WHICH SPINOSAURUS CAME OUT?" and is not answered in the clip. Advisory: the "???" covers the middle of the silhouettes; move it off the shape in future.

## 2026-10-15: final package, round 2 (creative director)
Re-checked: title and description in `metadata.json` (unchanged since the round 1 approval), `build/thumbnail_small.png`,
`build/chapters.txt` (11 chapters from 0:00, they match the items and the {{CHAPTERS}} slot), script opening, samples f_001/f_002,
the round 2 post-render visual screener section (main PASS, shorts PASS) and `build/qc.json` (985 s, problems: []).
- **Title:** "The Creepiest Prehistoric Animals Scientists Drew All Wrong" is unchanged and still delivers the full 11-item list.
- **Thumbnail:** unchanged grid. It reads at 320 px, with 11 red X's and the Spinosaurus '?', and it matches the opening image.
- **First 60 s:** f_001 shows the BRONTOSAURUS label, the OLD DRAWING card with the '?' on the head and the counter at 154 with its
  border intact. f_002 shows the 1903 rename beat. The item name and the twist are both on time (style bible 3.2).
- **Round 1 render blockers resolved:** the counter is unclipped in all 9 shots, the short03 end card is recognisable, and qc is clean.
- **Carried (non-blocking):** the editor never explicitly confirmed the pronunciations of Ramsköld, Öhningen, Scheuchzer and
  Rozhdestvensky. The owner should listen for them during the 18 h review window. The screener's "???" placement on end cards
  is an engine/director follow-up for future Shorts.
Series bible already logs 019 (total 161). Episode log status updated to "package approved, final".
FINAL: APPROVED
