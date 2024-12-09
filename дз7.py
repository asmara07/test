#school managment system

students = {}
opened_class = [i for i in range(1, 4)]
closed_class = []


def check_in(name, blok):
    students[name] = blok
    opened_class.remove(blok)
    closed_class.append(blok)


def check_out(name):
    closed_class.remove(students[name])
    opened_class.append(students[name])
    students.pop(name)


def show_class():
    return closed_class

while True:
    choice = input('Что хотите сделать? ')
    if choice.lower() == 'добавить':
        name = input('Имя студента : ')
        print(opened_class)
        blok = int(input('Класс: '))
        check_in(name, blok)
        print('Готово студент добавлен!')
    elif choice.lower() == 'удалить':
        name = input('Имя студента : ')
        check_out(name)
        print('Готово студент удален!')
    elif choice.lower() == 'номера':
        print(show_class())




















