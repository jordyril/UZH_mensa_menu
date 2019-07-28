import os
from bs4 import BeautifulSoup

import requests

DIRECTORY = f"D:/OneDrive - bf.uzh.ch/Code/Python/UZH_mensa"
os.chdir(DIRECTORY)
from menu_classes import Menu, Dish


class Mensa(object):
    def __init__(self, url, day):
        self._url = url
        self.day = day
        self.url = self._url.format(self.day.lower())

        self.__retrieve_webpage()
        self.__retrieve_mensa()
        self.__retrieve_status()
        self.__retrieve_menu()

    def __retrieve_webpage(self):
        r = requests.get(self.url)
        self._webpage = BeautifulSoup(r.text, "lxml")

    def __retrieve_status(self):
        soup = self._webpage

        table = soup.find("table")

        if table is not None:
            self.status, self.__open = "OPEN", True
            self.menu = Menu()
        else:
            self.status, self.__open = "CLOSED", False
            self.menu = None

    def __retrieve_mensa(self):
        soup = self._webpage
        t = soup.find("ul", role="navigation", id="thirdlevel")
        a = t.find_all("a", class_="active")
        self.mensa = a[-1].text

    def __retrieve_menu(self):
        if self.__open:
            soup = self._webpage
            body = soup.find("div", class_="newslist-description")

            self.menu.add_dishes(body)

    def summary(self):
        if self.__open:
            summary = ""

            for dish in self.menu.dishes:
                summary += dish.summary
                summary += "\n \n"

        else:
            summary = f"{self.mensa} is {self.status.lower()}"
        return summary
