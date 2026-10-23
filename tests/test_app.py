import io
import runpy
import unittest
from unittest.mock import patch

import app


class IncidentTests(unittest.TestCase):
    def setUp(self):
        storage_patch = patch.object(app, "INCIDENTS", [])
        storage_patch.start()
        self.addCleanup(storage_patch.stop)

    def test_incident_defaults_to_open(self):
        incident = app.Incident(1, "Report", "low")

        self.assertEqual(incident.status, "open")

    def test_classify_incident_matches_all_keywords_case_insensitively(self):
        cases = [
            ("fire", "critical"),
            ("explosion", "critical"),
            ("gas leak", "critical"),
            ("water leak", "high"),
            ("power outage", "high"),
            ("road blocked", "high"),
            ("street light", "medium"),
            ("pothole", "medium"),
        ]

        for keyword, expected in cases:
            with self.subTest(keyword=keyword):
                description = f"Reported {keyword.upper()} near the park"
                self.assertEqual(app.classify_incident(description), expected)

    def test_classify_incident_defaults_to_low(self):
        for description in ["", "Graffiti on a wall"]:
            with self.subTest(description=description):
                self.assertEqual(app.classify_incident(description), "low")

    def test_classify_incident_prioritizes_higher_severity(self):
        cases = [
            ("pothole, water leak and fire", "critical"),
            ("street light damaged after a power outage", "high"),
        ]

        for description, expected in cases:
            with self.subTest(description=description):
                self.assertEqual(app.classify_incident(description), expected)

    def test_create_incident_classifies_and_stores_report(self):
        description = "Large water leak near Sector 15"

        incident = app.create_incident(description)

        self.assertEqual(incident, app.Incident(1, description, "high", "open"))
        self.assertEqual(len(app.INCIDENTS), 1)
        self.assertIs(app.INCIDENTS[0], incident)

    def test_create_incident_assigns_sequential_ids(self):
        first = app.create_incident("Fire near the park")
        second = app.create_incident("Pothole on Main Street")

        self.assertEqual([first.id, second.id], [1, 2])
        self.assertEqual(app.INCIDENTS, [first, second])

    def test_list_incidents_returns_empty_list_without_reports(self):
        self.assertEqual(app.list_incidents(), [])

    def test_list_incidents_returns_all_fields_in_creation_order(self):
        app.create_incident("Fire near the park")
        app.create_incident("Pothole on Main Street")

        self.assertEqual(
            app.list_incidents(),
            [
                {
                    "id": 1,
                    "description": "Fire near the park",
                    "severity": "critical",
                    "status": "open",
                },
                {
                    "id": 2,
                    "description": "Pothole on Main Street",
                    "severity": "medium",
                    "status": "open",
                },
            ],
        )

    def test_list_incidents_returns_independent_dictionaries(self):
        incident = app.create_incident("Fire near the park")

        result = app.list_incidents()
        result[0]["status"] = "closed"
        result.clear()

        self.assertEqual(incident.status, "open")
        self.assertEqual(app.INCIDENTS, [incident])
        self.assertEqual(app.list_incidents()[0]["status"], "open")

    def test_script_prints_created_incident_and_dictionary_list(self):
        with patch("sys.stdout", new_callable=io.StringIO) as output:
            runpy.run_path(app.__file__, run_name="__main__")

        self.assertEqual(
            output.getvalue(),
            "CityOps Incident Created\n"
            "Incident(id=1, description='Large water leak near Sector 15', "
            "severity='high', status='open')\n"
            "\nAll incidents:\n"
            "[{'id': 1, 'description': 'Large water leak near Sector 15', "
            "'severity': 'high', 'status': 'open'}]\n",
        )


if __name__ == "__main__":
    unittest.main()