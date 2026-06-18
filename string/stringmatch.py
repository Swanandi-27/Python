while (1):
    print("\n1.Reverse String \n2.palindrome \n3.upper to lower \n4.count words in string\n5.find duplicate char in string \n6.Exit")
    ch=int(input("enter you choice"))
    match ch:
        case 1:
            print()
            ip=input("enter a string:")
            v=ip[::-1]
            print(v)
        case 2:
            print()
            ip=input("enter a string:")
            if ip==ip[::-1]:
                print("palindrome")
            else:
                print("not palindrome")

        case 3:
            print("\n1.upper\n2.lower\n3.swap")
            choice=int(input("enter your choice"))
            match choice:
                case 1:
                    a=input("enter a string:")
                    a_new=""
                    for i in a:
                        if i>='a' and i<='z':
                            a_new+=(chr(ord(i)-32))
                    print(a_new)
                case 2:
                    a=input("enter a string:")
                    a_new=""
                    for i in a:
                        if i>='A' and i<='Z':
                            a_new+=(chr(ord(i)+32))
                    print(a_new)

                case 3:
                    a=input("enter your choice")
                    a_new=""
                    for i in a:
                        if i>='a' and i<='z':
                            a_new+=(chr(ord(i)-32))
                        elif i>='A' and i<='Z':
                            a_new+=(chr(ord(i)+32))
                    print(a_new)

                case _:
                    print("Invalid choice ")
        case 4:
            x=input("enter a string:")
            count=1
            for i in x:
                if ' ' in i:
                    count+=1
            print(count)
        case 5:
            x=input("enter s string")
            print(len(x))
            new=""
            for ch in x:
                if ch not in new:
                    new+=ch
                    
            print("ans",new,len(new))
        case 6:
            print("----------Thank You-------------")
        case _:
            print("Invalid choice")

    op=int(input("do you want to continue if yes 1 or no 0"))
    if(op!=1):
        print("---------------Thank you-----------------")
        break
 