from models.model import Book,Customer,Sale,session
from crud.crud import add_book,add_customer,add_sale
from crud.crud import get_all_books,get_all_customers,get_all_sales,date

# # create book  
book1 = Book(title="Python 101", author="Guido", price=29.99, stock=10)
book2 = Book(title="Javascript for beginners", author="Jon Doe", price=199.70, stock=7)
book3 = Book(title="Flask Dive Deep", author="Owang Sino", price=234.33, stock=12)
book4 = Book(title="Learning React",author="Allan Woe", price=345.8, stock=4)
book5 = Book(title="Geeksforgeeks", author="Okello Ann", price=56.78, stock=9)
# #create customer
customer1 = Customer(name="Alice", email="alice@example.com", address="123 Street")
customer2 = Customer(name="Wambui", email="wambui@gmail.com", address="Molo street")
customer3 = Customer(name="karanja", email="karanja@example.com", address="45 street")
customer4 = Customer(name="Ruth", email="ruth@gmail.com", address="kiks Avenue")
customer5 = Customer(name="Joan", email="joan@gmail.com", address="456 Streer")

# # create a sale
sale1 = Sale(description="Alice buys Python book", customer=customer1, book=book1)
sale2 = Sale(description="Wambui buys javascript for beginners on discount", customer=customer2,book=book2)
sale3 = Sale(description="Karanja buys Flask Dive Book on offer",customer=customer3,book=book3)
sale4 = Sale(description="Ruth buys learning React book ", customer=customer4,book=book4)
sale5 = Sale(description="Joan buys Geeksforgeeks book on discount", customer=customer5,book=book5)
# # add to session
session.add_all([book2,book3,book4,book5,customer2,customer3,customer4,customer5,sale2,sale3,sale4,sale5])
session.commit()


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
        