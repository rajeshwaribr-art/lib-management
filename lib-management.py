class Book:
    def _init_(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def _str_(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"{self.title} by {self.author} [{status}]"


class Library:
    def _init_(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added successfully.")

    def view_books(self):
        if not self.books:
            print("No books in the library.")
            return
        print("\nBooks in Library:")
        for idx, book in enumerate(self.books, 1):
            print(f"{idx}. {book}")

    def borrow_book(self, book_title):
        for book in self.books:
            if book.title.lower() == book_title.lower():
                if not book.is_borrowed:
                    book.is_borrowed = True
                    print(f"You have borrowed '{book.title}'.")
                    return
                else:
                    print(f"Sorry, '{book.title}' is already borrowed.")
                    return
        print(f"Book '{book_title}' not found.")

    def return_book(self, book_title):
        for book in self.books:
            if book.title.lower() == book_title.lower():
                if book.is_borrowed:
                    book.is_borrowed = False
                    print(f"Thank you for returning '{book.title}'.")
                    return
                else:
                    print(f"'{book.title}' was not borrowed.")
                    return
        print(f"Book '{book_title}' not found.")


def main():
    library = Library()
    
    while True:
        print("\n=== Library Management System ===")
        print("1. Add Book")
        print("2. View Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            book = Book(title, author)
            library.add_book(book)
        elif choice == "2":
            library.view_books()
        elif choice == "3":
            title = input("Enter book title to borrow: ")
            library.borrow_book(title)
        elif choice == "4":
            title = input("Enter book title to return: ")
            library.return_book(title)
        elif choice == "5":
            print("Exiting Library System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if _name_ == "_main_":
    main()