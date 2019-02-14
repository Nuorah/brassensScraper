from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

page = urlopen("https://www.paroles.net/georges-brassens")

soup = BeautifulSoup(page, 'html.parser')

print(soup.prettify())