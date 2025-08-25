from models.model import Book, Sale, Customer, session
from datetime import date

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

#add sale
def add_sale(book_id, customer_id, sale_date, description):
    new_sale = Sale(book_id=book_id, customer_id=customer_id, sale_date=sale_date,description=description)
    session.add(new_sale)
    session.commit()
    print(f"sale added:Book ID {book_id} Customer ID {customer_id} Date {sale_date} Description {description}")     