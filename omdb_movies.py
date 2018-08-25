import omdb
import datetime
import time
import os
import re
import urllib
import requests
from os import listdir
from os.path import isfile, join

omdb.set_default('apikey', "adc23445")
path = "C:\Movies"
titles = []
results = []
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
        print("\n")
        print(f"Title: {result['title']}")
        print(f"Year: {result['year']}")
        print(f"Rated: {result['rated']}")
        if result["released"] == "N/A":
            print("Release date: N/A")
        else:
            print(f"Release date: {time.strftime('%d.%m.%Y', time.strptime(result['released'], '%d %b %Y'))}")
        print(f"Runtime: {result['runtime']}")