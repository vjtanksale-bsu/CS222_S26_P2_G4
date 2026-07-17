class CourseReader:
    """Reads course data and provides available course numbers."""

    def __init__(self, filename):
        # Store the input file name.
        self.filename = filename

    def load_courses(self):
        """Load course information into a dictionary."""
        courses = {}

        # Read each course section from the file.
        with open(self.filename, "r") as file:
            for line in file:
                parts = line.split()

                course_number = parts[0]
                section = {
                    "section": parts[1],
                    "days": parts[2],
                    "start_time": parts[3],
                    "end_time": parts[4]
                }

                if course_number not in courses:
                    courses[course_number] = []

                courses[course_number].append(section)

        return courses

    def get_available_course_numbers(self):
        """Return a list of available course numbers."""
        courses = self.load_courses()
        return list(courses.keys())
