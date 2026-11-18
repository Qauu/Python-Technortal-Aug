from data import library,Book

def view_books():
    if len(library) == 0:
        print("No books available in the library.")
    else:
        print("{:<10} {:<10} {:<10} {:<20} {:<15}".format('Book ID', 'Title', 'Author', 'ISBN', 'Published Year'))
        print("="*90)

        for book in library:
            print("{:<10} {:<10} {:<10} {:<20} {:<15}".format(book.book_id, book.title, book.author,book.isbn, book.published_year))
    print()

def add_book():
    book_id = input("Enter the Book ID: ")
    for book in library:
     if book.book_id == book_id:
        print("Book with this ID already exists.")
        break
     else:
        title = input("Enter the book title: ")
        author = input("Enter the book author: ")
        isbn = input("Enter the book ISBN: ")
        published_year = input("Enter the book published year: ")
        new_book=Book(book_id,title,author,isbn,published_year)
        library.append(new_book)
        print("Book added successfully.\n")
        

def remove_book():
    book_id = input("Enter the Book ID to remove: ")
    for book in library:
     if book.book_id == book_id:
        library.remove(book)
        print("Book removed successfully.\n")
        break
     else:
        print("Book not found.\n")

def update_book():
    book_id = input("Enter the Book ID to update: ")
    for book in library:
        if book.book_id==book_id:
            book.title = input("Enter the book title: ")
            book.author = input("Enter the book author: ")
            book.isbn = input("Enter the book ISBN: ")
            book.published_year = input("Enter the book published year: ")
            print("Book updated successfully.\n")
            break
        else:
             print("Book with this ID already exists.")