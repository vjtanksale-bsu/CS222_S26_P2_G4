import os
from typing import List
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors


class ScheduledCourse:
    """Value object representing a successfully scheduled course entry."""

    def __init__(self, name: str, time_slot: str, professor: str):
        if not name or not name.strip():
            raise ValueError("Course name cannot be blank.")

        if not time_slot or not time_slot.strip():
            raise ValueError("Time slot cannot be blank.")

        if not professor or not professor.strip():
            raise ValueError("Professor name cannot be blank.")

        self.name = name.strip()
        self.time_slot = time_slot.strip()
        self.professor = professor.strip()


class TimetablePdfExporter:
    """Exports a weekly timetable to a PDF document."""

    def __init__(self, output_path: str):
        if not output_path or not output_path.strip():
            raise ValueError("Target local output file path cannot be blank.")

        output_path = output_path.strip()

        if not output_path.lower().endswith(".pdf"):
            raise ValueError("Output file must have a .pdf extension.")

        self._output_path = output_path

    def export(self, courses: List[ScheduledCourse]) -> None:
        """
        Export the provided schedule into a PDF file.

        :param courses: List of ScheduledCourse objects.
        :raises ValueError: Invalid input.
        :raises RuntimeError: File system or PDF generation failure.
        """

        if courses is None:
            raise ValueError("Schedule data cannot be None.")

        if len(courses) == 0:
            raise ValueError("Schedule data cannot be empty.")

        validated_courses = []

        for course in courses:
            if not isinstance(course, ScheduledCourse):
                raise ValueError(
                    "Every item in courses must be a ScheduledCourse object."
                )
            validated_courses.append(course)

        directory = os.path.dirname(self._output_path)
        if directory:
            os.makedirs(directory, exist_ok=True)

        try:
            doc = SimpleDocTemplate(
                self._output_path,
                pagesize=letter,
            )

            styles = getSampleStyleSheet()

            story = []

            story.append(
                Paragraph(
                    "Official Weekly Timetable",
                    styles["Heading1"],
                )
            )

            story.append(
                Paragraph(
                    "Generated via Course Registration System (Iteration 3)",
                    styles["Normal"],
                )
            )

            story.append(Spacer(1, 20))

            table_data = [
                [
                    "Course Name",
                    "Time Slot",
                    "Professor",
                ]
            ]

            for course in validated_courses:
                table_data.append(
                    [
                        course.name,
                        course.time_slot,
                        course.professor,
                    ]
                )

            table = Table(
                table_data,
                colWidths=[200, 150, 150],
                repeatRows=1,
            )

            table.setStyle(
                TableStyle(
                    [
                        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
                        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
                        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                        ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                        ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
                        ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
                        ("GRID", (0, 0), (-1, -1), 1, colors.darkgrey),
                    ]
                )
            )

            story.append(table)

            doc.build(story)

        except (IOError, OSError) as e:
            raise RuntimeError(
                f"Failed to export PDF due to a file system error: {e}"
            ) from e

        except Exception as e:
            raise RuntimeError(
                f"Unexpected error while generating PDF: {e}"
            ) from e