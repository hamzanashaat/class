class member:
    def __init__(self, book_ID, book_name, author, publication_year):
        self.__book_ID = book_ID
        self.__book_name = book_name
        self.__author = author
        self.__publication_year = publication_year

    def show_book_details(self):
        return f"Book ID: {self.__book_ID}, Book Name: {self.__book_name}, Author: {self.__author}, Publication Year: {self.__publication_year}"

    def get_book_ID(self):
        return self.__book_ID

    def get_publication_year(self):
        return self.__publication_year
