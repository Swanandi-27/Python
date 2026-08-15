from person  import person
class tester(person):
    def __init__(self, name, id, skills,age):
        super().__init__(name, id, skills)
        self.age=age


    def calculate_bonus(self):
        salary=int(input("enter your salary:"))
        bonus=salary*0.20
        super().bonus()
        print(bonus)
        print(f"your salary in this month will be {salary+bonus}")

    def testing(self):
        print("Im testing application")
