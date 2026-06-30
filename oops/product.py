from fpdf import FPDF
import smtplib
from email.message import EmailMessage
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
                        print()
                            
                

                
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

            for i in item:
                print(f"Product : {i[0]}")
                print(f"Brand   : {i[1]}")
                print(f"Qty     : {i[2]}")
                print(f"Price   : {i[3]}")
                print(f"Total   : {i[4]}")
                print("--------------------------")

            print(f"Grand Total = {final_total}")
            print("===============================")
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.cell(200,10,txt="shopping bill",ln=True,align="c")
            pdf.ln(10)
            for i in item:
                pdf.cell(200,10,txt=f"product:{i[0]}",ln=True)
                pdf.cell(200,10,txt=f"Brand:{i[1]}",ln=True)
                pdf.cell(200,10,txt=f"Quantity:{i[2]}",ln=True)
                pdf.cell(200,10,txt=f"Price:{i[3]}",ln=True)
                pdf.cell(200,10,txt=f"Total:{i[4]}",ln=True)
                pdf.cell(200,10,txt="---------------------",ln=True)

            pdf.cell(200,10,txt=f"Grand total:{final_total}",ln=True)
            pdf.output("bill.pdf")
            print("pdf created sucessfully")

            receiver = input("Enter buyer email: ")

            sender = "kachiswanandi@gmail.com"
            password = "zlfh nuyp ujho pbfn"

            msg = EmailMessage()
            msg["Subject"] = "Your Bill"
            msg["From"] = sender
            msg["To"] = receiver
            msg.set_content("Your bill is attached.")

            with open("bill.pdf", "rb") as f:
                file_data = f.read()

            msg.add_attachment(file_data, maintype="application", subtype="pdf", filename="bill.pdf")

            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(sender, password)
            server.send_message(msg)
            server.quit()

            print("Bill sent successfully")




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
