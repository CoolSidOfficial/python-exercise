"""Instead of using the .txt file from above (or instead of,
 if you want the challenge), take this .txt file,
 and count how many of each “category” of each image there are.
 This text file is actually a list of files corresponding to the
 SUN database scene recognition database,

 and lists the file directory hierarchy for the images.
 Once you take a look at the first line or two of the file,
 it will be clear which part represents the scene category.
 To do this, you’re going to have to remember a bit about string parsing in Python 3.
 I talked a little bit about it in this post."""

def file_open():
    name=input("Please enter the path to open\n>>")
    with open(name,"r") as file:
        global word
        word=file.readlines()
        #word=word.split()
def get_text():
    global data
    data=dict()
    for i in word:
        sp=i.split("/")
        l=(len(sp))-1
        global final_word
        final_word=sp[l]
        data[final_word]=data.get(final_word,0)+1




if __name__=="__main__":
     file_open()
     get_text()
     for key,values in data.items():
        print("'{}'- and number of time it appeared '{}' time".format(key,values))
###done
##link>>>>https://www.practicepython.org/exercise/2014/12/06/22-read-from-file.html
