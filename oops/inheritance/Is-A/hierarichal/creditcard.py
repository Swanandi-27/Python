from payment import payment
class credit(payment):
    def pay(self):
        super().payment_details()
        
        print("payment done by credit card ")

c=credit(5000)

c.pay()
