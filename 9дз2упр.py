class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_info(self):
        print(f"Имя: {self.name}, возраст: {self.age}")

person = Person("Мария", 19)
person2 = Person ("Лиана", 23)
person3 = Person("Максим", 26)

person.display_info()
person2.display_info()
person3.display_info()





        