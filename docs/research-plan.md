# P1-003: Short Research Plan

**Owner:** Estella · **Reviewer:** Kaleb  
**Status:** Draft — forecast comparison details await P1-004.

## 1. Plan and prepare

**Title:** Can We Forecast Edmonton's Worst Pothole Weeks?

**Question:** Can recent weather conditions improve forecasts of Edmonton's
weekly pothole-related 311 reports compared with historical seasonal patterns?

**Objective:** Test whether adding recent temperature, freeze–thaw conditions,
and precipitation improves forecast accuracy. The [background notes](background-notes.md)
explain why these variables are worth testing; they do not establish that
weather will improve our forecasts.

## 2. Collect and prepare data

- **Study period:** 2023–2025, as recommended in the merged [data check](data-check.md).
- **Sources:** [Edmonton 311 requests](https://data.edmonton.ca/d/q7ua-agfg)
  and [ECCC historical weather](https://climate.weather.gc.ca/), using
  EDMONTON INTL A (station 50149).
- **Outcome:** Count distinct `row_id` values for eligible road/alley pothole
  requests by `date_created`, using full Monday–Sunday weeks. Follow the
  exact category filter in the data check; exclude information-only inquiries.
  Keep requests with missing neighbourhood names because totals are citywide.
- **Weather:** Summarize temperature, freeze–thaw conditions, and precipitation
  for the previous week. Retain quality flags and do not treat missing values
  as zero. Exclude a forecast pair if its previous-week weather is incomplete;
  this excludes the August 19–25, 2024 forecast pair. Drop partial boundary weeks.
- Save source links, download dates, and cleaning steps so the analysis can be repeated.

## 3. Analyze and interpret

Compare a seasonal baseline with a forecast that also uses previous-week
weather. Use only information available before the forecast week.

Train on earlier weeks and compare both approaches on the same eligible later
weeks, using mean absolute error (the average size of forecast errors).
Build the baseline from training data only. Report whether weather improves
accuracy, even if the answer is no.

**Pending P1-004:** Kaleb's proposed baseline, model, temperature summaries,
freeze–thaw definition, and chronological training/test dates. Review these
together before modelling; this draft does not finalize them.

## 4. Write and share

Produce one short LaTeX report exported as PDF, including the question,
method, forecast comparison, key figures, and limitations. A website post,
poster, or dashboard is optional.

## Limitations, credit, and privacy

- Requests measure reporting activity, including repeat complaints, rather
  than unique physical potholes. Category wording and reporting behaviour may change.
- Three years provide limited seasonal history. Airport weather may differ
  from conditions inside Edmonton. Predictive accuracy does not establish causation.
- Analyze and publish citywide weekly totals; do not try to identify callers
  or link requests to individuals. No new participant data will be collected.
- Credit the City of Edmonton, ECCC, and cited papers. Before publishing data
  or figures, confirm and record the applicable source reuse and attribution
  terms: [City terms](https://data.edmonton.ca/stories/s/msh8-if28)
  and [ECCC terms](https://weather.gc.ca/mainmenu/disclaimer_e.html).

## 5. Project review

Estella and Kaleb review the method, findings, and limitations, finalize the
report, and record a few improvements for the next project. The first four
phases follow the SCI 201 structure described in the README; this final
review is an additional club step.
