import LibraryLogic
from LibraryLogic import add_new_book_to_library, search_book_in_library, edit_book_in_library, display_library
import tkinter as tk
from tkinter import Canvas, PhotoImage


class LibraryInterface:
    def __init__(self, master):
        self.master = master
        master.title("Library Management System")

        self.master.geometry("400x300")
        self.master.configure(bg="#E6E6FA")

        self.canvas = Canvas(master, width=400, height=80, bg="#E6E6FA")
        self.canvas.pack(side="top", pady=(10, 0), padx=10)

        self.img = PhotoImage(file="_Lib.gif")

        self.canvas.create_image(0, 0, anchor="nw", image=self.img)

        self.label = tk.Label(master, text = "Welcom to the Library!")
        self.label.pack()

        self.exit_button = tk.Button(master, text="Exit", command=self.exit_program,
                                     width=20)
        self.exit_button.pack(side="bottom", pady=(0, 10), )

        self.add_book_button = tk.Button(master, text="Add New Book", command=self.add_new_book_to_library,
                                         width = 20)
        self.add_book_button.pack(side="bottom", pady=(0, 10), )

        self.search_books_button = tk.Button(master, text="Search Books", command=self.search_book_in_library,
                                             width = 20)
        self.search_books_button.pack(side="bottom", pady=(0, 10), )

        self.edit_books_button = tk.Button(master, text="Edit Book", command=self.edit_book_in_library,
                                           width = 20)
        self.edit_books_button.pack(side="bottom", pady=(0, 10), )

        self.display_books_button = tk.Button(master, text="Display Books", command=self.display_library,
                                              width = 20)
        self.display_books_button.pack(side="bottom", pady=(0, 10), )


    library = {}

    def exit_program(self):
        self.master.destroy()

    def add_new_book_to_library(self):
        LibraryLogic.add_new_book_to_library(self.library)

    def search_book_in_library(self):
        LibraryLogic.search_book_in_library(self.library)

    def edit_book_in_library(self):
        LibraryLogic.edit_book_in_library(self.library)

    def display_library(self):
        LibraryLogic.display_library(self.library)



