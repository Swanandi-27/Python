#receives dynamic instance value
class mobile:
    def __init__(self,uname,ubrand,ucolor,uprice):
        self.name=uname
        self.brand=ubrand
        self.color=ucolor
        self.price=uprice


obj=mobile("iphone15","iphone","black","100")
obj1=mobile("iphone16","iphone","purple","200")
print(obj.name,obj.brand,obj.color,obj.price)
print(obj1.name,obj1.brand,obj1.color,obj1.price)

x=[obj,obj1]
for i in x:
    print(i.name)
