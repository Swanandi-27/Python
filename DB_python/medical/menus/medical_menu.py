from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.align import Align

console = Console()


def show_menu():
    console.clear()

    # Header
    header = Panel(
        Align.center(
            "[bold]💊 MEDICINE STOCK MANAGER[/bold]\n"
            "[italic]Pharmacy Inventory Management System[/italic]"
        ),
        border_style="blue",
        padding=(1, 2)
    )

    console.print(header)
    console.print()
 
    # Menu table
    menu = Table(
        title="[bold]MAIN MENU[/bold]",
        show_header=False,
        box=None,
        padding=(0, 2)
    )

    menu.add_column(justify="left", width=30)
    menu.add_column(justify="left", width=30)

    menu.add_row(
        "[bold cyan][1][/bold cyan] ➕ Add Medicine"
        
    )

    menu.add_row(
        "[bold cyan][2][/bold cyan] 📋 View Medicines"
    )

    menu.add_row(
        "[bold cyan][3][/bold cyan] 🔍 Search Medicine"
    )

    menu.add_row(
        "[bold cyan][4][/bold cyan] ✏️ Update Medicine"
    )

    menu.add_row(
        "[bold cyan][5][/bold cyan] 🗑️ Delete Medicine"
       
    )
    menu.add_row(
        "[bold cyan][6][/bold cyan] ⚠️ Low Stock"
    )
    menu.add_row("[bold cyan][7][/bold cyan] ⏰ Expiry Alerts"
                 )
    menu.add_row("[bold cyan][8][/bold cyan] 📊 Dashboard")
    menu.add_row(
        "[bold cyan][9][/bold cyan] 📤 Export to Excel")
    menu.add_row("[bold cyan][10][/bold cyan] 🚪 Exit")


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

    return choice