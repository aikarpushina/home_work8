"""
Модуль для работы студентов
"""

import libs

def find_grade_student(student: list, journal: list, last_name: str, first_name: str) -> tuple:
    result = {}
    stud = libs.find_student(student=student, last_name=last_name, first_name=first_name)
    if stud:
        les = (
            (lesson.get("lesson"),
             (next((les
                    for les in lesson.get("student")
                    if les.get("student_id") == stud.get("id")), None)))
            for lesson in journal)
        for item in les:
            if item[1]:
                result[item[0]] = item[1].get("grade")
            else:
                result[item[0]] = []
    else:
        return f'{last_name} {first_name} not found', None
    return f'{last_name} {first_name}', result