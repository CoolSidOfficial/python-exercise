"""Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether
they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

Extras:

    Keep the game going until the user types “exit”
    Keep track of how many guesses the user has taken, and when the game ends, print this out.

"""
from os import system
import random
import time
history=list()
def random_num():
    num = random.randint(0,9+1)
    return num
while True:
    guess_num=input("Please enter your guess \n>>".center(100))
    if guess_num =="exit":
        print("you are exiting")
        time.sleep(2)
        exit()

    elif  guess_num =="history":
        print(history)
        break

    try:
        guess_num=int(guess_num)
        history.append(guess_num)
    except:
        system("clear")
        print("enter only numbers ")
        continue


    data= random_num()# it will create an random num


    if guess_num == data:
        print("what ! you just guessed the right num",guess_num)
    else:
        print("your guess is wrong,nice try")
        if data>guess_num:# it will till how near the user guessed the number
            print("you guest was too low")
        elif data<guess_num:
            print("you guest was too high")
        print("The right answer is {}".format(data))

# done
# link>>https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html
