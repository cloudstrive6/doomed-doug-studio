"""Ops monitor: checks every hour that production, uploads, publishes and cross-posts are on track.

    python -m studio health            # report only
    python -m studio health --fix      # also apply the safe mechanical fixes (CI does this)

Each problem is an Issue with an `owner`:
  auto   - fixed mechanically right here (stage drift, re-dispatching production, retrying Shorts uploads)
  agent  - needs diagnosis: the monitor workflow hands these to the ops-monitor Claude agent, which routes the
           fix to the right team agent (pipeline/prompts/monitor.md)
  owner  - only a human can do it (expired logins, Studio-only actions, workflow-file changes)
State (first seen, attempts, last alert) lives in data/monitor/state.json so alerts and fixer runs are not repeated
every hour; the owner hears about a problem once when it needs them, then at most every 12 h, plus when it clears.
"""
from __future__ import annotations

import datetime as dt
import json
import subprocess
from dataclasses import asdict, dataclass, field

from .config import ROOT, load_config

STATE = ROOT / "data" / "monitor" / "state.json"
REPORT = ROOT / "data" / "monitor" / "latest.json"
NOW = lambda: dt.datetime.now(dt.timezone.utc)  # noqa: E731


@dataclass
class Issue:
    key: str                 # stable id, e.g. "produce_failing" or "crosspost:004:short02:tiktok"
    severity: str            # high | medium | low
    owner: str               # auto | agent | owner
    summary: str             # one line for Telegram
    detail: str = ""         # evidence for the fixer agent
    route: str = ""          # which team agent / command should fix it
    fixed: bool = False      # set when --fix resolved it in this run
    extra: dict = field(default_factory=dict)


def _utc(s: str) -> dt.datetime:
    return dt.datetime.fromisoformat(s.replace("Z", "+00:00")).astimezone(dt.timezone.utc)


def _gh(args: list[str]) -> str:
    r = subprocess.run(["gh", *args], capture_output=True, text=True, cwd=ROOT, timeout=120)
    if r.returncode:
        raise RuntimeError(r.stderr.strip()[:300])
    return r.stdout


def _episodes():
    for ep in sorted((ROOT / "episodes").iterdir()):
        mp = ep / "metadata.json"
        if ep.is_dir() and (ep / "status.json").exists():
            meta = json.loads(mp.read_text(encoding="utf-8")) if mp.exists() else {}
            sp = ep / "shorts.json"
            shorts = json.loads(sp.read_text(encoding="utf-8"))["shorts"] if sp.exists() else []
            yield ep, meta, shorts


# ------------------------------------------------------------------ checks


def check_stages(fix: bool) -> list[Issue]:
    """An episode with a YouTube id must be at `uploaded` (a stale run once reset one to `built`, which made every
    later run re-render it instead of making the next episode)."""
    from .__main__ import get_stage, set_stage
    out = []
    for ep, meta, _ in _episodes():
        if meta.get("youtube_id") and get_stage(ep) != "uploaded":
            i = Issue(f"stage_drift:{ep.name}", "high", "auto",
                      f"{ep.name} is on YouTube but its stage was '{get_stage(ep)}'", route="python -m studio stage")
            if fix:
                set_stage(ep, "uploaded", f"monitor: restored ({meta['youtube_id']})")
                i.fixed = True
            out.append(i)
    return out


def _runs(workflow: str, n: int = 12) -> list[dict]:
    return json.loads(_gh(["run", "list", "--workflow", workflow, "--limit", str(n), "--json",
                           "databaseId,status,conclusion,createdAt,updatedAt,event,url"]))


