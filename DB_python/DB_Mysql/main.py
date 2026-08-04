from CRUD import *



while True:
    print("\n----- MENU -----")
    print("1. Add Student")
    print("2. Search by Age")
    print("3. Search Name")
    print("4. Display Even ID Students")
    print("5. Count Records")
    print("6. Max Age Student")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            add()
        case 2:
            age()
        case 3:
            search_name()
        case 4:
            even_id()
        case 5:
            count_records()
        case 6:
            max_age()
        case 7:
            print("Thank You")
            break
        case _:
            print("Invalid Choice")