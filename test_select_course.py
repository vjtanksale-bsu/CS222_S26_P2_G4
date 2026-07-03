import unittest
from select_course import load_courses


class TestCourseSelection(unittest.TestCase):

    def test_load_courses(self):
        courses = load_courses("course.txt")

        self.assertIn("CS222", courses)
        self.assertIn("MATH166", courses)


if __name__ == "__main__":
    unittest.main()