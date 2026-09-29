"""GitHub Actions minutes used this month by private repos (private-repo free quota: 2,000 min/month, shared by
every private repo of the account; public repos are free and not counted).

Counts each job's runtime rounded UP to the whole minute (how GitHub bills), with the OS multiplier
(Linux 1x, Windows 2x, macOS 10x). This is an estimate that tracks GitHub's figure closely; for the exact number
GitHub's billing page (Settings → Billing and plans) is authoritative.

Env: GH_USAGE_TOKEN (classic PAT with `repo` scope, to see every private repo of the account) or GITHUB_TOKEN
(sees only this repo). Usage: python -m studio actions-usage [--alert]
"""
from __future__ import annotations

import datetime as dt
import json
import math
import os
import urllib.request

API = "https://api.github.com"
MULT = {"ubuntu": 1, "linux": 1, "windows": 2, "macos": 10}


def _get(url, token):
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}",
                                               "Accept": "application/vnd.github+json",
                                               "X-GitHub-Api-Version": "2022-11-28"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())


def _mult(labels):
    s = " ".join(labels or []).lower()
    for k, v in MULT.items():
        if k in s:
            return v
    return 1


def private_repos(token, owner):
    if os.environ.get("GH_USAGE_TOKEN"):
        out, page = [], 1
        while True:
            batch = _get(f"{API}/user/repos?visibility=private&affiliation=owner&per_page=100&page={page}", token)
            out += [r["full_name"] for r in batch]
            if len(batch) < 100:
                return out
            page += 1
    return [os.environ.get("GITHUB_REPOSITORY", f"{owner}/doomed-doug-studio")]


def month_usage(token, owner, today=None):
    today = today or dt.datetime.now(dt.timezone.utc)
    start = today.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    per_repo = {}
    for repo in private_repos(token, owner):
        total, page = 0, 1
        while True:
            runs = _get(f"{API}/repos/{repo}/actions/runs?per_page=100&page={page}"
                        f"&created=>={start.date().isoformat()}", token).get("workflow_runs", [])
            for run in runs:
                jobs = _get(f"{API}/repos/{repo}/actions/runs/{run['id']}/jobs?per_page=100", token).get("jobs", [])
                for j in jobs:
                    if not j.get("started_at") or not j.get("completed_at"):
                        continue
                    a = dt.datetime.fromisoformat(j["started_at"].replace("Z", "+00:00"))
                    b = dt.datetime.fromisoformat(j["completed_at"].replace("Z", "+00:00"))
                    secs = (b - a).total_seconds()
                    if secs > 0:
                        total += math.ceil(secs / 60) * _mult(j.get("labels"))
            if len(runs) < 100:
                break
            page += 1
        if total:
            per_repo[repo] = total
    return {"month": start.strftime("%Y-%m"), "total_minutes": sum(per_repo.values()), "per_repo": per_repo,
            "quota": 2000, "scope": "account" if os.environ.get("GH_USAGE_TOKEN") else "this repo only"}


def check(alert: bool = False) -> dict:
    from .config import load_config
    gh_cfg = load_config().get("github", {})
    warn_at, public_at = int(gh_cfg.get("actions_warn_at", 1500)), int(gh_cfg.get("actions_public_at", 1900))
    token = os.environ.get("GH_USAGE_TOKEN") or os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if not token:
        raise SystemExit("set GH_USAGE_TOKEN (or GITHUB_TOKEN)")
    owner = (os.environ.get("GITHUB_REPOSITORY") or "cloudstrive6/").split("/")[0]
    u = month_usage(token, owner)
    used = u["total_minutes"]
    u["level"] = "switch" if used >= public_at else ("warn" if used >= warn_at else "ok")
    if not alert or u["level"] == "ok":
        return u
    from . import notify
    top = ", ".join(f"{r.split('/')[-1]} {m}" for r, m in sorted(u["per_repo"].items(), key=lambda x: -x[1])[:5])
    msg = f"⚠️ GitHub Actions minutes {u['month']}: {used} / {u['quota']} ({u['scope']}). Top repos: {top}\n"
    if u["level"] == "switch":
        msg += _make_public()
    else:
        msg += f"The repo switches to Public automatically at {public_at} minutes."
    notify.send(msg)
    _issue(msg)
    return u


def _make_public() -> str:
    """Flip this repo to Public (needs GH_ADMIN_TOKEN: fine-grained PAT on this repo, Administration: read/write)."""
    repo, token = os.environ.get("GITHUB_REPOSITORY"), os.environ.get("GH_ADMIN_TOKEN")
    if not repo or not token:
        return ("Reached the switch threshold, but GH_ADMIN_TOKEN is not set, so the repo is still private. Run: "
                f"gh repo edit {repo or 'cloudstrive6/doomed-doug-studio'} --visibility public "
                "--accept-visibility-change-consequences")
    info = _get(f"{API}/repos/{repo}", token)
    if not info.get("private"):
        return "Repo is already Public."
    req = urllib.request.Request(f"{API}/repos/{repo}", method="PATCH", data=json.dumps({"visibility": "public"}).encode(),
                                 headers={"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json"})
    try:
        urllib.request.urlopen(req, timeout=30).read()
        return "✅ Switched the repo to PUBLIC: Actions minutes are now free and unlimited."
    except Exception as e:
        return f"❌ Tried to switch the repo to Public but failed: {e}"


def _issue(msg):
    """Also open a GitHub issue (you get an email) in case Telegram isn't set up."""
    repo, token = os.environ.get("GITHUB_REPOSITORY"), os.environ.get("GITHUB_TOKEN")
    if not repo or not token:
        return
    title = "GitHub Actions minutes alert " + dt.date.today().strftime("%Y-%m")
    try:
        existing = _get(f"{API}/repos/{repo}/issues?state=open&per_page=50", token)
        if any(i["title"] == title for i in existing):
            return
        req = urllib.request.Request(f"{API}/repos/{repo}/issues", method="POST",
                                     data=json.dumps({"title": title, "body": msg}).encode(),
                                     headers={"Authorization": f"Bearer {token}",
                                              "Accept": "application/vnd.github+json"})
        urllib.request.urlopen(req, timeout=30).read()
    except Exception as e:
        print(f"[usage] could not open issue: {e}")
