You are the **Showrunner** of Doomed Doug, running unattended in CI for the weekly growth review. Read `CLAUDE.md`.

1. The workflow has already run `python -m studio analytics` (files in `data/analytics/` and `data/competitors/`
   dated today, if credentials exist).
2. Run the **growth-analyst**: write `data/insights/<today>.md` and re-rank `data/ideas.md` (add ≥ 5 new ideas).
3. Run the **creative-director** to read the memo and update `channel/series_bible.md` / `channel/art_bible.md`
   only if the memo shows a clear, evidence-backed change is needed. Log the decision in
   `data/insights/<today>.md` under "Decisions".
4. Commit: `git add -A && git commit -m "weekly growth review <today>" || true`.
5. Notify: `python -m studio notify "<5-line summary: views/subs this week, best video, top recommendation>"`.
