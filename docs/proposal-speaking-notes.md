# Proposal presentation brief and speaking notes

**Issue:** [P1-007](https://github.com/kalebpham/DataBridge/issues/7)  
**Task owners:** Estella and Kaleb  
**Status:** Estella's speaking draft prepared; Kaleb's technical evidence, joint decisions, and rehearsal pending  
**Prepared:** November 11, 2026, with AI drafting assistance

Use these notes for the Phase 1 proposal discussion. The accompanying [PowerPoint discussion draft](../reports/proposal-presentation.pptx) turns the proposal into 11 editable slides with embedded notes. Both documents remain subject to technical completion and joint review; neither reports findings. The proposed eight-minute split gives each person approximately four minutes, including the shared conclusion. Adjust after a joint rehearsal.

## Run of presentation

| Section | Speaker | Suggested time | Purpose |
| --- | --- | --- | --- |
| 1. The question and why it matters | Estella | 1 minute | Introduce the general spatial question and reporting interpretation. |
| 2. Can the data support it? | Kaleb | 1 minute | Present the verified sources, coverage, and geographic resolution. |
| 3. What would we compare? | Estella | 1.5 minutes | Explain study units and the proposed persistence rule. |
| 4. How would we analyze it? | Kaleb | 1.5 minutes | Present the finalized comparisons, methods, and uncertainty plan. |
| 5. What can we responsibly conclude? | Estella | 1 minute | Explain bias, privacy, and limits. |
| 6. How would we carry it out? | Kaleb | 1 minute | Confirm tools, workload, resources, and timeline. |
| 7. Decisions before collection | Both | 1 minute, shared equally | Summarize readiness and the remaining decisions. |

## 1. Estella: the question and why it matters

**Suggested speaking text:**

> Our first DataBridge project asks which Edmonton neighbourhoods consistently have the most pothole reports, and what factors are associated with those patterns. We want to study general spatial patterns over several years, rather than predict a particular week.
>
> The distinction between reports and physical potholes matters. Our literature review brings together research on Edmonton reporting channels, a Houston pothole study, and work on interpreting 311 data. These sources motivate treating reports as records of service demand, with limitations, rather than a complete inventory of road damage.
>
> Our proposed contribution is a transparent neighbourhood comparison: which areas repeatedly have high reporting volumes, how that changes over time, and how data quality affects the interpretation. We are presenting a research plan today, not findings.

**Source support:** [Literature review](literature-review.md), particularly Lu and Johnson (2016), Cook et al. (2024), and White and Trump (2018). Retain these citations in any eventual slides; do not present the sources' findings as DataBridge results.

## 2. Kaleb: data feasibility handoff

Complete this section from P1-003 before describing the data as ready:

- Name the actual source datasets, their identifiers, and access dates.
- Show the verified date range, pothole category mapping, request identity, and neighbourhood fields.
- Explain whether geographic identifiers and boundaries are compatible across the selected years.
- Describe known coverage gaps and how zero counts can be distinguished from missing coverage.
- Identify applicable source licences and the feasible common study window.

If an item remains unresolved, report it as a feasibility question. Do not substitute the provisional 2023–2025 window for confirmed availability.

## 3. Estella: what we would compare

**Suggested speaking text:**

> We propose an observational study using existing municipal records. One observation would represent one neighbourhood during one calendar month. Monthly observations would let us describe seasonal patterns, while complete annual totals would support year-to-year comparisons.
>
> We need a common set of neighbourhoods with comparable coverage. A blank record is not automatically zero reports. We would first distinguish complete coverage, known gaps, and unresolved coverage, and keep unlocated requests visible in a quality summary.
>
> To make “consistently” measurable, our proposed definition selects the highest-reporting fifth of eligible neighbourhoods in each year. A neighbourhood would be considered persistently high reporting if it appears in that group in at least two-thirds of the included years. With three years, that means at least two years. Tied positive counts would be included and disclosed, and we would examine other reasonable cutoffs rather than rely on a single map.
>
> These are proposed definitions for the team to agree before comparing ranked outcomes. They do not mean a neighbourhood is a statistically significant cluster or that its roads are less safe. The study dates and final eligibility rules still depend on the feasibility findings.

**Source support:** These are original proposed design choices in [methodology.md](methodology.md), not thresholds established by the literature. The full protocol documents ties, sparse counts, exclusions, and sensitivity checks.

## 4. Kaleb: analysis handoff

Complete this section from P1-001 and P1-005:

- State the final descriptive and inferential questions separately.
- Explain the count/rank tables, monthly summaries, and persistence comparisons to produce.
- Explain which optional associated factors are actually available and why they are relevant.
- Justify any count model, comparison, and uncertainty method; account for repeated observations and spatial/temporal dependence.
- Distinguish raw volumes from any road-length-adjusted rate and explain the denominator.
- Explain which diagnostics would change the analysis and how exploratory changes will be recorded.

Do not imply that fitting a model is necessary for a useful descriptive project, or that an unverified variable will be collected.

## 5. Estella: responsible conclusions

**Suggested speaking text:**

> The central limitation is that reporting depends on both local conditions and the process of reporting. Different road networks, missing locations, and different ways of contacting the City may affect neighbourhood counts. A lower count does not prove that an area has fewer defects or less need for maintenance.
>
> We would use neighbourhood-level outputs and avoid trying to recover exact incident locations or identify residents. Before using or sharing data, we need to check the selected dataset terms, attribution requirements, and privacy implications. The ethics assessment records those checks; it does not claim that an institutional determination has already been made.
>
> Our conclusions would stay within the verified study period and records. We can describe repeated reporting concentrations and supported associations, but not claim causal effects, complete physical pothole counts, or validated road safety rankings.

**Source support:** [Ethics and limitations](ethics-and-limitations.md) and its cited official guidance; [literature review](literature-review.md) for the reporting interpretation.

## 6. Kaleb: resources and delivery handoff

Confirm these jointly rather than treating the proposal estimates as commitments:

- Tool choice and who can run the workflow.
- Data storage/access arrangement and any resource needs.
- Availability of both team members and an agreed kickoff date.
- Time for collection, analysis, report writing, presentation, poster, and review.
- A contingency if the source inventory cannot support the planned comparison.

## 7. Shared closing

**Estella's suggested text:**

> Our planning documents now give us a starting design, the literature behind its interpretation, and a record of ethical and measurement limitations. Before moving to full collection, we need to agree on the common study window, eligibility rules, and definitions, using the actual source checks.

**Kaleb's part:** State which technical decisions are supported by evidence, which remain unresolved, and the agreed next action. Neither speaker should imply the team has approved a decision that is still open.

## Questions to prepare for

| Likely question | Proposed answer |
| --- | --- |
| Why study neighbourhoods? | The design uses the verified geographic resolution and compatible identifiers. Exact-road conclusions require different evidence. |
| Why monthly observations? | They retain seasonal context while annual totals support persistence comparisons. Final suitability depends on coverage and sparsity. |
| Why select the top fifth? | It is a transparent starting definition, not a natural or statistically established cutoff. The plan includes alternative cutoffs and explicit tie handling. |
| What if three comparable years are unavailable? | Revise the period or question before testing persistence; a smaller descriptive study may still be useful. |
| Does a hotspot mean worse roads? | It means higher recorded reporting under the stated definition. Exposure, reporting behaviour, and measurement can also affect counts. |
| Are we ready to collect all the data? | Only after source feasibility, relevant data-use checks, and the protocol decisions have been resolved and recorded. |

## Final preparation checklist

- [ ] Estella reads her sections aloud and revises them into her own speaking style.
- [ ] Kaleb fills the technical sections with linked evidence from P1-001, P1-003, and P1-005.
- [ ] Both agree on the design and any decisions that remain open.
- [x] Prepare an editable discussion deck with readable citations and speaker notes.
- [ ] Both update the deck after technical decisions are finalized and review the content.
- [ ] Rehearse together, verify an approximately equal speaking split, and record feedback.

No dataset statistics, maps, coefficients, significance results, or model performance values are available to insert at this stage.
