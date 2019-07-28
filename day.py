from menu_classes import Menu
from mensa_class import Mensa
from general import URLS


class Day(object):
    def __init__(self, day):
        self.URLS = URLS
        self.day = day
        self.mensas = []
        self.__retrieve_menus()

    def __str__(self):
        return self.day.capitalize()

    def __repr__(self):
        return self.day.capitalize()

    def __retrieve_menus(self):
        for url in self.URLS:
            self.mensas.append(Mensa(url, self.day))

    def summary(self):
        summary = ""
        for mensa in self.mensas:
            summary += f"{mensa.mensa.upper()} \n"


print("aaau\u0332zzz")


def underline(text):
    n = len(text)
    text_u = "{:s}\n{:s}\n".format(text, n * "-")

    return text_u


print(underline("test"))

test = Day("montag")

test.retrieve_menus()

print(test.mensas[0].summary())

test.URLS

