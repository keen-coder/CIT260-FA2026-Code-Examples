from book import Book
from library import Library

def main():
    book = Book('Starting out with Python', 'Tony Gaddis')

    library1 = Library('Penn College Library', [book])

    library2 = library1.copy()

    print(library1)
    print(library2)

    library2.get_books()[0].set_title('New Title')

    print(library1)
    print(library2)




if __name__ == '__main__':
    main()