## 2026-10-09 01:10 UTC — schedule gap Sat 10 Oct / Mon 12 Oct
Cause: 009 was scheduled for Sun 11 Oct 5:00 NZDT, leaving Sat 10 Oct empty; no episode queued for Mon 12 Oct.
Change: moved 009-every-prehistoric-ocean (wbBQSRcTLGU) publishAt 2026-10-10T16:00Z -> 2026-10-09T16:00Z (15 h of review window) via videos.update; metadata.json publish_at updated.
Verification: read back via videos.list, publishAt = 2026-10-09T16:00:00Z.
Remaining: Sun 11 Oct and Mon 12 Oct now open; production (need_episode) must supply the next episodes. Nothing needed from the owner.

## 2026-10-27 04:10 UTC — schedule gap (Wed 28 / Fri 30 Oct)
Cause: daily cadence outran production; only 3 long videos queued with gaps between them.
Changed: moved 025 (b85fECVktMA) to 2026-10-27T16:00Z (Wed 28 5AM NZDT), 026 (PZtxJTh4bUQ) to 2026-10-28T16:00Z, 027 (KCh-dKve4iM) to 2026-10-29T16:00Z, via videos.update and metadata.json. All read back correctly (about 12h+ review window for 025).
Verification: health now only flags Sat 31 Oct, which production (auto) must fill. Needs owner: none.

## 2026-11-08 UTC — production stuck (039-chimp-family-tree at idea, 50 h)
Cause: every produce.yml run since 2026-11-06 fails within ~1 min. Claude stages report "Credit balance is too low" (ANTHROPIC_API_KEY_BACKUP) and the subscription token reports "You've hit your weekly limit · resets 7pm (UTC)". Not a code bug; no agent can run.
Changed: nothing (re-dispatching now would only fail again; no quality gates touched). Episodes up to 038 are uploaded, the queue runs through Tue 10 Nov.
Verification: run 42502798789 log shows both is_error results.
Needs owner: top up Anthropic API credit (console billing) so the backup key works; subscription limit resets 19:00 UTC today, after which the next scheduled produce run should resume 039. If it doesn't, run `gh workflow run produce.yml`.
