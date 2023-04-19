hour_count = int(input("Введи кол-во отработанных часов: "))
credit_balance = int(input("Введите остаток по кредиту: "))
food_price = int(input("Введите траты на еду : "))
salary = 200 * hour_count / 2 ** 3 + hour_count
if salary >= hour_count + credit_balance + food_price:
    print("Денег хватает ложись спать")
else:
    print("Работай солнце еще высоко !!!") 
