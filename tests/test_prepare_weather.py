"""Check week alignment, missingness, strict crossings, and input integrity."""

import csv
import importlib.util
import io
import json
from datetime import date, timedelta
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch


spec = importlib.util.spec_from_file_location(
    "prepare_weather", Path(__file__).resolve().parents[1] / "scripts/prepare_weather.py")
weather = importlib.util.module_from_spec(spec)
spec.loader.exec_module(weather)


def source_row(day):
    row = {"Station Name": weather.STATION, "Climate ID": weather.CLIMATE_ID,
           "Date/Time": str(day), "Data Quality": ""}
    for key, (column, flag) in weather.MEASURES.items():
        row[column] = {"min_temp": "-1", "max_temp": "1", "mean_temp": "0",
                       "precip_total": "0.0"}[key]
        row[flag] = ""
    return row


def encode(rows):
    handle = io.StringIO()
    writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
    writer.writeheader()
    writer.writerows(rows)
    return ("\ufeff" + handle.getvalue()).encode("utf-8")


def week_rows(start):
    return [source_row(start + timedelta(days=i)) for i in range(7)]


def summarized(rows, start):
    days = {}
    for year in sorted({int(row["Date/Time"][:4]) for row in rows}):
        days.update(weather.parse_daily(encode([r for r in rows if r["Date/Time"].startswith(str(year))]), year))
    return next(w for w in weather.summarize(days) if w["weather_week_start"] == str(start))


class WeatherChecks(unittest.TestCase):
    def test_hand_calculated_week_and_strict_zero_crossings(self):
        start = date(2023, 1, 2)
        rows = week_rows(start)
        for i, row in enumerate(rows):
            row["Mean Temp (°C)"] = str(i - 3)
            row["Total Precip (mm)"] = str(i / 10)
        rows[0]["Min Temp (°C)"] = "0"  # Touching zero is not crossing it.
        rows[1]["Max Temp (°C)"] = "0"
        rows[2]["Total Precip Flag"] = "T"
        rows[2]["Total Precip (mm)"] = "0.0"
        result = summarized(rows, start)
        self.assertEqual((result["mean_temp"], result["freeze_thaw_days"], result["precip_total"]), (0, 5, 1.9))
        self.assertTrue(result["complete"])
        self.assertEqual(json.loads(result["quality_flags"])["2023-01-04"], {"precip_total": "T"})

    def test_august_gaps_are_not_zero_or_partial_summaries(self):
        start = date(2024, 8, 12)
        rows = week_rows(start)
        for i in (2, 4):
            for key in ("min_temp", "max_temp", "mean_temp"):
                column, flag = weather.MEASURES[key]
                rows[i][column], rows[i][flag] = "", "M"
        rows[4]["Total Precip (mm)"] = ""
        rows[4]["Total Precip Flag"] = "M"
        result = summarized(rows, start)
        self.assertFalse(result["complete"])
        self.assertEqual((result["mean_temp"], result["freeze_thaw_days"], result["precip_total"]), ("", "", ""))
        self.assertEqual((result["mean_temp_days"], result["freeze_thaw_valid_days"], result["precip_days"]), (5, 5, 6))
        self.assertEqual(set(json.loads(result["missing_dates"])), {"2024-08-14", "2024-08-16"})
        self.assertEqual(json.loads(result["quality_flags"])["2024-08-16"]["precip_total"], "M")

    def test_absent_day_and_unflagged_blank_are_missing(self):
        start = date(2023, 1, 2)
        rows = week_rows(start)
        rows[0]["Mean Temp (°C)"] = ""
        result = summarized(rows[:-1], start)
        self.assertEqual(result["observed_days"], 6)
        self.assertFalse(result["complete"])
        self.assertEqual(result["mean_temp"], "")
        self.assertEqual(json.loads(result["missing_dates"])["2023-01-08"], ["daily_record"])

    def test_full_week_dates_and_cross_year_week(self):
        start = date(2024, 12, 30)
        result = summarized(week_rows(start), start)
        self.assertTrue(result["complete"])
        weeks = weather.summarize({})
        self.assertEqual(len(weeks), 156)
        self.assertEqual(weeks[0]["weather_week_start"], "2023-01-02")
        self.assertEqual(weeks[-1]["weather_week_start"], "2025-12-22")
        self.assertEqual(len({w["weather_week_start"] for w in weeks}), 156)
        self.assertTrue(all(date.fromisoformat(w["weather_week_start"]).weekday() == 0 for w in weeks))

    def test_invalid_source_fails_before_aggregation(self):
        row = source_row(date(2023, 1, 2))
        for column, value in [("Station Name", "OTHER"), ("Climate ID", "0000000"),
                              ("Date/Time", "2024-01-02"), ("Mean Temp (°C)", "NaN"),
                              ("Total Precip (mm)", "-1"), ("Min Temp (°C)", "3")]:
            with self.subTest(column=column), self.assertRaises(ValueError):
                weather.parse_daily(encode([row | {column: value}]), 2023)
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            weather.parse_daily(encode([row, row]), 2023)
        del row["Total Precip Flag"]
        with self.assertRaisesRegex(ValueError, "schema"):
            weather.parse_daily(encode([row]), 2023)

    def test_offline_missing_input_and_tampered_cache_fail_without_network(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).parent) as folder, patch.object(weather, "urlopen") as network:
            raw = Path(folder)
            with self.assertRaisesRegex(ValueError, "Offline input missing"):
                weather.load_inputs(raw, offline=True)
            (raw / "daily_2023.csv").write_bytes(encode([source_row(date(2023, 1, 2))]))
            (raw / "daily_2023.json").write_text(json.dumps({
                "url": weather.source_url(2023), "sha256": "changed"}), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "provenance mismatch"):
                weather.load_inputs(raw, offline=True)
            network.assert_not_called()


if __name__ == "__main__":
    unittest.main()
