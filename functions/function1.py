#functions
#1)build-in funnction  ex len() sum() mx()

#2)user defined function
#types of user defined functions

#1) not return type no argument
def greet():  #function define
    print("welcome!")
 
greet()  #function calling

#we use parameters at the time of declartions
#we use argument at the time of function calling

#2)no return type with argument
def greet1(ip):
    print("welcome",ip)

name=input("enter your name:")
greet1(name)

#3)#with return type without argument
def getno():
    return 10**2

#getno() does not show any o/p
op=getno()  #1st way for calling

print(op)

print(getno())#second way of calling

#4)with return type with argumennt
def cube(num):
    cube1=num**3
    return cube1
num=int(input("enter your num"))
print(cube(num))


#addition of 2 numbers

def add(a,b):
    print(a+b)

a=int(input("enter one number"))
b=int(input("enter second umber:"))
add(a,b)

#*args (arbitary arument) receives multiple inputs
def add1(*args):
    print(sum(args))
    print(type(args))

add1(1,2,4,5,6,8,9)


def infor(name,age,marks):
    return f"name:{name}\nage:{age}\nmarks:{marks}\n"

name=input("enter your name:")
age=int(input("enter your age"))
marks=float(input("enter your marks"))
print(infor(name,age,marks))
