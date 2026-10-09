# Decisions: 013-closer-to-a-hippo

## 2026-10-09: script gate (draft 3): APPROVED

Screener round 3: PASS (facts PASS, hook 8, structure 8, voice 7, policy 0 items, 2,904 spoken words).

Why I would click and keep watching: item 1 named at word 29, twist ("the hippos got there first") at about 0:39; every item has a
clean one-line twist; the distance meter gives a visible reason to stay; the thesis line ("It's a vegetarian. It killed him anyway.") and
the lettuce payoff ("It was accepted.") land the boss. Kid-appeal and advertiser risks handled as briefed (Escobar once, "cocaine" once,
one factual dung beat, no calves, no safety instructions, no teeth on Doug).

Brief amendment: first-death target changed from about 2:45 to about **3:45** (the 2:45 target was unreachable within the brief's own
word budget for items 1-2). The script's first death lands at about 3:42.

Notes for downstream (non-blocking, no further script rounds):
1. Word margin is 4 words above the 2,900 floor. Director/editor cuts must be offset; add any words in The Night Walk.
2. Optional writer-free tidies the editor may apply only if word-neutral: The Honk "louder replies" -> "stronger replies"; The Shallows
   "Its closest living relatives" -> "Their closest living relatives".
3. Script header comment still says "Draft 2"; cosmetic, ignore.
4. Titler: no "cocaine" in title, thumbnail or tags; include "Entertainment and education only. Do not approach wild animals."
5. Art: red sweat drawn orange-red (never blood red); hippo looks dangerous, not cuddly; no teeth in contact with Doug.
6. Script writer: add Science News (Milius, 2004) as second source for the red sweat pigments in facts.md; drop the stale row 57 line.

## 2026-10-09: thumbnail A/B: A WINS (thumbnail.json unchanged)

A (archetype C hero close-up, "VEGETARIAN") beats B (archetype B distance pyramid).
1. A builds a curiosity gap B lacks: the word "VEGETARIAN" against a gaping, tusked mouth is the episode thesis in one look,
   and it adds to the title ("...Deadlier the Closer Doug Gets") rather than repeating it. B repeats the title's gradient with numbers.
2. Feed size (168x94): A's hippo mouth and the word stay legible. In B the hippo in the top two bands (grazing, waterline) shrinks to grey
   specks; only the bottom mouth tile reads.
3. Archetype C carries the reference channel's biggest outliers; it is what the brief proposed and what the titler's thumbnail_brief specified.
4. Policy: both clean (no blood, no red sweat, no "cocaine", no teeth touching Doug, adult tone). A's hippo looks dangerous, not cuddly.
Keep B on file as a test variant if YouTube Test & Compare is used after launch.
- 2026-10-09: Packaged. Script 3 rounds (fact fixes, first death ~3:42), keyframes 2 rounds (art-director+visual-screener PASS), thumbnail A (VEGETARIAN) PASS. Risks: runtime 14.5 min (under brief 15-17); hipposudoric pronunciation not checked by ear; s250 black frame ~1.7s; thumbnail optional nits (text margin, stray tooth).

## 2026-10-09: final package: APPROVED

Reviewed: title + alt_titles, `build/thumbnail.png` (+ feed-size), description/tags/playlist in `metadata.json`, `build/chapters.txt`,
script opening, samples f_001-f_003 (first ~60 s), and `reviews/visual_review_postrender.md`.

1. **Title: keep "Why Hippos Get Deadlier the Closer Doug Gets".** 44 chars, first T6 gradient for us (no back-to-back formula; 011 T7,
   012 T1). It promises exactly the distance axis the video delivers (11,000 km to 0 m). The strongest alt,
   "How a Hippo Would Kill Doug at Every Distance", is a "How ... Would Kill Doug" formula we already used in 001/003/008/010; not clearly
   stronger, so no swap. Keep the alts on file for a title test if CTR underperforms.
2. **Thumbnail: pass.** "VEGETARIAN" against the open, tusked mouth plus Doug offering a lettuce is the thesis in one look and adds to
   the title instead of repeating it. Reads at 320x180. Hippo is dangerous, not cuddly; no blood, no teeth on Doug. Non-blocking nits
   (10 px text margin, stray horizontal incisor) remain; fix only if the thumbnail is touched again.
3. **Description: pass.** Hook sentence is honest ("counted among the deadliest large animals in Africa", hedged), item run-through matches
   the chapters, sources listed, disclaimer and AI-use disclosure present, no safety advice. Tags clean (no "cocaine").
4. **Chapters: pass.** Start at 0:00, 10 chapters = 10 items, names identical to caption bars (style bible rule 7). "Cocaine Hippos" as a
   chapter name is accepted: it is the item's name, the widely used news term, and it stays out of title/thumbnail/tags as briefed.
   Watch the Studio monetization icon after upload; if it goes yellow, rename the chapter + caption to "Escobar's Hippos".
5. **First 60 s: pass.** Opens on the thumbnail image (0.5 s frame confirmed by the screener), item 1 named within the first ~30 words,
   twist ("the hippos got there first") at ~0:39, then the 4 -> ~200 -> 1,400 chart gives a fast visual escalation. HUD (DOUG DEATHS 107,
   DISTANCE TO HIPPO 11,000 km) legible from frame one.
6. **Known, accepted:** runtime 14.5 min (under the 15-18 target; acceptable, the pacing is tight). "Hipposudoric" pronunciation not yet
   checked by ear; editor should listen once before upload.

**Pending (not a creative blocker):** the post-render visual screener FAILED on cropped counter labels (s194, s221, s248, s249) and the
stray red arrow in s251. The director has fixed the shotlist and a re-render is queued; this approval assumes the re-render passes the
visual re-screen, including the `shorts render` re-run for short03. If the re-screen fails, the package does not ship until it passes.

Series bible updated: Doug death total 114; 013 log row finalised.

FINAL: APPROVED
- 2026-10-09 final review round 1: visual FAIL (main+shorts): counters cropped in s194/s221/s248/s249, stray arrow s251. Director fixed shotlist; .rerender requested (final, shorts). Stage left unchanged pending round 2.
