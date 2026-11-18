from file import load_data,save_data
class Book:
    def __init__(self,book_id,title,author,isbn,published_year):
        self.books=load_data()
        self.book_id=book_id
        self.title = title
        self.author = author 
        self.isbn = isbn 
        self.published_year = published_year
    
book1 = Book('BID1','PythonBook','Jame','ISBN1','2020')
book2 = Book('BID2','JavaBook','Sean','ISBN2','2019')
library = [book1,book2]