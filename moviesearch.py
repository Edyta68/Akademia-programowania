import omdb
import time
import datetime


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

def function_sort():
    if sorting == "Rating":
        results.sort(key=get_rating)
    elif sorting == "Popularity":
        results.sort(key=get_votes)
    elif sorting == "Length":
        results.sort(key=get_length)
    elif sorting == "Release date":
        results.sort(key=get_date)


omdb.set_default('apikey', "1ecdeb9a")
print("\n")

print("TYPE THE TITLE TO DISPLAY INFORMATION ABOUT MOVIE OR 'END' TO EXIT THE PROGRAM.\n")

while True:
    user_type = input("Type movie title: ")
    if user_type == 'end':
        exit()
    sorting = user_type.split(" : ")
    titles = sorting[0].split(", ")
    if len(sorting) > 1:
        sorting = sorting[1]
    else:
        sorting = "No sorting"
    results = []
    for title in titles:
        result = omdb.title(title)
        if not result:
            result['title'] = title
            result['error'] = True
        results.append(result)

    function_sort()

    for result in results:
        if 'error' in result:
            print("No movie found with this title")
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
            print(f"Genre: {result['genre']}")
            print(f"Type: {result['type']}")
            print(f"Director: {result['director']}")
            print(f"Actors: {result['actors']}")
            print(f"Plot: {result['plot']}")
            print(f"IMDB rating: {result['imdb_rating']}")
            print(f"IMDB votes: {result['imdb_votes']}")