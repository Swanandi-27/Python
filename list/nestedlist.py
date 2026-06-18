#List         || nested list
#[]           || [[],[],[]]

x=[[10,20],[11.2,12.3]]
print(x[1])
print(x[1][1])


x=[[10,20],[11.2,12.3],"hi",90]
print(x[2])

print()
for i in x:
    print(i)
print()
#accessing nested list elements
for i in x:
    if type(i)==list:
        for j in i:
            print(j)
        continue
        
    print(i)


print()
s=[[10,20],[30,40],[60,70]]
for i in s:
    print(i[0])


print()
s=[[10,20],[30,40],[60,70]]
for i in s:
    print(i[1])

 