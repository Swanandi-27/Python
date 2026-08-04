from services.Student1_services import *
def student_menu():
    choice=int(input("1.ADD\n2.update\n3.read\n4.delete\n5.exit\n enter your choice"))
    match choice:
        case 1:
            add_student()
        case 2:
            pass
        case 3:
            read_student()
        case 4:
            pass
        
        case 5:
            print("exit from Student  menu!")
        case _:
            print("Invalid choice")