import click
from models.model import session, Book,Customer,Sale
from crud.crud import add_book , delete_book, get_all_books,add_customer,get_all_customers,delete_customer,add_sale,get_all_sales,delete_sale


while True:
    click.secho("BOOKSTORE INVENTORY AND SALES", fg="red")
    click.secho("1. Manage book", fg="blue")
    click.secho("2. Manage customers", fg="yellow")
    click.secho("3. Update sales", fg="green")
    click.secho("4. Exit",fg="yellow")
 
    user_input =click.prompt ("Enter oPtion", type=int)
    click.secho(f"You have entered option {user_input}")

    if user_input == 1:
        click.secho("1. Add book",fg="blue")
        click.secho("2. view book", fg="red")
        click.secho("3. Delete book",fg="yellow")
        user_selection = click.prompt("Enter option 1 or 2 or 3",type=int)
        if user_selection == 1:
            book_title = click.prompt("Enter book tittle")
            book_author = click.prompt ("Enter book author")
            book_price = click.prompt("Enter book price",type=int)
            book_stock = click.prompt("Enter book stock",type=int)
            add_book (session,book_title,book_author,book_price,book_stock)

            click.secho(f"books added successfully",fg="red")

        if user_selection == 2:

         click.secho(f"All books in the inventory",fg="green")
         get_all_books()

        if user_selection ==3:
          book_id = click.prompt("Enter book ID to delete", type=int)
          delete_book(session, book_id)
        
          click.secho(f"book deleted successfully",fg="red") 


    if user_input == 2:
       click.secho("1. Add customer",fg="blue")
       click.secho("2. view customer", fg="red")
       click.secho("3. Delete customer",fg="yellow")          
      
       user_selection = click.prompt("Enter option (1, 2 or 3)", type=int)

       if user_selection ==1:
          name = click.prompt("Enter customer name")
          email = click.prompt("Enter customer email")
          address = click.prompt("Enter customer address")
          add_customer(session, name, email,address)

          click.secho(f"customer added successfully")


       if user_selection ==2: 
           click.secho(f"All customers",fg="green") 
           get_all_customers()

       if user_selection ==3:  
           customer_id = click.prompt("Enter customer ID to delete", type=int)
           delete_customer(session, customer_id)

           click.secho(f"customer deleted successfully")


    if user_input ==3: 
       click.secho("1. Add sales",fg="blue")
       click.secho("2. view sales", fg="red")
       click.secho("3. Delete sales",fg="yellow") 

       user_selection = click.prompt("Enter option (1, 2 or 3)", type=int)

       if user_selection ==1:
            
            customer_id = click.prompt("Enter customer ID", type=int)
            book_id = click.prompt("Enter book ID", type=int)
            quantity = click.prompt("Enter quantity", type=int)
            add_sale(session, customer_id, book_id, quantity)

            click.echo(f"Sale added successfully")

       if user_selection == 2:
             click.secho(" All Sales:", fg="yellow")
             get_all_sales(session)

       if user_selection == 3:
             sale_id = click.prompt("Enter sale ID to delete", type=int)
             delete_sale(session, sale_id)
             click.secho(f"Sale deleted succussfully")
    elif user_input == 4: 
       click.secho(f"EXITING",fg="red")
       break        
           


    




   