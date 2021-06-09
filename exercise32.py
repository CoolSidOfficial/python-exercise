"""
This exercise is Part 3 of 3 of the Hangman exercise series.
The other exercises are: Part 1 and Part 2.

You can start your Python journey anywhere, but to finish this exercise
 you will have to have finished Parts 1 and 2 or
  use the solutions (Part 1 and Part 2).

In this exercise, we will finish building Hangman.
 In the game of Hangman, the player only has 6 incorrect guesses
 (head, body, 2 legs, and 2 arms) before they lose the game.

In Part 1, we loaded a random word list and picked a word from it.
 In Part 2, we wrote the logic for guessing the letter and
 displaying that information to the user.
 In this exercise, we have to put it all together and
  add logic for handling guesses.

Copy your code from Parts 1 and 2 into a new file as a starting point.
Now add the following features:

    Only let the user guess 6 times, and tell the user
     how many guesses they have left.
    Keep track of the letters the user guessed.
     If the user guesses a letter they already guessed,
     don’t penalize them - let them guess again.

Optional additions:

    When the player wins or loses, let them start a new game.
    Rather than telling the user "You have 4 incorrect guesses left",
    display some picture art for the Hangman. This is challenging -
    do the other parts of the exercise first!

Your solution will be a lot cleaner if you make use of functions to help you!
"""
#------------------------------------------------------------
from os import system
from colorama import init,Fore,Back,Style
from exercise31 import *  # it will give everything
#---------------------------------------------------------------
import random
import time
import exercise30 # for importing word from net
#----------------------------------------------------------------
init(autoreset=True)   # it helps to autochange colour
#--------------------------------------------------------------------
def give_word():      # it will give us a word
    exercise30.get_file()
    list_=[]
    with open("ex30.txt","r") as file : # it will open that text file
        for i in file:
            word=i.strip() # it remove\n from last
            list_.append(word)
    return random.choice(list_)
#------------------------------------------------------------------------------
def main():
    exercise32_drawing.want_man=True
    print(Back.RED+"Please wait finding a word from net".center(80))
    text=give_word().upper()    # the word
    start(True,text,len(text))  # start the game

#-------------------------------------------------------------------------------
if __name__=="__main__":
    while True: # it will run till user does enter exit
     main()
     playagain()
#link>>https://www.practicepython.org/exercise/2017/01/10/32-hangman.html
