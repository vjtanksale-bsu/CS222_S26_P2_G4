class CourseAvailabilityValidator:
    """Validates whether a selected course is offered."""

    def __init__(self, courses):
        # Store the course dictionary.
        self.courses = courses

    def normalize_course_number(self, course_number):
        """Clean and standardize the entered course number."""
        if not isinstance(course_number, str):
            return ""

        return course_number.strip().upper()

    def is_course_offered(self, course_number):
        """Return True when the course exists in the offered courses."""
        normalized_course = self.normalize_course_number(course_number)

        if not normalized_course:
            return False

        return normalized_course in self.courses

    def validate_course(self, course_number):
        """Return a valid course number or raise an error."""
        normalized_course = self.normalize_course_number(course_number)

        if not self.is_course_offered(course_number):
            raise ValueError(
                f"{normalized_course or 'Course'} is not offered."
            )

        return normalized_course