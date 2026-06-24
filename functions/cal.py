def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def muladd(*args):
    print(sum(args))

while True:
    print("\n1.addition\n2.substraction\n3.multiplication\n4.division\n5:additin of multiple elemts\n6.combine operation \n7.exit")
    choice=int(input("enter y our choice"))
    match choice:
        case 1:
            a=int(input("enter first number:"))
            b=int(input("enter second number"))
            print(add(a,b))
        case 2:
            a=int(input("enter first number:"))
            b=int(input("enter second number"))
            print(sub(a,b))
            
        case 3:
            a=int(input("enter first number:"))
            b=int(input("enter second number"))
            print(mul(a,b))
        
        case 4:
            a=int(input("enter first number:"))
            b=int(input("enter second number"))
            print(div(a,b))
        case 5:
            numbers = []
            n = int(input("How many numbers do you want to add? "))

            for i in range(n):
                num = int(input("Enter number: "))
                numbers.append(num)

            muladd(*numbers)

        case 6:
           
            result = int(input("Enter first number: "))

            while True:
                op = input("Enter operator (+,-,*,/,=): ")

                if op == "=":
                    print("Final Result =", result)
                    break

                num = int(input("Enter second number: "))

                match op:
                    case "+":
                        result = add(result, num)
                    case "-":
                        result = sub(result, num)
                    case "*":
                        result = mul(result, num)
                    case "/":
                        result = div(result, num)
                    case _:
                        print("Invalid operator")
                        continue

                print("Current Result =", result)
                                
        case 7:
            exit()
            
        case _:
            print("Invalid choice")


