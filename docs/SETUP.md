# Doomed Doug: one-time setup

Follows the InforMed social-accounts blueprint (same secret names, same OAuth approach). About 30–45 minutes.
Secrets go into `studio/.env` (git-ignored) and GitHub → Settings → Secrets via `gh secret set NAME`.
Never paste a secret into a chat, issue or commit.

## 1. YouTube channel ✅
`@DoomedDoug` created. In YouTube Studio:
- Customization → upload `channel/avatar.png` (Picture), `channel/banner.png` (Banner), `channel/watermark.png`
  (Video watermark, "Entire video"); paste `channel/description.md` into Description.
- Settings → Channel → Feature eligibility → **verify phone** (needed for custom thumbnails, longer uploads).
- Settings → Channel → Advanced → Audience: **No, it's not made for kids**.
- Settings → Upload defaults: Category *Science & Technology*, language *English*.

## 2. Google Cloud project (YouTube + Text-to-Speech)
1. <https://console.cloud.google.com/projectcreate> → name "Doomed Doug". **Link a billing account**
   (Billing → Link). Text-to-Speech requires it even inside its free monthly allowance. Set a budget alert at
   $5 (Billing → Budgets & alerts) so nothing surprises you. One 17-min episode is roughly 15–20K characters.
2. APIs & Services → Library → enable **YouTube Data API v3**, **YouTube Analytics API**,
   **Cloud Text-to-Speech API**.
3. **OAuth consent screen** (Google Auth Platform): External; app name "Doomed Doug Publisher"; support email;
   privacy/terms URLs (public pages: e.g. publish `docs/PRIVACY.md` and `docs/TERMS.md` as a public GitHub Gist);
   **Publish app → In production** (in *Testing* mode the refresh token dies after 7 days).
4. Credentials → Create credentials → **OAuth client ID** → **Desktop app** → put the ID and secret in
   `studio/.env` as `YOUTUBE_CLIENT_ID=...` and `YOUTUBE_CLIENT_SECRET=...`.
5. Credentials → Create credentials → **API key** → *Restrict key* → API restrictions: **Cloud Text-to-Speech API**
   only → put it in `.env` as `GOOGLE_TTS_API_KEY=...`, then `gh secret set GOOGLE_TTS_API_KEY`.

## 3. Authorize the channel
```bash
cd studio && SAVE_SECRETS=1 python -m studio auth
```
A browser opens (callback on `127.0.0.1:53682`). Sign in with the Google account that owns Doomed Doug → choose
the **Doomed Doug** channel → Advanced → Go to app → allow. Scopes: `youtube.upload`, `youtube.readonly`,
`youtube.force-ssl`, `yt-analytics.readonly`, `yt-analytics-monetary.readonly`. The refresh token is written to
`.env` and all three `YOUTUBE_*` secrets to GitHub; it is never printed.

## 4. Claude Code in the cloud
```bash
claude setup-token
```
Copy the long-lived token it prints straight into `gh secret set CLAUDE_CODE_OAUTH_TOKEN` (paste at the prompt).
This runs the agent team on your Claude subscription inside GitHub Actions.

## 5. Telegram alerts (recommended)
@BotFather → `/newbot` → token → message the bot once → `https://api.telegram.org/bot<TOKEN>/getUpdates` →
`chat.id` → `gh secret set TELEGRAM_BOT_TOKEN` and `gh secret set TELEGRAM_CHAT_ID`.
You get: "episode scheduled" (with thumbnail + Studio link), failures, weekly growth summary.

## 6. Pick the voice
```bash
python -m studio voices
```
Listen to `channel/voice_samples/*.wav` (Charon, Fenrir, Orus, Puck, Iapetus, Algenib) and set `voice.name` in
`config/channel.yaml`.

## 7. First run
GitHub → Actions → **Produce episode** → Run workflow with *skip_upload* ticked → download the artifact
(`final.mp4`, thumbnail) and watch it. When happy, run again without *skip_upload* (or wait for Monday's cron).

## 5b. Actions-minutes watch (private repo quota)
Private repos share **2,000 free Actions minutes per month per account** (public repos are free). `usage.yml` checks
daily and alerts (Telegram + a GitHub issue → email) at 1,500 and at 2,000, the cue to switch this repo to Public:
`gh repo edit cloudstrive6/doomed-doug-studio --visibility public --accept-visibility-change-consequences`.
For an account-wide count (all your private repos, not just this one) create a **fine-grained PAT**: GitHub →
Settings → Developer settings → Fine-grained tokens → Repository access *All repositories* → Permissions
*Actions: Read-only* (Metadata read is automatic) → `gh secret set GH_USAGE_TOKEN`.
Estimated Doomed Doug usage: ~60–120 min per episode + ~10 min per growth review + ~1 min/day watch
≈ 350–600 min/month at one episode a week.

## Secrets checklist
| Secret | From |
|---|---|
| `CLAUDE_CODE_OAUTH_TOKEN` | `claude setup-token` |
| `GOOGLE_TTS_API_KEY` | Cloud API key restricted to Text-to-Speech |
| `YOUTUBE_CLIENT_ID`, `YOUTUBE_CLIENT_SECRET`, `YOUTUBE_REFRESH_TOKEN` | Desktop OAuth client + `python -m studio auth` |
| `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID` | @BotFather / getUpdates |
| `GH_USAGE_TOKEN` (optional, recommended) | fine-grained PAT, all repos, Actions read-only |

## How it runs
- **Monday 06:00 UTC** `produce.yml`: agents write → screen → draw → package; final render + QC; final screening;
  upload **private with publishAt** = next Friday 12:00 New York (≥ 3 days out). Telegram pings you with the
  Studio link: review it any time before Friday; to stop it, set it back to Private/unscheduled in Studio.
- **Sunday 14:00 UTC** `growth.yml`: analytics + competitor pull → growth memo → re-ranked idea backlog.
- To publish twice a week later: add a day to `schedule.publish_days` and a second cron line in `produce.yml`.

## Troubleshooting
| Symptom | Fix |
|---|---|
| Telegram says "YouTube did not keep the publishAt schedule" | The Cloud project is unaudited, so API uploads are locked private. Schedule the video by hand in Studio and submit the YouTube API audit form (Google Cloud → YouTube Data API → "Audit and quota extension"). |
| `access_denied` on auth | OAuth app still in *Testing*: publish it to *In production* |
| thumbnail not set | Phone-verify the channel |
| Stage A fails "no packaged episode" | Read the `claude_stage_a.jsonl` artifact; the next run resumes the same episode |
