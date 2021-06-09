"""Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Paper beats rock
    Rock beats scissors
    Scissors beats paper
"""
import time
from os import system
def intro():   # it will give some introduction aout game
    print("Hey welcome to the rock paper scissor game".center(100))
    print("""Please Remember the rules\n[1] Rock beats scissors\n[2]Scissors beats paper\n[3]Paper beats rock""")
    time.sleep(3)
    system("clear")
def choose(player): # it will give  choice
    print("{},choose an option Please".format(player))
    print("[1]Rock\n[2]Paper\n[3]Scissor\n")
    while True:
      choice=input(">>")
      print(choice)
      if len(choice) ==0:
         continue
      break
    return choice
def option(name,data):# it will return the values as 1 ,2 or 3 for rock,paper,scissor
    print(data)

    if data == "1":
        system("clear")
        print(name.center(100,"#"))
        print("YOU CHOOSED ROCK".center(100,"#"))
        new_data=1
        return new_data
    elif data == "2":
        system("clear")
        print(name.center(100,"#"))
        print("YOU CHOOSED PAPER".center(100,"#"))
        new_data=2
        return new_data
    elif data == "3":
        system("clear")
        print(name.center(100,"#"))
        print("YOU CHOOSED SCISSOR".center(100,"#"))
        new_data=3
        return new_data
    else:
        print("some error occured ")
        time.sleep(4)

def ch_rock(data1,data2):
    if data1==data2:
        print("It is a tie you both choose the same")
    elif data1 > data2:
        if data1 == 2 and data2 ==1:
            print("{} won the round because he choose paper and paper beats rock".format(player_1))
        elif data1== 3 and data2 ==2:
            print("{} won the round as he chooses scissor and scissor beats paper ".format(player_1))
    elif data1 < data2:
        if data1 == 1 and data2 ==2:
            print("{} won the round because he choose paper and paper beats rocks".format(player_2))
        elif data1 ==1 and data2 ==3:
            print("{} won the round because he choose rock and rock beat scissor".format(player_1) )
        elif data1 ==2 and data2==3:
            print("{}won the round as he choose scissor and scissor cuts paper".format(player_2))
player_1=input("please enter 1 st player name>>>")
player_2=input("please enter 2 st player name>>>>>>")
print("the names are {}  and   {} ".format(player_1,player_2))
time.sleep(2)
system("clear")
while True:
    intro()
    print(player_1 ,"it is your turn")
    data1=choose(player_1)
    print("{} you choose {} option".format(player_1,data1))
    time.sleep(5)
    system("clear")

    print(player_2 ,"it is your turn")
    data2=choose(player_2)
    print("{} you choose {} option".format(player_2,data2))
    time.sleep(5)
    system("clear")
    value=option(player_1,data1)
    value2=option(player_2,data2)
    system("clear")
    ch_rock(value,value2)
    time.sleep(5)
    system("clear")
    print("would you like to play more".center(150))
    more=input("please enter yes or no>>")
    if more =="yes":
        continue
    else:
        break
time.sleep(5)
system("clear")
print("Bye,Bye")
#done
#https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
