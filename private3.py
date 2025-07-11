class member:
    def __init__(self, book_ID, book_name, author, publication_year):
        self.__book_ID = book_ID
        self.__publication_year = publication_year

    def set_book_ID(self, book_ID):
        self.__book_ID = book_ID

    def set_publication_year(self, publication_year):
        self.__publication_year = publication_year
