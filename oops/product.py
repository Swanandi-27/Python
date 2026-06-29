class product1:
    def __init__(self,name,brand,mfg,exp,qty,price):
        self.name=name
        self.brand=brand
        self.mfg=mfg
        self.exp=exp
        self.qty=qty
        self.price=price

obj=product1("panipuri masala","MDH","29-06-2026","20-07-2026",10,150)
obj1=product1("pavbhaji masala","MDH","29-06-2026","22-07-2026",20,200)
obj2=product1("pavbhaji masala","Suhana","29-06-2026","22-07-2026",20,210)
y=[obj,obj1,obj2]


while True:
    print("\n1.all products\n2.search product\n3.generate bill\n4.Exit")
    choice=int(input("enter your choice:"))
    match choice:
        case 1:
            
            for i in y:
                print(f"name:{i.name}\nbrand:{i.brand}\nMFG:{i.mfg}\nEXP:{i.exp}\nQty:{i.qty}\nPrice:{i.price}")
                print("=========================================")
        case 2:
            print("\n1.brand\n2.name\n")
            ch=int(input("enter your choice:"))
            match ch:
                case 1:
                    brand=input("enter your brand:")
                    found=False
                    for i in y:
                        found=True
                        if i.brand == brand:
                            print(f"name:{i.name}\nbrand:{i.brand}\nMFG:{i.mfg}\nEXP:{i.exp}\nQty:{i.qty}\nPrice:{i.price}")
                            print("===============================")
                    if found==False:
                        print("brand not found")
                case 2:
                    name=input("enter the name of product:")
                    found=False
                    for i in y:
                        found=True
                        if i.name==name:
                            print(f"name:{i.name}\nbrand:{i.brand}\nMFG:{i.mfg}\nEXP:{i.exp}\nQty:{i.qty}\nPrice:{i.price}")
                            print("===============================")
                    if found==False:
                        print("product  not found")
                            
                

                
                case _:
                    print("Invalid Choice")
                    

        case 3:
            final_total=0
            item=[]

            while True:
                name=input("Enter product name: ")
                brand=input("Enter brand: ")
                qty=int(input("Enter quantity: "))

                found=False

                for i in y:
                    if i.name == name and i.brand == brand:
                        found=True

                        if i.qty >= qty:
                            total = qty * i.price
                            final_total += total
                            item.append([i.name,i.brand,i.qty,i.price,total])

                            print("\nProduct added successfully")
                            

                            i.qty -= qty
                        else:
                            print("Insufficient stock")
                        break

                if found==False:
                    print("Product not found")

                ch=input("Do you want to add more items? (yes/no): ")

                if ch.lower() == "no":
                    break

            print("\n========== FINAL BILL ==========")

            for item in item:
                print(f"Product : {item[0]}")
                print(f"Brand   : {item[1]}")
                print(f"Qty     : {item[2]}")
                print(f"Price   : {item[3]}")
                print(f"Total   : {item[4]}")
                print("--------------------------")

            print(f"Grand Total = {final_total}")
            print("===============================")



        case 4:
            exit()
            


        
















#hw 
#class product
#       name,brand,mfg,exp,qty,price
# operations - 1) all detailes 
#              2)search
#                       1)brand
#                       2)name
#                       3)price
#  acording to brand name ex"suhaha" show all suhana products 

#purchase -->generate bill 
#then after bill generation qty will automatically get updated


#hw 
#try to download the bill with .pdf extension
#send the bill pdf to user email
