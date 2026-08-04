from services.Student1_services import *
def sstudent_menu():
    print("\n1.update\n2.view\n3.view department name\n4.search\n5.exit")
    ch =  int(input("enter your choice"))
    match ch:
        case 1:
            update_student()
        case 2:
            read_student()
        case 3:
            view_student_department()
        case 4:
            search_student()
        case 5:
            exit()
        case _:
            print("Invalid choice")