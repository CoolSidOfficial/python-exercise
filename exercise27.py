"""This exercise is Part 3 of 4 of the Tic Tac Toe exercise series.
The other exercises are: Part 1, Part 2, and Part 4.

In a previous exercise we explored the idea of using a list of lists as a
 “data structure” to store information about a tic tac toe game.
 In a tic tac toe game, the “game server” needs to know where the Xs and Os
 are in the board, to know whether player 1 or player 2 (or whoever is X and O won).

There has also been an exercise about drawing the actual tic tac toe gameboard
using text characters.

The next logical step is to deal with handling user input. When a player
 (say player 1, who is X) wants to place an X on the screen,
 they can’t just click on a terminal.
 So we are going to approximate this clicking simply by asking the user for a
  coordinate of where they want to place their piece.

As a reminder, our tic tac toe game is really a list of lists.
The game starts out with an empty game board like this:

game = [[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]]

The computer asks Player 1 (X) what their move is (in the format row,col),
 and say they type 1,3. Then the game would print out

game = [[0, 0, X],
	[0, 0, 0],
	[0, 0, 0]]

And ask Player 2 for their move, printing an O in that place.

Things to note:

    For this exercise, assume that player 1 (the first player to move) will
	 always be X and player 2 (the second player) will always be O.
    Notice how in the example I gave coordinates for where I want to move
	starting
	 from (1, 1) instead of (0, 0). To people who don’t program, starting to count
	  at 0 is a strange concept, so it is better for the user experience
	  if the row counts and column counts start at 1. This is not required
	  , but whichever way you choose to implement this, it should be explained
	   to the player.
    Ask the user to enter coordinates in the form “row,col”
	 - a number, then a comma, then a number.
	 Then you can use your Python skills to figure out which row and column
	 they want their piece to be in.
    Don’t worry about checking whether someone won the game,
	but if a player tries to put a piece in a game position where there already
	is another piece, do not allow the piece to go there.

Bonus:

    For the “standard” exercise, don’t worry about “ending” the game -
	 no need to keep track of how many squares are full.
	  In a bonus version, keep track of how many squares are full and
	   automatically stop asking for moves when there are no more valid moves.

"""
from colorama import init,Fore,Back,Style
from os import system
import time
#---------------importing-----------------------#
def print_board():
    for i  in  game:
         print(Fore.WHITE+Style.BRIGHT+" |".join(i).center(80))   # printing the board again

def input_checker(player_):  # it will check is input is valid
    if player_=="":
        print(Fore.RED+"[error:]string cannot be empty")
        return False
    elif len(player_)<=2:
        print(Fore.RED+"[error:]Input is wrong ")
        return False
    elif player_=="exit":
        print("Exiting thanks for playing it\n \nHOPE YOU ENJOY IT\n\nBy Siddhant Jain")
        time.sleep(3)
        exit()
    else:
        #global user_data
        #suser_data=player_.split(",")#
        return True
def append(data,name,player_type="---"): # it will add  the player choice
            row=int(data[0])
            coloumn=int(data[1])

            try:
                if  name[row][coloumn]=="---":# replace "  |" with "---"
                    name[row][coloumn]=player_type
                else:
                    print("This slot has been taken by another player ")
                    return

            except:
                print("your input exceded the range of 3*3 board")
                time.sleep(5)
                intro()
            else:
                pass
def intro(board_name):
  while True:

    #system("clear")
    #print_board()  enabled it used in another module
    print("Please enter row number like this  '1,2' where 1 is row and 2 is coloumn  ")
    player1=input(Fore.MAGENTA+"player1 it your turn :[>>]")
    checker=input_checker(player1)
    if checker ==False:
       continue
    append(user_data,board_name,"  X ")
    print_board()
    player2=input(Fore.WHITE+"player2 it your turn :[>>]")
    checker=input_checker(player2)
    if checker ==False:
       continue
    append(user_data,board_name,"  O ")


init(autoreset=True)
if __name__=="__main__":

  game = [["---","---" ,"---"],
 	      [ "---", "---", "---"],
          ["---", "---", "---"]]
  print(Fore.RED+" Welcome to tic toe game\n\n\n\n\n\n".center(80))
  print_board()
  intro(game)
# done
# link>>https://www.practicepython.org/exercise/2015/11/26/27-tic-tac-toe-draw.html
