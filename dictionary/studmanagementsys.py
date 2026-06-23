for key in stud:
    total = 0

    print("Student ID:", key)
    print("Name:", stud[key]["name"])

    for v in stud[key]["marks"]:
        total += v

    print("total marks:", total)

    per = total / len(stud[key]["marks"])
    print("percentage:", per, "%")
    print()
while True:
    print("welcome to student management system")
    print("\n1.add student\n2.view\n3.calculate total,percentage\n4.topper or lower\n5.exit")
    choice=int(input("enter your choice:"))
    match choice:
        case 1:
            n = int(input("How many students? "))

            for i in range(n):
                sid = int(input("Enter student ID: "))
    
                name = input("Enter name: ")
                age = int(input("Enter age: "))
                sub = input("Enter subjects: ").split(",")
                marks = tuple(map(int, input("Enter marks: ").split(",")))

            stud[sid] = {
                    "name": name,
                    "age": age,
                    "sub": sub,
                    "marks": marks
                }

            print(stud)
        case  2:
            for key,details in stud.items():
                print(f"student is: {key}")
                for k,v in details.items():
                    print(k,v)
                print()
        
        case 3:
            for key in stud:
                total = 0

                print("Student ID:", key)
                print("Name:", stud[key]["name"])

                for v in stud[key]["marks"]:
                    total += v

                print("total marks:", total)

                per = total / len(stud[key]["marks"])
                print("percentage:", per, "%")
                print()
            

                
            
        case 4:
            print("\n1.Topper\n2.Lower:")
            ch=int(input("enter your choice:"))
            match ch:
                case 1:
                    print("\n1.math\n2.java\n3.python")
                    ch1=int(input("enter your choice"))
                    match ch1:
                        case 1:
                            print("math")
                            max_marks = 0
                            name = ""

                            for sid in stud:
                                if stud[sid]["marks"][0] > max_marks:
                                    max_marks = stud[sid]["marks"][0]
                                    name = stud[sid]["name"]

                            print("Math Topper:", name, max_marks)
                        case 2:
                            print("java")
                            max_marks = 0
                            name = ""

                            for sid in stud:
                                if stud[sid]["marks"][1] > max_marks:
                                    max_marks = stud[sid]["marks"][1]
                                    name = stud[sid]["name"]

                            print("Math Topper:", name, max_marks)
                        case 3:
                            print("python")
                            max_marks = 0
                            name = ""

                            for sid in stud:
                                if stud[sid]["marks"][2] > max_marks:
                                    max_marks = stud[sid]["marks"][2]
                                    name = stud[sid]["name"]

                            print("Math Topper:", name, max_marks)
                case 2:
                    print("\n1.math\n2.java\n3.python")
                    ch1=int(input("enter your choice"))
                    match ch1:
                        case 1:
                            print("math")
                            min_marks = 999
                            name = ""

                            for sid in stud:
                                if stud[sid]["marks"][0] < min_marks:
                                    min_marks = stud[sid]["marks"][0]
                                    name = stud[sid]["name"]

                            print("Math Lower:", name, min_marks) 
                            
                        case 2:
                            print("java")
                            min_marks = 999
                            name = ""

                            for sid in stud:
                                if stud[sid]["marks"][1] < min_marks:
                                    min_marks = stud[sid]["marks"][1]
                                    name = stud[sid]["name"]

                            print("Math Lower:", name, min_marks) 
                           
                        case 3:
                            print("python")
                            min_marks = 999
                            name = ""

                            for sid in stud:
                                if stud[sid]["marks"][2] < min_marks:
                                    min_marks = stud[sid]["marks"][2]
                                    name = stud[sid]["name"]

                            print("Math Lower:", name, min_marks) 
                

                case _:
                    print("invalid choice")

                
                
            
        case 5:
            print("Thank you ")
            exit()
        case _:
            print("Invalid choice")

 

