from person  import person
class developer(person):
    def __init__(self, name, id, skills,age):
        super().__init__(name, id, skills)
        self.age=age


    def calculate_bonus(self):
        salary=int(input("enter your salary:"))
        bonus=salary*0.15
        super().bonus()
        print(bonus)
        print(f"your salary in this month will be {salary+bonus}")

    def developing(self):
            print("Im writing code ")
    


