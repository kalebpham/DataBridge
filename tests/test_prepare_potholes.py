"""Checks for outcome definitions and calendar handling; no network calls."""
import importlib.util
import unittest
from datetime import timedelta
from pathlib import Path

spec = importlib.util.spec_from_file_location("potholes", Path(__file__).parents[1] / "scripts/prepare_potholes.py")
p = importlib.util.module_from_spec(spec)
spec.loader.exec_module(p)


class PrepareTests(unittest.TestCase):
    def setUp(self):
        self.coverage = [{"day": (p.START + timedelta(days=i)).isoformat(), "n": "1"}
                         for i in range((p.END - p.START).days)]

    def row(self, identifier, day, label="Road Pothole"):
        return {"row_id": identifier, "date_created": day + "T12:00:00.000",
                "service_category": "Potholes", "service_description": label}

    def test_filter_distinct_ids_boundaries_and_zero_weeks(self):
        rows = [self.row("1", "2023-01-02"), self.row("1", "2023-01-02"),
                self.row("2", "2023-01-08", "POTHOLE:Alley Pothole"),
                self.row("3", "2023-01-03", "Info Asphalt  and  Potholes"),
                self.row("4", "2023-01-01"), self.row("5", "2025-12-31")]
        weeks, audit = p.prepare(rows, self.coverage)
        self.assertEqual(len(weeks), 156)
        self.assertEqual(weeks[0], {"week_start": "2023-01-02", "report_count": 2})
        self.assertEqual(weeks[-1]["week_start"], "2025-12-22")
        self.assertEqual(weeks[1]["report_count"], 0)
        self.assertEqual(audit["partial_boundary_week_reports"], 2)
        self.assertEqual(audit["duplicate_rows_removed"], 1)
        # Records intentionally have no neighbourhood field and remain eligible.
        self.assertEqual(audit["full_week_reports"], 2)

    def test_incomplete_source_coverage_does_not_become_zero(self):
        with self.assertRaisesRegex(ValueError, "Missing all-service coverage"):
            p.prepare([], self.coverage[1:])

    def test_unknown_label_requires_review(self):
        with self.assertRaisesRegex(ValueError, "Unreviewed pothole label"):
            p.prepare([self.row("1", "2023-01-02", "New pothole category")], self.coverage)

    def test_conflicting_id_and_missing_date_require_review(self):
        with self.assertRaisesRegex(ValueError, "Conflicting records"):
            p.prepare([self.row("1", "2023-01-02"), self.row("1", "2023-01-03")], self.coverage)
        row = self.row("2", "2023-01-02")
        del row["date_created"]
        with self.assertRaisesRegex(ValueError, "Missing request ID or creation date"):
            p.prepare([row], self.coverage)


if __name__ == "__main__":
    unittest.main()
