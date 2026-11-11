"""Capture bounded public-data evidence for planning issue #3 (Python stdlib only).

This inspects metadata, at most 20 request records, a boundary index and small
server-side summaries. It does not build the study dataset or fit any models.
Run from any directory; --output must name a new directory to protect snapshots.
"""

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen


BASE = "https://data.edmonton.ca"
LICENCE_URL = BASE + "/stories/s/Open-Government-Licence-Edmonton/msh8-if28/"
ATTRIBUTION = "Contains information licensed under the Open Government Licence - City of Edmonton."
START = "2023-01-01T00:00:00"
END = "2026-01-01T00:00:00"  # Exclusive: three complete calendar years.
ROAD_DESCRIPTIONS = (
    "POTHOLE:Road Pothole",
    "Road Pothole",
    "Pothole: Arterial Road",
    "Pothole: Residential Road",
    "Pothole: Collector Road",
    "Pothole: Industrial Road",
)
ROAD_FILTER = "service_category = 'Potholes' AND service_description IN (" + ",".join(
    "'" + value.replace("'", "''") + "'" for value in ROAD_DESCRIPTIONS
) + ")"
STUDY_FILTER = (
    f"({ROAD_FILTER}) AND date_created >= '{START}' AND date_created < '{END}'"
)


def resource(dataset, **params):
    return f"{BASE}/resource/{dataset}.json?" + urlencode(params)


def jobs():
    aggregate = (
        "count(*) as rows,count(row_id) as with_row_id,"
        "count(distinct row_id) as distinct_row_ids,"
        "count(neighbourhood_id) as with_neighbourhood_id,"
        "count(neighbourhood) as with_neighbourhood_name,"
        "min(date_created) as earliest,max(date_created) as latest"
    )
    return {
        "requests_metadata": f"{BASE}/api/views/q7ua-agfg.json",
        "boundaries_metadata": f"{BASE}/api/views/65fr-66s6.json",
        "category_extent": resource("q7ua-agfg", **{
            "$select": aggregate, "$where": "service_category = 'Potholes'"}),
        "category_candidates": resource("q7ua-agfg", **{
            "$select": "service_category,service_description,count(*) as rows",
            "$where": "upper(service_category) like '%POTHOLE%' OR upper(service_description) like '%POTHOLE%'",
            "$group": "service_category,service_description", "$order": "rows DESC", "$limit": 100}),
        "study_extent": resource("q7ua-agfg", **{
            "$select": aggregate, "$where": STUDY_FILTER}),
        "study_months": resource("q7ua-agfg", **{
            "$select": "date_trunc_ym(date_created) as month,count(*) as rows,count(neighbourhood_id) as with_neighbourhood_id",
            "$where": STUDY_FILTER, "$group": "month", "$order": "month", "$limit": 100}),
        "study_descriptions_by_year": resource("q7ua-agfg", **{
            "$select": "date_extract_y(date_created) as year,service_description,count(*) as rows",
            "$where": STUDY_FILTER, "$group": "year,service_description",
            "$order": "year,service_description", "$limit": 100}),
        "study_neighbourhoods": resource("q7ua-agfg", **{
            "$select": "neighbourhood_id,neighbourhood,count(*) as rows",
            "$where": STUDY_FILTER, "$group": "neighbourhood_id,neighbourhood",
            "$order": "neighbourhood_id,neighbourhood", "$limit": 1000}),
        "request_sample": resource("q7ua-agfg", **{
            "$select": "row_id,date_created,service_category,service_description,neighbourhood_id,neighbourhood,nbhd_latitude,nbhd_longitude,request_status,status_detail,interaction_channel,referral_type,count",
            "$where": STUDY_FILTER, "$order": "date_created,row_id", "$limit": 20}),
        "duplicate_statuses": resource("q7ua-agfg", **{
            "$select": "status_detail,count(*) as rows", "$where": f"({STUDY_FILTER}) AND upper(status_detail) like '%DUPLICAT%'",
            "$group": "status_detail", "$order": "rows DESC", "$limit": 100}),
        "boundary_index": resource("65fr-66s6", **{
            "$select": "neighbourhood_number,name,effective_start_date,effective_end_date",
            "$order": "neighbourhood_number", "$limit": 1000}),
        "boundary_geometry_sample": resource("65fr-66s6", **{
            "$select": "neighbourhood_number,name,geometry_multipolygon",
            "$where": "neighbourhood_number = 6350", "$limit": 1}),
    }


def fetch(name, url):
    request = Request(url, headers={"User-Agent": "DataBridge-feasibility/0.1"})
    with urlopen(request, timeout=45) as response:
        raw = response.read()
    data = json.loads(raw)
    if name.endswith("_metadata"):
        # Omit changing per-column cached values and platform UI configuration.
        data = {key: data.get(key) for key in (
            "id", "name", "description", "attribution", "license", "licenseId",
            "rowsUpdatedAt", "viewLastModified", "metadata", "columns")}
        data["metadata"] = {key: data["metadata"].get(key) for key in (
            "custom_fields", "rowIdentifier")}
        data["columns"] = [
            {key: column.get(key) for key in (
                "fieldName", "name", "dataTypeName", "description")}
            for column in data["columns"]
            if not column.get("fieldName", "").startswith(":")
        ]
    return name, {
        "retrieved_at_utc": datetime.now(timezone.utc).isoformat(),
        "source_url": url,
        "response_sha256": hashlib.sha256(raw).hexdigest(),
        "metadata_projection": name.endswith("_metadata"),
        "data": data,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=False)
    failures = []
    with ThreadPoolExecutor(max_workers=3) as pool:
        futures = {pool.submit(fetch, name, url): name for name, url in jobs().items()}
        for future in as_completed(futures):
            name = futures[future]
            try:
                _, evidence = future.result()
                # Never silently accept the row limit as a complete grouped/index result.
                if isinstance(evidence["data"], list):
                    caps = {"study_neighbourhoods": 1000, "boundary_index": 1000,
                            "category_candidates": 100, "study_months": 100,
                            "study_descriptions_by_year": 100, "duplicate_statuses": 100}
                    if name in caps and len(evidence["data"]) >= caps[name]:
                        raise ValueError("Result reached cap; paginate before claiming completeness")
                (args.output / f"{name}.json").write_text(
                    json.dumps(evidence, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
                print(f"Saved {name}", flush=True)
            except Exception as error:
                failures.append({"query": name, "error": str(error)})
                print(f"FAILED {name}: {error}", flush=True)
    manifest = {
        "purpose": "Planning evidence only; no hypothesis tests or neighbourhood rankings.",
        "source_attribution": ATTRIBUTION,
        "source_licence_url": LICENCE_URL,
        "study_start_inclusive": START, "study_end_exclusive": END,
        "primary_road_descriptions": ROAD_DESCRIPTIONS,
        "sample_note": "First 20 matching rows ordered by date and ID; not a random sample.",
        "failures": failures,
    }
    (args.output / "manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
