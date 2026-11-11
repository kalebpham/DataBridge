# Draft analysis plan: neighbourhood reporting persistence

**Issue:** [#5](https://github.com/kalebpham/DataBridge/issues/5). **Owner:** Kaleb Pham. **Reviewer:** Estella Li (pending).

**Status:** Conditional draft, November 11, 2026. Incorporate Estella's literature review (#2), study design (#4), and ethics review (#6) before freezing it. Only source-feasibility summaries have been inspected; no neighbourhood outcome rankings or hypothesis tests have been run.

This plan implements the proposed questions and operational definitions in the [scope draft](research-proposal.md). The [feasibility document](data-feasibility.md) identifies conditions that may require an amendment. The pilot will also test whether this planning/review approach is workable for future DataBridge teams.

## 1. Freeze inputs and eligibility

- Proposed period: January 2023-December 2025; monthly study units.
- Proposed outcome: distinct request IDs under the six-label road-pothole filter. Retain repeat reports with distinct IDs in the main measure.
- Freeze extraction timestamp, query/filter version, deduplication decisions, geographic crosswalk/boundary version and cohort before computing rankings. Preserve source identifiers, retrieval provenance and a cleaning/exclusion log.
- Resolve the six unmatched historical IDs and verify a fixed cohort with comparable geography over the study. Eligibility must not depend on whether a neighbourhood happens to have many reports. Apply one common cohort to annual/seasonal comparisons.
- Audit category changes and the 2025 volume discontinuity. If comparability fails, restrict the question or period and document the change before examining neighbourhood results.
- Create explicit coverage flags. Do not fill unverified absent neighbourhood-months with zero. For the primary three-year comparisons require a common set of 36 defensibly observed months; otherwise revise the primary period/cohort. Missing-location requests stay outside neighbourhood counts with their volume disclosed.

No raw extraction, inferential sample size or statistical power is established by the current planning evidence. The full dataset will require checks beyond the 20-row sample and aggregate audits.

## 2. Descriptive outputs

| Question | Variables and summaries | Output and interpretation |
| --- | --- | --- |
| Where is reporting volume highest? | Monthly `Y[n,t]`, annual totals and mean monthly counts over common coverage. | Ranked table and neighbourhood polygons; volume of published reports only. |
| Is high reporting persistent? | Annual hotspot indicators, exact membership frequency and complete-season indicators. | Membership matrix, frequency map and annual/seasonal overlap tables. |
| Are patterns seasonal? | Citywide and neighbourhood monthly counts; month-of-year summaries with yearly values shown. | Time plots and seasonal summaries. Three years are limited replication, not a long-term climatology. |
| Do measurement choices change the picture? | Duplicate-status exclusions, category scope and geographic resolution alternatives. | Sensitivity comparison of ranks, membership and records excluded. |

Use one common legend for count maps that are intended to be compared; mark excluded/missing polygons distinctly from zero. Include time period, cohort, filter, report definition and source attribution in captions. Avoid point heatmaps based on neighbourhood centres and avoid the label "road-damage hotspot".

## 3. Hotspot membership, ties and persistence

Use the proposed positive-count top-decile rule in the scope draft: `k = ceil(0.10*N)`, inclusive ties at the kth-largest count, positive counts only. Report actual group sizes. All-zero periods have undefined hotspot membership/persistence and remain explicitly flagged. In low-volume periods where fewer than `k` neighbourhoods have positive counts, flag the result as sparse rather than padding the group with zero-report areas.

For every eligible neighbourhood report annual membership as 0/3, 1/3, 2/3 or 3/3. Label at least 2/3 "consistently high reporting" only after the proposed definition is reviewed. Show the actual annual counts beside that label. Report the three pairwise annual Spearman correlations using average ranks for ties; correlations are undefined if a ranking is constant.

For each annual pair, report intersection size and Jaccard overlap `|A intersect B| / |A union B|`, along with both set sizes. Jaccard overlap is undefined for an empty union. Compare the intersection descriptively with `|A|*|B|/N`, the expected intersection under an independent uniformly assigned-membership reference with fixed group sizes. This reference is not a valid spatial/temporal independence assumption by default and will not generate confirmatory p-values.

Aggregate only complete meteorological seasons. Winter is December-February, labelled by its ending year. The proposed window supplies winter 2024 and 2025, and spring/summer/autumn 2023-2025: 11 complete seasons before coverage exclusions. Report the denominator of observed, defined seasons for every persistence summary; do not compare partial winters or silently count missing seasons as non-membership. Examine like-season year comparisons as well as the pooled seasonal frequency.

The top-decile cutoff and two-of-three rule are operational choices, not discovered natural thresholds. Report sensitivity to top 5% and 20% cutoffs with the same positive/tie rule, and distinguish strict 3/3 membership from the main 2/3 definition. Do not select whichever threshold gives the most appealing pattern.

## 4. Conditional count modelling and hypotheses

The core deliverable can be a reproducible descriptive study. Model-based analysis is a conditional extension for the hypothesis about neighbourhood differences after accounting for time.

A candidate mean model is `log(mu[n,t]) = alpha + neighbourhood[n] + month_of_year[t] + year[t]`. Start with a Poisson specification; consider negative binomial counts if conditional overdispersion warrants it and estimation is stable. Neither model is automatically appropriate just because the outcome is a count. Inspect design rank, separation/all-zero units, residual patterns and leverage; disclose model-specific exclusions instead of changing the descriptive cohort silently. Month and year terms can absorb shared calendar patterns but do not establish why those patterns occurred.

The proposed global null is that all identifiable neighbourhood effects are zero, conditional on the model. The alternative is that at least one differs. A global difference does not by itself demonstrate persistence of a particular hotspot; the annual/seasonal summaries address that separately.

Before reporting model uncertainty or testing this null:

1. Check conditional dispersion, observed-versus-fitted counts, zero frequencies, convergence and influential neighbourhoods/months. Excess zeros alone do not justify a zero-inflated model.
2. Examine within-neighbourhood residual autocorrelation and residual spatial association using a documented polygon-neighbour adjacency rule. Record isolated polygons and sensitivity to adjacency choices. Missing/invalid polygons limit these checks.
3. Choose and justify a dependence-aware inference procedure with the literature/design review. Neighbourhood-clustered errors alone do not handle dependence between adjacent neighbourhoods; independent-row bootstrapping is unsuitable. Three calendar years provide too few year clusters for a routine year-clustered approximation. A temporal/spatial block or explicit correlation model needs a justified block/correlation choice and enough replication.
4. If no defensible procedure is available within the pilot, retain fitted comparisons as exploratory and omit inferential confidence intervals and significance claims. Document the reason. Do not use an ordinary independent-observation likelihood-ratio p-value as a workaround.

If the team elects a confirmatory model test, record the final model, dependence procedure and one primary global test **before** fitting neighbourhood outcomes. Use a proposed two-sided familywise level of 0.05, subject to review. Any post-hoc pairwise family must be declared and adjusted (for example with Holm's method) using valid underlying tests. Report effect sizes and method-qualified 95% confidence intervals only when the inference method supports them; avoid ranking neighbourhoods solely by p-value. Explain Type I/II errors and assess design-specific power through a justified simulation if feasible. Until then, power is unknown and non-rejection cannot establish equivalence.

The published records are an administrative dataset, not a random sample of all physical potholes. Any intervals describe uncertainty under an explicit model; they do not account automatically for unreported defects, unknown coverage or measurement bias.

## 5. Optional exposure and sensitivity analyses

Counts are the primary measure. Do not divide by neighbourhood population, polygon area or road length until the selected denominator is verified and the resulting question is stated.

If road length becomes available, verify road class, lane-versus-centreline length, units, period, complete coverage and alignment to the study's geography. Document treatment of boundary roads and zero/missing exposure. A `log(road_km)` offset estimates reporting intensity under a proportional-exposure assumption; an estimated `log(road_km)` coefficient asks how volume scales with road extent. These are different models. A time-invariant road-length coefficient is not identifiable alongside unrestricted fixed effects for each neighbourhood; specify a separate between-neighbourhood or appropriately justified hierarchical model. Neither association is causal evidence about damage.

Required descriptive robustness checks, if supported by the collected fields:

- Exclude `Duplicate Request Exists` while retaining all other main rules; compare results with the main measure.
- Compare annual, complete-season and monthly descriptions; disclose sparse periods.
- Compare the frozen core geography with any separately justified harmonized cohort. Never quietly substitute a current polygon for an unresolved historical one.
- Assess a separately labelled alley-inclusive scope if the team approves the category mapping.
- Show source category/interaction-channel composition over time and review the 2025 discontinuity before attributing changes to neighbourhood characteristics.

These checks are not permission to choose a preferred result. Report material disagreements, changes in membership and excluded counts. New questions arising from the data must be labelled exploratory and added to a dated amendment log.

## 6. Reporting and completion gates

The report should distinguish source-quality observations, descriptive study results and any model-dependent conclusions. Include exact cohort/period, missing/excluded records, filtering decisions, operational thresholds, limitations and reproducibility instructions. No finding supports a claim that a neighbourhood has objectively worse roads or that residents' characteristics cause reporting differences.

Forecasting remains optional and separate. If undertaken, write a separate target/horizon, historical baseline and chronological train/validation/test design; keep all neighbourhoods from the same period together and use only information available at prediction time.

Before marking #5 complete:

- [ ] Resolve feasibility and geography decisions from #3 and the study-design issue #4.
- [ ] Incorporate the literature review and ethics/measurement limitations (#2 and #6).
- [ ] Agree the scope, cohort, coverage mask, thresholds and any inferential commitments.
- [ ] Obtain Estella's review and record the actual decisions/amendments.

No sign-off is recorded. This draft is useful preparation for review, not a completed analysis or a finalized club-wide research procedure.
