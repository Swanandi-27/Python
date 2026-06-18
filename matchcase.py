#syntax
#match ip:
    #case1:

    #case 2:

    #case_:(default case)

print("GEO Calculator \n1 Triangle \n2 Rectangle \n3 Circle \n4 Exit")
choice=int(input("enter your choice"))
match choice:
    case 1:
        print("Triangle case executed")
        print("1.area")
        print("2.perimeter \n3.EXIT")
        ch=int(input("enter you choice"))

        match ch:
            case 1:
                print("you selected area")
                base=int(input("enter base of triangle "))
                height=int(input("enter the height of the triangle "))
                area=0.5*base*height
                print("Area of triangle",area)
            case 2:
                print("you selected perimeter")
                a=int(input("enter the first side of the triangle"))
                b=int(input("enter the second side of the triangle"))
                c=int(input("enter the third side of the triangle"))
                perimeter=a+b+c
                print("the perimeter of the triangle:",perimeter)


            case 3:
                print("Exit from triangle")
            case _ :
                print("Invalid choice ")
    case 2:
        print("\n1.area \n2.perimeter \n3.exit")
        ch=int(input("enter your choice"))
        match ch:
            case 1:
                l=int(input("enter the length of the rectangle"))
                b=int(input("enter the breadth of the rectangle"))
                area=l*b
                print("area of rectangle :",area)

            case 2:
                l=int(input("enter the length of the rectangle"))
                b=int(input("enter the breadth of the rectangle"))
                peri=2*(l+b)
                print("perimeter of rectangle :",peri)

            case 3:
                print("Exit")

            case _:
                print("Invalid choice")



    case 3:
        print("\n1.area \n2.circumference \n3.exit")
        ch=int(input("enter your choice"))
        pi=3.14
        match ch:
            case 1:
                r=int(input("enter the radius of the circle"))
                area=pi*r*r
                print("the area of circle is ",area)

            case 2:
                r=int(input("enter the radius of the circle"))
                cir=2*pi*r
                print("the area of circle is ",cir)
            case 3:
                print("Exit")

            case _:
                print("Invalid choice")


                

        

    case 4:
        print("Thank you")
    case _ :
        print("Invalid Choice")