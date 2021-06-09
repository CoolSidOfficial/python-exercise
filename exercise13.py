"""Write a program that asks the user how many Fibonnaci numbers
 to generate and then generates them.
 Take this opportunity to think about how you can use functions.
  Make sure to ask the
  user to enter the number of numbers in the sequence to generate
  .
  (Hint: The Fibonnaci seqence is a sequence of numbers where the
   next number in the sequence is the sum of the
   previous two numbers in the sequence.
   The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
"""
numbers=[1,1]
data=input("Please enter the number to generate Fibonnaci series\n>>")
try:# convert the str in  numbers
    data=int(data)
except :
    print("your input is wrong ")
    exit()
    data=int(data)
for length in range(1, data-1): #to work until user numbers
   if length ==1:
     answer=numbers[0]+numbers[1]
     numbers.append(answer)
   else:
       last=len(numbers)-1    # tell last number in list
       sec_last=len(numbers)-2  # tell last second number in list
       answer=numbers[last]+numbers[sec_last]
       numbers.append(answer)
print(numbers)
##done
#link >>https://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html
