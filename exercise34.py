"""This exercise is Part 2 of 4 of the birthday data exercise series.
The other exercises are: Part 1, Part 3, and Part 4.

In the previous exercise we created a dictionary of famous scientists’ birthdays.
 In this exercise, modify your program from Part 1 to load the birthday dictionary from
 a JSON file on disk, rather than having the dictionary defined in the program.

Bonus: Ask the user for another scientist’s name and birthday to add to the dictionary,
 and update the JSON file you have on disk with the scientist’s name.
  If you run the program multiple times and keep adding new names,
   your JSON file should keep getting bigger and bigger.
"""
#----------------------------importing standard modules-------------------------------------------
import json
from colorama import init,Fore,Back,Style
from os import system
#-------------------------------------------#importing custom--------------------------------
from exercise33 import data,cls,ask
#-----------------   for changing colors automatically----------------------------------------------------------------
init(autoreset=True)
#----------------------------------------------------------------------------------
def write_to_json():  # it will create json file from words
    with open(path,"w") as file:
        json.dump(data,file,indent=5)
#-------------------------------------------------read from json--------------------------------
def read_from_json():   # it will load json file
    with open (path,"r")as file:
        json_data=json.load(file)
        return json_data
#---------------------------------------new scientist name-----------------------------------------------------
def new_choice(): # it will ask
    cls(2)
    print(Fore.BLUE+Style.BRIGHT+"Do you wish to add another name".center(80))
    add_name=input(Fore.WHITE+Style.BRIGHT+"Please enter yes or no :[#>>]")
    if add_name=="yes":
        new_scientist() # it will  ask add new name
    else:
        print(Fore.WHITE+"Ok thanks for using it".center(80))
        exit()
#------------------------------------------------------------------
def new_scientist():
    global final_name,new_dob
    cls()
    while True:
      print(Fore.WHITE+Style.BRIGHT+" Please enter the scientist name".center(80))
      new_name=input(Fore.MAGENTA+Style.BRIGHT+"input Here [#>>]")
      if new_name =="":
        print(Fore.RED+Style.BRIGHT+"[error] Cannot enter empty string")
        continue
      elif new_name=="exit":
        print("Exiting")
        cls()
        exit()
      else:
        new_name=new_name.split()
        name=list(map(lambda n:n.capitalize(),new_name))  # it will capitalize name first word
        final_name=" ".join(name)

      print(Fore.WHITE+Style.BRIGHT+" Please enter the scientist Birthday".center(80))
      new_dob=input(Fore.MAGENTA+Style.BRIGHT+"In this format 'May 05, 1818' [#>>]")
      if new_dob =="":
         print(Fore.RED+Style.BRIGHT+"[error] Cannot enter empty string")
         continue
      elif new_dob=="exit":
         print("Exiting")
         cls()
         exit()
      else:
         print("Saving it name is : {} and birthday on : {}".format(final_name,new_dob))
         break
#--------------------------------------    this will write new names in extising json file-----------------------------------------------
def write_new_data():
    with open(path,"w")as file:
         dict_words={final_name:new_dob}
         json_data.update(dict_words)
         json.dump(json_data,file,indent=7)
#---------------------------     main file------------------------------------------------
if __name__=="__main__":
    path="/home/siddhant/Desktop/python2.0/exercise/exercise34.json"
    #write_to_json() #only run it to save the file  first time
    json_data=read_from_json()
    new_word=ask(json_data)
    cls()
    try:
        print(Fore.BLACK+Back.WHITE+"{}'s birthday is on {}".format(new_word,json_data[new_word]).center(80))
    except:
        print(Style.BRIGHT+Fore.WHITE+"The name given is wrong ".center(80))
        exit()
        cls(4)
    new_choice()   # it will do you wish to add new name or no
    write_new_data() # it will update the given name permanently
    print(Fore.RED+"The list has been updated successfully")
#done
# link>>https://www.practicepython.org/exercise/2017/02/06/34-birthday-json.html
