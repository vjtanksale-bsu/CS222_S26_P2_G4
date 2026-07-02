# CS222_S26_P2_G4 - Branch: user-story-4
# Course Scheduling System — Timetable Generation

This branch contains the implementation of **User Story 4**, focusing on visual timetable generation, metadata rendering, and core schedule conflict detection.

---

## Feature Overview

### User Story 4
> **As a student,** > I want to view my generated timetable or receive an error prompt if there is a conflict  
> **so that** I can confirm my schedule or resolve registration failures.

---

## Acceptance Criteria

1. **Visual Timetable Grid** The system successfully displays a completed weekly timetable grid if all selected courses have no scheduling conflicts.

2. **Course Details Display** Each course rendered within the visual timetable explicitly displays:
   - Course Name
   - Time Slot
   - Professor Name

3. **Conflict Detection & Rejection** The system automatically rejects the layout generation and flags the specific conflicting courses if any selected courses overlap in time.

4. **Explicit Error Prompting** The system displays a clear, user-friendly error message explaining that the generation failed due to a schedule conflict.

---

## Technical Implementation Details

- **TDD Approach**: Every acceptance criterion is driven by unit tests in `tests/`, ensuring that edge cases (such as exact back-to-back courses or multiple overlapping slots) are handled robustly.
- **Clean Code**: Code is structured to separate the *Conflict Detection Logic* (Core Domain) from the *Grid Rendering UI* (Presentation Layer).

---

## Authors
- Haozhi Xue
