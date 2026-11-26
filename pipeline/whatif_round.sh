#!/usr/bin/env bash
# One What If build round in CI:  [fixer, from round 2]  -> prep -> render -> thumbnails -> Shorts -> independent
# review -> gate. Writes passed=true|false and episode=<id> to $GITHUB_OUTPUT. Never uploads (the workflow does).
#   SLUG=<slug> ROUND=<n> bash pipeline/whatif_round.sh
set -uo pipefail
W="whatif/${SLUG:?}"
R="${ROUND:?}"
out() { [ -n "${GITHUB_OUTPUT:-}" ] && echo "$1" >> "$GITHUB_OUTPUT"; echo "$1"; }
t0=$SECONDS
lap() { echo "::notice::round $R $1 done at $(( (SECONDS - t0) / 60 )) min"; }

if [ "$R" -gt 1 ]; then
  bash pipeline/claude_run.sh "claude_fix_$R.jsonl" 300 "$(cat pipeline/prompts/fix_whatif.md)

WDIR=$W
ROUND=$R" || echo "fixer ended with an error; continuing with what it left"
  lap fixer
fi

python -m studio.whatif_ci prep "$W" || echo "preflight has FAIL items (the reviewer and the gate will see them)"
lap prep
python -m studio.whatif_ci render "$W" || echo "QC has problems (the gate will hold)"
lap render
python -m studio.whatif_ci thumbs "$W" || echo "thumbnails failed"
python -m studio.whatif_ci shorts "$W" || echo "some Shorts have problems (they will be held back)"
lap shorts

rm -f "$W/review.json"
bash pipeline/claude_run.sh "claude_review_$R.jsonl" 200 "$(cat pipeline/prompts/review_whatif.md)

WDIR=$W
ROUND=$R" || echo "reviewer ended with an error"
lap review

if python -m studio.whatif_ci gate "$W"; then
  out "passed=true"
  python -m studio.whatif_ci publish "$W"
  out "episode=$(python -c "import json;print(json.load(open('$W/state.json'))['episode'])")"
else
  out "passed=false"
fi
exit 0
