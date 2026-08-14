from engine import engine
class car:
    def __init__(self,uip):
        self.color="black"
        self.e=engine(uip)

    def car_details(self):
        print(self.e.show_engine())
        return f"car details are: \n{self.color}"


obj=car(200)
print(obj.e.name,obj.e.horsepower)
print(obj.car_details())
#print(obj.e.show_engine())