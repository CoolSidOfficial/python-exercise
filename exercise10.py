"""This week’s exercise is going to be revisiting an old exercise (see Exercise 5),
except require the solution in a different way.

Take two lists, say for example these two:

	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two list
s of different sizes.

    Randomly generate two lists to test this
"""
import random
list_1=list()
list_2=list()
list_3=list()
main_list=list()
count=0
def max_range(name,range): # to create random list
 while True:
  global count
  count+=1
  li=random.randint(0,101)
  name.append(li)
  if count ==range:	break


max_range(list_1,1000)
count=0
max_range(list_2, 800)
for u in list_1:# adding common in new list
	if u in list_2:
		list_3.append(u)
for i in list_3:# removing duplicates from new list
	if i  not in main_list:
		main_list.append(i)
print("print this is the  new list which  contain num\n{})  ".format(main_list))




#done
#link >>https://www.practicepython.org/exercise/2014/04/10/10-list-overlap-comprehensions.html
