from Menus.dept_menu import *
from Menus.student_menu import *
from Menus.sstudent_menu import *
from services.Student1_services import *
choice=int(input("Welcome to CMC \n1.admin\n2.student\n3.exit\n.enter your choice:"))
match choice:
    case 1:
        ip=int(input("1.DEPT\n2.Student\n3.Exit \nenter your choice:"))
        match ip:
            case 1:
                dept_menu()
            case 2:
                student_menu()
            case 3:
                print("exit from dept....")
                exit()
            case _:
                print("Invalid choice")

    case 2:
        sstudent_menu()
    case 3:
        exit()
    case _:
        print("Invalid choice")
                
                
                
