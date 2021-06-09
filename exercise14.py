"""
Write a program (function!) that takes a list and returns
a new list that contains all the
 elements of the first list minus all the duplicates.

Extras:

    Write two different functions to do this -
    one using a loop and constructing a list, and another using sets.
    Go back and do Exercise 5 using sets, and
     write the solution for that in a different function.

"""
new_list=[]

def lis(word):    # it will remove duplicates
    if word not in new_list:
        new_list.append(word)


print("Enter names  or numbers to remove duplicates,seprated by a comma".center(100,"#"))
data=input("#>>")
list_data=data.split(",")  # it will create list
print(list_data)
for word in list_data:
    lis(word)
print(" this is the words filtered and we removeed duplicates")
print(new_list)

#done
#link>>https://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html
