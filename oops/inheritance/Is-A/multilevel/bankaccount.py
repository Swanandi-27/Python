class bankaccount:
    def __init__(self,account_no,account_holder,balance):
        self.account_no=account_no
        self.account_holder=account_holder
        self.balance=balance

    def deposite(self):
        amount=int(input("enter amountto deposite:"))
        self.balance+=amount
        return f"available balance after depositr {self.balance}"

    def withdraw(self):
        amount=int(input("enter amount to withdrwa"))
        if amount>0:
            self.balance-=amount
            return f"available balance  after withdraw:{self.balance}"

    def check_balance(self):
        return f"available balnce :{self.balance}"

        