x=((10,20),(30,40))
print(x[1][0])
for i in x:
    print(i)

print()
for i in x:
    for j in i:
            print(j)
       
        
print()
x=((10,20),34,(40,50),"hi")
for i in x:
    if type(i)==tuple:
        for j in i:
            print(j)
        continue
        
    print(i)

print()
x=((10,20),34,(40,50),"hi",[10,20])
for i in x:
    if type(i)==tuple or type(i)==list:
        for j in i:
            print(j)
        continue
    else:    
        print(i)

print("_----------")
print("_----------")
x=(90,"hi",("red",[10,20]),[100,200])

for i in x:
    if type(i)==tuple or type(i)==list:
        for j in i:
            if type(j)==tuple or type(j)==list:
                for k in j:
                    print(k)
                continue
            print(j)
        continue
    print(i)
