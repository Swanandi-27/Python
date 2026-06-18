student=[1,"ram",45,2,"sita",78,3,"pooja",90]
print(student)
print("IDs:")
for i in range(0, len(student),3):
    print(student[i])
print("Names:")
for i in range(1, len(student),3):
    print(student[i])
print("\nMarks:")
for i in range(2, len(student),3):
    print(student[i])


#combine
for i in range(len(student)):
    if i%3==0:
        print(student[i])
        print(student[i+1])
        print(student[i+2])
        print("========")


#HOMEWORK:
#x=[101,57,6,98,32,10,57,98]
#1)user pass the key check if key is present or not 
#2)print the duplicate elemts in the list
#3)unique elemts 
#4)withour sorting inbuild function ->sort
#5)even elemts represent -->0
#odd elemts repesent-->1