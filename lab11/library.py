from book import Book

class Library:
    
    #Default Constructor
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book_id):
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                break

    def get_book_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def get_book_by_author(self, author):
        for book in self.books:
            if book.author == author:
                return book
        return None

    def get_inventory_count(self):
        return len(self.books)