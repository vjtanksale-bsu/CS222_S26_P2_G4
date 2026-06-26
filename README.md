# CS222_S26_P2_G4
# Feature: Available Course Display (User Story 2)

## Description

As a student,  
I want to view all available course numbers,  
So that I can decide which courses I want to register for.

---

## Acceptance Criteria & Implementation Plan

We will implement this feature following TDD principles.

### 1. Display Offered Courses

- **Criteria:** The system displays all offered course numbers.
- **TDD Target:** Test that all available course numbers are returned or displayed.

### 2. Display Before Course Selection

- **Criteria:** The list is shown before course selection begins.
- **TDD Target:** Test that available courses can be retrieved before user course input.

### 3. Unique Course Numbers

- **Criteria:** Each course number appears only once.
- **TDD Target:** Test that duplicate course numbers are removed from the displayed list.

### 4. Review Before Selection

- **Criteria:** The user can review the list before entering course selections.
- **TDD Target:** Test that the course list is accessible before selected courses are submitted.
