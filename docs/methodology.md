# Proposed observational study design

**Issue:** [P1-004](https://github.com/kalebpham/DataBridge/issues/4)  
**Task owner:** Estella (@estella1221)  
**Reviewer:** Kaleb (@kalebpham)  
**Status:** Proposed protocol; conditional on P1-001 scope agreement and P1-003 data feasibility  
**Prepared:** November 11, 2026, with AI research and drafting assistance

This document specifies proposed decisions rather than completed analyses. No source export, field mapping, coverage assessment, or model has been verified by this task. Calendar dates and eligibility must be finalized from Kaleb's feasibility findings before this becomes the approved protocol.

## 1. Question, design, and scope of inference

**Question:** Which Edmonton neighbourhoods consistently have the most pothole reports, and what factors are associated with these patterns?

Use a retrospective observational design with secondary municipal records. The target of description is **recorded pothole service requests attributable to eligible Edmonton neighbourhoods during the selected historical period**. It is not a probability sample of all road defects, residents, or travel experiences.

The principal outcome is report volume. “Most reports” means highest counts over comparable periods. “Consistently” will mean repeatedly qualifying as a high-reporting neighbourhood under the definition below. Associated factors are secondary and conditional on accessible data. No forecasts or causal effects are core deliverables.

## 2. Study period and unit

**Provisional date choice:** January 1, 2023 through December 31, 2025: three complete calendar years preceding the current year. This is a planning recommendation, not a claim that these data are available.

Use that window only if P1-003 verifies complete, comparable records for all three years. Otherwise select the latest three consecutive complete calendar years with compatible categories and geography, document the revision, and freeze the dates before outcome comparisons. Do not combine a partial year with full-year totals. If fewer than three complete years are available, report descriptive comparisons and revise the persistence question before testing it.

**Observation unit:** neighbourhood × calendar month. Monthly aggregation retains seasonal context without imposing a next-week prediction objective. Annual totals derived from the same eligible months will be used for the primary persistence comparison. Record date interpretation, source timezone, and month boundaries in the field mapping after checking metadata; do not assume a timezone for an undocumented timestamp.

Use a common geographic cohort with adequate coverage in every included year. Report how exclusions change the scope of the study. No sample-size or power claim can be made before the record inventory is known.

## 3. Operational definition of persistent high reporting

These are proposed rules to agree before examining ranked outcomes:

1. Let N be the number of neighbourhoods eligible throughout the complete comparison window.
2. For each year, rank annual request counts and select the highest k, where k = ceiling(0.20 × N).
3. Include neighbourhoods tied at the kth count, provided that count is positive; report that ties can select more than 20%. If the cutoff is zero, do not call the selected set meaningful high-reporting hotspots; revisit aggregation/feasibility before interpretation.
4. Define a persistent high-reporting neighbourhood as selected in at least ceiling(2 × Y / 3) of the Y eligible years. For a three-year window, this means at least two years.
5. Report each neighbourhood's count, annual rank, number of selected years, and eligibility alongside the classification. Present the thresholds as project definitions, not statistically significant cluster tests.

Use 10% and 25% selections as sensitivity checks, with all results reported rather than choosing the most compelling map. Summarize month-of-year patterns and year-to-year rank changes separately. If counts are too sparse to support rankings, revise and document the design rather than force classifications.

## 4. Variables and measurement plan

The names below are analysis concepts, **not asserted source field names**. P1-003 must supply the source-to-analysis mapping.

| Concept | Type and proposed use | Required verification |
| --- | --- | --- |
| Request identifier | Identifier for distinct requests and duplicate-export checks | Uniqueness scope across current and archived files; snapshot/update behaviour. |
| Request category | Inclusion filter for pothole service requests | Exact labels/codes and changes over the study window. |
| Request creation date | Defines calendar month and year | Meaning, parse format, timezone, missing/invalid values. |
| Neighbourhood identifier | Geographic grouping key | Whether it identifies the issue's area; stable codes, aliases, and boundary versions. |
| Monthly request count | Nonnegative integer response | Distinct eligible requests in a neighbourhood-month with known coverage. |
| Coverage indicator | Eligibility/quality variable | Source evidence for complete months; no-record cells alone do not establish coverage. |
| Month and year | Temporal controls and descriptive strata | Complete common periods. |
| Road length, optional | Exposure denominator or associated factor | Units, road classes, date, complete geographic coverage, compatible boundaries, positive lengths. |
| Reporting channel, optional | Sensitivity/measurement context | Availability and stable channel definitions. |
| Weather/traffic, optional | Context or separately justified association | Verified station/measurement coverage and appropriate spatial interpretation. |

Population is not automatically the preferred exposure denominator for road reports. Counts describe volume; reports per road kilometre describe volume relative to mapped road extent, not confirmed damage risk.

## 5. Inclusion and exclusion rules

Include records only when the verified category mapping identifies a pothole request, creation date falls in the approved window, and a valid neighbourhood key can be linked to the chosen geography.

Do not require a request to remain open or to have been repaired. Filtering by current status could omit older closed requests and distort time comparisons. Inspect the source's retention rules before assuming closed requests remain in exports.

Retain unlocated requests in an audit total and report their share by month/year. Exclude them from neighbourhood rankings without assigning them to a nearby centre point. Report excluded categories, invalid dates, out-of-window records, unresolved geographic keys, and overlapping exports in a record-flow table. Do not silently remove inconvenient observations or large valid counts.

**Missing versus zero:** build the neighbourhood-month panel only after establishing which combinations are eligible and covered. A covered cell with no eligible requests can be zero. Unknown or incomplete coverage is missing. The primary annual comparison requires all 12 covered months for each included neighbourhood-year and a common cohort across years. Global source gaps cannot be inferred away from active neighbourhoods.

## 6. Duplicate and update handling

Separate duplicate export rows from separate reports about the same physical issue. Remove exact repeated records with the same validated request identity and log the number removed. If repeated identifiers carry updates, define a deterministic source-documented snapshot rule and preserve the original creation date; do not count status updates as new requests.

Distinct request identifiers remain separate requests unless the provider documents a reliable duplicate link or equivalent rule. Shared neighbourhood centres and dates do not justify incident-level deduplication. Report unresolved duplicate uncertainty and any defensible alternative count as a sensitivity analysis; do not estimate physical pothole totals.

## 7. Geographic compatibility

Use the City's published geographic resolution as a constraint: general centre points are not incident coordinates ([City documentation](https://www.edmonton.ca/programs_services/311-open-data)). Join by verified codes and boundaries, not nearest-road or point-density methods.

Select and record a boundary version. Where names change but areas do not, document a reviewed identifier crosswalk. Where boundaries change, use a verified compatible common geography or exclude affected areas from the primary comparable cohort and report them separately. Do not allocate neighbourhood totals to new boundaries without defensible supporting data. Record unmatched keys and changes in the number of eligible areas.

## 8. Planned interpretation and statistical handoff

Primary outputs are a coverage audit, neighbourhood annual count/rank tables, monthly summaries, and descriptive hotspot/persistence maps. The [literature review](literature-review.md) motivates keeping reports and condition measurements distinct.

For P1-005, Kaleb should select an appropriate inferential method only after the data inventory and diagnostics. Count models may describe differences adjusted for month/year, but repeated neighbourhood observations and common citywide shocks require dependence-aware uncertainty. Spatial dependence should also be assessed. Predefine primary comparisons and address multiple testing if comparing many neighbourhoods.

Do not estimate a time-invariant road-length effect alongside a full set of neighbourhood fixed effects without addressing collinearity. Exposure offsets and neighbourhood effects answer different questions; road-length-adjusted reporting and raw volume should be presented separately. Avoid including citywide weather together with a complete set of month-year indicators and claiming independently identified weather effects.

The study may describe persistent reporting concentrations within its window. It cannot establish individual reporting propensity, identify every damaged road, prove a neighbourhood characteristic causes defects, or establish that fewer requests mean less maintenance need. Generalization beyond the study window requires additional evidence.

## 9. Reproducibility and SCI 201 alignment

Retain source URLs, export dates, licence references, field mappings, inclusion rules, processing decisions, counts at each cleaning step, and versions of source boundaries. Preserve a frozen input manifest where permitted; prefer download scripts to publishing raw request rows. No collection code is specified before the actual schema is verified.

This is SCI 201 Phase 1 planning: define study units, variables, spatial/temporal design, and analysis in advance. A small quality pilot informs Phase 2 collection; descriptive and inferential analysis belong to Phase 3; a cited report, presentation, and poster belong to Phase 4. The supplied Fall 2026 syllabus (pp. 1, 5) informs the framework, not course deadlines or an assessment submission.

## 10. Decisions needed before finalizing

| Decision | Proposed resolution | Status / owner |
| --- | --- | --- |
| Scope and hypotheses | Confirm the README question and the reporting interpretation. | Pending P1-001; Kaleb + Estella. |
| Dates and cohort | Use 2023–2025 only if verified; otherwise latest three compatible full years. | Pending P1-003; Kaleb. |
| Schema and category mapping | Record actual fields and pothole codes. | Pending P1-003; Kaleb. |
| Coverage and geography | Verify completeness and a common boundary/identifier system. | Pending P1-003; Kaleb; Estella incorporates. |
| Persistence definitions | Agree top 20%, tie handling, and two-thirds-of-years rule. | Proposed; both review before ranked analysis. |
| Denominator | Keep raw volumes primary; add road rates only with verified lengths. | Pending feasibility and analysis plan. |
| Inferential methods | Choose diagnostics, contrasts, and dependence-aware uncertainty. | Pending P1-005; Kaleb. |
| Ethics/data use | Resolve the dataset-specific checklist in the ethics document. | Pending P1-006 review; Estella + Kaleb. |

Drafting this protocol does not resolve its data dependencies or constitute either person's approval.
