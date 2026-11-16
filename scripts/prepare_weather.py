#!/usr/bin/env python3
"""Prepare P2-002 weekly ECCC weather. Python 3.9+; standard library only."""

import argparse
import csv
import hashlib
import io
import json
import math
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen


START, END = date(2023, 1, 1), date(2026, 1, 1)  # END is exclusive.
STATION, CLIMATE_ID = "EDMONTON INTL A", "3012216"
LICENCE = "https://climate.weather.gc.ca/prods_servs/attachment1_e.html"
MEASURES = {
    "min_temp": ("Min Temp (°C)", "Min Temp Flag"),
    "max_temp": ("Max Temp (°C)", "Max Temp Flag"),
    "mean_temp": ("Mean Temp (°C)", "Mean Temp Flag"),
    "precip_total": ("Total Precip (mm)", "Total Precip Flag"),
}
FIELDS = ["weather_week_start", "mean_temp", "freeze_thaw_days", "precip_total",
          "complete", "observed_days", "mean_temp_days", "freeze_thaw_valid_days",
          "precip_days", "quality_flags", "missing_dates"]


def source_url(year):
    return "https://climate.weather.gc.ca/climate_data/bulk_data_e.html?" + urlencode({
        "format": "csv", "stationID": 50149, "Year": year,
        "Month": 1, "Day": 1, "timeframe": 2})


def parse_daily(content, year):
    """Validate the source schema/station; preserve flags and missing values."""
    reader = csv.DictReader(io.StringIO(content.decode("utf-8-sig")))
    required = {"Station Name", "Climate ID", "Date/Time", "Data Quality"}
    required.update(column for pair in MEASURES.values() for column in pair)
    if not required.issubset(reader.fieldnames or []):
        raise ValueError("Unexpected ECCC CSV schema; inspect the source before proceeding.")
    days = {}
    for row in reader:
        if None in row or any(row[k] is None for k in required):
            raise ValueError("Malformed ECCC daily row.")
        if row["Station Name"] != STATION or row["Climate ID"] != CLIMATE_ID:
            raise ValueError("Unexpected station in ECCC download.")
        day = date.fromisoformat(row["Date/Time"])
        if day.year != year or not START <= day < END:
            raise ValueError("Unexpected date in ECCC download.")
        if day in days:
            raise ValueError(f"Duplicate weather date: {day}.")
        values, flags = {}, {}
        if row["Data Quality"].strip():
            flags["data_quality"] = row["Data Quality"].strip()
        for key, (column, flag_column) in MEASURES.items():
            text, flag = row[column].strip(), row[flag_column].strip()
            if flag:
                flags[key] = flag
            # M denotes missing. A blank number stays missing even without a flag.
            value = None if not text or flag == "M" else float(text)
            if value is not None and not math.isfinite(value):
                raise ValueError(f"Non-finite {key} on {day}.")
            if key == "precip_total" and value is not None and value < 0:
                raise ValueError(f"Negative precipitation on {day}.")
            values[key] = value
        low, high = values["min_temp"], values["max_temp"]
        if low is not None and high is not None and low > high:
            raise ValueError(f"Minimum exceeds maximum temperature on {day}.")
        days[day] = {"values": values, "flags": flags}
    if not days:
        raise ValueError("Empty ECCC daily download.")
    return days


