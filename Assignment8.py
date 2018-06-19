#Q.1 What is time tuple.
import time
print(time.gmtime(0))

#Q.2. wap for formatted time.
import datetime
print(datetime.date.today())
print(time.ctime())

#Q.3.extract month from time.
import datetime
print(time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime()))
l=list(time.localtime())
print(l)
print(l[1])

#Q.4.extract day from the time.
from datetime import datetime
now=datetime.now()
print("day",now.strftime("%A"))
#Q.5.extract date from the time.
import datetime
print(time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime()))
l=list(time.localtime())
print(l)
print(l[2])
#Q.6 wap to print time using localtime method
import time
print(time.localtime())


#Q.7.find the factorial of number by input using math function.
num=int(input("enter the number which you want factorial: "))
import math
print(math.factorial(num))

#Q.8.find the gcd of anumber input by using math package function.
num1=int(input("enter first number"))
num2=int(input("enter second number"))
import math
print(math.gcd(num1,num2))

#Q.9.using os package.
import os
print(os.getcwd())
print(os.environ)
