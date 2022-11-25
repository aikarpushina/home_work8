"""
Модуль для работы преподователя
"""

import libs
import uuid


def add_student(student: list, last_name: str, first_name: str, klass: str) -> None:
    student.append(
        {
            "id": str(uuid.uuid4()),
            "last_name": last_name,
            "first_name": first_name,
            "klass": klass
        }
    )


def add_grade(student: list, journal: list, last_name: str, first_name: str, lesson: str, grade: int) -> None:
    stud = libs.find_student(student=student, last_name=last_name, first_name=first_name)
    if stud:
        less = next((less
                     for less in journal
                     if less.get("lesson") == lesson), None)
        if less:
            les = next((les
                        for les in less.get("student")
                        if les.get("student_id") == stud.get("id")), None)
            if les:
                les.get("grade").append(grade)
            else:
                less.get("student").append({"student_id": stud.get("id"), "grade": [grade]})
        else:
            print(f"Lesson {lesson} not found")
    else:
        print(f"Student {last_name} {first_name} not found")