def check_production(fix: bool) -> list[Issue]:
    """Schedule coverage (no empty publish day ahead), queue depth, failing or stuck production runs."""
    from zoneinfo import ZoneInfo

    from .youtube import in_launch_phase, local, queue_status, taken_slots
    out: list[Issue] = []
    cfg = load_config()["schedule"]
    tz = ZoneInfo(cfg["timezone"])
    q = queue_status()
    try:
        runs = _runs("produce.yml")
    except Exception as e:
        return [Issue("github_api", "medium", "agent", f"Can't read GitHub Actions runs: {e}")]
    active = [r for r in runs if r["status"] in ("queued", "in_progress", "waiting", "pending", "requested")]
    done = [r for r in runs if r["status"] == "completed"]

    # 1) every publish day in the next 3 days should have a long video scheduled
    days = {"Mon": 0, "Tue": 1, "Wed": 2, "Thu": 3, "Fri": 4, "Sat": 5, "Sun": 6}
    wanted = {days[d] for d in (cfg["launch"]["publish_days"] if in_launch_phase() else cfg["publish_days"])}
    hh, mm = map(int, cfg["publish_time"].split(":"))
    have = {_utc(t).astimezone(tz).date() for t in taken_slots()}
    today = NOW().astimezone(tz).date()
    gaps = []
    for k in range(0, 4):
        d = today + dt.timedelta(days=k)
        slot = dt.datetime(d.year, d.month, d.day, hh, mm, tzinfo=tz)
        if d.weekday() in wanted and slot > NOW() and d not in have:
            gaps.append(slot)
    if gaps:
        soon = (gaps[0] - NOW()) < dt.timedelta(hours=30)
        later = sorted(t for t in taken_slots() if _utc(t) > gaps[0])
        # the owner prefers no empty days over a long review window: if a later episode exists, the agent may pull
        # it forward into the gap (keeping >= 6 h of review); otherwise production just has to catch up
        out.append(Issue("schedule_gap", "high" if soon else "medium", "agent" if later else "auto",
                         "No long video scheduled for " + ", ".join(local(g.astimezone(dt.timezone.utc)
                                                                          .isoformat()) for g in gaps[:3]),
                         detail=json.dumps({**q, "later_scheduled": later}),
                         route="pull the next scheduled episode forward (YouTube publishAt + metadata.json)"
                               if later else "production run"))

    # 2) consecutive failed production runs
    fails = 0
    for r in done:
        if r["conclusion"] in ("failure", "timed_out", "startup_failure"):
            fails += 1
        elif r["conclusion"] == "success":
            break
    if fails >= 2 and not active:  # a run in progress may already carry the fix; judge it when it finishes
        out.append(Issue("produce_failing", "high", "agent", f"Last {fails} production runs failed",
                         detail="\n".join(f"{r['createdAt']} {r['conclusion']} {r['url']}" for r in done[:fails]),
                         route="diagnose the run logs, route to the agent that owns the failing stage",
                         extra={"run_ids": [r["databaseId"] for r in done[:fails]]}))

    # 3) the same episode in progress for too long
    from .__main__ import get_stage
    for name in q["in_progress"]:
        st = json.loads((ROOT / "episodes" / name / "status.json").read_text(encoding="utf-8"))
        first = _utc(st["history"][0]["at"]) if st.get("history") else NOW()
        if NOW() - first > dt.timedelta(hours=36):
            out.append(Issue(f"episode_stuck:{name}", "high", "agent",
                             f"{name} has been in production for {int((NOW() - first).total_seconds() // 3600)} h "
                             f"(stage {get_stage(ROOT / 'episodes' / name)})",
                             detail=json.dumps(st["history"][-8:]), route="showrunner / the agent owning that stage"))

    # 4) queue below target and nothing running -> start a production run (mechanical)
    if q["need_episode"] and not active:
        last = done[0] if done else None
        idle = not last or NOW() - _utc(last["updatedAt"]) > dt.timedelta(hours=2)
        if idle and q["queued"] < q["target"]:
            i = Issue("queue_low", "medium", "auto", f"Queue {q['queued']}/{q['target']} and no production running",
                      route="dispatch produce.yml")
            if fix and fails < 3:  # don't hammer a pipeline that keeps failing; the agent handles that
                _gh(["workflow", "run", "produce.yml"])
                i.fixed = True
                i.summary += ": started a production run"
            out.append(i)
    return out


