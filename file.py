from data import Book
def load_data():
    books=[]
    with open('books.txt','r')as file:
        for line in file:
            title,author,year=line.strip().split(',')
            book=Book(title,author,year)
            book.append(book)
        return books

def save_data(books):
    with open('books.txt','w')as file:
        for book in books:
            file.write(f"{book.title},{book.author},{book.year}\n")
