first_number = int(input("Введи первое число: "))
second_number = int(input("Введи второе число: "))
third_number = int(input("Введи третье число: "))
if first_number != second_number != third_number:
    print("0")
elif first_number == second_number == third_number:
    print("3")
else:
    print("2")

# Неправильно работает программа
# Введи первое число: 2
# Введи второе число: 1
# Введи третье число: 2
# 0