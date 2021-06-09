"""
This exercise is Part 1 of 4 of the birthday data exercise series. The other exercises are: Part 2, Part 3, and Part 4.

For this exercise, we will keep track of when our friend’s birthdays are, and be
able to find that information based on their name. Create a dictionary (in your file) of names and birthdays.
 When you run your program it should ask the user to enter a name,
 and return the birthday of that person back to them. The interaction should look something like this:

>>> Welcome to the birthday dictionary. We know the birthdays of:
Albert Einstein
Benjamin Franklin
Ada Lovelace
>>> Who's birthday do you want to look up?
Benjamin Franklin
>>> Benjamin Franklin's birthday is 01/17/1706.
"""
#------------------------------------------------importing----------------------------------------------------
from colorama import init,Fore,Back,Style
from os import system
import time
#------------------------------------it will auto reset colours-------------------------------------------------
init(autoreset=True)
#---------------------------------------------data----------------------------------------------
data={"Siddhant Jain":"August 10, 2003",
      "Queen Elizabeth":"September 7, 1533",
      "Colonel Harland Sanders":"September 9, 1890",
      "Roald Dahl":"September 13, 1916",
      "Michael Faraday":"September 22, 1791",
      "Albert Einstein":"March 14, 1879",
      "Neil deGrasse Tyson ":"October 5, 1958",
      "Stephen Hawking ":"January 8, 1942",
      "Sir Isaac Newton" :"January 4, 1643",
      "Marie Curie":"November 7, 1867",
      "Tim Berners Lee":" June 8, 1955",
      "CV Raman":"November 7, 1888",
      "Niels Bohr":"October 7, 1885",
      "John Dalton":"September 6, 1766",
      "Alan Turing":"June 23, 1912",
      "Adolf Hitler":"April 20, 1889",
      "Mahatma Gandhi":"October 2, 1869",
      "Karl Marx":" May 05, 1818",
      "Charles Darwin":"February 12, 1809",
      "Christopher Columbus":"31 October, 1451",
      "Robert Hooke":"July 28, 1635",
      "Leonardo da Vinci":"April 15, 1452",
      "Elon Musk":"June 28, 1971",
      "Thomas Edison":"February 11, 1847",
      "Nikola Tesla":"July 10, 1856"
}   # big persoanlites names
#----------------------------------clear screen--------------------------------------------------------------------
def cls(t=0.25):
    time.sleep(t)
    system("clear")
#----------------------------------------------  check user input--------------------------------------------------------
def ask(d=data): #wher d can be dictionary
    print(Fore.WHITE+Style.BRIGHT+"Welcome to the birthday dictionary We knows birthdays of :\n".center(80))
    for i in d.keys():       # it will print the names  from dictionary
        print(i)
    time.sleep(3)
    while True:
     print(Fore.MAGENTA+"Who's birthday do you want to look up?")
     dob=input("Enter the name::#>>")
     if dob =="":
        print("[error :] It cannot be empty")
        cls()
        continue
     elif dob=="exit":
        cls()
        print(Fore.WHITE+"Exiting thanks for using  it".center(80))
        exit()
     else:
        return dob  # it will send the string

#------------------------------------------------------------------------------------------------------------

if __name__=="__main__":
    cls()

    word=ask() # this is the word
    cls(0)
    try:
        print(Fore.BLACK+Back.WHITE+"{}'s birthday is on {}".format(word,data[word]).center(80))
    except:
        print(Style.BRIGHT+Fore.WHITE+"The name given is wrong ".center(80))
        cls(4)
        exit()
#done
#link>>https://www.practicepython.org/exercise/2017/01/24/33-birthday-dictionaries.html
