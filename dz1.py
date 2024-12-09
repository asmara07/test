
kontakts = ["Мария", "Олег", "Алексей", "Павел", "Дарья", "Олег" ]

if kontakts == input("Выберите действие : 1-добавить, контакт, 2-удалить контакт, 3-изменить контакт"):
    print("kontakts")

elif kontakts == "1":
    name = input("введите название контакта :")
    kontakts.extend({name})
    print("контакт {name} добавлен")
elif kontakts == "2":
    name = input("введите название контакта :")
    kontakts.remove({name})
    print("контакт {name} удален")
elif kontakts == "3":
    name = input("введите название контакта :")
    kontakts.insert({name})
    print("контакт {name} изменен")




