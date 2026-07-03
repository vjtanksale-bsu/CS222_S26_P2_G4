import unittest
from select_course import load_courses, course_exists

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
        courses = load_courses("course.txt")
        selected = ["CS222"]

        result = select_course("CS222", courses, selected)

        self.assertFalse(result)
        self.assertEqual(selected.count("CS222"), 1)