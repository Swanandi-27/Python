from vehicle import vehicle
class Bike(vehicle):

    def __init__(self, fuel_Type, brand,color,price):
        super().__init__(fuel_Type, brand)
        self.color=color
        self.price=price
        

    def ride(self):
        return "Bike ride to fast"

    def customer_start(self):
        print(super().start())
        return "BRUMMMHHHHHHHH"

b1=Bike("petrol","BMW","black",5000)
print(b1.color)
print(b1.fuel_Type)
print(b1.start())
print(b1.ride())
print(b1.stop())
print(b1.customer_start())
