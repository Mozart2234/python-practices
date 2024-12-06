class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            print(f"You have borrowed {self.title} by {self.author}")
        else:
            print(f"{self.title} by {self.author} is not available")

    def return_book(self):
        if not self.available:
            self.available = True
            print(f"You have returned {self.title} by {self.author}")
        else:
            print(f"{self.title} by {self.author} is already available")


class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print(f"{book.title} by {book.author} is not available")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f"You have not borrowed {book.title} by {book.author}")

    def books_borrowed(self):
        print("Books borrowed:")
        for book in self.borrowed_books:
            print(f"{book.title} by {book.author}")


class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)
        print(f"{book.title} by {book.author} has been added to the library")

    def register_user(self, user):
        self.users.append(user)
        print(f"{user.name} has been added to the library")

    def show_available_books(self):
        if not self.books:
            print("No books available")

        print("Available books:")
        for book in self.books:
            if book.available:
                print(f"{book.title} by {book.author}")


book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("1984", "George Orwell")

user1 = User("Alice", 1)
user2 = User("Bob", 2)

library = Library()
library.add_book(book1)
library.add_book(book2)

user1.borrow_book(book1)
user2.borrow_book(book2)

user2.borrow_book(book2)

user1.books_borrowed()
user2.books_borrowed()

library.show_available_books()

user2.return_book(book2)
user1.return_book(book1)

library.show_available_books()
