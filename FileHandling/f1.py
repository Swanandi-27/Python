#create file 
#file=open("myfile.txt",'x')
#print(f"{file} created")
#insert -->w--->write("str")
#with 
try:
    file=open("FileHandling/myfirstfile.txt",'x')
    print(f"{file} created")
except FileExistsError as e:
    print(e)


#with the help of write method we can insert the data but it overrides the data 
with open("FileHandling/myfirstfile.txt",'w') as w:
    w.write("Hello world")
    print("data inserted")

#read
with open("FileHandling/myfirstfile.txt",'r') as r:
    print(r.read())


#append--->a--->write
with open("FileHandling/myfirstfile.txt",'a') as a:
    a.write("\nhow are you ?")
    print("new data added")



