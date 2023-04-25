size = int(input("Введите площядь квартиры: "))
price = int(input("Введите цену квартиры (цены в миллионах): "))
if (size >= 100 and price <= 10) or (size >= 80 and price <= 7):
    print("Квартира подходит!!!")
else:
    print("Не подходит")
