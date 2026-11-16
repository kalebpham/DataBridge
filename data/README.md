# Weekly weather — P2-002

From the repository root, with Python 3.9+ and no additional packages:

```sh
python scripts/prepare_weather.py
python scripts/prepare_weather.py --offline
python -m unittest discover -s tests -p "test_prepare_weather.py" -v
```

The first run downloads ECCC station **50149, EDMONTON INTL A**, climate ID
**3012216**, for [2023](https://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=50149&Year=2023&Month=1&Day=1&timeframe=2),
[2024](https://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=50149&Year=2024&Month=1&Day=1&timeframe=2),
and [2025](https://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=50149&Year=2025&Month=1&Day=1&timeframe=2).
Later runs reuse `data/raw/weather/daily_YEAR.csv` and matching JSON metadata.
Raw inputs are ignored by Git. Keep them to reproduce this exact snapshot;
`--offline` refuses to download. A fresh download may contain revisions: use a
new `--raw-dir data/raw/weather-new-snapshot` to preserve the original files.
Cache hashes are verified before processing.

Output: [`processed/weekly_weather.csv`](processed/weekly_weather.csv), **156 full
Monday–Sunday weeks**, January 2, 2023–December 28, 2025. There are **155 complete
weeks** and one incomplete week, August 12–18, 2024. The three source files
contain all **1,096 calendar dates**. Download timestamps (UTC), source URLs,
SHA-256 hashes and counts are in [`processed/weather_sources.json`](processed/weather_sources.json).
The output and provenance are identical on an offline rerun.

| Column | Meaning |
| --- | --- |
| `weather_week_start` | ISO Monday date (`YYYY-MM-DD`), matching P2-001's `week_start` format. |
| `mean_temp` | Average of seven daily mean temperatures, °C. |
| `freeze_thaw_days` | Days with daily minimum strictly below 0°C and maximum strictly above 0°C, 0–7. Air-temperature indicator, rather than observed road freeze–thaw. |
| `precip_total` | Sum of seven daily total-precipitation observations, mm. |
| `complete` | `True` only when all seven days have mean/minimum/maximum temperature and precipitation. Parse explicitly as a Boolean; the text `False` is not an eligible week. |
| `observed_days` | Number of daily source records present, 0–7. |
| `mean_temp_days`, `freeze_thaw_valid_days`, `precip_days` | Number of usable daily observations for each summary, 0–7. |
| `quality_flags` | JSON mapping dates to nonblank source flags for the four measurements and `data_quality`. `{}` means no flags; raw files retain every source column. |
| `missing_dates` | JSON mapping dates to missing measurement names, or `daily_record` for an absent row. `{}` means no gaps. |

Blank or `M`-flagged daily values stay missing; an affected weekly summary is
blank, even if some days are available. No zero imputation or partial-week
averages/totals. Numeric observations with other flags remain available and
their flags are retained for review. Trace precipitation remains the supplied
`0.0` with flag `T`; it is not missing. See ECCC's
[technical documentation](https://climate.weather.gc.ca/doc/Technical_Documentation.pdf).

The current inputs have missing minimum, maximum and mean temperatures on
**August 14 and 16, 2024**, plus missing precipitation on **August 16**.
The August 12 weather week is retained with `complete=False`; P2-003 must exclude
its **August 19–25 target week** from both models. Join target Monday to weather
Monday exactly seven days earlier. Do not interpret weather-week dates as target dates.

January 1, 2023 and December 29–31, 2025 lie in partial boundary weeks and are
omitted from this weather table. The full weather week December 30, 2024–January
5, 2025 is retained because it supplies the January 6 forecast. Target-week
eligibility and split labels belong to P2-003; this script does not fit models.
Airport observations may differ from conditions inside Edmonton. Historical
observations may be revised after the forecast date.

## Source credit and reuse

**Based on Environment and Climate Change Canada data.** DataBridge calculated
the weekly summaries independently; ECCC has not endorsed this analysis.
The [ECCC historical-data licence](https://climate.weather.gc.ca/prods_servs/attachment1_e.html)
was checked November 15, 2026. Redistribution requires source acknowledgement,
no explicit charge for the ECCC data product, and recipients' acceptance of the
same redistribution restrictions before use. By using these redistributed
summaries, you accept those linked restrictions. ECCC supplies the data without
warranties of quality, accuracy or completeness. Retain this notice and licence
link when sharing the summaries.
