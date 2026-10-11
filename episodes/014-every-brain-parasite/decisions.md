# 014 decisions

## 2026-10-10: script gate (draft 3): APPROVED

Screener round 3 PASS (`script_review.md`: facts 0 errors, opening 8/10, structure 8/10, voice 8/10, TTS/policy/length pass).
Read in full against `brief.md`:
1. Opening: "Killifish Fluke." at spoken word 29, twist ("The fish isn't sick. It's dancing. ... the audience is a heron.") at about 0:41. Meets 3.2.
2. Axis and items: 9 items in brief order, three spoken bands (Steers you / Lives in you / Eats you), costume drop on screen at the band shift. Counter 114 to 121, 7 deaths; survivals Rat Lungworm ("Doug is fine. Mostly.") and Spirometra (counter ticks to 119 and back, "with a sigh"). Every item really reaches the brain/CNS, so the title is honest.
3. Gags and callbacks: "Doug did not agree to this.", "hi friend?" x3 (slug, sheepdog, horse), cap survives (pond, grass blade, flowerpot). Exactly two callbacks to 002 (zombie ant fungus, Naegleria with no water-source detail).
4. Risk lines held: no prevention/treatment advice, no drug names, no tissue/surgery description, real patients anonymous (no names, ages, children), no culture or hygiene jokes (the pork joke is only Doug's useless salad), pork myth corrected, Halicephalobus presented as rare. Real-case fact lines carry no jokes; the "7 HUMAN CASES" card is a joke-free hold.
5. Length: 2,932 spoken words (about 15:02).

Tidy-ups made by me (no re-screen needed, no facts touched):
- Header comment line 2: "Draft 2" changed to "Draft 3".
- Line 283 (Gnathostoma kicker) duplicated line 279. Kept line 279 (it is the brief's twist) and replaced the kicker with a Doug-side line: "Doug never left home. The worm did all the sightseeing." Word count 2,937 to 2,932; footer updated.

Notes for downstream (non-blocking):
- Director/graphic designer: 013's thumbnail and boss used VEGETARIAN + lettuce. Here the VEGETARIAN sign (Pork Tapeworm) and the garden lettuce (Rat Lungworm) are brief-mandated beats, but keep them out of the thumbnail and draw the sign differently from 013's text treatment so it does not read as a rerun.
- Lancet Liver Fluke runs 366 words (target 300-330). Editor: keep its holds tight; trim the "Researchers think..." line visually, not in narration.
- Titler: add "Entertainment and education only. Nothing here is medical advice." to the description; don't use "...Every Brain Parasite Feels Like".

SCRIPT: APPROVED

## 2026-10-11: thumbnail pick: A (3x3 grid) WINS, B (hero "IT WALKS") kept as thumbnail_b.json

I rendered both at 1280x720 and at 320x180 feed size (B rendered to a temp path with `python -m studio art`).
Reasons for picking A:
1. **Grammar and brief:** A is archetype A (style bible 2.A): 9 tiles in item order, rounded black frames, bold comic labels that match the chapter names, and a ramp from pale pond green to the near-black boss tile. It uses no title words, no anatomy, no scans or photos, and no VEGETARIAN sign or lettuce. This is exactly the brief's `thumbnail_brief`.
2. **Avoids 013's look:** 013 was an archetype C hero (big subject on a flat field, tiny Doug bottom-right). B uses the same composition (giant head on flat maroon, tiny Doug bottom-right), so we would ship two hero layouts in a row. A breaks the run.
3. **Honest packaging:** the title promises *every* brain parasite. A shows all 9 as a table of contents. B sells only Gnathostoma (item 7), so "IT WALKS" over-indexes one item.
4. **Opening image:** the thumbnail is the opening image, and A leads straight into "Killifish Fluke." (tile 1, top left). B would open on item 7.
5. **Feed size:** A's labels are still readable at 320x180 and the dark boss tile with the red cap catches the eye. B reads more boldly in the feed, which is its only real advantage, but it doesn't make up for points 2-4.

Non-blocking notes on A: in the Lancet Liver Fluke tile the dark ant costume is a bit murky against the gold, and the five head-diagram tiles in rows 2-3 look alike. Each one is told apart by its host prop (slug, ham, frog, fish), which is acceptable. If 014 under-performs on CTR after 7 days, test B as the swap thumbnail.

THUMBNAIL: A APPROVED
- 2026-10-11: packaged. Rounds: script 3, assets 1, keyframes 2 (AD pass r1, VS pass r2), thumbnail A picked. Risk: runtime 14:31 slightly under 15-17 target; speech 206 wpm (1 over).

## 2026-10-11: final package gate: APPROVED

What I reviewed: `metadata.json` (title, alt_titles, description, tags, playlist), `build/thumbnail.png`, `build/chapters.txt`, `build/samples/f_001-f_003`, the opening of `script.md` and `build/captions.srt` (0:00-1:30), and `reviews/visual_review_postrender.md`.
1. **Title kept:** "What Dying From Every Brain Parasite Would Feel Like" (T1). It is the proven body-horror formula and it is honest: all 9 items reach the brain/CNS, and Doug dies in 7 of them. It isn't back-to-back with 012's T1 (013 was T6 in between), and it doesn't use the "...Every Brain Parasite Feels Like" wording. None of the alts is stronger. "How Every Brain Parasite Would Kill Doug" repeats 010's formula and is wrong, because Doug survives 2 items. "Creepiest"/"Most Disturbing" are softer and have no death promise. "Deeper They Go" would over-promise, because the axis is severity, not depth. No swap.
2. **Thumbnail:** archetype A 3x3 grid that ramps from pond green to near-black, with labels that match the chapters. It has no title words, no anatomy and no gore, and the red caps carry it at feed size. The boss tile (cap on the flowerpot) is the best curiosity hook on the channel so far. Same as the earlier pick.
3. **Opening:** the thumbnail grid is the first frame. "Killifish Fluke." is spoken at 0:08.5 (about word 25), and the twist "The fish isn't sick. It's dancing." comes at 0:40. Both meet style bible 3.2. There is a cold-open thesis line plus "Doug did not agree to this." within 7 s. Doug is in costume and the counter (114) is visible by the third sample.
4. **Description/chapters:** the first line is accurate ("about nine in ten" matches facts), it has the medical disclaimer and the AI-use note, there are 6 sources, and there is no advice. The chapters start at 0:00, there are 9 of them, they are in item order, and they match the thumbnail labels. Tags are relevant with no stuffing. Playlist `parasites` is valid.
5. **Condition (not a package issue):** the post-render visual screener FAIL (counter cropped in s014/s024, which carries into short01) has a fix queued (camera x 960). Upload only after the re-render, `qc` passes, and the visual screener PASSES both the new final and short01. Optional polish from that review (s250 arrow, short03 label nudges) is the director's call.

PACKAGE: APPROVED (conditional on re-render + visual screener PASS)

## 2026-10-11: final review round 1
- QC exit 0 (duration 14:31, no problems). Visual screener: VERDICT (main) FAIL, VERDICT (shorts) FAIL: s014/s024 zoom-ins cropped the death counter ("11" instead of "114"). Showrunner set camera.x to 960 on both (shotlist validates). `.rerender` requests final + shorts. Stage left at `packaged`; not qc_passed until round 2 passes. Optional s250 arrow / short03 label polish not applied.
- Creative director approved the package (title, thumbnail, description, opening), conditional on the re-render passing.

FINAL: APPROVED
