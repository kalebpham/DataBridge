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

## Pilot Project 01: Where Will Edmonton's Next Pothole Reports Be?

**Research area:** Spatial data analysis and urban infrastructure  
**Status:** Planning; geographic data coverage must be verified  
**Estimated duration:** 5–6 weeks from project kickoff

We plan to predict which Edmonton neighbourhoods will receive the most pothole reports in the following week. The intended output is a neighbourhood-level forecast map and ranking that can be evaluated against future reports. This could support discussion of where further inspection may be useful; it is not a validated inspection or maintenance tool.

**The outcome is reported pothole service requests, not confirmed physical potholes.** According to the [City's 311 data documentation](https://www.edmonton.ca/programs_services/311-open-data), published coordinates represent general neighbourhood or ward centres rather than exact request locations. The pilot will therefore use neighbourhoods, subject to verifying the selected dataset, rather than claim to predict individual potholes or road segments.

### Research questions and hypotheses

Our primary question is: **Which Edmonton neighbourhoods will receive the most pothole reports next week, and can we predict them more accurately than a historical hotspot baseline?**

We will also investigate:

1. Do recent neighbourhood reporting patterns improve predictions beyond historical seasonal patterns?
2. Do forecast hotspots remain consistent across seasons, or move between neighbourhoods?
3. Does adding past weather improve predictions beyond neighbourhood history and seasonality?
4. Where does the model perform poorly, and how might reporting differences explain those errors?

**Primary hypothesis:** A model incorporating recent neighbourhood report counts and seasonality will rank next week's highest-reporting neighbourhoods more accurately than a baseline using each neighbourhood's historical seasonal average.

**Null hypothesis:** The proposed model provides no improvement over that baseline on future held-out weeks.

**Secondary hypothesis:** Past weather provides additional predictive value beyond neighbourhood history and seasonality. Citywide weather alone does not distinguish locations; its added value must be tested rather than assumed.

These are hypotheses to test, not established findings. The proposal will specify the primary metric, number of hotspot neighbourhoods to select, and comparison procedure before model evaluation.

### Objectives

- Establish whether historical 311 data supports a reliable neighbourhood-level forecasting study.
- Build a documented dataset of report counts by neighbourhood and week.
- Compare future hotspot predictions with a simple, reproducible historical baseline.
- Create maps and communicate forecast errors, uncertainty, and reporting biases.
- Establish a research workflow that future DataBridge teams can reuse.

### Planned data sources

| Source | Intended use |
| --- | --- |
| [City of Edmonton — 311 Open Data](https://www.edmonton.ca/programs_services/311-open-data) | Verify pothole categories, dates, neighbourhood identifiers, geographic precision, and historical coverage; construct neighbourhood-week report counts. |
| [City of Edmonton — Open Data Catalogue](https://data.edmonton.ca/) | Identify suitable official neighbourhood boundaries for mapping; verify identifiers and boundary versions before joining. |
| [Environment and Climate Change Canada — Historical Climate Data](https://climate.weather.gc.ca/) | Assess past temperature and precipitation as optional predictors. |
| [City of Edmonton — Daily Weather Data](https://data.edmonton.ca/Environmental-Services/Weather-Data-Daily-Environment-Canada/s4ws-tdws) | Assess as an alternative source of historical weather observations. |

Exact fields, study dates, boundaries, and weather stations have not yet been selected. The team will verify schemas, licences, access methods, geographic resolution, and coverage before implementing collection. If neighbourhood data are too incomplete or weekly counts too sparse, revise the question or aggregation period in the proposal and document the change before evaluating models.

### Study design and planned analyses

**Design and study units.** Conduct an observational study using secondary data. Each study unit is one neighbourhood in one Monday–Sunday week; the response is its pothole-report count. Define eligible neighbourhoods, study dates, exclusions, variables, forecast timing, and intended scope of inference in the proposal. Reports are not a random sample of road defects.

**Data collection and quality.** Pilot the collection process on a small sample before full extraction. Check category definitions, date handling, neighbourhood identifiers, missing locations, duplicates, boundary changes, and coverage across time. Maintain a data dictionary and cleaning log. A neighbourhood-week with no records can be assigned zero only when source coverage supports that interpretation; incomplete coverage must remain distinguishable from zero reports. Do not interpret general centre-point coordinates as exact incident locations.

**Features and exploratory analysis.** Examine neighbourhood maps, seasonal patterns, recent reporting trends, sparsity, and missingness. Candidate features include lagged report counts, past rolling averages, neighbourhood effects, and seasonality. Optional weather features include lagged precipitation, mean temperature, and freeze–thaw days (daily minimum below 0°C and maximum above 0°C). Air temperature is only a proxy for pavement conditions. Road or traffic characteristics may be explored later if suitable data are verified.

**Models and comparison.** Begin with a baseline using each neighbourhood's historical seasonal average, estimated from training data. Assess Poisson regression for neighbourhood-week counts and negative binomial regression if overdispersion warrants it, incorporating neighbourhood effects and time-varying predictors as supported by the design. Rank neighbourhoods by predicted counts. Choose methods based on data quality, study design, and diagnostics; document why each is appropriate.

**Evaluation and interpretation.** Use chronological training, validation, and test periods, keeping all neighbourhoods for a given week in the same period. Forecast the following week using only information available at forecast time. Fit transformations and tune models on training/validation periods; reserve the final test period for evaluation. Use rolling or expanding-window evaluation if coverage permits.

For the location question, a planned primary metric is **precision among the top k neighbourhoods**: the proportion of predicted top-k neighbourhoods that also appear in the observed top k. Specify k and rules for tied counts during planning. Also report the share of future reports captured by selected neighbourhoods, neighbourhood-week MAE/RMSE, and performance across neighbourhoods. Compare every model with the baseline. Quantify uncertainty using a method that respects repeated observations and temporal dependence; avoid treating neighbourhood-weeks as independent replicates.

Separate predictive performance from statistical inference. Where hypothesis tests or confidence intervals are used, justify assumptions, consider Type I/II errors and power, and interpret effect sizes and uncertainty. Associations in these observational records cannot establish causes of potholes.

## Research process: following SCI 201

DataBridge will organize research around the **four phases described in the University of Alberta's SCI 201 — Scientific Process, Fall 2026 syllabus** (course description, p. 1; topic outline, p. 5). The steps below adapt that framework to this club project. They do not imply course affiliation or instructor endorsement.

| SCI 201 phase | How we will apply it | Review output |
| --- | --- | --- |
| **1. Planning and Preparation** | Critically review and cite literature; define the problem, questions, and testable hypotheses; address ethics; specify study units, variables, spatial/temporal scope, sampling or inclusion rules, observational design, and limits of inference. Plan analysis, resources, responsibilities, and timing before collecting data. | Written research proposal, source references, analysis plan, and short proposal presentation. |
| **2. Data Collection** | Pilot the design and collection procedure; assess accuracy, precision, reliability, validity, adequacy, and sources of error. Verify secondary datasets, document missingness and exclusions, and preserve reproducible processing steps. | Reviewed data dictionary, quality checks, collection/cleaning log, and documented analysis dataset. |
| **3. Data Analysis and Interpretation** | Use descriptive summaries and methods suited to the study design. Evaluate assumptions, forecasts, and baselines; justify any hypothesis tests and confidence intervals; consider uncertainty, error, and alternative explanations before drawing conclusions. | Reproducible analysis, diagnostics, figures/tables, evaluation results, and an interpretation of limitations. |
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

## Proposed repository structure

This layout is a plan for the pilot project. The files and folders below have not yet been implemented; this repository currently provides the project README.

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
- Processed neighbourhood-week dataset, subject to source licences and privacy considerations.
- Exploratory notebooks, figures, and regression modelling scripts.
- Model diagnostics, chronological hotspot forecast evaluation, and baseline comparisons.
- Final research report, oral presentation, research poster, and public-facing project summary.
- Neighbourhood forecast maps and an optional interactive dashboard.
- Internal retrospective on research quality and team collaboration.

These outputs are planned and have not yet been completed.

## Tentative pilot timeline

| Week | Planned focus |
| --- | --- |
| **1** | SCI 201 Phase 1: literature review, ethics and study design, geographic feasibility checks, written proposal, analysis plan, and proposal presentation. |
| **2** | Phase 2: pilot collection, quality checks, neighbourhood-week aggregation, and dataset documentation. |
| **3** | Phase 3: exploratory maps, feature engineering, and historical hotspot baseline development. |
| **4** | Phase 3: count modelling, diagnostics, chronological hotspot evaluation, and interpretation of uncertainty. |
| **5** | Phase 4: research report, forecast maps, oral presentation, poster, and reproducibility review. |
| **6, if needed** | Final revisions, optional dashboard, approved publication, and retrospective. |

The schedule starts at project kickoff and may change based on data availability and team capacity.

## Research limitations

- Service requests reflect reporting activity and may include duplicates; they do not measure every physical pothole.
- Residents' reporting behaviour, access to reporting channels, and neighbourhood differences in road extent or traffic can affect observed counts. Report volume is not a direct measure of road condition or risk per kilometre.
- Weather-station observations may differ from road-surface conditions across Edmonton.
- Weather effects may occur over several days or weeks, complicating lag selection.
- Published centre-point coordinates limit spatial resolution. Missing location fields, boundary changes, and sparse counts may further constrain neighbourhood comparisons.
- Seasonality, temporal autocorrelation, and spatial dependence can affect statistical inference and forecast evaluation.
- Observational associations do not establish causality.
- Incomplete historical coverage may constrain sample size and predictive accuracy.

Findings and performance claims will only be published after real data have been analyzed, evaluated, and reviewed. Project completion requires validated, clearly communicated research as well as reproducible code.
