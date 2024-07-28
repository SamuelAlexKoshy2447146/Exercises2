"""4. Create a Python program to efficiently manage and handle a library's collection of books.
Each book in the library is represented with the following attributes: title, author, publisher,
volume, year of publication, and ISBN (International Standard Book Number).
Design and implement a module named LibraryManager.py that includes functions to manage
books in the library. Collect data for 25 recently published books on topics such as Operating
Systems, Data Structures, and Machine Learning using Python, published between 2020 and
2024. Store this information in a dictionary where the key is the ISBN, and the value is another
dictionary containing the book details.

Within the LibraryManager.py module, create functions to:
• Add a book to the library.
• Remove a book from the library by its ISBN.
• Retrieve and display the details of a book using its ISBN.
• Search for books by title or author.
• List all books currently in the library.
• Update the details of an existing book.
• Check if a book is available in the library by its ISBN.

Demonstrate the functionality of your module by adding a few sample books, removing a book,
retrieving the details of a book, searching for books, listing all books, updating book details,
and checking the availability of a book.
"""

from pprint import pprint
from typing import Any


books = {
    "9780134853979": {
        "title": "Modern Operating Systems",
        "author": "Andrew S. Tanenbaum, Herbert Bos",
        "publisher": "Pearson",
        "volume": "4th Edition",
        "year_of_publication": 2022,
        "stock": 6,
    },
    "9781119800361": {
        "title": "Operating System Concepts",
        "author": "Abraham Silberschatz, Peter B. Galvin, Greg Gagne",
        "publisher": "Wiley",
        "volume": "10th Edition",
        "year_of_publication": 2021,
        "stock": 3,
    },
    "9781838551981": {
        "title": "Linux Kernel Programming",
        "author": "Kaiwan N Billimoria",
        "publisher": "Packt Publishing",
        "volume": "2nd Edition",
        "year_of_publication": 2021,
        "stock": 7,
    },
    "9780596005658": {
        "title": "Understanding the Linux Kernel",
        "author": "Daniel P. Bovet, Marco Cesati",
        "publisher": "O'Reilly Media",
        "volume": "3rd Edition",
        "year_of_publication": 2020,
        "stock": 8,
    },
    "9780135462402": {
        "title": "Windows Internals",
        "author": "Pavel Yosifovich, Mark E. Russinovich, David A. Solomon, Alex Ionescu",
        "publisher": "Microsoft Press",
        "volume": "7th Edition",
        "year_of_publication": 2020,
        "stock": 2,
    },
    "9781119731429": {
        "title": "Data Structures and Algorithms in Python",
        "author": "Michael T. Goodrich, Roberto Tamassia, Michael H. Goldwasser",
        "publisher": "Wiley",
        "volume": "1st Edition",
        "year_of_publication": 2021,
        "stock": 5,
    },
    "9781680507225": {
        "title": "Problem Solving with Algorithms and Data Structures using Python",
        "author": "Bradley N. Miller, David L. Ranum",
        "publisher": "Franklin, Beedle & Associates Inc.",
        "volume": "3rd Edition",
        "year_of_publication": 2020,
        "stock": 0,
    },
    "9781838826201": {
        "title": "Python Data Structures and Algorithms",
        "author": "Benjamin Baka",
        "publisher": "Packt Publishing",
        "volume": "1st Edition",
        "year_of_publication": 2020,
        "stock": 4,
    },
    "9780367355742": {
        "title": "Algorithms and Data Structures for Massive Datasets",
        "author": "Dzejla Medjedovic, John Reif",
        "publisher": "CRC Press",
        "volume": "1st Edition",
        "year_of_publication": 2022,
        "stock": 9,
    },
    "9780134854543": {
        "title": "Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow",
        "author": "Aurélien Géron",
        "publisher": "O'Reilly Media",
        "volume": "2nd Edition",
        "year_of_publication": 2020,
        "stock": 6,
    },
    "9781119555162": {
        "title": "Python Machine Learning",
        "author": "Sebastian Raschka, Vahid Mirjalili",
        "publisher": "Wiley",
        "volume": "3rd Edition",
        "year_of_publication": 2020,
        "stock": 0,
    },
    "9781492045021": {
        "title": "Machine Learning with Python Cookbook",
        "author": "Chris Albon",
        "publisher": "O'Reilly Media",
        "volume": "1st Edition",
        "year_of_publication": 2020,
        "stock": 7,
    },
    "9781617294433": {
        "title": "Deep Learning with Python",
        "author": "François Chollet",
        "publisher": "Manning Publications",
        "volume": "2nd Edition",
        "year_of_publication": 2021,
        "stock": 8,
    },
    "9781800209060": {
        "title": "Machine Learning with PyTorch and Scikit-Learn",
        "author": "Sebastian Raschka, Yuxi (Hayden) Liu, Vahid Mirjalili",
        "publisher": "Packt Publishing",
        "volume": "1st Edition",
        "year_of_publication": 2022,
        "stock": 3,
    },
    "9781484272097": {
        "title": "Machine Learning Engineering with Python",
        "author": "Andrew P. McMahon",
        "publisher": "Apress",
        "volume": "1st Edition",
        "year_of_publication": 2022,
        "stock": 9,
    },
    "9781913367315": {
        "title": "Machine Learning for Absolute Beginners",
        "author": "Oliver Theobald",
        "publisher": "Independently Published",
        "volume": "3rd Edition",
        "year_of_publication": 2020,
        "stock": 4,
    },
    "9781787125933": {
        "title": "Advanced Machine Learning with Python",
        "author": "John Hearty",
        "publisher": "Packt Publishing",
        "volume": "1st Edition",
        "year_of_publication": 2020,
        "stock": 2,
    },
    "9781789800883": {
        "title": "Python Machine Learning Projects",
        "author": "Lisa Tagliaferri",
        "publisher": "Packt Publishing",
        "volume": "1st Edition",
        "year_of_publication": 2022,
        "stock": 0,
    },
    "9781492041139": {
        "title": "Data Science from Scratch: First Principles with Python",
        "author": "Joel Grus",
        "publisher": "O'Reilly Media",
        "volume": "2nd Edition",
        "year_of_publication": 2020,
        "stock": 7,
    },
    "9781492051695": {
        "title": "Natural Language Processing with Python",
        "author": "Steven Bird, Ewan Klein, Edward Loper",
        "publisher": "O'Reilly Media",
        "volume": "2nd Edition",
        "year_of_publication": 2021,
        "stock": 1,
    },
    "9781491963043": {
        "title": "Applied Text Analysis with Python: Enabling Language-Aware Data Products with Machine Learning",
        "author": "Benjamin Bengfort, Rebecca Bilbro, Tony Ojeda",
        "publisher": "O'Reilly Media",
        "volume": "1st Edition",
        "year_of_publication": 2020,
        "stock": 5,
    },
    "9781492043493": {
        "title": "Generative Deep Learning: Teaching Machines to Paint, Write, Compose, and Play",
        "author": "David Foster",
        "publisher": "O'Reilly Media",
        "volume": "1st Edition",
        "year_of_publication": 2020,
        "stock": 8,
    },
    "9781138492537": {
        "title": "Data Science and Machine Learning: Mathematical and Statistical Methods",
        "author": "Dirk P. Kroese, Zdravko I. Botev, Thomas Taimre, Radislav Vaisman",
        "publisher": "CRC Press",
        "volume": "1st Edition",
        "year_of_publication": 2020,
        "stock": 6,
    },
    "9781492064337": {
        "title": "Machine Learning Design Patterns: Solutions to Common Challenges in Data Preparation, Model Building, and MLOps",
        "author": "Valliappa Lakshmanan, Sara Robinson, Michael Munn",
        "publisher": "O'Reilly Media",
        "volume": "1st Edition",
        "year_of_publication": 2020,
        "stock": 9,
    },
    "9783031333422": {
        "title": "Machine Learning with Python: Theory and Implementation",
        "author": "Amin Zollanvari",
        "publisher": "Springer Cham",
        "volume": None,
        "year_of_publication": 2023,
        "stock": 2,
    },
}


