exp = int(input("Введите кол-во опыта: "))
base_lvl = 1
if exp >= 5000:
    base_lvl += 3
elif exp >= 2500:
    base_lvl += 2
elif exp >= 1000:
    base_lvl +=1
print("You lvl =",base_lvl)
