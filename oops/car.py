class car:
    brand="BMW"
    def __init__(self,name,model,wheel,price,avalbal):

        self.name=name 
        self.model=model
        self.wheel=wheel
        self.price=price
        self.avalbal=avalbal

obj=car("car1","X5","4",200,6)
print(obj.name,obj.brand,obj.model,obj.wheel,obj.price,obj.avalbal)

obj1=car("car2","X6","4",100,10)
print(obj1.name,obj1.brand,obj1.model,obj1.wheel,obj1.price,obj1.avalbal)

y=[obj,obj1]
for i in y:
    print("name:",i.name)
    print("brand:",i.brand)
    print("model:",i.model)
    print("price:",i.price)
    print("available:",i.avalbal)
    print("---------------------------------")


total=0
for i in y:
    total+=i.avalbal*i.price
print("total stock available :",total)

for i in y:
    if i.avalbal>5 and i.avalbal<10:
        print(i.name,i.avalbal)

 



