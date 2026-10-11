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
