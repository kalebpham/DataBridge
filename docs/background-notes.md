# P1-001: Background Research

**Owner:** Estella  
**Status:** Draft — ready for team review

## Research question

Can recent weather conditions improve forecasts of Edmonton’s weekly
pothole-related 311 reports compared with historical seasonal patterns?

## 1. Weather and potholes

**Source:** Sadeghi et al. (2016).
*Algorithm and Software for Proactive Pothole Repair.*

[Read the full report](https://rosap.ntl.bts.gov/view/dot/31565/dot_31565_DS1.pdf)

### Main findings

- The study examined relationships between weather, traffic, and
  pothole patching in Indiana.
- Temperature and freeze–thaw conditions were relevant, but the
  relationships differed across road types.
- The study used repair records as a measure of pothole activity.
  These are different from residents’ 311 reports.

**Limitation — repair data resolution:** For the road-segment prediction
analysis, repair records covered roughly 10-mile sections. This was too
coarse to confirm or reject the finer-scale predictions. These findings
should therefore be treated as preliminary, rather than validated forecasts
of individual potholes. See [Section 3.4.4 and the Executive Summary](https://rosap.ntl.bts.gov/view/dot/31565/dot_31565_DS1.pdf#page=24).

**What this means for our project:** Temperature and freeze–thaw
cycles are reasonable variables to test. This study does not prove
that they will improve Edmonton’s weekly forecasts.

**Sections reviewed:** Weather data and modelling methods,
results, and limitations.

## 2. Forecasting 311 requests

**Source:** Xu et al. (2017).
*Predicting demand for 311 non-emergency municipal services:
An adaptive space-time kernel approach.*

[Paper and publication details](https://doi.org/10.1016/j.apgeog.2017.10.012)

### Main findings

- The study predicted daily sanitation requests in Chicago using
  historical request patterns.
- Its proposed model generally performed better than the comparison
  methods, including historical averaging.
- It studied daily spatial patterns, rather than Edmonton’s weekly
  pothole-report totals.

**What this means for our project:** Historical reporting patterns
provide a useful starting point. We still need to test whether
adding weather improves forecasts compared with a seasonal baseline.

**Sections reviewed:** Data, methods, results, and limitations
(Sections 2–4).

## Our project’s approach

Compare two forecasts:

1. **Baseline:** Use historical seasonal patterns in pothole reports.
2. **Weather model:** Add recent temperature, freeze–thaw cycles,
   and precipitation.

Use only information available before the forecast week. Test both
models on later weeks that were not used to train them.

Our outcome is the number of pothole-related 311 reports, not the
number of physical potholes. We must check which request categories
to include before counting reports.

## Review

- [ ] Estella checks the notes against the linked papers.
- [ ] Kaleb reviews whether the findings support our research plan.

These notes were drafted with AI assistance. Team review is pending.
