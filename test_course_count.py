import unittest
from course_count import validate_course_count


class TestCourseCount(unittest.TestCase):

    def test_valid_course_count(self):
        self.assertEqual(validate_course_count("3"), 3)

    def test_invalid_non_number_input(self):
        with self.assertRaises(ValueError):
            validate_course_count("abc")

    def test_invalid_zero_input(self):
        with self.assertRaises(ValueError):
            validate_course_count("0")

    def test_invalid_negative_input(self):
        with self.assertRaises(ValueError):
            validate_course_count("-2")


if __name__ == "__main__":
    unittest.main()
