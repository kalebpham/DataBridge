"""Capture additional bounded evidence for issue #3; no study rankings or models."""

import argparse
import calendar
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from decimal import Decimal
import json
from pathlib import Path

from inspect_data_sources import (
    ATTRIBUTION, BASE, END, LICENCE_URL, START, STUDY_FILTER, fetch, resource,
)


def canonical_id(value):
    """Normalize number-serialized identifiers without truncating decimals."""
    number = Decimal(str(value))
    if not number.is_finite() or number != number.to_integral_value():
        raise ValueError(f"Not a whole-number neighbourhood ID: {value!r}")
    return str(int(number))


def geometry_summary(geometry):
    def points(value):
        if isinstance(value, list):
            if len(value) >= 2 and all(isinstance(v, (int, float)) for v in value[:2]):
                yield value[:2]
            else:
                for child in value:
                    yield from points(child)
    coordinates = list(points(geometry["coordinates"]))
    return {
        "type": geometry["type"], "point_count": len(coordinates),
        "bbox": [min(p[0] for p in coordinates), min(p[1] for p in coordinates),
                 max(p[0] for p in coordinates), max(p[1] for p in coordinates)],
    }


def summarize(output):
    """Derive source-quality diagnostics from saved responses, not live reads."""
    def load(name):
        return json.loads((output / f"{name}.json").read_text(encoding="utf-8"))["data"]

    channels = defaultdict(Counter)
    for row in load("road_month_channels"):
        channels[row["month"][:4]][row.get("interaction_channel", "<missing>")] += int(row["rows"])
    duplicates = Counter()
    for row in load("road_month_duplicate_status"):
        duplicates[row["month"][:4]] += int(row["rows"])
    all_service = defaultdict(Counter)
    incomplete_days = []
    for row in load("all_service_days_by_month"):
        year, month = map(int, row["month"][:7].split("-"))
        days = int(row["days_with_records"])
        all_service[str(year)]["rows"] += int(row["rows"])
        all_service[str(year)]["days_with_records"] += days
        if days != calendar.monthrange(year, month)[1]:
            incomplete_days.append(row)
    annual = []
    for year in sorted(channels):
        total = sum(channels[year].values())
        annual.append({
            "year": year, "road_reports": total,
            "duplicate_flagged": duplicates[year],
            "without_duplicate_flag": total - duplicates[year],
            "duplicate_flag_percent": round(100 * duplicates[year] / total, 4),
            "channels": dict(channels[year]),
            "all_service_rows": all_service[year]["rows"],
            "all_service_days_with_records": all_service[year]["days_with_records"],
        })
    historical = {canonical_id(r["neighbourh"]): r for r in load("historical_candidate_polygons")}
    current = {canonical_id(r["neighbourhood_number"]): r for r in load("current_candidate_polygons")}
    comparisons = []
    # Investigative candidates only. These pairs are NOT approved crosswalks.
    for old, new in (("1150", "1151"), ("5462", "5471"), ("5464", "5472"),
                     ("5575", "5570"), ("4485", "4260"), ("2691", "2671")):
        before = historical[old]["the_geom"]
        after = current[new]["geometry_multipolygon"]
        comparisons.append({
            "historical_id": old, "current_candidate_id": new,
            "historical": geometry_summary(before), "current": geometry_summary(after),
            "coordinate_arrays_equal": before == after,
            "interpretation": "Bounding boxes and coordinate equality do not establish geographic equivalence or approve a mapping.",
        })
    result = {
        "purpose": "Derived diagnostics; no neighbourhood rankings, approved crosswalks or causal conclusions.",
        "annual": annual, "months_with_incomplete_all_service_day_presence": incomplete_days,
        "historical_index_rows": len(load("historical_boundary_index")),
        "historical_index_distinct_ids": len({canonical_id(r["neighbourh"]) for r in load("historical_boundary_index")}),
        "candidate_geometry_comparisons": comparisons,
    }
    (output / "summary.json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="utf-8")


def jobs():
    period = f"date_created >= '{START}' AND date_created < '{END}'"
    candidate_ids = "1150,1151,2691,2671,4485,4260,4261,5462,5471,5464,5472,5575,5570"
    return {
        "historical_boundaries_metadata": f"{BASE}/api/views/5bk4-5txu.json",
        "historical_boundary_index": resource("5bk4-5txu", **{
            "$select": "neighbourh,name,date_effec,date_eff_2", "$order": "neighbourh", "$limit": 1000}),
        "historical_candidate_polygons": resource("5bk4-5txu", **{
            "$select": "neighbourh,name,the_geom", "$where": f"neighbourh IN ({candidate_ids})",
            "$order": "neighbourh", "$limit": 100}),
        "current_candidate_polygons": resource("65fr-66s6", **{
            "$select": "neighbourhood_number,name,geometry_multipolygon",
            "$where": f"neighbourhood_number IN ({candidate_ids})",
            "$order": "neighbourhood_number", "$limit": 100}),
        "candidate_request_identifiers": resource("q7ua-agfg", **{
            "$select": "neighbourhood_id,neighbourhood,min(date_created) as earliest,max(date_created) as latest,count(*) as rows",
            "$where": f"({STUDY_FILTER}) AND neighbourhood_id IN ({candidate_ids})",
            "$group": "neighbourhood_id,neighbourhood", "$order": "neighbourhood_id,neighbourhood", "$limit": 100}),
        "road_month_channels": resource("q7ua-agfg", **{
            "$select": "date_trunc_ym(date_created) as month,interaction_channel,count(*) as rows,count(neighbourhood_id) as with_neighbourhood_id",
            "$where": STUDY_FILTER, "$group": "month,interaction_channel", "$order": "month,interaction_channel", "$limit": 1000}),
        "road_month_duplicate_status": resource("q7ua-agfg", **{
            "$select": "date_trunc_ym(date_created) as month,count(*) as rows",
            "$where": f"({STUDY_FILTER}) AND status_detail = 'Duplicate Request Exists'",
            "$group": "month", "$order": "month", "$limit": 100}),
        "category_descriptions_by_year": resource("q7ua-agfg", **{
            "$select": "date_extract_y(date_created) as year,service_description,count(*) as rows",
            "$where": f"({period}) AND service_category = 'Potholes'",
            "$group": "year,service_description", "$order": "year,service_description", "$limit": 100}),
        "all_service_days_by_month": resource("q7ua-agfg", **{
            "$select": "date_trunc_ym(date_created) as month,count(*) as rows,count(distinct date_trunc_ymd(date_created)) as days_with_records",
            "$where": period, "$group": "month", "$order": "month", "$limit": 100}),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=False)
    failures = []
    with ThreadPoolExecutor(max_workers=3) as pool:
        pending = {pool.submit(fetch, name, url): name for name, url in jobs().items()}
        for future in as_completed(pending):
            name = pending[future]
            try:
                _, evidence = future.result()
                if isinstance(evidence["data"], list):
                    cap = 1000 if name in ("historical_boundary_index", "road_month_channels") else 100
                    if len(evidence["data"]) >= cap:
                        raise ValueError("Result reached cap; paginate before claiming completeness")
                (args.output / f"{name}.json").write_text(
                    json.dumps(evidence, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
                print(f"Saved {name}", flush=True)
            except Exception as error:
                failures.append({"query": name, "error": str(error)})
                print(f"FAILED {name}: {error}", flush=True)
    (args.output / "manifest.json").write_text(json.dumps({
        "purpose": "Issue #3 follow-up: source comparability; no research rankings or models.",
        "source_attribution": ATTRIBUTION, "source_licence_url": LICENCE_URL,
        "study_start_inclusive": START, "study_end_exclusive": END,
        "failures": failures,
    }, indent=2) + "\n", encoding="utf-8")
    if failures:
        raise SystemExit(1)
    summarize(args.output)


if __name__ == "__main__":
    main()
