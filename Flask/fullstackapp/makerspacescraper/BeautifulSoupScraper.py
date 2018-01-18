import urllib2
from bs4 import BeautifulSoup
import sys

#Fetching the webpage
try:
    htmlObject  = urllib2.urlopen("https://www.diyhacking.com/makerspaces")
except urllib2.HTTPError as e:
    print("There was an exception in the code:  " + str(e))
    sys.exit()

bsObj = BeautifulSoup(htmlObject)
for link in bsObj.findAll("a"):
    if 'href' in link.attrs:
        print(link.attrs['href'])

