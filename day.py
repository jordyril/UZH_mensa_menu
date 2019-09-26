from mensa import Mensa
from util import underline


class Day(object):
    def __init__(self, day, urls):
        self.URLS = urls
        self.day = day.lower()
        self.mensas = []
        self.__retrieve_menus()

    def __str__(self):
        return self.day.capitalize()

    def __repr__(self):
        return self.day.capitalize()

    def __retrieve_menus(self):
        for url in self.URLS:
            self.mensas.append(Mensa(url, self.day))

    @property
    def summary(self):
        summary = ""
        for mensa in self.mensas:
            summary += f"{underline(mensa.mensa.upper())}"
            summary += mensa.summary
        return summary

    # def optimal(self, value, max_min):
    #     mensa_optimals = []


# test = Day("montag", URLS)

# test
# test.mensas[0].menu.meals[0].values["energy"]

# print(test.summary)

# test.URLS

# x = [111, 1234.3, 4.0]
# import numpy as numpy

# n
# max(x)

# import operator

# index, value = max(enumerate(x), key=operator.itemgetter(1))

# max(x)


# List.index(max(x))
