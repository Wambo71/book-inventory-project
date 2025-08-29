import click
from models.model import session, Book,Customer,Sale
from crud.crud import add_book , delete_book, get_all_books,add_customer,get_all_customers,delete_customer,add_sale,get_all_sales,delete_sale,update_book


# Infinite loop to keep showing the menu until user exits
while True:
    #Main menu
    click.secho("BOOKSTORE INVENTORY AND SALES", fg="red")
    click.secho("1. Manage book", fg="blue")
    click.secho("2. Manage customers", fg="yellow")
    click.secho("3. Update sales", fg="green")
    click.secho("4. Exit",fg="yellow")

  #prompt user for a choice
    user_input =click.prompt ("Enter oPtion", type=int)
    click.secho(f"You have entered option {user_input}")

    if user_input == 1:
        click.secho("1. Add book",fg="blue")
        click.secho("2. view book", fg="red")
        click.secho("3. Delete book",fg="yellow")
        click.secho("4. Update book",fg="green")
        user_selection = click.prompt("Enter option 1 . 2 , 3 or 4",type=int)
        
        #Add a book
        if user_selection == 1:
            book_title = click.prompt("Enter book tittle")
            book_author = click.prompt ("Enter book author")
            book_price = click.prompt("Enter book price",type=int)
            book_stock = click.prompt("Enter book stock",type=int)
            add_book (book_title,book_author,book_price,book_stock)

            click.secho(f"books added successfully",fg="red")
        
        #View books
        if user_selection == 2:

         click.secho(f"All books in the inventory",fg="green")
         get_all_books()
        
        #delete a book
        if user_selection ==3:
          book_id = click.prompt("Enter book ID to delete", type=int)
          delete_book( book_id)
        
          click.secho(f"book deleted successfully",fg="red") 
        
        #update a book
        if user_selection ==4:
           book_id = click.prompt("Enter book ID to update", type=int)
           title = click.prompt("Enter new title", default="", show_default=False)
           author = click.prompt("Enter new author", default="", show_default=False)
           price = click.prompt("Enter new price", default="",show_default=False)
           stock = click.prompt("Enter new stock", default="",show_default=False)

           update_book(
            session,
            book_id, 
            title if title else None, 
            author if author else None, 
            int(price) if price.strip() else None, 
            int(stock) if stock else None
        )



    if user_input == 2:
       click.secho("1. Add customer",fg="blue")
       click.secho("2. view customer", fg="red")
       click.secho("3. Delete customer",fg="yellow")          
      
       user_selection = click.prompt("Enter option (1, 2 or 3)", type=int)
       
       #Add new customer
       if user_selection ==1:
          name = click.prompt("Enter customer name")
          email = click.prompt("Enter customer email")
          address = click.prompt("Enter customer address")
          add_customer( name, email,address)

          click.secho(f"customer added successfully")

        #View all customers
       if user_selection ==2: 
           click.secho(f"All customers",fg="green") 
           get_all_customers()
         
         #delete customer
       if user_selection ==3:  
           customer_id = click.prompt("Enter customer ID to delete", type=int)
           delete_customer(customer_id)

           click.secho(f"customer deleted successfully")




    if user_input ==3: 
       click.secho("1. Add sales",fg="blue")
       click.secho("2. view sales", fg="red")
       click.secho("3. Delete sales",fg="yellow") 

       user_selection = click.prompt("Enter option (1, 2 or 3)", type=int)
       
       #Add new sale
       if user_selection ==1:
            
            customer_id = click.prompt("Enter customer ID", type=int)
            book_id = click.prompt("Enter book ID", type=int)
          
            sale_date = click.prompt("Enter sale date(DD-MM-YYYY)")
            description = click.prompt("Enter sale description")
            add_sale( customer_id, book_id,sale_date,description)

            click.echo(f"Sale added successfully")
        
        #view sales
       if user_selection == 2:
             click.secho(" All Sales:", fg="yellow")
             get_all_sales()
        
        #delete sales
       if user_selection == 3:
             sale_id = click.prompt("Enter sale ID to delete", type=int)
             delete_sale(sale_id)
             click.secho(f"Sale deleted succussfully")
             
    elif user_input == 4: 
       click.secho(f"EXITING",fg="red")
       break        
           


    





   