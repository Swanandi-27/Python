x=[]
print(x)
print(type(x))

x=[10,20,30]
print(x)
#access element in list
print(x[1])
#update element in the list 
print("update")
print(x[2])
x[2]=300
print(x[2])
#acess lemets of list one by one 
print("access list elemts using loop")
y=[10,20,30]
for i in y:
    print(i)

#add elemst in the list taking user i/p
#s=[]
#for i in range(5):
#    p=input(f"enter {i+1} elemnt")
#    s.append(p)
#print(s)

#extend-->
x=[1,2]
print(x)
x.extend([3,4,5])
print(x)

#insert(index,value)--->
d=[11,13]
d.insert(1,12)
print(d)

#remove(element)/pop(index)
e=[10,8,9,"hi",90,89]
e.remove("hi")
print(e)
e.pop(4)
print(e)
e.clear()#empty the entire string
print(e)

#count elemts in the string ex=how many times 10 appear in the string 
f=[10,20,40,60,10,30]
print(f.count(10))
print(f.index(30))#return the index of the elemt in the string
f.sort()#sorts the givent string
print(f)
f.reverse()#reverse the given string
print(f)

y=f.copy()
print(y)
