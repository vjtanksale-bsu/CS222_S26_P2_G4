def load_courses(filename):
    """
    Read all courses from the input file and store them in a dictionary.

    Returns:
        {
            "CS222": [
                {
                    "section": "574",
                    "days": "TR",
                    "start": "1500",
                    "end": "1650"
                },
                ...
            ],
            ...
        }
    """
    course_catalog = {}

    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split()

            if len(parts) != 5:
                continue

            course_number, section, days, start, end = parts

            section_info = {
                "section": section,
                "days": days,
                "start": start,
                "end": end
            }

            if course_number not in course_catalog:
                course_catalog[course_number] = []

            course_catalog[course_number].append(section_info)

    return course_catalog


def course_exists(course_number, course_catalog):
    """
    Check whether a course number exists.
    """
    return course_number in course_catalog


def select_courses(course_catalog, required_courses):
    """
    Allow the student to select course numbers.

    Args:
        course_catalog: Dictionary returned by load_courses().
        required_courses: Number of courses requested
                          (provided by User Story 1).

    Returns:
        Dictionary containing all selected courses and their sections.
    """

    selected_courses = {}

    while len(selected_courses) < required_courses:

        course_number = input(
            f"Enter course {len(selected_courses)+1}: "
        ).strip().upper()

        if not course_exists(course_number, course_catalog):
            print("Invalid course number. Please try again.")
            continue

        if course_number in selected_courses:
            print("Course already selected. Please enter a different course.")
            continue

        selected_courses[course_number] = course_catalog[course_number]

    print("\nCourse selections accepted.")
    return selected_courses