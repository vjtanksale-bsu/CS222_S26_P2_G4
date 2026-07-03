import unittest
from select_course import load_courses, course_exists, select_course

class TestCourseSelection(unittest.TestCase):

    def test_valid_course(self):
        courses = load_courses("courses.txt")
        self.assertTrue(course_exists("CS222", courses))

    def test_select_valid_course(self):
        courses = load_courses("courses.txt")
        selected = []
        
        result = select_course("CS222", courses, selected)
        self.assertTrue(result)
        self.assertIn("CS222", selected)

    def test_invalid_course(self):
        courses = load_courses("courses.txt")
        selected = []

        result = select_course("CS999", courses, selected)

        self.assertFalse(result)
        self.assertNotIn("CS999", selected)

    def test_duplicate_course(self):
        courses = load_courses("courses.txt")
        selected = ["CS222"]

        result = select_course("CS222", courses, selected)

        self.assertFalse(result)
        self.assertEqual(selected.count("CS222"), 1)

    def test_course_limit(self):
        courses = load_courses("courses.txt")
        selected = []

        required_courses = 2

        if len(selected) < required_courses:
            self.assertTrue(select_course("CS222", courses, selected))

        if len(selected) < required_courses:
            self.assertTrue(select_course("MATH166", courses, selected))

        if len(selected) < required_courses:
            select_course("CS120", courses, selected)

if __name__ == "__main__":
    unittest.main()