def add_book(book: dict[str, dict[str, Any]]):
    """Add a book to the library

    Args:
        book (dict[str, dict[str, Any]]): The book to be added

    Returns:
        bool: True if the book got added, else False
    """

    isbn = [key for key in book.keys()][0]
    if isbn in books:
        return False
    books.update(book)
    return True


def remove_book(isbn_code: str):
    """Remove a book from the library

    Args:
        isbn_code (str): The book to be removed

    Returns:
        bool: True if the book got removed, else False
    """

    if isbn_code in books:
        books.pop(isbn_code)
        return True
    return False


def retrieve_book(isbn_code: str):
    """Retrieve a book from the library

    Args:
        isbn_code (str): The book to be retrieved

    Returns:
        dict[str, Any] | None: The book if it is available, else None
    """

    if isbn_code in books:
        return books[isbn_code]


def search_book(*, title: str = "", author: str = ""):
    """Search for a book with either title or author name

    Args:
        title (str, optional): The title name. Defaults to "".
        author (str, optional): The author name. Defaults to "".

    Raises:
        ValueError: If no value is given

    Returns:
        list: The books that match the criteria
    """
    
    if title == "" and author == "":
        raise ValueError("At least one argument must be given")
    result = []
    if title != "":
        for book in books.values():
            if title.lower() in book["title"].lower():
                result.append(book)
    else:
        for book in books.values():
            if author.lower() in book["author"].lower():
                result.append(book)
    return result


