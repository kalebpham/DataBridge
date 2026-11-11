# DataBridge

**Bridging classroom learning and practical experience through student-led data projects.**

DataBridge is a proposed interdisciplinary student organization at the **University of Alberta**. We bring together students interested in statistics, data science, data engineering, and programming to investigate real-world questions and build useful tools.

Our goal is to give students experience with the full project lifecycle: defining a problem, working with data, evaluating results, and communicating findings clearly.

> **Current status:** DataBridge is in development and has not yet received official student group recognition. Our first pilot project is in the planning stage. No datasets have been collected or analyzed, and no research findings or model performance results are available.

## What we do

DataBridge has two planned project streams:

| Stream | Focus | Potential outputs |
| --- | --- | --- |
| **Independent Research** | Student teams develop research questions, gather data, and conduct statistical investigations. | Research reports, visualizations, statistical models, and dashboards. |
| **External Partner Projects** | Teams collaborate with nonprofits, researchers, university departments, and community organizations on practical data problems. | Analytical tools, automated data pipelines, predictive models, and interactive dashboards. |

Our first pilot belongs to **Independent Research**. External partnerships are a planned stream; no partnerships are announced here.

## Pilot Project 01: Mapping Edmonton's Pothole Reporting Hotspots

**Research area:** Spatial data analysis and urban infrastructure  
**Status:** Planning; geographic data coverage must be verified  
**Estimated duration:** 5–6 weeks from project kickoff

We plan to investigate which Edmonton neighbourhoods tend to have the most pothole reports and whether these spatial patterns persist across seasons and years. The intended outputs are neighbourhood hotspot maps, comparisons of reporting levels, and an analysis of associated factors over a defined historical study period.

