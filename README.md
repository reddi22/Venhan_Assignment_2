# Library Management System

This is a simplified library management system implemented in Python using Object-Oriented Programming (OOP) concepts.

## Features

- **Book Management**:
  - Add new books to the library database.
  - Update existing book information.
  - Remove books from the library database.

- **Borrower Management**:
  - Add new borrowers to the library system.
  - Update borrower information.
  - Remove borrowers from the system.

- **Book Borrowing and Returning**:
  - Borrow books by linking the borrower's membership ID to the book details.
  - Record the due date for each borrowed book.
  - Handle overdue books.
  - Return books and update the database accordingly.

- **Book Search and Availability**:
  - Search for books by title, author, or genre.
  - Display the availability status of each book.

## Usage

Run the `library_management.py` file to interact with the library system.

## Example

```python
from library_management import Library, Book, Borrower

library = Library()

# Adding books
book1 = Book("Midnight's Children", "F. Salman Rushdie", "8331818372", "Fiction", 2)
book2 = Book("A Suitable Boy", "Vikram Seth", "9640739947", "Fiction", 3)
book3 = Book("The White Tiger", "Aravind Adiga", "9515859770", "Fiction", 4)
book4 = Book("Train to Pakistan", "Khushwant Singh", "9287342726", "Historical Fiction", 5)
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)

# Adding borrowers
borrower1 = Borrower("Ramu", "Ramu@gmail.com", "B1")
borrower2 = Borrower("Seenu", "Seeu@gmail.com", "B2")
borrower3 = Borrower("Sita", "Sita@gmail.com", "B3")
library.add_borrower(borrower1)
library.add_borrower(borrower2)
library.add_borrower(borrower3)

# Borrowing and returning books
print(library.borrow_book("B1", "8331818372"))
library.advance_day(15)  # Advancing the day by 15 days
print(library.return_book("B1", "8331818372"))

# Searching books
results = library.search_books(author="Vikram Seth")
for book in results:
    print(book)

# Displaying all books and borrowers
library.display_books()
library.display_borrowers()
