import math 

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Ошибка: деление на ноль"
    
def percent( x, y):
    return x * (y / 100)

def sqrt(x):  
    return math.sqrt(x)

def pow( x, y):
    return x ** y

def discriminant(a, b, c):  
    return b**2 - 4*a*c




print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")
print("5. Процент")
print("6. Корень")
print("7. Cтепень")

choice = input("Введите номер операции (1/2/3/4/5/6/7/8): ")

if choice != '8':  
 x = float(input("Введите первое число: "))
if choice != '6':  
 if choice != '8':  
  y = float(input("Введите второе число: "))

if choice == '1':
    print(f"{x} + {y} = {add(x, y)}")
elif choice == '2':
    print(f"{x} - {y} = {subtract(x, y)}")
elif choice == '3':
    print(f"{x} * {y} = {multiply(x, y)}")
elif choice == '4':
    print(f"{x} / {y} = {divide(x, y)}")
elif choice == '5':
     print(f"({x} * {y} / 100)= {percent(x, y)}")
elif choice == '6':
    print(f"√{x} = {sqrt(x)}")
elif choice == '7':
     print(f"{x} ** {y} = {pow(x, y)}") 
     
     
elif choice == '8':
    a = float(input("Введите коэффициент a: "))
    b = float(input("Введите коэффициент b: "))
    c = float(input("Введите коэффициент c: "))
    D = discriminant(a, b, c)
    print(f"Дискриминант D = {D}")
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        print(f"Корни уравнения: x1 = {x1}, x2 = {x2}")
    elif D == 0:
        x1 = -b / (2 * a)
        print(f"Единственный корень уравнения: x1 = {x1}")
    else:
        print("Корней нет (или они комплексные).")
else:
    print("Неверный выбор!")