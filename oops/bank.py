class bank:
    bankname="SBI"
    Ifsc_code="SBI0012340"
    def __init__(self,name,bal,mail):
        self.name=name
        self.bal=bal
        self.mail=mail

    def show(self):
        print(f"name:{self.name}\nbalance:{self.bal}\nemail:{self.mail}\nBank_name:{self.bankname}\nifsc:{self.Ifsc_code}")

    def checkbal(self):
        print("balance is:",self.bal)

    def deposite(self):

        amount=int(input("enter amount you want to deposite:"))
        if amount>0:
            self.bal+=amount
            print("total balance is :",self.bal)

    def withdraw(self):

        amount=int(input("enter amount you want to withdarw:"))
        if amount>self.bal:
            print("insufficient balance")
        else:
            self.bal-=amount
            print("total balance is :",self.bal)

    def fd(self):
        amount=int(input("enter the amount you want to fix deposite"))
        month=int(input("Choose FD months (3 / 6 / 12): "))
        if amount>self.bal:
            print("Insufficieence balance")
        elif month==3:
            final_amount = amount + (amount * 7 / 100)
            print("maturity amount:",final_amount)
        elif month==6:
            final_amount = amount + (amount * 10 / 100)
            print("maturity amount:",final_amount)

        elif month==12:
            final_amount = amount + (amount * 12 / 100)
            print("maturity amount:",final_amount)
        else:
            print("invalid choice")

    def rich(self,y):
        if y[0].bal > y[1].bal:
            y[0].show()

        elif y[1].bal > y[0].bal:
            y[1].show()

        else:
            print("Both have same balance")



        




    




        

user1=bank("swanandi",1500,"@123")
user2=bank("aastha",1000,"a@2005")
y=[user1,user2]
user1.show()
user1.checkbal()
user1.deposite()
user1.withdraw()
user1.fd()
print()
user1.rich(y)

 