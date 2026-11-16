#!/usr/bin/env python3
"""Prepare P2-001 weekly counts. Python 3.9+; no third-party packages."""

import argparse
import csv
import hashlib
import json
from collections import Counter
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen


API = "https://data.edmonton.ca/resource/q7ua-agfg.json"
SOURCE = "https://data.edmonton.ca/d/q7ua-agfg"
LICENCE = "https://data.edmonton.ca/stories/s/msh8-if28"
START, END = date(2023, 1, 1), date(2026, 1, 1)  # END is exclusive.
DATE_FILTER = "date_created >= '2023-01-01T00:00:00' AND date_created < '2026-01-01T00:00:00'"
INCLUDE = {
    "POTHOLE:Road Pothole", "Road Pothole", "POTHOLE:Alley Pothole",
    "Pothole: Arterial Road", "Pothole: Collector Road",
    "Pothole: Residential Road", "Pothole: Industrial Road",
}
EXCLUDE = {"Info Pothole Repair Timeline", "Info Asphalt  and  Potholes",
           "ETS Pothole", "VLSE-ETS Pothole", "Gravel Road", "Washboard"}


def fetch(params):
    url = API + "?" + urlencode(params)
    request = Request(url, headers={"User-Agent": "DataBridge-research/1.0"})
    with urlopen(request, timeout=90) as response:
        return json.load(response)


def download(raw_dir):
    """Cache only relevant fields, plus coverage evidence, for an offline rerun."""
    where = "service_category = 'Potholes' AND " + DATE_FILTER
    count_before = int(fetch({"$select": "count(*) as n", "$where": where})[0]["n"])
    rows = []
    offset = 0
    while True:
        page = fetch({"$select": "row_id,date_created,service_category,service_description",
                      "$where": where, "$order": "date_created,row_id",
                      "$limit": 5000, "$offset": offset})
        rows.extend(page)
        if len(page) < 5000:
            break
        offset += 5000
    count_after = int(fetch({"$select": "count(*) as n", "$where": where})[0]["n"])
    if count_before != count_after or len(rows) != count_after:
        raise ValueError("Source changed during download; rerun with --refresh.")
    coverage = fetch({"$select": "date_trunc_ymd(date_created) as day,count(*) as n",
                      "$where": DATE_FILTER, "$group": "day", "$order": "day",
                      "$limit": 5000})
    undated = int(fetch({"$select": "count(*) as n",
                         "$where": "service_category = 'Potholes' AND date_created IS NULL"})[0]["n"])
    snapshot = {"downloaded_at_utc": datetime.now(timezone.utc).isoformat(),
                "source": SOURCE, "api": API, "date_filter": DATE_FILTER,
                "rows": rows, "daily_all_service_coverage": coverage,
                "undated_pothole_rows_in_entire_feed": undated}
    raw_dir.mkdir(parents=True, exist_ok=True)
    # Only replace the previous cache once all requests succeeded.
    path = raw_dir / "snapshot.json"
    temp = raw_dir / "snapshot.tmp"
    temp.write_text(json.dumps(snapshot, ensure_ascii=False), encoding="utf-8")
    temp.replace(path)
    return snapshot


def monday(day):
    return day - timedelta(days=day.weekday())


def prepare(rows, coverage):
    """Apply the accepted filter and count distinct IDs, including genuine zeros."""
    # All-service activity supports coverage; it cannot prove every request was captured.
    covered = {date.fromisoformat(r["day"][:10]) for r in coverage if int(r["n"]) > 0}
    expected = {START + timedelta(days=i) for i in range((END - START).days)}
    missing = sorted(expected - covered)
    if missing:
        raise ValueError("Missing all-service coverage dates; investigate before counting: "
                         + ", ".join(str(d) for d in missing[:10]))
    counts, excluded = Counter(), Counter()
    seen, duplicate_rows = {}, 0
    for row in rows:
        if row.get("service_category") != "Potholes":
            raise ValueError("Unexpected service category in source export.")
        description = row.get("service_description")
        if description not in INCLUDE | EXCLUDE:
            raise ValueError(f"Unreviewed pothole label: {description!r}. Review before changing the filter.")
        identifier = row.get("row_id")
        timestamp = row.get("date_created")
        if not identifier or not timestamp:
            raise ValueError("Missing request ID or creation date; investigate the source row.")
        created = datetime.fromisoformat(timestamp)
        if created.tzinfo is not None:
            raise ValueError("Expected the source's timezone-free calendar dates; review changed schema.")
        day = created.date()
        if not START <= day < END:
            raise ValueError("Request date outside 2023–2025.")
        identity = (timestamp, description)
        if identifier in seen:
            if seen[identifier] != identity:
                raise ValueError(f"Conflicting records for request ID {identifier}.")
            duplicate_rows += 1
            continue
        seen[identifier] = identity
        if description in INCLUDE:
            counts[monday(day)] += 1
        else:
            excluded[description] += 1
    first = START + timedelta(days=(-START.weekday()) % 7)
    weeks = []
    week = first
    while week + timedelta(days=6) < END:
        weeks.append({"week_start": week.isoformat(), "report_count": counts[week]})
        week += timedelta(days=7)
    full_week_dates = {date.fromisoformat(r["week_start"]) for r in weeks}
    audit = {"downloaded_rows": len(rows), "duplicate_rows_removed": duplicate_rows,
             "unique_pothole_category_requests": len(seen),
             "included_requests_before_boundary_exclusion": sum(counts.values()),
             "excluded_labels": dict(sorted(excluded.items())),
             "partial_boundary_week_reports": sum(n for w, n in counts.items() if w not in full_week_dates),
             "full_week_count": len(weeks), "full_week_reports": sum(w["report_count"] for w in weeks),
             "zero_report_weeks": sum(w["report_count"] == 0 for w in weeks),
             "covered_calendar_days": len(expected & covered)}
    return weeks, audit


