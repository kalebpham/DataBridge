# P1-003: Short Research Plan

**Owner:** Estella · **Reviewer:** Kaleb  
**Status:** Ready for Kaleb’s review — updated to match P1-004.

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

Compare two forecasts on the same eligible weeks:

- **Seasonal baseline:** Average training-week report counts for the forecast
  month's calendar month. Assign each week to the month of its Monday.
- **Weather model:** Poisson regression with a log link, using the same month
  categories plus previous-week mean temperature, freeze–thaw-day count, and
  total precipitation. A freeze–thaw day has minimum air temperature below
  0°C and maximum above 0°C; this is an air-temperature indicator.

| Stage | Full target weeks |
| --- | --- |
| Training | January 9–December 31, 2023 |
| Validation | January 1–December 29, 2024 |
| Final test | January 6–December 28, 2025 |

Use 2024 to check the methods. Then refit both on eligible 2023–2024 weeks
and freeze the specification and fitted values before evaluating 2025.
Only use weather from before each target week. Omit the target week
December 30, 2024–January 5, 2025 because it crosses the evaluation boundary;
its weather can still supply the January 6 forecast.

Apply the same missing-data exclusions to both approaches in fitting and
scoring. Compare unrounded forecasts using **mean absolute error (MAE)**,
the average size of forecast errors. Report both MAEs, their difference,
the number of evaluated weeks, and a plot of actual counts and forecasts.
Lower MAE is better; report the result even if weather does not help.

Check model convergence, dispersion, and residuals during implementation.
Use validation results for changes before examining the final test results.
Any high-volume-week breakdown is exploratory; report its threshold and
number of weeks. Treat previous-week weather availability as a backtest
assumption because downloaded observations may include later revisions.

Full details: [P1-004 forecast comparison](https://github.com/kalebpham/DataBridge/blob/8dcfcfad306d182599668ab7529099f1c4c3cf4e/docs/forecast-comparison.md).
This summary matches its reviewed revision; PR #12 is still awaiting merge.

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
