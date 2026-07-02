import unittest
from datetime import time
from timetable import Course, TimetableGenerator, ScheduleConflictException

class TestTimetableGenerator(unittest.TestCase):

    # ====================  (Acceptance Criteria 1) ====================
    def test_successful_timetable_rendering(self):
        """
        Target: Verify that valid, non-overlapping course profiles pass validation
        and correctly render into the weekly timetable grid with full metadata.
        """
        # Arrange: Initialize mock course data with disjoint/non-overlapping time slots
        course1 = Course("Computer Science 104", "Monday", time(9, 0), time(10, 30), "Prof. Morgan")
        course2 = Course("Software Engineering 202", "Monday", time(11, 0), time(12, 30), "Prof. Smith")
        
        generator = TimetableGenerator()
        generator.add_course(course1)
        generator.add_course(course2)
        
        # Act: Inject components into the generator context and attempt grid compilation
        rendered_grid = generator.generate_grid()
        
        # Assert: Verify that the multi-dimensional layout dictionary contains exact mapped keys/values
        self.assertIn("Monday", rendered_grid)
        self.assertIn("09:00-10:30", rendered_grid["Monday"])
        self.assertEqual("Computer Science 104 (Prof. Morgan)", rendered_grid["Monday"]["09:00-10:30"])
        self.assertEqual("Software Engineering 202 (Prof. Smith)", rendered_grid["Monday"]["11:00-12:30"])

    # ====================  (Acceptance Criteria 2) ====================
    def test_conflict_handling_raises_exception(self):
        """
        Target: Boundary testing for overlapping hours. Ensure that the conflict 
        engine successfully intercepts bad data and throws the precise custom exception.
        """
        # Arrange: Construct two distinct courses with conflicting hour ranges on Monday
        course1 = Course("AI Integration", "Monday", time(10, 0), time(11, 30), "Prof. Xue")
        course2 = Course("Database Systems", "Monday", time(11, 0), time(12, 30), "Prof. Jones") # Overlaps at 11:00
        
        generator = TimetableGenerator()
        generator.add_course(course1)
        generator.add_course(course2)
        
        # Act & Assert: Expect the execution to fail, throwing the precise custom domain exception
        with self.assertRaises(ScheduleConflictException) as context:
            generator.generate_grid()
            
        # Assert: Validate that the caught exception contains descriptive error context for the UI
        self.assertIn("Schedule conflict detected", str(context.exception))
        self.assertIn("AI Integration", str(context.exception))
        self.assertIn("Database Systems", str(context.exception))

if __name__ == '__main__':
    unittest.main()