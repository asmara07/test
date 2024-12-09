
class Card :
    def __init__(self, card_number, balance = 0 ):
        self.card_number = card_number
        self.balance = balance
    def add_balance(self, money ):
        self.balance += money
card_1 = Card(1)
card_2 = Card(2)
card_1.add_balance(100)
print(card_1.balance)




class BankAccount:
    def init(self, name, balance=0):
        self.holder_name = name
        self.balance = balance
    def deposit(self, money):
        self.balance += money
        print("Баланс пополнен")
    def cash(self, money):
        if self.balance >= money:
            self.balance -= money
            print("Средства были сняты")
        else:
            print("Недостаточно средств")
    def my_balance(self):
        print(f"Ваш баланс: {self.balance} сум")

user1 = BankAccount(name=input("Введите своё имя"))
while True:
    menu = input("Выберите действие:\n"
                 "1-Пополнить баланс\n"
                 "2- Снять деньги\n"
                 "3- Посмотреть баланс: ")
    if menu == "1":
        user1.deposit(money=int(input("Введите сумму: ")))
    elif menu == "2":
        user1.cash(money=int(input("Введите сумму: ")))
    elif menu == "3":
        user1.my_balance()
    else:
        print("такого действия нет")