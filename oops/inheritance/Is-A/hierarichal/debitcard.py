from payment import payment
class debit(payment):
    def pay(self):
        super().payment_details()
        
        print("payment done by debit card ")

d=debit(5000)

d.pay()
