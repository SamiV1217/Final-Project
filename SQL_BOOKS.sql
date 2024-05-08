
-- Drop existing tables to start fresh every time this SQL is run
DROP TABLE IF EXISTS Book;
DROP TABLE IF EXISTS Publisher;
--Make the Book table
CREATE TABLE "Book" (
	"book_id"	INTEGER NOT NULL,
	"publisher_id"	INTEGER NOT NULL,
	"book_name"	TEXT NOT NULL,
	"year"	INTEGER NOT NULL,
	"price"	REAL NOT NULL,
	FOREIGN KEY("publisher_id") REFERENCES "Publisher"("publisher_id"),
	PRIMARY KEY("book_id")
);

--Make the Publisher table
CREATE TABLE "Publisher" (
	"publisher_id"	INTEGER NOT NULL,
	"publisher_name"	TEXT NOT NULL,
	PRIMARY KEY("publisher_id")
);

--Insert publishers into publsiher  table
INSERT INTO Publisher (publisher_name)
VALUES("Pearson");
INSERT INTO Publisher(publisher_name)
VALUES("Murach");
INSERT INTO Publisher(publisher_name)
VALUES("McGraw Hill");
INSERT INTO Publisher(publisher_name)
VALUES("Scholastic");
INSERT INTO Publisher(publisher_name)
VALUES("Wiley");

--Insert books into book table
INSERT INTO Book (publisher_id,book_name, year, price)
VALUES(2,"Programming in Python",2021,60.00);
INSERT INTO Book (publisher_id,book_name, year, price)
VALUES(1,"Managerial Accounting",2022,40.00);
INSERT INTO Book (publisher_id,book_name, year, price)
VALUES(3,"Principles of Marketing",2020,30.00);
INSERT INTO Book (publisher_id,book_name, year, price)
VALUES(4,"Building Programs in Java",2019,80.00);
INSERT INTO Book (publisher_id,book_name, year, price)
VALUES(5,"World Religions",2023,70.00);