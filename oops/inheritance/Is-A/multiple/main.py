from employeedetails import employee
from personaldetails import personal
from companydetails import company
obj=employee("swanandi","pune",20,"IT","Data Scientist","Microsoft","200000")

obj.display_emp_details()
obj.show()#--->mro-->child-->parent1-->parent2--obj

#same method present in both the classes
#classname.methodnamme(obj)
personal.show(obj)
company.show(obj)
#print(employee.mro())