# 034 Every Reason the Bison Is Yellowstone's Most Terrifying Animal: decisions

## 2026-11-01, creative director: script gate (draft 2)
Screener round 2 (script_review.md): the written verdict is FAIL on one facts.md sourcing item (F5), with scores hook 8, structure 8, voice 8, 0 policy items and 2,115 words. The review says "Once F5 is in facts.md with no other changes, this script passes." I checked this myself:
- facts.md now has the F5 row under The Jam (Cowboy State Daily, 2025-06-06: "Bison jams are a frequent occurrence on the narrow roads running throughout Yellowstone"; "straddling both lanes"; "the bison stuck to the side of the road"). It covers all three lines (the Record kicker "along the road", the Jam's "often ... at the front", and "along and across").
- script.md was last changed at 17:22, before the round-2 review (17:24). Only facts.md changed after it (17:25). So the condition "no other changes" holds, and word 35 and word 144 are untouched.

1. **Approved.** Draft 2 delivers the brief:
   - the calendar axis January to August, with the bands Winter / Spring / Summer / The rut
   - 9 items, deaths 268-274, survives The Snowplow and The Wallow
   - item 1 The Wolves, one of the three strongest
   - both callbacks (005 Blue Babe: the stew is canon in 005; 012 the stuck bison)
   - the sober card with no names
   - the required honesty line (2000-2015: 25 hurt, 0 died; bears have killed more)
   - no children, no named victims and no safety advice
   The opening passes the retention rules: concrete sentence 1, the referee promise by about 0:10, "The Wolves." at word 35, the twist at word 144, and death 268 by about 1:17. The title stays honest because the script says "injured", never "killed", the most.
2. **The deviations from the brief are accepted.** All of them are fact-driven:
   - MacNulty 2014 is in PLoS ONE, and "stand their ground" is cut
   - Conrad & Balison is cut
   - "most charges involve cows" is cut
   - 55 km/h (NPS) in place of 56
   - the fence wording is cut
   - the bellow distance is cut
   - "several hundred tonnes" is cut
   - the 2023 calf release is reduced to "the herd would not take it back, and the calf died", with no fine and no name
3. **Accepted, with a watch note:** the 23 m park distance appears twice (the tennis-court line in The Speed and the rule in The Record). The brief said to state it once. Both times it is a fact or a measurement, not an instruction, and the screener ruled it non-advice, so it stays. **Titler / Shorts:** never package the distance as a tip ("how far to stay").
4. **Editor:** keep the thumbnail hold at about 1.5 s or less (word 35 and the twist have no slack). Pronunciation: Lamar "luh-MAR", Hayden "HAY-den".
5. **Director notes (not blocking):**
   - a. The Hump: no horn contact anywhere. Doug leaves the top of the frame and only the cap comes back.
   - b. Show the BUTT / HOOK / TOSS icons as symbols only, with no people in them.
   - c. The Calf: keep the calf distant and plain (no eyes detail, no smile), with the cow filling the frame. The riverbank hold carries no joke.
   - d. The Jam's AUGUST 2022 head-butt: the car rocks, and no person is shown inside it in danger.
   - e. The sober card in The Record: white on black, no Doug.
   - f. Wolves never kill anything on screen.
6. **Series bible updated:** the counter goes to 274, with a 034 log row.
APPROVED

## 2026-11-01, director: shotlist
208 shots (s001 thumbnail hold, 1.5 s on "In Yellowstone,"); all 2,115 spoken words in order; Doug in 81% of shots; 9 chapters; counter 267 to 274; calendar HUD (icon + month label under the counter, red RUT from s195). How the CD's notes 5a-f are staged:
- a. The Hump: Doug goes up out of the top of the frame on a dotted arc (s069) with no contact; s070 holds on empty sky while the cap floats down; then black (s071).
- b. BUTT / HOOK / TOSS (s059-s061): `bison_head_icon` plus red arrows in empty boxes, no people.
- c. The Calf: the calf is only ever distant (scale 0.28-0.35) or a black silhouette; the cow fills the frame in s076 and s091; s085-s086 are a plain grey card (no figures, no counter); s087-s088 hold on the empty riverbank with no joke.
- d. AUGUST 2022 (s145-s147): an empty glazed car rocks (rotate -5, shake); no person in or near it; Doug is not in these shots.
- e. Sober card (s124-s127): white text on `#15181a`, numbers only, no Doug, no counter.
- f. Wolves never kill: the wolves stand, back away or run off; "bison have killed wolves" is an `!` over a standing bison while a wolf retreats (s019). Doug's death 268 happens off screen (s024 arrow, then black).
- Deaths are all off screen + black + ghost Doug + cap. No horn ever touches Doug; the referee impact cuts to black at 50% of s200.
- Shorts: Snowplow (s029-s036), Speed (s096-s107), Rut (s178-s186); none use the calf, the sober card or a real incident, and none package the 23 m distance. Titles and descriptions are filled.

## 2026-11-01, creative director: thumbnail gate (A, B, C)
Inputs: `build/thumbnail.png`, `thumbnail_b.png`, `thumbnail_c.png` and their `_small` (168x94) versions; `thumbnail.json`,
`thumbnail_test_b.json`, `thumbnail_test_c.json`; brief section 8. **No visual-screener thumbnail report exists yet**
(visual_review.md round 3 lists "all three thumbnails" as still pending), so no variant can clear the package gate today.
The verdicts below are the creative call; the gate opens only after a visual-screener PASS on the revised set.
Checked on all three: no title/alt word on the image, no BISON/YELLOWSTONE/TERRIFYING, no distance numbers or safety wording,
no horn touches Doug, no calf, no real people, bulls keep hump and beard at 168x94, no gore. All pass those hard rules.

**A (lead, "IT'S BEHIND YOU"): REVISE (small).** The concept is the click: tiny smiling Doug, selfie stick up, a bull filling
the frame behind him. At 168x94 the bison and the text read. But the bull reads as a bow or a stretch, not a charge, and that
undersells the text.
1. Sell the charge: raise both existing `spray` dust puffs (x120 and x330) to density 0.25, and add a third `spray` at the front
   hooves (x 860, y 655, r 70, color #c9a46a, density 0.25). Add 3 short black motion lines (width 6) behind the hump, around
   x 250-330 and y 140-260.
2. The kicked-back hind leg cut by the left edge (about x 0-110, y 320-400) reads as a loose tube. Move the bull to x 470
   (keep scale 1.5) so the leg comes in from the edge as part of the body, or re-angle it. Keep the horn-to-Doug gap at 60 px or more.
3. Keep the text, colours, Doug's pose and expression as they are. Script s001 now says "IT'S BEHIND YOU" (script.md line 20,
   a stage direction only, no spoken words changed).

**B (challenger, "REFEREE"): APPROVE (creative).** This is the strongest of the three. It is the payoff promise as an image,
Doug's shock face plus a whistle reads at feed size, and the symmetry makes the danger instant. Two optional polish notes, not blocking:
- a. Doug's `arms_up` arms read as two crossed sticks behind the shirt. If the referee_shirt sleeves can sit on the raised
  arms, do that. Otherwise leave it.
- b. The dust_plume's inner contour lines are busy. If the asset has a lighter version, use it. Otherwise leave it.

**C (grid control): REVISE.** The grid deviates from the brief (Wolves, Snowplow, Calf, Speed, Record, Rut). Dropping Calf and
Record is correct (calf risk, and the sober record should not be packaged), but item 1 is missing, and two tiles misread at 168x94.
1. Replace HUMP with **WOLVES** (item 1, the hook item the opening pays off first): a line of 4-5 `grey_wolf` facing one standing
   `american_bison` on a pale blue tile. At feed size the pink `bison_hump_cutaway` reads as raw meat or a brain. It is fine in the
   video, but not on the thumbnail.
2. Keep the WALLOW label but change the art. At feed size a bull on its back with all four legs up reads as a dead animal.
   Show the bull on its side with its legs half folded, inside a big dust spray (`dust_cloud` or a dense `spray`), so it
   clearly reads as rolling.
3. Reorder the tiles along the episode year: WOLVES, SNOWPLOW, SPEED (top row); WALLOW, JAM, RUT (bottom row). RUT stays bottom-right as the worst.
4. Put Doug in 2 tiles, not 1, so the channel's hook shows: tiny worried Doug beside the wolves line, plus the JAM Doug as he is.
   Keep him small (scale 0.25 or less in tile) per style bible 2 ("one tile among many").

Next: graphic designer applies A 1-3 and C 1-4 (B as is, a/b optional), re-renders all three plus `_small` versions, then the
visual screener runs the thumbnail check. Back to me only if the screener changes anything beyond these notes.
