from models.model import Book, Sale, Customer, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import session

#Add a book
def add_book(title,author,price,stock):
    new_book = Book(title=title,author=author,stock=stock)
    session.add(new_book)
    session.commit()
    print(f"book '{title}'was added successfully")