"""This exercise is Part 4 of 4 of the birthday data exercise series.
The other exercises are: Part 1, Part 2, and Part 3.

In the previous exercise we counted how many birthdays there are in each month
 in our dictionary of birthdays.

In this exercise, use the bokeh Python library to plot a histogram of which
 months the scientists have birthdays in! Because it would take a long time for
  you to input the months of various
scientists, you can use my scientist birthday JSON file. Just parse out the
months(if you don’t know how, I suggest looking at the previous exercise or
its solution) and draw your histogram.

If you are using a purely web-based interface for coding, this exercise
won’t work for you, since it requires installing the bokeh Python package.
Now might be a good time to install Python on your own computer.
"""
#---------------------------------------------------------------------------------------
from bokeh.plotting import figure,show,output_file
from bokeh.palettes import Spectral6
import json
#------------------------------   it will create an html page --------------------------------------------------------------
output_file("/home/siddhant/Desktop/python2.0/fun/exercise36.html",title="Scientist data")
#---------------------------   it will read json file-----------------------------------------------------------------
def open_json(path):
    with open(path,"r") as file:

      d=json.load(file)
      return d
#---------------it will count no of times of each month occured---------------------------------
def count_months():
    global histogram
    histogram={}
    for names,date in data.items():
      sp=date.split()
      month=sp[0]
      histogram[month]=histogram.get(month,0)+1
#-----------------------------------------main--------------------------------------
if __name__=="__main__":
   location_json="/home/siddhant/Desktop/python2.0/exercise/exercise34.json"
   data=open_json(location_json)   # it will return json data in dictionary form
   count_months()                   # it will count months
   month_x=[name for name ,occured in histogram.items()]    # it will gives names of months in list
   month_y=[occured for name,occured in histogram.items()]   # it will gives no times  months occured in list
   color=["red","green","red","green","red","green","red","green","red","green","red","green"] # will be red color and odd will be green color
   plot=figure(plot_height=600, # height
               plot_width=1300,  # width
               border_fill_color="blue",
               title="Number of scientists born in same month",
               title_location="above",
               x_axis_label="Months",
               y_axis_label="Number",
               x_range=month_x,          #this will show months
               toolbar_location=None,
               tools="")
   plot.vbar(month_x,top=month_y,width=0.5,fill_color=color)
   show(plot) # this will execute and open the webpage
#DONE
#link>>https://www.practicepython.org/exercise/2017/04/02/36-birthday-plots.html

# the last exercise
