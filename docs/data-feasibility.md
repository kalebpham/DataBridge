# Preliminary data feasibility: Pilot 01

**Issue:** [#3](https://github.com/kalebpham/DataBridge/issues/3). **Owner:** Kaleb Pham. **Reviewer:** Estella Li (pending).

**Inspection date:** November 11, 2026. **Recommendation:** Conditional go for planning a historical neighbourhood report-volume study; resolve comparability and measurement questions before full collection and analysis. The [follow-up comparability review](data-comparability.md) adds historical boundaries and daily/channel/duplicate diagnostics; its recommendations should inform the study design.

This document reports source inspection, not research findings. It uses metadata, a non-random 20-row sample, a current boundary index, one polygon, and server-side aggregates. No neighbourhood rankings, fitted models or hypothesis tests have been produced.

## Sources and reproducibility

| Official source | Dataset or page | Use |
| --- | --- | --- |
| [311 Requests](https://data.edmonton.ca/City-Administration/311-Requests/q7ua-agfg) | `q7ua-agfg`; [metadata](https://data.edmonton.ca/api/views/q7ua-agfg.json) | Request fields, category labels, dates, missingness and identifier checks. |
| [City 311 documentation](https://www.edmonton.ca/programs_services/311-open-data) | Source explanation and archive links | Centre-point geography, missing locations and intended interpretation. |
| [City of Edmonton - Neighbourhoods](https://data.edmonton.ca/City-Administration/City-of-Edmonton-Neighbourhoods/65fr-66s6) | `65fr-66s6`; [metadata](https://data.edmonton.ca/api/views/65fr-66s6.json) | Current neighbourhood names, identifiers, effective dates and polygon geometry. |
| [Open Government Licence - Edmonton](https://data.edmonton.ca/stories/s/Open-Government-Licence-Edmonton/msh8-if28/) | Current portal licence page and its embedded public licence document | Source-use conditions and attribution; the linked text was read for this inspection. |

The [dated evidence directory](evidence/2026-11-11/) contains the queries, retrieval timestamps, response hashes and results supporting the numerical statements below. Metadata files retain selected fields rather than all platform caches. The other query responses are retained as returned. `manifest.json` records the six-label proposed road filter and sample limitations.

To repeat the bounded inspection with Python's standard library, use a **new** output directory:

```powershell
python scripts/inspect_data_sources.py --output docs/evidence/new-inspection
```

The script makes public read-only API requests, retrieves only 20 individual request records, and does not create the full analysis dataset. Source records and statuses can change between queries; these are not transactionally synchronized snapshots. Re-running later can yield different results. The script refuses to overwrite an existing snapshot and fails rather than treating capped grouped results as complete.

## Availability, categories and study period

The live `Potholes` category had **44,762 rows**, spanning **January 1, 2023 to November 10, 2026** in the inspection. Its metadata says current year plus two previous years, while another metadata field says coverage from 2016 onward. Neither description establishes actual retained coverage: the dated aggregate query is the evidence for the records currently accessible. Archives are discoverable through the City's 311 page, but their schemas and completeness have not been inspected for this task.

Filtering only on `service_category = 'Potholes'` would mix road reports, alley reports and information requests. The six exact road labels in the [scope draft](research-proposal.md#proposed-request-filter) occur in each proposed study year. Excluded examples include `Info Asphalt  and  Potholes`, `Info Pothole Repair Timeline`, `POTHOLE:Alley Pothole`, `ETS Pothole` and gravel/washboard labels outside the main category. Similar-looking labels must not be merged by an undocumented substring rule.

For the six-label filter and **2023-2025** window, the preliminary aggregates are:

| Year | Matching rows | With non-null neighbourhood ID | Months with matching rows |
| --- | ---: | ---: | ---: |
| 2023 | 4,886 | 4,676 | 12 |
| 2024 | 4,605 | 4,496 | 12 |
| 2025 | 13,456 | 13,199 | 12 |
| Total | 22,947 | 22,371 | 36 |

The large change in 2025 needs interpretation. Follow-up checks find increases in both app and phone reports and a larger duplicate-flagged share; requests without that flag also increase. The main road label increases within its existing definition, while overall all-service volumes are broadly similar. These checks do not establish whether reporting, operations, coding or physical conditions caused the change. See the [year-specific evidence and limits](data-comparability.md#2025-reporting-change); do not interpret this as measured road damage.

**Recommendation:** Start with 36 calendar months, aggregating to complete seasons and years for persistence. Low citywide winter volumes make weekly neighbourhood comparisons a poor default for this initial scope. Presence of records in all months supports a candidate window, but is not proof of complete daily ingestion or neighbourhood coverage. Exclude partial 2026 from the main comparison.

## Location quality and boundary compatibility

- **576 / 22,947 rows (2.51%)** lack a neighbourhood ID; **563** lack both ID and name. Thirteen have a name but no ID. Non-null is not equivalent to a valid join.
- There are **404 distinct non-null request neighbourhood IDs** under the proposed filter. The current boundary index has **407 records and 407 unique IDs**.
- Six request IDs do not match that index: `1150` (OLIVER, 127 rows), `2691` (HORSE HILL NEIGHBOURHOOD 1A, 3), `4485` (LEWIS FARMS INDUSTRIAL, 59), `5462` (CHAPPELLE, 51), `5464` (HERITAGE VALLEY TOWN CENTRE, 17), and `5575` (WINDERMERE AREA, 15). That is **272 additional rows** requiring geographic resolution; they are separate from missing-ID rows.
- The current index includes effective start dates within or after the study window. These dates can reflect a naming or administrative change rather than creation of a physically new neighbourhood. For example, it contains ID `1151` with a 2024 effective start, while historical reports include `1150`. This observation alone does not justify treating the polygons as identical.
- The selected Kenilworth record (`6350`) returns a `MultiPolygon`, confirming actual polygon availability. Geometry validity, completeness across all polygons and historical equivalence remain unchecked.

Use `neighbourhood_id` to `neighbourhood_number` as the candidate join, normalizing numeric representations to canonical integer strings. Use names for audit/display, not automatic fuzzy joins. Verify a historical crosswalk or boundary version for old/new IDs. Exclude unresolved units from spatial comparisons and disclose their counts; do not silently drop them or assign them to a nearby centre point. A fixed comparable cohort is still to be established.

Follow-up inspection identifies an [official 2021 boundary snapshot](https://data.edmonton.ca/d/5bk4-5txu) containing all six unmatched historical IDs. Its `neighbourh` field serializes IDs with `.0`, requiring whole-number normalization. It offers an alternative historical reference layer; it does not prove boundary stability through 2025. Candidate crosswalks and rejected name-based substitutions are documented in the [geography follow-up](data-comparability.md#historical-neighbourhood-boundaries).

The City's documentation and field descriptions identify request coordinates as **neighbourhood or ward centres**, not incident positions. Never use them for individual-pothole mapping, road-segment assignment, within-neighbourhood density or recovery of exact locations. Aggregate by recorded neighbourhood ID before joining a validated polygon layer.

## Duplicates and the meaning of a row

All **22,947** inspected matching rows have a `row_id`, and all IDs are distinct in the server aggregate. This supports an identifier audit; it does not prove each row is a distinct physical incident. The source describes IDs as system-generated request identifiers and reports that duplicates are removed in its metadata.

However, **7,701 matching rows (33.56%)** have `status_detail = 'Duplicate Request Exists'`. Such records also occur in the inspected sample. These are distinct request IDs with a duplicate-related status, not repeated copies of the same ID.

Proposed handling:

1. Audit repeated IDs during full extraction; collapse byte-identical copies and quarantine conflicting versions until a documented resolution is possible.
2. Retain distinct IDs with duplicate-related statuses in the main **report-volume** measure.
3. Repeat descriptive comparisons excluding that status, explicitly changing the measure to reports without that recorded flag. It still does not estimate unique potholes.
4. Never deduplicate different IDs on date plus centroid: many unrelated reports share those values. Open/closed status and closure date do not establish repair completion.

## Preliminary field dictionary

| API field | Source type | Proposed use and caution |
| --- | --- | --- |
| `row_id` | Text | Published request identifier; preserve as text, audit uniqueness. |
| `date_created` | Floating/calendar date | Defines study inclusion and report month. Returned timestamps have no timezone suffix; confirm source convention rather than converting them as UTC. |
| `service_category` | Text | Exact main category filter; case/spacing are meaningful. |
| `service_description` | Text | Explicit six-label road subset; classification comparability needs review. |
| `neighbourhood_id` | Number, serialized as a string | Candidate geographic join. Missing and unmatched values require separate accounting. |
| `neighbourhood` | Text | Label and cross-check; not a stable historical identifier. |
| `nbhd_latitude`, `nbhd_longitude`, `nbhd_location` | Number/location | Neighbourhood centre for display only, not incident coordinates. |
| `ward`, `ward_location` | Text/location | Optional contextual geography; not a substitute for a missing neighbourhood. |
| `request_status`, `status_detail` | Text | Snapshot of processing status; duplicate-related sensitivity, not verified condition or repair. |
| `interaction_channel`, `referral_type` | Text | Audit reporting/handling mix; no assumption that every row is a unique resident or inspection. |
| `date_closed` | Floating/calendar date | Not needed for the primary outcome; source definition does not promise completed repair. |
| `year`, `month_number`, `month` | Number/text | Audit against `date_created`; derive analytical periods consistently from the latter. |
| `count` | Number | Source charting helper described as equivalent to a row count; do not treat it as potholes per ticket. |
| Boundary `neighbourhood_number`, `name` | Number/text | Current unique ID and display label; historical compatibility is conditional. |
| Boundary `effective_start_date`, `effective_end_date` | Floating/calendar date | Administrative dates with empty field descriptions; do not infer complete geographic histories. |
| Boundary `geometry_multipolygon` | Multipolygon | Candidate neighbourhood outlines; validate geometry and version before mapping. |

## Missing coverage, rates and terms

Construct a neighbourhood-month panel only after fixing the cohort and source-coverage audit. Store a separate coverage flag and reason. A period with no source records is unknown until a defensible coverage rule supports zero; dates with no pothole reports do not on their own prove outages either. Review all-service source activity and documentation as supporting checks, recognizing that these do not guarantee pothole-specific completeness. Present exclusion and missing-location totals by time.

The follow-up all-service check finds source records on every calendar day in each of the 36 proposed months. This rules out wholly empty all-service days in the inspected feed, but does not prove full ingestion or pothole-specific completeness. The coverage-mask rule remains a study-design decision.

No road-length dataset has been inspected, and no exposure denominator is validated. Keep rates and road-length modelling outside the core study. Polygon area and neighbourhood population must not be substituted for road length without changing the question.

Both inspected dataset metadata files label the licence **See Terms of Use** (`SEE_TERMS_OF_USE`). The linked current portal page is titled **Open Government Licence - Edmonton**, Version 1.0, July 2022. Its embedded public text permits copying and adaptation subject to source acknowledgement, and excludes rights in personal information and specified third-party/official-symbol material. The retained public evidence includes attribution and a licence link in its README and manifest; this is not a transfer of the City's data rights to DataBridge. Cite the City, dataset titles, source URLs and retrieval date; do not apply a future code licence to source data or imply City endorsement. The small retained sample uses already-published fields without attempts to identify reporters or recover incident locations. Estella's broader ethics/source-use assessment (#6) remains pending, including checking any additional restrictions on future sources.

## Review gates and unresolved gaps

| Question | Current evidence | Next decision |
| --- | --- | --- |
| Can we start scoping a monthly study? | Candidate fields, 36 populated months and road labels exist. | Review the candidate period and filter with Estella. |
| Are years fully comparable? | 2025 increase persists across channels and without duplicate flags; cause unresolved. | Show years separately, preserve sensitivity checks and document assumptions; revise claims/window if necessary. |
| Can we map every report? | Historical 2021 polygons contain the six old IDs; some current-name substitutions are geographically invalid. | Verify actual transitions or apply consistent exclusions; approve a historical reference layer and fixed cohort. |
| Are repeat reports important? | One third carry a duplicate-related status. | Approve report-volume interpretation and sensitivity analysis. |
| Can absent records become zeros? | All-service records exist daily; complete ingestion and unit-level observability remain unestablished. | Agree a coverage rule using this supporting evidence before building the panel. |
| Can we report rates? | No verified denominator. | Use counts in the core study. |
| Is source-use review complete? | Current licence text read and public evidence attributed; broader assessment pending. | Incorporate into #6 and review any added sources before redistributing the full dataset. |

**Review record:** Estella's review is pending. Issue #3 remains open; this is a supported preliminary recommendation, not approval to bypass the remaining design tasks.
