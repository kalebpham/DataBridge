# P1-004: Plan the forecast comparison

**Owner:** Kaleb. **Reviewer:** Estella.

**Status:** Draft for P1-004 review, November 12, 2026.

We will test whether previous-week weather improves forecasts of citywide weekly pothole-related 311 requests. Follow the accepted [data check](data-check.md) for sources, report categories and missing observations.

## Two forecasts

1. **Seasonal baseline.** Predict the average weekly report count for the forecast week's calendar month, calculated from training weeks only. Assign each Monday-Sunday week to the month of its Monday. For example, a March forecast uses the average of training weeks whose Mondays fall in March.
2. **Seasonal plus weather model.** Fit a Poisson regression with a log link for weekly counts. Include the forecast month's categorical effect and three previous-week weather variables. A month-only Poisson model gives the same fitted monthly means as the baseline, so the added predictors are the weather variables.

The three weather variables are the average daily mean temperature, the number of freeze-thaw days, and total daily precipitation summed across the previous Monday-Sunday week. Define a freeze-thaw day as daily minimum temperature below 0 C and daily maximum above 0 C. This is an air-temperature indicator of a within-day crossing. Keep reported trace precipitation values and their quality flags as described in the data check.

For the weather model, estimate the intercept, month effects and weather coefficients using training data. Keep forecasts as non-negative expected counts without rounding before scoring. Check convergence, dispersion and residual patterns during implementation. Any change of model or features should be documented using validation results before opening the final test results.

## Earlier training, later testing

| Stage | Full target weeks | Purpose |
| --- | --- | --- |
| Training | January 9-December 31, 2023 | Estimate both approaches. Earlier boundary weeks lack a complete prior weather week within our data window. |
| Validation | January 1-December 29, 2024 | Check the proposed methods and address implementation problems. |
| Final test | January 6-December 28, 2025 | Compare the frozen approaches on later weeks. |

These are inclusive date ranges, each starting Monday and ending Sunday. Omit December 30, 2024-January 5, 2025 because it crosses the validation/test boundary. Previous-week weather for the January 6, 2025 forecast can still use December 30-January 5 observations.

After validation, agree the specification and refit both approaches using eligible 2023-2024 training/validation weeks. Freeze coefficients and baseline monthly averages for the 2025 comparison. Supply each forecast with its known calendar month and observed previous-week weather. Changes prompted by 2025 results become exploratory follow-up work.

## Fair comparison and missing data

- Count distinct qualifying request IDs in full Monday-Sunday target weeks. Keep the same report filter and the same eligible forecast pairs for both methods in fitting and evaluation.
- Use weather dated before the target week. For example, August 12-18 weather supplies the August 19-25 forecast. The missing August 2024 weather excludes that following forecast pair from both approaches. Record every exclusion and the number of evaluated weeks.
- Exclude pairs with incomplete previous-week temperature or precipitation. Preserve the missing-data flags. Include weeks with zero qualifying reports when source coverage supports that interpretation.
- Historical weather downloads can include later revisions. Availability of the previous week's observations at forecast issuance remains a backtest assumption to document.

## Accuracy and interpretation

Use **mean absolute error (MAE)**, the average of `abs(actual reports - predicted reports)` over exactly the same final-test weeks. If actual reports are 50 and a forecast is 42, its absolute error is 8 reports. Lower MAE indicates better forecast accuracy.

Report both MAEs, the number of evaluated weeks, and `baseline MAE - weather-model MAE`. A positive difference favours the weather model. Report percentage improvement only when baseline MAE is greater than zero. Plot actual counts and both forecasts over the test weeks and show how their absolute errors vary by season and high-volume weeks.

Interpret the result for this held-out year and this baseline. Three years provide limited seasonal history, and reporting volumes can shift. Adding weather may help or may reduce accuracy. Keep the full test-period comparison and its limitations visible in the research report.

The chronological evaluation and MAE follow the forecasting guidance below. Poisson regression is the proposed count model for team review.

- [Forecasting: Principles and Practice, evaluating forecast accuracy](https://otexts.com/fpp3/toolbox.html#evaluating-point-forecast-accuracy)
- [Statsmodels generalized linear models](https://www.statsmodels.org/stable/glm.html)

## Review

- [ ] Estella reviews the monthly baseline, weather model and freeze-thaw definition.
- [ ] Both agree on the chronological split, paired exclusions and MAE comparison before modelling.
