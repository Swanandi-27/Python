menu=((1,"paneer",400),(2,"chinese",350),(3,"brownnie",250 ),(4,"nachos",350))
order=[]
while True:
    print("1.view menu\n2.order\n3.view order\n4.generate bill\n5.exit")
    ch=int(input("enter your choice"))
    match ch:
        case 1:
            print("items are:")
            print("item no\t\t\titemn name\t\titem price")
            for i in menu:
                print(f"{i[0]}\t\t\t{i[1]}\t\t\t{i[2]}")

        case 2:
            
            item_no=int(input("Enter item no: "))

            for i in menu:
                if i[0] == item_no:
                    qty=int(input("Enter quantity: "))
                    order.append([i[1], qty, i[2]])
                    break

            print(order)
        case 3:
            print("View order")
            for i in order:
                print(i)
            add=input("do you want to add more items(yes/no)")
            if add.lower() =="yes":
                item_no=int(input("Enter item no: "))
                for i in menu:
                    if i[0] == item_no:
                        qty=int(input("Enter quantity: "))
                        order.append([i[1], qty, i[2]])
                        break
                print(order)
                



            

        case 4:
            total=0
            print("Item\t\tQty\tPrice\tAmount")
            for i in order:
                amount = i[1] * i[2]
                total += amount
                print(f"{i[0]}\t\t{i[1]}\t{i[2]}\t{amount}")

            print("----------------------------")
            print("Total Bill =", total)

            
            
        case 5:
            print("Thnak you visit again")
            exit()

            
        case _:
            print("Invalid choice:")