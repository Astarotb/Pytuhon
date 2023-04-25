chair_one = int(input("Введи стоимость стула в туалет: "))
chair_two = int(input("Введи стоимость стула на кухню: "))
chair_three = int(input("Введи стоимость стула в спальню: "))
price_all_chair = chair_one + chair_two + chair_three
if chair_one + chair_two + chair_three > 10000:
    print(price_all_chair * 10 / 100)
else:
    print("Вы укладываетесь в 10000")
