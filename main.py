import click
from models.model import session, Book,Customer,Sale
from crud.crud import add_book , delete_book, get_all_books


while True:
    click.secho("BOOKSTORE INVENTORY AND SALES", fg="red")
    click.secho("1. Manage book", fg="blue")
    click.secho("2. Manage customers", fg="yellow")
    click.secho("3. Update sales", fg="green")
    click.secho("4. Exit",fg="yellow")

    user_input =click.prompt ("Enter OPtion", type=int)
    click.secho(f"You have entered option {user_input}")

    if user_input == 1:
        click.secho("1.Add book",fg="blue")
        click.secho("2. Delete book", fg="red")
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

    if user_selection ==3:
          book_id = click.prompt("Enter book ID to delete", type=int)
          delete_book(session, book_id)
        
    click.secho(f"book deleted successfully",fg="red")    

    




   