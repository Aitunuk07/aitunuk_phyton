#bonus challenge 
scores = [85, 72, 90, 68, 47, 95, 80, 77, 55, 89]
grades = []
even_count = 0
odd_count = 0
def get_letter_grade(score): 
    if score >= 90:
        return "A", "Сдал"
    elif score >= 80:
        return "B", "Сдал"
    elif score >= 70:
        return "C", "Сдал"
    elif score >= 60:
        return "D", "Сдал"
    else:
        return "F", "Не сдал"
    
for score in scores:
    letter_grade, status = get_letter_grade(score)
    grades. append ((score, letter_grade, status))
    if score % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print ("Результаты оценок:")

for score, grade, status in grades:
    print(f"Балл: {score} → Оценка: {grade} ({status})")
print (f"Четных оценок: {even_count}")
print (f"Нечетных оценок: {odd_count}")