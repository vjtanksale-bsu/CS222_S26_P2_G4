def load_courses(filename):
    courses = []

    with open(filename, "r") as file:
        for line in file:
            parts = line.split()

            if parts:
                course_number = parts[0]

                if course_number not in courses:
                    courses.append(course_number)

    return courses