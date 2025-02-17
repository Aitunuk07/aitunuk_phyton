grade = int(input("Введите вашу оценку за тест (0-100)"))

if grade>= 90:
    homework = input("Вы сдали все домашние задания? (да/нет)").strip().lower()
    if homework == "да":
        print("Отлично! Оценка: А+")
    else:
        print("Хорошая работа, но сдайте все задания! Оценка: А")
elif 80 <= grade <90:
    attendance = input("Вы посещали более 75% занятий? (да/нет)").strip().lower()
    if attendance == "да":
        print("Хорошо! Оценка: В")
    else:
        print("Нужно посещать занятия! Оценка: С")
else:
    print("Старайтесь лучше!")