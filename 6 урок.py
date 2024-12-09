all_products = {"картофель": 10, "морковь": 30}
while True:
    menu = input("Что хотите сделать?\n1- Добавить\n2- Продукты:")
    if menu.lower() == "добавить":
        product = input("Введите название продукта: ")
        count = int(input("Введите количество продукта: "))
        if product in all_products.keys():
            all_products[product] += count
            print("Количество продукта изменено")
        else:
            all_products[product] = count
            print("Продукт добавлен")
    elif menu.lower() == "продукты":
        number = 0
        for name, count in all_products.items():
            number += 1
            print(f"{number}. {name} = {count} кг")