def list_available_books():
    """List all available books that can be taken from the library

    Returns:
        dict: The books that can be withdrawn
    """
    
    available_books = {}
    for book, data in books.items():
        if data["stock"] > 0:
            available_books.update({book: data["title"]})
    return available_books


def list_all_books():
    """List of all books in the library

    Returns:
        dict: All the books in the library
    """
    
    all_books = {}
    for book, data in books.items():
        all_books.update({book: data["title"]})
    return all_books


def update_book(isbn_code: str, **kwargs):
    """Update a book if isbn code is found in the library

    Args:
        isbn_code (str): The code for the book

    Raises:
        ValueError: If an invalid key is given

    Returns:
        bool: True if the book got edited, else False
    """
    if isbn_code in books:
        for key, value in kwargs.items():
            if key in books[isbn_code]:
                books[isbn_code][key] = value
            else:
                raise ValueError(f"Invalid key: {key}")
        return True
    return False


def check_availability(isbn_code: str):
    """Check if a book is in stock

    Args:
        isbn_code (str): The isbn code of the book

    Returns:
        bool: True if in stock, else False
    """
    
    if isbn_code not in books:
        return False
    return books[isbn_code]["stock"] > 0


if __name__ == "__main__":
    new_book = {
        "9781492079331": {
            "title": "Programming Rust",
            "author": "Jim Blandy, Jason Orendorff",
            "publisher": "O'Reilly Media",
            "volume": "2nd Edition",
            "year_of_publication": 2021,
            "stock": 1,
        }
    }
    old_book = {
        "9781138492537": {
            "title": "Data Science and Machine Learning: Mathematical and Statistical Methods",
            "author": "Dirk P. Kroese, Zdravko I. Botev, Thomas Taimre, Radislav Vaisman",
            "publisher": "CRC Press",
            "volume": "1st Edition",
            "year_of_publication": 2020,
            "stock": 1,
        },
    }

    # Count books
    print("No. of books in library:", len(books))

    # Add a new book
    print("\nNew Book:", new_book)
    print("Add status:", add_book(new_book))
    print("No. of books after adding new book:", len(books))
    print("\nOld book:", old_book)
    print("Add status:", add_book(old_book))
    print("No. of books after adding old book:", len(books))

    # Remove a book
    isbn_code = "9780596005658"
    print("\nRemoving book with code:", isbn_code)
    print("Remove status:", remove_book(isbn_code))
    print("No. of books after removing book:", len(books))
    fake_isbn = "9783031333421"
    print("\nRemoving book with (fake) code:", fake_isbn)
    print("Remove status:", remove_book(fake_isbn))
    print("No. of books after removing book:", len(books))

    # available_books = list_available_books()
    # print("List of available books:")
    # pprint(available_books)

    all_books = list_all_books()
    print("\nList of all books")
    pprint(all_books)

    book_search = search_book(title="Data Structures")
    print("\nList of books with title 'Data Structures'", book_search)
    book_search = search_book(author="Joel Grus")
    print("\nList of books with author 'Joel Grus'", book_search)

    # Find a book
    def found_book(isbn: str):
        retrieved_book = retrieve_book(isbn)
        if retrieved_book is not None:
            print("Retrieved book:", retrieved_book)
        else:
            print("Could not find the book")

    isbn = "9791492041139"
    print("\nRetrieve book:", isbn)
    found_book(isbn)

    isbn = "9781492041139"
    print("\nRetrieve book:", isbn)
    found_book(isbn)

    update_book(isbn, volume="3rd Edition")
    print("\nEdit volume of the book")
    found_book(isbn)

    print("\nChecking availability of book:")
    isbn_none = "9781680507225"
    isbn_available = "9781787125933"
    print("Is book with isbn:", isbn_none, "available?", check_availability(isbn_none))
    print(
        "Is book with isbn:",
        isbn_available,
        "available?",
        check_availability(isbn_available),
    )
