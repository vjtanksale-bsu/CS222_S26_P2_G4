class CourseDisplay:
    """Displays available course numbers from course data."""

    def __init__(self, courses):
        # Store the course dictionary.
        self.courses = courses

    def get_available_course_numbers(self):
        """Return all available course numbers."""
        return list(self.courses.keys())

    def get_display_text(self):
        """Return course numbers as display text."""
        course_numbers = self.get_available_course_numbers()

        if not course_numbers:
            return "No available courses found."

        return "\n".join(course_numbers)

    def display_courses(self):
        """Print available course numbers for the user."""
        print(self.get_display_text())
