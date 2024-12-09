def create_list():
    my_list = []
    return my_list
a = create_list()
a.append(1)
print(a)

 def comment(name, text, likes):
      return (f"Автор коммента: {name}\n"
              f"Текст коммента : {text}\n"
              f"Лайки:{likes}")
  print(comment('lilis23', 'wow ', 100))



def spam1(*args):
    return args

print(spam1(1,2,3,'hello'))#(1,2,3,'hello')



def spam1(**kwargs):
    for k,v in kwargs.items:
        return k,v

print(spam1(name='my1', age=23))

