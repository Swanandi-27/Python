stud={
  101:{
   "name":"swanandi",
    "age":19,
    "sub":["math","eng","java"],
    "marks":(90,89,67)
   
  },
  102:{
   "name":"aastha",
    "age":220,
    "sub":["math","eng","java"],
    "marks":(90,89,67)
   
  },
  103:{
   "name":"bhakti",
    "age":23,
    "sub":["math","eng","java"],
    "marks":(79,80,62)
   
  }
}

print(stud)
print()
print(stud[101])
print("\n",stud[101]["sub"])
print("\n",stud[101]["sub"][2])




for val in stud.values():
    for key in val:
        print(key)


print(stud[102].items())

for key in stud:
    print(key)
    for v in stud[key]["marks"]:
        print(v,end=" ")
    print()




    
    

for i in stud:
    print("stud id:", i)
    print("name:", stud[i]["name"])
    print("age:", stud[i]["age"])
    print("sub:", stud[i]["sub"])
    print("marks:", stud[i]["marks"])
    print("--------")



for key,details in stud.items():
    print(f"student is: {key}")
    for k,v in details.items():
        print(k,v)
    print()


