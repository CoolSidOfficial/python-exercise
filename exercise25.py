"""This time, we’re going to do exactly the opposite. You, the user,
 will have in your head a number between 0 and 100.
  The program will guess a number, and you, the user, will say whether it is
  too high, too low, or your number.

At the end of this exchange, your program should print out how many guesses it
 took to get your number.

As the writer of this program, you will have to choose how your program will
 strategically guess. A naive strategy can be to simply start the guessing at 1,
  and keep going (2, 3, 4, etc.) until you hit the number.
  But that’s not an optimal guessing strategy.
   An alternate strategy might be to guess 50 (right in the middle of the range),
    and then increase / decrease by 1 as needed. After you’ve written the program,
    try to find the optimal strategy! (We’ll talk about what is the optimal
    one next week with the solution.)
"""
from os import system
import time

def take_num():  # this function will take  number from user
   global number
   number=input("Please enter the number between 0 to 100 to guess\n>>")
   try:
       number=int(number)
   except Exception as fault:
      print(fault)
      exit()
   else:
      print("This is number you given us to {} to guess".format(number))
   finally:
      time.sleep(3)
      system("clear")
def naive_strategy(num):# this function will use for loop to find number:
    pass
    global history,t1,t2
    history=0
    t1=time.ctime()
    for i in range(0,101):
        if i == num:
            print("It is the right number I think:",i)
            time.sleep(2)
            break
        else:
            history+=1
            continue
    t2=time.ctime()
def optimal_strategy(num): # this function will find mid range and find the number
    mid=50
    global time1,time2
    time1=time.ctime()
    if num ==mid:
        print("we just guessed your number",mid)
    elif num < mid :
        for i in range(0,mid):
            if i==num:
                print("we just guessed your number ",i)
                break
    elif num > mid:
        for i in range(mid,100+1):
            if i==num:
                print("we just guessed your number ",i)
                break
    time2=time.ctime()



if __name__=="__main__":
      take_num()
      naive_strategy(number)
      print(history)
      print("IT took {} guesss to guess your number:".format(history))
      time.sleep(2.5)
      system("clear")
      print("now we will use different  strategy to guess your number")
      optimal_strategy(number)
      #print(t1,t2,time1,time2)
## done

## link>>https://www.practicepython.org/exercise/2015/11/01/25-guessing-game-two.html
