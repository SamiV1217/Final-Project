import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3
from contextlib import closing
from objects import Publisher, Book
from findBook import *

class insertFunctions:
    #SQL for the book being inserted as well as display message
    def insertBook(label, title, year, pub, price=0):
        if len(title) == 0 or pub == 0:
            label.configure(text="Title and publisher ID cannot be blank or 0.", fg="red")
            label.pack()
        elif findBook(title):
            label.configure(text=title+" already exists", fg="orange")
            label.pack()
        else:
            label.configure(text=""+title+" has been inserted.", fg="green")
            conn = sqlite3.connect("books.sqlite")
            c = conn.cursor()
            conn.row_factory = sqlite3.Row
            with closing(conn.cursor()) as c:
                sql = '''INSERT INTO Book 
                        (book_name, year, publisher_ID, price)
                         VALUES 
                         (?, ?, ?, ?)'''
                c.execute(sql, (title, year, pub, price))
                conn.commit()
            label.pack()
    #Clear the text boxes of current information
    def clear(label, titling, year, pub, price):
        titling.delete(0,tk.END)
        year.set(0)
        pub.set(0)
        price.set(0.00)
        label.configure(text="")

    #Function to display insert book window  
    def inserting(root):
        insertingWindow = Toplevel(root)
        insertingWindow.title("Insert Book")
        insertingWindow.geometry("400x175")
        frame = ttk.Frame(insertingWindow, padding="10 10 10 10")
        frame.pack(fill=tk.BOTH, expand=True)

        title = tk.StringVar()
        ttk.Label(frame, text="Title:").grid(column=0, row=0, sticky=tk.E)
        titling = ttk.Entry(frame, width=25,textvariable=title)
        titling.grid(column=1, row=0, columnspan=2, sticky=tk.W)

        year = tk.IntVar()
        ttk.Label(frame, text="Year:").grid(column=0, row=1, sticky=tk.E)
        yearing = ttk.Entry(frame, width=25, textvariable=year)
        yearing.grid(column=1, row=1, columnspan=2, sticky=tk.W)

        pub = tk.IntVar()
        ttk.Label(frame, text="Publisher ID:").grid(column=0, row=2, sticky=tk.W)
        publisher = ttk.Entry(frame, width=25, textvariable=pub)
        publisher.grid(column=1, row=2, columnspan=2, sticky=tk.W)

        price = tk.DoubleVar()
        ttk.Label(frame, text="Price:").grid(column=0, row=3, sticky=tk.E)
        pricing = ttk.Entry(frame, width=25, textvariable=price)
        pricing.grid(column=1, row=3, columnspan=2, sticky=tk.W)
        
        label = Label(insertingWindow, text="", fg="green")

        
        button1 = ttk.Button(frame, text="Insert",command= lambda: insertFunctions.insertBook(label,title.get(), year.get(), pub.get(), price.get()))
        button1.grid(column=1,row=4)
        label.pack()
        
        button2 = ttk.Button(frame, text="Clear",command= lambda:insertFunctions.clear(label,titling, year, pub, price))
        button2.grid(column=2,row=4)
