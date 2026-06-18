stud={
    "rollno":101,
    "name":"swanandi",
    "age":19,
    "sub":["math","eng","java"],
    "marks":(90,89,67)
}
print(stud)

#methods
print(stud.keys())
print(stud.values())
print(stud.items()) 


#loop
print("iterate keys only")
for keys in stud:
    print(keys)

print()
print("iterate values only")
for values in stud.values():
    print(values)

print()
print("iterate both keys and values")
for k,v in stud.items():
    print(k,v)


for i in stud:
    if i=="sub":
        for v in stud[i]:
            print(v)
        

#acessing keys in the sub:marks format
#for i in range(len(stud["sub"])):
#    print(f"{stud["sub"][i]}:{stud["marks"][i]}")

#zip function hells to iterste multiples valyes of the keys 
for sv,mv in zip(stud["sub"],stud["marks"]):
    print(sv,mv)





        