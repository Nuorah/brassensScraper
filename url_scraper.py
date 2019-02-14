from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

def url_scraper():
    pages = []
    url = "https://www.paroles.net/georges-brassens"
    pages.append(urlopen(url))
    previousUrl = "https://www.paroles.net/georges-brassens"
    i = 2
    while (urlopen(url + "-" + str(i)).geturl() != previousUrl):
        previousUrl = urlopen(url + "-" + str(i)).geturl()
        pages.append(urlopen(url + "-" + str(i)))
        i = i + 1
    soups = []
    for page in pages:
        soups.append(BeautifulSoup(page, 'html.parser'))
    urls = []
    for soup in soups:
        for link in soup.findAll('a', attrs={'href': re.compile("^https://www.paroles.net/georges-brassens/")}):
            urls.append(link.get('href'))
    return urls