class ModifyCourses:
    """
    Manage selected courses.
    """

    def __init__(self, selected_courses):
        self.selected_courses = selected_courses

    def remove_course(self, course_number):
        """
        Remove a selected course.

        Args:
            course_number (str): The course number to remove.

        Returns:
            bool:
                True if the course is removed successfully.
                False if the course was not selected.
        """

        if course_number not in self.selected_courses:
            print("Course is not currently selected.")
            return False

        del self.selected_courses[course_number]

        print(f"{course_number} removed successfully.")
        return True