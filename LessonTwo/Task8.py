# Можно сделать короче (3)

x = int(input("Введи первое число: "))
y = int(input("Введи второе число: "))
z = int(input("Введи третье число: "))

if x > y:
    g_max = x
else:
    g_max = y    
if g_max > z:
    print(g_max)
else:
    print(z)
