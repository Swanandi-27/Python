#tuple is immutable
#indexing starts from 0
#size starts from 1
#represented with ()
#used to store fixed data


x=(10,20,30)
print(type(x))
print(x[2])
print()
for i in x:
    print(i)

print()
x=("red","blue","white")
print("red" in x)
print("grey" in x)

print()
x=(10,20)
y=(10,20)
z=x
print(x is y)
print(x is z)


print()
#tuple packing and unpacking
x=(10,20,30)  #packing
a,b,c=x  #unpacking
print(a,b,c)
