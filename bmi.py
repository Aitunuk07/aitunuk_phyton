#TEst 
height=float(input("Введите ваш рост: "))
weight=float(input("Введите ваш вес: "))

bmi=weight/(height / 100) **2

print(bmi)

if bmi <18.5:
    print("underweight") 
elif bmi <24.9:
    print("normal weight")
elif bmi <29.9:
    print("overweight")
elif bmi <34.9:
  print("obesity class I")
elif bmi <39.9:
 print("obesity class II")