""" Create a program that asks the user for a number
and then prints out a list of all the divisors of that number.
(If you don’t know what a divisor is, it is a number that divides evenly into
 another number.
 For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)"""


a=int(input("Please enter number\n>>>"))
li=[]
for i  in range(1,1000):
 digit=a%i
 if digit ==0:
   print(a, "is the divisior of" ,i )
   li.append(i)

 else:
  pass
print(li)
#done
#link>>https://www.practicepython.org/exercise/2014/02/26/04-divisors.html
