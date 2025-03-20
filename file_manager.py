import json
from student import Student

FILE_NAME = "students.json"

def save_students(students):
   
    students_data = []

    for student in students:
        students_data.append(student.to_dict())

    with open(FILE_NAME, 'w', encoding='utf-8') as file:
        json.dump(students_data, file, ensure_ascii=False, indent=4)

def load_students():
    students = []
    try:
        with open(FILE_NAME, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for student_data in data:
                students.append(Student(
                    student_data["student_id"],
                    student_data["name"],
                    student_data["age"],
                    student_data["grade"]
                ))
    except FileNotFoundError:
        pass 