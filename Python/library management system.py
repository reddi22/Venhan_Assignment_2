class Book:
    def __init__(self, title, author, isbn, genre, quantity):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.quantity = quantity

    def update_details(self, title=None, author=None, quantity=None):
        if title:
            self.title = title
        if author:
            self.author = author
        if quantity is not None:
            self.quantity = quantity

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Genre: {self.genre}, Quantity: {self.quantity}"

class Borrower:
    def __init__(self, name, contact, membership_id):
        self.name = name
        self.contact = contact
        self.membership_id = membership_id

    def update_details(self, name=None, contact=None):
        if name:
            self.name = name
        if contact:
            self.contact = contact

    def __str__(self):
        return f"Name: {self.name}, Contact: {self.contact}, Membership ID: {self.membership_id}"

class Library:
    def __init__(self):
        self.books = {}
        self.borrowers = {}
        self.borrowed_books = {}
        self.current_day = 0

    # Book Management
    def add_book(self, book):
        self.books[book.isbn] = book

    def remove_book(self, isbn):
        if isbn in self.books:
            del self.books[isbn]

    def update_book(self, isbn, title=None, author=None, quantity=None):
        if isbn in self.books:
            self.books[isbn].update_details(title, author, quantity)

    # Borrower Management
    def add_borrower(self, borrower):
        self.borrowers[borrower.membership_id] = borrower

    def remove_borrower(self, membership_id):
        if membership_id in self.borrowers:
            del self.borrowers[membership_id]

    def update_borrower(self, membership_id, name=None, contact=None):
        if membership_id in self.borrowers:
            self.borrowers[membership_id].update_details(name, contact)

    # Book Borrowing and Returning
    def borrow_book(self, membership_id, isbn, days=14):
        if membership_id in self.borrowers and isbn in self.books:
            book = self.books[isbn]
            if book.quantity > 0:
                book.quantity -= 1
                due_date = self.current_day + days
                self.borrowed_books[(membership_id, isbn)] = due_date
                return f"Book borrowed successfully! Due date: {due_date} days from now"
            else:
                return "Book not available"
        return "Invalid borrower ID or book ISBN"

    def return_book(self, membership_id, isbn):
        if (membership_id, isbn) in self.borrowed_books:
            book = self.books[isbn]
            book.quantity += 1
            del self.borrowed_books[(membership_id, isbn)]
            return "Book returned successfully"
        return "Book not borrowed"

    # Book Search and Availability
    def search_books(self, title=None, author=None, genre=None):
        results = []
        for book in self.books.values():
            if (title and title.lower() in book.title.lower()) or \
               (author and author.lower() in book.author.lower()) or \
               (genre and genre.lower() in book.genre.lower()):
                results.append(book)
        return results

    def display_books(self):
        for book in self.books.values():
            print(book)

    def display_borrowers(self):
        for borrower in self.borrowers.values():
            print(borrower)

    # Advance the current day
    def advance_day(self, days=1):
        self.current_day += days

# Example Usage:
if __name__ == "__main__":
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
   
#output:
 
#Book borrowed successfully! Due date: 14 days from now
#Book returned successfully
#Title: A Suitable Boy, Author: Vikram Seth, ISBN: 9640739947, Genre: Fiction, Quantity: 3
#Title: Midnight's Children, Author: F. Salman Rushdie, ISBN: 8331818372, Genre: Fiction, Quantity: 2
#Title: A Suitable Boy, Author: Vikram Seth, ISBN: 9640739947, Genre: Fiction, Quantity: 3
#Title: The White Tiger, Author: Aravind Adiga, ISBN: 9515859770, Genre: Fiction, Quantity: 4
#Title: Train to Pakistan, Author: Khushwant Singh, ISBN: 9287342726, Genre: Historical Fiction, Quantity: 5
#Name: Ramu, Contact: Ramu@gmail.com, Membership ID: B1
#Name: Seenu, Contact: Seeu@gmail.com, Membership ID: B2
#Name: Sita, Contact: Sita@gmail.com, Membership ID: B3