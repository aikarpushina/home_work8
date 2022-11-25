"""
Создать информационную систему позволяющую работать с учениками школы
Минимальные требования:
1 - учитель добавление ученика, добавление оценки за предмет ученику
2 - ученик Поиск по фамилии ученика
"""
import students
import teacher
import libs

student = [
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

print(students)
teacher.add_student(student=student, last_name="Testing", first_name="Test", klass="10b")
print(students)
print(libs.find_student(student=student, last_name="qwe", first_name="rty"))

print(journals)
teacher.add_grade(student=student, journal=journals, last_name="Petrov", first_name="Ivan", lesson="math", grade=5)
print(journals)

print(libs.find_student(student=student, last_name="Ivanov", first_name="Sergey"))

my_grade = students.find_grade_student(student=student, journal=journals, last_name="Petrov", first_name="Ivan")

print(f"student: {my_grade[0]}\ngrade: {my_grade[1]}")
teacher.add_grade(student=student, journal=journals, last_name="Petrov", first_name="Ivan", lesson="math", grade=3)
teacher.add_grade(student=student, journal=journals, last_name="Petrov", first_name="Ivan", lesson="math", grade=5)
teacher.add_grade(student=student, journal=journals, last_name="Petrov", first_name="Ivan", lesson="math", grade=4)
teacher.add_grade(student=student, journal=journals, last_name="Petrov", first_name="Ivan", lesson="geography", grade=5)
teacher.add_grade(student=student, journal=journals, last_name="Petrov", first_name="Ivan", lesson="geography", grade=4)
my_grade = students.find_grade_student(student=student, journal=journals, last_name="Petrov", first_name="Ivan")
print(f"student: {my_grade[0]}\ngrade: {my_grade[1]}")

my_test = students.find_grade_student(student=student, journal=journals, last_name="Testing", first_name="Test")
print(f"student: {my_test[0]}\ngrade: {my_test[1]}")
teacher.add_grade(student=student, journal=journals, last_name="Testing", first_name="Test", lesson="math", grade=3)
teacher.add_grade(student=student, journal=journals, last_name="Testing", first_name="Test", lesson="music", grade=5)
teacher.add_grade(student=student, journal=journals, last_name="Testing", first_name="Test", lesson="math", grade=5)
teacher.add_grade(student=student, journal=journals, last_name="Testing", first_name="Test", lesson="geography", grade=4)
my_test = students.find_grade_student(student=student, journal=journals, last_name="Testing", first_name="Test")
print(f"student: {my_test[0]}\ngrade: {my_test[1]}")

t = students.find_grade_student(student=student, journal=journals, last_name="qwe", first_name="asd")

print(f"student: {t[0]}\ngrade: {t[1]}")
