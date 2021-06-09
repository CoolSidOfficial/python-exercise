"""Use the BeautifulSoup and
requests Python packages to
print out a list of all the article titles on the New York Times homepage."""
#importing some modules
from os import system
import time
try:
    import requests
except:
    pass
    exit()
from bs4 import BeautifulSoup

website_url="https://www.nytimes.com/"
print("Scraping data from this website\n",website_url)
recv=requests.get(website_url)
Soup=BeautifulSoup(recv.text,"html.parser")
tags=Soup.find_all("h2")  ## it will find all h2 tags
system("clear")

for i in tags:
   print(i.get_text()) ## it will print text
#Done
#link>>>https://www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html
