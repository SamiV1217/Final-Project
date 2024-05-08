import sqlite3
from contextlib import closing

def findBook(title):
    conn = sqlite3.connect("Books.sqlite")
    c = conn.cursor()
    query = '''SELECT book_id
        FROM Book
        WHERE book_name=?'''
    c.execute(query, (title,))
    books = c.fetchall()
    if len(books) > 0:
        return True
    else:
        return False
