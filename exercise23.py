"""
Given two .txt files that have lists of
numbers in them, find the numbers that are overlapping.
 One .txt file has a list of all prime numbers under 1000, and the other .txt
 file has a list of happy numbers up to 1000."""

import time
from os import system

file_path="/home/siddhant/Desktop/python2.0/exercise/ex23.one.txt"

file2_path="/home/siddhant/Desktop/python2.0/exercise/ex23.more.txt"
def create_lists(path,name):
    with open(path,"r") as file:
      for word in file:
        name.append(word.strip())# strip used to remove \n
if __name__=="__main__":
    prime_numbers=list()
    happy_numbers=list()
    create_lists(file_path,prime_numbers)
    create_lists(file2_path,happy_numbers)
    for each in prime_numbers:
        if each in happy_numbers:
            #system("clear")
            print("{} is present in both lists".format(each))
            time.sleep(1)
        else:
            print("{} is not present in both lists".format(each))
            time.sleep(1)
##done
##link>>>https://www.practicepython.org/exercise/2014/12/14/23-file-overlap.html
