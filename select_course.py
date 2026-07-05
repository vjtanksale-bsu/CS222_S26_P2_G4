class CourseSelector:

    def __init__(self, filename):
        self.filename = filename
        self.course_catalog = self.load_courses()
        self.selected_courses = {}

    def load_courses(self):
        """
        Load course information from the input file into a dictionary.

        Returns:
            {
                "CS222": [
                    {
                        "section": "574",
                        "days": "TR",
                        "start_time": "1500",
                        "end_time": "1650"
                    },
                    ...
                ],
                ...
            }
        """
        courses = {}

        with open(self.filename, "r") as file:
            for line in file:
                parts = line.strip().split()

                if len(parts) != 5:
                    continue

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

    def course_exists(self, course_number):
        """Check whether the course number exists."""
        return course_number in self.course_catalog

    def select_courses(self, required_courses):
        """
        Allow the student to enter course numbers.

        Args:
            required_courses (int): Number of courses entered in User Story 1.

        Returns:
            dict: Selected courses with all section information.
        """

        while len(self.selected_courses) < required_courses:

            course_number = input(
                f"Enter course number {len(self.selected_courses) + 1}: "
            ).strip().upper()

            if not self.course_exists(course_number):
                print("Invalid course number. Please try again.")
                continue

            if course_number in self.selected_courses:
                print("Course already selected. Please enter a different course.")
                continue

            self.selected_courses[course_number] = self.course_catalog[course_number]

        print("\nCourse selections accepted.")
        return self.selected_courses

    def get_selected_courses(self):
        """Return the selected courses."""
        return self.selected_courses