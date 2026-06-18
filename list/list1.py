x=[10,20,30,40]
print(sum(x))
sum=0
for i in x:
    sum+=i
    print(sum)


print(len(x))
count=0
for i in x:
    count+=1
print(count)

print("maximum")
print(max(x))
max=0
for i in x:
    if i>max:
        max=i
print(max)

print("minimum")
print(min(x))
min=x[0]
for i in x:
    if i<min:
        min=i
print(min)




    