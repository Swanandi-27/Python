from A import A
class B:
    def __init__(self):
        self.age=20
        self.a=A()

obj=B()
print(obj.age,obj.a.name)
print(obj.a.x)
