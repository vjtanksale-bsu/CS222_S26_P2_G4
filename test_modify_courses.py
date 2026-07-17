import unittest

from modify_courses import ModifyCourses


class TestModifyCourses(unittest.TestCase):

    def setUp(self):
        self.selected_courses = {
            "CS222": [
                {
                    "section": "574",
                    "days": "TR",
                    "start_time": "1500",
                    "end_time": "1650"
                }
            ],
            "MATH166": [
                {
                    "section": "007",
                    "days": "MWF",
                    "start_time": "1100",
                    "end_time": "1345"
                }
            ]
        }

        self.modify = ModifyCourses(self.selected_courses)


    def test_remove_selected_course(self):
        result = self.modify.remove_course("CS222")

        self.assertTrue(result)
        self.assertNotIn(
            "CS222",
            self.modify.selected_courses
        )


    def test_remove_unselected_course(self):
        result = self.modify.remove_course("CS999")

        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()