from datetime import time
from typing import List, Dict

class ScheduleConflictException(Exception):
    """
    Custom exception thrown when a time overlap/conflict 
    is detected between two or more scheduled courses.
    """
    pass

class Course:
    def __init__(self, name: str, day: str, start_time: time, end_time: time, professor: str):
        self.name = name
        self.day = day
        self.start_time = start_time
        self.end_time = end_time
        self.professor = professor

    def overlaps_with(self, other: 'Course') -> bool:
        """
        Evaluates whether the current course overlaps in time with another course.
        Returns True if they occur on the same day and their time intervals intersect.
        """
        if self.day != other.day:
            return False
        
        # Standard interval overlap condition: (StartA < EndB) AND (EndA > StartB)
        return self.start_time < other.end_time and self.end_time > other.start_time

class TimetableGenerator:
    def __init__(self):
        # Stores the collection of courses to be validated and rendered
        self.courses: List[Course] = []

    def add_course(self, course: Course):
        """Adds a new course instance to the generation queue."""
        self.courses.append(course)

    def validate_no_conflicts(self):
        """
        Adheres to the Single Responsibility Principle (SRP).
        Performs an O(N^2) pairwise boundary check across all added courses 
        to ensure zero scheduling overlaps.
        """
        for i, course_a in enumerate(self.courses):
            for course_b in self.courses[i + 1:]:
                if course_a.overlaps_with(course_b):
                    raise ScheduleConflictException(
                        f"Schedule conflict detected on {course_a.day} "
                        f"between '{course_a.name}' and '{course_b.name}'."
                    )

    def generate_grid(self) -> Dict[str, Dict[str, str]]:
        """
        Executes the business logic workflow: 
        1. Validates data integrity (conflict resolution engine).
        2. Renders the clean weekly timetable grid structure as a nested dictionary.
        """
        # Trigger the validation constraint before execution
        self.validate_no_conflicts()
        
        grid = {}
        for course in self.courses:
            # Initialize day group if not already present in the dictionary
            if course.day not in grid:
                grid[course.day] = {}
            
            # Format time boundaries into a highly readable slot string (e.g., "09:00-10:30")
            time_slot = f"{course.start_time.strftime('%H:%M')}-{course.end_time.strftime('%H:%M')}"
            
            # Explicitly render full course details including course name and professor name
            grid[course.day][time_slot] = f"{course.name} ({course.professor})"
            
        return grid
    
    def print_grid(self):
        """
        Utility function to print the generated timetable grid in a human-readable format.
        Useful for debugging and visual verification of the rendered structure.
        """
        grid = self.generate_grid()
        for day, slots in grid.items():
            print(f"{day}:")
            for time_slot, course_info in slots.items():
                print(f"  {time_slot} : {course_info}")