"""Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

Extras:

    Use binary search.
"""

from os import system
import time
import random
def create_list():
       global final_list
       final_list=random.sample(range(500),100)
       final_list.sort()  # it will create a random list
def simple_search():
    word=int(input("please enter the word again we will verify it again\n"))
    if word in  final_list:
        print("It is present in our list".center(100,"#"))
        return True
    else:
        print("{} is not present in our list".format(word))
        time.sleep(5)
        print("exiting".center(100,"#"))
        exit()  # it will use simple for loop to find word in list
def binary_search(list,word):
    lower_num=0
    upper_num=len(list)-1
    while lower_num <=upper_num:
        mid_range=(lower_num+upper_num)//2
        if list[mid_range]==word:
            return True
        elif list[mid_range] <  word:
            lower_num=mid_range+1
        elif list[mid_range] > word:
            upper_num=mid_range-1
    return False  # it will use binary search method to find word
if __name__=="__main__":
    create_list()
    print(final_list)
    word=int(input("PLease enter the number to check "))
    verify1=binary_search(final_list, word)
    if verify1 is True:
        print("we just found your word in list".center(100,"#"))
        time.sleep(5)
        system("clear")
    else:
        print("sorry word can not be found in our list".center(100,"#"))
        time.sleep(5)
        system("clear")
        simple_search()  # it will reverify it using simple search
# done after giving 5 hours
# link>>>https://www.practicepython.org/exercise/2014/11/11/20-element-search.html
