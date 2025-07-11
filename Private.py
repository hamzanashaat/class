class member:
    def __init__(self, book_ID, book_name, author, publication_year):
        self.__book_ID = book_ID
        self.__publication_year = publication_year


        one = member("B001", "Python Programming", "Smith Johnson", 2020)
        print(f"Book ID: {one._member__book_ID}, Name: {one._member__book_name}, Author: {one._member.author}, Year: {one.__publication_year}")