def check_youtube(fix: bool) -> list[Issue]:
    """Every scheduled video must exist, be processed, and have the publish time we recorded; uploaded episodes
    must have all their Shorts uploaded."""
    from .youtube import yt
    out = []
    try:
        api = yt()
    except Exception as e:
        return [Issue("youtube_auth", "high", "owner", f"YouTube login failed: {str(e)[:150]}",
                      route="owner: python -m studio auth (re-approve), then update YOUTUBE_REFRESH_TOKEN")]
    want = {}
    for ep, meta, shorts in _episodes():
        for x, label in [(meta, "long")] + [(s, s["id"]) for s in shorts]:
            if x.get("youtube_id") and x.get("publish_at"):
                want[x["youtube_id"]] = (ep.name, label, x["publish_at"])
        if meta.get("youtube_id") and meta.get("publish_at"):
            up_at = _utc(meta.get("uploaded_at") or meta["publish_at"])
            missing = [s["id"] for s in shorts if not s.get("youtube_id")]
            if missing and NOW() - up_at > dt.timedelta(hours=3):
                i = Issue(f"shorts_missing:{ep.name}", "medium", "auto",
                          f"{ep.name}: Shorts {', '.join(missing)} were never uploaded", route="shorts upload")
                if fix:
                    i.fixed, i.summary = _retry_shorts(ep, missing, i.summary)
                if not i.fixed:
                    i.owner = "agent"
                out.append(i)
    ids = list(want)
    seen = {}
    for k in range(0, len(ids), 50):
        for v in api.videos().list(part="status", id=",".join(ids[k:k + 50])).execute().get("items", []):
            seen[v["id"]] = v["status"]
    for vid, (ep, label, publish_at) in want.items():
        st = seen.get(vid)
        if st is None:
            out.append(Issue(f"video_missing:{vid}", "high", "agent",
                             f"{ep} {label}: video {vid} no longer exists on YouTube (deleted or removed)",
                             route="re-upload via studio commands; check for a strike/rejection email"))
            continue
        if st.get("uploadStatus") in ("failed", "rejected", "deleted"):
            out.append(Issue(f"video_failed:{vid}", "high", "agent",
                             f"{ep} {label}: YouTube says {st.get('uploadStatus')} "
                             f"({st.get('failureReason') or st.get('rejectionReason') or ''})", route="re-upload"))
        elif st.get("uploadStatus") == "uploaded" and _utc(publish_at) - NOW() < dt.timedelta(hours=6):
            out.append(Issue(f"video_processing:{vid}", "high", "agent",
                             f"{ep} {label}: still processing and it goes public within 6 h", route="check / re-upload"))
        if st.get("privacyStatus") == "private" and st.get("publishAt") and _utc(st["publishAt"]) != _utc(publish_at):
            out.append(Issue(f"publish_time:{vid}", "medium", "agent",
                             f"{ep} {label}: YouTube publish time {st['publishAt']} differs from ours {publish_at}",
                             route="decide which is right; fix metadata/shorts.json or the video"))
        if _utc(publish_at) < NOW() - dt.timedelta(minutes=30) and st.get("privacyStatus") == "private":
            out.append(Issue(f"not_public:{vid}", "high", "agent",
                             f"{ep} {label}: should be public since {publish_at} but is still private",
                             route="check scheduling; set public via API if it was meant to be"))
    return out


def _retry_shorts(ep, missing: list[str], summary: str) -> tuple[bool, str]:
    """Download the missing Shorts from the episode's draft release and upload them (scheduler picks the slots)."""
    from . import shorts
    d = ep / "build" / "shorts"
    d.mkdir(parents=True, exist_ok=True)
    tag = f"ep-{ep.name[:3]}"
    try:
        for sid in missing:
            if not (d / f"{sid}.mp4").exists():
                _gh(["release", "download", tag, "-p", f"{sid}.mp4", "-D", str(d), "--clobber"])
        done = shorts.upload(ep)
        return bool(done), summary + f": uploaded {len(done)} now"
    except SystemExit as e:   # held by the visual screener
        return False, summary + f" ({e})"
    except Exception as e:
        return False, summary + f" (retry failed: {str(e)[:120]})"


