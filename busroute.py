from bs4 import BeautifulSoup
import urllib
import urllib.request

def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, 'lxml')
    return soupdata

soup = make_soup("https://www.pmpml.org/regular-service/")

for record in soup.select(".ng-scope"):
    print(record)




