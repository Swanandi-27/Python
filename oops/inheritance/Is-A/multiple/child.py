from parent1 import p1
from parent2 import p2
class child(p1,p2):
    def __init__(self,c_name,p1name,p2name):
        self.c_name=c_name
        #constructor chaining
        #classname.__init__(self,p1mame)
        #super().__init__(p1name)

        p1.__init__(self,p1name)
        p2.__init__(self,p2name)




obj=child("swanandi","suvarna","anup")
print(obj.c_name)
print(obj.p1name)
print(obj.p2name)
