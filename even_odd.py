#разделение четных и нечетных чисел
numbers = [12, 7, 34, 23, 45, 66, 89, 90, 41, 55]
even_numbers = []
odd_numbers = []

for num in numbers:
    if num % 2 == 0: 
        even_numbers.append(num)
    else:
        odd_numbers.append(num)
        
print(even_numbers)
print(odd_numbers)