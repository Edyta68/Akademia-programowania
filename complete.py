import omdb
import datetime
import time
import os
import re
import urllib
import requests
from os import listdir
from os.path import isfile, join
import webbrowser
import urllib.request
import urllib.parse


def add_folder_poster():
    allowed_title=result['title']
    for character in forbiddenCharacters:
        allowed_title = allowed_title.replace(character, "")
    newpath = f"C:/Movies/{allowed_title}"
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    put_info = open(f"{newpath}/{allowed_title}.txt", 'w')
    put_info.write(str(result))
    put_info.close()
    poster = result['poster']
    if not poster == "N/A":
        urllib.request.urlretrieve(poster, f"{newpath}/{allowed_title}.jpg")

def open_trailer():
    query_string = urllib.parse.urlencode({"search_query": result['title'] + ' trailer'})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    webbrowser.open("http://www.youtube.com/watch?v=" + search_results[0])


omdb.set_default('apikey', "adc23445")
path = "C:\Movies"
titles = []
results = []
forbiddenCharacters = ['\\', '/', ':', '*', '?', '|', '"', '<', '>']
user_choice = input("<TYPE> THE TITLE TO DISPLAY INFORMATION ABOUT MOVIE OR <LOAD> IT FROM FOLDER: ")

if user_choice == "type":
    user_type = input("Type movie title(s): ")
    titles = user_type.split(", ")
else:
    titles = [i for i in listdir("C:\Movies") if isfile(join(path, i))]
    skipWords = ['5.1', '7.1', '5 1', '7 1', 'DUAL AUDIO', 'DUAL-AUDIO', 'MULTI-CHANNEL', 'Ita-Eng',
                     '2160p', '4K', '1080p', '720p', '480p', '360p', 'HD', 'FULL HD', 'FULLHD', 'x264',
                     'CH', 'X264', 'HEVC', 'WEB-DL', 'BrRip', 'Rip', 'DVDRip', 'XviD', 'BLURAY',
                     'EXTENDED', 'REMASTERED', 'DIRECTORS', 'UNRATED', 'AlTERNATE', 'DVD']
    for index, movie in enumerate(titles):
        for word in skipWords:
            movie = movie.replace(word, "")
        titles[index] = movie
    for index, movie in enumerate(titles):
        titles[index] = movie.split(" .")[0].strip()

for title in titles:
    result = omdb.title(title)
    if not result:
        result['title'] = title
        result['error'] = True
    results.append(result)

for result in results:
    if 'error' in result:
        print(f"No movie found with the title: {result['title']} ")
    else:
        add_folder_poster()
        print("\n")
        print(f"Title: {result['title']}")
        print(f"Year: {result['year']}")
        print(f"Rated: {result['rated']}")
        if result["released"] == "N/A":
            print("Release date: N/A")
        else:
            print(f"Release date: {time.strftime('%d.%m.%Y', time.strptime(result['released'], '%d %b %Y'))}")
        print(f"Runtime: {result['runtime']}")
        print(f"Rating: {result['imdb_rating']}")
        print("\n")
        user_watch_trailer = input("DO YOU WANT TO WATCH THE TRAILER? ")
        if user_watch_trailer == "yes":
            open_trailer()
        else:
            exit()