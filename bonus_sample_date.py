#Bonus sample date
library_books = {
    "B001": {"title": "Основы Python", "borrower": "Алиса", "due_date": -5, "fine_rate": 0.50},
    "B002": {"title": "Наука о данных", "borrower": "Боб", "due_date": 3, "fine_rate": 0.75},
    "B003": {"title": "Введение в ИИ", "borrower": None, "due_date": 0, "fine_rate": 0.25},
    "B004": {"title": "Алгоритмы", "borrower": "Алиса", "due_date": 2, "fine_rate": 1.00}
}

def calculate_fine_and_status(book):
    due_date = book["due_date"]
    fine_rate = book["fine_rate"]
    borrower = book["borrower"]

    if borrower is None:
        return "Доступна", 0.00
    elif due_date >= 0:
        return "В срок", 0.00
    else:
        days_overdue = -due_date  
        fine = days_overdue * fine_rate
        return "Просрочена", fine

def generate_report(library_books):
    borrower_fines = {}
    for book_id, book in library_books.items():
        status, fine = calculate_fine_and_status(book)
        borrower = book["borrower"]

        
        if borrower is not None:
            if borrower in borrower_fines:
                borrower_fines[borrower] += fine
            else:
                borrower_fines[borrower] = fine

        print(f"Книга {book_id}: {book['title']}, Заемщик: {borrower if borrower else 'Нет'}, Статус: {status}, Штраф: ${fine:.2f}")

    if borrower_fines:
        max_fine_borrower = max(borrower_fines, key=borrower_fines.get)
        max_fine = borrower_fines[max_fine_borrower]
        print(f"Заемщик с наибольшими штрафами: {max_fine_borrower}, Общий штраф: ${max_fine:.2f}")
    else:
        print("Нет заемщиков с штрафами.")

generate_report(library_books)