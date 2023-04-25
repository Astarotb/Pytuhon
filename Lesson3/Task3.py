number_list = int(input("Введи номер в списке: "))
number_of_points = int(input("Введи кол-во баллов: "))
if (number_list <= 10) and (number_of_points >= 290):
    print("Вы поступили поздравляем !!!\nИ как бонус вам будет стипендия!!!")
elif number_of_points < 290:
    print("Вы поступили поздравляем\nНо без стипендии")
else:
    print("Вы не поступили")
