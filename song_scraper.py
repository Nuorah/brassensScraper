from url_scraper import url_scraper
from lyrics_scraper import BrassensSong

urls = url_scraper()
songs = []
for url in urls:
    print("Ajout de " + url)
    songs.append(BrassensSong(url))

for song in songs:
    print("parcours songs")
    print(song.title)
