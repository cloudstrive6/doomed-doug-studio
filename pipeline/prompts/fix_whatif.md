You are the **fixer** for a Doomed Doug What If episode, running unattended in CI after the independent review held
it back. WDIR (end of this prompt) is the episode folder. Your job: raise the review score above the target and
clear every must-fix, then hand back for a re-render. You do not render; the workflow does.

**Headless mode:** launch any agent in the foreground and wait; end your turn only when step 4 is done.

## Read
`WDIR/review.json` (must_fix, scores, Shorts notes), the newest round in `WDIR/video_review.md`,
`WDIR/build/preflight.json`, `channel/whatif_scores.json` (the target), `channel/whatif_bible.md`, and the engine
notes at the top of `pipeline/prompts/produce_whatif.md` (staging format, `lib:` props, the checks).

## 1. Plan
List each must-fix with the file and change that fixes it: staging in `WDIR/build_staging.py` (shots, poses, moves,
props, `shows`, kinetic words), the script (only when a line must change; keep the title drop and the facts), the
engine (only for a fault that would recur in any episode: then fix it in `studio/` generally and add a check to
`studio/whatif_check.py` so it never reaches a reviewer again), `thumbs.json`, `packaging.json`, `shorts_plan.json`.
Then pick the lowest-scoring criterion and make at least one change aimed at it beyond the must-fixes.

## 2. Apply
Make the changes. Never change how existing sets, props or characters draw for other episodes; add options instead.

## 3. Check
`python -m studio.whatif_ci prep WDIR` must end with 0 preflight FAIL. For changed scenes, run
`python -m studio.whatif stills WDIR` and look at the affected sheets yourself. If thumbnails or packaging changed,
run `python -m studio.whatif_ci thumbs WDIR` and look at `thumbs/sheet.jpg`.

## 4. Record
Write `WDIR/fixes.md` (append a `## Round N` section: each must-fix id, what you changed, file and line). Commit:
`git add -A whatif studio && git commit -m "whatif <slug>: fixes for review round N" || true`.

Rules: no em or en dashes; never touch secrets, workflows, `episodes/` or the pilot folder; never upload.
