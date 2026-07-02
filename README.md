## User Story 4: Timetable Generation & Conflict Handling
## Acceptance Criteria
**Visual Timetable Grid**
    The system displays a completed weekly timetable grid if all selected courses have no scheduling conflicts.
**Rich Metadata Display**
    Each course in the visual timetable explicitly displays the **Course Name**, **Time Slot**, and **Professor Name**.
**Conflict Detection Engine**
    The system automatically rejects the layout generation and flags the specific conflicting courses if any selected courses overlap in time.
**Explicit Error Prompting**
    The system displays an explicit, user-friendly error message explaining that the generation failed due to a schedule conflict.
## Technical Implementation Overview (TDD & Clean Code)
 **Test-Driven Development (TDD):** Implementation follows strict Red-Green-Refactor cycles. Core conflict boundaries (partial overlap, identical slots, back-to-back checking) are completely covered by automated test cases.
  **Defensive Design:** Time parsing and overlap checks are decoupled from UI grid rendering to ensure clean architecture and separation of concerns.
