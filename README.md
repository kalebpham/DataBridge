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

## Pilot Project 01: Can We Forecast Edmonton's Worst Pothole Weeks?

**Research area:** Environmental statistics and urban infrastructure  
**Status:** Planning  
**Estimated duration:** 5–6 weeks from project kickoff

We plan to investigate whether historical weather conditions—particularly freeze–thaw cycles and precipitation—can help forecast weeks with unusually high numbers of Edmonton pothole service requests.

**We are forecasting reported pothole service requests, not the number of physical potholes.** Reporting behaviour, duplicate requests, and gaps in data coverage can affect the observed counts.

### Research questions and hypotheses

Our primary question is: **Can historical weather conditions help predict the number of pothole reports submitted in Edmonton during a given week?**

We will also investigate:

1. Are freeze–thaw cycles associated with increased reports in subsequent weeks?
2. Does precipitation help predict reporting activity?
3. Which weather variables are most useful for forecasting high-reporting weeks?
4. Do weather-based models outperform a simple seasonal baseline?

**Primary hypothesis:** Greater freeze–thaw activity is associated with more pothole reports in subsequent weeks.

**Secondary hypothesis:** Adding weather variables improves forecasting accuracy compared with a model based on historical seasonality alone.

These are hypotheses to test, not established findings.

### Objectives

- Develop a documented, reproducible dataset combining weekly pothole reports and weather observations.
- Explore seasonal patterns and possible lagged relationships between weather and reporting activity.
- Evaluate one-week-ahead forecasts against a seasonal baseline.
- Communicate findings, uncertainty, and limitations in a research report.
- Establish a research workflow that future DataBridge teams can reuse.

### Planned data sources

| Source | Intended use |
| --- | --- |
| [City of Edmonton — 311 Open Data](https://www.edmonton.ca/programs_services/311-open-data) | Identify pothole-related service requests and aggregate them into weekly counts. |
| [Environment and Climate Change Canada — Historical Climate Data](https://climate.weather.gc.ca/) | Obtain historical daily temperature and precipitation observations from a suitable Edmonton station. |
| [City of Edmonton — Daily Weather Data](https://data.edmonton.ca/Environmental-Services/Weather-Data-Daily-Environment-Canada/s4ws-tdws) | Assess as an alternative source of historical weather observations. |

Before collecting data, the team will verify dataset schemas, historical coverage, station suitability, access methods, and applicable licences. Exact fields and study dates have not yet been selected.

### Methodology and planned analyses

**Data preparation.** Check request categories, timestamps, duplicate records, missing values, and historical coverage. Aggregate requests into Monday–Sunday weeks, align weather observations to the same weeks, and document all transformations. Missing records will not automatically be treated as zero reports.

**Feature engineering.** Use daily minimum and maximum temperatures to identify freeze–thaw days, defined as days with a minimum below 0°C and a maximum above 0°C. This is an air-temperature proxy, not a direct measurement of pavement freezing. Planned predictors include weekly freeze–thaw counts, mean temperature, precipitation totals, lagged weather variables, seasonal controls, and previous-week report counts where available.

**Exploratory analysis.** Examine weekly time series, monthly and seasonal summaries, weather–report relationships, missingness, and outliers.

**Statistical modelling.** Start with Poisson regression for weekly report counts and assess negative binomial regression if the data are substantially overdispersed. Evaluate model assumptions, residual patterns, effect sizes, confidence intervals, and temporal dependence.

**Forecasting and evaluation.** Forecast one week ahead using only information available when each forecast would have been issued. Use chronological training, validation, and test periods; consider rolling or expanding-window validation if coverage permits. Compare models with a simple seasonal baseline using mean absolute error (MAE), root mean squared error (RMSE), and prediction interval coverage where applicable.

A proposed **high-reporting week** is one above the 75th percentile of training-period weekly counts. Thresholds, preprocessing decisions, and model parameters will be fitted using training data only to prevent data leakage.

## Our five-stage workflow

| Stage | Main activities |
| --- | --- |
| **1. Research Planning** | Review background literature, define questions and hypotheses, identify data sources and methods, and agree on scope and timelines. |
| **2. Data Collection & Preparation** | Obtain, clean, validate, and integrate data; document sources and build reproducible processing scripts. |
| **3. Data Analysis & Modelling** | Explore patterns, fit appropriate statistical models, evaluate assumptions and forecasts, and interpret uncertainty. |
| **4. Research Reporting & Visualization** | Prepare figures, tables, and a research report; present findings and publish approved outputs. |
| **5. Project Review & Completion** | Review methodology and reproducibility, finalize deliverables, and record lessons for future teams. |

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

- Research proposal and brief literature review.
- Data dictionary, source documentation, and reproducible collection and cleaning scripts.
- Processed weekly dataset, subject to source licences and privacy considerations.
- Exploratory notebooks, figures, and regression modelling scripts.
- Model diagnostics, forecast evaluation, and baseline comparisons.
- Final research report and public-facing project summary.
- Optional interactive dashboard.
- Internal retrospective on research quality and team collaboration.

These outputs are planned and have not yet been completed.

## Tentative pilot timeline

| Week | Planned focus |
| --- | --- |
| **1** | Research planning, literature review, source verification, and task assignments. |
| **2** | Data collection, cleaning, weekly aggregation, and dataset documentation. |
| **3** | Feature engineering, exploratory analysis, and baseline development. |
| **4** | Regression modelling, diagnostics, and chronological forecast evaluation. |
| **5** | Research reporting, visualizations, and reproducibility review. |
| **6, if needed** | Final revisions, optional dashboard, approved publication, and retrospective. |

The schedule starts at project kickoff and may change based on data availability and team capacity.

## Research limitations

- Service requests reflect reporting activity and may include duplicates; they do not measure every physical pothole.
- Residents' reporting behaviour can affect observed trends.
- Weather-station observations may differ from road-surface conditions across Edmonton.
- Weather effects may occur over several days or weeks, complicating lag selection.
- Seasonality and autocorrelation can affect statistical inference and forecast evaluation.
- Observational associations do not establish causality.
- Incomplete historical coverage may constrain sample size and predictive accuracy.

Findings and performance claims will only be published after real data have been analyzed, evaluated, and reviewed. Project completion requires validated, clearly communicated research as well as reproducible code.
