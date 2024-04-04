import tkinter as tk
from LibraryLogic import add_new_book_to_library, search_book_in_library, edit_book_in_library, display_library
from LibraryInterface import LibraryInterface

def main():
    root = tk.Tk()
    app = LibraryInterface(root)
    root.mainloop()
if __name__ == "__main__":
    main()

    library = {}

    while True:
        print("\nChoose a command: ")
        print("1. Add new book to a library")
        print("2. Search book in library")
        print("3. To edit the book information")
        print("4. To display library")
        print("5. To quit")

        choice = input("Enter the number of the selected action: ")
        if choice == "1":
            add_new_book_to_library(library)
        elif choice == "2":
            search_book_in_library(library)
        elif choice == "3":
            edit_book_in_library(library)
        elif choice == "4":
            display_library(library)
        elif choice == "5":
            print("The program is completed!")
            break
        else:
            print("Failed choice. Please choose a command.")


