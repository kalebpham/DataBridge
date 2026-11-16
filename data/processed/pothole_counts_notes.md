# Weekly pothole counts — P2-001

Source: [City of Edmonton 311 requests](https://data.edmonton.ca/d/q7ua-agfg).
Downloaded (UTC): `2026-11-16T03:05:51.356342+00:00`.
Local input SHA-256: `a7e8cd665124bd93389fa267dddf0f1f55f888bf26dbf31240e7f34fbbdcc8dc`.

Output: `weekly_pothole_counts.csv` — 156 full Monday–Sunday weeks, 2023-01-02 through 2025-12-22 (week starts).
Columns: `week_start` (ISO Monday date), `report_count` (distinct request IDs).

## Filter and checks

Require `service_category = 'Potholes'`. Include these exact descriptions:

- `POTHOLE:Alley Pothole`
- `POTHOLE:Road Pothole`
- `Pothole: Arterial Road`
- `Pothole: Collector Road`
- `Pothole: Industrial Road`
- `Pothole: Residential Road`
- `Road Pothole`

Excluded category descriptions (distinct request counts):

- `ETS Pothole`: 5
- `Info Asphalt  and  Potholes`: 709
- `Info Pothole Repair Timeline`: 8
- `VLSE-ETS Pothole`: 1

- Downloaded category rows: 26457.
- Duplicate identical ID rows removed: 0.
- Eligible requests before boundary exclusions: 25734.
- Reports dropped in partial boundary weeks: 15.
- Reports in output: 25719.
- Zero-report weeks retained: 0.
- All-service daily coverage: 1096 of 1096 dates.
- Undated pothole records in the inspected entire feed: 0.

Missing neighbourhoods do not exclude requests; neighbourhood fields are not downloaded.
Use the source's published calendar dates without timezone conversion. Counts represent
distinct reported requests, including repeat complaints, rather than unique physical potholes.
All-service activity supports coverage but does not establish complete capture.

Only partial boundary weeks are removed here. Weather exclusions, the initial lag
requirement, and the validation/test boundary exclusion belong to P2-003.
No forecasts, test-set model scores, or feature selection are produced here.

## Reproduce

From the repository root, using Python 3.9+ (no extra packages):

```sh
python3 scripts/prepare_potholes.py
```

The first run downloads a cache to `data/raw/potholes/snapshot.json` (ignored by Git).
Later runs reuse that cache. Add `--refresh` to download the live feed again; it may
have changed. Keep the original local snapshot to reproduce this exact CSV.

Contains information licensed under the [Open Government Licence – City of Edmonton](https://data.edmonton.ca/stories/s/msh8-if28).
DataBridge's processing is independent and is not endorsed by the City.
