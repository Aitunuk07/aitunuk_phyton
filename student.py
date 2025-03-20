class Student:
    def _init_(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def _str_(self):
        return f"{self.student_id}, {self.name}, {self.age}, {self.grade}"

    def to_conversion(self):
        
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "grade": self.grade
        }