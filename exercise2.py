"""Ask the user for a number. Depending on whether the
 number is even or odd, print out an appropriate message to the user. Hint: 
how does an even / odd number react differently when divided by 2?

Extras:

    If the number is a multiple of 4, print out a different message.
    Ask the user for two numbers: one number to check (call it num) and 
one number to divide by (check). 
If check divides evenly into num, tell that to the user. 
If not, print a different appropriate message.

"""
num=int(input("Plese enter any  number we will tell is it even or odd\n>>"))
check= num%2
check4=num%4  # extras
#print(check)
if check ==1:
 print(num,"It is odd number")  
elif check ==0: 
 print (num ,"It is even number")
else:
 print ("It is odd number")
if  check4 ==0: #extras
 print( num,"Number is the multiple of 4")
#extras
enum=int(input("Please  enter  first num \n>>"))
enum2=int(input("Please enter second number\n >>"))
solve=enum2%enum
if solve ==0:
 print("It is even")
else: 
 print("It is odd number")
#done

#https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
