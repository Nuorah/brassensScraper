from url_scraper import url_scraper
from lyrics_scraper import BrassensSong


urls = url_scraper()
songs = []
with open("input.txt", "w") as text_file:
    for url in urls:
        print(url)
        text_file.write(" \n")
        print(" ")
        song = BrassensSong(url)
        for verse in song.verses:
            print("Writing : " + verse)
            text_file.write(verse + '\n')



"""for song in songs:
    print("parcours songs")
    print(song.title)"""
