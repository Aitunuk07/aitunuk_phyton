#Game
print("Попробуй угадать число!")
x = int(input("Число - "))

if x == 20:
    print("Правильно!")
elif x > 14 and x < 22:  
    print("Горячо")
else:
    print("Холодно")