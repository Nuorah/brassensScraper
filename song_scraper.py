from url_scraper import url_scraper
from lyrics_scraper import get_lyrics

urls = url_scraper()
with open("input.txt", "w") as text_file:
    for url in urls:
        print(url)
        text_by_lines = get_lyrics(url)
        text_file.write(" \n")
        text_file.write(text_by_lines[0])
        text_file.write(" \n")
        print(" ")
        for line in text_by_lines[1]:
            print("Writing : " + line)
            text_file.write(line + '\n')



"""for song in songs:
    print("parcours songs")
    print(song.title)"""