**The outcome is reported pothole service requests, not confirmed physical potholes.** According to the [City's 311 data documentation](https://www.edmonton.ca/programs_services/311-open-data), published coordinates represent general neighbourhood or ward centres rather than exact request locations. The pilot will therefore use neighbourhoods, subject to verifying the selected dataset, rather than claim to predict individual potholes or road segments.

### Research questions and hypotheses

Our primary question is: **Which Edmonton neighbourhoods consistently have the most pothole reports, and what factors are associated with these patterns?**

We will also investigate:

1. Are high-reporting neighbourhoods consistent across seasons and years?
2. How do neighbourhood reporting levels differ after accounting for seasonality and available data coverage?
3. If suitable data are available, are road-network or traffic characteristics associated with reporting levels?
4. How might differences in reporting behaviour affect the patterns we observe?

**Primary hypothesis:** Neighbourhood differences in pothole-reporting levels persist after accounting for seasonality and data coverage.

**Null hypothesis:** After accounting for seasonality and data coverage, there are no systematic neighbourhood differences in reporting levels.

**Secondary hypothesis:** If suitable road-network data are available, neighbourhoods with more road length have higher report counts. This association would not by itself imply worse road conditions.

These are hypotheses to test, not established findings. The proposal will define the study period, comparison measures, hotspot criteria, and analysis methods before testing. “In general” refers to patterns across the chosen study period; conclusions will be limited to the data and places studied.

### Objectives

- Establish whether historical 311 data supports reliable comparisons across neighbourhoods.
- Build a documented dataset of report counts by neighbourhood and a suitable time period.
- Identify high-reporting areas and assess whether patterns persist across seasons and years.
- Investigate associated factors and communicate uncertainty and reporting biases.
- Establish a research workflow that future DataBridge teams can reuse.

### Planned data sources

| Source | Intended use |
| --- | --- |
| [City of Edmonton — 311 Open Data](https://www.edmonton.ca/programs_services/311-open-data) | Verify pothole categories, dates, neighbourhood identifiers, geographic precision, and historical coverage; construct comparable neighbourhood-level report counts over time. |
| [City of Edmonton — Open Data Catalogue](https://data.edmonton.ca/) | Identify suitable official neighbourhood boundaries for mapping; verify identifiers and boundary versions before joining. |
| [Environment and Climate Change Canada — Historical Climate Data](https://climate.weather.gc.ca/) | Assess temperature and precipitation as optional variables for seasonal and temporal context. |
| [City of Edmonton — Daily Weather Data](https://data.edmonton.ca/Environmental-Services/Weather-Data-Daily-Environment-Canada/s4ws-tdws) | Assess as an alternative source of historical weather observations. |

Exact fields, study dates, boundaries, and weather stations have not yet been selected. The team will verify schemas, licences, access methods, geographic resolution, and coverage before implementing collection. Choose an aggregation period, such as month or season, based on coverage and sparsity. Document the choice and any design revisions in the proposal before testing hypotheses.

### Study design and planned analyses

**Design and study units.** Conduct an observational study using secondary data. Each study unit is one neighbourhood during a defined month or season; the response is its pothole-report count. Select the time unit and study dates during planning, based on data adequacy. Define eligible neighbourhoods, exclusions, variables, and intended scope of inference in the proposal. Reports are not a random sample of road defects.

**Data collection and quality.** Pilot collection on a small sample before full extraction. Check category definitions, date handling, neighbourhood identifiers, missing locations, duplicates, boundary changes, and coverage across time. Maintain a data dictionary and cleaning log. Assign zero to a neighbourhood-period with no records only when source coverage supports that interpretation. Do not interpret general centre-point coordinates as exact incident locations.

**Spatial and temporal exploration.** Map neighbourhood counts over comparable periods, summarize seasonality, and examine whether high-reporting areas persist across years. Define hotspot criteria and rules for tied counts in the analysis plan. Report raw volumes separately from exposure-adjusted rates: reports per road kilometre may be explored only if suitable road-length data are verified. Neither measure directly estimates physical pothole prevalence.

**Associated factors and models.** Assess Poisson regression for neighbourhood-period counts and negative binomial regression if overdispersion warrants it. Include neighbourhood effects, seasonality, and year as supported by the design. If verified, assess road length or traffic characteristics in an appropriately specified model; distinguish their associations from neighbourhood effects. Weather may provide temporal context, but citywide weather alone cannot explain spatial differences. Choose methods based on data quality, study design, and diagnostics, and document the reasoning.

**Evaluation and interpretation.** Examine model assumptions, overdispersion, residuals, and spatial and temporal dependence. Report effect sizes and confidence intervals using methods appropriate for repeated observations; justify any hypothesis tests and consider Type I/II errors, power, and multiple comparisons. Assess whether neighbourhood rankings and conclusions are stable across seasons, years, and reasonable aggregation choices. Label analyses developed after seeing the data as exploratory.

Prediction is an optional extension: if pursued, define its target and time horizon separately, compare it with a historical baseline, and evaluate on held-out periods using only information available at prediction time. The core study concerns general spatial patterns rather than a next-week forecast. Observational associations cannot establish causes of potholes, and reporting hotspots must not be presented as confirmed road-damage hotspots.

## Research process: following SCI 201

DataBridge will organize research around the **four phases described in the University of Alberta's SCI 201 — Scientific Process, Fall 2026 syllabus** (course description, p. 1; topic outline, p. 5). The steps below adapt that framework to this club project. They do not imply course affiliation or instructor endorsement.

| SCI 201 phase | How we will apply it | Review output |
| --- | --- | --- |
| **1. Planning and Preparation** | Critically review and cite literature; define the problem, questions, and testable hypotheses; address ethics; specify study units, variables, spatial/temporal scope, sampling or inclusion rules, observational design, and limits of inference. Plan analysis, resources, responsibilities, and timing before collecting data. | Written research proposal, source references, analysis plan, and short proposal presentation. |
| **2. Data Collection** | Pilot the design and collection procedure; assess accuracy, precision, reliability, validity, adequacy, and sources of error. Verify secondary datasets, document missingness and exclusions, and preserve reproducible processing steps. | Reviewed data dictionary, quality checks, collection/cleaning log, and documented analysis dataset. |
| **3. Data Analysis and Interpretation** | Use descriptive summaries and methods suited to the study design. Evaluate assumptions, spatial patterns, and model fit; justify any hypothesis tests and confidence intervals; consider uncertainty, error, and alternative explanations before drawing conclusions. | Reproducible analysis, diagnostics, figures/tables, evaluation results, and an interpretation of limitations. |
| **4. Scientific Writing and Presentation** | Prepare a report covering abstract, introduction, methods, results, discussion, conclusions, recommendations, and references. Communicate evidence through an oral presentation and research poster, with clear figures, citations, and appropriate scientific language. | Reviewed research report, presentation, poster, and approved public summary. |

The process is iterative: a failed quality check or unsupported assumption may require revisiting the design, with revisions documented. Following these four phases, DataBridge will conduct an additional **project review and retrospective** to check reproducibility, finalize deliverables, and improve team practices. This is a club management step, separate from SCI 201's four research phases.

## Team and responsibilities

**Co-Presidents:** Estella Li and Kaleb Pham. The Co-Presidents oversee the organization, Project Coordinators, and project teams. The planned executive structure also includes VP Finance, VP Marketing, and VP Events.

Each project is led by a **Project Coordinator**, who manages timelines, assigns responsibilities, monitors progress, and maintains project standards.

| Research role | Responsibilities |
| --- | --- |
| **Data Collection Specialist** | Identify data sources and collection methods; obtain, clean, validate, and integrate data; maintain data documentation. |
| **Research Analyst** | Conduct exploratory analysis, statistical testing, and modelling; create visualizations and interpret findings. |
| **Reporting Specialist** | Document the research process; prepare reports and presentations; communicate findings and limitations; prepare approved outputs for publication. |

All three research roles contribute to planning before data collection begins.

## Phase 1 planning documents

These drafts are prepared for team review, with unresolved data and design decisions recorded explicitly:

- [Literature review](docs/literature-review.md) — P1-002.
- [Proposed study design](docs/methodology.md) — P1-004.
- [Ethics and limitations](docs/ethics-and-limitations.md) — P1-006.
- [Working research proposal](docs/research-proposal.md) — P1-007; technical sections and joint approval pending.
- [Proposal presentation brief and speaking notes](docs/proposal-speaking-notes.md) — Estella’s draft and shared preparation checklist.

## Proposed repository structure

This layout is a plan for the pilot project. The repository currently contains this README and the Phase 1 planning drafts linked below; collection scripts, datasets, and analysis outputs have not yet been implemented.

```text
DataBridge/
├── README.md
├── LICENSE                       # To be selected by the team
├── .gitignore
├── requirements.txt              # To be added with Python implementation
├── docs/
│   ├── research-proposal.md
│   ├── literature-review.md
│   ├── methodology.md
│   ├── ethics-and-limitations.md
│   └── data-dictionary.md
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   └── exploratory-analysis.ipynb
├── src/
│   ├── collect_data.py
│   ├── clean_data.py
│   ├── build_features.py
│   ├── analyze.py
│   ├── train_model.py
│   └── evaluate_model.py
├── reports/
│   ├── final-report.qmd
│   └── figures/
├── tests/
└── outputs/
```

## Getting started and collaboration

There is no executable research code or dependency setup yet. No installation is required to read this README. Setup and execution instructions will be added when the implementation is available.

To work with a local copy, install Git and run:

```bash
git clone https://github.com/kalebpham/DataBridge.git
cd DataBridge
```

GitHub will be the main technical workspace for version control, documentation, and issue tracking. Planned tools include **Python or R**, **Jupyter Notebook or RStudio**, and **Quarto** for reproducible reports. Notion and Google Drive are planned for coordination and shared documents; Power BI or Streamlit may be used for an optional dashboard. Final tooling will be chosen during planning.

For proposed contributions, [open an issue](https://github.com/kalebpham/DataBridge/issues) to discuss a research idea, data source, documentation improvement, or task. Describe the proposed change and its purpose, then submit work through a pull request for review.

Data sources and transformations should be documented. Raw data should only be committed when redistribution is permitted and the records contain no confidential or personal information. Prefer reproducible downloads from official sources where possible.

## Expected deliverables

- Research proposal, analysis plan, brief literature review with references, and proposal presentation.
- Data dictionary, source documentation, and reproducible collection and cleaning scripts.
- Processed neighbourhood-period dataset, subject to source licences and privacy considerations.
- Exploratory notebooks, figures, and regression modelling scripts.
- Model diagnostics, neighbourhood comparisons, and assessment of hotspot stability across seasons and years.
- Final research report, oral presentation, research poster, and public-facing project summary.
- Neighbourhood hotspot maps and an optional interactive dashboard.
- Internal retrospective on research quality and team collaboration.

These outputs are planned and have not yet been completed.

## Tentative pilot timeline

| Week | Planned focus |
| --- | --- |
| **1** | SCI 201 Phase 1: literature review, ethics and study design, geographic feasibility checks, written proposal, analysis plan, and proposal presentation. |
| **2** | Phase 2: pilot collection, quality checks, neighbourhood-period aggregation, and dataset documentation. |
| **3** | Phase 3: exploratory maps, seasonal summaries, and neighbourhood comparisons. |
| **4** | Phase 3: count modelling, diagnostics, assessment of hotspot persistence, and interpretation of uncertainty. |
| **5** | Phase 4: research report, hotspot maps, oral presentation, poster, and reproducibility review. |
| **6, if needed** | Final revisions, optional dashboard, approved publication, and retrospective. |

The schedule starts at project kickoff and may change based on data availability and team capacity.

## Research limitations

- Service requests reflect reporting activity and may include duplicates; they do not measure every physical pothole.
- Residents' reporting behaviour, access to reporting channels, and neighbourhood differences in road extent or traffic can affect observed counts. Report volume is not a direct measure of road condition or risk per kilometre.
- Weather-station observations may differ from road-surface conditions across Edmonton.
- Weather effects may occur over several days or weeks, complicating lag selection.
- Published centre-point coordinates limit spatial resolution. Missing location fields, boundary changes, and sparse counts may further constrain neighbourhood comparisons.
- Seasonality, temporal autocorrelation, and spatial dependence can affect neighbourhood comparisons and statistical inference.
- Observational associations do not establish causality.
- Incomplete historical coverage may constrain sample size and the generalizability of conclusions.

Findings and performance claims will only be published after real data have been analyzed, evaluated, and reviewed. Project completion requires validated, clearly communicated research as well as reproducible code.
