from parent import A
class B(A):
    def __init__(self):
        print("def B constructor ")
        super().__init__()

c1=B()
