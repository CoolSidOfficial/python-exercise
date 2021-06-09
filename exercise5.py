"""Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

Extras:

    1:Randomly generate two lists to test this"""


#it will create random numbers that we will add in the list
import random
print("please wait  ")
list_a=[]
list_b=[]
limit=0
list_final=[]
while limit<1000:
    a=random.randint(0,100)
    b=random.randrange(0,100,2)# create random even numbers
    list_a.append(a)
    list_b.append(b)
    limit=limit+1

for num in list_a:# it will create a new list
  if num in list_b:
     list_final.append(num)
print(list_final)
#done
#link>>https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html
