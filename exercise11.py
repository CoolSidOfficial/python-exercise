"""Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no divisors.).
You can (and should!) use your answer to Exercise 4 to help you.
Take this opportunity to practice using functions, described below.
"""
from colorama import init,Fore,Back,Style
init(autoreset=True)
print(Fore.RED+"PLease enter any number we will tell you that the number is prime or not")
num=input("[>]")
def is_prime(n):
   d=[i for i in range(1,10) if (n %i)==0 ] # it will only return 1 if is  aprime
   return d
try:
     number=int(num)
except:
      print("you can enter only int value")
      exit()
data=is_prime(number)
if len(data) ==1:
    print(Fore.WHITE+"It is a prime number")
else:
    print(Fore.BLUE+"It is not a prime number")
#done
#link>>http://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html
