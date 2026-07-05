import unittest
from course_reader import CourseReader


class TestCourseReader(unittest.TestCase):
    
        def test_load_courses_returns_dictionary(self):
        # Create a small test course file.
        with open("test_courses.txt", "w") as file:
            file.write("CS120 001 MWF 0900 0950\n")
            file.write("CS120 003 TR 0930 1045\n")
            file.write("CS121 001 TR 1230 1345\n")

        reader = CourseReader("test_courses.txt")
        courses = reader.load_courses()

        self.assertIn("CS120", courses)
        self.assertEqual(len(courses["CS120"]), 2)
        self.assertEqual(courses["CS120"][0]["section"], "001")

    def test_get_available_course_numbers(self):

        # Create a small test course file.
        with open("test_courses.txt", "w") as file:
            file.write("CS120 001 MWF 0900 0950\n")
            file.write("CS120 003 TR 0930 1045\n")
            file.write("CS121 001 TR 1230 1345\n")
            file.write("CS222 005 TR 1100 1215\n")

        reader = CourseReader("test_courses.txt")

        self.assertEqual(
            reader.get_available_course_numbers(),
            ["CS120", "CS121", "CS222"]
        )


if __name__ == "__main__":
    unittest.main()
