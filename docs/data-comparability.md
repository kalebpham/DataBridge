# Issue #3 follow-up: geography and reporting comparability

**Prepared:** November 11, 2026. **Owner:** Kaleb Pham. **Review:** Pending for issue #3.

**Recommendation:** Retain the approved 2023-2025 monthly starting window for planning. Use the official historical boundary snapshot to investigate geographic harmonization, retain duplicate-related sensitivity analyses, and require year-specific comparisons. Proceed to study-design review with the unresolved geographic and measurement assumptions below explicitly recorded.

This is a source-quality investigation. It does not identify neighbourhood hotspots, estimate road damage, fit a model, or establish what caused the reporting increase.

## Evidence and reproduction

The [follow-up evidence directory](evidence/2026-11-11-comparability/) contains nine official API responses with retrieval times, queries and response hashes, plus a derived `summary.json`. It supplements the [initial feasibility review](data-feasibility.md) and its 12 source-inspection responses.

```powershell
python scripts/check_data_comparability.py --output docs/evidence/new-comparability-inspection
```

The script uses Python's standard library and the helper in `scripts/inspect_data_sources.py`. It saves bounded aggregates, a historical index and candidate polygons; it does not download all individual requests. Existing evidence directories cannot be overwritten. The derived summary normalizes whole-number IDs using decimal parsing: the historical field serializes values such as `1150.0`, while current/request fields use `1150`. Plain string comparison would produce false non-matches.

## 2025 reporting change

The same approved six-label road filter and complete calendar years give:

| Year | Road-report requests | Duplicate-flagged | Flagged share | Requests without that flag |
| --- | ---: | ---: | ---: | ---: |
| 2023 | 4,886 | 934 | 19.12% | 3,952 |
| 2024 | 4,605 | 1,024 | 22.24% | 3,581 |
| 2025 | 13,456 | 5,743 | 42.68% | 7,713 |

The duplicate-related status is `Duplicate Request Exists`. These remain distinct published request IDs, not duplicate rows to remove automatically.

Total 2025 volume is 2.92 times 2024 volume. Excluding that flag leaves a 2.15-fold difference. The increase in flagged requests contributes 4,719 of the 8,851 additional requests (53.3%), an arithmetic decomposition rather than a causal explanation. Repeat-report handling is important, but this status alone does not account for the whole increase.

| Year | Mobile App | Phone Call | Email | All-service records, all categories |
| --- | ---: | ---: | ---: | ---: |
| 2023 | 3,854 | 1,030 | 2 | 910,380 |
| 2024 | 3,658 | 946 | 1 | 895,854 |
| 2025 | 9,908 | 3,523 | 25 | 900,448 |

Both major reporting channels increase. The pattern is not confined to the app, and all-service feed volume is broadly similar across years. These diagnostics do not establish that recording practices or reporter behaviour remained constant.

All six road-description labels occur in every study year, and the main `POTHOLE:Road Pothole` label itself rises from 4,326 records in 2024 to 11,310 in 2025. Thus the aggregate change cannot be explained solely by the appearance of a newly named road class in our filter. Changes in coding or inclusion within existing labels are still possible.

Monthly duplicate-flagged counts and the category mix are retained for review. The early-2025 increase and changing duplicate-flag shares should be shown in source-quality plots when the dataset is assembled. Do not pool years without showing their separate patterns or interpret the increase as a measured increase in physical potholes.

### Relevant official operational context

The City's [account of its Repair application](https://transforming.edmonton.ca/new-tool-in-battle-against-edmontons-potholes/) describes a January 2024 launch and handling of repeat reports to reduce repeated inspections. It corroborates that reporting and operational deduplication are different concepts. It does not document that the published `status_detail` flag was applied identically over time, or establish the cause of the 2025 increase.

The article's operational totals are not directly reconciled with our six-label subset. Different scope, snapshots and business definitions may matter. Do not force our counts to equal those figures or treat the article as validation of feed completeness.

## Coverage: what the daily check establishes

The all-service aggregate contains records on **365 days in 2023, 366 in 2024 and 365 in 2025**. All 36 months have records on every calendar day. This finds no day with a complete absence of all-service records in the inspected feed.

