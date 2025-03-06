class Student:
    def __init__(self, name, student_id, grades):
            self.name = name
            self.student_id = student_id
            self.grades = []
            
    def add_grade(self, grade): 
            self.grades.append(grade)
            
    def calculate_average(self):
        return sum(self.grades)/len(self.grades) 

    def get_best_grade(self):
            if not self.grades:
                    return None
            return max(self.grades) 
            
    
    def get_worst_grade(self):
            if not self.grades:
                    return None
            return min(self.grades)
            
             
    def display_info(self):  
        average_grades = self.calculate_average()
        print(f"Student name:  {self.name}")
        print(f"Student ID:  {self.student_id}")
        print(f"Average grades {average_grades}") 
        print(f"Лучшая оценка {self.get_best_grade()}")
        print(f"Худшая оценка {self.get_worst_grade()}")
        print()
   
class StudentManager:
        def __init__ (self):
                self.students=[]
        
        def add_student(self, student: Student):
                self.students.append(student)
                
        def display_all_students(self):
                for student in self.students:
                        student.display_info()
                        
        def get_top_student(self):
                top_student = max(self.students, key = lambda student: student.calculate_average())
                return top_student
        
        def get_lowest_student(self):
                if not self.students:
                        return None
                lowest_student=self.students[0]
                for student in self.students[1:]:
                        if student.calculate_average()<lowest_student.calculate_average():
                                lowest_student=student
                                return lowest_student
                        
                                
                
                
                
student1 = Student("Alice Johnson", 101, 85.0)  
student2 = Student("Bob Smith", 102, 78.5)  
manager = StudentManager()


student1.add_grade(50)
student2.add_grade(45)
student1.add_grade(70)
student2.add_grade(56)
student1.add_grade(90)
student2.add_grade(100)
manager.add_student(student1)
manager.add_student(student2)

student1.display_info()
student2.display_info()
manager.display_all_students()

top_student = manager.get_top_student()
worst_student = manager.get_lowest_student()

if top_student:
        print("Лучший студент: ")
        top_student.display_info()
        
if worst_student:
        print("Студент с худшими оценками: ")
        worst_student.display_info()

