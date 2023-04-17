number = int(input("Введи четырех значное число: "))
num_one = number // 1000
num_two = (number // 100) % 10
num_three = (number // 10) % 10
num_four = number % 10
print(num_one, num_two, num_three, num_four)