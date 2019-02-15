from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

"""
Gets verses and words from lyrics of a George Brassens song from the website www.paroles.net.
Enter the url and the title. Use the url scraper to get all the brassens urls.
"""

def get_lyrics(url):
    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    text_by_lines = []
    if(soup.find_all('td', attrs={'class': 'titre'}) != []):
        title = soup.find_all('td', attrs={'class': 'titre'})[0].text.strip()
    else:
        title = ""
    for p in soup.findAll('p', attrs={'class': 'texte_chanson'}):
        for line in p.text.split("\n"):
            if line.strip() != "":
                text_by_lines.append(line.strip())
    return title, text_by_lines










