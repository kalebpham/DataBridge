# Literature review: Edmonton pothole reporting patterns

**Issue:** [P1-002](https://github.com/kalebpham/DataBridge/issues/2)  
**Task owner:** Estella (@estella1221)  
**Reviewer:** Kaleb (@kalebpham)  
**Status:** Draft for review; no project data have been analyzed  
**Prepared:** November 11, 2026, with AI research and drafting assistance

## Purpose and search approach

Research question: **Which Edmonton neighbourhoods consistently have the most pothole reports, and what factors are associated with these patterns?**

This is a focused narrative review, not a systematic review. Searches on November 11, 2026 combined Edmonton, 311, potholes, reporting bias, neighbourhoods, and spatial patterns. Sources were selected for direct local relevance, original research on how to interpret 311 data, or official descriptions of the data-generating process. The five sources below comprise three research papers and two City publications. Search coverage is limited; the selection does not establish that our question has never been studied.

Publisher pages, accessible article text, and an author-hosted manuscript were consulted. Summaries distinguish published findings from our proposed design choices. No article tables, figures, or full texts are reproduced.

## 1. Edmonton reporting channels and spatial patterns

**Citation:** Lu, Q., & Johnson, P. A. (2016). Characterizing New Channels of Communication: A Case Study of Municipal 311 Requests in Edmonton, Canada. *Urban Planning, 1*(2), 18–31. [DOI](https://doi.org/10.17645/up.v1i2.621) · [Open article PDF](https://www.cogitatiopress.com/urbanplanning/article/viewFile/621/344).

**Methods:** The authors examined Edmonton service requests from 2013–2015 using reporting-channel shares, spatial hotspot analysis, and regressions relating channel use to neighbourhood characteristics.

**Finding:** Reporting shifted toward Internet-enabled channels, with spatial differences and digital inequalities in channel use.

**Limitations:** This is an older, observational study of multiple service categories, not a current pothole-specific measurement of physical road damage. Its spatial methods cannot automatically be transferred to today's geographic precision.

**Implication:** Where available, inspect reporting-channel composition and changes over time. Neighbourhood differences may reflect how people contact the City as well as local infrastructure conditions.

## 2. Separating pothole reports from service need

**Citation:** Cook, S. J., Zuhlke, S., & Saywitz, R. (2024). Potholes, 311 reports, and a theory of heterogeneous resident demand for city services. *Policy Studies Journal, 52*(3), 647–669. [DOI and open article](https://doi.org/10.1111/psj.12540).

**Methods:** The Houston study distinguished resident pothole requests from proactively serviced potholes and analyzed tract-year counts, including neighbourhood characteristics and road-length/population controls.

**Finding:** Report volumes were associated with both measured need and neighbourhood characteristics. The study treats service demand and infrastructure need as distinct quantities.

**Limitations:** Houston's maintenance records are themselves a proxy for need. Observational associations and the local administrative context do not establish equivalent effects in Edmonton.

**Implication:** Label our response as reported requests. Road exposure may help interpret counts, but identifying reporting bias separately from damage would require an independent condition measure. Our available-data plan does not yet include one.

## 3. What 311 data can measure

**Citation:** White, A., & Trump, K.-S. (2018). The Promises and Pitfalls of 311 Data. *Urban Affairs Review, 54*(4), 794–823. [DOI](https://doi.org/10.1177/1078087416673202) · [Author-hosted 2017 manuscript](https://bpb-us-e1.wpmucdn.com/sites.mit.edu/dist/1/1008/files/2016/07/White-Trump-Promises-Pitfalls-311-Data-UAR-2017.pdf).

**Methods:** The authors compared geographically aggregated 311 reporting with voter turnout, political donations, and census return rates.

**Finding:** Relationships differed across participation measures, undermining a simple interpretation of 311 volume as general civic engagement. The authors identify service demand as a more defensible interpretation.

**Limitations:** The study addresses the interpretation of aggregated reporting, not Edmonton pothole prevalence. The linked manuscript predates the journal issue; use the final journal citation when citing the published work.

**Implication:** Avoid claims about residents' engagement or individual behaviour from neighbourhood counts. Low reporting does not establish low need.

## 4. Current geographic constraints

**Citation:** City of Edmonton. (n.d.). *311 Open Data*. Accessed November 11, 2026. [Official documentation](https://www.edmonton.ca/programs_services/311-open-data).

**Evidence:** The City's documentation says released locations use neighbourhood or ward centre points, and some requests lack captured location information.

**Limitation:** This documentation is not an audit of the selected export. Exact fields and historical coverage still require verification.

**Implication:** Use neighbourhood identifiers and official polygons. Treat geographic completeness as a quality measure. Point-density maps or road-segment assignments from these coordinates would imply unsupported precision.

## 5. Edmonton's operational pothole context

**Citation:** City of Edmonton. (2025, May 21). *The City develops new tool in the battle against Edmonton's potholes*. Transforming Edmonton. [Official article](https://transforming.edmonton.ca/new-tool-in-battle-against-edmontons-potholes/).

**Evidence:** The City describes its Repair application, duplicate reporting, proactive inspections, and a tool intended to predict future pothole locations. It also explains the operational importance of traffic and defect characteristics.

**Limitation:** This is an operational communication, not an independently evaluated prediction study or a source of accessible training data and performance estimates.

**Implication:** Do not describe DataBridge as Edmonton's first pothole mapping or prediction initiative. Distinguish duplicate records from different requests about the same defect; do not invent a blanket duplicate-removal percentage.

## Synthesis and a defensible project contribution

The sources motivate three distinctions: reporting versus underlying defects, spatial patterns versus reporting access, and descriptive maps versus validated prediction. They also show that local work already exists. Our contribution can be a small, reproducible examination of **pothole-specific neighbourhood reporting persistence across a verified common historical period**, with transparent coverage checks and cautious interpretation. This is a proposed project contribution, not a demonstrated gap in all published research.

The core study should answer which areas repeatedly rank high within the observed records. It should not promise exact defect locations, causal explanations, or improved forecasts. A statistical model can describe conditional associations if the data and assumptions support it; fitting one is not necessary to make the descriptive study useful.

## Decisions this review informs

| Decision | Recommendation for the proposal |
| --- | --- |
| Outcome | Count distinct reported requests, with duplicates handled according to verified identifiers and source documentation. |
| Geography | Neighbourhoods with compatible identifiers and boundaries; never infer exact road locations from area centres. |
| Persistence | Define high reporting and a repeat-occurrence threshold before ranking neighbourhoods; see the proposed protocol in [methodology.md](methodology.md). |
| Time | Prefer complete comparable years, retaining month-level observations for seasonal summaries. |
| Comparison | Present volumes first. Add reports per road kilometre only if a valid compatible denominator is verified. |
| Interpretation | Discuss reporting access and data coverage; do not label neighbourhoods as unsafe or residents as less engaged. |
| Added variables | Prioritize verified, interpretable exposure variables. Keep weather contextual and additional demographic linkage outside the initial scope. |

## Review checklist

- [ ] Estella checks that the summaries and proposed contribution reflect the team's intent.
- [ ] Kaleb reviews source interpretations and feasibility implications.
- [ ] Confirm the study dates and geographic resolution against P1-003.
- [ ] Incorporate agreed revisions into the Phase 1 proposal (P1-007).

The SCI 201 planning framework comes from the supplied Fall 2026 syllabus, pp. 1 and 5: literature review, research design, ethics, and proposal preparation. Course materials are not redistributed here.
