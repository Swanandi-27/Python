import datetime

#currentine--->now()
d=datetime.datetime.now()
print(d)

print(d.time())
print(d.date())
print(d.day)
print(d.month)
print(d.year)

#date---2026/06/25
today=datetime.date.today()
print(today)

#date after 5 days
after=today+datetime.timedelta(days=5)
print(after)

dob=datetime.date(2006,2,7)
cd=datetime.date.today()
print(cd-dob)
print(cd.year-dob.year)


#user1
user1=input("enter your name:")
year1=int(input("enter birth year"))
mon1=int(input("enter birth month"))
date1=int(input("enter date"))
dob1=datetime.date(year1,mon1,date1)


#user2
user2=input("enter your name:")
year2=int(input("enter birth year"))
mon2=int(input("enter birth month"))
date2=int(input("enter date"))
dob2=datetime.date(year2,mon2,date2)
if dob1>dob2:
    print("greater is :",user1)
elif dob2>dob1:
    print("greater is :",user2)
else:
    print("both are equal")


