"""Implement a function that takes as input three variables,
and returns the largest of the three.
Do this without using the Python max() function!

The goal of this exercise is to think
about some internals that Python normally
takes care of for us. All you need is some
 variables and if statements!"""
def new_int(*value):  ## arg used
    global integer
    try:
        v1=int(value[0])
        v2=int(value[1])
        v3=int(value[2])
        integer=True

    except :
        integer=False

    if integer:
         if v1 > v2 and v1>v3 :
             print(v1)
         elif v2>v3 and v2>v1:
             print(v2)
         elif v3>v1 and v3>v2:
             print(v3)
         else:
             print("some values are same".center(100,"$"))
if __name__=="__main__":
    inp=input("Please enter three integer seprated by comma\n>>>>")
    inp=inp.split(",")
    try:
        new_int(inp[0],inp[1],inp[2])
    except Exception as e:
        print("Something wrong ")
        print(e)
##done
#link>>>https://www.practicepython.org/exercise/2016/03/27/28-max-of-three.html
