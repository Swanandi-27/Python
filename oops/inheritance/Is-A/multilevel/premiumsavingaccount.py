from savingaccount import savingaccount
class premium(savingaccount):
    def __init__(self, account_no, account_holder, balannce):
        super().__init__(account_no, account_holder, balannce)

    def  calculate_benefits(self):
       
        if self.balance>=5000:
            benefits=500
            choice=input("do you want to add the benefit amount to your account Type(Yes/No)")
            if choice=="Yes":
                self.balance+=benefits
            else:
                print("you can reward for benefits as yr choice")

            
        else:
            print("maintain basic limit of premium accounf limit Rs 2000")



obj=premium(1,"swanandi",10000)
print(obj.check_balance())
print(obj.deposite())
print(obj.withdraw())
print(obj.calculate_interest())
print(obj.apply_interesrt())