class demo:
    def __init__(self,name,ID,age):
        self.name=name
        self.ID=ID
        self.age=age
    
    #instannce method
    def welcomme(self):
        return "hello students"
    def modify(self):

        newval=input("enter new name:")
        exname=self.name

        print(f"existing name {exname} and updated name {newval}")
        


obj=demo("swanandi",101,20)
print(obj.name,obj.ID,obj.age)

print(obj.welcomme())

obj.modify()


