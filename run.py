from LOLtask import Book

def main():
    my_book = Book("The John", "Smith Jones", 1949)
    print(f"Title: {my_book.title}, Author: {my_book.author}, Year: {my_book.year}")
    print("The book is available in the library!")

if __name__ == "__main__":
    main()