#!/usr/bin/env bash
# Engine smoke test: renders a 4-shot episode (silent narration) and runs validation. ~10 s.
set -euo pipefail
cd "$(dirname "$0")/.."
python -m studio render tests/smoketest --limit 4
python -m studio keyframes tests/smoketest
test -s tests/smoketest/build/draft.mp4 && echo "SMOKE OK"