def load_inputs(raw_dir, offline=False):
    """Reuse immutable local snapshots; never silently refresh historical inputs."""
    all_days, sources = {}, []
    raw_dir.mkdir(parents=True, exist_ok=True)
    for year in range(2023, 2026):
        path = raw_dir / f"daily_{year}.csv"
        meta_path = path.with_suffix(".json")
        if path.exists() != meta_path.exists():
            raise ValueError(f"Incomplete cache pair for {year}; use a new --raw-dir.")
        if path.exists():
            content = path.read_bytes()
            meta = json.loads(meta_path.read_text(encoding="utf-8"))
            if meta["url"] != source_url(year) or meta["sha256"] != hashlib.sha256(content).hexdigest():
                raise ValueError(f"Cache provenance mismatch for {year}.")
            datetime.fromisoformat(meta["downloaded_at_utc"])
            days = parse_daily(content, year)
        else:
            if offline:
                raise ValueError(f"Offline input missing: {path}.")
            request = Request(source_url(year), headers={"User-Agent": "DataBridge-research/1.0"})
            with urlopen(request, timeout=45) as response:
                content = response.read()
            days = parse_daily(content, year)  # Validate before saving the source.
            meta = {"year": year, "url": source_url(year),
                    "downloaded_at_utc": datetime.now(timezone.utc).isoformat(),
                    "sha256": hashlib.sha256(content).hexdigest()}
            path.write_bytes(content)
            meta_path.write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
        all_days.update(days)
        sources.append(meta | {"calendar_rows": len(days)})
    return all_days, sources


def summarize(days):
    """Keep every full calendar week, including incomplete weather weeks."""
    weeks = []
    week = START + timedelta(days=(-START.weekday()) % 7)
    while week + timedelta(days=6) < END:
        dates = [week + timedelta(days=i) for i in range(7)]
        means, crossings, precip = [], [], []
        flags, missing = {}, {}
        for day in dates:
            if day not in days:
                missing[day.isoformat()] = ["daily_record"]
                continue
            values = days[day]["values"]
            if days[day]["flags"]:
                flags[day.isoformat()] = days[day]["flags"]
            gaps = [key for key, value in values.items() if value is None]
            if gaps:
                missing[day.isoformat()] = gaps
            if values["mean_temp"] is not None:
                means.append(values["mean_temp"])
            if values["min_temp"] is not None and values["max_temp"] is not None:
                crossings.append(int(values["min_temp"] < 0 < values["max_temp"]))
            if values["precip_total"] is not None:
                precip.append(values["precip_total"])
        weeks.append({
            "weather_week_start": week.isoformat(),
            "mean_temp": round(math.fsum(means) / 7, 6) if len(means) == 7 else "",
            "freeze_thaw_days": sum(crossings) if len(crossings) == 7 else "",
            "precip_total": round(math.fsum(precip), 6) if len(precip) == 7 else "",
            "complete": len(means) == len(crossings) == len(precip) == 7,
            "observed_days": sum(day in days for day in dates),
            "mean_temp_days": len(means), "freeze_thaw_valid_days": len(crossings),
            "precip_days": len(precip),
            "quality_flags": json.dumps(flags, sort_keys=True, separators=(",", ":")),
            "missing_dates": json.dumps(missing, sort_keys=True, separators=(",", ":")),
        })
        week += timedelta(days=7)
    return weeks


def write_outputs(days, sources, output):
    weeks = summarize(days)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(weeks)
    audit = {"daily_rows": len(days), "expected_daily_rows": (END - START).days,
             "full_weeks": len(weeks), "complete_weeks": sum(w["complete"] for w in weeks),
             "incomplete_weeks": [w["weather_week_start"] for w in weeks if not w["complete"]],
             "partial_boundary_dates": [d.isoformat() for d in sorted(days)
                                        if d < date.fromisoformat(weeks[0]["weather_week_start"])
                                        or d > date.fromisoformat(weeks[-1]["weather_week_start"]) + timedelta(days=6)]}
    provenance = {"station_id": 50149, "station_name": STATION, "climate_id": CLIMATE_ID,
                  "sources": sources, "audit": audit,
                  "output_sha256": hashlib.sha256(output.read_bytes()).hexdigest()}
    output.with_name("weather_sources.json").write_text(
        json.dumps(provenance, indent=2) + "\n", encoding="utf-8")
    return audit


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--raw-dir", type=Path, default=Path("data/raw/weather"))
    parser.add_argument("--output", type=Path, default=Path("data/processed/weekly_weather.csv"))
    parser.add_argument("--offline", action="store_true", help="Require cached inputs; make no network requests.")
    args = parser.parse_args()
    days, sources = load_inputs(args.raw_dir, args.offline)
    print(json.dumps(write_outputs(days, sources, args.output), indent=2))


if __name__ == "__main__":
    main()
