from bs4 import BeautifulSoup
import requests
import numpy as np

from menu import Menu


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

        table = soup.find(
            "table"
        )  # if closed, first table is not food, but Umweltbelastung
        if not table:
            self._close_mensa()
            return None

        if "Ausgewogenheit" not in table.text:
            self._open_mensa()
        else:
            self._close_mensa()

    def __retrieve_mensa(self):
        soup = self._webpage
        t = soup.find("ul", role="navigation", id="thirdlevel")
        a = t.find_all("a", class_="active")
        self.mensa = a[-1].text

    def __retrieve_menu(self):
        if self.__open:
            soup = self._webpage
            body = soup.find("div", class_="newslist-description")
            self.menu.add_meals(body)

    def _close_mensa(self):
        self.status, self.__open = "CLOSED", False
        self.menu = None

    def _open_mensa(self):
        self.status, self.__open = "OPEN", True
        self.menu = Menu()

    @property
    def summary(self):
        if self.__open:
            summary = ""

            for meal in self.menu.meals:
                summary += meal.summary
                summary += "\n \n"

        else:
            summary = f"{self.mensa} is {self.status.lower()}"
        summary += "\n \n"
        return summary

    def max(self, value):
        values = [x.values[value] for x in self.menu.meals]
        idx = np.argmax(values)
        return self.menu.meals[idx]

    def min(self, value):
        values = [x.values[value] for x in self.menu.meals]
        idx = np.argmin(values)
        return self.menu.meals[idx]
