"""
Создать информационную систему позволяющую работать с учениками школы
Минимальные требования:
1 - учитель добавление ученика, добавление оценки за предмет ученику
2 - ученик Поиск по фамилии ученика
"""
import uuid

students = [
    {"id": "6fa0ba0f-bca6-41bb-ac3f-13de2a7bbf2f", "last_name": "Ivanov", "first_name": "Sergey", "klass": "10b"},
    {"id": "8f4cfe1f-1f78-4cdc-8cfd-a3406a990b3e", "last_name": "Petrov", "first_name": "Ivan", "klass": "10b"},
    {"id": "be087d42-da91-40b7-88dc-851078d568a0", "last_name": "Sidorov", "first_name": "Nikolay", "klass": "10b"},
]

journals = [
    {"lesson": "math",
     "student": [
        {"student_id": "6fa0ba0f-bca6-41bb-ac3f-13de2a7bbf2f", "grade": [3, 4, 5, 2, 5, 4]},
        {"student_id": "8f4cfe1f-1f78-4cdc-8cfd-a3406a990b3e", "grade": [2]},
        {"student_id": "be087d42-da91-40b7-88dc-851078d568a0", "grade": [4, 4, 4, 5]},
    ]},
    {"lesson": "geography",
     "student": [
        {"student_id": "6fa0ba0f-bca6-41bb-ac3f-13de2a7bbf2f", "grade": [4, 5, 4]},
        {"student_id": "8f4cfe1f-1f78-4cdc-8cfd-a3406a990b3e", "grade": [3]},
        {"student_id": "be087d42-da91-40b7-88dc-851078d568a0", "grade": [5, 5]},
    ]}
]


def add_student(student: list, last_name: str, first_name: str, klass: str) -> None:
    student.append(
        {
            "id": str(uuid.uuid4()),
            "last_name": last_name,
            "first_name": first_name,
            "klass": klass
        }
    )


def find_student(student: list, last_name: str, first_name: str) -> dict:
    stud = next((stud
                for stud in student
                if stud.get("last_name") == last_name
                and stud.get("first_name") == first_name), None)
    return stud


def add_grade(student: list, journal: list, last_name: str, first_name: str, lesson: str, grade: int) -> None:
    stud = find_student(student=student, last_name=last_name, first_name=first_name)
    if stud:
        less = next((less
                     for less in journal
                     if less.get("lesson") == lesson), None)
        if less:
            les = next((les for les in less.get("student") if les.get("student_id") == stud.get("id")), None)
            les.get("grade").append(grade)


def find_grade_student(student: list, journal: list, last_name: str, first_name: str) -> tuple:
    result = {}
    stud = find_student(student=student, last_name=last_name, first_name=first_name)
    if stud:
        les = (
            (lesson.get("lesson"),
             (next((les
                    for les in lesson.get("student")
                    if les.get("student_id") == stud.get("id")), None)))
            for lesson in journal)
        for item in les:
            result[item[0]] = item[1].get("grade")
    return last_name + " " + first_name, result


print(students)
add_student(student=students, last_name="Testing", first_name="Test", klass="10b")
print(students)
print(find_student(student=students, last_name="qwe", first_name="rty"))

print(journals)
add_grade(student=students, journal=journals, last_name="Petrov", first_name="Ivan", lesson="math", grade=5)
print(journals)

print(find_student(student=students, last_name="Ivanov", first_name="Sergey"))

my_grade = find_grade_student(student=students, journal=journals, last_name="Petrov", first_name="Ivan")

print(f"student: {my_grade[0]}\ngrade: {my_grade[1]}")
add_grade(student=students, journal=journals, last_name="Petrov", first_name="Ivan", lesson="math", grade=3)
add_grade(student=students, journal=journals, last_name="Petrov", first_name="Ivan", lesson="math", grade=5)
add_grade(student=students, journal=journals, last_name="Petrov", first_name="Ivan", lesson="math", grade=4)
add_grade(student=students, journal=journals, last_name="Petrov", first_name="Ivan", lesson="geography", grade=5)
add_grade(student=students, journal=journals, last_name="Petrov", first_name="Ivan", lesson="geography", grade=4)
print(f"student: {my_grade[0]}\ngrade: {my_grade[1]}")
