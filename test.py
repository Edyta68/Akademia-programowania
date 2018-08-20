def remove_chars(sentence):
    return sentence[1:-1]


assert remove_chars("country") == "ountr", "Failed test case"
assert remove_chars("Tieto") == "iet", "Failed test case"


def return_half(sentence):
    return sentence[0:sentence.__len__()//2]


assert return_half("Tieto") == "Ti", "Failed test case"
assert return_half("Work") == "Wo", "Failed test case"
assert return_half("Academy") == "Aca", "Failed test case"


def append_to_string(sentence):
    if len(sentence) >= 5:
       sentence += " World"
    else:
        sentence = "Welcome, " + sentence
    return sentence


assert append_to_string("Hello") == "Hello World", "Wrong"
assert append_to_string("Hi") == "Welcome, Hi", "Wrong"


def which_string(string1, string2):
    return string1 > string2

def filter_list(my_list):
    my_list = [element for element in my_list if type(element) is int]
    return my_list


assert filter_list([1, 5, 'A', 30, 'Hello', 50, 2.75]) == [1, 5, 30, 50], "Bad filtering!"


def who_likes_it(list_of_likes):
    if len(list_of_likes) == 0:
        return "no one likes this"
    elif len(list_of_likes) == 1:
        return list_of_likes[0] + " likes this"
    elif len(list_of_likes) == 2:
        return list_of_likes[0] + " and " + list_of_likes[1] + " like this"
    elif len(list_of_likes) == 3:
        return list_of_likes[0] + ", " + list_of_likes[1] + " and " + list_of_likes[2] + " like this"
    elif len(list_of_likes) == 4:
        return list_of_likes[0] + ", " + list_of_likes[1] + " and 2 others like this"


assert who_likes_it([]) == "no one likes this", "Wrong like count!"
assert who_likes_it(["Ryszard"]) == "Ryszard likes this", "Wrong like count!"
assert who_likes_it(["Marcin", "Michal"]) == "Marcin and Michal like this", "Wrong like count!"
assert who_likes_it(["Edyta", "Igor", "Kamil"]) == "Edyta, Igor and Kamil like this", "Wrong like count!"
assert who_likes_it(["Michal", "Maciej", "Bartosz", "Przemek"]) == "Michal, Maciej and 2 others like this", "Wrong like count!"
