x="india"  #[st:end:step]
print(x[3:5])
print(x[1:4])
print(x[2:])
print(x[:3])
print(x[0:5:2])
print()
x="india is my country!"
print(x[6:8])
print(x[12:17])
print(x[7:10])
print(x[16:])
print(x[-10:-15:-1])
print(x[::-1])

print()
ip=input("enter a string:")
if ip==ip[::-1]:
    print("palindrome")
else:
    print("not palindrome")


#count digit and char from the given string 
s="abc1234"
count=0
chr_count=0
for ch in s:
    if(ch>='0' and ch<='9'):
        count+=1
    
    if(ch>='a' and ch<='z'):
        chr_count+=1
print("character count",chr_count)
print("digit count",count)


s="abc1234"
count=0
chr_count=0
for ch in s:
    if ch.isdigit():
        count+=1
    
    if ch.isalpha():
        chr_count+=1

print("character count",chr_count)
print("digit count",count)


#charcater to ascii value and ascii value ti char
print(ord('a'))
print(chr(97))

#lower case to upper case 
w="abc"
for i in w:
    print(chr(ord(i)-32))

a="hello"
a_new=""
for i in a:
    if i>='a' and i<='z':
        a_new+=(chr(ord(i)-32))
print(a_new)

a = "sWapCaSe"
a_new = ""
for i in a:
    if i >= 'A' and i <= 'Z':
        a_new += chr(ord(i) + 32)
    else:
        a_new += i
print(a_new)


a="sWapCaSe"
a_new=""
for i in a:
    if i>='a' and i<='z':
        a_new+=(chr(ord(i)-32))
    elif i>='A' and i<='Z':
        a_new+=(chr(ord(i)+32))

    
print(a_new)
print()


s = "programming"
for i in  s:
    if ord(i) % 2 == 0:
        print(i)
        

x="programming"
print(len(x))
new=""
for ch in x:
    if ch not in new:
        new+=ch
        
print("ans",new,len(new))



x="hi"
print(len(x))
new=""
for ch in x:
    if ' ' not in ch:
        new+=ch
print("ans",new,len(new))