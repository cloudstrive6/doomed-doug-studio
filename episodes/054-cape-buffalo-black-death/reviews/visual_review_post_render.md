# Visual review: post-render (2026-11-21)

Scope: `build/final.mp4` (687.5 s) through the 23 samples in `build/samples/` and `build/qc.json`, plus extra frames I pulled at about 478-495 s, 520-576 s and 680-686 s. I also checked all three thumbnails and their `_small` versions, the title in `metadata.json`, and the 3 Shorts: each `*_preview.png`, 7 to 8 frames per mp4 including the last second, and a 0.5 s subtitle sweep of short01 from 30 to 45 s. Nothing was re-rendered.

VERDICT (main): PASS
VERDICT (shorts): PASS

## Main video: PASS

- `qc.json` reports `problems: []`. No sample is black, blank, glitched or frozen.
- The chapter labels run in order: DAGGA BOY, BOSS, HITCHHIKERS, THICKET, VOTE, CARRIER, BODYGUARDS, LION KILLER, MEGAHERD, then the end screen. DOUG DEATHS counts up from 396 to 401, and BUFFALO VS DOUG goes from 1 to DOZENS, HUNDREDS and 1,000+, all in the right order.
- In every frame I checked, Doug is on-model (red cap, white head) and readable. That includes the inside of the jeep, the tree branch, the INTERN badge and the night/orange bands.
- Text is legible, spelled correctly, and never cropped or overlapping a drawing.
- f_017 (an empty GROUP SIZE chart) is caught mid-build. At about 528 s the bars 1/2/3 and the lion head are drawn in. This is fine.
- The 2004 Kruger sequence at about 478-495 s is cartoon-only: the calf is fine, the lion runs off, the BATTLE AT KRUGER player and the tourists all read.
- There is no gore and nothing reads as a kids' show.
- f_023 and 680-686 s are the end screen. The dark panel and circle are the expected end-screen slots, and the SUBSCRIBE label and red arrow both read.
- Minor, not blocking: on f_004 the "1 M+" label has an odd space. "1 M+" still reads as the horn span.

## Thumbnails: PASS

Title: "Why the 800 kg Cape Buffalo That Kills Lions Only Eats Grass". All three thumbnails were checked at 1280x720 and at 168x94.

- **A, `BLACK DEATH`**: the bull's face and boss are the one focal point, and the text reads at 168 px. Doug in the reeds with his camera reads as a red-cap secondary. The thumbnail is not misleading.
- **B, `HE'S RETIRED`**: the text is the strongest of the three at feed size. The lying bull plus Doug with his camera at the wallow edge both read, and it pairs with "How an 800 kg Cape Buffalo Kills Without Ever Eating Meat".
- **C, `1,000+`**: the number and the herd wall read as one mass. Doug and the fleeing lion are small at 168 px but present. It matches the herd title.

None of the three shows gore or has a kids' tone.

## Shorts: PASS

These checks passed on all three Shorts:
- Titles are legible and fully on-screen.
- Subtitles are bold and legible, and in the mp4s they show whole words.
- The 16:9 drawings sit full-width with nothing cut off at the sides.
- Doug is on-model.
- The end card reads "FULL VIDEO: TAP BELOW", and its red arrow points straight down.
- There is no "???" card and no withheld payoff.

| Short | Title | Payoff in clip | Result |
|---|---|---|---|
| short01 (58.9 s) | The Birds on a Buffalo's Back Sometimes Drink Its Blood | yes: s055 "known to drink blood" plus the cleaner gag in s063 (a cherry juice box, no blood shown) | PASS |
| short02 (52.6 s) | Buffalo Herds Vote on Where to Go. Doug Voted Wrong | yes: the vote (s097-s103), then Doug votes the other way and is flattened (s107-s112, cartoon) | PASS |
| short03 (47.5 s) | Lions Caught a Buffalo Calf. Then the Herd Came Back | yes: the herd drives off the lions and the calf walks free (s149-s150), and the lions go home hungry | PASS |

Minor, not blocking:
1. The `short01_preview.png` still catches a subtitle mid-word ("away fro"). The mp4 itself shows "the birds away from" in full (checked from 30 to 31 s). This only affects the preview capture.
2. short03's hook frame (s146/s148) shows the lioness and the calf as solid black silhouettes. That was a deliberate choice, and the lion shape reads. The calf reads only as a "small animal", but the narration names it, so no change is required.
3. The HUD (DOUG DEATHS and BUFFALO VS DOUG) is small inside the vertical frame. It is decoration, not information the viewer needs.

No fixes required.
