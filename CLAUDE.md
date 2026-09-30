# Doomed Doug studio

Automated faceless YouTube channel **Doomed Doug** (@DoomedDoug): MS Paint stick-figure videos in the
disturbing science & nature lane. Every video the narrator sends Doug (stick man, red cap) somewhere nature
really doesn't want him. Format replicated from The Paint Explainer (structure/hooks/titles, not content).

## Map
| Path | What |
|---|---|
| `config/channel.yaml` | channel, voice (Chirp 3 HD), video, style, schedule, playlists, competitors |
| `style/paint_explainer_style_bible.md` | the replicated format: titles, hooks, script structure, visuals, thumbnails, rules per agent |
| `channel/series_bible.md` | Doug, narrator, running gags, death counter, episode log |
| `channel/art_bible.md` | palette, zone colours, line weights, layouts |
| `docs/SCENE_SCHEMA.md` | shotlist/scene/asset JSON format for the MS Paint engine |
| `.claude/agents/` | the team: creative-director, growth-analyst, script-writer, script-screener, youtube-titler, director, illustrator, art-director, graphic-designer, editor, visual-screener |
| `pipeline/prompts/` | showrunner prompts run by CI (`produce_episode`, `review_final`, `weekly_growth`) |
| `studio/` | Python engine: `paint.py` (renderer), `doug.py` (rig), `scene.py`, `assemble.py`, `tts.py`, `youtube.py`, `validate.py`, `notify.py` |
| `assets/library/` | reusable drawings (JSON) · `assets/fonts/` bundled open fonts |
| `episodes/<NNN-slug>/` | brief, script, facts, reviews, shotlist, metadata, thumbnail, status; `build/` is scratch (git-ignored) |
| `data/` | `ideas.md` backlog, `analytics/`, `competitors/`, `insights/` memos |

## Commands (`python -m studio <cmd>`, from this folder)
`status` · `new <slug>` · `stage <ep> <stage>` · `validate <ep> [shotlist|metadata]` · `keyframes <ep> [--shots s001,s002]`
· `asset-preview <name...>` · `thumbnail <ep>` · `art <scene.json> <out.png>` · `narrate <ep>` ·
`render <ep> [--limit N] [--final]` · `qc <ep>` · `upload <ep> [--dry-run]` · `analytics` · `notify "<text>" [--photo p]`
· `voices` · `auth` · `branding` · `queue` · `actions-usage` · `shorts validate|render|upload <ep>` · `shorts pending` · `shorts mark-related <shortYouTubeId>` · `auth-meta` · `social release <ep>` · `social publish-due [--dry-run]`

Stages: idea → scripted → script_approved → shotlisted → art_approved → packaged → built → qc_passed → uploaded.

## Rules for every agent
- Stay in the lane (nature horror). Real, sourced science; cartoon deaths only; never gore; adult-coded humour,
  never kids-show tone (the channel is **not made for kids**).
- Original scripts and drawings. Replicate the *format* in the style bible; never copy a competitor's wording,
  drawings or exact titles.
- Doug's design is locked (`studio/doug.py`); only the art director may add poses/gear.
- Never commit or print secrets (`.env`, tokens). Uploads happen only through `python -m studio upload` after QC.
- Uploads are scheduled `publishAt` ≥ 3 days out; the owner reviews in YouTube Studio during that window.
- Cadence: first 28 uploads daily (launch), then weekly on Fridays (`config/channel.yaml` → `schedule`).
