# CS222_S26_P2_G4
# Feature: Course Count Input (User Story 1)

## Description

As a student,  
I want to enter the number of courses I plan to register for,  
So that the scheduling system knows how many courses I need.

---

## Acceptance Criteria & Implementation Plan

We will implement this feature following TDD principles.

### 1. Prompt for Number of Courses

- **Criteria:** The system asks the user how many courses they want to register for.
- **TDD Target:** Test that the program accepts a valid number of courses.

### 2. Valid Positive Integer Input

- **Criteria:** The user can enter a positive integer.
- **TDD Target:** Test that positive integer input is accepted.

### 3. Invalid Input Handling

- **Criteria:** Invalid input is rejected with an error message.
- **TDD Target:** Test that non-numeric input and values less than 1 are rejected.

### 4. Continue After Valid Input

- **Criteria:** The system proceeds to course selection after a valid number is entered.
- **TDD Target:** Test that the valid number is returned or stored for the next step.
