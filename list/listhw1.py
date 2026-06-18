x = [101, 57, 6, 98, 32, 10, 57, 98]
y = []

while len(x) > 0:
    small = x[0]

    for i in x:
        if i < small:
            small = i

    y.append(small)
    x.remove(small)

print(y)



x = [101, 57, 6, 98, 32, 10, 57, 98]
for i in x:
    if i % 2 == 0:
        print(0)
    else:
        print(1)
print()