def check_social() -> list[Issue]:
    """Live items must reach Facebook / Instagram / TikTok within ~2 h; auth errors go straight to the owner."""
    cfg = load_config().get("social", {})
    out = []
    auth_words = ("OAuthException", "190", "expired", "Invalid OAuth", "permission", "401", "403", "reconnect")
    for ep, meta, shorts in _episodes():
        items = []
        if meta.get("youtube_id") and meta.get("publish_at") and cfg.get("facebook_long", True):
            items.append((meta, "long", ["facebook_video"], meta.get("social", {})))
        for s in shorts:
            if s.get("youtube_id") and s.get("publish_at"):
                need = [k for k, on in (("instagram", cfg.get("instagram_reels", True)),
                                        ("facebook", cfg.get("facebook_reels", True)),
                                        ("tiktok", cfg.get("tiktok", True))) if on]
                items.append((s, s["id"], need, s.get("social", {})))
        for x, label, need, sm in items:
            age = NOW() - _utc(x["publish_at"])
            if age < dt.timedelta(hours=2) or age > dt.timedelta(days=7):
                continue
            for k in need:
                if sm.get(k):
                    continue
                err = sm.get(f"{k}_error", "")
                owner = "owner" if any(w in err for w in auth_words) else "agent"
                out.append(Issue(f"crosspost:{ep.name}:{label}:{k}", "medium", owner,
                                 f"{ep.name} {label} not on {k} {int(age.total_seconds() // 3600)} h after going live"
                                 + (f": {err[:140]}" if err else ""),
                                 route="owner: renew the token/connection" if owner == "owner"
                                 else "studio/meta.py or studio/tiktok.py; rerun social publish-due"))
    return out


def check_related() -> list[Issue]:
    """Shorts whose long video is public but whose Related-video link isn't set (Studio-only, so the owner/Claude in
    Chrome does it). Reported once a day at most via the state file."""
    from .shorts import pending_related
    ready = [p for p in pending_related() if _utc(p["long_publish_at"]) < NOW()]
    if not ready:
        return []
    return [Issue("related_pending", "low", "owner",
                  f"{len(ready)} Short(s) need their Related video set in Studio (ask Claude to link them in Chrome)",
                  detail="\n".join(f"{p['short_title']} -> {p['related_title']}" for p in ready))]


def check_ticks() -> list[Issue]:
    """cron-job.org triggers tick.yml every 30 min; if it stops, production and cross-posting slow to GitHub's own
    (late, sometimes skipped) schedules."""
    try:
        runs = _runs("tick.yml", 3)
    except Exception:
        return []
    if not runs or NOW() - _utc(runs[0]["createdAt"]) > dt.timedelta(minutes=95):
        last = runs[0]["createdAt"] if runs else "never"
        return [Issue("tick_stale", "high", "owner", f"cron-job.org hasn't triggered the pipeline since {last}",
                      route="owner: check the cron-job.org job (it may be disabled after failures or the token "
                            "expired); the GitHub fallback schedules keep things running meanwhile")]
    return []


# ------------------------------------------------------------------ run + state


