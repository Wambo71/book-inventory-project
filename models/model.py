# one book can be purchased by many customers
#one custpmer can buy many books

from sqlalchemy import create_engine , Column , Integer , String , Float , ForeignKey , Date
from sqlalchemy.orm import declarative_base , relationship , sessionmaker
from datetime import date

#base for class models
Base = declarative_base()

#database connection
#engine = create_engine("sqlite:///bookstore.db")
#session = sessionmaker(bind=engine)
#session = session()

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer , primary_key=True)
    title = Column(String)
    author = Column(String)
    price = Column(Float)
    stock = Column(Integer)

    #relationship is that one book can be in manysales
    sales = relationship("Sale", back_populates="book")


class Customer(Base):
    __tablename__ = 'customers'  
    id = Column(Integer, primary_key=True)     
    name = Column(String)
    email = Column(String)
    address = Column(String)

    #relationship is that ome customer can make many sales
    sales = relationship("Sale", back_populates="customer")

class  Sale(Base): 
    __tablename__= 'sales'
    id = Column(Integer , primary_key=True)
    description = Column(String)
    sale_date = Column(Date, default=date . today)
    customer_id = Column(Integer , ForeignKey('customers.id'))
    book_id = Column(Integer , ForeignKey('books.id'))

    book = relationship("Book", back_populates="sales")
    customer = relationship("Customer",back_populates="sales")


# setup database
engine = create_engine("sqlite:///bookstore.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# create book  
#book1 = Book(title="Python 101", author="Guido", price=29.99, stock=10)
book2 = Book(title="Javascript for beginners", author="Jon Doe", price=199.70, stock=7)
book3 = Book(title="Flask Dive Deep", author="Owang Sino", price=234.33, stock=12)
book4 = Book(title="Learning React",author="Allan Woe", price=345.8, stock=4)
book5 = Book(title="Geeksforgeeks", author="Okello Ann", price=56.78, stock=9)
#create customer
#customer1 = Customer(name="Alice", email="alice@example.com", address="123 Street")
customer2 = Customer(name="Wambui", email="wambui@gmail.com", address="Molo street")
customer3 = Customer(name="karanja", email="karanja@example.com", address="45 street")
customer4 = Customer(name="Ruth", email="ruth@gmail.com", address="kiks Avenue")
customer5 = Customer(name="Joan", email="joan@gmail.com", address="456 Streer")

# create a sale
#sale1 = Sale(description="Alice buys Python book", customer=customer1, book=book1)
sale2 = Sale(description="Wambui buys javascript for beginners on discount", customer=customer2,book=book2)
sale3 = Sale(description="Karanja buys Flask Dive Book on offer",customer=customer3,book=book3)
sale4 = Sale(description="Ruth buys learning React book ", customer=customer4,book=book4)
sale5 = Sale(description="Joan buys Geeksforgeeks book on discount", customer=customer5,book=book5)
# add to session
session.add_all([book2,book3,book4,book5,customer2,customer3,customer4,customer5,sale2,sale3,sale4,sale5])
session.commit()
