"""This exercise is Part 1 of 3 of the Hangman exercise series.
 The other exercises are: Part 2 and Part 3.

In this exercise, the task is to write a function that picks a random word from
a list of words from the SOWPODS dictionary.
 Download this file and save it in the same directory as your Python code.
  This file is Peter Norvig’s compilation of the dictionary of words used in
  professional Scrabble tournaments.
  Each line in the file contains a single word.

Hint: use the Python random library for picking a random word."""

import requests
import random

"""_____________________"""
def get_file():
   global url
   link="http://norvig.com/ngrams/sowpods.txt"
   url=requests.get(link)
   url=url.text
   with open("ex30.txt","w")  as file:
      file.write(url)  # This function will get words from net and save it
def random_word():
    choose=random.choice(lis)
    print("This is the word we choose for you",choose) # this function will  choose a word from list


if __name__=="__main__":
    lis=[]
    get_file()
    with open("ex30.txt","r") as file : # it will open that text file
        for i in file:
            word=i.strip() # it remove\n from last
            lis.append(word)
    random_word()
### done
# link>>>https://www.practicepython.org/exercise/2017/01/10/32-hangman.html
