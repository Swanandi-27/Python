#An exception is an error that occurs during runtime
print("Start Program")
try:
    print(10/0)
except ZeroDivisionError:
    print("Don't divide by zero")   #cutomized msg for error
print("Program end")
print("-----------")

print("Start Program")
try:
    ip=int(input("Enter number:"))
    print("Your number is:",ip)
except ValueError as e:         #use the in built error msg
    print(e)
print("Program end")
print("-----------")

print("Start Program")
try:
    x=[10,20]
    print(x[4])
except IndexError as e:         #use the in built error msg
    print(e)
print("Program end")
print("-----------")

print("Start program")
try:
    x=[10,20]
    print(x[4])
    print(10/5)
except IndexError as e:     #use separate exception blocks for each error
    print(e)
except ZeroDivisionError as e:
    print(e)
print("Program end")
print("------------")

print("Start program")
try:
    x=[10,20]
    print(x[4])
    print(10/0)
except Exception as e:      #using parent 'exception' class to handle all the errors without specifying each
    print(e)
print("Program end")
print("------------")

print("Start program")
try:
    ip=int(input("Enter your number:"))
    print(10/ip)
except (ValueError,ZeroDivisionError):      #using only one except block and adding multiple error chances in it
    print("Something went wrong")
print("Program end")
print("------------")


print("Start program")
try:
    ip=int(input("Enter your number:"))
    print(10/ip)
except (ValueError,ZeroDivisionError):      
    print("Something went wrong")
finally:
    print("i always execute")       #finally keyword(actions performed even if error is present or not)
print("Program end")
print("------------")

class AgeError(Exception):
    pass
print("Start program")
age=int(input("Enter your age:"))
if age>18:
    print("Eligible")
else:
    raise AgeError("Age should be gretaer than 18")     #create your own exception
print("Program end")
print("------------")

print("Start program")
try:
    age=int(input("Enter your age:"))
    if age<18:
        raise AgeError("Age should be gretaer than 18")
    print("You are eligible")
except Exception as e:      
    print(e)
print("Program end")
print("------------")