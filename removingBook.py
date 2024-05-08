import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3
from contextlib import closing
from objects import Publisher, Book
from findBook import *

class removingBook:
    #SQL and message to remove a book from the database
    def deleteIt(label,title):
        if findBook(title):
            conn = sqlite3.connect("books.sqlite")
            c = conn.cursor()
            conn.row_factory = sqlite3.Row
            with closing(conn.cursor()) as c:
                sql =  '''DELETE FROM Book
                      WHERE book_name = ?'''
                c.execute(sql, (title,))
                conn.commit()
            label.config(text=""+title+" has been removed", fg="green")
        else:
            label.config(text=""+title+" does not exist", fg="red")

    #remove book window function
    def deleteBook(root):
        deletingWindow = Toplevel(root)
        deletingWindow.title("Remove a Book")
        deletingWindow.geometry("250x120")
        frame = ttk.Frame(deletingWindow, padding="10 10 10 10")
        frame.pack(fill=tk.BOTH, expand=True)
        
        title = tk.StringVar()
        ttk.Label(frame, text="Title:").pack()
        titling = ttk.Entry(frame, width=25,textvariable=title).pack()
        label = Label(deletingWindow,text="", fg="red")
        
        submitButton = ttk.Button(frame, text="Submit", command= lambda: removingBook.deleteIt(label, title.get()))
        submitButton.pack()
        label.pack()
