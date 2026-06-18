x = [101, 57, 6, 98, 32, 10, 57, 98]

key = int(input("Enter key: "))
if key in x:
    print("present")
else:
    print("not present")
print()

print("duplicate keys")

x = [101, 57, 6, 98, 32, 10, 57, 98]
y = []

for i in x:
    if x.count(i) > 1 and i not in y:
        print(i)
        y.append(i)


print("unique keys")
x = [101, 57, 6, 98, 32, 10, 57, 98]
 
for i in x:
    if x.count(i)<=1:
        print(i)

print()



x = [101, 57, 6, 98, 32, 10, 57, 98]
y = []

while len(x) > 0:
    min = x[0]

    for i in x:
        if i < min:
            min = i

    y.append(min)
    

print(y)
print()


x = [101, 57, 6, 98, 32, 10, 57, 98]
s=[]
for i in x:
    if i % 2 == 0:
        s.append(0)
    else:
        s.append(1)       
print(s)