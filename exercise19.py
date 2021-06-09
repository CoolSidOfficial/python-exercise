"""Using the requests and BeautifulSoup Python libraries
, print to the screen the full text of the article on this website
: http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture
.

The article is long, so it is split up between 4 pages.
Your task is to print out the text to the screen so that
you can read the full article without having to click any buttons.

(Hint: The post here describes in detail
 how to use the BeautifulSoup and requests libraries through the
  solution of the exercise posted here.)

This will just print the full text of the article to the screen.
It will not make it easy to read,
 so next exercise we will
  learn how to write this text to a .txt file."""
#importing
import requests
from bs4 import BeautifulSoup
link=requests.get("https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture")

soup=BeautifulSoup(link.text,"html.parser")
article=soup.find_all("p")  #searching all paragraph tags
a,n=0,0
for  each  in article: ## line
  if a<6:## to remove menu
        a+=1
        continue





  #print(each.get_text())
  if n<81:  # after words in article eg privacy policy
      print(each.get_text())
  n+=1
# done
# link>>>https://www.practicepython.org/exercise/2014/07/14/19-decode-a-web-page-two.html
