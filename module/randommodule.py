import random as r
#ex opt generation

print(r.randint(1000,9999))
print(r.random()) #generated floating value in the range of 0.0 to 1.0-->default range
print(r.randrange(0,10,2))#prints even numbers only 
print(r.randrange(1,10,2))

x=["red","black","blue","pink"]
print(r.choice(x)) #choice-->choose 1 random data from sequence
print(r.choices(x,k=2))#choices-->choose  random data from sequence based on key passed
r.shuffle(x) #shuffle original list 
print(x)


