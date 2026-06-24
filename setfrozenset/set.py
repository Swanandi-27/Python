#set
#mutable
#unique
#{}
#unordered mutable 
#can provide duplicate values but provided the unique elemts only 
x={}
print(type(x))

#manual input in the user
x={10,20}
print(type(x))

#user input in set
x=set()  #to create empty set
x.add(10)
print(x)
print()

#accessing the set elemets using loop
y={10,20,30,40,10,20}
for i in y:
    print(i)


#functions and methods
#add
y.add(90)
print(y)


#remove if we peovide the nonexisting elemt to the remove it gives error
y.remove(40)
print(y)

#remove 
y.discard(7)#if we provide the nonexisting elemmt to the discard it provides the set as it is 
y.discard(30)
print(y)

#pop
y.pop()
print(y)

#clear emty the entire string
y.clear()
print(y)

#copy
a={1,2}
b=a.copy()
print(b)

#update receives only single elemt at a type
#a.update(10,20,30)
print(a)

#if you want to update the group of elemts at a time  then pass it in the list
a.update([10,20,30])
print(a)

print()

