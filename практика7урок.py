clients = {}
opened_rooms = [i for i in range(1,11)]
closed_rooms = []

def check_in(name,room):
    clients[name] = room
    opened_rooms.remove(room)
    closed_rooms.append(room)

def check_out(name):
    closed_rooms.remove(clients[name])
    opened_rooms.append(clients[name])
    clients.pop(name)

def show_rooms():
    return closed_rooms





while True :
    choice = input("что хотите сделать? ")
    if choice.lower() == 'добавить':
        name = input('имя клиента : ')
        print(opened_rooms)
        room = int(input('номер: '))
        check_in(name, room )
        print("готово")
    elif choice.lower() == 'удалить':
        name = input('имя клиента :')
        check_out(name)
        print('готово')
    elif choise.lower











