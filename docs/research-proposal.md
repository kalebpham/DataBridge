# Phase 1 research proposal: neighbourhood pothole reporting patterns

**Shared issue:** [P1-007](https://github.com/kalebpham/DataBridge/issues/7)  
**Task owners:** Estella (@estella1221) and Kaleb (@kalebpham)  
**Status:** Working draft; Estella's background/design/ethics contribution prepared, technical decisions and joint approval pending  
**Prepared:** November 11, 2026, with AI research and drafting assistance

## Background and rationale

DataBridge's first pilot will examine where pothole service requests are concentrated within Edmonton and whether those reporting patterns recur over time. The intended contribution is an accessible, reproducible neighbourhood comparison with transparent definitions and data-quality documentation.

The [literature review](literature-review.md) summarizes three research papers and two City publications relevant to interpreting reports, geographic precision, and existing local work. It motivates measuring reporting activity directly and keeping claims about road damage, resident behaviour, and future prediction separate from the core descriptive question.

## Question and objectives

**Working question:** Which Edmonton neighbourhoods consistently have the most pothole reports, and what factors are associated with these patterns?

Objectives:

1. Verify that comparable neighbourhood-level data exist over a common historical period.
2. Describe annual reporting volumes and monthly patterns.
3. Identify areas that repeatedly meet an agreed high-reporting definition.
4. Investigate associated factors only when verified data and appropriate methods support them.
5. Communicate results and limitations through a reproducible report, presentation, poster, and public summary.

The working primary hypothesis is that neighbourhood differences persist after accounting for seasonality and coverage. Kaleb's scope and analysis tasks must refine the statistical hypotheses, comparison targets, and methods before any tests are performed.

## Proposed study design

The [methodology draft](methodology.md) specifies a retrospective observational design, neighbourhood-month units, eligibility and coverage rules, handling of duplicate exports, and compatible geographic identifiers. It proposes 2023–2025 only if all three years are verified as complete and comparable; otherwise dates must be revised before analysis.

The proposed persistence definition selects the highest-reporting fifth of eligible neighbourhoods each year, with explicit handling of tied counts, and identifies areas selected in at least two-thirds of the eligible years. This is an operational definition awaiting team agreement, not a test of statistically significant spatial clustering.

Raw report volume is the primary descriptive measure. Road-length-adjusted comparisons are optional and require a verified denominator. These decisions, exclusions, and the common geographic cohort must be frozen before comparing ranked outcomes.

## Ethics and limitations

The [ethics and limitations assessment](ethics-and-limitations.md) documents proposed privacy safeguards, licence verification, reporting bias, geographic limitations, and uncertainty about applicable ethics review. It does not constitute approval or an exemption determination.

The project will publish aggregate reporting comparisons with explicit dates and coverage. It will not represent these records as a complete pothole inventory, exact defect locations, causal evidence, or a validated road safety ranking.

## Technical sections pending Kaleb's work

| Required section | Evidence needed | Dependency |
| --- | --- | --- |
| Final scope and hypotheses | Agreed operational question and comparison targets. | P1-001 / #1. |
| Data sources and feasibility | Actual dataset identifiers, fields, category mapping, source terms, date coverage, and geographic compatibility. | P1-003 / #3. |
| Data dictionary and processing plan | Verified mappings for request identity, dates, neighbourhoods, missingness, and updates. | P1-003 / #3, coordinated with Estella's methodology. |
| Analysis and interpretation plan | Chosen comparisons/models, assumptions, diagnostics, uncertainty, and sensitivity analyses. | P1-005 / #5. |

These sections remain unverified. Links to general data portals are not substitutes for an inspected source inventory.

## Responsibilities, resources, and provisional schedule

Kaleb owns question/scope, data feasibility, and the analysis plan. Estella owns the literature review, study design, and ethics/bias assessment. Each reviews the other's work. Both own final proposal integration and the proposal presentation.

Use GitHub for reviewed documents and version history. Select Python or R and any mapping/reporting packages after confirming the data and analysis needs. No paid service or compute requirement is assumed.

| Relative stage | Planned work and exit condition |
| --- | --- |
| Phase 1, proposed week 1 | Complete feasibility, resolve design choices, review each document, and agree on the proposal and a short presentation. Extend planning if critical data questions remain. |
| Phase 2, proposed week 2 | Collect and prepare verified data under the agreed protocol; pass the coverage and quality checks. |
| Phase 3, proposed weeks 3–4 | Produce descriptive comparisons and appropriate analyses; check robustness and interpretation. |
| Phase 4, proposed week 5 | Prepare a cited scientific report, oral presentation, and research poster. |
| Additional week if needed | Resolve revisions, review reproducibility, and conduct the club retrospective. |

These are relative estimates, not committed dates. Both team members must agree on capacity and kickoff timing. The four research phases follow the supplied SCI 201 Fall 2026 syllabus (pp. 1, 5); the club retrospective is separate.

## Proposal presentation outline

An [11-slide PowerPoint discussion draft](../reports/proposal-presentation.pptx) is available with source references and embedded speaker notes. Its study window and definitions remain proposed; verified technical evidence and joint review are still required.

The [presentation brief and speaking notes](proposal-speaking-notes.md) provide Estella’s speaking draft, an equal-time run of presentation, and the evidence Kaleb needs to supply. The notes are not a completed slide deck or joint approval.

Split preparation and speaking time equally:

- **Estella:** background and literature, proposed study design, ethics, and interpretation limits.
- **Kaleb:** final question/hypotheses, data feasibility, technical analysis plan, and resources/timeline.
- **Together:** explain remaining decisions and answer design questions before moving to collection.

## References and readiness checklist

The linked [literature review](literature-review.md) contains full citations. The [ethics document](ethics-and-limitations.md) links the institutional guidance and source terms to verify. Retain the same references and decisions in the final consolidated proposal.

- [ ] Estella checks the research drafts and incorporates agreed changes.
- [ ] Kaleb completes and links P1-001, P1-003, and P1-005 evidence.
- [ ] Both finalize dates, cohort, hotspot definitions, data-use checks, and methods.
- [ ] Each reviews the complete proposal and records agreement.
- [ ] Both finalize the proposal presentation and realistic schedule.

No analysis results are claimed, and the proposal is not ready for approval until the listed dependencies are resolved.
