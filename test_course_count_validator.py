import unittest
from course_count_validator import CourseCountValidator


class TestCourseCountValidator(unittest.TestCase):

    def test_valid_course_count_is_accepted(self):
        available_courses = ["CS120", "CS121", "CS222"]
        validator = CourseCountValidator(available_courses)

        self.assertEqual(validator.validate_course_count(2), 2)

    def test_course_count_cannot_be_zero(self):
        available_courses = ["CS120", "CS121", "CS222"]
        validator = CourseCountValidator(available_courses)

        with self.assertRaises(ValueError):
            validator.validate_course_count(0)

    def test_course_count_cannot_be_negative(self):
        available_courses = ["CS120", "CS121", "CS222"]
        validator = CourseCountValidator(available_courses)

        with self.assertRaises(ValueError):
            validator.validate_course_count(-1)

    def test_course_count_must_be_integer(self):
        available_courses = ["CS120", "CS121", "CS222"]
        validator = CourseCountValidator(available_courses)

        with self.assertRaises(TypeError):
            validator.validate_course_count("two")

    def test_user_cannot_enter_more_courses_than_offered(self):
        available_courses = ["CS120", "CS121", "CS222"]
        validator = CourseCountValidator(available_courses)

        with self.assertRaises(ValueError):
            validator.validate_course_count(4)


if __name__ == "__main__":
    unittest.main()