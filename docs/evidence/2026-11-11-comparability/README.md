# Additional source comparability evidence - November 11, 2026

Contains information licensed under the [Open Government Licence - City of Edmonton](https://data.edmonton.ca/stories/s/Open-Government-Licence-Edmonton/msh8-if28/).

Source provider: City of Edmonton. No City endorsement is implied. The historical
layer's API metadata does not specify a licence tag; this gap is recorded for the
source-use review in [the follow-up notes](../../data-comparability.md).

Nine source responses were captured with
[`check_data_comparability.py`](../../../scripts/check_data_comparability.py):

- Historical boundary metadata and index from official dataset `5bk4-5txu`.
- Selected historical and current polygons for investigating six unmatched IDs and possible comparison areas. These are candidates, not approved mappings.
- Request identifier/date summaries for those areas, without individual request records.
- Monthly road-report channel and duplicate-status aggregates, category/description counts by year, and all-service daily-presence summaries by month for 2023-2025.

Each response file records the exact source URL, UTC retrieval time and original
response SHA-256. Metadata is projected after hashing. Other response arrays
are retained as decoded from the API. Separate live reads are not a transactional
snapshot. The script fails on capped grouped/index results and refuses to overwrite
an existing evidence directory.

`summary.json` is derived locally from these saved responses. It contains annual
source-quality totals, normalized historical ID counts and simple polygon
coordinate/bounding-box comparisons. These checks neither prove topological
equivalence nor establish that geographic boundaries were stable during the study.
They do not calculate neighbourhood hotspot rankings or test research hypotheses.