def run(fix: bool = False) -> dict:
    issues: list[Issue] = []
    for name, fn in (("stages", lambda: check_stages(fix)), ("production", lambda: check_production(fix)),
                     ("youtube", lambda: check_youtube(fix)), ("social", check_social),
                     ("related", check_related), ("ticks", check_ticks)):
        try:
            issues += fn()
        except Exception as e:
            issues.append(Issue(f"check_crashed:{name}", "medium", "agent",
                                f"Monitor check '{name}' crashed: {str(e)[:200]}", route="studio/health.py"))
    state = json.loads(STATE.read_text(encoding="utf-8")) if STATE.exists() else {"issues": {}}
    now = NOW().isoformat(timespec="seconds")
    current = {i.key for i in issues if not i.fixed}
    resolved = [k for k, v in state["issues"].items() if k not in current and not v.get("resolved")]
    for k in resolved:
        state["issues"][k]["resolved"] = now
    for i in issues:
        s = state["issues"].get(i.key)
        if not s or s.get("resolved"):
            s = state["issues"][i.key] = {"first_seen": now, "agent_attempts": 0}
        s.update(last_seen=now, summary=i.summary, owner=i.owner, severity=i.severity)
        if i.fixed:
            s["resolved"] = now
    # drop resolved entries older than 14 days
    cutoff = (NOW() - dt.timedelta(days=14)).isoformat()
    state["issues"] = {k: v for k, v in state["issues"].items() if not v.get("resolved") or v["resolved"] > cutoff}
    report = {"at": now, "issues": [asdict(i) for i in issues], "resolved_since_last": resolved}
    STATE.parent.mkdir(parents=True, exist_ok=True)
    STATE.write_text(json.dumps(state, indent=1), encoding="utf-8")
    REPORT.write_text(json.dumps(report, indent=1, ensure_ascii=False), encoding="utf-8")
    return report


def needs_agent(report: dict, max_attempts: int = 3, cooldown_h: float = 6) -> list[dict]:
    """Agent-owned issues that haven't been worked on recently and haven't used up their attempts."""
    state = json.loads(STATE.read_text(encoding="utf-8"))
    out = []
    for i in report["issues"]:
        if i["owner"] != "agent" or i["fixed"]:
            continue
        s = state["issues"].get(i["key"], {})
        last = s.get("agent_at")
        if s.get("agent_attempts", 0) >= max_attempts:
            continue
        if last and NOW() - _utc(last) < dt.timedelta(hours=cooldown_h):
            continue
        out.append(i)
    return out


def mark_agent_attempt(keys: list[str]):
    state = json.loads(STATE.read_text(encoding="utf-8"))
    for k in keys:
        s = state["issues"].setdefault(k, {})
        s["agent_attempts"] = s.get("agent_attempts", 0) + 1
        s["agent_at"] = NOW().isoformat(timespec="seconds")
    STATE.write_text(json.dumps(state, indent=1), encoding="utf-8")


def alert(report: dict) -> str | None:
    """Telegram digest: auto-fixes made, new/persisting owner issues (re-sent every 12 h), agent issues that ran out
    of attempts, and problems that cleared. Silent when everything is fine."""
    from . import notify
    state = json.loads(STATE.read_text(encoding="utf-8"))
    lines, now = [], NOW()
    fixed = [i for i in report["issues"] if i["fixed"]]
    if fixed:
        lines.append("🔧 Fixed automatically:\n" + "\n".join(f"• {i['summary']}" for i in fixed))
    need_you = []
    for i in report["issues"]:
        if i["fixed"]:
            continue
        s = state["issues"].get(i["key"], {})
        gave_up = i["owner"] == "agent" and s.get("agent_attempts", 0) >= 3
        if i["owner"] != "owner" and not gave_up:
            continue
        last = s.get("alerted_at")
        if last and now - _utc(last) < dt.timedelta(hours=12 if i["severity"] != "low" else 24):
            continue
        s["alerted_at"] = now.isoformat(timespec="seconds")
        need_you.append(f"• {i['summary']}" + (f"\n  → {i['route']}" if i.get("route") else "")
                        + ("\n  (the fixer agent tried 3 times)" if gave_up else ""))
    if need_you:
        lines.append("🙋 Needs you:\n" + "\n".join(need_you))
    cleared = [state["issues"][k]["summary"] for k in report.get("resolved_since_last", [])
               if k in state["issues"] and state["issues"][k].get("alerted_at")]
    if cleared:
        lines.append("✅ Cleared:\n" + "\n".join(f"• {c}" for c in cleared))
    STATE.write_text(json.dumps(state, indent=1), encoding="utf-8")
    if not lines:
        return None
    text = "🩺 Doomed Doug monitor\n\n" + "\n\n".join(lines)
    notify.send(text)
    return text
