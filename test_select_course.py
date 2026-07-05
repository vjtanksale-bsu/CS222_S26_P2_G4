import unittest
from unittest.mock import patch
from select_course import CourseSelector


class TestCourseSelector(unittest.TestCase):

    def setUp(self):
        self.selector = CourseSelector("courses.txt")

    def test_load_courses(self):
        """Test that courses are loaded correctly."""
        self.assertIn("CS222", self.selector.course_catalog)
        self.assertIn("MATH166", self.selector.course_catalog)

    def test_course_exists(self):
        """Test a valid course number."""
        self.assertTrue(self.selector.course_exists("CS222"))

    def test_course_not_exists(self):
        """Test an invalid course number."""
        self.assertFalse(self.selector.course_exists("CS999"))

    @patch("builtins.input", side_effect=["CS222"])
    def test_select_one_valid_course(self, mock_input):
        """Test selecting one valid course."""
        selected = self.selector.select_courses(1)

        self.assertEqual(len(selected), 1)
        self.assertIn("CS222", selected)

    @patch("builtins.input", side_effect=["CS999", "CS222"])
    def test_invalid_course_then_valid_course(self, mock_input):
        """Test entering an invalid course followed by a valid one."""
        selected = self.selector.select_courses(1)

        self.assertEqual(len(selected), 1)
        self.assertIn("CS222", selected)

    @patch("builtins.input", side_effect=["CS222", "CS222", "MATH166"])
    def test_duplicate_course(self, mock_input):
        """Test duplicate course selection."""
        selected = self.selector.select_courses(2)

        self.assertEqual(len(selected), 2)
        self.assertIn("CS222", selected)
        self.assertIn("MATH166", selected)


if __name__ == "__main__":
    unittest.main()