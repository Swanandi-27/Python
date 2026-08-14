from A import GP
class P(GP):
    abc="Hey"
    def __init__(self, name,age):
        super().__init__(name)
        self.age=age