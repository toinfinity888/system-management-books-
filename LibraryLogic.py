
class Book:
    def __init__(self, title, author, pages, date, genre):
        self.title = title
        self.author = author
        self.pages = pages
        self.date = date
        self.genre = genre

    # Creating a method for checking compliance with search criteria

    def matches_search_criteria(self, search_attributes, search_values):
        if search_attributes == "title" and self.title.lower() == search_values.lower():
            return True
        elif search_attributes == "author" and self.author.lower() == search_values.lower():
            return True
        elif search_attributes == "pages" and str(self.pages) == search_values:
            return True
        elif search_attributes == "date" and self.date.lower() == search_values.lower():
            return True
        elif search_attributes == "genre" and self.genre.lower() == search_values.lower():
            return True
        else:
            return False

    # Creating the method to formate the information as capitalize
    def formate_book_info(self):
        formatted_title = self.title.capitalize()
        formatted_author = self.author.title()
        formatted_genre = self.genre.capitalize()

        return (f"Title: {formatted_title}, Author: {formatted_author}, Pages: {self.pages}, Date: {self.date}, "
                f"Genre: {formatted_genre}")


# Creating a function which add a new book

def add_new_book_to_library(any_library):
    title = input("Enter the book title: ")
    author = input("Enter the author's name: ")
    pages = int(input("Enter the number of pages: "))
    date = input("Enter the date of publication: ")
    genre = input("Enter the genre of book: ")

    new_book = Book(title, author, pages, date, genre)

    # Checking for the availability of the genre in the library
    genre_books = any_library.get(genre, [])
    genre_books.append(new_book)
    any_library[genre] = genre_books

    print("New book has added to library!")
    print(new_book.formate_book_info())


def search_book_in_library(any_library):
    search_attributes = input("Enter search attribute (Title, Author, Pages, Date, Genre): ").lower()

    if search_attributes not in ["title", "author", "pages", "date", "genre"]:
        print("The entered attribute is invalid. \nPlease, enter an attribute from the list")
        return

    search_values = input(f"Enter a value for '{search_attributes}': ")

    found_books = []
    for genre, books in any_library.items():
        for book in books:
            if book.matches_search_criteria(search_attributes, search_values):
                found_books.append(book)
    if found_books:
        print("Books founded: ")
        for book in found_books:
            print(book.formate_book_info())
    else:
        print("Searching books not founded.")


# Creating a function to edit a book
def edit_book_in_library(any_library):
    title_searching_book = input("To edit a book, please enter the title: ")
    found_books = []
    for genre, books in any_library.items():
        for book in books:
            if book.matches_search_criteria("title", title_searching_book):
                found_books.append(book)

    if found_books:
        print("The books founded: ")
        for index, book in enumerate(found_books, start=1):
            print(f"{index}.", book.formate_book_info())
        choice = input("Choose a number of book to edit: ")
        try:
            choice_index = int(choice) - 1
            selected_book = found_books[choice_index]

            print("Choose a characteristic to change: ")
            print("1. Title")
            print("2. Author")
            print("3. Pages")
            print("4. Date")
            print("5. Genre")

            selected_characteristic = input("Enter the number of characteristic: ")

            if selected_characteristic == "1":
                new_title = input("Enter a new title for the book: ")
                selected_book.title = new_title
            elif selected_characteristic == "2":
                new_author = input("Enter a new author for the book: ")
                selected_book.author = new_author
            elif selected_characteristic == "3":
                new_pages = input("Enter a new page count for the book: ")
                selected_book.pages = int(new_pages)
            elif selected_characteristic == "4":
                new_date = input("Enter a new date for book: ")
                selected_book.date = new_date
            elif selected_characteristic == "5":
                new_genre = input("Enter a new genre for the book: ")
                selected_book.genre = new_genre
            else:
                print("The entered number is incorrect. Book editing has been interrupted.")
            print("Book information has been successfully edited.")
        except (ValueError, IndexError):
            print("Invalid input or index. Book editing has been interrupted.")
    else:
        print(f"The book with the title '{title_searching_book}' is not found in the library.")


def display_library(any_library):
    if not any_library:
        print("The library is empty.")

    print("The list of all books in library: ")
    for genre, books in any_library.items():
        for book in books:
            print(book.formate_book_info())
