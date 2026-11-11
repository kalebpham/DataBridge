# Pilot 01: Edmonton neighbourhood road-pothole reporting patterns

**Status:** Scope and operational definitions approved for [issue #1](https://github.com/kalebpham/DataBridge/issues/1), as reported by Kaleb in conversation on November 11, 2026. Geographic eligibility and coverage remain subject to the data-feasibility and study-design checks. The complete proposal is still in preparation.

**Prepared:** November 11, 2026.

**Task owner:** Kaleb Pham. **Reviewer:** Estella Li. Team approval received through Kaleb on November 11, 2026.

**Related work:** [Data feasibility](data-feasibility.md), [draft analysis plan](analysis-plan.md), and [shared proposal issue #7](https://github.com/kalebpham/DataBridge/issues/7).

## Purpose and primary question

Use published Edmonton 311 records to describe the geographic persistence of road-pothole reporting. The audience is students and readers interested in how public service-request data can be analyzed responsibly. There is no City partnership or operational maintenance use established.

**Approved primary question:** Among Edmonton neighbourhoods that can be compared on a consistent geographic basis, which have the highest volumes of published road-pothole reports during 2023-2025, and which remain high reporting across years and complete seasons?

The outcome is **published request activity**, not the number of unique physical potholes, road condition, or maintenance quality. Multiple requests can concern the same defect; a request can also be unconfirmed. A neighbourhood with few requests is not necessarily in good condition.

## Approved starting scope

| Decision | Approved starting choice | Condition before finalizing |
| --- | --- | --- |
| Study period | January 1, 2023 through December 31, 2025; API upper bound January 1, 2026 exclusive. | All 36 months appear in the feasibility query. Audit source continuity and changes in classification before interpreting trends. |
| Unit | One eligible neighbourhood in one calendar month. | Confirm missing/zero rules and geographic comparability in Estella's study design (#4). |
| Geography | A fixed cohort of neighbourhood IDs with defensible boundaries throughout the study period; include residential and industrial areas under the same documented eligibility rules. | Current polygons alone do not establish historical comparability. Resolve old/new IDs and boundary changes, or exclude affected units transparently. |
| Core outcome | Count distinct published `row_id` values meeting the explicit road-pothole filter below. | Resolve missing IDs and conflicting duplicate-ID rows during the full extraction audit. |
| Main summaries | Monthly and annual counts, annual hotspot membership, complete-season comparisons, and maps. | Freeze cohort, filter, coverage mask, and tie rule before calculating neighbourhood rankings. |
| Additional factors | Calendar month and year; road length only as a separately justified extension. | Road length, traffic and weather are not prerequisites for this pilot. |

2026 is excluded from the main study because it is incomplete at planning time. The live feed currently contains 2023, but its metadata describes a shorter rolling retention policy. Preserve the dated feasibility evidence and freeze a documented extraction promptly after design review; continued availability is not guaranteed. If 2023 cannot be recovered, agree on a revised period and persistence rule before analysis.

### Proposed request filter

Require `service_category = 'Potholes'` and one of these exact `service_description` values:

- `POTHOLE:Road Pothole`
- `Road Pothole`
- `Pothole: Arterial Road`
- `Pothole: Residential Road`
- `Pothole: Collector Road`
- `Pothole: Industrial Road`

These labels were observed in the official feed and form the approved starting grouping; their definitions have not been proven constant over time. Exclude information-only labels, alley reports, gravel/washboard categories, and the ambiguous ETS-specific labels from the main analysis. Record their counts and reasons in the eventual collection log. An alley-inclusive analysis could be a separately labelled sensitivity check. Discovering an unclassified label requires a documented amendment, not silent inclusion.

Do not restrict to closed requests: closure is not confirmation that a pothole was repaired. Keep separate request IDs marked `Duplicate Request Exists` in the main report-volume measure, and assess their exclusion as a sensitivity analysis. This preserves the distinction between duplicate data rows and repeat reports about an incident.

## Operational definitions

**Report count:** `Y[n,t]`, the number of distinct qualifying published request IDs assigned to neighbourhood `n` in month `t`, after documented handling of duplicate IDs. A count describes reporting volume; it has no population or road-length denominator.

**Most reports:** Rank annual totals within the same eligible cohort and common observed months. The 36-month mean count per observed month is a companion summary; with equal coverage it gives the same overall order as total counts. Unequal observed months must not be hidden by comparing unadjusted totals.

**Reporting hotspot:** A descriptive high-volume group, not a statistically significant spatial cluster. For a period with `N` comparable neighbourhoods, let `k = ceil(0.10 * N)`. Use the kth-largest count as the cutoff, include all positive counts tied at that cutoff, and exclude zero counts. If fewer than `k` neighbourhoods have positive counts, include only the positive ones and flag the period as sparse. If every count is zero, no hotspot is defined and the period does not contribute to persistence. Ties can make the group larger than 10%; report its actual size. This starting definition is approved; any later change requires a recorded amendment.

**Consistently high reporting:** Membership in the annual hotspot group in at least **two of the three complete study years**, using one fixed eligible cohort. Also report the exact membership frequency (0/3 through 3/3), so the binary label does not conceal variation. A changed study period requires a new, agreed frequency rule.

**Seasonal persistence:** Report hotspot membership frequency across complete meteorological seasons: March-May, June-August, September-November, and December-February. Label winter by its ending year. Within the proposed window, winter 2024 and winter 2025 are complete; winter 2023 and winter 2026 are not. There are 11 complete seasons before any coverage exclusions. Report seasonal frequencies separately from the annual consistency label and compare like seasons where possible.

**Rate:** An optional count divided by a verified exposure, such as road kilometres. No rate will be reported until the denominator's meaning, period, coverage and geographic join are validated. Reports per resident and reports per road kilometre answer different questions; neither measures physical pothole prevalence.

**Observed zero versus unknown:** Zero requires an eligible neighbourhood-period and a defensible source-coverage flag, with no qualifying records after cleaning. No records, by itself, does not establish coverage. Unavailable or unresolved periods remain missing; missing-location requests are never distributed proportionally among neighbourhoods.

## Secondary questions and hypotheses

| Question | Proposed hypothesis | Null or comparison | Planned assessment |
| --- | --- | --- | --- |
| Are high-reporting areas persistent? | Annual high-reporting membership overlaps more than expected under a specified no-persistence reference. | Membership is independent between years conditional on each year's hotspot size. | Annual membership frequencies, tied-rank correlations and overlap. Any reference comparison is conditional on an adequately justified dependence model; see the analysis plan. |
| Do neighbourhood differences remain after accounting for time? | Expected report counts differ by neighbourhood after allowing for calendar month and year. | No remaining neighbourhood effect under the specified count model. | Conditional exploratory count modelling with diagnostics; formal testing is gated on a defensible dependence strategy. |
| Do conclusions depend on measurement choices? | The main descriptive pattern is reasonably stable across duplicate-status and category sensitivity analyses. | No confirmatory null is specified for this robustness question. | Compare membership, ranks and excluded counts transparently. |
| If valid road exposure becomes available, is it associated with volume? | Larger road networks are associated with higher counts. | The road-length coefficient is zero in a separately specified model. | Optional between-neighbourhood association; cannot identify a time-invariant road-length coefficient alongside unrestricted neighbourhood fixed effects. |

The first hypothesis does not assert that observed persistence has been demonstrated. The independence reference is a descriptive benchmark whose limitations must be reported; it does not automatically provide a valid significance test for spatially dependent data.

## Intended deliverables

1. A documented neighbourhood-month dataset and reproducible preparation, subject to source terms and approved design.
2. Maps and tables describing report volume and annual/seasonal persistence, with coverage and exclusions visible.
3. A concise report and presentation explaining the question, methods, results, uncertainty and limits.
4. An internal retrospective identifying what the pilot teaches DataBridge about project scope, roles, reviews and realistic timelines.

Forecasting is outside the core scope. Any forecasting extension needs its own target, historical baseline and chronological evaluation.

## Decisions and review still needed

- [x] Kaleb reported team approval of the question, 2023-2025 monthly starting period, road-only filter, hotspot rule and consistency definition (#1), November 11, 2026.
- [ ] Finalize the actual geographic cohort and coverage mask using #3 and #4; approval of the scope does not establish historical boundary compatibility.
- [ ] Review feasibility evidence: coverage, 2025 volume change, duplicate statuses, missing IDs and historical/current geography mismatches (#3).
- [ ] Estella supplies literature implications (#2), the observational design (#4), and ethics/limitations assessment (#6).
- [ ] Agree on which analyses are descriptive, exploratory or confirmatory and how dependence will be handled (#5).
- [ ] Both assemble and review the complete proposal, resources, responsibilities, timeline and short presentation (#7).

**Approval record:** Team approval received through Kaleb in conversation on November 11, 2026. It covers the starting research scope and definitions. The literature review, observational design, ethics assessment, analysis-plan review and complete proposal remain separate tasks. Finalize geographic eligibility and coverage using issue #3's findings and the study design before moving to full analysis.

The SCI 201 phases are a starting framework for this pilot. DataBridge's club research process is being developed through the pilot and will be revised from experience; no course affiliation or endorsement is implied.
