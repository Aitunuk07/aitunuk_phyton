class Student:
    def __init__(self, name, student_id, grades):
            self.name = name
            self.student_id = student_id
            self.grades = []
            
    def add_grade(self, grade): 
            self.grades.append(grade)
            
    def calculate_average(self):
        return sum(self.grades)/len(self.grades)
             
        
    def display_info(self):  
        average_grades = self.calculate_average()
        print(f"Student name:  {self.name}")
        print(f"Student ID:  {self.student_id}")
        print(f"Average grades {average_grades}") 
        
        
student1 = Student("Alice Johnson", 101, 85.0)  
student2 = Student("Bob Smith", 102, 78.5)  

student1.add_grade(50)
student2.add_grade(45)
student1.add_grade(70)
student2.add_grade(56)
student1.add_grade(90)
student2.add_grade(100)

student1.display_info()
student2.display_info()