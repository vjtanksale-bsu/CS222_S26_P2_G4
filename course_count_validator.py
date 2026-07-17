class CourseCountValidator:
    """Validates the number of courses a student wants to register for."""

    def __init__(self, available_courses):
        # Store the available courses for validation.
        self.available_courses = available_courses

    def get_available_course_count(self):
        """Return how many unique courses are available."""
        return len(self.available_courses)

    def validate_course_count(self, course_count):
        """Validate the number of courses entered by the user."""
        if not isinstance(course_count, int):
            raise TypeError("Course count must be an integer.")

        if course_count <= 0:
            raise ValueError("Course count must be greater than zero.")

        if course_count > self.get_available_course_count():
            raise ValueError("Course count cannot be greater than available courses.")

        return course_count