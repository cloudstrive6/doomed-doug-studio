# 049 decisions

## 2026-11-16, creative director: episode chosen, brief written
- 049 = backlog #112, giant hornets (8.0). This confirms CD decision 3 in `data/insights/2026-11-15.md`. It deliberately overrides the playlist default:
  047 and 048 are both `animals`, and the default pick, #55 plants (6.3), has no engine. #111 great white vs orcas (8.7 in `topics`) is held so that
  it comes at least 3 slots after 048.
- Axis: size of the target (BEE, HIVE, DOUG, NORTH AMERICA). It is not a distance axis, because 043 and 048 both used distance.
- Title numbers (30 / 30,000 / afternoon) are provisional until they are sourced. The title changes to match the sources.
- 050 must leave `animals`.

## 2026-11-16, creative director: script approved (draft 2 + screener round-2 fixes)
- Verified fix 1 (line 9): "Later, Doug holds open a tree that could have produced nearly two hundred hornet queens." 15 words; "The Hunter." still at spoken words 34-35.
- Verified fix 2 (line 167): "But here's what the scary reputation leaves out." No remaining "nickname" reference; marker unique.
- Advisories (line 239 "straight", line 55 corner-shop analogy) left to the director/editor's discretion; not blocking.
- Stage -> script_approved after 3 screening rounds. Deaths 369-374 go into the series bible when the episode ships.

## 2026-11-16, director: shotlist
- 202 shots (s001 thumbnail ref, 2,013 spoken words matching the approved script exactly), 9 chapters, Doug in 82% of shots.
  Generator: `episodes/049-giant-hornet-slaughter/build/gen_shotlist.py` (build/ is git-ignored; regenerate from it before editing by hand).
- HUD: counter at (1590,162) plus THE TARGET (`the_target` icon at 0.2 + size-28 label "TARGET: ..." at (1590,238)). BEE from s002,
  HIVE from "One hive." (s047), DOUG from "One person." (s113), NORTH AMERICA from "One continent." (s154), stamped red-on-pink from death 374 (s193).
- Item palette (severity, light to dark): Hunter day meadow `#cfe9ff`/`#7cc25a`, Mark `#8fd3ff`/`#6fb24f`, Slaughter afternoon `#f6c45a`/`#b8913a`,
  Occupation dusk `#e88a4a`/`#9a7a4a`, Heat Ball `#8a6a8a`/`#5a4b3d`, Sting overcast forest `#b9c4a8`/`#5d6b45`, Toll sober cards `#15181a`,
  Hitchhiker night `#1b2f5a`/`#2b3d33`, Nest pre-dawn `#0b1020`/`#141e1a`. Diagram cards cream `#f4f1dc`; hornet nest interior `#d8cfbd`; hive interior `#e9b64a`.
- **One-off `cap_off` (logged per art bible):** The Toll s150-s153, Doug holds his cap in both hands (script stage direction); `doug_cap` is
  drawn at his hands, so exactly one cap is on screen. Sober item: no death, no joke, counter stays 372.
- Deaths: 369 meat ball bundle with the cap (no body); 370 `bee_costume_flat` + cap among X-eyed bees; 371 `hornet_costume_flat` + cap + steam;
  372 `on_back` dead + `beekeeper_suit_on_back`; 373 `on_back` dead behind the NO HORNETS sign; 374 empty hollow + vacuum hose + ghost.
- Shorts: short01 Heat Ball s093-s107 (ends on the 4-degree margin), short02 Nest s175-s187 with hook (ends on "nearly two hundred queens"),
  short03 Slaughter s049-s059 (ends "killed one by one"). Titles/descriptions left to the titler.

## 2026-11-16, creative director: package review (thumbnails A/B/C + ranked titles), CHANGES REQUIRED
Titles: all three are sourced (NYT 1995 Ono group: 20-30 hornets / 30,000 bees / 3 h / up to 40 bees a minute; WSU FS347E: larvae fed the paste),
and the script delivers each one (lines 29, 77, 109). No misleading promise.
No visual-screener report covers the thumbnails yet (visual_review.md only lists s001 as "pending"), so the package can't be approved until one exists.
- **A ("Why 30 Giant Hornets Can Kill 30,000 Bees in an Afternoon" / ONE BY ONE): I'd click. Approved.** The jaws are the hook, the X-eyed pile is
  cartoon-safe, and Doug's scream sells the scale. Non-blocking: the head-on hornet reads a little like a bumblebee. A small amount of black/orange
  abdomen striping showing behind the head would help.
- **B ("Why One Giant Hornet Can Kill 40 Bees a Minute" / IT BRINGS FRIENDS): I'd click. Approved.** This is the best Doug-in-peril image of the set:
  his deadpan face next to the side-on hornet, with the arriving line as the payoff. Text is legible at feed size.
