"""Given a .txt file that has a list of a bunch of names
, count how many of each name there are in the file
, and print out the results to the screen
. I have a .txt file for you
, if you want to use it!
"""
# extra will be there in the path2
import time
from os import system
def read_file(fn):
    try:

       with open(fn,"r") as file:
         global words
         words=file.read()
    except:
        print("No such file exist try entering full path".center(100,"*"))
        exit()
def add_dict():
    for i in word:
        data[i]=data.get(i,0)+1

if __name__=="__main__":
    data=dict()
    name=input("Please enter file path to open\n>> ")
    read_file(name)
    word=words.split()
    add_dict()
for name,times in data.items():
   print("  no of  {}  is :{}".format(name,times))
###done
#link>>https://www.practicepython.org/exercise/2014/12/06/22-read-from-file.html
