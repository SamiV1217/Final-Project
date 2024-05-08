import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3
from contextlib import closing
from objects import Publisher, Book
from findBook import *

class updateBookPrice:

    def on_click(event):
        event.widget.delete(0, tk.END)
    # SQL to change a book
    def updateDatabase(label, title, price):
        if len(title) == 0 or price == 0:
            label.configure(text="fill in each box", fg="red")
            label.pack()
        elif not findBook(title) and price > 0:
            label.configure(text="Title Not Found", fg="red")
            label.pack()
        else:
            label.configure(text=title+" has been updated.",fg="green")
            conn = sqlite3.connect("books.sqlite")
            c = conn.cursor()
            conn.row_factory = sqlite3.Row
            with closing(conn.cursor()) as c:
                sql = '''UPDATE Book
                    SET price = ?
                    WHERE book_name = ?'''
                c.execute(sql, (price, title))
                conn.commit()
    #UI for updating a book's price
    def updateBook(root):
        updateWindow = Toplevel(root)
        updateWindow.title("Update Book")
        updateWindow.geometry("300x120")
        frame = ttk.Frame(updateWindow, padding="10 10 10 10")
        frame.pack(fill=tk.BOTH, expand=True)

        title = tk.StringVar()
        ttk.Label(frame, text="Title:").grid(column=0, row=0, sticky=tk.E)
        titling = ttk.Entry(frame, width=25,textvariable=title)
        titling.grid(column=1, row=0)

        price = tk.DoubleVar()
        ttk.Label(frame, text="Price:").grid(column=0, row=1, sticky=tk.E)
        pricing = ttk.Entry(frame, width=25, textvariable=price)
        pricing.bind("<Button-1>", updateBookPrice.on_click)
        pricing.grid(column=1, row=1)

        label = Label(updateWindow, text="", fg="green")

        button1 = ttk.Button(frame, text="Change",command= lambda: updateBookPrice.updateDatabase(label,title.get(), price.get()))
        button1.grid(column=1,row=2)
        label.pack()
