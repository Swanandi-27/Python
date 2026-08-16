from ATM import ATM
class SBIATM(ATM):
    def withdraw(self, amount):
       if amount>0:
           self.bal-=amount
           print(f"amount deducted:{amount}\navailable balance is: ",self.bal)


obj=SBIATM(10000)
print(obj.getbal())
obj.withdraw(2000)