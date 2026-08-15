from p1 import p1
from p2 import p2
class child(p1,p2):
    def __init__(self):
        print("Child con called")
        p1.__init__(self)
        p2.__init__(self)

c=child()
