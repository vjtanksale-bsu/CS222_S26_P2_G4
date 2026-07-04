import unittest
from unittest.mock import patch

from select_course import (
    load_courses,
    course_exists,
    select_courses
)


class TestCourseSelection(unittest.TestCase):

    def setUp(self):
        self.course_catalog = load_courses("courses.txt")

    def test_load_courses(self):
        self.assertIn("CS222", self.course_catalog)
        self.assertIn("MATH166", self.course_catalog)

    def test_course_exists(self):
        self.assertTrue(course_exists("CS222", self.course_catalog))

    def test_course_not_exists(self):
        self.assertFalse(course_exists("CS999", self.course_catalog))

    @patch("builtins.input", side_effect=["CS222"])
    def test_select_one_valid_course(self, mock_input):

        selected = select_courses(self.course_catalog, 1)

        self.assertIn("CS222", selected)

    @patch("builtins.input", side_effect=["CS999", "CS222"])
    def test_invalid_course_then_valid_course(self, mock_input):

        selected = select_courses(self.course_catalog, 1)

        self.assertIn("CS222", selected)
        self.assertNotIn("CS999", selected)

    @patch("builtins.input", side_effect=["CS222", "CS222", "MATH166"])
    def test_duplicate_course(self, mock_input):

        selected = select_courses(self.course_catalog, 2)

        self.assertEqual(len(selected), 2)
        self.assertIn("CS222", selected)
        self.assertIn("MATH166", selected)


if __name__ == "__main__":
    unittest.main()