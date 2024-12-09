
products = {
    1: {"name": "Торт", "price": 50000},
    2: {"name": "Пирожное", "price": 15000},
    3: {"name": "Печенье", "price": 5000}}

cart = {}
def show_products():
    print("\nДоступные товары:")
    for id, details in products.items():
        print(f"{id}, {details['name']} - {details['price']} сумм")

def add_to_cart(product_id, quantity):
    if product_id in products:
        cart[product_id] = cart.get(product_id, 0) + quantity
        print(f"Добавлено: {products[product_id]['name']} ({quantity} шт.)")
    else:
        print("Такого товара нет.")

def remove_from_cart(product_id):
    if product_id in cart:
        del cart[product_id]
        print("Товар удалён из корзины.")
    else:
        print("Товар не найден в корзине.")

def show_cart():
    if not cart:
        print("\nКорзина пуста.")
    else:
        print("\nСодержимое корзины:")
        total = 0
        for id, qty in cart.items():
            name = products[id]["name"]
            price = products[id]["price"]
            total += qty * price
            print(f"{name}: {qty} шт.{qty * price} сумм.")
        print(f"Итог: {total} сумм.")

while True:
    print("1. Показать товары\n2. Добавить в корзину\n3. Удалить из корзины\n4. Показать корзину\n5. Выйти")
    choice = input("Выберите действие: ")

    if choice == "1":
        show_products()
    elif choice == "2":
        product_id = int(input("Введите ID товара: "))
        quantity = int(input("Введите количество: "))
        add_to_cart(product_id, quantity)
    elif choice == "3":
        product_id = int(input("Введите ID товара: "))
        remove_from_cart(product_id)
    elif choice == "4":
        show_cart()
    elif choice == "5":
        print("До свидания!")
        break
    else:
        print("Неверный выбор, попробуйте снова.")




