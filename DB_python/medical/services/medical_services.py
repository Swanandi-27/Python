from models.medical import medical
from openpyxl import Workbook
from db import conn,cursor
from rich.panel import Panel
from rich.console import Console
from rich.table import Table

console = Console()

def add_medicine():
    medicine=input("Enter medicine name: ")
    category=input("Enter medicine category: ")
    manufacturar=input("Enter manufacturar name: ")
    quantity=int(input("Enter quantity: "))
    price=float(input("Enter price: "))
    expiry=input("Enter expiry date (YYYY-MM-DD): ")
    supplier=input("Enter supplier name: ")
    query = "INSERT INTO medicines (medicine, category, manufacturar, quantity, price, expiry, supplier) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values=(medicine, category, manufacturar, quantity, price, expiry, supplier)
    cursor.execute(query, values)
    
    conn.commit()
    console.print("[green]Medicine added sucessfully.[/green]")

def view_medicines():
    query="select * from medicines"
    cursor.execute(query)
    rows=cursor.fetchall()
    if not rows:
        console.print("[yellow]no medicines found.[/yellow]")
        return

    table=Table(title="Medical stock")

    table.add_column("ID",justify="center")
    table.add_column("Medicine",justify="left")
    table.add_column("Category",justify="left")
    table.add_column("Manufacturar",justify="left")
    table.add_column("Quantity",justify="left")
    table.add_column("price",justify="left")
    table.add_column("Expiry",justify="left")
    table.add_column("Supplier",justify="leftt")


        
    for i in rows:
        table.add_row(
            str(i[0]),
            str(i[1]),
            str(i[2]),
            str(i[3]),
            str(i[4]),
            str(i[5]),
            str(i[6]),
            str(i[7])
            )
    console.print(table)



def search():
    menu = Table(
            title="[bold]Search[/bold]",
            show_header=False,
            box=None,
            padding=(0, 2)
        )


    menu.add_column(justify="left", width=30)
    menu.add_column(justify="left", width=30)

    menu.add_row(
        "[bold cyan][1][/bold cyan]Search BY ID"
        
    )

    menu.add_row(
        "[bold cyan][2][/bold cyan]Search BY Medicine Name "
    )

    menu.add_row(
        "[bold cyan][3][/bold cyan] Search by Manufacturar"
    )
    menu.add_row(
            "[bold cyan][4][/bold cyan] Search by Expiry"
        )

    menu_panel = Panel(
            menu,
            border_style="green",
            padding=(1, 2)
        )
    
    console.print(menu_panel) 
    console.print()

    choice = console.input(
        "[bold yellow]Enter your choice: [/bold yellow]"
    )

    match choice:

        case "1":
            medicine_id = console.input(
                "[bold yellow]Enter Medicine ID: [/bold yellow]"
            )

            query = "SELECT * FROM medicines WHERE medicine_ID = %s"
            cursor.execute(query, (medicine_id,))
            rows = cursor.fetchall()

        case "2":
            medicine = console.input(
                "[bold yellow]Enter Medicine Name: [/bold yellow]"
            )

            query = "SELECT * FROM medicines WHERE medicine LIKE %s"
            cursor.execute(query, (medicine,))
            rows = cursor.fetchall()

        case "3":
            manufacturar = console.input(
                "[bold yellow]Enter Manufacturar Name: [/bold yellow]"
            )

            query = "SELECT * FROM medicines WHERE manufacturar LIKE %s"
            cursor.execute(query, (manufacturar,))
            rows = cursor.fetchall()

        case "4":
            expiry = console.input(
                "[bold yellow]Enter Expiry Date (YYYY-MM-DD): [/bold yellow]"
            )

            query = "SELECT * FROM medicines WHERE expiry = %s"
            cursor.execute(query, (expiry,))
            rows = cursor.fetchall()

        case _:
            console.print("[red]Invalid choice![/red]")
            return

    # Display result
    if not rows:
        console.print("[red]No medicines found![/red]")
        return

    table = Table(title="Search Results")

    table.add_column("ID", justify="center")
    table.add_column("Medicine")
    table.add_column("Category")
    table.add_column("Manufacturar")
    table.add_column("Quantity", justify="center")
    table.add_column("Price", justify="right")
    table.add_column("Expiry", justify="center")
    table.add_column("Supplier")

    for medicine in rows:
        table.add_row(
            str(medicine[0]),
            str(medicine[1]),
            str(medicine[2]),
            str(medicine[3]),
            str(medicine[4]),
            str(medicine[5]),
            str(medicine[6]),
            str(medicine[7])
        )

    console.print(table)


def expiry_alerts():
    query = """
        SELECT * FROM medicines
        WHERE expiry BETWEEN CURDATE()
        AND DATE_ADD(CURDATE(), INTERVAL 30 DAY)
    """

    cursor.execute(query)
    rows = cursor.fetchall()

    if not rows:
        console.print("[green]No medicines expiring within 30 days.[/green]")
        return

    table = Table(title="Expiry Alerts")

    table.add_column("ID", justify="center")
    table.add_column("Medicine")
    table.add_column("Category")
    table.add_column("Manufacturar")
    table.add_column("Quantity", justify="center")
    table.add_column("Price", justify="right")
    table.add_column("Expiry", justify="center")
    table.add_column("Supplier")

    for i in rows:
        table.add_row(
            str(i[0]),
            str(i[1]),
            str(i[2]),
            str(i[3]),
            str(i[4]),
            str(i[5]),
            str(i[6]),
            str(i[7])
        )

    console.print(table)


def low_stock():
    query = """
        SELECT * FROM medicines
        WHERE quantity < 10
    """

    cursor.execute(query)
    rows = cursor.fetchall()

    if not rows:
        console.print("[green]No medicines are low in stock.[/green]")
        return

    table = Table(title="Low Stock Alerts")

    table.add_column("ID", justify="center")
    table.add_column("Medicine")
    table.add_column("Category")
    table.add_column("Manufacturar")
    table.add_column("Quantity", justify="center")
    table.add_column("Price", justify="right")
    table.add_column("Expiry", justify="center")
    table.add_column("Supplier")

    for i in rows:
        table.add_row(
            str(i[0]),
            str(i[1]),
            str(i[2]),
            str(i[3]),
            str(i[4]),
            str(i[5]),
            str(i[6]),
            str(i[7])
        )

    console.print(table)


def delete_medicine():
    medicine_id = console.input(
        "[bold yellow]Enter Medicine ID to delete: [/bold yellow]"
    )

    query = "DELETE FROM medicines WHERE medicine_id = %s"

    cursor.execute(query, (medicine_id,))
    conn.commit()

    if cursor.rowcount > 0:
        console.print("[green]Medicine deleted successfully.[/green]")
    else:
        console.print("[red]Medicine ID not found.[/red]")




def export_to_excel():
    query = "select * from medicines"
    cursor.execute(query)
    rows=cursor.fetchall()
    if not rows:
        console.print("[yellow]No medicinnes to export[/yellow]")
        return

    workbook = Workbook()
    sheet=workbook.active
    sheet.title="medical Stock"

    headers = [
        "ID",
        "Medicine",
        "Category",
        "Manufacturar",
        "Quantity",
        "price",
        "Expiry",
        "Supplier"

    ]
    sheet.append(headers)

    for i in rows:
        sheet.append(list(i))
    workbook.save("Medical_Stock.xlsx")

    console.print("[green]Medical stock exported to EXcel Sucessfully[/green]")

