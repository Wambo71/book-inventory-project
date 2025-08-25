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

# create book & customer
book1 = Book(title="Python 101", author="Guido", price=29.99, stock=10)
customer1 = Customer(name="Alice", email="alice@example.com", address="123 Street")

# create a sale
sale1 = Sale(description="Alice buys Python book", customer=customer1, book=book1)

# add to session
session.add_all([book1, customer1, sale1])
session.commit()
