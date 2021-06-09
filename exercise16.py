"""Write a password generator in Python.
Be creative with how you generate passwords -
strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
 The passwords should be random, generating a new password every time the user asks for a new password.
 Include your run-time code in a main method.

Extra:

    Ask the user how strong they want their password to be. For weak passwords, pick a word or
     two from a list.
"""

# importing functions
import time
import random
from os import system
import string
strong_list=[]
def intro(): # adding some words in dictionary
    print("Please enter  how many  some word should be used to create a password seprated by spaces ".center(50,"*"))
    global data
    data=input("\n>>>>")
    data=data.split()

def weak_pass():  # it will create a weak pass
   num=random.randint(100,999)
   li=random.randint(0,len(data))
   str_l=str(data[li])
   weak_password=str_l+str(num)
   print("This is the password generated for you\n>>>>>>>",weak_password)
   time.sleep(7)
def strong_pass(a): # it will create a strong password using a module string
    if a ==0:
      print("Using default keyspace for pass length".center(100,"@"))
      a=12
    for i in range(0,a):
      word="".join(string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation)
      words=random.choice(word)
      strong_list.append(words)
    strongpass= "".join(strong_list)
    system("clear")
    print("THIS IS THE PASSWORD GENRATED FOR YOU\n",strongpass)
    time.sleep(10)
while True:
    print("Do you want strong or weak pass")
    choice=input("[1]strong\n[2]weak\n>>")
    system("clear")
    if choice =="1":
        print("you choosed option 1:Strong")
        b=int(input("Please enter length of strong pass by default taken 12 ##\n>>>>>>"))
        strong_pass(b)
    elif choice =="2":
        print("you choosed option 2:Weak")
        intro()
        weak_pass()
    else:
        print("your input is wrong ,exiting")
        time.sleep(5)
        exit()
###done
#link>>>https://www.practicepython.org/exercise/2014/05/28/16-password-generator.html
