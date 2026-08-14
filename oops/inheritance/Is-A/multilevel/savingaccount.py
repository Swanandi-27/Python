from bankaccount import bankaccount
class savingaccount(bankaccount):

    def __init__(self, account_no, account_holder, balannce):
        super().__init__(account_no, account_holder, balannce)
        self.interest_rate=0

    def calculate_interest(self):
        amount=int(input("enter amount to calculate"))
        month=int(input("enter months to fixed amount"))
        rate = float(input("Enter annual interest rate (%): "))

        self.interest_rate = (amount * rate * month) / (100 * 12)

        print("Interest:", self.interest_rate)
        print("Total Amount:", amount + self.interest_rate)

    def apply_interesrt(self):
        self.balance+=self.interest_rate
        return f"after adding interest  {self.interest_rate}  available balnce is {self.balance}"