def write_outputs(snapshot, raw_path, output):
    # Undated rows anywhere in the feed cannot be assigned to a study year.
    if snapshot["undated_pothole_rows_in_entire_feed"]:
        raise ValueError("Undated pothole records exist; review their possible effect before proceeding.")
    weeks, audit = prepare(snapshot["rows"], snapshot["daily_all_service_coverage"])
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["week_start", "report_count"])
        writer.writeheader()
        writer.writerows(weeks)
    note = ["# Weekly pothole counts — P2-001", "",
            f"Source: [City of Edmonton 311 requests]({SOURCE}).",
            f"Downloaded (UTC): `{snapshot['downloaded_at_utc']}`.",
            f"Local input SHA-256: `{hashlib.sha256(raw_path.read_bytes()).hexdigest()}`.", "",
            f"Output: `{output.name}` — {len(weeks)} full Monday–Sunday weeks, "
            f"{weeks[0]['week_start']} through {weeks[-1]['week_start']} (week starts).",
            "Columns: `week_start` (ISO Monday date), `report_count` (distinct request IDs).", "",
            "## Filter and checks", "",
            "Require `service_category = 'Potholes'`. Include these exact descriptions:", ""]
    note += [f"- `{label}`" for label in sorted(INCLUDE)]
    note += ["", "Excluded category descriptions (distinct request counts):", ""]
    note += [f"- `{label}`: {n}" for label, n in audit["excluded_labels"].items()]
    note += ["", f"- Downloaded category rows: {audit['downloaded_rows']}.",
             f"- Duplicate identical ID rows removed: {audit['duplicate_rows_removed']}.",
             f"- Eligible requests before boundary exclusions: {audit['included_requests_before_boundary_exclusion']}.",
             f"- Reports dropped in partial boundary weeks: {audit['partial_boundary_week_reports']}.",
             f"- Reports in output: {audit['full_week_reports']}.",
             f"- Zero-report weeks retained: {audit['zero_report_weeks']}.",
             f"- All-service daily coverage: {audit['covered_calendar_days']} of {(END-START).days} dates.",
             "- Undated pothole records in the inspected entire feed: 0.", "",
             "Missing neighbourhoods do not exclude requests; neighbourhood fields are not downloaded.",
             "Use the source's published calendar dates without timezone conversion. Counts represent",
             "distinct reported requests, including repeat complaints, rather than unique physical potholes.",
             "All-service activity supports coverage but does not establish complete capture.", "",
             "Only partial boundary weeks are removed here. Weather exclusions, the initial lag",
             "requirement, and the validation/test boundary exclusion belong to P2-003.",
             "No forecasts, test-set model scores, or feature selection are produced here.", "",
             "## Reproduce", "", "From the repository root, using Python 3.9+ (no extra packages):", "",
             "```sh", "python3 scripts/prepare_potholes.py", "```", "",
             "The first run downloads a cache to `data/raw/potholes/snapshot.json` (ignored by Git).",
             "Later runs reuse that cache. Add `--refresh` to download the live feed again; it may",
             "have changed. Keep the original local snapshot to reproduce this exact CSV.", "",
             f"Contains information licensed under the [Open Government Licence – City of Edmonton]({LICENCE}).",
             "DataBridge's processing is independent and is not endorsed by the City.", ""]
    output.with_name("pothole_counts_notes.md").write_text("\n".join(note), encoding="utf-8")
    return audit


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--refresh", action="store_true", help="Replace the cached download with the current feed.")
    parser.add_argument("--raw-dir", type=Path, default=Path("data/raw/potholes"))
    parser.add_argument("--output", type=Path, default=Path("data/processed/weekly_pothole_counts.csv"))
    args = parser.parse_args()
    raw_path = args.raw_dir / "snapshot.json"
    snapshot = download(args.raw_dir) if args.refresh or not raw_path.exists() else json.loads(raw_path.read_text(encoding="utf-8"))
    audit = write_outputs(snapshot, raw_path, args.output)
    print(json.dumps(audit, indent=2))


if __name__ == "__main__":
    main()
