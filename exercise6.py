"""Ask the user for a string and print out whether this string is a
palindrome or not.
(A palindrome is a string that reads
the same forwards and backwards."""
word=input("Please enter a string\n>>>")
string_1=word.lower()
string_new=string_1[::-1]
if string_1 == string_new:
    print("the input string is a palindrome")
else:
    print("the input string is not a palindrome")

#done
#link>>https://www.practicepython.org/exercise/2014/03/12/06-string-lists.htmla
