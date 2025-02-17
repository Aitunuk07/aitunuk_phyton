num = int(input("Введите число: "))

if num % 2 == 0:
    if num % 4 == 0:
        print("Число делится на 4")
    else:
        print("Обычное чётное число")
else:
    if num % 5 == 0:
        print("Число делится на 5")
    else:
        print("Просто нечётное число")