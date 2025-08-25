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

#fetch data
def get_all_books():
    books = session.query(Book).all() 
    for book in books:
        print(f"{book.id}: {book.title} by {book.author} {book.price}")


def get_all_customers():
    customers = session.query(Customer).all() 
    for customer in customers:
        print(f"{customer.id}: {customer.name}, {customer.email}, {customer.address}")


def get_all_sales():
    sales = session.query(Sale).all()
    for sale in sales:
        print(f"{sale.id}: {sale.description} on {sale.sale_date}")



if __name__ == "__main__":
#   add_book("Django Mastery", "Jane Doe", 450.50, 6)
    add_book("Software Engineering", "Mary Jane", 340.67, 5)
    
    get_all_books()

    #add_customer("John","john@gmail.com", "123 Main St")
    add_customer("Warui", "warui@gmail.com", "Kitui Street")
    get_all_customers()

    #add_sale(1, 1, date.today(), "John buys Django Mastery") 
    add_sale(2, 2, date.today(), "Warui buys a software emgineering book")
    get_all_sales ()      
        
