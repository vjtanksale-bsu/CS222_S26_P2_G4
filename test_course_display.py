import unittest
from io import StringIO
from unittest.mock import patch
from course_display import CourseDisplay


class TestCourseDisplay(unittest.TestCase):

    def test_get_available_course_numbers(self):
        courses = {
            "MATH166": [
                {
                    "section": "007",
                    "days": "MWF",
                    "start_time": "1100",
                    "end_time": "1345"
                }
            ],
            "CS222": [
                {
                    "section": "574",
                    "days": "TR",
                    "start_time": "1500",
                    "end_time": "1650"
                }
            ],
            "CS120": [
                {
                    "section": "292",
                    "days": "MWF",
                    "start_time": "1800",
                    "end_time": "1850"
                }
            ]
        }

        display = CourseDisplay(courses)

        self.assertEqual(
            display.get_available_course_numbers(),
            ["MATH166", "CS222", "CS120"]
        )

    def test_get_display_text(self):
        courses = {
            "MATH166": [],
            "CS222": [],
            "CS120": []
        }

        display = CourseDisplay(courses)

        self.assertEqual(
            display.get_display_text(),
            "MATH166\nCS222\nCS120"
        )

    def test_course_number_appears_only_once(self):
        courses = {
            "CS222": [
                {
                    "section": "574",
                    "days": "TR",
                    "start_time": "1500",
                    "end_time": "1650"
                },
                {
                    "section": "996",
                    "days": "MWF",
                    "start_time": "1530",
                    "end_time": "1815"
                }
            ]
        }

        display = CourseDisplay(courses)

        self.assertEqual(display.get_display_text().count("CS222"), 1)

    def test_display_courses_prints_available_courses(self):
        courses = {
            "CS121": [],
            "CS230": []
        }

        display = CourseDisplay(courses)

        with patch("sys.stdout", new=StringIO()) as fake_output:
            display.display_courses()

        self.assertEqual(
            fake_output.getvalue().strip(),
            "CS121\nCS230"
        )

    def test_no_available_courses(self):
        courses = {}

        display = CourseDisplay(courses)

        self.assertEqual(
            display.get_display_text(),
            "No available courses found."
        )


if __name__ == "__main__":
    unittest.main()
