class Animal :
    def make_sound(self):
        print("издает звук")
some_animal = Animal()
some_animal.make_sound()
class Horse(Animal):
    def skakat(self):
        print("лошадь скачет")
horse1 = Horse()
horse1.make_sound = Horse()



class Dad :
    def rabotat(self):
        print("работает")

class Mom :
    def gotovit(self):
        print("готовить")

class Child(Dad,Mom):
    def uchitsa(self):
        print("учится")
child1 = Child()
child1.rabotat()
child1.gotovit()


class Player:
    def __init__(self, name, number):
        self.name = name
        self.number = number
    def passing(self):
        print("игрок дал пас")
    def shoot(self):
        print("игрок пнул мяч")
class Goalkeeper(Player):
    def __init__(self, name, number, height):
        super().__init__(name, number)
        self.height = height
    def save(self):
        print("голкипер поймал мяч в руки")
class Forward(Player):
    def __init__(self, name, number, speed):
        super().__init__(name, number)
        self.speed = speed
    def dribling(self):
        print("ловко управляет мячем")
class Defender(Player):
    def __init__(self, name, number, stamina):
        super().__init__(name, number)
        self.stamina = stamina
    def tackle(self):
        print("сделал подкат")



workers = {}
class Worker:
    def __init__(self, name, job):
        self.name = name
        self.job = job
        workers[name] = job
    def work(self):
        print("начал работать")
class Manager(Worker):
    def __init__(self, name, job, password):
        super().__init__(name, job)
        self.password = password
        workers[name] = job
    def all_info(self, password):
        if password == self.password:
            number = 0
            for n,j in workers.items():
                number += 1
                print(f"{number}. {n} - {j}")
        else:
            print("в доступе отказано")

programmer = Worker("Олег", 'программист')
sisadmin = Worker("Иван", 'сисадмин')
manager1 = Manager("Маша", "менеджер", 123)
manager1.all_info(123)
