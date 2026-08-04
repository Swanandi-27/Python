from Linkcode.CRUD import *
while True:
    print("\n1.Add Student\n2.View All Students \n3.Search\n4.Update\n5.Delet\n6.Exit")
    ch=int(input("Enter your choice:"))

    match ch:
        case 1:
            add_stud()
        case 2:
            view_all_stud()
        case 3:
            Search()
        case 4:
            update()
        case 5:
            delete()
        case 6:
            exit()
        case _:
            print("Invalid choice")

