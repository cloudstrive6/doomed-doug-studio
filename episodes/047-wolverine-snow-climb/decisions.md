# 047 decisions

## 2026-11-14: script gate (draft 3), creative director
Read brief.md, script.md (draft 3), script_review.md (PASS, 0 fact errors) and spot-checked facts.md for the load-bearing lines
(Finland 2013 damages, Swedish per-reproduction payments, several reindeer in quick succession, 562 dens, M56, M3, USFWS ~300).

- **Brief delivered:** cold-open fact with a number in sentence 1, payoff promise (Glacier's highest peak, ninety minutes) by ~0:10,
  "The Reindeer." at words 33-34, the Sweden litter-price twist well inside 45 s. Altitude axis with the four spoken bands, 9 items,
  M3's Mount Cleveland climb last. Counter 356 to 363, survivals at items 4 ("Doug is fine. The cabin is not.") and 5 (narrator
  quietly disappointed), deaths 360 and 363 flat. One costume (reindeer), one "Doug did not agree to this", one 041 callback,
  honesty line ("not known to attack people") early, "NEEDS SNOW." climate close. No Marvel, no kits on screen, no gore, no safety advice.
- **Deviation accepted:** item 7 dropped the Telfer & Kelsall foot-loading claim (facts.md: not supportable) and uses the Finnish agency's
  "several reindeer in quick succession" plus NatGeo "largest feet" instead. Better sourced than the brief's ask; item 7 is the softest
  stop (screener note), not blocking.
- **CD edit (line 141):** dropped "every day" (contradicted "on average") and changed "That's roughly the distance" to "The whole trip is
  roughly the distance" so the New York-Detroit analogy clearly refers to the 800 km, not the daily rate. Re-measured: 152 sentences,
  2,146 words, avg 14.12 (floor 14.0), max 33.
- **For the titler:** working title is delivered; "Why a Wolverine the Size of a Dog Can Kill a Reindeer" is also delivered (item 1 + 7).
  The "1,500 m in 90 minutes" alternate is delivered as spoken (about fifteen hundred meters, about ninety minutes). No "Doug" in the title.
- **For the director:** keep the rule 9 margin in mind; narration splits must not change wording.

SCRIPT: APPROVED

## 2026-11-14: shotlist, director
- 178 shots (s001 thumbnail, 9 chapters, 4 spoken band headers with `topbar: false`), narration = the approved script word for
  word (2,146 words; generator check fails on any mismatch), max 23 words per shot, Doug in 144/178 (81%).
- HUD: counter + `altitude_stake` icon with a red Doug-dot and an "ALTITUDE: FOREST/TREELINE/SNOW/SUMMIT" label at (1628, 238);
  the dot moves only on the spoken band lines (s004, s062, s119, s155). No height number is shown (none is spoken).
- Deaths 357-363: reindeer costume flat on black (s020), wedged in the pines (s041), frozen in the cache with a LEFTOVERS label
  (s060, ice_block "preserved" look with X eyes), on_back under the blown map (s118), cap alone on the snow (s136), Doug-shaped
  snowdrift + cap (s153), cap blown past the summit flag then black (s175). Survivals s079 ("Doug is fine.") and s094-s097.
- Staging reads: "cap sits on the table" is shown without Doug in frame (s078) to keep one cap per frame; Doug sinks knee- then
  hip-deep only (art bible: never surface above the hip), then cap-only. Kits never on screen (den shots are empty or mother only).
- Shorts: short01 s157-s167 (M3's climb, ends "It was a shortcut."), short02 s101-s109 (M56's 800 km walk), short03 s082-s089
  (smelling a carcass through two meters of snow). Titles/descriptions left for the titler.
- 24 new drawings requested in asset_requests.md (geometry pinned; `mount_cleveland` faces and `twin_pines` gap are load-bearing).
- Visual review round 1 fixes (director, 2026-11-14): s015 shows the kit only as a small featureless black silhouette lying at
  the den mouth with the tag string tied to it (screener asked for a blind kit; brief sec 7 keeps kit faces off-screen, so
  silhouette, no new asset); tag enlarged so "200,000 KR" clears the hole. s145 is now a den-chamber close-up (WARM inside vs
  COLD outside) and s146 a surface view of the den mound, breaking the s143-s146 cross-section run. s175 shows the wolverine
  going over the top with no cap on the summit (cap first appears s176/s177); s177 is a closer framing on the cap.

