def validate_course_count(user_input):
    try:
        course_count = int(user_input)
    except ValueError:
        raise ValueError("Course count must be a positive integer")

    if course_count <= 0:
        raise ValueError("Course count must be greater than zero")

    return course_count
