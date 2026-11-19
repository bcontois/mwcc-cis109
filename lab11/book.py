import uuid

class Book:

    #Default Constructor
    def __init__(self):
        self.title = ""
        self.author = ""
        self.genre = ""
        self.book_id = str(uuid.uuid4())
        self.__state = "Not in Inventory"
        self.__borrower = ""

    #Parameterized Constructor
    def __init__(self, title, author, genre, state="Checked In"):
        self.title = title
        self.author = author
        self.genre = genre
        self.book_id = self.book_id = str(uuid.uuid4())
        self.__state = state
        self.__borrower = ""

    def check_in(self):
        self.__state = "Checked In"
        self.__borrower = ""

    def check_out(self, borrower):
        self.__state = "Checked Out"
        self.__borrower = borrower

    def get_state(self, borrower):
        return self.__state

