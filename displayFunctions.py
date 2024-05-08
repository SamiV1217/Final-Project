import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3
from contextlib import closing

class displayFunctions:
    def display(root):
        displayWindow = Toplevel(root)
        displayWindow.title("Display Books")
        displayWindow.geometry("400x200")
        frame = ttk.Frame(displayWindow, padding="10 10 10 10")
        frame.pack(fill=tk.BOTH, expand=True)

        conn = sqlite3.connect("books.sqlite")
        c = conn.cursor()
        conn.row_factory = sqlite3.Row
        try:
            with closing(conn.cursor()) as c:
                query = '''SELECT * FROM Book'''
                c.execute(query)
                books = c.fetchall()
        except sqlite3.OperationalError as e:
            print("Error reading database -", e)
            books = None
        T = tk.Text(displayWindow)
        i = 1

        # display the results in the window
        if books != None:
            Label(frame, text=f"Title").grid(row=0,column=0)
            Label(frame, text=f"Year").grid(row=0,column=1)
            Label(frame, text=f"Publisher ID").grid(row=0,column=2)
            Label(frame, text=f"Price").grid(row=0,column=3)
            for book in books:
                book_name = Label(frame, text=f"{book['book_name']}").grid(row=i,column=0, sticky=tk.W)
                year = Label(frame, text=f"{book['year']}").grid(row=i,column=1)
                pubID = Label(frame, text=f"{book['publisher_id']}").grid(row=i,column=2)
                price = Label(frame, text=f"{book['price']}").grid(row=i,column=3)
                i = i+1

            ttk.Separator(frame).grid(column=1, row=1, rowspan=i, pady=25, padx=40)
            ttk.Separator(frame).grid(column=0, row=0, padx=40)
            ttk.Separator(frame).grid(column=2, row=1, rowspan=i, padx=40)
            ttk.Separator(frame).grid(column=3, row=1, rowspan=i, padx=40)



