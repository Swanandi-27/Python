print()
x="hello"
for i in range(len(x)-1,-1,-1):
    v=x[i]
    print(v,end="")
print()

s = "maharashtra"

print("Even position characters:")
for i in range(len(s)):
    if i % 2 == 0:
        print(s[i], end=" ")

print("\nOdd position characters:")
for i in range(len(s)):
    if i % 2 != 0:
        print(s[i], end=" ")

print("\nVowels:")
for ch in s:
    if ch=="a" or ch=="i" or ch=="o" or ch=="e" or ch=="u":
        print(ch)


s = "hello"

for ch in s:
    if 'a' <= ch <= 'z':
        print(chr(ord(ch) - 32), end="")
    else:
        print(ch, end="")


print()
s = "maha rash tra"
result = ""

for ch in s:
    if ch != " ":
        result += ch

print(result)


s = "python_programming"
temp = ""

for ch in s:
    if ch == 'p':
        temp = temp + 'x'
    else:
        temp = temp + ch

print(temp)




