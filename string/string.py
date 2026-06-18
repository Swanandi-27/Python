#String =immutable nature (cannot be changed) 
name="ram"
print(name)
print(id(name))
print(name[2])
print(name[0])

name="sita"
print(name)
print(id(name))

#given string --->fetch one by one char
for i in name:
    print(i)

#find length of the given string
print()
x="maharashtra"
print(len(x))

#reverse the given String 
print()
x="maharashtra"
for i in range(len(x)-1,-1,-1):
    print(x[i],end="")


print()
count=0
for i in x:
    count+=1
print(count)

#inbuild string methods 
#functions             |              methods
#predefined            |              classs
#userdefined           |              object refernce methodname()
#x="india"             |              or.upper
#print(len(x))         |              x.upper
 

s="hello how are you"
print(s.title())
print(s.capitalize())

#swap
a="india"
print(a.swapcase())
print(a.replace('a','x'))
print(a.replace('i','z'))

i="apple"
print(i.count('a'))
print(i.count('p'))
print(i.index('e'))
print(i.find('e'))
print(i.find('v'))
print(i.split())

j="apple banana grapes"
print(j.split())
k="apple,banana,grapes"
print(k.split(','))


#checking methods of string'
l="hello"
s=l.upper()
print(l.isupper())
print(s.isupper())
print(l.islower())

#check all alphabates
z="hello123"
print(l.isalpha())
print(z.isalpha())

#check number
r="123"
print(r.isnumeric())
print(r.isdigit())

#check numbers + alphabate
t="123hello45hi"
print(t.isalnum())

print(z.startswith('he'))
print(z.endswith('3'))

#remove white spaces
x="  hello"
print(len(x))

print(x.strip())
print(len(x.strip()))