- **C ("Why Giant Hornets Can Kill 30,000 Bees to Feed Their Young" / BABY FOOD): I wouldn't click. Required changes:**
  1. The larvae read as eggs or dumplings wearing brown hats. Draw them as grubs with their heads out of uncapped cells, mouths open and facing the hornet.
  2. The bundle reads as a potato or rock. Give it a bee-striped, chewed texture so it reads as "bees" with no visible parts (keep it gore-free).
  3. The hot pink background plus cute grubs plus "BABY FOOD" leans nursery. Switch to the nest-interior/dusk palette (`#d8cfbd` / `#9a7a4a` from the
     shotlist) so the tone stays adult-coded.
  4. Doug is a bystander. Put him in the bee costume next in line, with one larva turned toward him (the "you're next" joke). Keep the cap on.
  5. The bundle hides the hornet's face. Move it lower so the head and jaws are clear.
- Next: the graphic designer revises C, then the visual screener checks A/B/C (feed size and policy), then the package comes back to me. A and B
  don't need to come back unless the screener flags them.

## 2026-11-16, creative director: package re-review (revised C, tweaked A, B unchanged): CREATIVE APPROVAL, gate still waits on the screener
I looked at all three at 1280x720 and at feed size (168 px), each next to its title. The titles have not changed since the last review
and are still sourced and delivered.
- **A ("Why 30 Giant Hornets Can Kill 30,000 Bees in an Afternoon" / ONE BY ONE): approved.** My non-blocking note is done. The black/orange
  striped abdomen now shows behind the head, so at 168 px it reads as a hornet, not a bumblebee. The jaws are still the focal point, the X-eyed
  pile is still whole cartoon bees, and Doug is still screaming at the edge. I'd click.
- **B ("Why One Giant Hornet Can Kill 40 Bees a Minute" / IT BRINGS FRIENDS): approved, unchanged.**
- **C ("Why Giant Hornets Can Kill 30,000 Bees to Feed Their Young" / BABY FOOD): approved. All 5 of my changes are done, and so are the screener's.**
  1. The larvae are now segmented white grubs coming out of uncapped cells, with dark open mouths. They read as hungry, not as eggs. Done.
  2. The bundle is a chewed lump with bee stripes and no visible parts. It reads as "bees" and stays gore-free. Done.
  3. The hot pink is gone. The dark nest-wall brown over a brown comb is darker than the `#d8cfbd` I asked for, but that serves the intent
     better: grim and adult-coded, with no nursery read even with "BABY FOOD". Done.
  4. Doug is in the bee costume with the cap on, sweating, at the end of the row, and the third larva is turned toward him. The "you're next"
     joke lands. Done.
  5. The bundle hangs below the mandibles with background between them, so the head and jaws are clear. Done (this also covers screener item 3).
  - Screener item 1 (crop): I measured the yellow fill of "BABY FOOD". It ends at x 1204, which leaves about 60 px of right margin even with
    the outline. Fixed.
  - I'd click this now. "Feed Their Young" leads into "BABY FOOD" and on to the grub looking at Doug, which is the strongest curiosity gap of the three.
- Order stays as ranked: A is the primary title and thumbnail, and B/C are the test arms.
- **Gate condition:** the last visual-screener verdict on thumbnails is FAIL (on the old C), and A has changed since then. The visual screener
  must re-check A and C (feed size, crop, policy) and record PASS in `visual_review.md` before the stage moves to `packaged`. If the result is a
  PASS with polish notes only, this approval stands and the package doesn't need to come back to me. If it is a FAIL, the package comes back
  to me after the fixes.
- 2026-11-16 showrunner: script 3 rounds (writer/screener, CD approved), art 3 rounds (art-director+visual-screener), thumbnails 2 rounds (C redesigned). Risks: title numbers per 1995 NYT (kill count varies by source, 5k-25k in ABJ); Japan deaths stated as 'about 20/yr'; short03 title near-duplicates alt title B. Mistake: stage briefly set to packaged early and reverted to art_approved.

## 2026-11-16, creative director: final package approval
I reviewed the title, thumbnail A (`build/thumbnail.png`), the description and tags in `metadata.json`, `build/chapters.txt`, the opening of
`script.md`, samples f_001-f_002, and the post-render report in `visual_review.md`. Thumbnails and Shorts got a PASS. The main video's only FAIL
is the counter clipping in 5 shots. That is a render issue, not a packaging one. I checked `shotlist.json`: s006/s011/s041/s110/s176 now have
`camera.x` 960, and `.rerender` lists final + shorts. The visual screener still has to re-check those 5 last frames in the new `final.mp4` before
upload.
- **Title: keep "Why 30 Giant Hornets Can Kill 30,000 Bees in an Afternoon".** It is sourced (NYT 1995: 20-30 hornets, 30,000 bees, 3 h) and the
  first spoken line delivers it, in under 20 words. None of the alt titles is clearly stronger. "40 Bees a Minute" is the B test arm and nearly
  duplicates short03's title, so it can't be the primary.
