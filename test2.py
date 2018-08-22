def dic():
    thisdict = ({
            "apple": 1,
            "banana": 2,
            "cherry": 3
        })

    thisdict["orange"] = 4
    thisdict.pop("apple", None)
    print(thisdict)


dic()


def word_counter(sentence):
    from collections import Counter
    list1 = sentence.split(" ")
    counts = Counter(list1)
    return counts


def word_counter2(sentence):
    from collections import Counter
    list1 = sentence.split(" ")
    for ind, word in enumerate(list1):
        if len(word) == 1:
            continue
        if not word[-1].isalnum():
            list1.append(word[-1])
            list1[ind] = word[:-1]
    counts = Counter(list1)
    return counts

answer = {"Ala": 2, "ma": 2, "kota.": 1, "psa.": 1}
assert word_counter("Ala ma kota. Ala ma psa.") == answer

answer = {"Ala": 2, "ma": 2, "kota": 1, "psa": 1, ".": 2}
assert word_counter2("Ala ma kota. Ala ma psa.") == answer

import re


def validatePIN(PIN):
    return bool(re.fullmatch("\d{4}", PIN))


assert validatePIN("1234") == True, "Wrong validation!"
assert validatePIN("12345") == False, "Wrong validation!"
assert validatePIN("a234") == False, "Wrong validation!"


def validate_input(word):
    return bool(re.fullmatch ("[a-z 0-9_]{5,20}", word))

assert validate_input("Summer Academmy") == False, "Bad validation!"
assert validate_input("Summer_Academmy") == False, "Bad validation!"
assert validate_input("summer_academmy") == True, "Bad validation!"


import omdb

client = omdb.OMDBClient(apikey="1ecdeb9a")
res = client.request(t='Grease', y='1978')
xml_content = res.content
print(xml_content)


