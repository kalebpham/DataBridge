# Source inspection evidence - November 11, 2026

Contains information licensed under the [Open Government Licence - City of Edmonton](https://data.edmonton.ca/stories/s/Open-Government-Licence-Edmonton/msh8-if28/).

Source provider: City of Edmonton. This project is not endorsed by the City.
The source licence applies to the City's information; no repository code licence
is asserted over that source material.

These files support the [preliminary feasibility review](../../data-feasibility.md)
for issue #3. They do not constitute the final study dataset or research results.

- `requests_metadata.json` and `boundaries_metadata.json`: selected metadata and field descriptions from official dataset IDs `q7ua-agfg` and `65fr-66s6`. Cached column summaries and platform configuration are omitted.
- `category_extent.json` and `category_candidates.json`: available date range and candidate pothole labels across the live feed, including 2026. These are broader than the proposed study.
- `study_extent.json`, `study_months.json`, `study_descriptions_by_year.json`, `study_neighbourhoods.json`, and `duplicate_statuses.json`: server-side source-quality aggregates for the six-label road-pothole filter during 2023-2025. The neighbourhood aggregate is for identifier/join checks; no hotspot ranking was calculated.
- `request_sample.json`: first 20 matching records ordered by creation date and row ID, with selected public fields. This is a convenience sample, not a random sample or evidence of citywide missingness.
- `boundary_index.json`: current IDs, names and effective dates; it is not a historical crosswalk.
- `boundary_geometry_sample.json`: one current Kenilworth polygon demonstrating geometry availability, not a full geometry validation.
- `manifest.json`: candidate period/filter, source attribution and failure status. Attribution fields were added after the licence text linked from the official portal was read.

Each response file includes a source URL, retrieval time and SHA-256 of the
original response bytes. Metadata is projected after hashing, so its saved
projection will not reproduce the original response hash. Other data arrays are
the decoded original responses. Queries were separate live reads; minor changes
between responses are possible and should be reconciled in a frozen full extract.

The source inspection script is
[`scripts/inspect_data_sources.py`](../../../scripts/inspect_data_sources.py).
Re-run it into a new directory to preserve this evidence. The inspection made
12 successful public API requests; `manifest.json` records no failed queries.
