import os
import tempfile
import unittest

from PDF_generator import ScheduledCourse, TimetablePdfExporter


class TestTimetablePdfExporter(unittest.TestCase):

    def setUp(self):
        """Create a temporary sandbox for each test."""
        self.test_sandbox = tempfile.TemporaryDirectory()

    def tearDown(self):
        """Clean up temporary files."""
        self.test_sandbox.cleanup()

    def test_export_valid_schedule_successfully(self):
        """Verify that a valid schedule is exported to a PDF."""

        courses = [
            ScheduledCourse(
                "Introduction to CS",
                "Mon 09:00-11:00",
                "Dr. Alan Turing"
            ),
            ScheduledCourse(
                "Calculus I",
                "Wed 11:00-13:00",
                "Prof. Isaac Newton"
            ),
            ScheduledCourse(
                "General Physics",
                "Fri 14:00-16:00",
                "Dr. Marie Curie"
            )
        ]

        output_file = os.path.join(
            self.test_sandbox.name,
            "student_schedule.pdf"
        )

        exporter = TimetablePdfExporter(output_file)

        exporter.export(courses)

        self.assertTrue(os.path.exists(output_file))
        self.assertGreater(os.path.getsize(output_file), 0)

        # Verify the generated file is actually a PDF
        with open(output_file, "rb") as pdf:
            self.assertEqual(pdf.read(4), b"%PDF")

    def test_export_none_schedule(self):
        """Export should reject None."""

        output_file = os.path.join(
            self.test_sandbox.name,
            "schedule.pdf"
        )

        exporter = TimetablePdfExporter(output_file)

        with self.assertRaises(ValueError):
            exporter.export(None)

        self.assertFalse(os.path.exists(output_file))

    def test_export_empty_schedule(self):
        """Export should reject an empty list."""

        output_file = os.path.join(
            self.test_sandbox.name,
            "schedule.pdf"
        )

        exporter = TimetablePdfExporter(output_file)

        with self.assertRaises(ValueError):
            exporter.export([])

        self.assertFalse(os.path.exists(output_file))

    def test_export_invalid_object(self):
        """Every element must be a ScheduledCourse."""

        output_file = os.path.join(
            self.test_sandbox.name,
            "schedule.pdf"
        )

        exporter = TimetablePdfExporter(output_file)

        courses = [
            ScheduledCourse(
                "CS222",
                "Mon 09:00",
                "Dr. Smith"
            ),
            "Not a Course Object"
        ]

        with self.assertRaises(ValueError):
            exporter.export(courses)

    def test_output_directory_created(self):
        """Exporter should automatically create missing folders."""

        output_file = os.path.join(
            self.test_sandbox.name,
            "new_folder",
            "sub_folder",
            "schedule.pdf"
        )

        exporter = TimetablePdfExporter(output_file)

        exporter.export([
            ScheduledCourse(
                "CS222",
                "Mon 09:00",
                "Dr. Smith"
            )
        ])

        self.assertTrue(os.path.exists(output_file))

    def test_invalid_output_extension(self):
        """Output file must end with .pdf."""

        invalid_file = os.path.join(
            self.test_sandbox.name,
            "schedule.txt"
        )

        with self.assertRaises(ValueError):
            TimetablePdfExporter(invalid_file)

    def test_scheduled_course_validation(self):
        """ScheduledCourse should reject invalid values."""

        with self.assertRaises(ValueError):
            ScheduledCourse(
                "",
                "Mon 09:00",
                "Prof. Smith"
            )

        with self.assertRaises(ValueError):
            ScheduledCourse(
                "Data Structures",
                "",
                "Prof. Smith"
            )

        with self.assertRaises(ValueError):
            ScheduledCourse(
                "Data Structures",
                "Mon 09:00",
                ""
            )

        with self.assertRaises(ValueError):
            ScheduledCourse(
                None,
                "Mon 09:00",
                "Prof. Smith"
            )

        with self.assertRaises(ValueError):
            ScheduledCourse(
                "Data Structures",
                None,
                "Prof. Smith"
            )

        with self.assertRaises(ValueError):
            ScheduledCourse(
                "Data Structures",
                "Mon 09:00",
                None
            )

        with self.assertRaises(ValueError):
            ScheduledCourse(
                "   ",
                "Mon 09:00",
                "Prof. Smith"
            )

        with self.assertRaises(ValueError):
            ScheduledCourse(
                "Data Structures",
                "   ",
                "Prof. Smith"
            )

        with self.assertRaises(ValueError):
            ScheduledCourse(
                "Data Structures",
                "Mon 09:00",
                "   "
            )


if __name__ == "__main__":
    unittest.main()