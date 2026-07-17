import unittest
from course_availability_validator import CourseAvailabilityValidator


class TestCourseAvailabilityValidator(unittest.TestCase):

    def setUp(self):
        # Use dictionary-based course data.
        self.courses = {
            "CS120": [],
            "CS121": [],
            "CS222": []
        }

        self.validator = CourseAvailabilityValidator(self.courses)

    def test_offered_course_is_valid(self):
        self.assertTrue(
            self.validator.is_course_offered("CS120")
        )

    def test_unoffered_course_is_invalid(self):
        self.assertFalse(
            self.validator.is_course_offered("CS999")
        )

    def test_lowercase_course_is_valid(self):
        self.assertTrue(
            self.validator.is_course_offered("cs121")
        )

    def test_empty_course_is_invalid(self):
        self.assertFalse(
            self.validator.is_course_offered("")
        )

    def test_validate_course_returns_normalized_number(self):
        self.assertEqual(
            self.validator.validate_course(" cs222 "),
            "CS222"
        )

    def test_validate_course_raises_error(self):
        with self.assertRaises(ValueError):
            self.validator.validate_course("MATH999")


if __name__ == "__main__":
    unittest.main()