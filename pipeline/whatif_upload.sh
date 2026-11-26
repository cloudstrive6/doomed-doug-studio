#!/usr/bin/env bash
# Upload a gated What If episode (scheduled, private until its slot), its media for cross-posting and its Shorts.
#   bash pipeline/whatif_upload.sh <episode id>
set -uo pipefail
EP="${1:?episode id}"
python -m studio upload "$EP" || { python -m studio notify "❌ What If upload failed for $EP. Log: ${RUN_URL:-}"; exit 1; }
python -m studio social release "$EP" || python -m studio notify "Could not attach $EP media to a GitHub release (Facebook/Instagram). Log: ${RUN_URL:-}"
python -m studio shorts upload "$EP" || python -m studio notify "Shorts upload failed for $EP (long video is fine). Log: ${RUN_URL:-}"
python - "$EP" <<'EOF'
import json, sys
from pathlib import Path
from studio import notify
from studio.youtube import local
ep = Path("episodes") / sys.argv[1]
m = json.loads((ep / "metadata.json").read_text(encoding="utf-8"))
notify.send(f"🧪 {m['title']}: set the A/B/C thumbnail test in Studio once it is public ({local(m.get('publish_at'))}): "
            f"https://studio.youtube.com/video/{m.get('youtube_id')}/edit (Test & Compare, Thumbnail only, "
            f"files build/thumbnail.png, thumbnail_B.png, thumbnail_C.png in {ep.name}), or ask Claude to do it in Chrome.")
EOF
