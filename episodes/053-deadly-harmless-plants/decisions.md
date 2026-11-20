# 053 decisions

## 2026-11-20 · Script gate (creative director): draft 3 APPROVED

- **Screener:** draft 3 narrow re-screen PASS (facts 0 errors, hook 9/10, structure 8, voice 8, TTS and policy pass; 2,104 spoken words,
  about 10.8 min; rule 9 met at 148 sentences, average 14.22, longest 32).
- **Against the brief:** 9 items on the contact ladder in the four spoken bands, no header before item 1. "Water Hemlock." lands at words
  28-29; the carrot-family twist at about word 115 (about 35 s). The payoff promise is specific and honest ("the rain is only the start";
  it never says the rain kills). Gags as briefed: "Doug did not agree to this." once (item 1), "Doug is fine." variants fresh at 3, 5, 7, 8
  (one "Eventually." only), narrator quietly disappointed at Nightshade only, cap survives at every death. Counter 391 to 396 (items 1, 2,
  4, 6, 9), all flat. Outro is 19 words, one CTA, fresh. The optional 046 callback was not used; fine.
- **Boss "Doug insisted" fix: accepted.** The "No touch." band promises the tree does not need contact, and Doug still eats the apple. "The
  tree did not need him to eat the apple. Doug insisted." makes the extra step Doug's own deadpan choice, so the band stays honest. The rain
  (flat pink) and the smoke (streaming eyes) already deliver the no-touch harm, the "deaths are rarely documented ... more legend than fact"
  line comes before the death, and "nobody has tried all three in one afternoon" frames the cartoon death as Doug's excess, not a claim about
  the tree. Keep this order: honesty line, Doug's three actions, "Doug insisted.", the all-three line, death.
- **Accepted writer deviations:** "within an hour" from the USDA Forest Service (Schep gives no window in the abstract); mad honey "a day or
  two" (Jansen) and Xenophon's "third or fourth day"; the protected-status twist in place of beach roots; gympie pain "weeks" not "months",
  no "hollow"; belladonna eye drops as "the story goes"; oleander hot-dog test (Suchard and Greb 2020) as the myth twist; Strabo cut.
- **Safety check (my own read):** no doses, no ID keys, no first aid or antidotes, no children or pets, no mad-honey sale or recreational use,
  no gympie self-harm anecdotes, "severe, painful burns" said once, seizures said once and never shown. Nightshade delirium is "none of it
  is fun". Passes.
- **Not blocking (editor):** the screener's Nightshade note. If TTS stumbles on "dark and shiny and, according to ... sweet, and", split at
  "sweet." Otherwise leave it.
- **Would I click and keep watching:** yes. The best beats are the soup-mix cousin, the seed inside the only safe part, the hot-dog myth test,
  the century-old specimen that still stings, and the rain sprinkler under the boss tree.

## 2026-11-20 · Guidance for the titler and designer

- **Lead:** "The Deadliest Plants That Look Completely Harmless". All 9 items are sourced as looking harmless (vegetable look-alike, churchyard
  tree, sweet berries, roadside shrub, honey, milk, grand garden plant, cushion-soft leaf, beach tree).
- **"...That Don't Even Need You to Touch Them":** allowed as a test variant only. The boss delivers it through the rain and the smoke, but
  most items are eaten, so it must not lead.
- **Banned:** "Deadliest Plant on Earth" (unless attributed), "kills on touch", "the rain will kill you", "How to Survive", "Never Touch",
  any safety or foraging phrasing, "?", ALL CAPS, Simple Paint's "Every Poison" skeleton.
