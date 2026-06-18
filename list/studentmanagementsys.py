student=[[101,"swanandi",99],
         [102,"aastha",98],
         [103,"bhakti",97]]
while True:
    print()
    print("welcome to student management system")
    print("\n1.add\n2.view\n3.update\n4.delete\n5.Topper\n6.exit\n")
    choice=int(input("enter your choice:"))
    match choice:
        case 1:
            ip=int(input("enter how many student data do you want to add\n"))
            for i in range(ip):
                id=int(input("enter your id:"))
                name=input("enter your name:")
                marks=int(input("enter your marks"))
                student.append([id,name,marks])
                print(f"student{i+1} is added successfully") 
                
        case 2:
            print("student records")
            for i in student:
                print(i)
        case 3:
            
            
            id = int(input("Enter ID to update: "))

            found = False

            for i in student:
                if i[0] == id:
                    print("\n1.update name\n2.update marks\n3.update all")
                    ch=int(input("enter your choice"))
                    match ch:
                        case 1:
                            i[1] = input("Enter new name: ")
                            print("Student name updated successfully")
                            found = True
                            break
                        case 2:
                            i[2] = int(input("Enter new marks: "))
                            print("Student updated successfully")
                            found = True
                            break
                        case 3:
                            i[1] = input("Enter new name: ")
                            i[2] = int(input("Enter new marks: "))
                            print("Student name updated successfully")
                            found = True
                            break
                        case _:
                            print("incalid choice:")
                    

            if found==False:
                print("Student not found")
        case 4:
           
           id=int(input("ID: "))
           name = input("Name: ")
           marks = int(input("Marks: "))
           record = [id, name, marks]
           if record in student:
               student.remove(record)
               print("Student removed")
           else:
               print("Student not found")
           print(student)  
            
        case 5:
            max = 0
            name = ""

            for i in student:
                if i[2] > max:
                    max = i[2]
                    name = i[1]

            print("Topper:", name)
            print("Marks:", max)

        case 6:
            exit()
            print("Thankk you")
        case _:
            print("Invalid choice")

