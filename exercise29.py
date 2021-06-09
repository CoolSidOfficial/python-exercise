
"""

This exercise is Part 4 of 4 of the Tic Tac Toe exercise series.
 The other exercises are: Part 1, Part 2, and Part 3.

In 3 previous exercises, we built up a few components needed to build
a Tic Tac Toe game in Python:

    Draw the Tic Tac Toe game board
    Checking whether a game board has a winner
    Handle a player move from user input

The next step is to put all these three components together to make a
two-player Tic Tac Toe game! Your challenge in this exercise is to
use the functions from those previous exercises all together in the same
program to make a two-player game that you can play with a friend.
There are a lot of choices you will have to make when completing this exercise,
 so you can go as far or as little as you want with it.

Here are a few things to keep in mind:

    You should keep track of who won - if there is a winner,
     show a congratulatory message on the screen.
    If there are no more moves left, don’t ask for the next player’s move!

As a bonus, you can ask the players if they want to play again and
keep a running tally of who won more - Player 1 or Player 2.
"""
from os import system
import time
from colorama import init,Fore,Back,Style
#_________________--standard--modules--_____________________
from exercise24 import drawing                         ## it will create a 3*3 board for us
from exercise26 import corner_check,checker   # it will check for winner
from exercise27 import input_checker,append
#____________________________--importing done--____________________________
init(autoreset=True)### it will help colorama to support in windows pc
#___________________________________________________________________________
def cls():   #it will create clear screen
    system("clear")
#___________________________________________________________________________
def board_draw():
    global board
    board=[["  |" for x  in range(3)]for y in range(3) ] #it will draw a  board 3 range taken for tic toe board
#----------------------------------------------------------------------------
def string_changer(n):  # it will make user input easy for coordinate
    if n==1:
        return 0
    elif n==2:
        return 1
    elif n==3:
        return 2
    else:
        print("some unexpected error occured")
#-----------------------------------------------------------------------------
def player_turn(name):
    name=name.lower()
    print(Style.BRIGHT+"{}  it your turn bro choose the row and column".format(name).center(40))
    c1=input(Fore.WHITE+Style.BRIGHT+"input here[>>]")
    return c1 # it will return values enter by specific players
#-------------------------------------------------------------------------------------------
def modify_board(name,player_type,row,coloumn):
        try:
            if  name[row][coloumn]=="  |":
                name[row][coloumn]=player_type
            else:
                print(Fore.RED+"[error:]This slot has been taken by another player ".center(50))
                time.sleep(2)
                return "continue"

        except:
            print(Fore.RED+"[error:]your input exceded the range of 3*3 board".center(50))
            time.sleep(3)
            return "continue"
#---------------------------------------------------------------------------------------------
def is_not_empty():
    for i in range(3):
        if  " X|" in board[i][0] or " 0|" in board[i][0]:
          return True
#-------------------------------------------------------------------------------------
def start(player_name,type):
        global answer
        cls()           # it will clear screen
        is_not_empty()   # it will give true only if x or 0 in list
        if is_not_empty:
            answer=corner_check(board)  # it will give us the result
        drawing(board)   # player1
        string=player_turn(player_name)
        is_true=input_checker(string)
        if is_true ==False:
            time.sleep(2)
            start(player_name,type)
        else:
            string=string.split(",")
            row=string_changer(int(string[0]))
            coloumn=string_changer(int(string[1]))
            is_valid=modify_board(board,type,row,coloumn)
            if is_valid =="continue":
                start(player_name,type)
            else:
                pass
 #-----------------------------------------------------------------------------------
def finalcheck():
    x=" X|"
    y=" 0|"
    if answer ==x:
        cls()
        print(Back.BLUE+"player1 won the match".center(80))
        return True
    elif answer ==y:
        cls()
        print(Back.RED+"player2 won the match ".center(80))
        return True
    else:
          if  "  |"  not in board[0] and "  |" not in board[1] and "  |" not in board[2] :
            cls()
            print(Back.BLUE+"This game has been tie this game will not get any points".center(80))
            return False
#_____________________________________________________________________________________________
def main():
    while True:
        start("player1"," X|")
        last=finalcheck()
        if last:
            player1_="player-1"
            history[player1_]=history.get(player1_,0)+1
            break

        start("player2"," 0|")
        last=finalcheck()
        if last:
            player2_="player-2"
            history[player2_]=history.get(player2_,0)+1
            break
        if last==False:
            break



#--------------------------------------------------------------------------------------------
def play_again():
    print(Fore.MAGENTA+Style.BRIGHT+"Do you enjoy the game want to play again".center(80))

    again=input(Fore.WHITE+Style.BRIGHT+"Enter yes to play again or you can check history of winners[>>]")
    if again =="quit":
        cls()
        time.sleep(3)
        exit()
    elif  again =="yes":
        time.sleep(1.25)
        board_draw()
        drawing(board)
        cls()
        main()
    elif again =="history":
        for i,j in history.items():
            print("{} won {}".format(i,j))

        time.sleep(2.75)
#-----------------------------------------------------------------------------------------------
if __name__=="__main__":
    history={"player-1":0,"player-2":0}
    print(Fore.WHITE+Style.BRIGHT+" Welcome to the Tic Tac Toe  Game\n\n\n\n\n".center(80))
    input(Fore.RED+Style.BRIGHT+"Press any key to start".center(80))
    cls()
    print(Fore.WHITE+Style.BRIGHT+"  Tic Tac Toe  Game\n\n\n\n\n".center(80))
    #___________________________________________________________________________-_____________________
    board_draw()  # this create an empty board
    drawing(board)  # it will customize board
    #-------------------------------------------------------------------------------------------------------------

    print("Please enter row number like this  '1,2' where 1 is row and 2 is coloumn  ")
    input(Fore.RED+Style.BRIGHT+"Press any key to start the game".center(80))
    time.sleep(0.75)
    cls()
    main()
    play_again()
#____________________________________________________________________________________________________________
#done
# link>>https://www.practicepython.org/exercise/2016/08/03/29-tic-tac-toe-game.html
