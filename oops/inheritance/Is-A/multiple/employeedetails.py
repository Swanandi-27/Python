from personaldetails import personal
from companydetails import company
class employee(personal,company):
    def __init__(self,name,city,age,dept,role,cname,salary):
        personal.__init__(self,name,city,age)
        company.__init__(self,dept,role,cname)
        self.salary=salary

    def display_emp_details(self):
        print("====All Information of Employee====")
        print()
        self.diaplay()
        print()
        self.diaplay_company()
        print()
        print(f"salary:{self.salary}")


    