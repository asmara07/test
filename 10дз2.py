class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self):
        print(f"Марка: {self.brand}, Год выпуска: {self.year}")
class Car(Vehicle):
    def __init__(self, brand, year, doors):
        super().__init__(brand, year)
        self.doors = doors
    def display_info(self):
        super().display_info()
        print(f"Количество дверей: {self.doors}")
class Motorcycle(Vehicle):
    def __init__(self, brand, year, engine_type):
        super().__init__(brand, year)
        self.engine_type = engine_type
    def display_info(self):
        super().display_info()
        print(f"Тип двигателя: {self.engine_type}")
def main():
    car = Car("Cobalt", 2022, 4)
    motorcycle = Motorcycle("Vavilon", 2021, "V-twin")
    print("Информация об автомобиле:")
    car.display_info()
    print("\nИнформация о мотоцикле:")
    motorcycle.display_info()
if main  == "main":
    main()
    print()



