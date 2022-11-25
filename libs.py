"""
Модуль со вспомогательными функциями
"""


def find_student(student: list, last_name: str, first_name: str) -> dict:
    stud = next((stud
                 for stud in student
                 if stud.get("last_name") == last_name
                 and stud.get("first_name") == first_name), None)
    return stud
