from B import P
class c(P):
    pqr="Bye"

    def __init__(self, name, age,marks):
        super().__init__(name, age)
        self.marks=marks

obj=c("swanandi",20,90)
print(obj.pqr,obj.abc,obj.xyz)
print(obj.name,obj.age,obj.marks)

