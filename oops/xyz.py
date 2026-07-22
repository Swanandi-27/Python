class demo:  #to create empty class
    def __init__(self):
        print("default constructor called")


#objname=classname()
obj=demo()

#constrcutore are of 2 types
#1 default cons ->high priority->obj creation
#para connstructor -->high priority ->

#method to create constructoe --init--
#def --init--():

#variables 
#1)class variables -->data which we are going to use allover  

class demo1:
    ins_name="linkcode"

obj=demo1()

#access class variable using class name
print(demo1.ins_name)

#access calass variable using obj
print(obj.ins_name)
print()

#2)instance variable 
class demo2:
    #instance variable 
     def __init__(self):
            self.name="swanandi"
            self.age=20

obj=demo2()
print(obj.name)
print(obj.age)