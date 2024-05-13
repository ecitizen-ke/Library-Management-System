import json


# Represents a book with attributes title, author
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.checked_out = False

    def __str__(self):
        return f"{self.title} by {self.author}"


# Manages a collection of books with different methods
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print(f"Book '{title}' added successfully.")

    def display_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            for book in self.books:
                print(book)

    def search_book(self, title):
        found_books = [
            book for book in self.books if title.lower() in book.title.lower()
        ]
        if found_books:
            for book in found_books:
                print(book)
        else:
            print("Book not found")

    def check_out_book(self, title):
        for book in self.books:
            if title.lower() == book.title.lower() and not book.checked_out:
                book.checked_out = False
                print(f"Book '{title}' checked out successfully.")
                return
        print("Book not available for checkout.")

    def display_check_out_books(self):
        checked_out_books = [book for book in self.books if book.checked_out]
        if checked_out_books:
            print("Checked out books:")
            for book in checked_out_books:
                print(book)
        else:
            print("No books are currently checked out.")

    def return_book(self, title):
        for book in self.books:
            if title.lower() == book.title.lower() and book.checked_out:
                book.checked_out = False
                print(f"Book '{title} returned successfully.")
                return
        print("Book cannot be returned.")

    def save_library_to_file(self, filename):
        filename = "library.json"
        with open(filename, "w") as filename:
            json.dump(
                [vars(book) for book in self.books], filename
            )  # Saves the library data (book details) to a JSON file
        print("Library data saved successfully.")

    def load_library_from_file(self, filename):
        with open(filename, "r") as file:
            data = json.load(
                file
            )  # Saves the library data (book details) to a JSON file
            self.books = [Book(**book_data) for book_data in data]
        print("Library data loaded successfully.")


# Contains a loop for displaying a menu and handling user input
def main():
    library = Library()
    while True:
        print("\nLibrary Management System:")
        print("1. Add a new book")
        print("2. Display all books")
        print("3. Search for a book")
        print("4. Check out a book")
        print("5. Return a book")
        print("6. Display checked_out books")
        print("7. Save library data")
        print("8. Load library data")
        print("9. Delete book")
        print("10. Exit Library")

        choice = input("Enter your choice:")

        if choice == "1":
            title = input("Enter title of the book: ")
            author = input("Enter author of the book: ")
            library.add_book(title, author)
        elif choice == "2":
            library.display_books()
        elif choice == "3":
            title == input("Enter title to search: ")
            library.search_book(title)
        elif choice == "4":
            title == input("Enter title of the book to check out: ")
            library.check_out_book(title)
        elif choice == "5":
            title == input("Enter title of the book to return: ")
            library.return_book(title)
        elif choice == "6":
            library.display_checked_out_books()
        elif choice == "7":
            filename = input("Enter file name to save data: ")
            library.save_library_file(filename)
        elif choice == "8":
            filename = input("Enter file name to load data: ")
            library.load_library_from_file(filename)
        elif choice == "9":
            print("Exit from the library")
        else:
            print("Invalid choice.Please enter a number from 1 to 9")


if __name__ == "__main__":
    main()
