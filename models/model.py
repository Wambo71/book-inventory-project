# one book can be purchased by many customers
#one custpmer can buy many books

from sqlalchemy import create_engine , Column , Integer , String , Float , ForeignKey , Date
from sqlalchemy.orm import declarative_base , relationship , sessionmaker



#base for class models
Base = declarative_base()

# setup database
engine = create_engine("sqlite:///bookstore.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer , primary_key=True)
    title = Column(String(50), nullable=False)
    author = Column(String(40), nullable=False)
    price = Column(Integer, nullable=False)
    stock = Column(Integer, nullable=False)

    #relationship is that one book can be in manysales
    sales = relationship("Sale", back_populates="book")


class Customer(Base):
    __tablename__ = 'customers'  
    id = Column(Integer, primary_key=True)     
    name = Column(String(50),nullable=False)
    email = Column(String(50),unique=True,nullable=False)
    address = Column(String(50))

    #relationship is that ome customer can make many sales
    sales = relationship("Sale", back_populates="customer")

class  Sale(Base): 
    __tablename__= 'sales'
    id = Column(Integer , primary_key=True)
    description = Column(String)
    sale_date = Column(String)
    customer_id = Column(Integer , ForeignKey('customers.id'))
    book_id = Column(Integer , ForeignKey('books.id'))

    book = relationship("Book", back_populates="sales")
    customer = relationship("Customer",back_populates="sales")




