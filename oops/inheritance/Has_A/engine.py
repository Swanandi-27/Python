class engine:
    brand="ABC"
    def __init__(self,horsepower):
        self.name="V8"
        self.horsepower=horsepower


    def show_engine(self):
        return f"engine detials are:\n{self.brand} \n{self.name}\n{self.horsepower}"