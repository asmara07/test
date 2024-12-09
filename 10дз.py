class Animal:
    def make_sound(self):
        return
class Dog(Animal):
    def make_sound(self):
        return "Гав-гав"
class Cat(Animal):
    def make_sound(self):
        return "Мяу"
class Cow(Animal):
    def make_sound(self):
        return "Мууу"

def __init__(self,dog,cat,cow):
    self.dog = Dog()
    self.cat = Cat()
    self.cow = Cow()


    dog.make_sound()
    print("Собака произносит:")
    cat.make_sound()
    print("Кошка произносит:")
    cow.make_sound()
    print("Корова произносит:")
