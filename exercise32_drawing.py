from os import system
import time
from colorama import init,Style,Fore,Back
def clear_hangman(sec=2.0):
   system("clear")
   time.sleep(sec)                        #this file is created specially for hangman game exercise32.py
 #-------------------------------------------------------------------------------------- -
def draw_hangman(n):
     if n==1:
         print(rope.center(80))
     elif n==2:
         print(head.center(80))
     elif n==3:
         print(body.center(80))
     elif n==4:
         print(hands.center(80))
     elif n==5:
         print(legs.center(80))
     elif n==6:
         print(table.center(80))
     else:
         pass



#------------------------------------------------------------------------------
# ___________.._______
#| .__________))______|
#| | / /      ||
#| |/ /       ||
#| | /        ||.-''.
#| |/         |/  _  |               this is sample
#| |          ||  `/,|
#| |          (\\`_.'
#| |         .-`--'.
#| |        /Y . . Y\
#| |       // |   | \\
#| |      //  | . |  \\
#| |     ')   |   |   (`
#| |          ||'||
#| |          || ||
#| |          || ||
#| |          || ||
#| |         / | | \
#""""""""""|_`-' `-' |"""|
#|"|"""""""\ \       '"|"|
#| |        \ \        | |
#: :         \ \       : :
#. .          `'       . .













#--------------------------------------------------rope------------------------------------------------
rope=r'''
___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||
| |/         ||
| |          ||
| |          ||
| |          ||
| |          ||
| |          ||
| |          ||
| |          ||
| |          ||
| |          ||
| |
| |
| |
""""""""""|_
|"|"""""""\ \
| |        \ \
: :         \ \
. .          `'\\
'''
#-----------------------------------------------------------------------head----------------------------------------

head=r'''
___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  |
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |
| |
| |
| |
| |
| |
| |
| |
| |
""""""""""|_
|"|"""""""\ \
| |        \ \
: :         \ \
. .          `'\\
'''

#------------------------------------------------------------------------------body-----------------------------------------------
body=r'''
___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  |
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |         Y . . Y
| |         |   |
| |         | . |
| |         |   |
| |         |   |
| |         |   |
| |
| |
| |
""""""""""|_
|"|"""""""\ \
| |        \ \
: :         \ \
. .          `'
'''
#---------------------------------------------legs----------------------------------------------------------------
hands=r'''
___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  |
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        /Y . . Y\
| |       // |   | \\
| |      //  | . |  \\
| |     ')   |   |   (`
| |          ||'||
| |
| |
| |
| |
""""""""""|_
|"|"""""""\ \
| |        \ \
: :         \ \
. .
'''
#----------------------------------------------------------------------------legs----------------------------
legs=r'''
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  |
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        /Y . . Y\
| |       // |   | \\
| |      //  | . |  \\
| |     ')   |   |   (`
| |          ||'||
| |          || ||
| |          || ||
| |          || ||
| |         / | | \
| |         `-' `-'
""""""""""|--------------_|"""|
|"|"""""""-----------  '"|"|
| |
: :                     : :
. .                     . .
'''
#----------------------------------------------------------------------------------------table----------
table=r'''
___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  |
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        /Y . . Y\
| |       // |   | \\
| |      //  | . |  \\
| |     ')   |   |   (`
| |          ||'||
| |          || ||
| |          || ||
| |          || ||
| |         / | | \
""""""""""|_`-' `-' |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :
. .          `'       . .'''
if __name__=="__main__":
   while True:
    n=input("[>>]")
    if n=="exit":
        break
    n=int(n)
    draw_hangman(n)
    break
    clear_hangman(1)
#done
# specially made for exercise 32.py
#link>>https://www.practicepython.org/exercise/2017/01/10/32-hangman.html