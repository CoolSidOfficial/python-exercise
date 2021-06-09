"""This exercise is Part 2 of 3 of the Hangman exercise series.
 The other exercises are: Part 1 and Part 3.

Let’s continue building Hangman. In the game of Hangman, a clue word is
 given by the program that the player has to guess, letter by letter.
  The player guesses one letter at a time until the entire word has been guessed.
 (In the actual game, the player can only guess 6 letters incorrectly before losing).

Let’s say the word the player has to guess is “EVAPORATE”.
 For this exercise, write the logic that asks a player to guess a letter and
  displays letters in the clue word that were guessed correctly.
   For now, let the player guess an infinite number of times until they get the
    entire word. As a bonus, keep track of the letters the player guessed and
     display a different message if the player tries to guess that letter again.
Remember to stop the game when all the letters have been guessed correctly!
 Don’t worry about choosing a word randomly or keeping track
  of the number of guesses the player has remaining -
   we will deal with those in a future exercise.

An example interaction can look like this:

>>> Welcome to Hangman!
_ _ _ _ _ _ _ _ _
>>> Guess your letter: S
Incorrect!
>>> Guess your letter: E
E _ _ _ _ _ _ _ E
...

And so on, until the player gets the word."""
#---------------------------------------------------------------------------------------------------------------------
from colorama import init,Fore,Back,Style
from os import system
import time
import exercise32_drawing  # for drawing hangman for ex32
#-----------------------------------------------importing-------------------------------------------------------------------
init(autoreset=True)       # it will support colors in windows
#------------------------------------------------------------------------------------------------------------------------
def cls(timer=0.75):       # it will clear screen
    time.sleep(timer)
    system("clear")
#--------------------------------------------------------------------------------------------------------------------------------
def create_board(n=8):
    global board
    board=[" _ "for i in range(n)]   # it will create a board

#----------------------------- it will print board-----------------------------------------------------------------------------------------------
def draw_now():
    print(Fore.WHITE+Style.BRIGHT+" ".join(board).center(80))
#----------------------------------  it  is the main logic ---------------------------------------------------------------------
def guess_letters(input,word):
    print("\n\n\n")
    for i in range(len(word)):

        if inp ==word[i]:
            board[i] =" {} ".format(input)

#----------------------------------it will tell that the  player win it or not-----------------------------------------------------
def win_it():
    if " _ " not in board:
        cls(0.5)


        print(Fore.MAGENTA+"You just got the answer ".center(80))
        draw_now()
        cls(3)
        print(Fore.WHITE+"Thanks for playing ".center(80))
        return True
#---------------------------------------- this will check the user input--------------------------------------------------------------
def user(wor):
    global inp
    print("\n")
    inp=input(Fore.MAGENTA+Style.BRIGHT+"Please enter your one word:[::>]")

    if len(inp)<1:
        print(Fore.RED+"[error!!] input is too small")
        user(wor)
    elif inp =="exit":
        cls()
        print("Thanks for using it".center(80))
        exit()
    elif inp =="history":
        cls()
        print(history)
    elif inp=="wrong-count":
      print(count)
    elif inp=="give-up":
        print("This is the right answer {}".format(wor))
        cls(5)
        exit()
    elif len(inp)>2:
        print(Fore.RED+"[error!!] input is too large")
        user(wor)
    else :
        inp=inp.upper()
        return True
#--------------------- it will tell about any duplicates numbers---------------------------------------------------------------
def again():
    if inp in history:
        print(Fore.RED+"[error!!] This word is already present here".center(80))
        return True
    else:
        pass
#---------------------------------------   it will call hangman from another file ----------------------------------------------------------------------------------------
def hangman(c):
    exercise32_drawing.draw_hangman(c)
#-----------------------------------------------------------------------------------
def counter(wor,want_man):
    global count
    if inp in wor:
       print(Back.BLUE+"WOW ! You are right this word is present ".center(80))
       history.append(inp)
    else:  # it will give 6 chances only for ex32
        print(Style.BRIGHT+"Sorry try again::".center(80))

        count+=1
        if want_man:
            hangman(count)
            print(Fore.RED+"You just left with {} these many more chances".format(6-count))
            if count ==6:
                cls(3)
                print(Back.YELLOW+"GAME OVER".center(80))
                return True
#------------------------------------------------------------------------------------
def playagain():
    print(Back.YELLOW+Fore.BLUE+"Do you like to play again ".center(80))
    choice=input("Type yes to play again:[#>>]")
    print(choice)
    if choice =="yes":
        return
    else:
        cls(0.25)
        print(Fore.WHITE+Style.BRIGHT+"Thanks for playing it hope you enjoy it ::))".center(80))
        exit()
#--------------------------main ----------------------------------------------------------
def start(hang,word_,size=8):
    global history,count
    count=0
    history=[]
    print(Fore.YELLOW+"WELCOME TO HANGMAN GAME".center(80))
    print("\n\n\n")
    input(Style.BRIGHT+"Press any key to start the game".center(80))
    cls()                               # it wil clear screen
    create_board(size)              # it will create a board for us
    while True:
      if win_it():  # does the player win?
            break
      draw_now()             # it will print Board
      user(word_)            # check input
      if  again() :    # the letter has been used
           continue
      guess_letters(inp,word_) # main logic
      if counter(word_,hang):
           break        # it will count the wrong words input by user ex32
#-------------------------------------------------------------------------------------------
if __name__ =="__main__":
  text="HAMULATE".upper()
  start(False,text)

#done
#link>>https://www.practicepython.org/exercise/2017/01/02/31-guess-letters.html
