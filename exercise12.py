"""Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
 and makes
 a new list of only the first
 and last elements of the given list.
For practice, write this code inside a function."""
new_list=[]
def create_list(n): # add the user numbers in the list
    new_list.append(num)

def data():# tell the first and last numbers of list
   size=len(new_list)
   print("The  first word is ",new_list[0])
   print("The  last word is ",new_list[size-1])
count=0

while count<5:
 a=input("Please enter the numbers\n>>>")
 try :
    num=int(a)
 except:
    print("you are typing wrong")
    exit()
 print("{} adding it in list".format(num))
 create_list(num)
 count +=1
print("list succesfully created")
data()
#>>done
#>>link  https://www.practicepython.org/exercise/2014/04/25/12-list-ends.html