It does **not** prove that every pothole request was ingested, that categories were captured consistently, or that every neighbourhood was observable. It is supporting evidence for a candidate coverage rule. The observational design still needs to define the coverage mask and flag known outages, missing IDs or geographic transitions. An observed zero means zero qualifying published requests under that rule, never zero physical defects.

## Historical neighbourhood boundaries

The City publishes [2021 Federal Census: Neighbourhoods as of Official Census Day](https://data.edmonton.ca/d/5bk4-5txu), dataset `5bk4-5txu`. Its metadata explicitly describes a historical boundary snapshot and says it is not updated. The inspected index has **403 rows and 403 distinct normalized IDs**. This is a useful historical reference, not proof that all boundaries stayed unchanged during 2023-2025.

All six IDs missing from the current 407-ID index exist in this historical snapshot with the expected names. The candidate polygon checks reveal why current names must not be used as an automatic crosswalk:

| Historical ID and name | Current comparison | Observed evidence | Decision for now |
| --- | --- | --- | --- |
| `1150` OLIVER | `1151` WÎHKWÊNTÔWIN | The City confirms the rename; request IDs switch around late October/early November 2024. Historical/current bounding boxes match, but stored coordinate arrays differ. | Strong candidate for a documented rename crosswalk; verify actual polygon equivalence and effective handling before adopting it. |
| `5462` CHAPPELLE | `5471` CHAPPELLE | Same name and bounding box; stored coordinate arrays differ. The new ID appears in the study requests in November 2025. | Candidate recoding, not an approved equivalence. Verify the source history and geometry. |
| `5464` HERITAGE VALLEY TOWN CENTRE | `5472` same name | Current bounding box extends farther west and coordinate arrays differ. New-ID requests appear in December 2025. | Do not assume a pure ID change; resolve the extent change or exclude both definitions from a fixed-cohort comparison. |
| `4485` LEWIS FARMS INDUSTRIAL | `4260` LEWIS FARMS and `4261` LEWIS FARMS BUSINESS EMPLOYMENT | Historical geometry exists; current records have 2026 effective starts. Candidate `4260` covers only a portion of the historical extent. | Use historical geography as the study-period reference; do not map all old requests into either current ID without verified history. |
| `2691` HORSE HILL NEIGHBOURHOOD 1A | `2671` MARQUIS | The two inspected bounding boxes are disjoint; both historical IDs existed separately in 2021. | Reject this proposed name/area-based substitution. Retain the old unit only if its study-period eligibility can be established. |
| `5575` WINDERMERE AREA | `5570` WINDERMERE | The two inspected bounding boxes are disjoint; both historical IDs existed separately in 2021. | Reject this name-based substitution. Do not merge them because their names are similar. |

The City's [Naming Committee announcement](https://www.edmonton.ca/city_government/city_organization/naming-committee) confirms the Oliver/Wîhkwêntôwin rename. It establishes naming history, not numerical polygon equivalence. Equal bounding boxes also do not prove equal polygons, and unequal coordinate arrays can reflect harmless vertex changes as well as real boundary changes. The current diagnostics are not a topological geometry test.

**Recommended design approach:** Start from one explicit historical reference layer, resolve supported ID transitions, and build a fixed cohort independently of reporting volume. Where a transition cannot be resolved, exclude the affected geographic definitions consistently across the comparison window and report excluded requests. Do not drop just the new-ID rows and fill the resulting neighbourhood-months with zero. An alternative larger harmonized area requires verified containment/crosswalk information and an explicit scope amendment.

Validate all retained polygons and any crosswalk before mapping. A historical snapshot solves the absence of the six old IDs from the current index; it does not alone solve study-period boundary comparability.

## What remains for the study design and review

- Approve the coverage-mask rule using the supporting daily/monthly checks and source documentation.
- Verify candidate rename/recoding geometry, effective dates and any changed boundaries. Use consistent exclusions when exact harmonization is not defensible.
- Keep annual summaries separate and run duplicate-status sensitivity analyses. Record the explanation for the 2025 change as unresolved unless stronger evidence is found.
- Confirm any additional source-use conditions for the historical layer: its API metadata has no explicit licence tag. Retain City attribution and the portal licence link; incorporate this metadata gap into the source-use review (#6).
- Review the feasibility recommendation with Estella and incorporate decisions into #4 and #5. No reviewer sign-off for issue #3 is recorded here.
