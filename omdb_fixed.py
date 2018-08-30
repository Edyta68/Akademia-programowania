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

# When it comes to some movies, not all the information is available
# That's why in some places we check if the value is equal 'N/A' - not available
# Thanks to this we know to not take that movie into consideration while sorting


def get_rating(res):
    if 'imdb_rating' not in res:
        return -1
    if res['imdb_rating'] == 'N/A':
        return 0
    else:
        return float(res['imdb_rating'])


def get_length(res):
    if 'runtime' not in res:
        return -1
    if res['runtime'] == 'N/A':
        return 0
    else:
        return int(res['runtime'].split(" ")[0])


def get_date(res):
    if 'released' not in res:
        return -1
    if res['released'] == 'N/A':
        return 0
    else:
        return datetime.datetime.strptime(res['released'], '%d %b %Y').timestamp()


def get_votes(res):
    if 'imdb_votes' not in res:
        return -1
    if res['imdb_votes'] == 'N/A':
        return 0
    else:
        return int(res['imdb_votes'].replace(",", ""))


def function_sort(sorting):
    if sorting == "rating":
        results.sort(key=get_rating)
    elif sorting == "popularity":
        results.sort(key=get_votes)
    elif sorting == "length":
        results.sort(key=get_length)
    elif sorting == "release date":
        results.sort(key=get_date)


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


def get_correct_title():
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


def print_movie_information():
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


def open_trailer():
    query_string = urllib.parse.urlencode({"search_query": result['title'] + ' trailer'})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    webbrowser.open("http://www.youtube.com/watch?v=" + search_results[0], new=2)


omdb.set_default('apikey', "adc23445")
path = "C:\Movies"
titles = []
results = []
forbiddenCharacters = ['\\', '/', ':', '*', '?', '|', '"', '<', '>']
print("WELCOME TO MOVIE DATABASE!")
user_choice = input("\nDo you want to 'type' the title or 'load' it from folder? ")

if user_choice == "type":
    print("\nYou can additionally sort the movies by: rating, popularity, length and release date.\n")
    print("If you want to do so simply add ' : sorting option' after typing titles.\n")
    user_type = input("Type movie title(s) separated by coma and space: ")
    sorting = user_type.split(" : ")
    titles = sorting[0].split(", ")
    if len(sorting) > 1:
        sorting = sorting[1]
    else:
        sorting = "No sorting"
else:
    get_correct_title()

for title in titles:
    result = omdb.title(title)
    if not result:
        result['title'] = title
        result['error'] = True
    results.append(result)
if user_choice == "type":
    function_sort(sorting)
for result in results:
    if 'error' in result:
        print(f"No movie found with the title: {result['title']} ")
    else:
        print_movie_information()


