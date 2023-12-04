from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"


""" Write your functions here. """


def shortest_names(countries):
    res = min(len(ele) for ele in countries)
    my_list = []
    for country in countries:
        if len(country) == res:
            my_list.append(country)
    return my_list


def get_max_str(lst):
    return max(lst, key=len)


def most_vowels(items):
    def myFunc(e):
        return len(e)
    my_list = []
    for item in items:
        if 'a' in item and 'e' in item and 'i' in item and 'o' in item and 'u' in item:
            my_list.append(item)
            my_list.sort(reverse=True | False, key=myFunc)
            my_list
    return my_list[:3]


# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    countries = get_countries()

    """ Write the calls to your functions here. """

print('outcome short countries', shortest_names(countries))
print('countries with more vowels', most_vowels(countries))
