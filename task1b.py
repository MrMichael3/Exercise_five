### implement class Book here ###
class Book:
    isbn_counter = 9780000000000
    used_isbn = []

    def __init__(self, title, author, isbn=None):

        self.title = title
        self.author = author
        if self.check_isbn(str(isbn)):
            self.isbn = isbn
        else:
            self.isbn = self.generate_isbn()

    @staticmethod
    def generate_isbn():
        while Book.isbn_counter in Book.used_isbn:
            Book.isbn_counter += 1
        Book.used_isbn.append(Book.isbn_counter)
        return Book.isbn_counter

    @staticmethod
    def check_isbn(isbn):
        if len(isbn) == 13 and isbn.isdigit() and isbn[:3] == "978":
            Book.used_isbn.append(isbn)
            return True
        else:
            return False

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_isbn(self):
        return self.isbn


################################################################################
  ### test cases ###

book1 = Book("Harry Potter and the Philosopher's Stone", "J. K. Rowling",
             9780747532743)
book2 = Book("My Story", "Max Muster")
book3 = Book("My Story Part 2", "Max Muster", 970)

print(book1.get_isbn())  # should print: 9780747532743
print(book1.get_title())  # should print: Harry Potter and the Philosopher's Stone
print(book1.get_author())  # should print: J. K. Rowling

print(book2.get_isbn())  # should print: 9780000000000

print(book3.get_isbn())  # should print: 9780000000001
