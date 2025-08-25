from models.model import Book, Sale, Customer, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import session

#Add a book
def add_book(title,author,price,stock):
    new_book = Book(title=title, author=author, price=price, stock=stock)
    session.add(new_book)
    session.commit()
    print(f"book '{title}'was added successfully")

 #add customer
def add_customer(name,email,address):
    new_customer= Customer(name=name, email=email, address=address) 
    session.add(new_customer) 
    session.commit()
    print(f"customer '{name} {email} {address}'was added succesfully") 