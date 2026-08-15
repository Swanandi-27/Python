class payment:
    def __init__(self,amount):
        self.amount=amount

    def payment_details(self):
        print("Payment processing .....")
        print(f"payment amount:{self.amount}")