class CourseReader:
    """Reads course data and provides available course numbers."""

    def __init__(self, filename):
        self.filename = filename

    def load_courses(self):
        """Load course information from the course file."""
        courses = []

        with open(self.filename, "r") as file:
            for line in file:
                parts = line.split()

                course = {
                    "course_number": parts[0],
                    "section": parts[1],
                    "days": parts[2],
                    "start_time": parts[3],
                    "end_time": parts[4]
                }

                courses.append(course)

        return courses

    def get_available_course_numbers(self):
        """Return a list of unique available course numbers."""
        courses = self.load_courses()
        course_numbers = []

        for course in courses:
            if course["course_number"] not in course_numbers:
                course_numbers.append(course["course_number"])

        return course_numbers
