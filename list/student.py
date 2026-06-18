student=[[101,"swanandi",99],
         [102,"aastha",99],
         [103,"bhakti",98],
         [104,"ojaswi",98]]

print("student Id")
for i in student:
    
    print(i[0])

for i in student:
    print(f"{i[1]}----->{i[2]}")
print()


list=[]
id=int(input("enter the id:"))
name=input("enter name")
marks=int(input("/enter mark of the student"))
list.insert(0,id)
list.insert(1,name)
list.insert(2,marks)
print(list)
student.append(list)
print(student)

id1=int(input("enter the id:"))
name1=input("enter name")
marks1=int(input("/enter mark of the student"))
student.append([id1,name,marks])


#max student 
student = [[101,"swanandi",99],
           [102,"aastha",100],
           [103,"bhakti",98],
           [104,"ojaswi",98]]

max = 0
name = ""

for i in student:
    if i[2] > max:
        max = i[2]
        name = i[1]

print("Topper:", name)
print("Marks:", max)

#show the student record 
student = [[101,"swanandi",99],
           [102,"aastha",100],
           [103,"bhakti",98],
           [104,"ojaswi",98]]

for i in student :
    print(i)

