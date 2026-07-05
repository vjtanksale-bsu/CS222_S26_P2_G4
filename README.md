# CS222_S26_P2_G4

# Course Scheduling System

## Overview

This project is a course scheduling system developed for CS222 Project 2.

The program helps students build a semester schedule by allowing them to view available courses, enter the number of courses they want to register for, select course numbers, and generate a timetable. If a valid schedule cannot be created, the system should report the issue to the user.

The project is implemented in Python using Test-Driven Development (TDD), Clean Code principles, and GitHub branching workflow.

---

## Authors

- Xuancen Liu
- Qijun Ma
- Haozhi Xue

---

## User Stories

The project is divided into multiple user stories. Each user story is developed on its own GitHub branch before being merged into the main branch.

Current user stories include:

1. Course count input
2. Available course display
3. Course selection
4. Timetable generation and conflict validation

Detailed descriptions for each user story will be added as the project develops.

---

## Project Structure

The repository contains the main program files and unit test files for each user story.

Example files may include:

- `course_reader.py`
- `course_display.py`
- `timetable.py`
- `test_course_reader.py`
- `test_course_display.py`
- `test_of_timetable.py`
- `README.md`

---

## Development Process

This project follows:

- Test-Driven Development (TDD)
- Clean Code principles
- GitHub branch workflow
- Pull requests and code review
- Team communication through Microsoft Teams

Each feature should have related unit tests before being merged into the main branch.

---

## Running Tests

Unit tests are written using Python's `unittest` framework.

To run a test file, use:

```
python -m unittest test_file_name.py
```

For example:

```
python -m unittest test_course_display.py
```
