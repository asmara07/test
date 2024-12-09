class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
         self.books.append(book)
         print(f"книга '{book}' добавлена в библиотеку ")

    def remove_book(self,book):
     if book in self.books:
      self.books.remove(book)
      print(f"книга'{book}' удалена из библиотеки ")
     else:
      print(f" книга '{book}' не найдена в библиотеке")
    def show_books(self):
     if self.books:
         print("список книг в библиотеке: ")
         for book in self.books :
                print(f"{book}")
     else:
                print("библиотека и пуста")