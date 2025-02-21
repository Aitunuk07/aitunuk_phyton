students = [
 {
     "name": "Alice", 
     "subjects": ("Math", "Physics", "English"), 
     "scores": {"Math": 85, "Physics": 78, "English": 92}},
 {
     "name": "Bob", 
     "subjects": ("Math", "Biology", "English"), 
     "scores": {"Math": 72, "Biology": 88, "English": 80}},
 {
     "name": "Charlie", 
     "subjects": ("Math", "Physics", "Chemistry"), 
     "scores": {"Math": 90, "Physics": 95, "Chemistry": 85}},
]

def display_students(data):
    for student in data:
        name = student["name"]
        subjects = ", ".join(student["subjects"])
        print(f"{name} is enrolled in: {subjects}")
        

        
def get_average_score(name, data):
    for student in data:
        if student["name"] == name:
         x = sum(student["scores"].values())
         y = len(student["scores"])
         return x / y
    return None
 
 
def average_score(student):
     x = sum(student["scores"].values())
     y = len(student["scores"])
     return x / y
        
def find_top_student(students):
    return max(students, key=average_score)["name"]

def failed_students(data, passing_score=50):
    failed = []
    for student in data:
        for score in student["scores"].values():
            if score < passing_score:
                failed.append(student["name"])
                break
    return failed 


def unique_subjects(data):
    subjects = set()
    for student in data:
            subjects.update(student ["subjects"])
            return tuple(subjects)
        


    
    
display_students(students)
print(get_average_score("Alice", students))
print(find_top_student(students))
print(failed_students(students, passing_score=75))
print(unique_subjects(students))