- **Thumbnail A:** one focal point (jaws), the hornet reads as a hornet at feed size, the bees are whole and X-eyed with no gore, and Doug's
  scream gives the scale. It doesn't repeat the title's numbers. It is also the s001 opening image. I'd click.
- **First 60 s:** the thumbnail is held 1.5 s, then the promise and the payoff line (the Washington tree, ~200 queens). "The Hunter." lands at
  words 34-35. Item 1's twist (the hornet doesn't eat the bee; the larvae feed the adults) comes well within 45 s. f_002 (larva cells,
  confused Doug) is clean.
- **Description:** the first two lines restate the hook with no overpromise. The sources are listed, the AI-use and cartoon-death disclaimers
  are present, there are 3 hashtags, and it says nothing for kids. **Chapters:** 10 entries starting at 0:00, each ≥10 s, and the last one
  (9:32) falls inside the 11:20 runtime. Camera-only fixes don't change the timing, so the chapters stay valid after the re-render.
- `validate metadata` and `validate packaging`: OK. Playlist `animals`, so 050 must leave `animals` (brief decision).
- Series bible: deaths 369-374 are logged when the episode ships, as decided at script approval.
FINAL: APPROVED
- 2026-11-16 showrunner final review round 1: visual VERDICT (main) FAIL (DOUG DEATHS counter clipped in s006,s011,s041,s110,s176); camera.x set to 960; .rerender final+shorts requested. Shorts PASS. CD package approved. Stage left unchanged pending round 2.
- 2026-11-16 showrunner final review round 2: round-1 counters (s006,s011,s041,s110,s176) fixed, Shorts PASS, thumbnails PASS. visual VERDICT (main) FAIL: s029 and s061 (zoom 1.06, camera.x 900) still clip the DOUG DEATHS counter (s061 also clips Doug's bee-suit). Fix: camera.x 900 -> 960 in both. Round 2, so no further re-render requested here; stage left at built. Needs a manual or next-run shotlist fix + re-render.
FINAL: REJECTED visual screener main FAIL (counter clipped in s029, s061; camera.x 900 -> 960)
- 2026-11-16 showrunner final review (round 3 prompt): s029/s061 were still camera.x 900 in shotlist.json; set both to 960 (y, zoom unchanged). .rerender = final (Shorts unaffected, PASS). Stage left at built; needs round-4 visual re-check of s029/s061 last frames.
FINAL: REJECTED visual screener main FAIL pending re-render (s029, s061 camera.x fixed to 960 in shotlist)

## 2026-11-16, creative director: final package approval, round 2 (after the s029/s061 re-render)
Since my first approval, only camera.x changed (s029 and s061 are now 960 in `shotlist.json`, and I confirmed that). That can't affect packaging or timing.
- Visual screener post-render round 2: VERDICT (main) PASS, VERDICT (shorts) PASS. The DOUG DEATHS counter has about 55 px of margin in s029/s061, and the bee suit is fully in frame. `qc.json` problems: [], and the duration is 680.506 s (11:20.5).
- **Title** "Why 30 Giant Hornets Can Kill 30,000 Bees in an Afternoon": unchanged, sourced, and the first spoken line delivers it. Keep.
- **Thumbnail A** (`build/thumbnail.png`): unchanged. One focal point (the jaws), whole X-eyed cartoon bees with no gore, Doug for scale, and "ONE BY ONE" doesn't repeat the title. I'd click.
- **Description:** unchanged. The hook has no overpromise, 6 sources, the cartoon-death and AI-use disclaimers, 3 hashtags, and nothing kid-directed.
- **Chapters** (`build/chapters.txt`): 10 entries starting at 0:00. The last one, "9:32 The Nest" (572 s), runs about 108 s to the 680.5 s end. Every chapter is ≥10 s and all fall inside the runtime.
- **First 60 s:** the thumbnail is held 1.5 s, then the promise line and the payoff line (the Washington tree, ~200 queens). "The Hunter." is at words 34-35, and the twist (no eating, a meat ball for the larvae) lands well inside 45 s. In f_001 the hornet is labelled NORTHERN GIANT HORNET with LARGEST below it, Doug is on-model in the bee suit, and the counter reads 368. f_002 shows the larva cells, the meat ball and a confused Doug. Both are clean and adult-toned.
FINAL: APPROVED
