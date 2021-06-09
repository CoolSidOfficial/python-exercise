"""
Create a program that asks the user to enter their name and their age.
 Print out a message addressed to them that tells them
 the year that they will turn 100 years old.

Extras:

    Add on to the previous program by asking the user for another number and 
printing out that many copies of the previous message.
 (Hint: order of operations exists in Python)
    Print out that many copies of the previous message on separate lines.
 (Hint: the string "\n is the same as pressing the ENTER button)
"""
user_name=input("Please enter your name\n>>")
user_age=input("Please enter your age\n>>")
user_age=int(user_age)
year=2020
new_age=year - user_age
new_year=new_age + 100
print("So you will turn year  100 years old on this year:",new_year)

# extras
num_copy=input("Please enter the number to  give the multiples copies of it\n>>")
num_copy=int(num_copy)
loop=0
while loop<=num_copy:

 print("So you will turn year  100 years old on this year:",new_year,"\n")
 loop=loop + 1
 # done 
#link--https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
