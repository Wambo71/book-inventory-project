from models.model import Book, Sale, Customer, session
from datetime import date

# Add a book
def add_book(title, author, price, stock):
    new_book = Book(title=title, author=author, price=price, stock=stock)
    session.add(new_book)
    session.commit()
    print(f"Book '{title}' was added successfully")

# Add customer
def add_customer(name, email, address):
    new_customer = Customer(name=name, email=email, address=address)
    session.add(new_customer)
    session.commit()
    print(f"Customer '{name}' was added successfully")

# Add sale
def add_sale(book_id, customer_id, sale_date, description):
    new_sale = Sale(book_id=book_id, customer_id=customer_id, sale_date=sale_date, description=description)
    session.add(new_sale)
    session.commit()
    print(f"Sale added: Book ID {book_id}, Customer ID {customer_id}, Date {sale_date}, Description {description}")

# Fetch all books
def get_all_books():
    books = session.query(Book).all()
    for book in books:
        print(f"{book.id}: {book.title} by {book.author} ${book.price}")

# Fetch one book
def get_book(book_id):
    book = session.query(Book).filter_by(id=book_id).first()
    if book:
        print(f"Found: {book.id}: {book.title} by {book.author} ${book.price}")
    else:
        print("Book not found")

# Fetch all customers
def get_all_customers():
    customers = session.query(Customer).all()
    for customer in customers:
        print(f"{customer.id}: {customer.name}, {customer.email}, {customer.address}")

# Fetch one customer
def get_customer(customer_id):
    customer = session.query(Customer).filter_by(id=customer_id).first()
    if customer:
        print(f"Found: {customer.id}: {customer.name}, {customer.email}, {customer.address}")
    else:
        print("Customer not found")

# Fetch all sales
def get_all_sales():
    sales = session.query(Sale).all()
    for sale in sales:
        print(f"{sale.id}: {sale.description} on {sale.sale_date}")

# Delete book
def delete_book(book_id):
    book = session.query(Book).filter_by(id=book_id).first()
    if book:
        session.delete(book)
        session.commit()
        print(f"Book id:{book_id} deleted successfully")
    else:
        print("Book not found")

# Delete customer
def delete_customer(customer_id):
    customer = session.query(Customer).filter_by(id=customer_id).first()
    if customer:
        session.delete(customer)
        session.commit()
        print(f"Customer id:{customer_id} deleted successfully")
    else:
        print("Customer not found")

# Delete sale
def delete_sale(sale_id):
    sale = session.query(Sale).filter_by(id=sale_id).first()
    if sale:
        session.delete(sale)
        session.commit()
        print(f"Sale id:{sale_id} deleted successfully")
    else:
        print("Sale not found")