## 2026-11-14: package gate (thumbnails A/B/C), creative director
Read visual_review.md Rounds 3-5 and all three thumbnails at 1280x720 and at 168x94, each with its paired title.
Round 3 failed all three. The CD made the fixes directly with `/tmp/thumbgen/gen_ab_cdfix.py` and
`/tmp/thumbgen/gen_c_cdfix.py 860 438 3.0 1138`. Use those, not the old gen.py, which would undo the fixes.
Screener Round 5: PASS on all three.

- **A, "IT DOESN'T SINK" / "Why a 16 kg Wolverine Can Kill a Reindeer Six Times Heavier": APPROVED.** The reindeer
  is now clearly bigger than the wolverine (the old drawing reversed the "six times heavier" claim) and is fully in
  frame. The reindeer and Doug sit behind a snow lip with cracks, Doug sunk to his eyes. The wolverine stands on the
  crust and casts a paw shadow. The caption is nudged away from the duration badge.
- **B, "IT CLIMBS" / "Why the Wolverine Is the Scariest Small Predator Alive": APPROVED.** Doug is moved off the
  left edge onto the face at a bigger scale (0.67), screaming up at the wolverine on the summit.
- **C, "PER LITTER" / "Why Sweden Pays for the Wolverines That Kill Its Reindeer": APPROVED after the fix.** The
  tag was blank, so the joke was missing (the designer had also flagged this). The tag is now a large upright tag
  with "200,000" in bold black (facts.md: SEK 200,000 per documented reproduction). The US-looking banknote is gone,
  and Doug is smaller and clear of the tag. The thumb text was re-ranked through `package rank` as
  "200,000 PER LITTER". Ranking and pairings are unchanged; `package check` and `validate packaging` return OK.
- Not done (non-blocking screener notes): in C, the string loop hides the wolverine's eye; in B, Doug uses a
  standing scream pose rather than a climbing pose.

PACKAGE (THUMBNAILS): APPROVED
- 2026-11-14: script 3 rounds, art 2 rounds (visual 2), thumbnails 3 screener rounds (C tag size; CD edited), packaged. Risks: global speaking_rate changed 1.15->1.10 by editor (wpm 197); title A resembles 041 formula; M3 name sourced from news/guide pages.

## 2026-11-14: final package gate, creative director
Reviewed: metadata.json (title, alt_titles, description, tags, playlist), build/thumbnail.png (A), build/chapters.txt,
script opening, samples f_001-f_003 (0:00-1:00), visual_review.md Round 7 (PASS main + Shorts), build/qc.json (no
problems). `validate metadata` and `package check --dry-run` return OK. Nothing rendered.

- **Title: keep A**, "Why a 16 kg Wolverine Can Kill a Reindeer Six Times Heavier" (59 chars). It is concrete, the
  claim is delivered in the first sentence and backed by facts.md (about 16 kg vs a cow up to 100 kg), and it is the
  title paired with live thumbnail A in the D4 test. Alt B ("Scariest Small Predator Alive") is good but vaguer and
  belongs to thumbnail B; swapping is not clearly stronger. The "Why a [N kg] [Animal]..." formula echoes 041, but
  041 was six episodes back and 043-046 all use different formulas, so it is not back-to-back.
- **Thumbnail A**: caption readable, the cause (wolverine on the crust, reindeer and Doug sunk) is shown, no gore, no
  cute styling. Not misleading. Screener advisory (wolverine about 15% bigger at feed size) left for a future revisit.
- **Opening**: the wolverine and the reindeer are named in the first sentence (well under 35 words), the payoff
  promise (Mount Cleveland, 90-minute climb) is in the second, and the Sweden bounty twist lands inside 45 s. Frames
  0:00-1:00 are clean: map, 1996 payment, Doug in the reindeer costume, HUD legible, on-model.
- **Chapters**: start at 0:00, 10 entries, all at least 10 s, matching the 9 script items plus intro. The
  `{{CHAPTERS}}` placeholder is filled by studio/youtube.py at upload.
- **Description**: sourced (6 links), disclaimer and AI-use disclosure present, adult-coded, no safety advice.
  Playlist `animals`.
- Non-blocking: f_019 altitude stake overlaps the den entrance (cosmetic).

FINAL: APPROVED
