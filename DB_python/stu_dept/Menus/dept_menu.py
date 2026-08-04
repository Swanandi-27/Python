from services.dept_services import *
def dept_menu():
    choice=int(input("1.ADD\n2.update\n3.read\n4.delete\n5.exit\n enter your choice"))
    match choice:
        case 1:
            add_dept()
        case 2:
            update()
        case 3:
            read_dept()
        case 4:
            delete_dept()
        
        case 5:
            print("exit from department menu!")
        case _:
            print("Invalid choice")