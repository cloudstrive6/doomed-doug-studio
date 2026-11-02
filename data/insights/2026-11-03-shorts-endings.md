# Finding 2026-11-03: cliffhanger Shorts endings failed (reverted)

Shorts published 12–30 Oct, first 3 days after publishing (YouTube Analytics) [F]:
| Ending | n | Median views (3 d) | > 500 views | Avg % viewed |
|---|---|---|---|---|
| Old: payoff + "the full video is linked below" + simple end card | 33 | **998** | 23 / 33 | 58% |
| Cliffhanger: payoff withheld (Doug's fate), "???" silhouette teaser card | 20 | **206** | 5 / 20 | 47% |

Long-video views from Shorts links fell too: 33 (17–23 Oct) → 7 (24–30 Oct) → 5 (27 Oct–1 Nov) [F].
Posting volume is not the cause: Shorts views rose when we moved to 3/day on 15 Oct [F].
[I] The Shorts feed rewards completion and loops; withholding the payoff and ending on a static teaser card makes
viewers swipe before the end, so YouTube stops showing the Short.

Decision: Shorts end on their payoff again (director rules + `shorts validate` reject `tease_from`). 27 cliffhanger
Shorts were still scheduled (eps 026–035, up to 12 Nov) at the time of this finding. Do not retry the cliffhanger
format without a controlled test.
