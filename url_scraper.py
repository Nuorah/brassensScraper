from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

def url_scraper():
    url = "http://www.brassens-cahierdechanson.fr/COMMUN/toutes.html"
    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    urls = []
    for link in soup.findAll('a', attrs={'href': re.compile("^../OEUVRES/CHANSONS/")}):
        urls.append("http://www.brassens-cahierdechanson.fr" + link.get('href')[2:])
    return urls