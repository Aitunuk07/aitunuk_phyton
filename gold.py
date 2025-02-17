print("золото")
print("серебро")
print("обычный")

membership = str(input("Введите тип членства: "))
amount = float(input("Выберите сумму покупки: "))

if membership =="золото":

    if amount > 100:
        print("скидка 20%")
        discount = 0.2 
elif amount <100:
        print("скидка 10%") 
        discount=0.1
        
if membership =="серебро":
    
    if amount > 100: 
       
       discount = 0.15 
elif amount <100: 
        print("скидка 5%")
        discount = 0.05
        
        
if membership =="обычный":    
     if amount > 100:          
        discount=0.05 
elif amount <100:
         print("скидка не доступна")
         discount=0
         
       
price =  amount *(1-discount)  

print(f"Сумма после скидки:{price:.2f}")