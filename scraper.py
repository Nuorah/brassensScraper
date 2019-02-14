from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

"""
Gets verses and words from lyrics of a George Brassens song from the website www.paroles.net.
Title has to be in the format aupres-de-mon-arbre
"""

class BrassensSong:
    verses = []
    words = []
    title = ""

    def __init__(self, title):
        self.page = urlopen("https://www.paroles.net/georges-brassens/paroles-" + title.lower())
        self.soup = BeautifulSoup(self.page, 'html.parser')
        self.get_lyrics()
        self.get_title()
        self.get_words()

    def show_soup(self):
        print(soup)

    def not_eval(self, string):
        if string.startswith("eval"):
            return False
        return True

    def remove_eval(self, string):
        return string.split("eval", 1)[0]

    def get_lyrics(self):
        lyrics = self.soup.find_all("div", class_="song-text")[0].get_text().split('\n')
        lyrics = filter(self.not_eval, lyrics)
        lyrics = map(self.remove_eval, lyrics)
        for elem in lyrics:
            if elem != "":
                self.verses.append(elem.strip())

    def get_title(self):
        self.title = self.verses[0][22:]
        self.title = self.title.split("par Georges Brassens", 1)[0].strip()
        self.verses.pop(0)

    def get_words(self):
        for verse in self.verses:
            self.words.append(re.compile("[a-zA-Z0-9áàâäãåçéèêëíìîïñóòôöõúùûüýÿæœÁÀÂÄÃÅÇÉÈÊËÍÌÎÏÑÓÒÔÖÕÚÙÛÜÝŸÆŒ']+")
                              .findall(verse))
        flatwords = []
        for verse in self.words:
            for word in verse:
                flatwords.append(word.lower())
        self.words = flatwords








