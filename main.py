import click
from models.model import session
from crud.crud import (
    add_book, delete_book, get_all_books, update_book,
    add_customer, get_all_customers, delete_customer,
    add_sale, get_all_sales, delete_sale
)

while True:
    # Main Menu
    click.secho("=" * 50, fg="white")
    click.secho("BOOKSTORE INVENTORY AND SALES", fg="red")
    click.secho("=" * 50, fg="white")
    click.secho("1. Manage books", fg="blue")
    click.secho("2. Manage customers", fg="yellow")
    click.secho("3. Manage sales", fg="green")
    click.secho("4. Exit", fg="red")
    click.secho("-" * 50, fg="cyan")

    user_input = click.prompt("Enter option", type=int)
    click.secho("-" * 50, fg="white")

    # BOOKS MENU
    if user_input == 1:
        while True:
            click.secho("BOOK MENU", fg="blue")
            click.secho("1. Add book", fg="blue")
            click.secho("2. View books", fg="red")
            click.secho("3. Delete book", fg="yellow")
            click.secho("4. Update book", fg="green")
            click.secho("5. Back to Main Menu", fg="cyan")
            click.secho("-" * 50, fg="cyan")

            choice = click.prompt("Enter option (1-5)", type=int)

            if choice == 1:
                title = click.prompt("Enter book title")
                author = click.prompt("Enter book author")
                price = click.prompt("Enter book price", type=int)
                stock = click.prompt("Enter book stock", type=int)
                add_book(title, author, price, stock)
                click.secho("Book added successfully", fg="green")

            elif choice == 2:
                click.secho("All Books:", fg="yellow")
                get_all_books()

            elif choice == 3:
                book_id = click.prompt("Enter book ID to delete", type=int)
                delete_book(book_id)
                click.secho("Book deleted successfully", fg="red")

            elif choice == 4:
                book_id = click.prompt("Enter book ID to update", type=int)
                title = click.prompt("New title", default="", show_default=False)
                author = click.prompt("New author", default="", show_default=False)
                price = click.prompt("New price", default="", show_default=False)
                stock = click.prompt("New stock", default="", show_default=False)

                update_book(
                    session, book_id,
                    title if title else None,
                    author if author else None,

                    int(price) if price.strip() else None,
                    int(stock) if stock.strip() else None
                )
                click.secho("Book updated successfully", fg="green")

            elif choice == 5:  # Go back
                break
            else:
                click.secho("Invalid option, try again!", fg="red")

    # CUSTOMERS MENU
    elif user_input == 2:
        while True:
            click.secho("CUSTOMER MENU", fg="yellow")
            click.secho("1. Add customer", fg="blue")
            click.secho("2. View customers", fg="red")
            click.secho("3. Delete customer", fg="yellow")
            click.secho("4. Back to Main Menu", fg="cyan")
            click.secho("-" * 50, fg="cyan")

            choice = click.prompt("Enter option (1-4)", type=int)

            if choice == 1:
                name = click.prompt("Enter customer name")
                email = click.prompt("Enter customer email")
                address = click.prompt("Enter customer address")
                add_customer(name, email, address)
                click.secho("Customer added successfully", fg="green")

            elif choice == 2:
                get_all_customers()

            elif choice == 3:
                customer_id = click.prompt("Enter customer ID to delete", type=int)
                delete_customer(customer_id)
                click.secho("Customer deleted successfully", fg="red")

            elif choice == 4:  # Go back
                break
            else:
                click.secho("Invalid option, try again!", fg="red")

    # SALES MENU
    elif user_input == 3:
        while True:
            click.secho("SALES MENU", fg="green")
            click.secho("1. Add sale", fg="blue")
            click.secho("2. View sales", fg="red")
            click.secho("3. Delete sale", fg="yellow")
            click.secho("4. Back to Main Menu", fg="cyan")
            click.secho("-" * 50, fg="cyan")

            choice = click.prompt("Enter option (1-4)", type=int)

            if choice == 1:
                customer_id = click.prompt("Enter customer ID", type=int)
                book_id = click.prompt("Enter book ID", type=int)
                sale_date = click.prompt("Enter sale date (DD-MM-YYYY)")
                description = click.prompt("Enter sale description")
                add_sale(customer_id, book_id, sale_date, description)
                click.secho("Sale added successfully", fg="green")

            elif choice == 2:
                get_all_sales()

            elif choice == 3:
                sale_id = click.prompt("Enter sale ID to delete", type=int)
                delete_sale(sale_id)
                click.secho("Sale deleted successfully", fg="red")

            elif choice == 4:  # Go back
                break
            else:
                click.secho("Invalid option, try again!", fg="red")

    # EXIT PROGRAM
    elif user_input == 4:
        click.secho("Exiting...BYEEEE1!", fg="red")
        break
    else:
        click.secho("Invalid option. Try again!", fg="red")
