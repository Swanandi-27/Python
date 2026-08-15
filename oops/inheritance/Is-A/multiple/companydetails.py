class company:
    def __init__(self,dept,role,cname):
        self.dept=dept
        self.role=role
        self.cname=cname

    def diaplay_company(self):
        print("========company details=========")
        print(f"department:{self.dept}\nRole:{self.role}\ncompany_name:{self.cname}")


    def show(self):
            print("Hello i am from company class")