from menus.medical_menu import *
from services.medical_services import *

while True:

    choice = show_menu()

    if choice == "1":
        add_medicine()

    elif choice == "2":
        view_medicines()

    elif choice == "3":
        search()

    elif choice == "4":
        print("Update Medicine")

    elif choice == "5":
        delete_medicine()

    elif choice == "6":
        low_stock()

    elif choice == "7":
        expiry_alerts()

    elif choice == "8":
        print("Dashboard")

    elif choice == "9":
        export_to_excel()

    elif choice == "10":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")