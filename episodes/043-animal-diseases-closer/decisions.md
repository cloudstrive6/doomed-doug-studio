# 043 decisions

## 2026-11-10, creative director: brief
- Picked #108 (zoonotic diseases, `parasites`). The lane rule makes it the default alternative because 041 and 042 were both `animals`.
  #40 (rabies) is folded in as the boss.
- The title is T4 with no "Doug" (experiment ep 3 of 3). Axis: distance to Doug's front door (cave to couch). 9 items, 10-12 min, deaths 330-336.
- Policy gates for every later approval: WHO/CDC-consistent claims only, no COVID-19, no safety or medical instructions, no symptom imagery,
  no named patients, no stigmatising of animals or regions. See brief sec 7.

## 2026-11-10, creative director: script approved (draft 2)
- Screener PASS on draft 2 (facts 0 items, policy 0 items, hook 9, structure 8, voice 8, 2,063 words, about 10.6 min). Read the full
  script against the brief: the axis, bands, 9 items, counter 329 to 336, gags used once each, opening (word 35, twist about 0:36,
  payoff by about 0:09), the two allowed prevention facts said once each, and the brief sec 7 policy gates all hold.
- Accepted the fact-driven deviations from the brief: WHO 44,203 rabies deaths a year (2021 GHE) replaces 59,000, so the line is
  "one every twelve minutes"; Q fever "one to ten bacteria"; rabies survivors "a few dozen at most".
- Two copy fixes applied by the CD before approval (no new claims, so no re-screen needed):
  1. Line 308: "The cat is fine." becomes "The cat has no comment." A cat that passes on pneumonic plague is a sick cat, so the old
     line contradicted the CDC mechanism stated two lines earlier. It also diluted the once-only "Doug is fine." (item 4).
  2. Burger death calendar (stage direction) now flips 1990-1995, not 1990-1993, so Doug's vCJD death doesn't come before the first
     recorded vCJD deaths (1995; the disease was recognised in 1996).
- For the director and art: no symptom imagery anywhere; the dog, cat, macaque and bats look healthy and ordinary (not cute); germs
  stay faceless blobs. Optional screener note O1 (Pasteur's earlier 1885 patients) goes in facts.md only; the script is unchanged.
- Series bible updated: counter 336, death 330 played flat, HOW CLOSE device and the disease-episode visual rules, episode log row.

## 2026-11-10, director: shotlist
- 178 shots, all 2,064 spoken words in order (s001 = thumbnail, "A bat the weight of a phone"); 9 chapters; Doug in 65% of shots.
  Generator: build/gen_shotlist.py (scratch), so layout fixes stay re-runnable.
- HUD: counter (1590,162) + "HOW CLOSE: <stop>" size-28 label at (1590,238) with a small primitive fingerpost icon; the reserved zone
  runs down to y 260. The big fingerpost (primitives, planks 560 to 224 px wide) appears on each item's kicker shot with the new plank
  popping in; COUCH is stamped red at s173, and the HUD stop turns red from there.
- Sober cards (#15181a, white text, no Doug, no HUD) carry every real death toll: Marburg 1967, Python Cave 2007-08, Malaysia, B virus
  2021 plus the CDC 50/21 chart, Netherlands, H5N1 chart, vCJD, Four Corners, hantavirus 38%, the Black Death range, rabies 44,000 and
  1 every 12 min, and the rabies survivors. The hydrophobia line (s160) shows only a blank month calendar.
- Item kickers with no "Doug has died." line carry the death beat instead: s041 (date palm, "The next animal isn't after Doug's
  breakfast,"), s098 ("The cow is not safer."), s133 ("and they were still home."), s151 ("The cat has no comment."). Burger and Dog
  tick the counter mid-shot (s113, s171-s172 calendar flips, then cut to black).
- Logged cap exceptions: `cap_off` on upright Doug while the macaque holds the cap (s055-s059) and while the cap lies on the farm lane
  (s079-s082, one cap per frame); `cap_taken` on the death bodies whose cap sits on a prop (s025, s041, s098, s133, s151).
- Shorts: short01 Burger s105-s114, short02 Goat Dust s071-s082 (+ hook), short03 Cat s141-s151 (+ hook). All end on the payoff, simple
  end card. Titles are left for the youtube-titler.

## 2026-11-10, creative director: art gate (APPROVED, art_approved)
- Art director R2 PASS and visual screener R2 PASS read. Thumbnails reviewed full size against the ranked pairings in metadata.json packaging.
- A "UP TO 88%" + "The Deadliest Diseases Bats, Cats and Dogs Can Give Humans": the strongest of the three. One huge bat, a scared Doug and a torch beam all pull the eye to the number. 88% is the WHO upper Marburg CFR and the video delivers it as item 1. Would click.
- B "ON THE COUCH" + "Rabies and the Most Disturbing Diseases Animals Give Humans": the dog is ordinary and asleep, and Doug's grimace plus the warning triangle keep it adult-coded, not cosy. It matches the boss. Would click.
- C "HOW CLOSE?" + "The Deadliest Diseases a Bat, a Cat or a Dog Can Give You": the growing tiles and arrow make the axis readable at a glance, and the tiles match the title's animals. It is not the 3x3 grid in the brief, but this version reads better at 168 px. Accepted.
- Non-blocking: carry over the screener advisories (s057 bandage position, s170 bubble tail, s145 droplet grey) if those shots are touched again. Script line 10 still reads "88% FATAL", but thumbnail A ("UP TO 88%") is the opening image and is the one that counts.
