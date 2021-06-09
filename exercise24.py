"""

This exercise is Part 1 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 2, Part 3, and Part 4.

Time for some fake graphics! Let’s say we want to draw game boards that look like this:

 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---

This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes (8x8 for chess, 19x19 for Go, and many more).

Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.

Remember that in Python 3, printing to the screen is accomplished by

  print("Thing to show on screen")

"""
from colorama import Fore,Back,Style,init
from os import system
from time import time
init(autoreset=True)
def check_input(user):
    global v1,v2
    value=user.split("*")
    try:
        v1=int(value[0])
        v2=int(value[1])
    except Exception as error:
        print(error)
        print('some error in user input try again')
        return True
    else:
     return False
def drawing(new_board,gridx=3,gridy=3):   #new_board parameter should be removed
    """This board is created by hit and trial method so use the value taken precisely for 2d board drawing"""
    #global board >>>>>>>>>>>>>  this 2 comment has 2 be removed if you are not importing this
    #board=[["  |" for x  in range(gridx)]for y in range(gridy) ]
    for i in new_board:   # from here also
        length=Style.BRIGHT+"-----"*gridx
        print(length.center(80))
        print(Fore.RED+Style.BRIGHT+" ".join(i).center(75))
        print(length.center(80))
if __name__=="__main__":
    while True:
        print("Give us The size we will draw a board for you . for  the default size  3*3 " )
        given_size=input(Fore.WHITE+"Like this  value '3*3' [#>>]")
        if given_size  =="":
           print("Please enter correct size ")
           continue
        if given_size== "exit":
            print("Exiting")
            sleep(5)
            exit()
        is_wrong=check_input(given_size)
        if is_wrong ==True:
            continue
        system("clear")
        drawing(v1,v2)
# done
# link>>>http://www.practicepython.org/exercise/2014/12/27/24-draw-a-game-board.html
