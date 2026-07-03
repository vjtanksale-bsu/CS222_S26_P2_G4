def load_courses(filename):
    courses = []

    with open(filename, "r") as file:
        for line in file:
            parts = line.split()
            if parts:
                course = parts[0]
                if course not in courses:
                    courses.append(course)

    return courses

def course_exists(course_number, courses):
    return course_number in courses

def select_course(course_number, courses, selected, required_courses=None):

    if course_number not in courses:
        return False

    if course_number in selected:
        return False

    selected.append(course_number)
    return True