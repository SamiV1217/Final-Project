#connect to the books database
import sqlite3
from contextlib import closing
conn = sqlite3.connect("books.sqlite")
c = conn.cursor()
conn.row_factory = sqlite3.Row

from objects import Publisher, Book

#list the available books
# execute a SELECT statement - with exception handling
try:
    with closing(conn.cursor()) as c:
        query = '''SELECT * FROM Book'''
        c.execute(query)
        books = c.fetchall()
except sqlite3.OperationalError as e:
    print("Error reading database -", e)
    books = None

# display the results
if books != None:
    for book in books:
        print(f"{book['book_name']} | {book['year']} | {book['price']} | "
              f"{book['publisher_id']}")
    print()

#add a new book.
# execute an INSERT statement
name = "A Fish Called Wanda"
year = 1988
publisherID = 2
price = 19.99
with closing(conn.cursor()) as c:
    sql = '''INSERT INTO Book 
            (book_name, year, publisher_ID, price)
             VALUES 
             (?, ?, ?, ?)'''
    c.execute(sql, (name, year, publisherID, price))
    conn.commit()
print(name, "was inserted.\n")
#list the available books
# execute a SELECT statement - with exception handling
try:
    with closing(conn.cursor()) as c:
        query = '''SELECT * FROM Book'''
        c.execute(query)
        books = c.fetchall()
except sqlite3.OperationalError as e:
    print("Error reading database -", e)
    books = None

# display the results
if books != None:
    for book in books:
        print(f"{book['book_name']} | {book['year']} | {book['price']} | "
              f"{book['publisher_id']}")
    print()

#update the price of a book.
name2 = "Programming in Python"
newPrice = 195.99
with closing(conn.cursor()) as c:
    sql = '''UPDATE Book
            SET price = ?
            WHERE book_name = ?'''
    c.execute(sql, (newPrice, name2))
    conn.commit()
print(name2, " had its price updated.\n")

#list the available books
# execute a SELECT statement - with exception handling
try:
    with closing(conn.cursor()) as c:
        query = '''SELECT * FROM Book'''
        c.execute(query)
        books = c.fetchall()
except sqlite3.OperationalError as e:
    print("Error reading database -", e)
    books = None

# display the results
if books != None:
    for book in books:
        print(f"{book['book_name']} | {book['year']} | {book['price']} | "
              f"{book['publisher_id']}")
    print()

#delete a book.
# execute a DELETE statement-by name deletes ALL. -by ID just deletes 1
with closing(conn.cursor()) as c:
    sql =  '''DELETE FROM Book
              WHERE book_name = ?'''
    c.execute(sql, (name,))
    conn.commit()
print(name, "was deleted.\n")

#list the available books
# execute a SELECT statement - with exception handling
try:
    with closing(conn.cursor()) as c:
        query = '''SELECT * FROM Book'''
        c.execute(query)
        books = c.fetchall()
except sqlite3.OperationalError as e:
    print("Error reading database -", e)
    books = None

# display the results
if books != None:
    for book in books:
        print(f"{book['book_name']} | {book['year']} | {book['price']} | "
              f"{book['publisher_id']}")
    print()

