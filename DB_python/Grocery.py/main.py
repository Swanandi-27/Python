from productCRUD import *
adminUname="admin"
adminPass="1234"

print("\n1Admin\n2.Customer")
choice=int(input("enter your choice:")) 
match choice:
    case 1:
        username=input("enter username:")
        password=input("enter passworkd:")
        if username==adminUname and password==adminPass:
            while True:
                print("\n1.Add Product\n2.View All Products\n3.Search Product\n4.Update product Details \n5.Delete product\n6.Exit")
                ch=int(input("enter your choice:"))
                match ch:
                    case 1:
                        add()
                    case 2:
                        view()
                    case 3:
                        search()
                    case 4:
                        update()
                    case 5:
                        delete()
                    case 6:
                        break
                    case _:
                        print("Invalid choice")
            else:
                print("Invalid username or password")


    case 2:
        while True:
            print("\n1. View Products")
            print("2. Search Product")
            print("3. Add To Cart")
            print("4. View Cart")
            print("5. Generate Bill")
            print("6. Exit")

            ch = int(input("Enter Choice: "))

            match ch:
                case 1:
                    view()
                case 2:
                    search()
                case 3:
                    add_to_cart()
                case 4:
                    pass
                    view_cart()
                case 5:
                    pass
                    generate_bill()
                case 6:
                    break
                case _:
                    print("Invalid Choice")


