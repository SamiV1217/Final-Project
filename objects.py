from dataclasses import dataclass

@dataclass
class Publisher:
    publisher_ID:int = 0
    publisher_name:str = ""
        
@dataclass
class Book:
    book_id:int = 0
    book_name:str = ""
    year:int = 0
    price:int = 0
    publisher_ID:Publisher = None
