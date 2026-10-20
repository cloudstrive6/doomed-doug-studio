"""Monetization progress (YouTube Partner Program with ad revenue) and the owner's goal: monetize as soon as
possible, then reach $1,000/day from AdSense.

    python -m studio ypp            # print + write data/ypp/<date>.json
    python -m studio ypp --notify   # also send the Telegram summary

Ad-revenue tier requirements: 1,000 subscribers AND (4,000 public long-form watch hours in the last 365 days OR
10M valid public Shorts views in the last 90 days). Shorts watch time does not count toward the 4,000 hours.
Analytics data lags 2-3 days, so the figures are slightly behind.
"""
from __future__ import annotations

import datetime as dt
import json

from .config import ROOT

SUBS, HOURS, SHORTS = 1_000, 4_000, 10_000_000
GOAL_PER_DAY = 1_000.0
# planning assumptions (owner's goal is AdSense revenue); replace with the channel's real RPMs once monetized
RPM_LONG, RPM_SHORTS = 6.0, 0.06   # USD per 1,000 views, US-heavy science/education audience (rough mid estimates)


def _eta(have: float, need: float, per_day: float, today: dt.date) -> str:
    if have >= need:
        return "met"
    if per_day <= 0:
        return "no progress yet"
    days = (need - have) / per_day
    return f"~{(today + dt.timedelta(days=days)).isoformat()} at the last 7 days' pace" if days < 3650 else ">10 years at this pace"


def progress() -> dict:
    from .youtube import yt, yta
    api, an = yt(), yta()
    today = dt.date.today()
    end = today.isoformat()

    def q(days: int, lag: int = 0, **kw):
        last = today - dt.timedelta(days=lag)
        start = (last - dt.timedelta(days=days - 1)).isoformat()
        return an.reports().query(ids="channel==MINE", startDate=start, endDate=last.isoformat(),
                                  **kw).execute().get("rows", [])

    subs = int(api.channels().list(part="statistics", mine=True).execute()["items"][0]["statistics"]["subscriberCount"])
    by_type = lambda rows: {r[0]: r[1:] for r in rows}  # noqa: E731
    y = by_type(q(365, metrics="estimatedMinutesWatched,views", dimensions="creatorContentType"))
    s90 = by_type(q(90, metrics="views", dimensions="creatorContentType"))
    w7 = by_type(q(7, lag=3, metrics="estimatedMinutesWatched,views,subscribersGained,subscribersLost",
                   dimensions="creatorContentType"))
    long_hours = (y.get("videoOnDemand", [0, 0])[0]) / 60
    shorts_90 = s90.get("shorts", [0])[0]
    week_long_views = w7.get("videoOnDemand", [0, 0])[1]
    week_short_views = w7.get("shorts", [0, 0])[1]
    week_hours = w7.get("videoOnDemand", [0, 0])[0] / 60
    week_subs = sum(v[2] - v[3] for v in w7.values() if len(v) >= 4)
    est_day = (week_long_views * RPM_LONG + week_short_views * RPM_SHORTS) / 1000 / 7
    out = {
        "date": end,
        "subscribers": {"have": subs, "need": SUBS, "per_day_7d": round(week_subs / 7, 1),
                        "eta": _eta(subs, SUBS, week_subs / 7, today)},
        "long_watch_hours_365d": {"have": round(long_hours, 1), "need": HOURS, "per_day_7d": round(week_hours / 7, 2),
                                  "eta": _eta(long_hours, HOURS, week_hours / 7, today)},
        "shorts_views_90d": {"have": int(shorts_90), "need": SHORTS, "per_day_7d": round(week_short_views / 7),
                             "eta": _eta(shorts_90, SHORTS, week_short_views / 7, today)},
        "views_per_day_7d": {"long": round(week_long_views / 7), "shorts": round(week_short_views / 7)},
        "revenue_if_monetized_usd_per_day": round(est_day, 2),
        "goal_usd_per_day": GOAL_PER_DAY,
        "long_views_per_day_needed_for_goal": round(GOAL_PER_DAY / RPM_LONG * 1000),
        "assumptions": {"rpm_long": RPM_LONG, "rpm_shorts": RPM_SHORTS},
    }
    d = ROOT / "data" / "ypp"
    d.mkdir(parents=True, exist_ok=True)
    (d / f"{end}.json").write_text(json.dumps(out, indent=1), encoding="utf-8")
    return out


def summary(p: dict) -> str:
    s, h, sh = p["subscribers"], p["long_watch_hours_365d"], p["shorts_views_90d"]
    return (f"💰 Monetization progress ({p['date']})\n"
            f"• Subscribers: {s['have']:,}/{s['need']:,} (+{s['per_day_7d']}/day) → {s['eta']}\n"
            f"• Long-video watch hours (12 mo): {h['have']:,}/{h['need']:,} (+{h['per_day_7d']}/day) → {h['eta']}\n"
            f"• or Shorts views (90 d): {sh['have']:,}/{sh['need']:,} (+{sh['per_day_7d']:,}/day) → {sh['eta']}\n"
            f"• Views/day: long {p['views_per_day_7d']['long']:,}, Shorts {p['views_per_day_7d']['shorts']:,}\n"
            f"• If monetized today: ~${p['revenue_if_monetized_usd_per_day']:,}/day (goal ${p['goal_usd_per_day']:,.0f}/day "
            f"≈ {p['long_views_per_day_needed_for_goal']:,} long views/day at ${p['assumptions']['rpm_long']} RPM)")
