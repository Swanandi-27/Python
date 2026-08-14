from A import A
class B(A):
    
    def abc(self):
        print("hello abc")

    def __init__(self):
        print("def constructor child")
obj=B()
# print(obj.roll_no)
# obj.xyz()
# obj.abc()
print(B.mro())