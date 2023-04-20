# Перечитай условие

cube_guest = int(input("Кибук гостя: "))
cube_master = int(input("Кибик хозяина: "))
if cube_master >= cube_guest:
    print(cube_master - cube_guest,"Гость платит!!!")
else:
    print(cube_master + cube_guest,"Хозяин платит!!!")