- **Thumbnail:** "WRONG TREE" (as the script's first frame). No blisters, rashes or burns; flat cartoon pink at most.

## 2026-11-20 · Package gate (creative director): CHANGES REQUESTED (1 required, 2 small), then visual screener

- **Checked:** `validate packaging` OK and `package check --dry-run` OK (10 ranked, top 3 paired A/B/C, no title/thumb word
  duplication). I looked at all three PNGs at 1280x720 and the 168x94 renders. **There is no visual-screener report on the
  thumbnails yet.** visual_review.md round 1 left s001 and the thumbnail for later. So this gate stays open until the
  screener passes the thumbnails as well; my notes are below.

### Would I click each pairing
- **A: "The Deadliest Plants That Look Completely Harmless" + WRONG TREE (lead): yes.** The image is the title's promise: a
  sunny-rain beach tree that looks harmless, a smiling Doug under it, and two words saying something is off. The red trunk band
  and the red cap both read at 168 px. It works as a curiosity gap without any injury. Weak spot: Doug is small (about 90 px of
  head at full size, a dot in the feed).
- **B: "...That Don't Even Need You to Touch Them" + JUST RAIN (test): yes, and the strongest click.** The shocked pink Doug,
  white sap drops and dark storm sky sell the boss, and the title/text pair makes one sentence. It stays a test variant only
  (my 11-20 guidance: most items are eaten, so it must not lead). The rain and smoke in the boss deliver it honestly.
- **C: "How Doug Would Die From Plants That Look Harmless" + NOT PARSNIP (test): yes for a curious viewer, the weakest of the
  three.** The beige roots in the basket read as parsnips, so NOT PARSNIP lands as a joke, and the purple-blotched stem is
  accurate. At 168 px it is a cheerful campfire scene with little danger. That is acceptable for a test arm, and it is the only
  arm with Doug in the title, so it also gives us a read on the "Doug" variable.

### Decisions
- **s001 (thumbnail A as the opening frame under the hemlock line): KEPT, no change.** Style bible 3.2 / rule 3 says open on the
  thumbnail. The very next line (s002, about 3 s later) says "By the end, Doug sits under a tree in the rain", so the image is
  framed as the payoff promise right away, and "Water Hemlock." still lands at words 28-29. Moving the tree line ahead of the
  hemlock line would bury the approved hook fact. Keep s001 at its natural line length (min 2.0 s) and do not extend the hold.
  If C or B wins the test, the opening still uses A. That is fine, because the boss tree is the payoff in every arm.
- **Thumbnail C without the EDIBLE? tick: ACCEPTED, do not add it.** A 44 px tick box can't be read at feed size and would
  clutter the right third. NOT PARSNIP plus the parsnip-looking roots already carry the "mistaken for food" idea. The EDIBLE?
  device stays an in-video staging gag.

### Change requests (numbered)
1. **REQUIRED, graphic designer (thumbnail_test_b.json):** remove the three white peel flakes on Doug's cheek, which come from
   the `sunburn` gear. At 1280 px they read as blistering or peeling skin on the "touch" variant, and the brief and my 11-20
   guidance allow flat cartoon pink at most. Cover them with a small flat `#ff8a7a` patch (no outline) or, if the art director
   prefers, add a thumbnail-only no-peel option to the gear. Keep the pink head, red arms, shock face and white sap drops as
   they are. In-video sunburn shots (s138, s142-s143, s183-s188) stay as the art director passed them.
2. **Recommended, graphic designer (thumbnail.json, A):** scale Doug from 0.62 to about 0.8 and move him about 40 px left so
   he sits under the canopy edge with the three drips clearly falling from the leaves onto his cap. He should read as a figure,
   not a dot, at 168 px. Do not let him overlap the red band or the WRONG TREE text. Remove the grainy speckle along the top
   edge of the canopy (about x 180-520, y 0-60) if it comes from a spray/glow element. It looks like the "dirt" glow flagged in
   visual_review #13.
3. **Small, youtube-titler (metadata.json):** variant C's `thumb_idea`, candidate 3's `concept` and the C sentence in
   `thumbnail_brief` still say "the field guide's EDIBLE? box ticked YES". Make them match the delivered image (Doug stirring
   soup by a campfire, water hemlock beside him, parsnip-like roots in the basket). Do not change the titles or the order.

### Next
- Designer applies 1 (and 2), re-renders the thumbnails and the small versions → visual screener reviews all three thumbnails,
  plus s001, in round 2 → if PASS, the package is approved with no new CD pass, as long as nothing beyond items 1-3 changes.
  If the screener asks for anything that changes the concept or text, send it back to me.
