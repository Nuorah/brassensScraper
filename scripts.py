from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

url = "http://www.brassens-cahierdechanson.fr/OEUVRES/CHANSONS/ombremaris.html"

page = urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
#print(soup.prettify())
text_by_lines = []
print(soup.find_all('td', attrs={'class': 'titre'})[0].text)


#print(soup.prettify())