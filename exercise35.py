"""This exercise is Part 3 of 4 of the birthday data exercise series. The other
 exercises are: Part 1, Part 2, and Part 4.

In the previous exercise we saved information about famous scientists’ names and
 birthdays to disk. In this exercise, load that JSON file from disk, extract
 the months of all the birthdays, and count how many scientists have a birthday
 in each month.

Your program should output something like:

{
	"May": 3,
	"November": 2,
	"December": 1
}
"""
#-------------------------------------importing-----------------------------------------
from colorama import init,Fore,Back,Style
from os import system
import json
#--------------------------------------------------------------------------------
init(autoreset=True)#it will change colour automatically
#-----------------------------------------------------------------------------
def load_json():
    with open(path,"r")as file:
       words=json.load(file)
       return words
#------------------------------ histogram--------------------------------------
def months_counter():
   for i,j in json_data.items():
      months=j.split()
      month=months[0]
      dict_months[month]=dict_months.get(month,0)+1
#------------------------ main----------------------------------------
if __name__=="__main__":
    dict_months=dict()
    path="/home/siddhant/Desktop/python2.0/exercise/exercise34.json"
    json_data=load_json()
    months_counter()
    q=sorted(dict_months)  # just for look
    for i,j in dict_months.items():
        print(Fore.WHITE+Style.BRIGHT+i+Fore.RED+"  appeared this many times --",j)
        print("\n")
#--------------------------------------------------------------------------------------
# done
#link>>https://www.practicepython.org/exercise/2017/02/28/35-birthday-months.html
