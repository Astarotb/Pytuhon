points_rus = int(input("Введите кол-во баллов по русскому языку: "))
points_mat = int(input("Введите кол-во баллов по математике: "))
points_info = int(input("Введите кол-во баллов по информатике: "))
if points_info + points_mat + points_rus >= 270:
    print("Поздравляем вы поступили на бюджет!")
else:
    print("Вы тупой будите учиться за деньги ! lol")