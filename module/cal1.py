#import entire function
import cal
print(cal.add(30,20))
print(cal.sub(30,10))

#import selected functions only
from cal import add,sub
#useing the function created in the cal.py file 
print(add(30,20))
print(sub(30,10))


#modules are of 2 tyeps
#Inbuild                   #user define modules
#1 import                  #mod=filename
#math                      #import the existing file where functions are stores
#random                      
#datetime
