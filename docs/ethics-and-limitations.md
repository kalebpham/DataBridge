# Research ethics, data use, and limitations

**Issue:** [P1-006](https://github.com/kalebpham/DataBridge/issues/6)  
**Task owner:** Estella (@estella1221)  
**Reviewer:** Kaleb (@kalebpham)  
**Status:** Draft assessment; dataset-specific checks and team review outstanding  
**Prepared:** November 11, 2026, with AI research and drafting assistance

## 1. Scope and ethics status

The proposed study uses official secondary data to compare neighbourhood pothole-reporting patterns. No participant recruitment, surveys, interviews, resident-level profiling, or attempts to recover exact request locations are planned. This document records issues to address; it is not an ethics approval or institutional determination.

[TCPS 2 (2022), Chapter 2, Articles 2.2 and 2.4](https://ethics.gc.ca/eng/tcps2-eptc2_2022_chapter2-chapitre2.html) describe circumstances in which public information or anonymous secondary information can be used without REB review, subject to the stated conditions. Public access alone is not a sufficient assessment of privacy or linkage risk. The [University of Alberta's guidance](https://www.ualberta.ca/en/research/services/research-ethics/do-i-need-research-ethics-approval.html) identifies the REB as the final authority on whether review is required and provides a route for determination questions.

**Project assessment:** the planned neighbourhood-level, non-identifying use may fit an exemption, but that conclusion is conditional on the actual selected data and linkage. Record the basis for the assessment after schema inspection. If uncertainty remains, or the scope expands to identifiable data or participant contact, seek institutional guidance before that activity. No exemption or approval has been obtained or represented here.

## 2. Licensing and source register

The City's catalogue provides an [Open Government Licence page](https://data.edmonton.ca/stories/s/Open-Government-Licence-Edmonton/msh8-if28/). Its full licence text could not be extracted during this desk review. A legacy [City Open Data Terms of Use document](https://www.edmonton.ca/sites/default/files/public-files/documents/Web-version2.1-OpenDataAgreement.pdf) also appears in search results. Neither should be assumed to govern every current or archived dataset without checking the selected dataset's metadata.

Before downloading the analysis dataset, complete this register and retain the applicable terms/version. Do not treat the club's eventual code licence as a licence for external data.

| Planned source | Intended use | Licence / attribution status | Required action |
| --- | --- | --- | --- |
| Official Edmonton 311 export and any archives | Neighbourhood-period report counts | Dataset not selected; applicable terms and attribution not yet verified. | Kaleb records dataset ID, licence link/version, permitted uses, redistribution terms, and attribution wording. |
| Official neighbourhood boundaries | Mapping and identifier joins | Exact layer/version not selected. | Verify licence, date, geographic coverage, and attribution. |
| Road-length/network data, optional | Exposure-adjusted summaries | Dataset and licence not selected. | Verify lawful reuse, units, road classes, and compatibility before deriving rates. |
| Climate or traffic data, optional | Contextual analysis | Not selected or needed for the core descriptive study. | Check source-specific terms before adding these data. |

For each approved source, record its title, provider, URL, dataset identifier, access/export date, version or time range, licence URL/version, exact required attribution, and whether raw or transformed redistribution is permitted. Until checked, publish planning documents and code rather than raw datasets.

## 3. Privacy and publication practices

Collect only fields needed for the agreed design. Do not retain names, contact details, free-text complaint descriptions, photographs, or unnecessary exact addresses. Request identifiers may be used locally to check duplicate records, but should not appear in public analysis tables.

Do not link reports to identifiable residents, infer home addresses, or attempt re-identification. Use neighbourhood summaries and appropriate aggregation in maps. Review small or unusual cells for disclosure risk before publication; any suppression or aggregation should be documented, not presented as a universal threshold that guarantees anonymity.

Store permitted raw inputs in an access-controlled team location outside the public repository. Agree on retention at project completion and document any deletion or preservation decision. Source data already being public does not remove the need to minimize unnecessary republication.

## 4. Bias and limitations register

The actions below are proposed research controls, not completed checks.

| Risk | Why it matters | Planned response and remaining limit |
| --- | --- | --- |
| Reporting access and willingness | Requests depend on who notices and reports problems. | Consider channel changes if available; interpret counts as reporting demand. Bias cannot be fully separated from damage without independent measurements. |
| Missing locations | Excluded unlocated requests may distort neighbourhood comparisons. | Report unlocated shares over time; do not assign them to nearby areas or assume missingness is random. |
| General centre-point coordinates | Published points may represent an area rather than an incident. | Use official neighbourhood keys/polygons; avoid street-level claims or point-density interpretation. |
| Duplicate exports versus duplicate complaints | Repeated rows and separate requests about one defect are different. | Deduplicate verified record identities; retain distinct reports unless a defensible provider rule supports another treatment. |
| Road extent and traffic | Areas differ in roads, exposure, and opportunities to notice damage. | Present raw volume clearly; add road-length rates only with suitable denominators. These rates still do not measure physical condition. |
| Coverage and system changes | Archives, category definitions, retention, or channel changes can create apparent trends. | Audit completeness, freeze category mappings, and use common comparable periods/cohorts. |
| Spatial/temporal dependence | Nearby areas and repeated months may not be independent. | Use appropriate diagnostics and uncertainty; avoid treating every row as an independent replicate. |
| Geographic aggregation | Boundaries and chosen time units can change patterns. | Document versions and eligibility; assess reasonable aggregation sensitivity without selecting only favorable results. |
| Ecological inference | Area summaries do not describe each person or road. | Avoid individual-level behavioural or demographic claims. |
| Stigmatizing maps | A high-reporting label may be read as an unsafe-area designation. | Title maps “reported pothole requests,” include dates and caveats, and explain data quality and exposure. |

The reporting interpretation follows [Lu and Johnson (2016)](https://doi.org/10.17645/up.v1i2.621), [Cook et al. (2024)](https://doi.org/10.1111/psj.12540), and [White and Trump (2018)](https://doi.org/10.1177/1078087416673202), summarized in the [literature review](literature-review.md). Geographic constraints come from [City documentation](https://www.edmonton.ca/programs_services/311-open-data). The City's [2025 Repair article](https://transforming.edmonton.ca/new-tool-in-battle-against-edmontons-potholes/) illustrates why inspection, maintenance activity, and resident reports should not be conflated.

## 5. Claims and communication

**Supportable after analysis:** which eligible neighbourhoods have higher recorded request volumes in the verified period; whether those rankings recur; and appropriately qualified associations supported by the chosen methods.

**Unsupported by this design alone:** exact pothole locations, a complete inventory of defects, road safety rankings, individual residents' reporting propensity, causal effects, proof of inequitable service delivery, or validated future predictions.

Record design changes and distinguish planned from exploratory analysis. Report negative or inconclusive findings, uncertainty, and excluded coverage. Do not fabricate sample sizes, effect estimates, or significance. Use citations and original summaries rather than copying source figures or text. Following SCI 201's process does not imply University or instructor endorsement.

## 6. Outstanding decisions and review checklist

- [ ] Kaleb completes P1-003 with actual metadata, category/identifier mapping, coverage, and source licences.
- [ ] Estella checks the selected fields and proposed outputs for privacy and re-identification risks.
- [ ] Both document the basis for ethics-review applicability; resolve uncertainty through the institutional determination route where needed.
- [ ] Both agree on the geographic cohort, missing-data handling, duplicate rule, and whether optional linked data are justified.
- [ ] Both record a raw-data access and retention arrangement; verify attribution before any dataset release.
- [ ] Kaleb reviews this assessment against the finalized design and analysis plan.

Record each resolution with the decision, evidence/link, date, and reviewer. These outstanding checks allow planning to proceed; they must be resolved for the relevant data use or publication activity rather than replaced by a blanket “public data” assumption.
