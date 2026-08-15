from parent import A
class c(A):
    def __init__(self):
        print("def c constructor ")
        super().__init__()


c2=c()